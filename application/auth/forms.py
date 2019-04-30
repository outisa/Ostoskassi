from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=5, max=50), validators.Regexp(r'^\w*$')])
    password = PasswordField("Password", [validators.Length(min=6, max=30),validators.Regexp(r'^\w*$')])
    class Meta:
       csrf = False

class CreateForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=5, max=50), validators.Regexp(r'^\w*$')])
    password = PasswordField("Password", [validators.Length(min=6, max=30),validators.Regexp(r'^\w*$'), validators.EqualTo("confirm", message="Passwords must match!")])
    confirm = PasswordField("Repeat Password")

    class Meta:
       csrf = False


