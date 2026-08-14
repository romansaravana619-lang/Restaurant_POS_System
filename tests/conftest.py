import pytest
import requests


BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture
def auth_headers():
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": "admin",
            "password": "admin123",
        },
    )

    assert response.status_code == 200
    assert response.json()["success"] is True

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }