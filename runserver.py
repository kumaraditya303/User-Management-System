"""
This script runs the Data_Collector application using a development server.
"""
__author__='Kumar Aditya'
from Data_Collector import app
from Data_Collector import db 

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")
