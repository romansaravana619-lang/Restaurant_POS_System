"""
auth_middleware.py

JWT authentication middleware for Saru POS v1.0.
"""

from functools import wraps

from flask import request, jsonify

from utils.jwt_utils import decode_access_token


def require_auth(view_function):
    """
    Require a valid JWT Bearer token before accessing an endpoint.
    """

    @wraps(view_function)
    def wrapped(*args, **kwargs):
        authorization = request.headers.get("Authorization", "")

        if not authorization.startswith("Bearer "):
            return jsonify({
                "success": False,
                "message": "Authentication token is required."
            }), 401

        token = authorization.split(" ", 1)[1].strip()

        if not token:
            return jsonify({
                "success": False,
                "message": "Authentication token is required."
            }), 401

        payload = decode_access_token(token)

        if payload is None:
            return jsonify({
                "success": False,
                "message": "Invalid or expired authentication token."
            }), 401

        request.user = payload

        return view_function(*args, **kwargs)

    return wrapped

def require_role(*allowed_roles):
    """
    Require the authenticated user to have one of the allowed roles.

    Returns:
        403 if the authenticated user's role is not authorized.
    """

    def decorator(view_function):
        @wraps(view_function)
        def wrapped(*args, **kwargs):
            user = getattr(request, "user", None)

            if not user:
                return jsonify({
                    "success": False,
                    "message": "Authentication required."
                }), 401

            user_role = user.get("role")

            if user_role not in allowed_roles:
                return jsonify({
                    "success": False,
                    "message": "You do not have permission to access this resource."
                }), 403

            return view_function(*args, **kwargs)

        return wrapped

    return decorator