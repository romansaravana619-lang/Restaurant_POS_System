"""
Service layer for billing-related database operations.
Handles business logic and database interactions for the bills table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_bill(
    bill_id: str,
    customer_id: str,
    employee_id: str,
    table_id: str,
    invoice_number: str,
    bill_date: str,
    total_amount: float,
    status: str
) -> dict:
    """Adds a new bill to the database.

    Args:
        bill_id (str): The unique identifier for the bill.
        customer_id (str): The identifier of the customer linked to the bill.
        employee_id (str): The identifier of the employee who created the bill.
        table_id (str): The identifier of the restaurant table linked to the bill.
        invoice_number (str): The unique invoice number for the bill.
        bill_date (str): The date the bill was created.
        total_amount (float): The total amount for the bill.
        status (str): The current status of the bill.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO bills (
                bill_id,
                customer_id,
                employee_id,
                table_id,
                invoice_number,
                bill_date,
                total_amount,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                bill_id,
                customer_id,
                employee_id,
                table_id,
                invoice_number,
                bill_date,
                total_amount,
                status,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Bill added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Bill with this ID or invoice number already exists, or a referenced record does not exist."
        }

    except sqlite3.Error as db_error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def get_bill_by_id(bill_id: str) -> dict:
    """Retrieves a bill from the database by its ID.

    Args:
        bill_id (str): The unique identifier for the bill.

    Returns:
        dict: A dictionary containing the operation status and either
        the bill details or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                bill_id,
                customer_id,
                employee_id,
                table_id,
                invoice_number,
                bill_date,
                total_amount,
                status
            FROM bills
            WHERE bill_id = ?;
        """

        cursor.execute(select_query, (bill_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Bill not found."
            }

        return {
            "success": True,
            "bill": dict(row)
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


def get_all_bills() -> dict:
    """Retrieves all bills from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the bills list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                bill_id,
                customer_id,
                employee_id,
                table_id,
                invoice_number,
                bill_date,
                total_amount,
                status
            FROM bills
            ORDER BY bill_date DESC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No bills found."
            }

        bills_list = [dict(row) for row in rows]

        return {
            "success": True,
            "bills": bills_list
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


def update_bill(
    bill_id: str,
    customer_id: str,
    employee_id: str,
    table_id: str,
    invoice_number: str,
    bill_date: str,
    total_amount: float,
    status: str
) -> dict:
    """Updates an existing bill in the database.

    Args:
        bill_id (str): The unique identifier for the bill.
        customer_id (str): The identifier of the customer linked to the bill.
        employee_id (str): The identifier of the employee who created the bill.
        table_id (str): The identifier of the restaurant table linked to the bill.
        invoice_number (str): The unique invoice number for the bill.
        bill_date (str): The date the bill was created.
        total_amount (float): The total amount for the bill.
        status (str): The current status of the bill.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE bills
            SET
                customer_id = ?,
                employee_id = ?,
                table_id = ?,
                invoice_number = ?,
                bill_date = ?,
                total_amount = ?,
                status = ?
            WHERE bill_id = ?;
        """

        cursor.execute(
            update_query,
            (
                customer_id,
                employee_id,
                table_id,
                invoice_number,
                bill_date,
                total_amount,
                status,
                bill_id,
            ),
        )

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Bill not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Bill updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Invoice number already exists, or a referenced record does not exist."
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


def delete_bill(bill_id: str) -> dict:
    """Deletes a bill from the database by its ID.

    Args:
        bill_id (str): The unique identifier for the bill.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM bills
            WHERE bill_id = ?;
        """

        cursor.execute(delete_query, (bill_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Bill not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Bill deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Bill cannot be deleted because it is referenced by existing records."
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
