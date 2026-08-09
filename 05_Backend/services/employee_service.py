"""
Service layer for employee-related database operations.
Handles business logic and database interactions for the employees table.
"""

import sqlite3

from connection import get_connection, close_connection


def add_employee(
    employee_id: str,
    full_name: str,
    phone: str,
    email: str,
    designation: str,
    address: str,
    role: str,
    hire_date: str,
    salary: float,
    status: str
) -> dict:
    """Adds a new employee to the database.

    Args:
        employee_id (str): The unique identifier for the employee.
        full_name (str): The full name of the employee.
        phone (str): The phone number of the employee.
        email (str): The email address of the employee.
        designation (str): The designation of the employee.
        address (str): The address of the employee.
        role (str): The role assigned to the employee.
        hire_date (str): The date the employee was hired.
        salary (float): The salary of the employee.
        status (str): The current status of the employee.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO employees (
                employee_id,
                full_name,
                phone,
                email,
                designation,
                address,
                role,
                hire_date,
                salary,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                employee_id,
                full_name,
                phone,
                email,
                designation,
                address,
                role,
                hire_date,
                salary,
                status,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "Employee added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Employee with this ID, phone, or email already exists."
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


def get_all_employees() -> dict:
    """Retrieves all employees from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        the employees list or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                employee_id,
                full_name,
                phone,
                email,
                designation,
                address,
                role,
                hire_date,
                salary,
                status
            FROM employees
            ORDER BY employee_id ASC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No employees found."
            }

        employees_list = [dict(row) for row in rows]

        return {
            "success": True,
            "employees": employees_list
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


def get_employee_by_id(employee_id: str) -> dict:
    """Retrieves an employee from the database by its ID.

    Args:
        employee_id (str): The unique identifier for the employee.

    Returns:
        dict: A dictionary containing the operation status and either
        the employee details or an error message.
    """
    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                employee_id,
                full_name,
                phone,
                email,
                designation,
                address,
                role,
                hire_date,
                salary,
                status
            FROM employees
            WHERE employee_id = ?;
        """

        cursor.execute(select_query, (employee_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Employee not found."
            }

        return {
            "success": True,
            "employee": dict(row)
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


def update_employee(
    employee_id: str,
    full_name: str,
    phone: str,
    email: str,
    designation: str,
    address: str,
    role: str,
    hire_date: str,
    salary: float,
    status: str
) -> dict:
    """Updates an existing employee in the database.

    Args:
        employee_id (str): The unique identifier for the employee.
        full_name (str): The full name of the employee.
        phone (str): The phone number of the employee.
        email (str): The email address of the employee.
        designation (str): The designation of the employee.
        address (str): The address of the employee.
        role (str): The role assigned to the employee.
        hire_date (str): The date the employee was hired.
        salary (float): The salary of the employee.
        status (str): The current status of the employee.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        update_query = """
            UPDATE employees
            SET
                full_name = ?,
                phone = ?,
                email = ?,
                designation = ?,
                address = ?,
                role = ?,
                hire_date = ?,
                salary = ?,
                status = ?
            WHERE employee_id = ?;
        """

        cursor.execute(
            update_query,
            (
                full_name,
                phone,
                email,
                designation,
                address,
                role,
                hire_date,
                salary,
                status,
                employee_id,
            ),
        )

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Employee not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Employee updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Employee with this phone or email already exists."
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


def delete_employee(employee_id: str) -> dict:
    """Deletes an employee from the database by its ID.

    Args:
        employee_id (str): The unique identifier for the employee.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM employees
            WHERE employee_id = ?;
        """

        cursor.execute(delete_query, (employee_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "Employee not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "Employee deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Employee cannot be deleted because it is referenced by existing records."
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