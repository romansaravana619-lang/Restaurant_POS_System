"""
Billing Routes Module

This module defines the Flask routes for billing management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string, is_number

from services.billing_service import (
    add_bill,
    get_all_bills,
    get_bill_by_id,
    update_bill,
    delete_bill,
)


billing_bp = Blueprint("billing", __name__)


@billing_bp.route("/bills", methods=["POST"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def create_bill():
    """Creates a new bill."""

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

    bill_id = data.get("bill_id")
    customer_id = data.get("customer_id")
    employee_id = data.get("employee_id")
    table_id = data.get("table_id")
    invoice_number = data.get("invoice_number")
    bill_date = data.get("bill_date")
    total_amount = data.get("total_amount")
    status = data.get("status")

    if not all([
        is_non_empty_string(bill_id),
        is_non_empty_string(customer_id),
        is_non_empty_string(employee_id),
        is_non_empty_string(table_id),
        is_non_empty_string(invoice_number),
        is_non_empty_string(bill_date),
        is_number(total_amount),
        is_non_empty_string(status),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (bill_id, customer_id, employee_id, table_id, "
                "invoice_number, bill_date, total_amount, status) "
                "are required and must have valid types."
            )
        }), 400

    result = add_bill(
        bill_id,
        customer_id,
        employee_id,
        table_id,
        invoice_number,
        bill_date,
        total_amount,
        status,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@billing_bp.route("/bills", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_bills():
    """Retrieves all bills."""

    result = get_all_bills()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@billing_bp.route("/bills/<bill_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_bill(bill_id):
    """Retrieves a bill by its ID."""

    result = get_bill_by_id(bill_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@billing_bp.route("/bills/<bill_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_bill_route(bill_id):
    """Updates an existing bill."""

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

    customer_id = data.get("customer_id")
    employee_id = data.get("employee_id")
    table_id = data.get("table_id")
    invoice_number = data.get("invoice_number")
    bill_date = data.get("bill_date")
    total_amount = data.get("total_amount")
    status = data.get("status")

    if not all([
        is_non_empty_string(customer_id),
        is_non_empty_string(employee_id),
        is_non_empty_string(table_id),
        is_non_empty_string(invoice_number),
        is_non_empty_string(bill_date),
        is_number(total_amount),
        is_non_empty_string(status),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (customer_id, employee_id, table_id, "
                "invoice_number, bill_date, total_amount, status) "
                "are required and must have valid types."
            )
        }), 400

    result = update_bill(
        bill_id=bill_id,
        customer_id=customer_id,
        employee_id=employee_id,
        table_id=table_id,
        invoice_number=invoice_number,
        bill_date=bill_date,
        total_amount=total_amount,
        status=status,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@billing_bp.route("/bills/<bill_id>", methods=["DELETE"])
@require_auth
@require_role("Admin", "Manager")
def delete_bill_route(bill_id):
    """Deletes a bill by its ID."""

    result = delete_bill(bill_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404