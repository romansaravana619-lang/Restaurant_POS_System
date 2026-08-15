"""
Restaurant Table Routes Module

This module initializes the Flask Blueprint for restaurant table management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string, is_number

from services.restaurant_table_service import (
    add_restaurant_table,
    get_all_restaurant_tables,
    get_restaurant_table_by_id,
    update_restaurant_table,
    delete_restaurant_table,
)


restaurant_table_bp = Blueprint("restaurant_table", __name__)


@restaurant_table_bp.route("/restaurant-tables", methods=["POST"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def create_restaurant_table():
    """Creates a new restaurant table."""

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body cannot be empty."
        }), 400

    table_id = data.get("table_id")
    table_number = data.get("table_number")
    capacity = data.get("capacity")
    status = data.get("status")

    if not all([
        is_non_empty_string(table_id),
        is_non_empty_string(table_number),
        is_number(capacity),
        is_non_empty_string(status),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (table_id, table_number, capacity, status) "
                "are required and must have valid types."
            )
        }), 400

    result = add_restaurant_table(
        table_id,
        table_number,
        capacity,
        status
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@restaurant_table_bp.route("/restaurant-tables", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_restaurant_tables():
    """Retrieves all restaurant tables."""

    result = get_all_restaurant_tables()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@restaurant_table_bp.route("/restaurant-tables/<table_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_restaurant_table(table_id):
    """Retrieves a specific restaurant table by its ID."""

    result = get_restaurant_table_by_id(table_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@restaurant_table_bp.route("/restaurant-tables/<table_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_restaurant_table_route(table_id):
    """Updates an existing restaurant table."""

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body cannot be empty."
        }), 400

    table_number = data.get("table_number")
    capacity = data.get("capacity")
    status = data.get("status")

    if not all([
        is_non_empty_string(table_number),
        is_number(capacity),
        is_non_empty_string(status),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (table_number, capacity, status) "
                "are required and must have valid types."
            )
        }), 400

    result = update_restaurant_table(
        table_id=table_id,
        table_number=table_number,
        capacity=capacity,
        status=status
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@restaurant_table_bp.route("/restaurant-tables/<table_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_restaurant_table_route(table_id):
    """Deletes an existing restaurant table by its ID."""

    result = delete_restaurant_table(table_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404