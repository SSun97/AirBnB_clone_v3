#!/usr/bin/python3
"""New view for place review objects"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.review import Review

cls = "Review"
parent_cls = "Place"


@app_views.route("/places/<place_id>/reviews", strict_slashes=False,
                 methods=["GET"])
def get_reviews(place_id):
    """GET /place/review api route"""
    return get_all_cls(parent_cls, place_id, "reviews")


@app_views.route("/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    """GET /review with ID api route"""
    return get(cls, review_id)


@app_views.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """DELETE /review with ID api route"""
    return delete(cls, review_id)


@app_views.route("/places/<place_id>/reviews", strict_slashes=False,
                 methods=["POST"])
def post_review(place_id):
    """POST /reviews with place ID api route"""
    required_data = {"text", "user_id"}
    return post(cls, parent_cls, place_id, required_data)


@app_views.route("/reviews/<review_id>", methods=["PUT"])
def put_review(review_id):
    """PUT /reviews with ID api route"""
    ignored_data = ["id", "created_at", "updated_at", "user_id", "place_id"]
    return put(cls, review_id, ignored_data)
