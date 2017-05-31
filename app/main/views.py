"""
views.py

url routing to '/'
"""

from flask import render_template, session, redirect, url_for, abort, current_app, flash, request
from ..email import send_email #import email message from email.py
from . import main #import blueprint from main/
from datetime import datetime
from flask_moment import Moment

#from .forms import NameForm, EditProfileForm, EditProfileAdminForm, PostForm #import form class from forms.py

@main.route('/')
def index():
    return render_template('index.html',
                            time=datetime.utcnow(),
                            originTime=datetime(2017, 5, 1, 0, 0, 0))
