import requests


BASE_URL = "http://127.0.0.1:5000"


def test_restaurant_table_crud():
    table_id = "TEST_TABLE_001"

    # 1. Create Restaurant Table
    create_response = requests.post(
        f"{BASE_URL}/restaurant-tables",
        json={
            "table_id": table_id,
            "table_number": "T-TEST-01",
            "capacity": 4,
            "status": "Available"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 2. Get Restaurant Table
    get_response = requests.get(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["restaurant_table"]["table_id"] == table_id

    # 3. Update Restaurant Table
    update_response = requests.put(
        f"{BASE_URL}/restaurant-tables/{table_id}",
        json={
            "table_number": "T-TEST-01-UPDATED",
            "capacity": 6,
            "status": "Occupied"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 4. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert verify_response.status_code == 200

    updated_table = verify_response.json()["restaurant_table"]

    assert updated_table["table_number"] == "T-TEST-01-UPDATED"
    assert updated_table["capacity"] == 6
    assert updated_table["status"] == "Occupied"

    # 5. Delete Restaurant Table
    delete_response = requests.delete(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 6. Verify Delete
    deleted_response = requests.get(
        f"{BASE_URL}/restaurant-tables/{table_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False