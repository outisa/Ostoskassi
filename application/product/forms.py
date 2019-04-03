from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,  DecimalField, validators, SelectField

from application.category.models import Category

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=2)])
    price = DecimalField("Price")
    category_id = SelectField("Category", [validators.DataRequired()], coerce=int)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(a.id, a.category) for a in Category.query.order_by(Category.category)]
    class Meta:
        csrf = False


class UpdateForm(FlaskForm):
    price = DecimalField("Price")

    class Meta:
        csrf = False
