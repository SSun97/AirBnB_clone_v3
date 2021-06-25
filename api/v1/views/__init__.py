#!/usr/bin/python3
"""Create Blueprint"""

from flask import Blueprint, abort, make_response


def get_all_cls(parent_cls, parent_cls_id, parent_getter):
    """GET /cls api route"""
    parent = storage.get(parent_cls, parent_cls_id)
    if not parent:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify([info.to_dict() for info in getattr(parent, parent_getter)])



def get(cls, cls_id):
    """GET /model api route"""
    obj = storage.get(cls, cls_id)
    if not obj:
        return make_response(jsonify({"error": "Not found"}), 404)

    return jsonify(obj.to_dict())


def delete(cls, cls_id):
    """DELETE /model api route"""
    obj = storage.get(cls, cls_id)
    if not obj:
        return make_response(jsonify({"error": "Not found"}), 404)

    storage.delete(obj)
    storage.save()
    return make_response(jsonify({}), 200)


def post(cls, parent_cls, parent_cls_id, required_data):
    """POST /model api route"""
    from models.engine.db_storage import classes
    if parent_cls:
        parent = storage.get(parent_cls, parent_cls_id)
        if not parent:
            return make_response(jsonify({"error": "Not found"}), 404)

    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, 'Not a JSON')

    for requirement in required_data:
        if requirement not in data:
            message = "Missing " + requirement
            abort(400, message)

    if "user_id" in required_data:
        if not storage.get("User", data.get("user_id")):
            return make_response(jsonify({"error": "Not found"}), 404)

    if parent_cls:
        data[parent_cls.lower() + '_id'] = parent_cls_id
    obj = classes[cls](**data)
    obj.save()
    return make_response(jsonify(obj.to_dict()), 201)


def put(cls, cls_id, ignored_data):
    """PUT /cls api route"""
    obj = storage.get(cls, cls_id)
    if not obj:
        return make_response(jsonify({"error": "Not found"}), 404)

    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key not in ignored_data:
            setattr(obj, key, value)
    obj.save()
    return make_response(jsonify(obj.to_dict()), 200)

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.amenities import *
from api.v1.views.places_reviews import *
