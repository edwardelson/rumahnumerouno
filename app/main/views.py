"""
views.py

url routing to '/', 'login'
"""

from flask import render_template, session, redirect, url_for, abort, current_app, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from ..email import send_email #import email message from email.py
from ..models import User
from . import main #import blueprint from main/
from datetime import datetime
from flask_moment import Moment

from .forms import InquiryForm, LoginForm, LSTMForm
from ..ai_app import lstm_generate

@main.route('/', methods=['GET', 'POST'])
def index():
    form = InquiryForm()

    # POST method
    if form.validate_on_submit():
        # send inquiry to email
        send_email(user=form.name.data, email=form.email.data, content=form.content.data)
        return redirect(url_for('.index'))

    return render_template('index.html',
                            form=form,
                            time=datetime.utcnow(),
                            originTime=datetime(2017, 5, 1, 0, 0, 0))


@main.route('/admin', methods=['GET', 'POST'])
def admin():
    form = LoginForm()

    # POST method
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # if user is admin, login
        if user.is_administrator() and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Invalid Email or Password, Sorry Dude!')
    return render_template('admin.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.admin'))



# for AI Application
@main.route('/ai', methods=['GET', 'POST'])
def ai():
    formLSTM = LSTMForm()

    # POST method
    if formLSTM.validate_on_submit():
        seed = formLSTM.seed.data

        # generate text
        teori = lstm_generate(seed)

        return render_template('ai.html', teori=teori, formLSTM=formLSTM)


    return render_template('ai.html', formLSTM=formLSTM, teori="")
