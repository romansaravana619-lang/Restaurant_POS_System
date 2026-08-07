"""
Routes for managing categories in the Saru POS v1.0 application.

This module sets up the Flask Blueprint and imports the required
service functions for category management endpoints.
"""

from flask import Blueprint, request, jsonify

from services.category_service import (
    add_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category,
)

category_bp = Blueprint("category", __name__)

@category_bp.route("/categories", methods=["POST"])
def create_category():
    """Creates a new category.

    Reads category details from the request body, validates the input,
    and creates a new category record.

    Returns:
        tuple: A tuple containing the JSON response and HTTP status code.
    """
    data = request.get_json(silent=True) or {}

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    category_id = data.get("category_id")
    category_name = data.get("category_name")
    description = data.get("description")
    status = data.get("status")

    if not all([
        category_id,
        category_name,
        description,
        status
    ]):
        return jsonify({
            "success": False,
            "message": "All fields (category_id, category_name, description, status) are required."
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
def get_categories():
    """Retrieves all categories.

    Returns:
        tuple: A tuple containing the JSON response and HTTP status code.
    """
    result = get_all_categories()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@category_bp.route("/categories/<category_id>", methods=["GET"])
def get_category(category_id):
    """Retrieves a specific category by its ID.

    Args:
        category_id (str): The unique identifier of the category.

    Returns:
        tuple: A tuple containing the JSON response and HTTP status code.
    """
    result = get_category_by_id(category_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@category_bp.route("/categories/<category_id>", methods=["PUT"])
def update_category_route(category_id):
    """Updates an existing category.

    Expects a JSON payload containing the updated category details.

    Args:
        category_id (str): The unique identifier of the category.

    Returns:
        tuple: A tuple containing the JSON response and HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    category_name = data.get("category_name")
    description = data.get("description")
    status = data.get("status")

    if not all([
        category_name,
        description,
        status
    ]):
        return jsonify({
            "success": False,
            "message": "All fields (category_name, description, status) are required."
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
def delete_category_route(category_id):
    """Deletes a specific category by its ID.

    Args:
        category_id (str): The unique identifier of the category.

    Returns:
        tuple: A tuple containing the JSON response and HTTP status code.
    """
    result = delete_category(category_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

