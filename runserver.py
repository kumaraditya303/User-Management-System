"""
This script runs the Data_Collector application using a development server.
"""
__author__='Kumar Aditya'
from os import environ
from Data_Collector import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
