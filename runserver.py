'''
This script runs the main application using a development server.
'''
import logging
import os

from flask_sqlalchemy import *

from main import app, db
from main.models import User

__author__ = 'Kumar Aditya'
if os.path.exists('logs.log'):
    os.remove('logs.log')

if __name__ == '__main__':
    db.create_all()
    if User.query.filter_by(name=app.config['ADMIN_USERNAME'], password=app.config['ADMIN_PASSWORD'], role='admin') is None:
        user = User(name=app.config['ADMIN_USERNAME'],
                    password=app.config['ADMIN_PASSWORD'], role='admin')
        db.session.add(user)
        db.session.commit()
    logging.basicConfig(filename='logs.log',level=logging.DEBUG)
    app.run()
