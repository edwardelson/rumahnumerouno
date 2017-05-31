"""
views.py

url routing to '/'
"""

from flask import render_template, session, redirect, url_for, abort, current_app, flash, request
from ..email import send_email #import email message from email.py
from . import main #import blueprint from main/
from datetime import datetime
from flask_moment import Moment

from .forms import InquiryForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = InquiryForm()

    # POST method
    if form.validate_on_submit():
        # send inquiry to email
        send_email(user=form.name.data, email=form.email.data, content=form.content.data)
        flash('Thank you for your inquiry!')
        return redirect(url_for('.index'))

    return render_template('index.html',
                            form=form,
                            time=datetime.utcnow(),
                            originTime=datetime(2017, 5, 1, 0, 0, 0))
