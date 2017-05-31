"""
config.py

configure parameters for RumahNumeroUno Webapp
1. secret key for form
2. email
"""

import os

# parent class Config
class Config:
    # secret_key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # email: subject settings
    RNO_MAIL_SUBJECT_PREFIX = '[Rumah Numero Uno]'
    RNO_MAIL_SENDER = 'Rumah Numero Uno Admin <rumah.numero.uno@gmail.com>'
    RNO_ADMIN = os.environ.get('RNO_ADMIN')
    # SSL
    SSL_DISABLE = True

    @staticmethod
    def init_app(app):
        pass

# configuration for development, subclass of Config
class DevelopmentConfig(Config):
    DEBUG = True


# additional config for Heroku deployment
class HerokuConfig(Config):
    SSL_DISABLE=bool(os.environ.get('SSL_DISABLE'))


# dict mapping
config = {
    'development': DevelopmentConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
