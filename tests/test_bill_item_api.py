import requests


BASE_URL = "http://127.0.0.1:5000"


def test_bill_item_crud():
    category_id = "TEST_CAT_BI_001"
    menu_item_id = "TEST_MENU_BI_001"
    customer_id = "TEST_CUST_BI_001"
    table_id = "TEST_TABLE_BI_001"
    bill_id = "TEST_BILL_BI_001"
    bill_item_id = "TEST_BILL_ITEM_001"

    employee_id = "EMP001"

    # 1. Create temporary category
    category_response = requests.post(
        f"{BASE_URL}/categories",
        json={
            "category_id": category_id,
            "category_name": "Bill Item Test Category",
            "description": "Temporary category for bill item test",
            "status": "Active"
        }
    )

    assert category_response.status_code == 201
    assert category_response.json()["success"] is True

    # 2. Create temporary menu item
    menu_response = requests.post(
        f"{BASE_URL}/menu-items",
        json={
            "menu_item_id": menu_item_id,
            "category_id": category_id,
            "item_name": "Bill Item Test Food",
            "price": 100.0,
            "description": "Temporary menu item",
            "availability": "Available"
        }
    )

    assert menu_response.status_code == 201
    assert menu_response.json()["success"] is True

    # 3. Create temporary customer
    customer_response = requests.post(
        f"{BASE_URL}/customers",
        json={
            "customer_id": customer_id,
            "customer_name": "Bill Item Test Customer",
            "phone": "9876543210",
            "email": "billitemtest@example.com",
            "status": "Active"
        }
    )

    assert customer_response.status_code == 201
    assert customer_response.json()["success"] is True

    # 4. Create temporary restaurant table
    table_response = requests.post(
        f"{BASE_URL}/restaurant-tables",
        json={
            "table_id": table_id,
            "table_number": "BI-TEST-01",
            "capacity": 4,
            "status": "Available"
        }
    )

    assert table_response.status_code == 201
    assert table_response.json()["success"] is True

    # 5. Create temporary bill
    bill_response = requests.post(
        f"{BASE_URL}/bills",
        json={
            "bill_id": bill_id,
            "customer_id": customer_id,
            "employee_id": employee_id,
            "table_id": table_id,
            "invoice_number": "BI-TEST-INV-001",
            "bill_date": "2026-08-10",
            "total_amount": 200.0,
            "status": "Pending"
        }
    )

    assert bill_response.status_code == 201
    assert bill_response.json()["success"] is True

    # 6. Create bill item
    create_response = requests.post(
        f"{BASE_URL}/bill-items",
        json={
            "bill_item_id": bill_item_id,
            "bill_id": bill_id,
            "menu_item_id": menu_item_id,
            "quantity": 2,
            "unit_price": 100.0,
            "subtotal": 200.0
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 7. Get bill item
    get_response = requests.get(
        f"{BASE_URL}/bill-items/{bill_item_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["bill_item"]["bill_item_id"] == bill_item_id

    # 8. Update bill item
    update_response = requests.put(
        f"{BASE_URL}/bill-items/{bill_item_id}",
        json={
            "bill_id": bill_id,
            "menu_item_id": menu_item_id,
            "quantity": 3,
            "unit_price": 120.0,
            "subtotal": 360.0
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 9. Verify update
    verify_response = requests.get(
        f"{BASE_URL}/bill-items/{bill_item_id}"
    )

    assert verify_response.status_code == 200

    updated_item = verify_response.json()["bill_item"]

    assert updated_item["quantity"] == 3
    assert updated_item["unit_price"] == 120.0
    assert updated_item["subtotal"] == 360.0

    # 10. Delete bill item
    delete_response = requests.delete(
        f"{BASE_URL}/bill-items/{bill_item_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 11. Verify bill item deleted
    deleted_response = requests.get(
        f"{BASE_URL}/bill-items/{bill_item_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False

    # 12. Cleanup bill
    cleanup_bill = requests.delete(
        f"{BASE_URL}/bills/{bill_id}"
    )

    assert cleanup_bill.status_code == 200
    assert cleanup_bill.json()["success"] is True

    # 13. Cleanup customer
    cleanup_customer = requests.delete(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert cleanup_customer.status_code == 200
    assert cleanup_customer.json()["success"] is True

    # 14. Cleanup restaurant table
    cleanup_table = requests.delete(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert cleanup_table.status_code == 200
    assert cleanup_table.json()["success"] is True

    # 15. Cleanup menu item
    cleanup_menu = requests.delete(
        f"{BASE_URL}/menu-items/{menu_item_id}"
    )

    assert cleanup_menu.status_code == 200
    assert cleanup_menu.json()["success"] is True

    # 16. Cleanup category
    cleanup_category = requests.delete(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert cleanup_category.status_code == 200
    assert cleanup_category.json()["success"] is True