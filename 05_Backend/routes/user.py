"""
User Management Routes Module

This module defines the Flask routes for user management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role

from services.user_service import (
    add_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)


user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
@require_auth
@require_role("Admin")
def create_user():
    """Creates a new user."""

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    user_id = data.get("user_id")
    employee_id = data.get("employee_id")
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")
    status = data.get("status")

    required_string_fields = [
        user_id,
        employee_id,
        username,
        password,
        role,
        status,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": (
                "All fields (user_id, employee_id, username, "
                "password, role, status) are required."
            )
        }), 400

    result = add_user(
        user_id=user_id,
        employee_id=employee_id,
        username=username,
        password=password,
        role=role,
        status=status,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@user_bp.route("/users", methods=["GET"])
@require_auth
@require_role("Admin")
def get_users():
    """Retrieves all users."""

    result = get_all_users()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@user_bp.route("/users/<user_id>", methods=["GET"])
@require_auth
@require_role("Admin")
def get_user(user_id):
    """Retrieves a user by its ID."""

    result = get_user_by_id(user_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@user_bp.route("/users/<user_id>", methods=["PUT"])
@require_auth
@require_role("Admin")
def update_user_route(user_id):
    """Updates an existing user."""

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    employee_id = data.get("employee_id")
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")
    status = data.get("status")

    required_string_fields = [
        employee_id,
        username,
        password,
        role,
        status,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": (
                "All fields (employee_id, username, password, "
                "role, status) are required."
            )
        }), 400

    result = update_user(
        user_id=user_id,
        employee_id=employee_id,
        username=username,
        password=password,
        role=role,
        status=status,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@user_bp.route("/users/<user_id>", methods=["DELETE"])
@require_auth
@require_role("Admin")
def delete_user_route(user_id):
    """Deletes a user by its ID."""

    result = delete_user(user_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404