from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import IntegerField, validators, SelectField, StringField
from application.product.models import Product

class ListForm(FlaskForm):
    product_id = SelectField("Product", coerce=int)
    amount = IntegerField("Amount of products", [validators.NumberRange(min=1, max=100, message="Please give number between %(min)s and %(max)s")])

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.product_id.choices = [(a.id, a.name) for a in Product.query.filter_by(account_id=current_user.id)]

    class Meta:
        csrf = False

class NameForm(FlaskForm):
    name = StringField("Shoppinglist", [validators.Length(min=3, max=50), validators.Regexp('^\w+(\s\w+)*$')])

    class Meta:
        csrf = False
