"""
models.py

1. User database class
"""

from . import db, login_manager

# for database
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)

    # assign automatic role
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        # assign admin role if user's email is similar to RNO_ADMIN
        if self.email == current_app.config['RNO_ADMIN']:
            self.is_admin = True

    #==========
    # password
    #==========
    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_administrator(self):
        return self.is_admin

    #==========
    # insert Admin
    #==========
    @staticmethod
    def insert_admin():
        u = User(username='admin',
                 email=current_app.config['RNO_ADMIN'],
                 password=current_app.config['RNO_ADMIN_PASSWORD'])

        db.session.add(u)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


# Flask login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
