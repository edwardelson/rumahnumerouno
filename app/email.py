"""
email.py

configure email object
"""

from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


# send mail asynchronously
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# send mail function
def send_email(to, subject, template, **kwargs):
    # get current_app context
    app = current_app._get_current_object()

    # create Message object
    msg = Message(app.config['RNO_MAIL_SUBJECT_PREFIX'] + subject,
                    sender=app.config['RNO_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    # create Thread
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
