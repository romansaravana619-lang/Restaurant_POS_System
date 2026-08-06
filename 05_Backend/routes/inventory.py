"""Inventory Routes for Saru POS v1.0.

This module defines the Flask blueprint and routes for managing inventory
operations, including creating, retrieving, updating, and deleting
inventory items.
"""

from flask import Blueprint, request, jsonify
from services.inventory_service import (
    add_inventory_item,
    get_all_inventory_items,
    get_inventory_item_by_id,
    update_inventory_item,
    delete_inventory_item
)

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory-items", methods=["POST"])
def create_inventory_item():
    """Creates a new inventory item.

    Reads inventory item details from the request body, validates the input,
    and creates a new inventory record.

    Returns:
        tuple: JSON response and corresponding HTTP status code.
    """
    data = request.get_json(silent=True) or {}

    # Validate request body
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    # Extract fields
    inventory_id = data.get("inventory_id")
    supplier_id = data.get("supplier_id")
    item_name = data.get("item_name")
    unit = data.get("unit")
    quantity = data.get("quantity")
    unit_cost = data.get("unit_cost")
    reorder_level = data.get("reorder_level")
    status = data.get("status")

    # Validate required fields
    if not all([
        inventory_id,
        supplier_id,
        item_name,
        unit,
        quantity is not None,
        unit_cost is not None,
        reorder_level is not None,
        status
    ]):
        return jsonify({
            "success": False,
            "message": "All fields (inventory_id, supplier_id, item_name, unit, quantity, unit_cost, reorder_level, status) are required."
        }), 400

    # Call service layer
    result = add_inventory_item(
        inventory_id,
        supplier_id,
        item_name,
        unit,
        quantity,
        unit_cost,
        reorder_level,
        status
    )

    # Return response
    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400

@inventory_bp.route("/inventory-items", methods=["GET"])
def get_inventory_items():
    """Retrieves all inventory items.

    Delegates fetching to the service layer and returns a list of inventory
    items or an error response based on the operation's success.

    Returns:
        tuple: A tuple containing the JSON response dictionary and the HTTP status
            code (200 for success, 404 if not found or failed).
    """
    result = get_all_inventory_items()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@inventory_bp.route("/inventory-items/<inventory_id>", methods=["GET"])
def get_inventory_item(inventory_id):
    """Retrieves a specific inventory item by its ID.

    Args:
        inventory_id (str): The unique identifier of the inventory item.

    Returns:
        tuple: A tuple containing the JSON response dictionary and the HTTP status
            code (200 for success, 404 if not found or failed).
    """
    result = get_inventory_item_by_id(inventory_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@inventory_bp.route("/inventory-items/<inventory_id>", methods=["PUT"])
def update_inventory_item_route(inventory_id):
    """Updates an existing inventory item by its ID.

    Validates the request payload to ensure all required inventory fields are present,
    then updates the corresponding inventory record.

    Args:
        inventory_id (str): The unique identifier of the inventory item to update.

    Returns:
        tuple: A tuple containing the JSON response dictionary and the HTTP status
            code (200 for success, 400 for bad request/validation failure, 404 if not found).
    """
    data = request.get_json(silent=True)

    if data is None:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "Request body must be valid JSON.",
                }
            ),
            400,
        )

    required_fields = [
        "supplier_id",
        "item_name",
        "unit",
        "quantity",
        "unit_cost",
        "reorder_level",
        "status",
    ]

    if not all(field in data for field in required_fields):
        return (
            jsonify(
                {
                    "success": False,
                    "message": (
                        "All fields (supplier_id, item_name, unit, quantity, unit_cost,"
                        " reorder_level, status) are required."
                    ),
                }
            ),
            400,
        )

    result = update_inventory_item(
        inventory_id,
        data.get("supplier_id"),
        data.get("item_name"),
        data.get("unit"),
        data.get("quantity"),
        data.get("unit_cost"),
        data.get("reorder_level"),
        data.get("status"),
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@inventory_bp.route("/inventory-items/<inventory_id>", methods=["DELETE"])
def delete_inventory_item_route(inventory_id):
    """Deletes an inventory item by its ID.

    Args:
        inventory_id (str): The unique identifier of the inventory item to delete.

    Returns:
        tuple: A tuple containing the JSON response dictionary and the HTTP status
            code (200 for success, 404 if not found or deletion failed).
    """
    result = delete_inventory_item(inventory_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404