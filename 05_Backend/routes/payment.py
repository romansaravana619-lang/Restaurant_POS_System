"""
Payment Routes Module

This module defines the Flask routes for payment management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from services.payment_service import (
    add_payment,
    get_all_payments,
    get_payment_by_id,
    update_payment,
    delete_payment,
)


payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/payments", methods=["POST"])
def create_payment():
    """Creates a new payment.

    Reads payment details from the request body, validates the input,
    and creates a new payment record through the service layer.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    payment_id = data.get("payment_id")
    bill_id = data.get("bill_id")
    payment_method = data.get("payment_method")
    payment_status = data.get("payment_status")
    payment_date = data.get("payment_date")
    paid_amount = data.get("paid_amount")

    string_fields = [
        payment_id,
        bill_id,
        payment_method,
        payment_status,
        payment_date,
    ]

    if (
        not all(
            isinstance(field, str) and field.strip()
            for field in string_fields
        )
        or paid_amount is None
        or paid_amount == ""
    ):
        return jsonify({
            "success": False,
            "message": "All fields (payment_id, bill_id, payment_method, payment_status, payment_date, paid_amount) are required."
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
def get_payments():
    """Retrieves all payments.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_all_payments()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@payment_bp.route("/payments/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    """Retrieves a payment by its ID.

    Args:
        payment_id (str): The unique identifier of the payment.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_payment_by_id(payment_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@payment_bp.route("/payments/<payment_id>", methods=["PUT"])
def update_payment_route(payment_id):
    """Updates an existing payment.

    Args:
        payment_id (str): The unique identifier of the payment.

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
    payment_method = data.get("payment_method")
    payment_status = data.get("payment_status")
    payment_date = data.get("payment_date")
    paid_amount = data.get("paid_amount")

    string_fields = [
        bill_id,
        payment_method,
        payment_status,
        payment_date,
    ]

    if (
        not all(
            isinstance(field, str) and field.strip()
            for field in string_fields
        )
        or paid_amount is None
        or paid_amount == ""
    ):
        return jsonify({
            "success": False,
            "message": "All fields (bill_id, payment_method, payment_status, payment_date, paid_amount) are required."
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
def delete_payment_route(payment_id):
    """Deletes a payment by its ID.

    Args:
        payment_id (str): The unique identifier of the payment.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = delete_payment(payment_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404