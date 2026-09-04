"""
Service layer for user management database operations.
Handles business logic and database interactions for the users table.
"""

import sqlite3

from argon2 import PasswordHasher

from connection import get_connection, close_connection


password_hasher = PasswordHasher()


def add_user(
    user_id: str,
    employee_id: str,
    username: str,
    password: str,
    role: str,
    status: str
) -> dict:
    """Adds a new user with an Argon2 password hash."""

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        hashed_password = password_hasher.hash(password)

        insert_query = """
            INSERT INTO users (
                user_id,
                employee_id,
                username,
                password,
                role,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                user_id,
                employee_id,
                username,
                hashed_password,
                role,
                status,
            ),
        )

        connection.commit()

        return {
            "success": True,
            "message": "User added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "User ID, employee ID, or username already exists."
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


def get_all_users() -> dict:
    """Retrieves all users from the database."""

    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                user_id,
                employee_id,
                username,
                role,
                status
            FROM users
            ORDER BY user_id ASC;
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No users found."
            }

        users_list = [dict(row) for row in rows]

        return {
            "success": True,
            "users": users_list
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


def get_user_by_id(user_id: str) -> dict:
    """Retrieves a user from the database by user ID."""

    connection = None

    try:
        connection = get_connection()
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        select_query = """
            SELECT
                user_id,
                employee_id,
                username,
                role,
                status
            FROM users
            WHERE user_id = ?;
        """

        cursor.execute(select_query, (user_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "User not found."
            }

        return {
            "success": True,
            "user": dict(row)
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


def update_user(
    user_id: str,
    employee_id: str,
    username: str,
    password: str,
    role: str,
    status: str
) -> dict:
    """Updates an existing user. Password is changed only when provided."""

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        if password and password.strip():
            hashed_password = password_hasher.hash(password)

            update_query = """
                UPDATE users
                SET
                    employee_id = ?,
                    username = ?,
                    password = ?,
                    role = ?,
                    status = ?
                WHERE user_id = ?;
            """

            params = (
                employee_id,
                username,
                hashed_password,
                role,
                status,
                user_id,
            )

        else:
            update_query = """
                UPDATE users
                SET
                    employee_id = ?,
                    username = ?,
                    role = ?,
                    status = ?
                WHERE user_id = ?;
            """

            params = (
                employee_id,
                username,
                role,
                status,
                user_id,
            )

        cursor.execute(update_query, params)

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "User not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "User updated successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Employee ID or username already exists."
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


def delete_user(user_id: str) -> dict:
    """Deletes a user from the database by user ID."""

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = """
            DELETE FROM users
            WHERE user_id = ?;
        """

        cursor.execute(delete_query, (user_id,))

        if cursor.rowcount == 0:
            connection.rollback()

            return {
                "success": False,
                "message": "User not found."
            }

        connection.commit()

        return {
            "success": True,
            "message": "User deleted successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "User cannot be deleted because it is referenced by existing records."
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