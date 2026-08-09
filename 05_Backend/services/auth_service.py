"""
auth_service.py

Contains authentication business logic for Saru POS v1.0.
No Flask routes are defined here — pure service-layer logic.
Uses connection utilities from connection.py.
"""

import sqlite3

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

from connection import get_connection, close_connection


password_hasher = PasswordHasher()


def verify_user(username, password):
    """
    Verify user credentials against the users table.

    Supports Argon2 password hashes and performs a one-time migration
    for existing plaintext passwords after successful authentication.
    """

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                user_id,
                employee_id,
                username,
                password,
                role,
                status
            FROM users
            WHERE username = ?
              AND status = 'Active'
        """

        cursor.execute(query, (username,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Invalid username or password.",
            }

        stored_password = row["password"]
        password_verified = False
        plaintext_password = False

        try:
            password_verified = password_hasher.verify(
                stored_password,
                password,
            )

        except (VerificationError, InvalidHashError):
            password_verified = False

        # Backward compatibility for existing plaintext passwords.
        if not password_verified and stored_password == password:
            password_verified = True
            plaintext_password = True

        if not password_verified:
            return {
                "success": False,
                "message": "Invalid username or password.",
            }

        # Migrate existing plaintext password to Argon2.
        if plaintext_password:
            hashed_password = password_hasher.hash(password)

            update_query = """
                UPDATE users
                SET password = ?
                WHERE user_id = ?
            """

            cursor.execute(
                update_query,
                (hashed_password, row["user_id"]),
            )

            connection.commit()

        user = {
            "user_id": row["user_id"],
            "employee_id": row["employee_id"],
            "username": row["username"],
            "role": row["role"],
            "status": row["status"],
        }

        return {
            "success": True,
            "user": user,
        }

    except sqlite3.Error as db_error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {db_error}",
        }

    except Exception as error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}",
        }

    finally:
        if connection is not None:
            close_connection(connection)