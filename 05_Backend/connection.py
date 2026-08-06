"""
============================================================
Saru Systems
Saru POS v1.0
Database Connection Module
============================================================
"""

import sqlite3
from pathlib import Path

# Database Path
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR.parent / "04_Database" / "database" / "restaurant_pos.db"


def get_connection():
    """
    Creates and returns a SQLite database connection.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    # Enable dictionary-like row access
    connection.row_factory = sqlite3.Row

    return connection


def close_connection(connection):
    """
    Safely closes the database connection.
    """

    if connection:
        connection.close()