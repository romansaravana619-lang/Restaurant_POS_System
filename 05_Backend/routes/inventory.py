"""Inventory Routes for Saru POS v1.0.

This module defines the Flask blueprint and routes for managing inventory
operations, including creating, retrieving, updating, and deleting
inventory items.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role

from services.inventory_service import (
    add_inventory_item,
    get_all_inventory_items,
    get_inventory_item_by_id,
    update_inventory_item,
    delete_inventory_item
)


inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/inventory-items", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_inventory_item():
    """Creates a new inventory item."""

    data = request.get_json(silent=True) or {}

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    inventory_id = data.get("inventory_id")
    supplier_id = data.get("supplier_id")
    item_name = data.get("item_name")
    unit = data.get("unit")
    quantity = data.get("quantity")
    unit_cost = data.get("unit_cost")
    reorder_level = data.get("reorder_level")
    status = data.get("status")

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
            "message": (
                "All fields (inventory_id, supplier_id, item_name, unit, "
                "quantity, unit_cost, reorder_level, status) are required."
            )
        }), 400

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

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@inventory_bp.route("/inventory-items", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_inventory_items():
    """Retrieves all inventory items."""

    result = get_all_inventory_items()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@inventory_bp.route("/inventory-items/<inventory_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_inventory_item(inventory_id):
    """Retrieves a specific inventory item by its ID."""

    result = get_inventory_item_by_id(inventory_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@inventory_bp.route("/inventory-items/<inventory_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_inventory_item_route(inventory_id):
    """Updates an existing inventory item by its ID."""

    data = request.get_json(silent=True)

    if data is None:
        return (
            jsonify({
                "success": False,
                "message": "Request body must be valid JSON.",
            }),
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
            jsonify({
                "success": False,
                "message": (
                    "All fields (supplier_id, item_name, unit, quantity, "
                    "unit_cost, reorder_level, status) are required."
                ),
            }),
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
@require_auth
@require_role("Admin", "Manager")
def delete_inventory_item_route(inventory_id):
    """Deletes an inventory item by its ID."""

    result = delete_inventory_item(inventory_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404