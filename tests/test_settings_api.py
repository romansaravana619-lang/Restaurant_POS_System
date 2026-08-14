import requests

BASE_URL = "http://127.0.0.1:5000"


def test_settings_crud(auth_headers):
    setting_id = "TEST_SETTING_001"

    try:
        # 1. Create Settings
        create_response = requests.post(
            f"{BASE_URL}/settings",
            headers=auth_headers,
            json={
                "setting_id": setting_id,
                "restaurant_name": "Test Restaurant",
                "gst_number": "TESTGST001",
                "address": "Test Address",
                "phone": "9876500022",
                "email": "testsettings@example.com",
                "currency": "INR",
                "tax_percentage": 5.0
            }
        )

        print("SETTINGS STATUS:", create_response.status_code)
        print("SETTINGS BODY:", create_response.text)

        assert create_response.status_code == 201
        assert create_response.json()["success"] is True

        # 2. Get Settings
        get_response = requests.get(
            f"{BASE_URL}/settings/{setting_id}",
            headers=auth_headers
        )

        assert get_response.status_code == 200
        assert get_response.json()["success"] is True

        setting = get_response.json()["setting"]

        assert setting["setting_id"] == setting_id
        assert setting["restaurant_name"] == "Test Restaurant"
        assert setting["currency"] == "INR"
        assert setting["tax_percentage"] == 5.0

        # 3. Update Settings
        update_response = requests.put(
            f"{BASE_URL}/settings/{setting_id}",
            headers=auth_headers,
            json={
                "restaurant_name": "Updated Test Restaurant",
                "gst_number": "UPDATEDGST001",
                "address": "Updated Test Address",
                "phone": "9876500033",
                "email": "updatedsettings@example.com",
                "currency": "USD",
                "tax_percentage": 12.0
            }
        )

        assert update_response.status_code == 200
        assert update_response.json()["success"] is True

        # 4. Verify Update
        verify_response = requests.get(
            f"{BASE_URL}/settings/{setting_id}",
            headers=auth_headers
        )

        assert verify_response.status_code == 200

        updated_setting = verify_response.json()["setting"]

        assert updated_setting["restaurant_name"] == "Updated Test Restaurant"
        assert updated_setting["gst_number"] == "UPDATEDGST001"
        assert updated_setting["currency"] == "USD"
        assert updated_setting["tax_percentage"] == 12.0

        # 5. Delete Settings
        delete_response = requests.delete(
            f"{BASE_URL}/settings/{setting_id}",
            headers=auth_headers
        )

        assert delete_response.status_code == 200
        assert delete_response.json()["success"] is True

        # 6. Verify Delete
        deleted_response = requests.get(
            f"{BASE_URL}/settings/{setting_id}",
            headers=auth_headers
        )

        assert deleted_response.status_code == 404
        assert deleted_response.json()["success"] is False

    finally:
        # Cleanup leftover test setting if test fails midway
        try:
            requests.delete(
                f"{BASE_URL}/settings/{setting_id}",
                headers=auth_headers
            )
        except Exception:
            pass