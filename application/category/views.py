from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.category.models import Category
from application.category.forms import CategoryForm
from application.product.models import Product

@app.route("/category/list", methods=["GET", "POST"])
@login_required
def category_index():
    return render_template("category/listCategories.html", categories=Category.list_categories_for_user(current_user.id), form = CategoryForm())

@app.route("/category/newCategory/")
@login_required
def category_form():
    return render_template("category/newCategory.html", form = CategoryForm())

@app.route("/category/delete/<category_id>/", methods=["POST"])
@login_required
def category_delete(category_id):
    t =  Category.query.get(category_id)
    products=Product.list_category_ids_in_use(category_id)
    if not products:
        db.session().delete(t)
        db.session().commit()
        return redirect(url_for("category_index"))
    return render_template("category/listCategories.html", categories=Category.list_categories_for_user(current_user.id), form = CategoryForm(),
                                                error="Not able to delete! " + t.category +" is needed in one or more products.")

@app.route("/category/update/<category_id>/", methods=["POST", "GET"])
@login_required
def category_update(category_id):
    form = CategoryForm(request.form)
    if not form.validate():
        return render_template("category/listCategories.html", categories=Category.list_categories_for_user(current_user.id), form = form)
    newC = form.category.data
    t = Category.query.get(category_id)
    t.category = newC
    db.session().commit()

    return redirect(url_for("category_index"))

@app.route("/category/", methods=["POST"])
@login_required
def category_create():
    form = CategoryForm(request.form)
    if not form.validate():
        return render_template("category/newCategory.html", form = form)

    t = Category(form.category.data)
    t.account_id = current_user.id
 
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("category_index"))

