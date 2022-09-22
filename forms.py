from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField, DateField, TextAreaField

from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class SampleForm(FlaskForm):
    number = IntegerField("Number", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    date = DateField("Date", validators=[DataRequired()])
    text = TextAreaField("TextArea", validators=[DataRequired()])

    body = CKEditorField("Comment", validators=[DataRequired()])

    submit = SubmitField("Submit")
