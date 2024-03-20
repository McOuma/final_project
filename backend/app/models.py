import datetime

from flask import jsonify

from app import bcrypt, db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email_address = db.Column(db.String(), unique=True)
    password_hash = db.Column(db.String(), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email_address, password_hash, created_on):
        self.username = username
        self.email_address = email_address
        self.password_hash = password_hash
        self.created_on = created_on

    def __repr__(self):
        return "<User %r>" % self.username

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def generate_token(self):
        pass


class Caregiver(User):
    __tablename__ = "caregivers"
    caregiver_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), unique=True)
    last_name = db.Column(db.String(), unique=True)
    national_id = db.Column(db.Integer(), unique=True)
    phone_no = db.Column(db.Integer(), unique=True)
    location = db.Column(db.String(), unique=True)
    certification = db.Column(db.String(), unique=True)

    def __init__(self,username,email_address,password_hash,created_on,first_name,last_name,national_id,phone_no,location,certification):
        super().__init__(username, email_address, password_hash, created_on)
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone_no = phone_no
        self.location = location
        self.certification = certification

    def make_reviews(self):
        pass

    def request_payment(self):
        pass
