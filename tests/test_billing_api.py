import requests

BASE_URL = "http://127.0.0.1:5000"


def test_billing_crud(auth_headers):
    customer_id = "TEST_CUST_BILL_001"
    table_id = "TEST_TABLE_BILL_001"
    bill_id = "TEST_BILL_001"
    invoice_number = "TEST-INV-001"

    # Existing seeded employee
    employee_id = "EMP001"

    try:
        # 1. Create temporary customer
        customer_response = requests.post(
            f"{BASE_URL}/customers",
            headers=auth_headers,
            json={
                "customer_id": customer_id,
                "customer_name": "Billing Test Customer",
                "phone": "9876543210",
                "email": "billingtest@example.com",
                "status": "Active"
            }
        )

        assert customer_response.status_code == 201
        assert customer_response.json()["success"] is True

        # 2. Create temporary restaurant table
        table_response = requests.post(
            f"{BASE_URL}/restaurant-tables",
            headers=auth_headers,
            json={
                "table_id": table_id,
                "table_number": "B-TEST-01",
                "capacity": 4,
                "status": "Available"
            }
        )

        assert table_response.status_code == 201
        assert table_response.json()["success"] is True

        # 3. Create bill
        create_response = requests.post(
            f"{BASE_URL}/bills",
            headers=auth_headers,
            json={
                "bill_id": bill_id,
                "customer_id": customer_id,
                "employee_id": employee_id,
                "table_id": table_id,
                "invoice_number": invoice_number,
                "bill_date": "2026-08-10",
                "total_amount": 500.00,
                "status": "Pending"
            }
        )

        assert create_response.status_code == 201
        assert create_response.json()["success"] is True

        # 4. Get bill
        get_response = requests.get(
            f"{BASE_URL}/bills/{bill_id}",
            headers=auth_headers
        )

        assert get_response.status_code == 200
        assert get_response.json()["success"] is True
        assert get_response.json()["bill"]["bill_id"] == bill_id

        # 5. Update bill
        update_response = requests.put(
            f"{BASE_URL}/bills/{bill_id}",
            headers=auth_headers,
            json={
                "customer_id": customer_id,
                "employee_id": employee_id,
                "table_id": table_id,
                "invoice_number": invoice_number,
                "bill_date": "2026-08-10",
                "total_amount": 750.00,
                "status": "Paid"
            }
        )

        assert update_response.status_code == 200
        assert update_response.json()["success"] is True

        # 6. Verify update
        verify_response = requests.get(
            f"{BASE_URL}/bills/{bill_id}",
            headers=auth_headers
        )

        assert verify_response.status_code == 200

        updated_bill = verify_response.json()["bill"]

        assert updated_bill["total_amount"] == 750.00
        assert updated_bill["status"] == "Paid"

        # 7. Delete bill
        delete_response = requests.delete(
            f"{BASE_URL}/bills/{bill_id}",
            headers=auth_headers
        )

        assert delete_response.status_code == 200
        assert delete_response.json()["success"] is True

        # 8. Verify bill deleted
        deleted_response = requests.get(
            f"{BASE_URL}/bills/{bill_id}",
            headers=auth_headers
        )

        assert deleted_response.status_code == 404
        assert deleted_response.json()["success"] is False

    finally:
        # Cleanup bill if test fails midway
        try:
            requests.delete(
                f"{BASE_URL}/bills/{bill_id}",
                headers=auth_headers
            )
        except Exception:
            pass

        # Cleanup temporary customer
        try:
            requests.delete(
                f"{BASE_URL}/customers/{customer_id}",
                headers=auth_headers
            )
        except Exception:
            pass

        # Cleanup temporary restaurant table
        try:
            requests.delete(
                f"{BASE_URL}/restaurant-tables/{table_id}",
                headers=auth_headers
            )
        except Exception:
            pass