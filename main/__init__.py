'''
The flask application package.
'''

from flask import *
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import *


app = Flask(__name__)
app.config.from_object('config.ProductionConfig')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import main.views