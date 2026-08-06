"""
customer_service.py

Service layer for customer-related database operations.
Handles all business logic and database interactions
for the customers table.
"""

import sqlite3
from connection import get_connection, close_connection


def add_customer(customer_id, customer_name, phone, email, status):
    """
    Add a new customer to the database.

    Args:
        customer_id (str): Customer ID.
        customer_name (str): Customer name.
        phone (str): Phone number.
        email (str): Email address.
        status (str): Customer status.

    Returns:
        dict: Success status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Insert customer record
        query = """
            INSERT INTO customers (
                customer_id,
                customer_name,
                phone,
                email,
                status
            )
            VALUES (?, ?, ?, ?, ?)
        """

        cursor.execute(
            query,
            (
                customer_id,
                customer_name,
                phone,
                email,
                status
            )
        )

        connection.commit()

        return {
            "success": True,
            "message": "Customer added successfully."
        }

    except sqlite3.IntegrityError:
        return {
            "success": False,
            "message": "Customer ID already exists."
        }

    except sqlite3.Error as db_error:
        return {
            "success": False,
            "message": f"Database error: {db_error}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)


def get_all_customers():
    """
    Retrieve all customer records ordered by customer name.

    Returns:
        dict: Success status and customer list.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve all customers
        query = """
            SELECT
                customer_id,
                customer_name,
                phone,
                email,
                status
            FROM customers
            ORDER BY customer_name;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        # No records found
        if not rows:
            return {
                "success": False,
                "message": "No customers found."
            }

        customers = []

        for row in rows:
            customers.append({
                "customer_id": row["customer_id"],
                "customer_name": row["customer_name"],
                "phone": row["phone"],
                "email": row["email"],
                "status": row["status"]
            })

        return {
            "success": True,
            "customers": customers
        }

    except sqlite3.Error as db_error:
        return {
            "success": False,
            "message": f"Database error: {db_error}"
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)

def get_customer_by_id(customer_id):
    """
    Retrieve a single customer record by their ID.

    Args:
        customer_id (int or str): The unique identifier of the customer to retrieve.

    Returns:
        dict: A dictionary containing success status and the customer details,
              or an error message if the customer is not found or an exception occurs.
    """
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Execute parameterized SQL query to fetch a single customer record
        query = """
            SELECT
                customer_id,
                customer_name,
                phone,
                email,
                status
            FROM customers
            WHERE customer_id = ?;
        """
        cursor.execute(query, (customer_id,))
        row = cursor.fetchone()

        # Check if customer record exists
        if not row:
            return {
                "success": False,
                "message": "Customer not found."
            }

        # Convert fetched row into a dictionary
        customer = {
            "customer_id": row[0],
            "customer_name": row[1],
            "phone": row[2],
            "email": row[3],
            "status": row[4]
        }

        return {
            "success": True,
            "customer": customer
        }

    except sqlite3.Error as db_error:
        # Handle SQLite specific errors
        return {
            "success": False,
            "message": f"Database error: {db_error}"
        }

    except Exception as error:
        # Handle generic/unexpected errors
        return {
            "success": False,
            "message": f"An error occurred: {str(error)}"
        }

    finally:
        # Always close the database connection
        if connection:
            close_connection(connection)


def update_customer(customer_id: int, customer_name: str, phone: str, email: str, status: str) -> dict:
    """
    Updates an existing customer's information in the Saru POS database.

    Args:
        customer_id (int): The unique identifier of the customer to update.
        customer_name (str): The updated full name of the customer.
        phone (str): The updated contact phone number.
        email (str): The updated email address.
        status (str): The updated account status (e.g., 'active', 'inactive').

    Returns:
        dict: A dictionary containing a boolean 'success' flag and a descriptive 'message'.
    """
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Parameterized SQL query to prevent SQL injection
        update_query = """
            UPDATE customers
            SET customer_name = ?,
                phone = ?,
                email = ?,
                status = ?
            WHERE customer_id = ?
        """
        
        # Execute the update query with provided parameters
        cursor.execute(
            update_query, 
            (customer_name, phone, email, status, customer_id)
        )
        
        # Commit the transaction
        connection.commit()

        # Check if any rows were actually updated
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Customer not found."
            }

        return {
            "success": True,
            "message": "Customer updated successfully."
        }

    except sqlite3.Error as db_error:
        # Handle SQLite-specific exceptions
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }
        
    except Exception as error:
        # Handle any other generic exceptions
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }
        
    finally:
        # Ensure the database connection is always closed
        if connection is not None:
            close_connection(connection)

def delete_customer(customer_id: int) -> dict:
    """Deletes a customer record from the database by ID.

    Args:
        customer_id (int): The unique identifier of the customer to delete.

    Returns:
        dict: A dictionary containing the operational status ('success')
        and a descriptive message ('message').
    """
    connection = None
    try:
        # Establish connection to the SQLite database
        connection = get_connection()
        cursor = connection.cursor()

        # Parameterized query to prevent SQL injection vulnerabilities
        delete_query = "DELETE FROM customers WHERE customer_id = ?"
        cursor.execute(delete_query, (customer_id,))

        # Commit the deletion transaction
        connection.commit()

        # Check if a row was actually affected/deleted
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Customer not found."
            }

        return {
            "success": True,
            "message": "Customer deleted successfully."
        }

    except sqlite3.Error as db_error:
        # Revert changes on database failure
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"Database error occurred: {str(db_error)}"
        }

    except Exception as error:
        # Revert changes on unexpected application errors
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        # Guarantee resource cleanup regardless of success or failure
        if connection is not None:
            close_connection(connection)