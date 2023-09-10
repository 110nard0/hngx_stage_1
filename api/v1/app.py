#!/usr/bin/env pytuhon3
"""HNGx Stage 1 API module"""

from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/')
def hello_world():
    return 'Hello from HNGX!'


@app.errorhandler(404)
def not_found(error) -> str:
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404
