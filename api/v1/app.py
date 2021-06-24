#!/usr/bin/python3
"""create a variable app, instance of Flask"""

from models import storage
from api.v1.views import app_views
from flask import Flask
app = Flask(__name__)
app.register_blueprint(app_views)
import os
# app.config.from_envvar('')


@app.teardown_appcontext
def close_storage(self):
    """Close the storage"""
    storage.close()

if __name__ == '__main__':
    hoho = os.getenv("HBNB_API_HOST", default = "0.0.0.0")
    popo = os.getenv("HBNB_API_PORT", default = 5000)
    app.run(host=hoho, port=popo, threaded=True, debug=True)