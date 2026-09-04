import sqlite3
import sys
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parents[1] / "05_Backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

import pytest


@pytest.fixture
def isolated_db(tmp_path, monkeypatch):
    db = tmp_path / "restaurant_pos.db"
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript("""
        CREATE TABLE customers (customer_id TEXT PRIMARY KEY, customer_name TEXT NOT NULL, phone TEXT UNIQUE, email TEXT, status TEXT NOT NULL);
        CREATE TABLE employees (employee_id TEXT PRIMARY KEY, full_name TEXT NOT NULL, phone TEXT UNIQUE, email TEXT UNIQUE, designation TEXT, address TEXT, role TEXT NOT NULL, hire_date TEXT, salary REAL, status TEXT NOT NULL);
        CREATE TABLE restaurant_tables (table_id TEXT PRIMARY KEY, table_number TEXT UNIQUE NOT NULL, capacity INTEGER NOT NULL, status TEXT NOT NULL);
        CREATE TABLE categories (category_id TEXT PRIMARY KEY, category_name TEXT UNIQUE NOT NULL, description TEXT, status TEXT NOT NULL);
        CREATE TABLE menu_items (menu_item_id TEXT PRIMARY KEY, category_id TEXT NOT NULL, item_name TEXT NOT NULL, price REAL NOT NULL, description TEXT, availability TEXT NOT NULL, FOREIGN KEY(category_id) REFERENCES categories(category_id));
        CREATE TABLE settings (setting_id TEXT PRIMARY KEY, restaurant_name TEXT NOT NULL, gst_number TEXT, address TEXT, phone TEXT, email TEXT, currency TEXT NOT NULL, tax_percentage REAL NOT NULL);
        CREATE TABLE bills (bill_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, employee_id TEXT NOT NULL, table_id TEXT NOT NULL, invoice_number TEXT UNIQUE NOT NULL, bill_date TEXT NOT NULL, total_amount REAL NOT NULL, status TEXT NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(customer_id), FOREIGN KEY(employee_id) REFERENCES employees(employee_id), FOREIGN KEY(table_id) REFERENCES restaurant_tables(table_id));
        CREATE TABLE bill_items (bill_item_id TEXT PRIMARY KEY, bill_id TEXT NOT NULL, menu_item_id TEXT NOT NULL, quantity INTEGER NOT NULL, unit_price REAL NOT NULL, subtotal REAL NOT NULL, FOREIGN KEY(bill_id) REFERENCES bills(bill_id), FOREIGN KEY(menu_item_id) REFERENCES menu_items(menu_item_id));
        CREATE TABLE payments (payment_id TEXT PRIMARY KEY, bill_id TEXT UNIQUE NOT NULL, payment_method TEXT NOT NULL, payment_status TEXT NOT NULL, payment_date TEXT, paid_amount REAL NOT NULL, FOREIGN KEY(bill_id) REFERENCES bills(bill_id));
    """)
    conn.execute("INSERT INTO customers VALUES ('C1','Customer','9000000000',NULL,'Active')")
    conn.execute("INSERT INTO employees VALUES ('E1','Employee','9000000001',NULL,NULL,NULL,'Staff',NULL,NULL,'Active')")
    conn.execute("INSERT INTO restaurant_tables VALUES ('T1','T1',4,'Available')")
    conn.execute("INSERT INTO categories VALUES ('CAT1','Food',NULL,'Active')")
    conn.execute("INSERT INTO menu_items VALUES ('M1','CAT1','Rice',100,NULL,'Available')")
    conn.execute("INSERT INTO settings VALUES ('S1','Test',NULL,NULL,NULL,NULL,'INR',5)")
    conn.commit(); conn.close()

    import connection
    monkeypatch.setattr(connection, "DATABASE_PATH", Path(db))
    return db


def test_checkout_is_atomic_and_calculates_total(isolated_db):
    from services.billing_service import create_checkout

    result = create_checkout('C1', 'E1', 'T1', 'INV-TEST-1', '2026-09-03', 'Cash', [
        {'menu_item_id': 'M1', 'quantity': 2},
    ])
    assert result['success'] is True
    assert result['bill']['subtotal'] == 200.0
    assert result['bill']['tax_amount'] == 10.0
    assert result['bill']['total_amount'] == 210.0

    conn = sqlite3.connect(isolated_db)
    assert conn.execute('SELECT COUNT(*) FROM bills').fetchone()[0] == 1
    assert conn.execute('SELECT COUNT(*) FROM bill_items').fetchone()[0] == 1
    assert conn.execute('SELECT COUNT(*) FROM payments').fetchone()[0] == 1
    conn.close()


def test_checkout_rejects_unavailable_item_without_writes(isolated_db):
    from services.billing_service import create_checkout

    result = create_checkout('C1', 'E1', 'T1', 'INV-TEST-2', '2026-09-03', 'Cash', [
        {'menu_item_id': 'DOES-NOT-EXIST', 'quantity': 1},
    ])
    assert result['success'] is False

    conn = sqlite3.connect(isolated_db)
    assert conn.execute('SELECT COUNT(*) FROM bills').fetchone()[0] == 0
    assert conn.execute('SELECT COUNT(*) FROM bill_items').fetchone()[0] == 0
    assert conn.execute('SELECT COUNT(*) FROM payments').fetchone()[0] == 0
    conn.close()
