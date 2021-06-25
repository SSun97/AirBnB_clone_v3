#!/usr/bin/python3
"""create a variable app, instance of Flask"""


import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def not_found(err):
    """page not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def close_storage(self):
    """Close the storage"""
    storage.close()


if __name__ == '__main__':
    hoho = os.getenv("HBNB_API_HOST", default="0.0.0.0")
    popo = os.getenv("HBNB_API_PORT", default=5000)
    app.run(host=hoho, port=popo, threaded=True, debug=True)
