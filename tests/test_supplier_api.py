import requests


BASE_URL = "http://127.0.0.1:5000"


def test_supplier_crud():
    supplier_id = "TEST_SUP_001"

    # 1. Create Supplier
    create_response = requests.post(
        f"{BASE_URL}/suppliers",
        json={
            "supplier_id": supplier_id,
            "supplier_name": "Automated Test Supplier",
            "contact_person": "Test Contact",
            "phone": "9876543210",
            "email": "testsupplier@example.com",
            "address": "Coimbatore",
            "status": "Active"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 2. Get Supplier
    get_response = requests.get(
        f"{BASE_URL}/suppliers/{supplier_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["supplier"]["supplier_id"] == supplier_id

    # 3. Update Supplier
    update_response = requests.put(
        f"{BASE_URL}/suppliers/{supplier_id}",
        json={
            "supplier_name": "Updated Test Supplier",
            "contact_person": "Updated Contact",
            "phone": "9999999999",
            "email": "updatedsupplier@example.com",
            "address": "Updated Coimbatore",
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 4. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/suppliers/{supplier_id}"
    )

    assert verify_response.status_code == 200

    updated_supplier = verify_response.json()["supplier"]

    assert updated_supplier["supplier_name"] == "Updated Test Supplier"
    assert updated_supplier["phone"] == "9999999999"

    # 5. Delete Supplier
    delete_response = requests.delete(
        f"{BASE_URL}/suppliers/{supplier_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 6. Verify Delete
    deleted_response = requests.get(
        f"{BASE_URL}/suppliers/{supplier_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False