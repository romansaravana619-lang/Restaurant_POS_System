"""
Service layer for billing-related database operations.
Handles business logic and database interactions for the bills table.
"""

import sqlite3
from uuid import uuid4

from connection import get_connection, close_connection



def create_checkout(
    customer_id: str,
    employee_id: str,
    table_id: str,
    invoice_number: str,
    bill_date: str,
    payment_method: str,
    items: list,
) -> dict:
    """Create a complete paid bill in one database transaction.

    Menu prices are read from the database and the bill total is calculated
    server-side. This prevents a client from changing prices or creating a
    partially saved bill when one of the individual API calls fails.
    """
    connection = None
    try:
        if not items or not isinstance(items, list):
            return {"success": False, "message": "At least one bill item is required."}
        if payment_method not in {"Cash", "UPI", "Card"}:
            return {"success": False, "message": "Invalid payment method."}

        connection = get_connection()
        cursor = connection.cursor()

        customer = cursor.execute(
            "SELECT customer_id FROM customers WHERE customer_id = ? AND status = 'Active'",
            (customer_id,),
        ).fetchone()
        if not customer:
            return {"success": False, "message": "Active customer not found."}

        employee = cursor.execute(
            "SELECT employee_id FROM employees WHERE employee_id = ? AND status = 'Active'",
            (employee_id,),
        ).fetchone()
        if not employee:
            return {"success": False, "message": "Active employee not found."}

        table = cursor.execute(
            "SELECT table_id, status FROM restaurant_tables WHERE table_id = ?",
            (table_id,),
        ).fetchone()
        if not table:
            return {"success": False, "message": "Restaurant table not found."}

        active_session = cursor.execute(
            """SELECT session_id FROM dining_sessions
               WHERE customer_id = ? AND table_id = ? AND status = 'Active'
               LIMIT 1""",
            (customer_id, table_id),
        ).fetchone()
        table_is_available = str(table["status"]).lower() == "available"
        if not table_is_available and not active_session:
            return {"success": False, "message": "Selected table is not available for this customer."}

        setting = cursor.execute(
            "SELECT tax_percentage FROM settings ORDER BY setting_id ASC LIMIT 1"
        ).fetchone()
        tax_percentage = float(setting["tax_percentage"] if setting else 0)

        normalized_items = []
        subtotal = 0.0
        for item in items:
            menu_item_id = item.get("menu_item_id") if isinstance(item, dict) else None
            quantity = item.get("quantity") if isinstance(item, dict) else None
            if not isinstance(menu_item_id, str) or not menu_item_id.strip():
                return {"success": False, "message": "Each bill item needs a menu item ID."}
            if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
                return {"success": False, "message": "Bill item quantity must be a positive integer."}

            row = cursor.execute(
                """SELECT menu_item_id, item_name, price
                   FROM menu_items
                   WHERE menu_item_id = ? AND availability = 'Available'""",
                (menu_item_id,),
            ).fetchone()
            if not row:
                return {"success": False, "message": f"Menu item {menu_item_id} is unavailable."}

            unit_price = float(row["price"])
            line_total = round(unit_price * quantity, 2)
            subtotal += line_total
            normalized_items.append({
                "menu_item_id": row["menu_item_id"],
                "item_name": row["item_name"],
                "quantity": quantity,
                "unit_price": unit_price,
                "subtotal": line_total,
            })

        subtotal = round(subtotal, 2)
        tax_amount = round(subtotal * tax_percentage / 100, 2)
        total_amount = round(subtotal + tax_amount, 2)
        bill_id = f"BILL{uuid4().hex[:20].upper()}"
        payment_id = f"PAY{uuid4().hex[:20].upper()}"

        cursor.execute(
            """INSERT INTO bills
               (bill_id, customer_id, employee_id, table_id, invoice_number,
                bill_date, total_amount, status)
               VALUES (?, ?, ?, ?, ?, ?, ?, 'Completed')""",
            (bill_id, customer_id, employee_id, table_id, invoice_number, bill_date, total_amount),
        )

        for index, item in enumerate(normalized_items):
            bill_item_id = f"BITEM{uuid4().hex[:20].upper()}"
            cursor.execute(
                """INSERT INTO bill_items
                   (bill_item_id, bill_id, menu_item_id, quantity, unit_price, subtotal)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (bill_item_id, bill_id, item["menu_item_id"], item["quantity"], item["unit_price"], item["subtotal"]),
            )

        cursor.execute(
            """INSERT INTO payments
               (payment_id, bill_id, payment_method, payment_status, payment_date, paid_amount)
               VALUES (?, ?, ?, 'Paid', ?, ?)""",
            (payment_id, bill_id, payment_method, bill_date, total_amount),
        )

        # Completed checkout closes the active dining session and releases the table.
        if active_session:
            cursor.execute(
                """UPDATE dining_sessions
                   SET status = 'Closed', closed_at = ?
                   WHERE session_id = ?""",
                (bill_date, active_session["session_id"]),
            )
            cursor.execute(
                "UPDATE restaurant_tables SET status = 'Available' WHERE table_id = ?",
                (table_id,),
            )

        connection.commit()

        return {
            "success": True,
            "message": "Checkout completed successfully.",
            "bill": {
                "bill_id": bill_id,
                "invoice_number": invoice_number,
                "bill_date": bill_date,
                "customer_id": customer_id,
                "employee_id": employee_id,
                "table_id": table_id,
                "subtotal": subtotal,
                "tax_percentage": tax_percentage,
                "tax_amount": tax_amount,
                "total_amount": total_amount,
                "status": "Completed",
                "payment_method": payment_method,
                "items": normalized_items,
            },
        }
    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {"success": False, "message": "Checkout could not be completed because a record already exists or a reference is invalid."}
    except sqlite3.Error:
        if connection:
            connection.rollback()
        return {"success": False, "message": "Checkout could not be completed because of a database error."}
    except Exception:
        if connection:
            connection.rollback()
        return {"success": False, "message": "Checkout could not be completed."}
    finally:
        if connection is not None:
            close_connection(connection)

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
