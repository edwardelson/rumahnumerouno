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
# db auto migration
from flask_migrate import Migrate, MigrateCommand
# initiate app/
from app import create_app, db
from app.models import User

# create Flask object
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# make shell context
def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


#for deployment
@manager.command
def deploy():
    """ Run deployment tasks """
    from flask_migrate import upgrade

    upgrade()

    User.insert_admin()

# run the server
if __name__ == '__main__':
    manager.run()
