#!/usr/bin/python3
"""file to create a route /status on
 the object app_views that returns
 a JSON content"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def json_status():
    """Return JSON file: status ok"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Return /status route"""
    dictcls = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    dictcls = {key: storage.count(val) for key, val in dictcls.items()}
    return jsonify(dictcls)
