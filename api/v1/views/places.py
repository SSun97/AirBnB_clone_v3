#!/usr/bin/python3
"""New view for place objects"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.place import Place


cls = "Place"
parent_cls = "City"


@app_views.route("/cities/<city_id>/places", strict_slashes=False,
                 methods=["GET"])
def get_all_places(city_id):
    """GET all places api route"""
    return get_all_cls(parent_cls, city_id, "places")


@app_views.route("/places/<place_id>", methods=["GET"])
def get_place(place_id):
    """GET /place api route"""
    return get(cls, place_id)


@app_views.route("/places/<place_id>", methods=["DELETE"])
def delete_place(place_id):
    """DELETE /place api route"""
    return delete(cls, place_id)


@app_views.route("/places", strict_slashes=False, methods=["POST"])
def post_place():
    """POST /place api route"""
    required_data = {"user_id", "name"}
    return post(cls, None, None, required_data)


@app_views.route("/places/<place_id>", methods=["PUT"])
def put_place(place_id):
    """PUT /place api route"""
    ignore_data = ["id", "user_id", "city_id", "created_at", "updated_at"]
    return put(cls, place_id, ignore_data)
