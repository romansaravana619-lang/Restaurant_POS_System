"""
seed_data.py

Inserts default seed records into the Saru POS v1.0 database.
Uses connection utilities from connection.py.
Records are inserted only if they do not already exist (INSERT OR IGNORE).
"""

import sqlite3
from connection import get_connection, close_connection


def seed_default_data():
    """Insert default records into employees, users, categories, and settings tables."""
    connection = None
    try:
        # Establish database connection
        connection = get_connection()
        cursor = connection.cursor()

        # ------------------------------------------------------------
        # Seed default employee (Administrator)
        # ------------------------------------------------------------
        cursor.execute(
            """
            INSERT OR IGNORE INTO employees (
                employee_id, full_name, phone, email,
                role, hire_date, salary, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                "EMP001",
                "Administrator",
                "9999999999",
                "admin@sarupos.com",
                "Admin",
                "2026-01-01",
                50000,
                "Active",
            ),
        )

        # ------------------------------------------------------------
        # Seed default user (admin login)
        # ------------------------------------------------------------
        cursor.execute(
            """
            INSERT OR IGNORE INTO users (
                user_id, employee_id, username, password, role, status
            )
            VALUES (?, ?, ?, ?, ?, ?);
            """,
            (
                "USER001",
                "EMP001",
                "admin",
                "admin123",
                "Admin",
                "Active",
            ),
        )

        # ------------------------------------------------------------
        # Seed default categories
        # ------------------------------------------------------------
        categories = [
            ("CAT001", "Main Course", "Active"),
            ("CAT002", "Beverages", "Active"),
            ("CAT003", "Desserts", "Active"),
        ]
        cursor.executemany(
            """
            INSERT OR IGNORE INTO categories (
                category_id, category_name, status
            )
            VALUES (?, ?, ?);
            """,
            categories,
        )

        # ------------------------------------------------------------
        # Seed default restaurant settings
        # ------------------------------------------------------------
        cursor.execute(
            """
            INSERT OR IGNORE INTO settings (
                setting_id, restaurant_name, gst_number, address,
                phone, email, currency, tax_percentage
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """,
            (
                "SET001",
                "Saru POS Restaurant",
                "GST123456789",
                "Coimbatore",
                "9876543210",
                "admin@sarupos.com",
                "INR",
                5,
            ),
        )

        # Commit all seed data changes to the database
        connection.commit()

        print("✅ Seed data inserted successfully.")

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
    seed_default_data()