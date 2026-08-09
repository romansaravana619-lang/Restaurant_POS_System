"""
Service layer for settings-related database operations.
Handles business logic and database interactions for the settings table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_setting(
    setting_id: str,
    restaurant_name: str,
    gst_number: str,
    address: str,
    phone: str,
    email: str,
    currency: str,
    tax_percentage: float
) -> dict:
    """Adds a new settings record to the database.

    Args:
        setting_id (str): The unique identifier for the settings record.
        restaurant_name (str): The restaurant name.
        gst_number (str): The GST number.
        address (str): The restaurant address.
        phone (str): The restaurant phone number.
        email (str): The restaurant email address.
        currency (str): The currency used by the restaurant.
        tax_percentage (float): The applicable tax percentage.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO settings (
                setting_id,
                restaurant_name,
                gst_number,
                address,
                phone,
                email,
                currency,
                tax_percentage
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                setting_id,
                restaurant_name,
                gst_number,
                address,
                phone,
                email,
                currency,
                tax_percentage,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Settings added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Settings with this ID already exists."
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


def get_all_settings() -> dict:
    """Retrieves all settings records from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the settings list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                setting_id,
                restaurant_name,
                gst_number,
                address,
                phone,
                email,
                currency,
                tax_percentage
            FROM settings
            ORDER BY setting_id ASC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No settings found."
            }

        settings_list = [dict(row) for row in rows]

        return {
            "success": True,
            "settings": settings_list
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


def get_setting_by_id(setting_id: str) -> dict:
    """Retrieves a settings record from the database by its ID.

    Args:
        setting_id (str): The unique identifier for the settings record.

    Returns:
        dict: A dictionary containing the operation status and either
        the settings details or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                setting_id,
                restaurant_name,
                gst_number,
                address,
                phone,
                email,
                currency,
                tax_percentage
            FROM settings
            WHERE setting_id = ?;
        """

        cursor.execute(select_query, (setting_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Settings not found."
            }

        return {
            "success": True,
            "setting": dict(row)
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


def update_setting(
    setting_id: str,
    restaurant_name: str,
    gst_number: str,
    address: str,
    phone: str,
    email: str,
    currency: str,
    tax_percentage: float
) -> dict:
    """Updates an existing settings record in the database.

    Args:
        setting_id (str): The unique identifier for the settings record.
        restaurant_name (str): The restaurant name.
        gst_number (str): The GST number.
        address (str): The restaurant address.
        phone (str): The restaurant phone number.
        email (str): The restaurant email address.
        currency (str): The currency used by the restaurant.
        tax_percentage (float): The applicable tax percentage.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE settings
            SET
                restaurant_name = ?,
                gst_number = ?,
                address = ?,
                phone = ?,
                email = ?,
                currency = ?,
                tax_percentage = ?
            WHERE setting_id = ?;
        """

        cursor.execute(
            update_query,
            (
                restaurant_name,
                gst_number,
                address,
                phone,
                email,
                currency,
                tax_percentage,
                setting_id,
            ),
        )

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Settings not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Settings updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Settings with this ID already exists."
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


def delete_setting(setting_id: str) -> dict:
    """Deletes a settings record from the database by its ID.

    Args:
        setting_id (str): The unique identifier for the settings record.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM settings
            WHERE setting_id = ?;
        """

        cursor.execute(delete_query, (setting_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Settings not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Settings deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Settings cannot be deleted because it is referenced by existing records."
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