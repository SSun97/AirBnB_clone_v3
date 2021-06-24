#!/usr/bin/python3
"""New view for state objects"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.city import City


cls = "City"
parent_cls = "State"


@app_views.route("/states/<state_id>/cities", strict_slashes=False,
                 methods=["GET"])
def get_all_cities(state_id):
    """GET all cities api route"""
    return get_all_cls(parent_cls, state_id, "cities")


@app_views.route("/cities/<city_id>", methods=["GET"])
def get_city(city_id):
    """GET /cities api route"""
    return get(cls, city_id)


@app_views.route("/cities/<city_id>", methods=["DELETE"])
def delete_city(city_id):
    """DELETE /city api route"""
    return delete(cls, city_id)


@app_views.route("/states/<state_id>/cities",
                 strict_slashes=False, methods=["POST"])
def post_city(state_id):
    """POST /cities api route"""
    required_data = {"name"}
    return post(cls, parent_cls, state_id, required_data)


@app_views.route("/cities/<city_id>", methods=["PUT"])
def put_city(city_id):
    """PUT /cities api route"""
    ignore_data = ["id", "created_at", "updated_at"]
    return put(cls, city_id, ignore_data)
