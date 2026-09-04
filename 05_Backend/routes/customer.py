"""
routes/customer.py

Blueprint for customer-related API endpoints.
Handles HTTP request parsing, validation, and response formatting.
All business logic is delegated to the service layer.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string

from services.customer_service import (
    add_customer,
    get_all_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)


customer_bp = Blueprint("customer", __name__)


@customer_bp.route("/customers", methods=["POST"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def create_customer():
    """Creates a new customer."""

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

    customer_name = data.get("customer_name")
    phone = data.get("phone")
    email = data.get("email")
    status = data.get("status", "Active")
    table_id = data.get("table_id")

    # Customer name and phone are mandatory.
    # Email is optional.
    if not is_non_empty_string(customer_name):
        return jsonify({
            "success": False,
            "message": "Customer name is required and must be a valid string."
        }), 400

    if not is_non_empty_string(phone):
        return jsonify({
            "success": False,
            "message": "Customer phone is required and must be a valid string."
        }), 400

    # Email is optional.
    # If supplied, it must be a non-empty string.
    if email is not None and not is_non_empty_string(email):
        return jsonify({
            "success": False,
            "message": "Email must be a valid string when provided."
        }), 400

    # Status defaults to Active.
    if not is_non_empty_string(status):
        status = "Active"

    if table_id is not None and not is_non_empty_string(table_id):
        return jsonify({
            "success": False,
            "message": "Table ID must be a valid string when provided."
        }), 400

    # Customer ID is intentionally NOT accepted from the frontend.
    # The service layer will generate the next Customer ID automatically.
    result = add_customer(
        customer_name,
        phone,
        email,
        status,
        table_id
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@customer_bp.route("/customers", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_customers():
    """Retrieves all customers."""

    result = get_all_customers()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@customer_bp.route("/customers/<customer_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_customer(customer_id):
    """Retrieves a customer by ID."""

    result = get_customer_by_id(customer_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@customer_bp.route("/customers/<customer_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_customer_route(customer_id):
    """Updates an existing customer."""

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

    customer_name = data.get("customer_name")
    phone = data.get("phone")
    email = data.get("email")
    status = data.get("status")

    if not is_non_empty_string(customer_name) or not is_non_empty_string(phone):
        return jsonify({
            "success": False,
            "message": "Customer name and phone are required and must be valid strings."
        }), 400

    if email is not None and not is_non_empty_string(email):
        return jsonify({
            "success": False,
            "message": "Email must be a valid string when provided."
        }), 400

    if not is_non_empty_string(status):
        status = "Active"

    result = update_customer(
        customer_id,
        customer_name,
        phone,
        email,
        status
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@customer_bp.route("/customers/<customer_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_customer_route(customer_id):
    """Deletes a customer by ID."""

    result = delete_customer(customer_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404