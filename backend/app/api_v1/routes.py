from flask import jsonify

from app.api_v1 import api


@api.route('/')
def get_homepage():
    homepage_data = {"mesaage":"Were John"}
    return jsonify(homepage_data)