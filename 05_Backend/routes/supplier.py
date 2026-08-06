"""
Saru POS v1.0 Flask Backend
Supplier Routes

This module sets up the Flask Blueprint for supplier management,
handling routing for supplier-related operations.
"""

from flask import Blueprint, request, jsonify
from services.supplier_service import (
    add_supplier,
    get_all_suppliers,
    get_supplier_by_id,
    update_supplier,
    delete_supplier
)

supplier_bp = Blueprint("supplier", __name__)

@supplier_bp.route("/suppliers", methods=["POST"])
def create_supplier():
    """Create a new supplier.

    Reads supplier details from the request body, validates the input,
    and creates a new supplier record.

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

    # Extract fields from request
    supplier_id = data.get("supplier_id")
    supplier_name = data.get("supplier_name")
    contact_person = data.get("contact_person")
    phone = data.get("phone")
    email = data.get("email")
    address = data.get("address")
    status = data.get("status")

    # Validate required fields
    if not all([
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    ]):
        return jsonify({
            "success": False,
            "message": "All fields (supplier_id, supplier_name, contact_person, phone, email, address, status) are required."
        }), 400

    # Call service layer
    result = add_supplier(
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    )

    # Return response
    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@supplier_bp.route("/suppliers", methods=["GET"])
def get_suppliers():
    """Retrieve all suppliers.

    Fetches all supplier records from the database ordered by supplier name.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    result = get_all_suppliers()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@supplier_bp.route("/suppliers/<supplier_id>", methods=["GET"])
def get_supplier(supplier_id):
    """Retrieve a single supplier by ID.

    Fetches the details of a specific supplier from the database using their
    unique supplier ID.

    Args:
        supplier_id (str): The unique identifier of the supplier.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    result = get_supplier_by_id(supplier_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@supplier_bp.route("/suppliers/<supplier_id>", methods=["PUT"])
def update_supplier_route(supplier_id):
    """Update an existing supplier.

    Reads updated supplier details from the request body, validates the input,
    and updates the supplier record.

    Args:
        supplier_id (str): The unique identifier of the supplier.

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

    # Extract fields from request
    supplier_name = data.get("supplier_name")
    contact_person = data.get("contact_person")
    phone = data.get("phone")
    email = data.get("email")
    address = data.get("address")
    status = data.get("status")

    # Validate required fields
    if not all([
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    ]):
        return jsonify({
            "success": False,
            "message": "All fields (supplier_name, contact_person, phone, email, address, status) are required."
        }), 400

    # Call service layer
    result = update_supplier(
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    )

    # Return response
    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@supplier_bp.route("/suppliers/<supplier_id>", methods=["DELETE"])
def delete_supplier_route(supplier_id):
    """Delete a supplier by ID.

    Removes the supplier record corresponding to the provided supplier ID
    from the database.

    Args:
        supplier_id (str): The unique identifier of the supplier to delete.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
    """
    result = delete_supplier(supplier_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404