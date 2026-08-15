"""
Payment Routes Module

This module defines the Flask routes for payment management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth
from utils.validation import is_non_empty_string, is_number

from services.payment_service import (
    add_payment,
    get_all_payments,
    get_payment_by_id,
    update_payment,
    delete_payment,
)


payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/payments", methods=["POST"])
@require_auth
def create_payment():
    """Creates a new payment."""

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

    payment_id = data.get("payment_id")
    bill_id = data.get("bill_id")
    payment_method = data.get("payment_method")
    payment_status = data.get("payment_status")
    payment_date = data.get("payment_date")
    paid_amount = data.get("paid_amount")

    if not all([
        is_non_empty_string(payment_id),
        is_non_empty_string(bill_id),
        is_non_empty_string(payment_method),
        is_non_empty_string(payment_status),
        is_non_empty_string(payment_date),
        is_number(paid_amount),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (payment_id, bill_id, payment_method, "
                "payment_status, payment_date, paid_amount) are required "
                "and must have valid types."
            )
        }), 400

    result = add_payment(
        payment_id,
        bill_id,
        payment_method,
        payment_status,
        payment_date,
        paid_amount,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@payment_bp.route("/payments", methods=["GET"])
@require_auth
def get_payments():
    """Retrieves all payments."""

    result = get_all_payments()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@payment_bp.route("/payments/<payment_id>", methods=["GET"])
@require_auth
def get_payment(payment_id):
    """Retrieves a payment by its ID."""

    result = get_payment_by_id(payment_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@payment_bp.route("/payments/<payment_id>", methods=["PUT"])
@require_auth
def update_payment_route(payment_id):
    """Updates an existing payment."""

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
    payment_method = data.get("payment_method")
    payment_status = data.get("payment_status")
    payment_date = data.get("payment_date")
    paid_amount = data.get("paid_amount")

    if not all([
        is_non_empty_string(bill_id),
        is_non_empty_string(payment_method),
        is_non_empty_string(payment_status),
        is_non_empty_string(payment_date),
        is_number(paid_amount),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "All fields (bill_id, payment_method, payment_status, "
                "payment_date, paid_amount) are required "
                "and must have valid types."
            )
        }), 400

    result = update_payment(
        payment_id=payment_id,
        bill_id=bill_id,
        payment_method=payment_method,
        payment_status=payment_status,
        payment_date=payment_date,
        paid_amount=paid_amount,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@payment_bp.route("/payments/<payment_id>", methods=["DELETE"])
@require_auth
def delete_payment_route(payment_id):
    """Deletes a payment by its ID."""

    result = delete_payment(payment_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404