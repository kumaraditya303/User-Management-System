"""
The flask application package.
"""

from flask import *
from flask_sqlalchemy import *
from flask_migrate import *
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Data_Collector import views 
