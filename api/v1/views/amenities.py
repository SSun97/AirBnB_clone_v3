#!/usr/bin/python3
"""Amenities related endpoints"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.amenity import Amenity

cls = "Amenity"


@app_views.route("/amenities", strict_slashes=False,
                 methods=["GET"], defaults={"amenity_id": None})
@app_views.route("/amenities/<amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    """GET /aminities api route"""
    if not amenity_id:
        list_all_objs = [val.to_dict() for val in storage.all(cls).values()]
        return jsonify(list_all_objs)

    return get(cls, amenity_id)


@app_views.route("/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    """DELETE /amenity api route"""
    return delete(cls, amenity_id)


@app_views.route("/amenities", strict_slashes=False, methods=["POST"])
def post_amenity():
    """POST /amenity api route"""
    required_data = {"name"}
    return post(cls, None, None, required_data)


@app_views.route("/amenities/<amenity_id>", methods=["PUT"])
def put_amenity(amenity_id):
    """PUT /amenity api route"""
    ignored_data = ["id", "created_at", "updated_at"]
    return put(cls, amenity_id, ignored_data)
