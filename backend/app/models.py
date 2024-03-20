import datetime

from app import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email_address = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String(), unique=True, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now.utc)
