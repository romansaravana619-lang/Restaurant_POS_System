"""
User Management Routes Module

This module defines the Flask routes for user management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from services.user_service import (
    add_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)


user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["POST"])
def create_user():
    """Creates a new user.

    Reads user details from the request body, validates the input,
    and creates a new user record through the service layer.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
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
            "message": "All fields (user_id, employee_id, username, password, role, status) are required."
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
def get_users():
    """Retrieves all users.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_all_users()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@user_bp.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    """Retrieves a user by its ID.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_user_by_id(user_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@user_bp.route("/users/<user_id>", methods=["PUT"])
def update_user_route(user_id):
    """Updates an existing user.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
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
            "message": "All fields (employee_id, username, password, role, status) are required."
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
def delete_user_route(user_id):
    """Deletes a user by its ID.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = delete_user(user_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404