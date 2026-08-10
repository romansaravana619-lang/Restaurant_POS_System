import requests


BASE_URL = "http://127.0.0.1:5000"


def test_customer_crud():
    customer_id = "TEST_CUS_001"

    # 1. Create Customer
    create_response = requests.post(
        f"{BASE_URL}/customers",
        json={
            "customer_id": customer_id,
            "customer_name": "Automated Test Customer",
            "phone": "9876543210",
            "email": "testcustomer@example.com",
            "status": "Active"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 2. Get Customer
    get_response = requests.get(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["customer"]["customer_id"] == customer_id

    # 3. Update Customer
    update_response = requests.put(
        f"{BASE_URL}/customers/{customer_id}",
        json={
            "customer_name": "Updated Test Customer",
            "phone": "9999999999",
            "email": "updated@example.com",
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 4. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert verify_response.status_code == 200

    updated_customer = verify_response.json()["customer"]

    assert updated_customer["customer_name"] == "Updated Test Customer"
    assert updated_customer["phone"] == "9999999999"

    # 5. Delete Customer
    delete_response = requests.delete(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 6. Verify Delete
    deleted_response = requests.get(
        f"{BASE_URL}/customers/{customer_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False