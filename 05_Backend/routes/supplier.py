"""
Saru POS v1.0 Flask Backend
Supplier Routes

This module sets up the Flask Blueprint for supplier management,
handling routing for supplier-related operations.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role

from services.supplier_service import (
    add_supplier,
    get_all_suppliers,
    get_supplier_by_id,
    update_supplier,
    delete_supplier
)


supplier_bp = Blueprint("supplier", __name__)


@supplier_bp.route("/suppliers", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_supplier():
    """Create a new supplier."""

    data = request.get_json(silent=True) or {}

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    supplier_id = data.get("supplier_id")
    supplier_name = data.get("supplier_name")
    contact_person = data.get("contact_person")
    phone = data.get("phone")
    email = data.get("email")
    address = data.get("address")
    status = data.get("status")

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
            "message": (
                "All fields (supplier_id, supplier_name, contact_person, "
                "phone, email, address, status) are required."
            )
        }), 400

    result = add_supplier(
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@supplier_bp.route("/suppliers", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_suppliers():
    """Retrieve all suppliers."""

    result = get_all_suppliers()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@supplier_bp.route("/suppliers/<supplier_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_supplier(supplier_id):
    """Retrieve a single supplier by ID."""

    result = get_supplier_by_id(supplier_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@supplier_bp.route("/suppliers/<supplier_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_supplier_route(supplier_id):
    """Update an existing supplier."""

    data = request.get_json(silent=True) or {}

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    supplier_name = data.get("supplier_name")
    contact_person = data.get("contact_person")
    phone = data.get("phone")
    email = data.get("email")
    address = data.get("address")
    status = data.get("status")

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
            "message": (
                "All fields (supplier_name, contact_person, phone, "
                "email, address, status) are required."
            )
        }), 400

    result = update_supplier(
        supplier_id,
        supplier_name,
        contact_person,
        phone,
        email,
        address,
        status
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 400

@supplier_bp.route("/suppliers/<supplier_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_supplier_route(supplier_id):
    """Delete a supplier by ID."""

    result = delete_supplier(supplier_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404