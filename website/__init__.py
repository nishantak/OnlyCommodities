from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.secret_key ='t3am.t4r|k3y'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
