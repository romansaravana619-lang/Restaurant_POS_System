import requests


BASE_URL = "http://127.0.0.1:5000"


def test_payment_crud():
    customer_id = "TEST_CUST_PAY_001"
    table_id = "TEST_TABLE_PAY_001"
    bill_id = "TEST_BILL_PAY_001"
    payment_id = "TEST_PAYMENT_001"

    employee_id = "EMP001"

    # 1. Create temporary customer
    customer_response = requests.post(
        f"{BASE_URL}/customers",
        json={
            "customer_id": customer_id,
            "customer_name": "Payment Test Customer",
            "phone": "9876543210",
            "email": "paymenttest@example.com",
            "status": "Active"
        }
    )

    assert customer_response.status_code == 201
    assert customer_response.json()["success"] is True

    # 2. Create temporary restaurant table
    table_response = requests.post(
        f"{BASE_URL}/restaurant-tables",
        json={
            "table_id": table_id,
            "table_number": "PAY-TEST-01",
            "capacity": 4,
            "status": "Available"
        }
    )

    assert table_response.status_code == 201
    assert table_response.json()["success"] is True

    # 3. Create temporary bill
    bill_response = requests.post(
        f"{BASE_URL}/bills",
        json={
            "bill_id": bill_id,
            "customer_id": customer_id,
            "employee_id": employee_id,
            "table_id": table_id,
            "invoice_number": "PAY-TEST-INV-001",
            "bill_date": "2026-08-10",
            "total_amount": 500.0,
            "status": "Pending"
        }
    )

    assert bill_response.status_code == 201
    assert bill_response.json()["success"] is True

    # 4. Create payment
    create_response = requests.post(
        f"{BASE_URL}/payments",
        json={
            "payment_id": payment_id,
            "bill_id": bill_id,
            "payment_method": "Cash",
            "payment_status": "Pending",
            "payment_date": "2026-08-10",
            "paid_amount": 500.0
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 5. Get payment
    get_response = requests.get(
        f"{BASE_URL}/payments/{payment_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["payment"]["payment_id"] == payment_id

    # 6. Update payment
    update_response = requests.put(
        f"{BASE_URL}/payments/{payment_id}",
        json={
            "bill_id": bill_id,
            "payment_method": "UPI",
            "payment_status": "Completed",
            "payment_date": "2026-08-10",
            "paid_amount": 500.0
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 7. Verify update
    verify_response = requests.get(
        f"{BASE_URL}/payments/{payment_id}"
    )

    assert verify_response.status_code == 200

    updated_payment = verify_response.json()["payment"]

    assert updated_payment["payment_method"] == "UPI"
    assert updated_payment["payment_status"] == "Completed"
    assert updated_payment["paid_amount"] == 500.0

    # 8. Delete payment
    delete_response = requests.delete(
        f"{BASE_URL}/payments/{payment_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 9. Verify payment deleted
    deleted_response = requests.get(
        f"{BASE_URL}/payments/{payment_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False

    # 10. Cleanup bill
    cleanup_bill = requests.delete(
        f"{BASE_URL}/bills/{bill_id}"
    )

    assert cleanup_bill.status_code == 200
    assert cleanup_bill.json()["success"] is True

    # 11. Cleanup customer
    cleanup_customer = requests.delete(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert cleanup_customer.status_code == 200
    assert cleanup_customer.json()["success"] is True

    # 12. Cleanup restaurant table
    cleanup_table = requests.delete(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert cleanup_table.status_code == 200
    assert cleanup_table.json()["success"] is True