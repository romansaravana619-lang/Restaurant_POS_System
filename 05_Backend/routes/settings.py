"""
Settings Routes Module

This module defines the Flask routes for restaurant settings management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from services.settings_service import (
    add_setting,
    get_all_settings,
    get_setting_by_id,
    update_setting,
    delete_setting,
)


settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings", methods=["POST"])
def create_setting():
    """Creates a new settings record.

    Reads settings details from the request body, validates the input,
    and creates a new settings record through the service layer.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    setting_id = data.get("setting_id")
    restaurant_name = data.get("restaurant_name")
    gst_number = data.get("gst_number")
    address = data.get("address")
    phone = data.get("phone")
    email = data.get("email")
    currency = data.get("currency")
    tax_percentage = data.get("tax_percentage")

    required_string_fields = [
        setting_id,
        restaurant_name,
        currency,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Required fields (setting_id, restaurant_name, currency) are missing."
        }), 400

    optional_string_fields = [
        gst_number,
        address,
        phone,
        email,
    ]

    for field in optional_string_fields:
        if field is not None and not isinstance(field, str):
            return jsonify({
                "success": False,
                "message": "Optional text fields must be strings."
            }), 400

    if tax_percentage is None or tax_percentage == "":
        return jsonify({
            "success": False,
            "message": "Required field tax_percentage is missing."
        }), 400

    result = add_setting(
        setting_id=setting_id,
        restaurant_name=restaurant_name,
        gst_number=gst_number,
        address=address,
        phone=phone,
        email=email,
        currency=currency,
        tax_percentage=tax_percentage,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@settings_bp.route("/settings", methods=["GET"])
def get_settings():
    """Retrieves all settings records.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_all_settings()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@settings_bp.route("/settings/<setting_id>", methods=["GET"])
def get_setting(setting_id):
    """Retrieves a settings record by its ID.

    Args:
        setting_id (str): The unique identifier for the settings record.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_setting_by_id(setting_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@settings_bp.route("/settings/<setting_id>", methods=["PUT"])
def update_setting_route(setting_id):
    """Updates an existing settings record.

    Args:
        setting_id (str): The unique identifier for the settings record.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    restaurant_name = data.get("restaurant_name")
    gst_number = data.get("gst_number")
    address = data.get("address")
    phone = data.get("phone")
    email = data.get("email")
    currency = data.get("currency")
    tax_percentage = data.get("tax_percentage")

    required_string_fields = [
        restaurant_name,
        currency,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Required fields (restaurant_name, currency) are missing."
        }), 400

    optional_string_fields = [
        gst_number,
        address,
        phone,
        email,
    ]

    for field in optional_string_fields:
        if field is not None and not isinstance(field, str):
            return jsonify({
                "success": False,
                "message": "Optional text fields must be strings."
            }), 400

    if tax_percentage is None or tax_percentage == "":
        return jsonify({
            "success": False,
            "message": "Required field tax_percentage is missing."
        }), 400

    result = update_setting(
        setting_id=setting_id,
        restaurant_name=restaurant_name,
        gst_number=gst_number,
        address=address,
        phone=phone,
        email=email,
        currency=currency,
        tax_percentage=tax_percentage,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@settings_bp.route("/settings/<setting_id>", methods=["DELETE"])
def delete_setting_route(setting_id):
    """Deletes a settings record by its ID.

    Args:
        setting_id (str): The unique identifier for the settings record.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = delete_setting(setting_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404