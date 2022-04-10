import os

from flask import Flask
from flask_mail import Mail

def init_app():
    app = Flask(__name__)
    return app