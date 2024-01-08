#!/usr/bin/python3
"""
Create a Route `/status` on the object app_views.
"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    """
    Returns a JSON response for RESTful API health
    """
    response = {'status': 'OK'}
    return jsonify(response)

app = Flask(__name__)

@app.route('/api/v1/stats', methods=['GET'])
def stats():
    classes = ['User', 'Place', 'City', 'Amenity', 'State', 'Review']  # Add or remove class names as needed
    counts = {}
    for cls in classes:
        counts[cls] = storage.count(cls)
    return jsonify(counts)
