from flask_login import UserMixin
import datetime
from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model,UserMixin):
    __tablename__="users"
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email_address = db.Column(db.String(225), unique=True)
    password_hash = db.Column(db.String(125), nullable=False)
    created_on=db.Column(db.DateTime(), datatime=datetime.now.UTC)