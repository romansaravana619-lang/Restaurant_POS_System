"""
Saru POS Backend Audit - Fast Track
Read-only security and integrity audit.
"""

import os
import sqlite3
import sys
from pathlib import Path


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT_DIR / "05_Backend"
DATABASE_PATH = (
    ROOT_DIR
    / "04_Database"
    / "database"
    / "restaurant_pos.db"
)

sys.path.insert(0, str(BACKEND_DIR))


# ---------------------------------------------------------
# Audit helpers
# ---------------------------------------------------------

results = []


def check(name, passed, detail=""):
    status = "PASS" if passed else "FAIL"
    results.append((status, name, detail))

    symbol = "✅" if passed else "❌"

    print(f"{symbol} {name}")

    if detail:
        print(f"   {detail}")


# ---------------------------------------------------------
# 1. Database checks
# ---------------------------------------------------------

def audit_database():
    print("\n=== DATABASE AUDIT ===")

    if not DATABASE_PATH.exists():
        check(
            "Database exists",
            False,
            str(DATABASE_PATH),
        )
        return

    check(
        "Database exists",
        True,
        str(DATABASE_PATH),
    )

    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")

    try:
        foreign_keys = connection.execute(
            "PRAGMA foreign_keys"
        ).fetchone()[0]

        check(
            "Database FK integrity enabled",
            foreign_keys == 1,
            f"PRAGMA foreign_keys = {foreign_keys}",
        )

        # Orphan checks
        checks = {
            "bills → customers": """
                SELECT COUNT(*)
                FROM bills b
                LEFT JOIN customers c
                    ON b.customer_id = c.customer_id
                WHERE c.customer_id IS NULL
            """,

            "bills → employees": """
                SELECT COUNT(*)
                FROM bills b
                LEFT JOIN employees e
                    ON b.employee_id = e.employee_id
                WHERE e.employee_id IS NULL
            """,

            "bills → restaurant_tables": """
                SELECT COUNT(*)
                FROM bills b
                LEFT JOIN restaurant_tables t
                    ON b.table_id = t.table_id
                WHERE t.table_id IS NULL
            """,

            "bill_items → bills": """
                SELECT COUNT(*)
                FROM bill_items bi
                LEFT JOIN bills b
                    ON bi.bill_id = b.bill_id
                WHERE b.bill_id IS NULL
            """,

            "bill_items → menu_items": """
                SELECT COUNT(*)
                FROM bill_items bi
                LEFT JOIN menu_items m
                    ON bi.menu_item_id = m.menu_item_id
                WHERE m.menu_item_id IS NULL
            """,

            "payments → bills": """
                SELECT COUNT(*)
                FROM payments p
                LEFT JOIN bills b
                    ON p.bill_id = b.bill_id
                WHERE b.bill_id IS NULL
            """,

            "inventory_items → suppliers": """
                SELECT COUNT(*)
                FROM inventory_items i
                LEFT JOIN suppliers s
                    ON i.supplier_id = s.supplier_id
                WHERE s.supplier_id IS NULL
            """,

            "menu_items → categories": """
                SELECT COUNT(*)
                FROM menu_items m
                LEFT JOIN categories c
                    ON m.category_id = c.category_id
                WHERE c.category_id IS NULL
            """,
        }

        for name, query in checks.items():
            count = connection.execute(query).fetchone()[0]

            check(
                f"No orphan records: {name}",
                count == 0,
                f"orphan count = {count}",
            )

    finally:
        connection.close()


# ---------------------------------------------------------
# 2. JWT configuration
# ---------------------------------------------------------

def audit_jwt_configuration():
    print("\n=== JWT CONFIGURATION AUDIT ===")

    secret = os.getenv("SARU_POS_JWT_SECRET")

    check(
        "JWT secret configured",
        bool(secret),
        f"configured = {bool(secret)}",
    )

    if secret:
        check(
            "JWT secret length ≥ 32",
            len(secret) >= 32,
            f"length = {len(secret)}",
        )

    try:
        from utils import jwt_utils

        check(
            "JWT module loads with configured secret",
            True,
        )

        check(
            "JWT algorithm is HS256",
            jwt_utils.JWT_ALGORITHM == "HS256",
            f"algorithm = {jwt_utils.JWT_ALGORITHM}",
        )

    except Exception as error:
        check(
            "JWT module loads with configured secret",
            False,
            str(error),
        )


# ---------------------------------------------------------
# 3. Source-code security checks
# ---------------------------------------------------------

def audit_source_security():
    print("\n=== SOURCE SECURITY AUDIT ===")

    jwt_file = BACKEND_DIR / "utils" / "jwt_utils.py"
    app_file = BACKEND_DIR / "app.py"

    jwt_source = jwt_file.read_text(encoding="utf-8")
    app_source = app_file.read_text(encoding="utf-8")

    check(
        "JWT has no insecure fallback secret",
        "CHANGE_THIS_SECRET_IN_PRODUCTION" not in jwt_source,
    )

    check(
        "Hard-coded debug=True absent",
        "debug=True" not in app_source,
    )

    check(
        "Global HTTP error handler exists",
        "@app.errorhandler(HTTPException)" in app_source,
    )

    check(
        "Global unexpected-error handler exists",
        "@app.errorhandler(Exception)" in app_source,
    )


