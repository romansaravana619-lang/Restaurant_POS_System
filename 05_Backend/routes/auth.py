"""
auth.py

Authentication routes for Saru POS v1.0.
Defines the /login endpoint using a Flask Blueprint.
"""

from flask import Blueprint, request, jsonify

from services.auth_service import verify_user


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user using username and password.

    Returns:
        JSON response containing authentication result.
    """

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not username.strip():
        return jsonify({
            "success": False,
            "message": "Username is required."
        }), 400

    if not isinstance(password, str) or not password:
        return jsonify({
            "success": False,
            "message": "Password is required."
        }), 400

    result = verify_user(username, password)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 401