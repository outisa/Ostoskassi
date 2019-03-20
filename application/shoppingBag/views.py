from application import app, db
from flask import redirect, render_template, request, url_for
from application.shoppingBag.models import Category

@app.route("/shoppingBag", methods=["GET"])
def shoppingBag_index():
    return render_template("shoppingBag/listCategories.html", shoppingBag = Category.query.all())

@app.route("/shoppingBag/newCategory/")
def shoppingBag_form():
    return render_template("shoppingBag/newCategory.html")

@app.route("/shoppingBag/<categoryId>/", methods=["POST", "GET"])
def shoppingBag_update(categoryId):
    uusi = request.form.get("newcategory")
    t = Category.query.get(categoryId)
    t.category = uusi
    db.session().commit()

    return redirect(url_for("shoppingBag_index"))

@app.route("/shoppingBag/", methods=["POST"])
def shoppingBag_create():
    t = Category(request.form.get("category"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("shoppingBag_index"))

