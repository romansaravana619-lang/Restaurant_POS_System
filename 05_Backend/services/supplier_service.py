from copy import error
import sqlite3
from connection import get_connection, close_connection

def add_supplier(
    supplier_id: str,
    supplier_name: str,
    contact_person: str,
    phone: str,
    email: str,
    address: str,
    status: str
) -> dict:
    """Adds a new supplier to the database.

    Args:
        supplier_id (str): The unique identifier for the supplier.
        supplier_name (str): The name of the supplier or company.
        contact_person (str): The name of the main contact person.
        phone (str): The contact phone number.
        email (str): The contact email address.
        address (str): The physical address of the supplier.
        status (str): The current status of the supplier (e.g., 'Active', 'Inactive').

    Returns:
        dict: A dictionary containing the success status and a descriptive message.
    """
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO suppliers 
            (supplier_id, supplier_name, contact_person, phone, email, address, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (
            supplier_id, 
            supplier_name, 
            contact_person, 
            phone, 
            email, 
            address, 
            status
        ))
        connection.commit()

        return {
            "success": True,
            "message": "Supplier added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"Supplier with this ID or phone number already exists."
        }
    except sqlite3.Error as db_error:
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"A database error occurred: {db_error}"
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

def get_all_suppliers() -> dict:
    """Retrieves all supplier records from the database.

    Returns:
        dict: A dictionary containing the operational status ('success')
        and either a list of supplier dictionaries ('suppliers')
        or a descriptive message ('message').
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve all suppliers ordered by supplier name
        query = """
            SELECT
                supplier_id,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status
            FROM suppliers
            ORDER BY supplier_name;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        # Check if suppliers exist
        if not rows:
            return {
                "success": False,
                "message": "No suppliers found."
            }

        # Convert rows into a list of dictionaries
        suppliers = []

        for row in rows:
            suppliers.append({
                "supplier_id": row[0],
                "supplier_name": row[1],
                "contact_person": row[2],
                "phone": row[3],
                "email": row[4],
                "address": row[5],
                "status": row[6]
            })

        return {
            "success": True,
            "suppliers": suppliers
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


def get_supplier_by_id(supplier_id: str) -> dict:
    """Retrieves a single supplier record by its unique ID.

    Args:
        supplier_id (str): The unique identifier of the supplier.

    Returns:
        dict: A dictionary containing the operational status ('success')
        and either the supplier details ('supplier') or an error message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve supplier by ID
        query = """
            SELECT
                supplier_id,
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status
            FROM suppliers
            WHERE supplier_id = ?;
        """
        cursor.execute(query, (supplier_id,))
        row = cursor.fetchone()

        # Check if supplier exists
        if not row:
            return {
                "success": False,
                "message": "Supplier not found."
            }

        # Convert row into dictionary
        supplier = {
            "supplier_id": row[0],
            "supplier_name": row[1],
            "contact_person": row[2],
            "phone": row[3],
            "email": row[4],
            "address": row[5],
            "status": row[6]
        }

        return {
            "success": True,
            "supplier": supplier
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

def update_supplier(
    supplier_id: str,
    supplier_name: str,
    contact_person: str,
    phone: str,
    email: str,
    address: str,
    status: str
) -> dict:
    """Updates an existing supplier's information in the database.

    Args:
        supplier_id (str): The unique identifier of the supplier.
        supplier_name (str): The updated supplier name.
        contact_person (str): The updated contact person.
        phone (str): The updated phone number.
        email (str): The updated email address.
        address (str): The updated supplier address.
        status (str): The updated supplier status.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Update supplier details
        query = """
            UPDATE suppliers
            SET
                supplier_name = ?,
                contact_person = ?,
                phone = ?,
                email = ?,
                address = ?,
                status = ?
            WHERE supplier_id = ?;
        """

        cursor.execute(
            query,
            (
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                status,
                supplier_id
            )
        )

        connection.commit()

        # Check whether the supplier exists
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Supplier not found."
            }

        return {
            "success": True,
            "message": "Supplier updated successfully."
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


def delete_supplier(supplier_id: str) -> dict:
    """Deletes a supplier record from the database by ID.

    Args:
        supplier_id (str): The unique identifier of the supplier to delete.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Delete supplier
        query = """
            DELETE FROM suppliers
            WHERE supplier_id = ?;
        """

        cursor.execute(query, (supplier_id,))
        connection.commit()

        # Check whether a supplier was actually deleted
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Supplier not found."
            }

        return {
            "success": True,
            "message": "Supplier deleted successfully."
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