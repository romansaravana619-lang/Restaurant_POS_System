"""
Bill Item Routes Module

This module defines the Flask routes for bill item management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify
from utils.auth_middleware import require_auth

from services.bill_item_service import (
    add_bill_item,
    get_all_bill_items,
    get_bill_item_by_id,
    update_bill_item,
    delete_bill_item,
)

bill_item_bp = Blueprint("bill_item", __name__)


@bill_item_bp.route("/bill-items", methods=["POST"])
@require_auth
def create_bill_item():
    """Creates a new bill item.

    Reads bill item details from the request body, validates the input, and
    creates a new bill item record through the service layer.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    bill_item_id = data.get("bill_item_id")
    bill_id = data.get("bill_id")
    menu_item_id = data.get("menu_item_id")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")
    subtotal = data.get("subtotal")

    string_fields = [bill_item_id, bill_id, menu_item_id]

    if (
        not all(isinstance(field, str) and field.strip() for field in string_fields)
        or quantity is None
        or quantity == ""
        or unit_price is None
        or unit_price == ""
        or subtotal is None
        or subtotal == ""
    ):
        return jsonify({
            "success": False,
            "message": "All fields (bill_item_id, bill_id, menu_item_id, quantity, unit_price, subtotal) are required."
        }), 400

    result = add_bill_item(
        bill_item_id,
        bill_id,
        menu_item_id,
        quantity,
        unit_price,
        subtotal,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@bill_item_bp.route("/bill-items", methods=["GET"])
@require_auth
def get_bill_items():
    """Retrieves all bill items.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_all_bill_items()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@bill_item_bp.route("/bill-items/<bill_item_id>", methods=["GET"])
@require_auth
def get_bill_item(bill_item_id):
    """Retrieves a bill item by its ID.

    Args:
        bill_item_id (str): The unique identifier for the bill item.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_bill_item_by_id(bill_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@bill_item_bp.route("/bill-items/<bill_item_id>", methods=["PUT"])
@require_auth
def update_bill_item_route(bill_item_id):
    """Updates an existing bill item.

    Args:
        bill_item_id (str): The unique identifier for the bill item.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    bill_id = data.get("bill_id")
    menu_item_id = data.get("menu_item_id")
    quantity = data.get("quantity")
    unit_price = data.get("unit_price")
    subtotal = data.get("subtotal")

    string_fields = [bill_id, menu_item_id]

    if (
        not all(isinstance(field, str) and field.strip() for field in string_fields)
        or quantity is None
        or quantity == ""
        or unit_price is None
        or unit_price == ""
        or subtotal is None
        or subtotal == ""
    ):
        return jsonify({
            "success": False,
            "message": "All fields (bill_id, menu_item_id, quantity, unit_price, subtotal) are required."
        }), 400

    result = update_bill_item(
        bill_item_id=bill_item_id,
        bill_id=bill_id,
        menu_item_id=menu_item_id,
        quantity=quantity,
        unit_price=unit_price,
        subtotal=subtotal,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@bill_item_bp.route("/bill-items/<bill_item_id>", methods=["DELETE"])
@require_auth
def delete_bill_item_route(bill_item_id):
    """Deletes a bill item by its ID.

    Args:
        bill_item_id (str): The unique identifier for the bill item.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = delete_bill_item(bill_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

