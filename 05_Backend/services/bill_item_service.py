"""
Service layer for bill item-related database operations.
Handles business logic and database interactions for the bill_items table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_bill_item(
    bill_item_id: str,
    bill_id: str,
    menu_item_id: str,
    quantity: int,
    unit_price: float,
    subtotal: float
) -> dict:
    """Adds a new bill item to the database.

    Args:
        bill_item_id (str): The unique identifier for the bill item.
        bill_id (str): The identifier of the bill linked to the item.
        menu_item_id (str): The identifier of the menu item linked to the bill item.
        quantity (int): The quantity of the menu item.
        unit_price (float): The price of one menu item unit.
        subtotal (float): The subtotal amount for the bill item.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO bill_items (
                bill_item_id,
                bill_id,
                menu_item_id,
                quantity,
                unit_price,
                subtotal
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                bill_item_id,
                bill_id,
                menu_item_id,
                quantity,
                unit_price,
                subtotal,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Bill item added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Bill item with this ID already exists, or a referenced bill or menu item does not exist."
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


def get_all_bill_items() -> dict:
    """Retrieves all bill items from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the bill items list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                bill_item_id,
                bill_id,
                menu_item_id,
                quantity,
                unit_price,
                subtotal
            FROM bill_items
            ORDER BY bill_item_id ASC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No bill items found."
            }

        bill_items_list = [dict(row) for row in rows]

        return {
            "success": True,
            "bill_items": bill_items_list
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


def get_bill_item_by_id(bill_item_id: str) -> dict:
    """Retrieves a bill item from the database by its ID.

    Args:
        bill_item_id (str): The unique identifier for the bill item.

    Returns:
        dict: A dictionary containing the operation status and either
        the bill item details or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                bill_item_id,
                bill_id,
                menu_item_id,
                quantity,
                unit_price,
                subtotal
            FROM bill_items
            WHERE bill_item_id = ?;
        """

        cursor.execute(select_query, (bill_item_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Bill item not found."
            }

        return {
            "success": True,
            "bill_item": dict(row)
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


def update_bill_item(
    bill_item_id: str,
    bill_id: str,
    menu_item_id: str,
    quantity: int,
    unit_price: float,
    subtotal: float
) -> dict:
    """Updates an existing bill item in the database.

    Args:
        bill_item_id (str): The unique identifier for the bill item.
        bill_id (str): The identifier of the bill linked to the item.
        menu_item_id (str): The identifier of the menu item linked to the bill item.
        quantity (int): The quantity of the menu item.
        unit_price (float): The price of one menu item unit.
        subtotal (float): The subtotal amount for the bill item.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE bill_items
            SET
                bill_id = ?,
                menu_item_id = ?,
                quantity = ?,
                unit_price = ?,
                subtotal = ?
            WHERE bill_item_id = ?;
        """

        cursor.execute(
            update_query,
            (
                bill_id,
                menu_item_id,
                quantity,
                unit_price,
                subtotal,
                bill_item_id,
            ),
        )

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Bill item not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Bill item updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Referenced bill or menu item does not exist."
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


def delete_bill_item(bill_item_id: str) -> dict:
    """Deletes a bill item from the database by its ID.

    Args:
        bill_item_id (str): The unique identifier for the bill item.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM bill_items
            WHERE bill_item_id = ?;
        """

        cursor.execute(delete_query, (bill_item_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Bill item not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Bill item deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Bill item cannot be deleted because it is referenced by existing records."
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
