from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args
from sqlalchemy import and_

from application import app, db
from application.category.models import Category
from application.product.models import Product
from application.product.forms import ProductForm, UpdateForm
from application.shoppinglistProduct.models import Shoppinglistproduct


@app.route("/product/updateProduct/<product_id>")
@login_required
def update_product_form(product_id):
    return render_template("product/updateProduct.html", form = UpdateForm(), product_id=product_id)

@app.route("/product/list", methods=["GET","POST"])
@login_required
def product_index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    products = Product.list_products_user(current_user.id)
    total = len(products)
    pagination_products = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template('product/listProducts.html', products=pagination_products,
                           page=page, per_page=per_page, pagination=pagination, form = ProductForm())


@app.route("/product/delete/<product_id>/", methods=["POST"])
@login_required
def product_delete(product_id):
    product =  Product.query.get(product_id)
    # Checks, if product is on shoppinglist table. If so, first deletes this row from shoppinglist table.
    product_on_list = db.session.query(Shoppinglistproduct).filter_by(product_id=product.id).all()
    for on_list in product_on_list:
        db.session().delete(on_list)
    db.session().delete(product)
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/update/<product_id>/", methods=["POST", "GET"])
@login_required
def product_update(product_id):
    form = UpdateForm(request.form)
    if not form.validate():
        return render_template("product/updateProduct.html", form = form, product_id=product_id)
    name = form.name.data
    product = Product.query.filter(and_(Product.name==name, Product.account_id==current_user.id, Product.id!=product_id)).first()
    if product:
        return render_template("product/updateProduct.html", form=form, product_id=product_id,
                             error = "Product exists already")
    update_product = Product.query.get(product_id)
    update_product.name = form.name.data
    update_product.price = form.price.data
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/", methods=["POST", "GET"])
@login_required
def product_create():
    form = ProductForm(request.form)
    if not form.validate():
        for error in form.name.errors:
            flash(error + ' Example of the name: "my Product_22"')
        for error in form.price.errors:
            flash(error)
        return redirect(url_for("product_index"))
    name = form.name.data
    product = Product.query.filter(and_(Product.name==name, Product.account_id==current_user.id)).first()
    if product:
        flash('Product exists already')
        return redirect(url_for("product_index"))
    new_product = Product(form.name.data, form.price.data)
    new_product.account_id = current_user.id
    new_product.category_id = form.category_id.data
    db.session().add(new_product)
    db.session().commit()

    return redirect(url_for("product_index"))
