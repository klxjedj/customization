"""
The flask application package.
"""
from flask_bootstrap import Bootstrap
from flask import Flask
app = Flask(__name__)
Bootstrap(app)
import FlaskWebProject1.views

