"""
jwt_utils.py

JWT creation and verification utilities for Saru POS v1.0.
"""

import os
from datetime import datetime, timedelta, timezone

import jwt


JWT_SECRET = os.getenv("SARU_POS_JWT_SECRET")

if not JWT_SECRET:
    raise RuntimeError(
        "SARU_POS_JWT_SECRET environment variable is not configured."
    )
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 60


def create_access_token(user):
    """
    Create a JWT access token for an authenticated user.
    """

    now = datetime.now(timezone.utc)

    payload = {
        "user_id": user["user_id"],
        "employee_id": user["employee_id"],
        "username": user["username"],
        "role": user["role"],
        "iat": now,
        "exp": now + timedelta(minutes=JWT_EXPIRATION_MINUTES),
    }

    return jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )


def decode_access_token(token):
    """
    Verify and decode a JWT access token.

    Returns:
        Decoded payload if valid.
        None if invalid or expired.
    """

    try:
        return jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM],
        )

    except jwt.PyJWTError:
        return None