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

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()

            # If somebody manages bypass login with this user id created because of adding default categories.
            if current_user.get_id == 0:
                return login_manager.unauthorized()

            unauthorized = False

            if role != "ANY":
                unauthorized = True

                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()

            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# load application content
from application import views

from application.category import models
from application.category import views

from application.shoppinglist import models
from application.shoppinglist import views

from application.product import models
from application.product import views

from application.shoppinglistProduct import models

from application.auth import models
from application.auth import views

# login functionality part two and adding default data in the category
from application.auth.models import User

from application.category.models import Category
# User '0' must be added, so that postreSQL can add default data to the category,
# because otherwise adding categories with account_id 0 would violate foreign key rules ('0 does not exists in table account').
# However, it is not the way I would prefer to have this done.
event.listen(User.__table__, 'after_create', DDL(""" INSERT INTO account (id) VALUES (0) """))
event.listen(Category.__table__, 'after_create',
            DDL(""" INSERT INTO category (category, account_id) VALUES ('Clothes', 0), ('Shoes', 0), ('Vegetables', 0),
                  ('Prepared food', 0), ('Bread', 0), ('Fruits', 0), ('Other', 0), ('Toiletries', 0), ('Cleaning', 0), ('Soft Drinks', 0), ('Snacks', 0) """))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# database creation
try:
    db.create_all()
except:
    pass
