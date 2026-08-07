import sqlite3
from connection import get_connection, close_connection

def add_category(
    category_id: str,
    category_name: str,
    description: str,
    status: str
) -> dict:
    """Adds a new category to the database.

    Args:
        category_id (str): The unique identifier for the category.
        category_name (str): The name of the category.
        description (str): A brief description of the category.
        status (str): The category status (Active or Inactive).

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Insert category
        insert_query = """
            INSERT INTO categories (
                category_id,
                category_name,
                description,
                status
            )
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(
            insert_query,
            (
                category_id,
                category_name,
                description,
                status
            )
        )

        connection.commit()

        return {
            "success": True,
            "message": "Category added successfully."
        }

    except sqlite3.IntegrityError:
        if connection:
            connection.rollback()

        return {
            "success": False,
            "message": "Category with this ID or name already exists."
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

def get_all_categories() -> dict:
    """Retrieves all categories from the database.

    Returns:
        dict: A dictionary containing the operation status and either
        a list of categories or a descriptive message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve all categories
        select_query = """
            SELECT
                category_id,
                category_name,
                description,
                status
            FROM categories
            ORDER BY category_name
        """

        cursor.execute(select_query)
        rows = cursor.fetchall()

        if not rows:
            return {
                "success": False,
                "message": "No categories found."
            }

        categories = []

        for row in rows:
            categories.append({
                "category_id": row["category_id"],
                "category_name": row["category_name"],
                "description": row["description"],
                "status": row["status"]
            })

        return {
            "success": True,
            "categories": categories
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

def get_category_by_id(category_id: str) -> dict:
    """Retrieves a category from the database by its ID.

    Args:
        category_id (str): The unique identifier for the category.

    Returns:
        dict: A dictionary containing the operation status and either
        the category details or a descriptive message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Retrieve category by ID
        select_query = """
            SELECT
                category_id,
                category_name,
                description,
                status
            FROM categories
            WHERE category_id = ?
        """

        cursor.execute(select_query, (category_id,))
        row = cursor.fetchone()

        if not row:
            return {
                "success": False,
                "message": "Category not found."
            }

        return {
            "success": True,
            "category": {
                "category_id": row["category_id"],
                "category_name": row["category_name"],
                "description": row["description"],
                "status": row["status"]
            }
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

def update_category(
    category_id: str,
    category_name: str,
    description: str,
    status: str
) -> dict:
    """Updates an existing category in the database.

    Args:
        category_id (str): The unique identifier of the category.
        category_name (str): The updated category name.
        description (str): The updated category description.
        status (str): The updated category status.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Update category
        update_query = """
            UPDATE categories
            SET
                category_name = ?,
                description = ?,
                status = ?
            WHERE category_id = ?;
        """

        cursor.execute(
            update_query,
            (
                category_name,
                description,
                status,
                category_id
            )
        )

        connection.commit()

        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Category not found."
            }

        return {
            "success": True,
            "message": "Category updated successfully."
        }

    except sqlite3.Error as db_error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)

def delete_category(category_id: str) -> dict:
    """Deletes a category from the database by its ID.

    Args:
        category_id (str): The unique identifier of the category.

    Returns:
        dict: A dictionary containing the operation status and message.
    """
    connection = None

    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # Delete category
        delete_query = """
            DELETE FROM categories
            WHERE category_id = ?;
        """

        cursor.execute(delete_query, (category_id,))
        connection.commit()

        # Check whether a category was deleted
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Category not found."
            }

        return {
            "success": True,
            "message": "Category deleted successfully."
        }

    except sqlite3.Error as db_error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        if connection is not None:
            connection.rollback()

        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        if connection is not None:
            close_connection(connection)