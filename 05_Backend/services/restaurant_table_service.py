"""
Service layer for restaurant table-related database operations.
Handles business logic and database interactions for the restaurant_tables table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_restaurant_table(table_id: str, table_number: str, capacity: int, status: str) -> dict:
    """
    Adds a new restaurant table to the database.

    Args:
        table_id (str): The unique identifier for the restaurant table.
        table_number (str): The unique table number or name.
        capacity (int): The seating capacity of the table.
        status (str): The current status of the table.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO restaurant_tables 
            (table_id, table_number, capacity, status)
            VALUES (?, ?, ?, ?)
        """
        
        cursor.execute(query, (table_id, table_number, capacity, status))
        connection.commit()

        return {
            "success": True,
            "message": "Restaurant table added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Restaurant table with this ID or table number already exists."
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

def get_all_restaurant_tables() -> dict:
    """
    Retrieves all restaurant tables from the database.

    Returns:
        dict: A dictionary containing the success status and either a list of 
              restaurant tables or an error message. If no restaurant tables 
              are found, success will be False.
    """
    connection = None
    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            SELECT 
                table_id, 
                table_number, 
                capacity, 
                status 
            FROM 
                restaurant_tables 
            ORDER BY 
                table_number ASC
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No restaurant tables found."
            }

        restaurant_tables_list = [dict(row) for row in rows]

        return {
            "success": True,
            "restaurant_tables": restaurant_tables_list
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


def get_restaurant_table_by_id(table_id: str) -> dict:
    """
    Retrieves a specific restaurant table from the database by its ID.

    Args:
        table_id (str): The unique identifier for the restaurant table.

    Returns:
        dict: A dictionary containing the success status and either the 
              restaurant table data or an error message.
    """
    connection = None
    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        query = """
            SELECT 
                table_id, 
                table_number, 
                capacity, 
                status 
            FROM 
                restaurant_tables 
            WHERE 
                table_id = ?
        """
        
        cursor.execute(query, (table_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Restaurant table not found."
            }

        return {
            "success": True,
            "restaurant_table": dict(row)
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

def update_restaurant_table(table_id: str, table_number: str, capacity: int, status: str) -> dict:
    """
    Updates an existing restaurant table in the database.

    Args:
        table_id (str): The unique identifier for the restaurant table to update.
        table_number (str): The new unique table number or name.
        capacity (int): The new seating capacity of the table.
        status (str): The new status of the table.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE restaurant_tables
            SET table_number = ?,
                capacity = ?,
                status = ?
            WHERE table_id = ?
        """
        
        cursor.execute(query, (table_number, capacity, status, table_id))
        
        if cursor.rowcount == 0:
            connection.rollback()
            return {
                "success": False,
                "message": "Restaurant table not found."
            }
            
        connection.commit()
        
        return {
            "success": True,
            "message": "Restaurant table updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Restaurant table with this table number already exists."
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

def delete_restaurant_table(table_id: str) -> dict:
    """
    Deletes a restaurant table from the database.

    Args:
        table_id (str): The unique identifier for the restaurant table to delete.

    Returns:
        dict: A dictionary containing the success status and a response message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM restaurant_tables WHERE table_id = ?"
        cursor.execute(query, (table_id,))
        
        if cursor.rowcount == 0:
            connection.rollback()
            return {
                "success": False,
                "message": "Restaurant table not found."
            }
            
        connection.commit()
        
        return {
            "success": True,
            "message": "Restaurant table deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": "Restaurant table cannot be deleted because it is referenced by existing records."
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