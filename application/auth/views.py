from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from application.category.models import Category
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first() 
    if not user:
        return render_template("auth/loginform.html", form = form,
                                            error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index2"))

@app.route("/auth/newAccount", methods = ["GET", "POST"])
def auth_create():
    if request.method == "GET":
        return render_template("auth/newAccount.html",  form = LoginForm())
    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/newAccount.html", form = form)

    t = User(form.username.data, form.password.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("index2"))

@app.route("/auth/delete/<user_id>", methods = ["POST", "GET"])
@login_required
def auth_delete(user_id):
   user = User.query.get(user_id)
   db.session().delete(user)
   db.session().commit()


   return redirect(url_for("index3"))
