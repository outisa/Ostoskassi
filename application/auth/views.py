from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from passlib.hash import pbkdf2_sha256

from application.category.models import Category
from application.product.models import Product
from application.shoppinglist.models import Shoppinglist
from application.shoppinglistProduct.models import Shoppinglistproduct
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, CreateForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    hash = user.password
    check_password = pbkdf2_sha256.verify(form.password.data, hash)
    if not user or not check_password:
        return render_template("auth/loginform.html", form = form,
                                            error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout", methods = ["POST", "GET"])
def auth_logout():
    logout_user()
    return redirect(url_for("index2"))

@app.route("/auth/newAccount", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/newAccount.html",  form = CreateForm())
    form = CreateForm(request.form)
    if not form.validate():
        return render_template("auth/newAccount.html", form = form)

    name = form.username.data
    user = User.query.filter_by(username=name).first()
    if user:
        return render_template("auth/newAccount.html", form = form, 
                                                 error = "Username already exists, choose another one")
    hash = pbkdf2_sha256.hash(form.password.data)
    new_user = User(form.username.data, hash)

    db.session().add(new_user)
    db.session().commit()

    login_user(new_user)
    return redirect(url_for("index", message = "hello"))

@app.route("/auth/areYouSure/<user_id>", methods = ["GET","POST"])
@login_required
def auth_are_you_sure(user_id):
    return render_template("auth/areYouSure.html", user_id=user_id )

@app.route("/auth/delete/<user_id>", methods = ["POST", "GET"])
@login_required
def auth_delete(user_id):
    t =  User.query.get(user_id)
    for p in db.session().query(Product).filter_by(account_id=user_id):
        onList =  db.session.query(Shoppinglistproduct).filter_by(product_id=p.id).all()
        for listed in onList:
            db.session().delete(listed)
        db.session().delete(p)
    for c in db.session().query(Category).filter_by(account_id=user_id):
        db.session().delete(c)
    for s in db.session().query(Shoppinglist).filter_by(account_id=user_id):
        db.session().delete(s)
    db.session().delete(t)
    db.session().commit()


    return redirect(url_for("index3"))
