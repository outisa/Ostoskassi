from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    category = StringField("Category", [validators.Length(min=3), validators.Regexp(r'^[\w]+$')])

    class Meta:
        csrf = False
