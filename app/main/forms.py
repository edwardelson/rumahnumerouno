"""
forms.py

create wtforms
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, Regexp

# inquiry form at /index
class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    content = TextAreaField('Content')
    submit = SubmitField('Submit')


# Login form at /admin
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


# Form for LSTM
class LSTMForm(FlaskForm):
    seed = StringField('Topic', validators=[Required(), Length(1, 50), Regexp('^[a-zA-Z][a-zA-Z]*$')])
    submit = SubmitField('Enlighten Me')
