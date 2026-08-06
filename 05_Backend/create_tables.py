"""
============================================================
Saru Systems
Saru POS v1.0
Database Table Creation Module
============================================================
"""

from dbm import error
import sqlite3
from connection import get_connection, close_connection


def create_users_table():
    """Create the users table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the users table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                employee_id TEXT UNIQUE,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT NOT NULL
            );
        """

        cursor.execute(create_table_query)
        connection.commit()

        print("✅ Users table created successfully.")

    except sqlite3.Error as db_error:
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    finally:
        if connection is not None:
            close_connection(connection)


def create_employees_table():
    """Create the employees table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the employees table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                phone TEXT UNIQUE,
                email TEXT UNIQUE,
                designation TEXT,
                address TEXT,
                role TEXT NOT NULL,
                hire_date TEXT,
                salary REAL,
                status TEXT NOT NULL
            );
        """

        cursor.execute(create_table_query)
        connection.commit()

        print("✅ Employees table created successfully.")

    except sqlite3.Error as db_error:
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    finally:
        if connection is not None:
            close_connection(connection)


def create_categories_table():
    """Create the categories table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the categories table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS categories (
                category_id TEXT PRIMARY KEY,
                category_name TEXT UNIQUE NOT NULL,
                description TEXT,
                status TEXT NOT NULL
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Categories table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_menu_items_table():
    """Create the menu_items table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the menu_items table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS menu_items (
                menu_item_id TEXT PRIMARY KEY,
                category_id TEXT NOT NULL,
                item_name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                availability TEXT NOT NULL,
                FOREIGN KEY (category_id)
                    REFERENCES categories(category_id)
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Menu items table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")
    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")
    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)

def create_customers_table():
    """Create the customers table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the customers table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                phone TEXT UNIQUE,
                email TEXT,
                status TEXT NOT NULL
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Customers table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_restaurant_tables_table():
    """Create the restaurant_tables table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the restaurant_tables table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS restaurant_tables (
                table_id TEXT PRIMARY KEY,
                table_number TEXT UNIQUE NOT NULL,
                capacity INTEGER NOT NULL,
                status TEXT NOT NULL
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Restaurant tables table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_bills_table():
    """Create the bills table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the bills table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS bills (
                bill_id TEXT PRIMARY KEY,
                customer_id TEXT NOT NULL,
                employee_id TEXT NOT NULL,
                table_id TEXT NOT NULL,
                invoice_number TEXT UNIQUE NOT NULL,
                bill_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
                FOREIGN KEY (table_id) REFERENCES restaurant_tables(table_id)
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Bills table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_bill_items_table():
    """Create the bill_items table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the bill_items table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS bill_items (
                bill_item_id TEXT PRIMARY KEY,
                bill_id TEXT NOT NULL,
                menu_item_id TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (bill_id) REFERENCES bills(bill_id),
                FOREIGN KEY (menu_item_id) REFERENCES menu_items(menu_item_id)
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Bill items table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_payments_table():
    """Create the payments table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the payments table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS payments (
                payment_id TEXT PRIMARY KEY,
                bill_id TEXT UNIQUE NOT NULL,
                payment_method TEXT NOT NULL,
                payment_status TEXT NOT NULL,
                payment_date TEXT,
                paid_amount REAL NOT NULL,
                FOREIGN KEY (bill_id) REFERENCES bills(bill_id)
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Payments table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)

def create_suppliers_table():
    """Create the suppliers table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the suppliers table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id TEXT PRIMARY KEY,
                supplier_name TEXT NOT NULL,
                contact_person TEXT,
                phone TEXT UNIQUE,
                email TEXT,
                address TEXT,
                status TEXT NOT NULL
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Suppliers table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_inventory_items_table():
    """Create the inventory_items table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the inventory_items table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS inventory_items (
                inventory_id TEXT PRIMARY KEY,
                supplier_id TEXT NOT NULL,
                item_name TEXT NOT NULL,
                unit TEXT NOT NULL,
                quantity REAL NOT NULL,
                unit_cost REAL NOT NULL,
                reorder_level REAL,
                status TEXT NOT NULL,
                FOREIGN KEY (supplier_id)
                    REFERENCES suppliers(supplier_id)
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Inventory items table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


def create_settings_table():
    """Create the settings table in the database if it does not already exist."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # SQL statement to create the settings table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS settings (
                setting_id TEXT PRIMARY KEY,
                restaurant_name TEXT NOT NULL,
                gst_number TEXT,
                address TEXT,
                phone TEXT,
                email TEXT,
                currency TEXT NOT NULL,
                tax_percentage REAL NOT NULL
            );
        """

        # Execute table creation query
        cursor.execute(create_table_query)

        # Commit changes to the database
        connection.commit()

        print("✅ Settings table created successfully.")

    except sqlite3.Error as db_error:
        # Handle database-related errors
        print(f"Database error occurred: {db_error}")

    except Exception as error:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {error}")

    finally:
        # Ensure connection is closed regardless of success or failure
        if connection is not None:
            close_connection(connection)


if __name__ == "__main__":
    create_users_table()
    create_employees_table()
    create_categories_table()
    create_menu_items_table()
    create_customers_table()
    create_restaurant_tables_table()
    create_bills_table()
    create_bill_items_table()
    create_payments_table()
    create_suppliers_table()
    create_inventory_items_table()
    create_settings_table()