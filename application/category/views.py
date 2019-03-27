from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.category.models import Category
from application.category.forms import CategoryForm

@app.route("/category", methods=["GET"])
def category_index():
    return render_template("category/listCategories.html", shoppingBag = Category.query.all())

@app.route("/category/newCategory/")
@login_required
def category_form():
    return render_template("category/newCategory.html", form = CategoryForm())

@app.route("/category/delete/<categoryId>", methods=["POST"])
@login_required
def category_delete(categoryId):
    t = Category.query.get(categoryId)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("category_index"))

@app.route("/category/<categoryId>/", methods=["POST", "GET"])
@login_required
def category_update(categoryId):
    uusi = request.form.get("newcategory")
    t = Category.query.get(categoryId)
    t.category = uusi
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

