import sqlite3
from connection import get_connection, close_connection


def add_inventory_item(
    inventory_id,
    supplier_id,
    item_name,
    unit,
    quantity,
    unit_cost,
    reorder_level,
    status,
):
    """Adds a new inventory item to the database.

    Args:
        inventory_id (str): The unique identifier for the inventory item.
        supplier_id (str): The unique identifier of the supplier.
        item_name (str): The name of the inventory item.
        unit (str): The unit of measurement.
        quantity (float): The available stock quantity.
        unit_cost (float): Cost per unit.
        reorder_level (float): Minimum stock level before reorder.
        status (str): Inventory item status.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO inventory_items (
                inventory_id,
                supplier_id,
                item_name,
                unit,
                quantity,
                unit_cost,
                reorder_level,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                inventory_id,
                supplier_id,
                item_name,
                unit,
                quantity,
                unit_cost,
                reorder_level,
                status,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Inventory item added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Inventory ID already exists."
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


def get_all_inventory_items() -> dict:
    """Retrieves all inventory items from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the inventory items list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """
            SELECT
                inventory_id,
                supplier_id,
                item_name,
                unit,
                quantity,
                unit_cost,
                reorder_level,
                status
            FROM inventory_items
            ORDER BY item_name;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No inventory items found."
            }

        inventory_items = []

        for row in rows:
            inventory_items.append({
                "inventory_id": row[0],
                "supplier_id": row[1],
                "item_name": row[2],
                "unit": row[3],
                "quantity": row[4],
                "unit_cost": row[5],
                "reorder_level": row[6],
                "status": row[7]
            })

        return {
            "success": True,
            "inventory_items": inventory_items
        }

    except sqlite3.Error as db_error:
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def get_inventory_item_by_id(inventory_id: str) -> dict:
    """Retrieves a single inventory item from the database by ID.

    Args:
        inventory_id (str): The unique identifier of the inventory item.

    Returns:
        dict: A dictionary containing the operation status and either
        the inventory item details or an error message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve inventory item by ID
        select_query = """
            SELECT
                inventory_id,
                supplier_id,
                item_name,
                unit,
                quantity,
                unit_cost,
                reorder_level,
                status
            FROM inventory_items
            WHERE inventory_id = ?;
        """

        cursor.execute(select_query, (inventory_id,))
        row = cursor.fetchone()

        # Check whether the inventory item exists
        if not row:
            return {
                "success": False,
                "message": "Inventory item not found."
            }

        inventory_item = {
            "inventory_id": row[0],
            "supplier_id": row[1],
            "item_name": row[2],
            "unit": row[3],
            "quantity": row[4],
            "unit_cost": row[5],
            "reorder_level": row[6],
            "status": row[7]
        }

        return {
            "success": True,
            "inventory_item": inventory_item
        }

    except sqlite3.Error as db_error:
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)

def update_inventory_item(
    inventory_id: str,
    supplier_id: str,
    item_name: str,
    unit: str,
    quantity: float,
    unit_cost: float,
    reorder_level: float,
    status: str
) -> dict:
    """Updates an existing inventory item in the database.

    Args:
        inventory_id (str): The unique identifier of the inventory item.
        supplier_id (str): The supplier ID associated with the inventory item.
        item_name (str): The inventory item name.
        unit (str): The unit of measurement.
        quantity (float): The available stock quantity.
        unit_cost (float): Cost per unit.
        reorder_level (float): Minimum stock level before reorder.
        status (str): Inventory item status.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE inventory_items
            SET
                supplier_id = ?,
                item_name = ?,
                unit = ?,
                quantity = ?,
                unit_cost = ?,
                reorder_level = ?,
                status = ?
            WHERE inventory_id = ?;
        """

        cursor.execute(
            update_query,
            (
                supplier_id,
                item_name,
                unit,
                quantity,
                unit_cost,
                reorder_level,
                status,
                inventory_id
            )
        )

        connection.commit()

        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Inventory item not found."
            }

        return {
            "success": True,
            "message": "Inventory item updated successfully."
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


def delete_inventory_item(inventory_id: str) -> dict:
    """Deletes an inventory item from the database by ID.

    Args:
        inventory_id (str): The unique identifier of the inventory item.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Delete inventory item
        delete_query = """
            DELETE FROM inventory_items
            WHERE inventory_id = ?;
        """

        cursor.execute(delete_query, (inventory_id,))
        connection.commit()

        # Check whether an inventory item was actually deleted
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Inventory item not found."
            }

        return {
            "success": True,
            "message": "Inventory item deleted successfully."
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
