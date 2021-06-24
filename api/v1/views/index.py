#!/usr/bin/python3
"""file to create a route /status on the object app_views that returns a JSON content"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def json_status():
    """Return JSON file: status ok"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def json_stats():
    """Return JSON file: status of object counts"""
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User
    stats_dict = {}
    for clsk, clsv in storage.all().items():
        clsname = clsk.split('.')[0]
        stats_dict[clsname] = storage.count(clsname)
    return jsonify(stats_dict)
