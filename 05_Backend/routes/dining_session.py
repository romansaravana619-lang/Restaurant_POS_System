"""
Routes for dining session management in Saru POS.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string

from services.dining_session_service import (
    create_dining_session,
    get_active_dining_session_by_customer,
)


dining_session_bp = Blueprint("dining_session", __name__)


@dining_session_bp.route("/dining-sessions", methods=["POST"])
@require_auth
@require_role("Admin", "Manager", "Staff")
def create_dining_session_route():
    """Creates a new dining session."""

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

    session_id = data.get("session_id")
    customer_id = data.get("customer_id")
    table_id = data.get("table_id")
    status = data.get("status", "Active")
    started_at = data.get("started_at")

    if not all([
        is_non_empty_string(session_id),
        is_non_empty_string(customer_id),
        is_non_empty_string(table_id),
        is_non_empty_string(status),
        is_non_empty_string(started_at),
    ]):
        return jsonify({
            "success": False,
            "message": (
                "session_id, customer_id, table_id, status and "
                "started_at are required."
            )
        }), 400

    result = create_dining_session(
        session_id,
        customer_id,
        table_id,
        status,
        started_at,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@dining_session_bp.route(
    "/customers/<customer_id>/active-dining-session",
    methods=["GET"],
)
@require_auth
@require_role("Admin", "Manager", "Staff")
def get_active_customer_dining_session(customer_id):
    """Gets the active dining session for a customer."""

    if not is_non_empty_string(customer_id):
        return jsonify({
            "success": False,
            "message": "Customer ID is required."
        }), 400

    result = get_active_dining_session_by_customer(customer_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404
