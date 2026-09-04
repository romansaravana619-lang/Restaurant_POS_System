import requests

BASE_URL = "http://127.0.0.1:5000"


def test_customer_crud(auth_headers):
    customer_id = None

    try:
        # 1. Create Customer
        create_response = requests.post(
            f"{BASE_URL}/customers",
            headers=auth_headers,
            json={
                "customer_name": "Automated Test Customer",
                "phone": "9876543211",
                "email": "testcustomer@example.com",
                "status": "Active"
            }
        )

        assert create_response.status_code == 201
        assert create_response.json()["success"] is True
        customer_id = create_response.json()["customer_id"]
        assert customer_id.startswith("CUST")

        # 2. Get Customer
        get_response = requests.get(
            f"{BASE_URL}/customers/{customer_id}",
            headers=auth_headers
        )

        assert get_response.status_code == 200
        assert get_response.json()["success"] is True
        assert get_response.json()["customer"]["customer_id"] == customer_id

        # 3. Update Customer
        update_response = requests.put(
            f"{BASE_URL}/customers/{customer_id}",
            headers=auth_headers,
            json={
                "customer_name": "Updated Test Customer",
                "phone": "9876543299",
                "email": "updated@example.com",
                "status": "Active"
            }
        )

        assert update_response.status_code == 200
        assert update_response.json()["success"] is True

        # 4. Verify Update
        verify_response = requests.get(
            f"{BASE_URL}/customers/{customer_id}",
            headers=auth_headers
        )

        assert verify_response.status_code == 200

        updated_customer = verify_response.json()["customer"]

        assert updated_customer["customer_name"] == "Updated Test Customer"
        assert updated_customer["phone"] == "9999999999"
        assert updated_customer["email"] == "updated@example.com"
        assert updated_customer["status"] == "Active"

        # 5. Delete Customer
        delete_response = requests.delete(
            f"{BASE_URL}/customers/{customer_id}",
            headers=auth_headers
        )

        assert delete_response.status_code == 200
        assert delete_response.json()["success"] is True

        # 6. Verify Delete
        deleted_response = requests.get(
            f"{BASE_URL}/customers/{customer_id}",
            headers=auth_headers
        )

        assert deleted_response.status_code == 404
        assert deleted_response.json()["success"] is False

    finally:
        # Cleanup customer if test fails midway
        try:
            requests.delete(
                f"{BASE_URL}/customers/{customer_id}",
                headers=auth_headers
            )
        except Exception:
            pass