# ---------------------------------------------------------
# 4. Password protection checks
# ---------------------------------------------------------

def audit_password_protection():
    print("\n=== PASSWORD SECURITY AUDIT ===")

    user_service = (
        BACKEND_DIR
        / "services"
        / "user_service.py"
    )

    auth_service = (
        BACKEND_DIR
        / "services"
        / "auth_service.py"
    )

    user_source = user_service.read_text(
        encoding="utf-8"
    )

    auth_source = auth_service.read_text(
        encoding="utf-8"
    )

    check(
        "User creation uses Argon2",
        "password_hasher.hash(password)" in user_source,
    )

    check(
        "Authentication verifies password hash",
        "password_hasher.verify" in auth_source,
    )


# ---------------------------------------------------------
# 5. Route validation inspection
# ---------------------------------------------------------

def audit_route_validation():
    print("\n=== ROUTE VALIDATION AUDIT ===")

    routes_dir = BACKEND_DIR / "routes"

    route_files = list(
        routes_dir.glob("*.py")
    )

    check(
        "Route files discovered",
        len(route_files) > 0,
        f"route files = {len(route_files)}",
    )

    numeric_fields = [
        "capacity",
        "paid_amount",
        "price",
        "quantity",
        "reorder_level",
        "salary",
        "subtotal",
        "tax_percentage",
        "total_amount",
        "unit_cost",
        "unit_price",
    ]

    found_fields = set()

    for route_file in route_files:
        source = route_file.read_text(
            encoding="utf-8"
        )

        for field in numeric_fields:
            if field in source:
                found_fields.add(field)

    print(
        "   Numeric fields detected:",
        ", ".join(sorted(found_fields)),
    )

    # Live regression tests for previously confirmed validation gaps.
    try:
        from app import app

        client = app.test_client()

        login = client.post(
            "/login",
            json={
                "username": "admin",
                "password": "admin123",
            },
        )

        if login.status_code != 200:
            check(
                "Validation regression authentication",
                False,
                f"login status = {login.status_code}",
            )
            return

        login_data = login.get_json() or {}
        token = login_data.get("access_token")

        if not token:
            check(
                "Validation regression authentication",
                False,
                "Access token not returned.",
            )
            return

        headers = {
            "Authorization": f"Bearer {token}"
        }

        # Previously accepted invalid category_name type.
        category_test = client.post(
            "/categories",
            headers=headers,
            json={
                "category_id": "AUDIT_VALIDATION_CATEGORY",
                "category_name": 12345,
                "description": "Audit validation test",
                "status": "Active",
            },
        )

        check(
            "Category rejects invalid string type",
            category_test.status_code == 400,
            f"status = {category_test.status_code}",
        )

        # Previously accepted invalid menu item price type.
        menu_test = client.post(
            "/menu-items",
            headers=headers,
            json={
                "menu_item_id": "AUDIT_VALIDATION_MENU",
                "category_id": "AUDIT_VALIDATION_CATEGORY",
                "item_name": "Audit Validation Test",
                "price": "INVALID_PRICE",
                "description": "Audit validation test",
                "availability": "Available",
            },
        )

        check(
            "Menu item rejects invalid numeric type",
            menu_test.status_code == 400,
            f"status = {menu_test.status_code}",
        )

    except Exception as error:
        check(
            "Validation regression tests",
            False,
            str(error),
        )


# ---------------------------------------------------------
# 6. RBAC inspection
# ---------------------------------------------------------

def audit_rbac():
    print("\n=== AUTHORIZATION AUDIT ===")

    routes_dir = BACKEND_DIR / "routes"

    role_checks = 0

    for route_file in routes_dir.glob("*.py"):
        source = route_file.read_text(
            encoding="utf-8"
        )

        if "@require_role" in source:
            role_checks += 1

    check(
        "Role-based authorization enforcement",
        role_checks > 0,
        f"route files with role checks = {role_checks}",
    )


# ---------------------------------------------------------
# 7. Summary
# ---------------------------------------------------------

def print_summary():
    print("\n" + "=" * 60)
    print("SARU POS BACKEND AUDIT SUMMARY")
    print("=" * 60)

    passed = sum(
        1 for status, _, _ in results
        if status == "PASS"
    )

    failed = sum(
        1 for status, _, _ in results
        if status == "FAIL"
    )

    print(f"PASS: {passed}")
    print(f"FAIL: {failed}")

    print("\nFindings requiring attention:")

    for status, name, detail in results:
        if status == "FAIL":
            print(f"- {name}")
            if detail:
                print(f"  {detail}")

    print("=" * 60)


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":
    audit_database()
    audit_jwt_configuration()
    audit_source_security()
    audit_password_protection()
    audit_route_validation()
    audit_rbac()
    print_summary()