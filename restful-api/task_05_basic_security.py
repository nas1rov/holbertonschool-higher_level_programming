#!/usr/bin/python3
"""
Flask API with Basic and JWT Authentication, including Role-based access.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'  # Real işdə bunu gizli saxla!

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçilər bazası (yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Hissəsi ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün şifrəni yoxlayır"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Yalnız düzgün Basic Auth məlumatı olanlar üçün"""
    return "Basic Auth: Access Granted"

# --- JWT Authentication Hissəsi ---

@app.route('/login', methods=['POST'])
def login():
    """İstifadəçi girişi və JWT token verilməsi"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rol məlumatını tokenin içinə (identity) yerləşdiririk
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Düzgün JWT token tələb edən endpoint"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Yalnız 'admin' rolu olanlar üçün"""
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- JWT Xəta İdarəediciləri (Checker üçün vacibdir) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
