from flask import jsonify

from app.api_v1 import api


@api.route("/")
def homepage():
    homepage_data = {"mesaage": "Welcome to Homepage"}
    return jsonify(homepage_data)
