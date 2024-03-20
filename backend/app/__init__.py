from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()
from app.api_v1.routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    db.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(api)
    return app
