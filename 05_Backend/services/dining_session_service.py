"""
Service layer for dining session-related database operations.
Handles business logic and database interactions for the dining_sessions table.
"""

import sqlite3

from connection import get_connection, close_connection


ALLOWED_SESSION_STATUSES = {
    "Active",
    "Closed",
}


def create_dining_session(
    session_id: str,
    customer_id: str,
    table_id: str,
    status: str,
    started_at: str,
) -> dict:
    """
    Creates a new active dining session.
    """

    connection = None

    try:
        if status not in ALLOWED_SESSION_STATUSES:
            return {
                "success": False,
                "message": "Invalid dining session status."
            }

        connection = get_connection()
        cursor = connection.cursor()

        table = cursor.execute(
            """SELECT table_id, table_number, capacity, status
               FROM restaurant_tables WHERE table_id = ?""",
            (table_id,),
        ).fetchone()
        if not table:
            return {"success": False, "message": "Restaurant table not found."}
        if str(table["status"]).lower() != "available":
            return {"success": False, "message": "Selected table is not available."}

        cursor.execute(
            """
            SELECT session_id
            FROM dining_sessions
            WHERE table_id = ?
              AND status = 'Active'
            LIMIT 1
            """,
            (table_id,),
        )

        existing_table_session = cursor.fetchone()

        if existing_table_session:
            return {
                "success": False,
                "message": "Table already has an active dining session."
            }

        cursor.execute(
            """
            SELECT session_id
            FROM dining_sessions
            WHERE customer_id = ?
              AND status = 'Active'
            LIMIT 1
            """,
            (customer_id,),
        )

        existing_customer_session = cursor.fetchone()

        if existing_customer_session:
            return {
                "success": False,
                "message": "Customer already has an active dining session."
            }

        cursor.execute(
            """
            INSERT INTO dining_sessions (
                session_id,
                customer_id,
                table_id,
                status,
                started_at,
                closed_at
            )
            VALUES (?, ?, ?, ?, ?, NULL)
            """,
            (
                session_id,
                customer_id,
                table_id,
                status,
                started_at,
            ),
        )

        cursor.execute(
            "UPDATE restaurant_tables SET status = 'Occupied' WHERE table_id = ?",
            (table_id,),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Dining session created successfully.",
            "session_id": session_id,
            "customer_id": customer_id,
            "table_id": table_id,
            "status": status,
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Invalid customer or table reference."
        }

    except sqlite3.Error as e:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {str(e)}"
        }

    except Exception as e:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(e)}"
        }

    finally:
        if connection:
            close_connection(connection)


def get_active_dining_session_by_customer(customer_id: str) -> dict:
    """
    Retrieves the active dining session for a customer.
    """

    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                session_id,
                customer_id,
                table_id,
                status,
                started_at,
                closed_at
            FROM dining_sessions
            WHERE customer_id = ?
              AND status = 'Active'
            ORDER BY started_at DESC
            LIMIT 1
            """,
            (customer_id,),
        )

        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "No active dining session found."
            }

        return {
            "success": True,
            "dining_session": dict(row),
        }

    except sqlite3.Error as e:
        return {
            "success": False,
            "message": f"Database error occurred: {str(e)}"
        }

    except Exception as e:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(e)}"
        }

    finally:
        if connection:
            close_connection(connection)
