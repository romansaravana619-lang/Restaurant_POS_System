import requests


BASE_URL = "http://127.0.0.1:5000"


def test_menu_item_crud():
    category_id = "TEST_CAT_MENU_001"
    menu_item_id = "TEST_MENU_001"

    # 1. Create temporary category
    category_response = requests.post(
        f"{BASE_URL}/categories",
        json={
            "category_id": category_id,
            "category_name": "Menu Test Category",
            "description": "Temporary category for menu item test",
            "status": "Active"
        }
    )

    assert category_response.status_code == 201
    assert category_response.json()["success"] is True

    # 2. Create menu item
    create_response = requests.post(
        f"{BASE_URL}/menu-items",
        json={
            "menu_item_id": menu_item_id,
            "category_id": category_id,
            "item_name": "Automated Test Fried Rice",
            "price": 150.0,
            "description": "Temporary menu item for automated testing",
            "availability": "Available"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 3. Get menu item
    get_response = requests.get(
        f"{BASE_URL}/menu-items/{menu_item_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["menu_item"]["menu_item_id"] == menu_item_id

    # 4. Update menu item
    update_response = requests.put(
        f"{BASE_URL}/menu-items/{menu_item_id}",
        json={
            "category_id": category_id,
            "item_name": "Updated Test Fried Rice",
            "price": 180.0,
            "description": "Updated automated test menu item",
            "availability": "Available"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 5. Verify update
    verify_response = requests.get(
        f"{BASE_URL}/menu-items/{menu_item_id}"
    )

    assert verify_response.status_code == 200

    updated_item = verify_response.json()["menu_item"]

    assert updated_item["item_name"] == "Updated Test Fried Rice"
    assert updated_item["price"] == 180.0
    assert updated_item["description"] == "Updated automated test menu item"

    # 6. Delete menu item
    delete_response = requests.delete(
        f"{BASE_URL}/menu-items/{menu_item_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 7. Verify menu item deleted
    deleted_response = requests.get(
        f"{BASE_URL}/menu-items/{menu_item_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False

    # 8. Delete temporary category
    cleanup_response = requests.delete(
        f"{BASE_URL}/categories/{category_id}"
    )

    assert cleanup_response.status_code == 200
    assert cleanup_response.json()["success"] is True