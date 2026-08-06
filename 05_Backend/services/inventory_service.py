import sqlite3
from connection import get_connection, close_connection


def add_product(
    product_id: str,
    product_name: str,
    category_id: str,
    price: float,
    stock: int,
    status: str = "Active",
) -> dict:
    """Adds a new product record to the inventory database.

    Args:
        product_id (int): The unique identifier for the product.
        product_name (str): The display name of the product.
        category_id (int): Foreign key referencing the product category.
        price (float): Unit price of the product.
        stock (int): Initial available quantity in stock.
        status (str, optional): Account/item status. Defaults to "active".

    Returns:
        dict: A dictionary containing the operational status ('success')
            and a descriptive message ('message').
    """
    conn = None
    try:
        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Parameterized query to safely insert product details
        insert_query = """
            INSERT INTO inventory_items (product_id, product_name, category_id, price, stock, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(
            insert_query,
            (product_id, product_name, category_id, price, stock, status),
        )

        # Commit transaction to make changes permanent
        conn.commit()

        return {
            "success": True,
            "message": "Product added successfully."
        }

    except sqlite3.IntegrityError:
        # Handle unique constraint violations (e.g., duplicate product_id)
        if conn:
            conn.rollback()
        return {
            "success": False,
            "message": "Product ID already exists."
        }

    except sqlite3.Error as db_err:
        # Handle generic SQLite errors
        if conn:
            conn.rollback()
        return {
            "success": False,
            "message": f"Database error occurred: {str(db_err)}"
        }

    except Exception as e:
        # Handle unexpected application errors
        if conn:
            conn.rollback()
        return {
            "success": False,
            "message": f"An unexpected error occurred: {str(e)}"
        }

    finally:
        # Guarantee connection cleanup regardless of outcome
        if conn:
            close_connection(conn)


def get_all_products() -> dict:
    """Retrieves all product records from the inventory database.

    Returns:
        dict: A dictionary containing the operational status ('success')
            and either a list of product dictionaries ('products') or 
            a descriptive error/info message ('message').
    """
    connection = None
    try:
        # Establish connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Execute query to retrieve all products ordered alphabetically by name
        select_query = """
            SELECT
                product_id,
                product_name,
                category_id,
                price,
                stock,
                status
            FROM inventory_items
            ORDER BY product_name;
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()

        # Return a specific message if the table is empty
        if not rows:
            return {
                "success": False,
                "message": "No products found."
            }

        # Convert the fetched tuples into a list of dictionaries
        products = []
        for row in rows:
            products.append({
                "product_id": row[0],
                "product_name": row[1],
                "category_id": row[2],
                "price": row[3],
                "stock": row[4],
                "status": row[5]
            })

        return {
            "success": True,
            "products": products
        }

    except sqlite3.Error as db_error:
        # Handle SQLite-specific database errors
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        # Handle unexpected application errors
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        # Guarantee connection cleanup regardless of outcome
        if connection:
            close_connection(connection)


def get_product_by_id(product_id: int) -> dict:
    """Retrieves a single product record from the inventory database by ID.

    Args:
        product_id (int): The unique identifier of the product to retrieve.

    Returns:
        dict: A dictionary containing the operational status ('success')
            and either the product details dictionary ('product') or 
            a descriptive message ('message').
    """
    connection = None
    try:
        # Establish connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Execute parameterized query to retrieve the specific product
        select_query = """
            SELECT
                product_id,
                product_name,
                category_id,
                price,
                stock,
                status
            FROM inventory_items
            WHERE product_id = ?;
        """
        cursor.execute(select_query, (product_id,))
        row = cursor.fetchone()

        # Return error response if the record does not exist
        if not row:
            return {
                "success": False,
                "message": "Product not found."
            }

        # Format the retrieved row tuple as a dictionary
        product = {
            "product_id": row[0],
            "product_name": row[1],
            "category_id": row[2],
            "price": row[3],
            "stock": row[4],
            "status": row[5]
        }

        return {
            "success": True,
            "product": product
        }

    except sqlite3.Error as db_error:
        # Handle SQLite-specific database errors
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        # Handle unexpected application errors
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        # Guarantee connection cleanup regardless of outcome
        if connection is not None:
            close_connection(connection)

def update_product(
    product_id: int,
    product_name: str,
    category_id: int,
    price: float,
    stock: int,
    status: str
) -> dict:
    """Updates an existing product's information in the inventory database.

    Args:
        product_id (int): The unique identifier of the product to update.
        product_name (str): The updated display name of the product.
        category_id (int): The updated foreign key referencing the product category.
        price (float): The updated unit price of the product.
        stock (int): The updated available stock quantity.
        status (str): The updated status of the product (e.g., 'active', 'inactive').

    Returns:
        dict: A dictionary containing a boolean 'success' flag and a descriptive 'message'.
    """
    connection = None
    try:
        # Establish connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Parameterized SQL query to safely update product details and prevent SQL injection
        update_query = """
            UPDATE inventory_items
            SET 
                product_name = ?,
                category_id = ?,
                price = ?,
                stock = ?,
                status = ?
            WHERE product_id = ?;
        """
        
        # Execute the update query with the provided parameters
        cursor.execute(
            update_query, 
            (product_name, category_id, price, stock, status, product_id)
        )
        
        # Commit the transaction to apply changes
        connection.commit()

        # Check if any rows were actually modified (product exists)
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Product not found."
            }

        return {
            "success": True,
            "message": "Product updated successfully."
        }

    except sqlite3.Error as db_error:
        # Rollback transaction on SQLite-specific database errors
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }
        
    except Exception as error:
        # Rollback transaction on unexpected application errors
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }
        
    finally:
        # Guarantee connection cleanup regardless of outcome
        if connection:
            close_connection(connection)


def delete_product(product_id: int) -> dict:
    """Deletes a product record from the inventory database by ID.

    Args:
        product_id (int): The unique identifier of the product to delete.

    Returns:
        dict: A dictionary containing the operational status ('success')
            and a descriptive message ('message').
    """
    connection = None
    try:
        # Establish connection to the database
        connection = get_connection()
        cursor = connection.cursor()

        # Parameterized query to safely delete product details and prevent SQL injection
        delete_query = """
            DELETE FROM inventory_items
            WHERE product_id = ?;
        """

        # Execute deletion query
        cursor.execute(delete_query, (product_id,))

        # Commit transaction to finalize changes
        connection.commit()

        # Check if any row was actually affected/deleted
        if cursor.rowcount == 0:
            return {
                "success": False,
                "message": "Product not found."
            }

        return {
            "success": True,
            "message": "Product deleted successfully."
        }

    except sqlite3.Error as db_error:
        # Rollback transaction on SQLite-specific database errors
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"Database error occurred: {db_error}"
        }

    except Exception as error:
        # Rollback transaction on unexpected application errors
        if connection:
            connection.rollback()
        return {
            "success": False,
            "message": f"An unexpected error occurred: {error}"
        }

    finally:
        # Guarantee resource cleanup regardless of outcome
        if connection:
            close_connection(connection)


