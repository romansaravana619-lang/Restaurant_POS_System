"""
Routes for managing categories in the Saru POS v1.0 application.

This module sets up the Flask Blueprint and imports the required
service functions for category management endpoints.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role

from utils.validation import is_non_empty_string

from services.category_service import (
    add_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category,
)


category_bp = Blueprint("category", __name__)


@category_bp.route("/categories", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_category():
    """Creates a new category."""

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

    category_id = data.get("category_id")
    category_name = data.get("category_name")
    description = data.get("description")
    status = data.get("status")

    if not all([
        is_non_empty_string(category_id),
        is_non_empty_string(category_name),
        is_non_empty_string(description),
        is_non_empty_string(status)
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (category_id, category_name, "
                "description, status) are required and must be valid strings."
            )
        }), 400

    result = add_category(
        category_id,
        category_name,
        description,
        status
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@category_bp.route("/categories", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_categories():
    """Retrieves all categories."""

    result = get_all_categories()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@category_bp.route("/categories/<category_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_category(category_id):
    """Retrieves a specific category by its ID."""

    result = get_category_by_id(category_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@category_bp.route("/categories/<category_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_category_route(category_id):
    """Updates an existing category."""

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

    category_name = data.get("category_name")
    description = data.get("description")
    status = data.get("status")

    if not all([
        is_non_empty_string(category_name),
        is_non_empty_string(description),
        is_non_empty_string(status)
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (category_name, description, "
                "status) are required and must be valid strings."
            )
        }), 400

    result = update_category(
        category_id=category_id,
        category_name=category_name,
        description=description,
        status=status
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@category_bp.route("/categories/<category_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_category_route(category_id):
    """Deletes a specific category by its ID."""

    result = delete_category(category_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404
       