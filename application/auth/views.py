from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from passlib.hash import pbkdf2_sha256

from application.category.models import Category
from application.product.models import Product
from application.shoppinglist.models import Shoppinglist
from application.shoppinglistProduct.models import Shoppinglistproduct
from application import app, db, login_manager, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, CreateForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        flash('No such username or password!')
        return render_template("auth/loginform.html", form = form)

    hash = user.password
    check_password = pbkdf2_sha256.verify(form.password.data, hash)
    if not check_password:
        flash('No such username or password!')
        return render_template("auth/loginform.html", form = form)

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout", methods = ["POST", "GET"])
def auth_logout():
    logout_user()
    flash('You are successfully logged out!')
    return redirect(url_for("index"))

@app.route("/auth/newAccount", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/newAccount.html",  form = CreateForm())
    form = CreateForm(request.form)
    if not form.validate():
        flash('Use charackters A-Z, a-z and 0-9. For example "new_User09".')
        return render_template("auth/newAccount.html", form = form)

    name = form.username.data
    user = User.query.filter_by(username=name).first()
    if user:
        flash('Username exists already, try with another one')
        return render_template("auth/newAccount.html", form = form)

    hash = pbkdf2_sha256.hash(form.password.data)
    new_user = User(form.username.data, hash)

    db.session().add(new_user)
    db.session().commit()

    login_user(new_user)
    return redirect(url_for("index"))

# Checks, if user wants to delete his/her account
@app.route("/auth/areYouSure/<user_id>", methods = ["GET","POST"])
@login_required(role="ANY")
def auth_are_you_sure(user_id):
    user = User.query.get(user_id)
    # Avoids error, if user is NoneType
    if not user:
        return login_manager.unauthorized()
    if user.id != current_user.id:
        return login_manager.unauthorized()

    return render_template("auth/areYouSure.html", user_id=user_id )

@app.route("/auth/delete/<user_id>", methods = ["POST", "GET"])
@login_required(role="ANY")
def auth_delete(user_id):
    user = User.query.get(user_id)
    # Avoids error, if user is NoneType
    if not user:
        return login_manager.unauthorized()
    if user.id != current_user.id:
        return login_manager.unauthorized()

    # Following loop deletes user related data from product and shoppinglist tables.
    for product in db.session().query(Product).filter_by(account_id=user_id):
        onList =  db.session.query(Shoppinglistproduct).filter_by(product_id=product.id).all()
        for listed in onList:
            db.session().delete(listed)
        db.session().delete(product)
    # Following first loop deletes user related data from category table and second one from shoppinglist table.
    for category in db.session().query(Category).filter_by(account_id=user_id):
        db.session().delete(category)
    for shoppinglist in db.session().query(Shoppinglist).filter_by(account_id=user_id):
        db.session().delete(shoppinglist)
    # And finally user will be deleted.
    db.session().delete(user)
    db.session().commit()

    flash('Your account and all your data has been deleted!')
    return redirect(url_for("index"))
