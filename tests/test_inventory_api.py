import requests


BASE_URL = "http://127.0.0.1:5000"


def test_inventory_crud():
    supplier_id = "TEST_SUP_INV_001"
    inventory_id = "TEST_INV_001"

    # 1. Create temporary supplier
    supplier_response = requests.post(
        f"{BASE_URL}/suppliers",
        json={
            "supplier_id": supplier_id,
            "supplier_name": "Inventory Test Supplier",
            "contact_person": "Inventory Test Contact",
            "phone": "9876543210",
            "email": "inventorysupplier@example.com",
            "address": "Coimbatore",
            "status": "Active"
        }
    )

    assert supplier_response.status_code == 201
    assert supplier_response.json()["success"] is True

    # 2. Create inventory item
    create_response = requests.post(
        f"{BASE_URL}/inventory-items",
        json={
            "inventory_id": inventory_id,
            "supplier_id": supplier_id,
            "item_name": "Test Rice",
            "unit": "kg",
            "quantity": 50,
            "unit_cost": 60.0,
            "reorder_level": 10,
            "status": "Active"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 3. Get inventory item
    get_response = requests.get(
        f"{BASE_URL}/inventory-items/{inventory_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["inventory_item"]["inventory_id"] == inventory_id

    # 4. Update inventory item
    update_response = requests.put(
        f"{BASE_URL}/inventory-items/{inventory_id}",
        json={
            "supplier_id": supplier_id,
            "item_name": "Updated Test Rice",
            "unit": "kg",
            "quantity": 100,
            "unit_cost": 65.0,
            "reorder_level": 20,
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 5. Verify update
    verify_response = requests.get(
        f"{BASE_URL}/inventory-items/{inventory_id}"
    )

    assert verify_response.status_code == 200

    updated_item = verify_response.json()["inventory_item"]

    assert updated_item["item_name"] == "Updated Test Rice"
    assert updated_item["quantity"] == 100
    assert updated_item["unit_cost"] == 65.0

    # 6. Delete inventory item
    delete_response = requests.delete(
        f"{BASE_URL}/inventory-items/{inventory_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 7. Verify inventory item deleted
    deleted_response = requests.get(
        f"{BASE_URL}/inventory-items/{inventory_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False

    # 8. Delete temporary supplier
    cleanup_response = requests.delete(
        f"{BASE_URL}/suppliers/{supplier_id}"
    )

    assert cleanup_response.status_code == 200
    assert cleanup_response.json()["success"] is True