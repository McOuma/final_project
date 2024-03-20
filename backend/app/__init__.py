from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
from app.api_v1.routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Development")
    db.init_app(app)
    app.register_blueprint(api)
    return app
