#!/usr/bin/python3
"""
A simple Flask API with user management endpoints.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}


@app.route("/")
def home():
    """Root endpoint message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API"""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the status of the API"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary"""
    # Gələn məlumatın JSON olub-olmadığını yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    # Şərtləri yoxlayırıq: Username mütləqdir və unikal olmalıdır
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini lüğətə əlavə edirik
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
