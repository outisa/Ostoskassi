from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listen
from sqlalchemy import event, DDL

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shoppingBag.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
# login functionality part one
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# load application content
from application import views

from application.category import models
from application.category import views
from category.models import Category

#@event.listens_for(Category.__table__, 'after_create')
#def insert_initial_values(*args, **kwargs):
#    db.session().add(Category(category='Candys', account_id=0))
#    db.session().add(Category(category='Fruits', account_id=0))
#    db.session().add(Priority(category='Vegetables', account_id=0))
#    db.session().commit()
event.listen(Category.__table__, 'after_create',
            DDL(""" INSERT INTO category (category, account_id) VALUES ('Clothes', 0), ('Shoes', 0), ('Vegetables', 0), ('Prepared food', 0),
            ('Bread', 0), ('Fruits', 0), ('Other', 0), ('Toiletries', 0), ('Cleaning', 0), ('Soft Drinks', 0), ('Snacks', 0) """))

from application.shoppinglist import models
from application.shoppinglist import views

from application.product import models
from application.product import views

from application.shoppinglistProduct import models

from application.auth import models
from application.auth import views

# login functionality part two
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation
try:
    db.create_all()
except:
    pass
