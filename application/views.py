from flask import render_template
from application import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def index2():
    return render_template("index2.html")

@app.route("/delete")
def index3():
    return render_template("index3.html")
