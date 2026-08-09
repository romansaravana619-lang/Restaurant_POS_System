"""
Service layer for payment-related database operations.
Handles business logic and database interactions for the payments table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_payment(
    payment_id: str,
    bill_id: str,
    payment_method: str,
    payment_status: str,
    payment_date: str,
    paid_amount: float
) -> dict:
    """Adds a new payment to the database.

    Args:
        payment_id (str): The unique identifier for the payment.
        bill_id (str): The identifier of the bill linked to the payment.
        payment_method (str): The method used to make the payment.
        payment_status (str): The current status of the payment.
        payment_date (str): The date the payment was made.
        paid_amount (float): The amount paid for the bill.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO payments (
                payment_id,
                bill_id,
                payment_method,
                payment_status,
                payment_date,
                paid_amount
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                payment_id,
                bill_id,
                payment_method,
                payment_status,
                payment_date,
                paid_amount,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Payment added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Payment with this ID already exists, the bill already has a payment, or the referenced bill does not exist."
        }

    except sqlite3.Error as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {str(error)}"
        }

    except Exception as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(error)}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def get_all_payments() -> dict:
    """Retrieves all payments from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the payments list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                payment_id,
                bill_id,
                payment_method,
                payment_status,
                payment_date,
                paid_amount
            FROM payments
            ORDER BY payment_date DESC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No payments found."
            }

        payments_list = [dict(row) for row in rows]

        return {
            "success": True,
            "payments": payments_list
        }

    except sqlite3.Error as error:
        return {
            "success": False,
            "message": f"Database error occurred: {str(error)}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(error)}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def get_payment_by_id(payment_id: str) -> dict:
    """Retrieves a payment from the database by its ID.

    Args:
        payment_id (str): The unique identifier for the payment.

    Returns:
        dict: A dictionary containing the operation status and either
        the payment details or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                payment_id,
                bill_id,
                payment_method,
                payment_status,
                payment_date,
                paid_amount
            FROM payments
            WHERE payment_id = ?;
        """

        cursor.execute(select_query, (payment_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Payment not found."
            }

        return {
            "success": True,
            "payment": dict(row)
        }

    except sqlite3.Error as error:
        return {
            "success": False,
            "message": f"Database error occurred: {str(error)}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(error)}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def update_payment(
    payment_id: str,
    bill_id: str,
    payment_method: str,
    payment_status: str,
    payment_date: str,
    paid_amount: float
) -> dict:
    """Updates an existing payment in the database.

    Args:
        payment_id (str): The unique identifier for the payment.
        bill_id (str): The identifier of the bill linked to the payment.
        payment_method (str): The method used to make the payment.
        payment_status (str): The current status of the payment.
        payment_date (str): The date the payment was made.
        paid_amount (float): The amount paid for the bill.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE payments
            SET
                bill_id = ?,
                payment_method = ?,
                payment_status = ?,
                payment_date = ?,
                paid_amount = ?
            WHERE payment_id = ?;
        """

        cursor.execute(
            update_query,
            (
                bill_id,
                payment_method,
                payment_status,
                payment_date,
                paid_amount,
                payment_id,
            ),
        )

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Payment not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Payment updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "The bill already has a payment, or the referenced bill does not exist."
        }

    except sqlite3.Error as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {str(error)}"
        }

    except Exception as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(error)}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def delete_payment(payment_id: str) -> dict:
    """Deletes a payment from the database by its ID.

    Args:
        payment_id (str): The unique identifier for the payment.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM payments
            WHERE payment_id = ?;
        """

        cursor.execute(delete_query, (payment_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Payment not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Payment deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Payment cannot be deleted because it is referenced by existing records."
        }

    except sqlite3.Error as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {str(error)}"
        }

    except Exception as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(error)}"
        }

    finally:
        if connection is not None:
            close_connection(connection)