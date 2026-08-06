"""
auth.py

Authentication routes for Saru POS v1.0.
Defines the /login endpoint using a Flask Blueprint.
"""

from flask import Blueprint, request, jsonify
from services.auth_service import verify_user

# Create authentication blueprint
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    """Authenticate a user using username and password."""
    # Parse JSON request body
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    password = data.get("password")

    # Validate required fields
    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Username and password are required."
        }), 400

    # Verify user credentials via the auth service
    result = verify_user(username, password)

    # Return appropriate HTTP status based on verification result
    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 401