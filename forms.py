from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired

from flask_ckeditor import CKEditorField


class SampleForm(FlaskForm):
    username = StringField("Your Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    date = DateField("Registered Date", validators=[DataRequired()])

    body = CKEditorField("This is CKEditor", validators=[DataRequired()])

    submit = SubmitField("Submit")
