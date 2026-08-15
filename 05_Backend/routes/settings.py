"""
Settings Routes Module

This module defines the Flask routes for restaurant settings management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string, is_number

from services.settings_service import (
    add_setting,
    get_all_settings,
    get_setting_by_id,
    update_setting,
    delete_setting,
)


settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_setting():
    """Creates a new settings record."""

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

    setting_id = data.get("setting_id")
    restaurant_name = data.get("restaurant_name")
    gst_number = data.get("gst_number")
    address = data.get("address")
    phone = data.get("phone")
    email = data.get("email")
    currency = data.get("currency")
    tax_percentage = data.get("tax_percentage")

    if not all([
        is_non_empty_string(setting_id),
        is_non_empty_string(restaurant_name),
        is_non_empty_string(currency),
        is_number(tax_percentage),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "Required fields (setting_id, restaurant_name, "
                "currency, tax_percentage) are required "
                "and must have valid types."
            )
        }), 400

    optional_string_fields = [
        gst_number,
        address,
        phone,
        email,
    ]

    if not all(
        field is None or is_non_empty_string(field)
        for field in optional_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Optional text fields must be non-empty strings."
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
@require_auth
@require_role("Admin", "Manager")
def get_settings():
    """Retrieves all settings records."""

    result = get_all_settings()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@settings_bp.route("/settings/<setting_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager")
def get_setting(setting_id):
    """Retrieves a settings record by its ID."""

    result = get_setting_by_id(setting_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@settings_bp.route("/settings/<setting_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_setting_route(setting_id):
    """Updates an existing settings record."""

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

    restaurant_name = data.get("restaurant_name")
    gst_number = data.get("gst_number")
    address = data.get("address")
    phone = data.get("phone")
    email = data.get("email")
    currency = data.get("currency")
    tax_percentage = data.get("tax_percentage")

    if not all([
        is_non_empty_string(restaurant_name),
        is_non_empty_string(currency),
        is_number(tax_percentage),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "Required fields (restaurant_name, currency, "
                "tax_percentage) are required and must have valid types."
            )
        }), 400

    optional_string_fields = [
        gst_number,
        address,
        phone,
        email,
    ]

    if not all(
        field is None or is_non_empty_string(field)
        for field in optional_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Optional text fields must be non-empty strings."
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
@require_auth
@require_role("Admin", "Manager")
def delete_setting_route(setting_id):
    """Deletes a settings record by its ID."""

    result = delete_setting(setting_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404