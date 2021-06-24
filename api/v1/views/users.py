#!/usr/bin/python3
"""New view for user objects"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.user import User


cls = "User"


@app_views.route("/users", strict_slashes=False,
                 methods=["GET"], defaults={"user_id": None})
@app_views.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """GET /user api route"""
    if not user_id:
        lst_objs = [val.to_dict() for val in storage.all(cls).values()]
        return jsonify(lst_objs)

    return get(cls, user_id)


@app_views.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """DELETE /user api route"""
    return delete(cls, user_id)


@app_views.route("/users", strict_slashes=False, methods=["POST"])
def post_user():
    """POST /user api route"""
    required_data = {"email", "password"}
    return post(cls, None, None, required_data)


@app_views.route("/users/<user_id>", methods=["PUT"])
def put_user(user_id):
    """PUT /user api route"""
    ignore_data = ["id", "email", "created_at", "updated_at"]
    return put(cls, user_id, ignore_data)
