from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args

from sqlalchemy import and_

from application import app, db
from application.shoppinglist.models import Shoppinglist
from application.shoppinglist.forms import ListForm, NameForm
from application.product.models import Product
from application.shoppinglistProduct.models import Shoppinglistproduct

@app.route("/shoppinglist/list", methods=["GET","POST"])
@login_required
def shoppinglist_index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    shoppinglists=Shoppinglist.shoppinglists_for_current_user(current_user.id)
    total = len(shoppinglists)
    pagination_shoppinglists = shoppinglists[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("shoppinglist/listShoppinglist.html", lists=pagination_shoppinglists, page=page,
                           per_page=per_page, pagination=pagination, form = NameForm())

@app.route("/shoppinglist/show/<shoppinglist_id>", methods=["POST", "GET"])
@login_required
def shoppinglist_show(shoppinglist_id):
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    list = Shoppinglist.shoppinglist_show_contents(shoppinglist_id)
    total = len(list)
    pagination_list = list[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template("shoppinglist/showShoppinglist.html", contents=pagination_list, page=page,
                           per_page=per_page, pagination=pagination, form = ListForm(),
                           slist_id=shoppinglist_id, total=Shoppinglist.shoppinglist_total_price(shoppinglist_id))

@app.route("/shoppinglist/update/<shoppinglist_id>", methods=["POST", "GET"])
@login_required
def shoppinglist_update(shoppinglist_id):
    form = ListForm(request.form)
    if not form.validate():
        return render_template("shoppinglist/showShoppinglist.html", lists=Shoppinglist.shoppinglists_for_current_user(current_user.id),
                                             slist_id=shoppinglist_id, form = form, total=Shoppinglist.shoppinglist_total_price(shoppinglist_id))
    shoppinglist = Shoppinglist.query.get(shoppinglist_id)
    product = Product.query.get(form.product_id.data)
    on_list = db.session.query(Shoppinglistproduct).filter(and_(Shoppinglistproduct.shoppinglist_id==shoppinglist.id, Shoppinglistproduct.product_id==product.id)).first()
    if on_list:
        Shoppinglistproduct.update_product_total(form.amount.data, shoppinglist_id, product.id)
        return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))

    a = Shoppinglistproduct(form.amount.data)
    a.product_id = product.id
    a.shoppinglist_id = shoppinglist.id
    a.total_product = form.amount.data
    db.session().add(a)
    db.session.commit()
    return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))

# Removes chosen product from the shoppinglist. (Deletes a row with this product_id and shoppinglist_id combination from shoppinglistproduct)
@app.route("/shoppinglist/remove/<product_id>/<shoppinglist_id>", methods=["POST"])
@login_required
def shoppinglist_remove(product_id, shoppinglist_id):
    product_on_list = db.session.query(Shoppinglistproduct).filter(and_(Shoppinglistproduct.product_id==product_id, Shoppinglistproduct.shoppinglist_id==shoppinglist_id)).first()
    db.session().delete(product_on_list)
    db.session().commit()
    return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))


@app.route("/shoppinglist/delete/<shoppinglist_id>", methods=["POST"])
@login_required
def shoppinglist_delete(shoppinglist_id):
    t = Shoppinglist.query.get(shoppinglist_id)
    isOnList = db.session.query(Shoppinglistproduct).filter_by(shoppinglist_id=t.id).all()
    for isOn in isOnList:
        db.session().delete(isOn)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("shoppinglist_index"))

@app.route("/shoppinglist/create", methods=["POST","GET"])
@login_required
def shoppinglist_create():
    form = NameForm(request.form)
    if not form.validate():
        flash('Word must be 3-50 characters long. Example "New list_23".')
        return redirect(url_for("shoppinglist_index"))

    t = Shoppinglist(form.name.data)
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("shoppinglist_index"))

@app.route("/shoppinglist/", methods=["POST","GET"])
@login_required
def shoppinglist_costs_per_category():
    return render_template("shoppinglist/costsPerCategory.html", costs = Shoppinglistproduct.show_total_costs_per_category(current_user.id))
