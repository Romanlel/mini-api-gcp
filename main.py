from flask import Flask, request, jsonify
from datetime import datetime
from app.gcs_utils import read_file_from_gcs, write_file_to_gcs
from app.joke_utils import generate_joke

import os

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to the mini-API on GCP!"})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"server_time": datetime.utcnow().isoformat() + "Z"})

@app.route("/data", methods=["GET"])
def get_data():
    return read_file_from_gcs()

@app.route("/data", methods=["POST"])
def post_data():
    content = request.json
    return write_file_to_gcs(content)

@app.route("/joke", methods=["GET"])
def joke():
    return jsonify({"joke": generate_joke()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
