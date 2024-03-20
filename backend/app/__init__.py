from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.api_v1.routes import api

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(api, prefix="/api/")

    return app
