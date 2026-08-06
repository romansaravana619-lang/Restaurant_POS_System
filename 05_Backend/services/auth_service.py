"""
auth_service.py

Contains authentication business logic for Saru POS v1.0.
No Flask routes are defined here — pure service-layer logic.
Uses connection utilities from connection.py.
"""

import sqlite3
from connection import get_connection, close_connection


def verify_user(username, password):
    """
    Verify user credentials against the users table.

    Args:
        username (str): Username provided by the client.
        password (str): Password provided by the client.

    Returns:
        dict: Result dictionary containing success status and either
              the matched user record or an error message.
    """
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Query user by username and password using parameterized query
        query = """
            SELECT user_id,
                   employee_id,
                   username,
                   role,
                   status
            FROM users
            WHERE username = ?
              AND password = ?
              AND status = 'Active'
        """
        cursor.execute(query, (username, password))
        row = cursor.fetchone()

        # If a matching user record is found
        if row:
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

        # No matching record found
        return {
            "success": False,
            "message": "Invalid username or password.",
        }

    except sqlite3.Error as db_error:
        # Handle database-related errors
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}",
        }

    except Exception as error:
        # Handle any other unexpected errors
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}",
        }

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)
    