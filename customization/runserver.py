"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    HOST ='0.0.0.0'
    PORT=80
    app.run(HOST, PORT)
