"""
routes/customer.py

Blueprint for customer-related API endpoints.
Handles HTTP request parsing, validation, and response formatting.
All business logic is delegated to the service layer.
"""

from flask import Blueprint, request, jsonify
from utils.auth_middleware import require_auth, require_role
from services.customer_service import (
    add_customer,
    get_all_customers,
    get_customer_by_id,
    update_customer,
    delete_customer
)

customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customers', methods=['POST'])
@require_auth
@require_role("Admin", "Manager", "Staff")
def create_customer():
    """
    Create a new customer.

    Request JSON Body:
        {
            "customer_id": "CUS001",
            "customer_name": "Saravana Kumar",
            "phone": "9876543210",
            "email": "saravana@gmail.com",
            "status": "Active"
        }

    Returns:
        JSON response with success status and message.
        HTTP 201 on success.
        HTTP 400 on validation failure or service failure.
    """
    data = request.get_json(silent=True) or {}

    # Validate that request body exists
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    # Extract fields from request
    customer_id = data.get('customer_id')
    customer_name = data.get('customer_name')
    phone = data.get('phone')
    email = data.get('email')
    status = data.get('status')

    # Validate that all required fields are present
    if not all([customer_id, customer_name, phone, email, status]):
        return jsonify({
            "success": False,
            "message": "All fields (customer_id, customer_name, phone, email, status) are required."
        }), 400

    # Call service layer to add the customer
    result = add_customer(customer_id, customer_name, phone, email, status)

    # Return appropriate HTTP status based on service result
    if result.get("success"):
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@customer_bp.route("/customers", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_customers():
    """
    Retrieve all registered customers.

    Returns:
        JSON response containing customer list or an error message.
    """
    result = get_all_customers()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@customer_bp.route("/customers/<customer_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_customer(customer_id):
    """
    Retrieve a single customer using customer_id.
    """

    result = get_customer_by_id(customer_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@customer_bp.route("/customers/<customer_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def update_customer_route(customer_id):
    """
    Update an existing customer.
    """

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    customer_name = data.get("customer_name")
    phone = data.get("phone")
    email = data.get("email")
    status = data.get("status")

    if not all([customer_name, phone, email, status]):
        return jsonify({
            "success": False,
            "message": "customer_name, phone, email and status are required."
        }), 400

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
    """
    Delete a customer using customer_id.
    """

    result = delete_customer(customer_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404