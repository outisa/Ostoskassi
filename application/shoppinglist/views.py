from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.shoppinglist.models import Shoppinglist
from application.shoppinglist.forms import ListForm, NameForm
from application.product.models import Product
from application.shoppinglistProduct.models import Shoppinglistproduct

@app.route("/shoppinglist/list", methods=["GET","POST"])
@login_required
def shoppinglist_index():
    return render_template("shoppinglist/listShoppinglist.html", lists=Shoppinglist.shoppinglists_for_current_user(current_user.id))

@app.route("/shoppinglist/show/<shoppinglist_id>", methods=["POST", "GET"])
@login_required
def shoppinglist_show(shoppinglist_id):
    return render_template("shoppinglist/showShoppinglist.html", list=Shoppinglist.shoppinglist_show_contents(shoppinglist_id),
                                                                        slist_id=shoppinglist_id, form=ListForm(), total=Shoppinglist.shoppinglist_total_price(shoppinglist_id))

@app.route("/shoppinglist/createShoppinlist/")
@login_required
def shoppinglist_form():
    return render_template("shoppinglist/createShoppinglist.html", form = NameForm())

@app.route("/shoppinglist/update/<shoppinglist_id>", methods=["POST", "GET"])
@login_required
def shoppinglist_update(shoppinglist_id):
    form = ListForm(request.form)
    if not form.validate():
        return render_template("shoppinglist/showShoppinglist.html", lists=Shoppinglist.shoppinglists_for_current_user(current_user.id),
                                             slist_id=shoppinglist_id, form = form, total=Shoppinglist.shoppinglist_total_price(shoppinglist_id))
    shoppinglist = Shoppinglist.query.get(shoppinglist_id)
    product = Product.query.get(form.product_id.data)
    on_list = db.session.query(Shoppinglistproduct).filter_by(shoppinglist_id=shoppinglist_id).all()
    for product_on_list in on_list:
        if product_on_list.product_id == product.id:
            if form.amount.data == 0:
                db.session().delete(product_on_list)
                db.session().commit()
            else:
                Shoppinglistproduct.update_product_total(form.amount.data, shoppinglist_id, product.id)
            return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))
    if form.amount.data == 0:
        return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))

    a = Shoppinglistproduct(form.amount.data)
    a.product_id = product.id
    a.shoppinglist_id = shoppinglist.id
    a.total_product = form.amount.data
    db.session().add(a)
    db.session.commit()
    return redirect(url_for("shoppinglist_show", shoppinglist_id=shoppinglist_id))


@app.route("/shoppinglist/delete/<shoppinglist_id>", methods=["POST"])
@login_required
def shoppinglist_delete(shoppinglist_id):
    t = Shoppinglist.query.get(shoppinglist_id)
    isOnList = db.session().query(Shoppinglistproduct).filter_by(shoppinglist_id=t.id).first()
    if isOnList:
        db.session().delete(isOnList)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("shoppinglist_index"))

@app.route("/shoppinglist/create", methods=["POST","GET"])
@login_required
def shoppinglist_create():
    form = NameForm(request.form)
    if not form.validate():
        return render_template("shoppinglist/createShoppinglist.html", form = form)

    t = Shoppinglist(form.name.data)
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("shoppinglist_index"))
