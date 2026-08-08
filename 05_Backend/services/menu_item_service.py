import sqlite3
from connection import get_connection, close_connection

def add_menu_item(menu_item_id: str, category_id: str, item_name: str, price: float, description: str, availability: str) -> dict:
    """
    Adds a new menu item to the database.

    Args:
        menu_item_id (str): The unique identifier for the menu item.
        category_id (str): The identifier of the category this menu item belongs to.
        item_name (str): The name of the menu item.
        price (float): The price of the menu item.
        description (str): A brief description of the menu item.
        availability (str): The availability status of the menu item.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO menu_items 
            (menu_item_id, category_id, item_name, price, description, availability)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        
        cursor.execute(query, (menu_item_id, category_id, item_name, price, description, availability))
        connection.commit()

        return {
            "success": True,
            "message": "Menu item added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Menu item with this ID already exists or category does not exist."
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

def get_all_menu_items() -> dict:
    """
    Retrieves all menu items from the database.

    Returns:
        dict: A dictionary containing the success status and either a list of 
              menu items or an error message. If no menu items are found, 
              success will be False.
    """
    connection = None
    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            SELECT 
                menu_item_id, 
                category_id, 
                item_name, 
                price, 
                description, 
                availability 
            FROM 
                menu_items 
            ORDER BY 
                item_name ASC
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No menu items found."
            }

        menu_items_list = [dict(row) for row in rows]

        return {
            "success": True,
            "menu_items": menu_items_list
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


def get_menu_item_by_id(menu_item_id: str) -> dict:
    """
    Retrieves a specific menu item from the database by its ID.

    Args:
        menu_item_id (str): The unique identifier for the menu item.

    Returns:
        dict: A dictionary containing the success status and either the 
              menu item data or an error message.
    """
    connection = None
    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            SELECT 
                menu_item_id, 
                category_id, 
                item_name, 
                price, 
                description, 
                availability 
            FROM 
                menu_items 
            WHERE 
                menu_item_id = ?
        """
        
        cursor.execute(query, (menu_item_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Menu item not found."
            }

        return {
            "success": True,
            "menu_item": dict(row)
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

def update_menu_item(menu_item_id: str, category_id: str, item_name: str, price: float, description: str, availability: str) -> dict:
    """
    Updates an existing menu item in the database.

    Args:
        menu_item_id (str): The unique identifier for the menu item to update.
        category_id (str): The new category identifier for the menu item.
        item_name (str): The new name of the menu item.
        price (float): The new price of the menu item.
        description (str): The new description for the menu item.
        availability (str): The new availability status of the menu item.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE menu_items
            SET category_id = ?,
                item_name = ?,
                price = ?,
                description = ?,
                availability = ?
            WHERE menu_item_id = ?
        """
        
        cursor.execute(query, (category_id, item_name, price, description, availability, menu_item_id))
        
        if cursor.rowcount == 0:
            connection.rollback()
            return {
                "success": False,
                "message": "Menu item not found."
            }
            
        connection.commit()
        
        return {
            "success": True,
            "message": "Menu item updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Category does not exist or data integrity violation."
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

def delete_menu_item(menu_item_id: str) -> dict:
    """
    Deletes a menu item from the database.

    Args:
        menu_item_id (str): The unique identifier for the menu item to delete.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM menu_items WHERE menu_item_id = ?"
        cursor.execute(query, (menu_item_id,))
        
        if cursor.rowcount == 0:
            connection.rollback()
            return {
                "success": False,
                "message": "Menu item not found."
            }
            
        connection.commit()
        
        return {
            "success": True,
            "message": "Menu item deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Menu item cannot be deleted because it is referenced by existing records."
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