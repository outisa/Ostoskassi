from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.product.models import Product
from application.product.forms import ProductForm, UpdateForm


@app.route("/product/newProduct/")
@login_required
def product_form():
    return render_template("product/newProduct.html", form = ProductForm())

@app.route("/product/list", methods=["GET","POST"])
@login_required
def product_index():
    return render_template("product/listProducts.html", products=Product.list_products_user(current_user.id), form = UpdateForm())

@app.route("/product/delete/<product_id>/", methods=["POST"])
@login_required
def product_delete(product_id):
    t =  Product.query.get(product_id)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/update/<product_id>/", methods=["POST", "GET"])
@login_required
def product_update(product_id):
    form = UpdateForm(request.form)
    if not form.validate():
        return render_template("product/listProducts.html", form = form)
    t = Product.query.get(product_id)
    t.price = form.price.data
    db.session().commit()
    return redirect(url_for("product_index"))

@app.route("/product/", methods=["POST"])
@login_required
def product_create():
    form =ProductForm(request.form)
    if not form.validate():
        return render_template("product/newProduct.html", form = form) 
    t = Product(form.name.data, form.price.data)
    t.account_id = current_user.id
    t.category_id = form.category_id.data
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("product_index"))
