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
def send_email(user, email, content, **kwargs):
    # get current_app context
    app = current_app._get_current_object()

    # create Message object
    msg = Message(app.config['RNO_MAIL_SUBJECT_PREFIX'] + " Inquiry From: " + user,
                    sender=app.config['RNO_MAIL_SENDER'], recipients=[app.config['RNO_ADMIN']])
    msg.body = render_template('mail/inquiry_template.txt', user=user, email=email, content=content, **kwargs)
    msg.html = render_template('mail/inquiry_template.html', user=user, email=email, content=content, **kwargs)

    # create Thread
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
