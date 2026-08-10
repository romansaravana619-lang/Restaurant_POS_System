import requests


BASE_URL = "http://127.0.0.1:5000"


def test_category_crud():
    category_id = "TEST_CAT_001"

    # 1. Create Category
    create_response = requests.post(
        f"{BASE_URL}/categories",
        json={
            "category_id": category_id,
            "category_name": "Automated Test Category",
            "description": "Category created by automated test",
            "status": "Active"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 2. Get Category
    get_response = requests.get(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["category"]["category_id"] == category_id

    # 3. Update Category
    update_response = requests.put(
        f"{BASE_URL}/categories/{category_id}",
        json={
            "category_name": "Updated Test Category",
            "description": "Updated category description",
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 4. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert verify_response.status_code == 200

    updated_category = verify_response.json()["category"]

    assert updated_category["category_name"] == "Updated Test Category"
    assert updated_category["description"] == "Updated category description"

    # 5. Delete Category
    delete_response = requests.delete(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 6. Verify Delete
    deleted_response = requests.get(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False