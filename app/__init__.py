"""
/app

configure app/ with config.py
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from config import config
from flask_login import LoginManager

# configure database
from flask_sqlalchemy import SQLAlchemy

# initialize objects
mail = Mail()
moment = Moment()
bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.admin'

# create application
def create_app(config_name):
    app = Flask(__name__)
    # run additional init_app from Config class
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # initialize objects with config.py
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    # database setup
    db.init_app(app)
    # login setup
    login_manager.init_app(app)

    # call Blueprint from main/
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
