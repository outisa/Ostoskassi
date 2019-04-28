from flask_wtf import FlaskForm
from flask_login import current_user
from sqlalchemy import or_
from wtforms import StringField, IntegerField,  DecimalField, validators, SelectField
from application.category.models import Category

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2, max=100), validators.Regexp(r'^[(\w+\s)*\w]+$')])
    price = DecimalField("Price", [validators.NumberRange(min=0.01, max=10000.00, message="Please give a number between %(min)s and %(max)s!")])

    category_id = SelectField("Category", coerce=int)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(a.id, a.category) for a in Category.query.filter(or_(Category.account_id==current_user.id, Category.account_id==0))]


    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2, max=150), validators.Regexp(r'^[(\w+\s)*\w]+$')])
    price = DecimalField("Price", [validators.NumberRange(min=0.01, max=10000.00, message="Please give a number between %(min)s and %(max)s!")])

    class Meta:
        csrf = False
