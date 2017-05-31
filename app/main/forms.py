"""
forms.py

create wtforms
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length, Email


class InquiryForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    content = TextAreaField('Content')
    submit = SubmitField('Submit')
