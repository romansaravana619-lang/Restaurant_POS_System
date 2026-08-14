"""
Menu Item Routes Module

This module initializes the Flask Blueprint for menu item management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string, is_number

from services.menu_item_service import (
    add_menu_item,
    get_all_menu_items,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item,
)


menu_item_bp = Blueprint("menu_item", __name__)


@menu_item_bp.route("/menu-items", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_menu_item():
    """Creates a new menu item."""

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

    menu_item_id = data.get("menu_item_id")
    category_id = data.get("category_id")
    item_name = data.get("item_name")
    price = data.get("price")
    description = data.get("description")
    availability = data.get("availability")

    if not all([
        is_non_empty_string(menu_item_id),
        is_non_empty_string(category_id),
        is_non_empty_string(item_name),
        is_number(price),
        is_non_empty_string(description),
        is_non_empty_string(availability),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (menu_item_id, category_id, item_name, "
                "price, description, availability) are required "
                "and must have valid types."
            )
        }), 400

    result = add_menu_item(
        menu_item_id,
        category_id,
        item_name,
        price,
        description,
        availability
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@menu_item_bp.route("/menu-items", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_menu_items():
    """Retrieves all menu items."""

    result = get_all_menu_items()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@menu_item_bp.route("/menu-items/<menu_item_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_menu_item(menu_item_id):
    """Retrieves a specific menu item by its ID."""

    result = get_menu_item_by_id(menu_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@menu_item_bp.route("/menu-items/<menu_item_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_menu_item_route(menu_item_id):
    """Updates an existing menu item."""

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
    item_name = data.get("item_name")
    price = data.get("price")
    description = data.get("description")
    availability = data.get("availability")

    if not all([
        is_non_empty_string(category_id),
        is_non_empty_string(item_name),
        is_number(price),
        is_non_empty_string(description),
        is_non_empty_string(availability),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (category_id, item_name, price, "
                "description, availability) are required "
                "and must have valid types."
            )
        }), 400

    result = update_menu_item(
        menu_item_id=menu_item_id,
        category_id=category_id,
        item_name=item_name,
        price=price,
        description=description,
        availability=availability
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@menu_item_bp.route("/menu-items/<menu_item_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_menu_item_route(menu_item_id):
    """Deletes an existing menu item."""

    result = delete_menu_item(menu_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404