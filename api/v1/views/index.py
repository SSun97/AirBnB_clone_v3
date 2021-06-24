#!/usr/bin/python3
"""file to create a route /status on
 the object app_views that returns
 a JSON content"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def json_status():
    """Return JSON file: status ok"""
    return jsonify({"status": "OK"})
