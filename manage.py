#!/usr/bin/env/ python

"""
manage.py

1. initiate app/
2. establish context
3. define testunit
4. run manager
"""

import os

from flask_script import Manager, Shell
# initiate app/
from app import create_app

# create Flask object
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

# make shell context
def make_shell_context():
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))

# run the server
if __name__ == '__main__':
    manager.run()
