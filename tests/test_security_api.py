import requests

BASE_URL = "http://127.0.0.1:5000"


def test_protected_endpoint_requires_authentication():
    response = requests.post(
        f"{BASE_URL}/customers",
        json={
            "customer_id": "SECURITY_TEST_001",
            "customer_name": "Security Test Customer",
            "phone": "9876500000",
            "email": "securitytest@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 401
    assert response.json()["success"] is False

def test_protected_endpoint_rejects_invalid_token():
    response = requests.post(
        f"{BASE_URL}/customers",
        headers={
            "Authorization": "Bearer invalid-token-123"
        },
        json={
            "customer_id": "SECURITY_TEST_002",
            "customer_name": "Invalid Token Test",
            "phone": "9876500001",
            "email": "invalidtoken@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 401
    assert response.json()["success"] is False

def test_protected_endpoint_allows_valid_token(auth_headers):
    response = requests.post(
        f"{BASE_URL}/customers",
        headers=auth_headers,
        json={
            "customer_name": "Valid Token Test",
            "phone": "9876500102",
            "email": "validtoken@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 201
    assert response.json()["success"] is True
    customer_id = response.json()["customer_id"]
    assert customer_id.startswith("CUST")

    cleanup_response = requests.delete(
        f"{BASE_URL}/customers/{customer_id}",
        headers=auth_headers
    )

    assert cleanup_response.status_code == 200
    assert cleanup_response.json()["success"] is True

def test_protected_endpoint_rejects_malformed_authorization_header():
    response = requests.post(
        f"{BASE_URL}/customers",
        headers={
            "Authorization": "InvalidBearerToken"
        },
        json={
            "customer_id": "SECURITY_TEST_004",
            "customer_name": "Malformed Header Test",
            "phone": "9876500003",
            "email": "malformed@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 401
    assert response.json()["success"] is False

def test_protected_endpoint_rejects_tampered_token(auth_headers):
    valid_token = auth_headers["Authorization"].replace("Bearer ", "")

    # Modify a meaningful character inside the JWT signature
    tampered_token = (
        valid_token[:-10]
        + ("A" if valid_token[-10] != "A" else "B")
        + valid_token[-9:]
    )

    response = requests.post(
        f"{BASE_URL}/customers",
        headers={
            "Authorization": f"Bearer {tampered_token}"
        },
        json={
            "customer_id": "SECURITY_TEST_005",
            "customer_name": "Tampered Token Test",
            "phone": "9876500004",
            "email": "tampered@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 401
    assert response.json()["success"] is False

def test_protected_get_endpoint_requires_authentication():
    response = requests.get(
        f"{BASE_URL}/customers"
    )

    assert response.status_code == 401
    assert response.json()["success"] is False

def test_protected_update_endpoint_requires_authentication():
    response = requests.put(
        f"{BASE_URL}/customers/SECURITY_TEST_001",
        json={
            "customer_name": "Unauthorized Update",
            "phone": "9876500010",
            "email": "unauthorized@example.com",
            "status": "Active"
        }
    )

    assert response.status_code == 401
    assert response.json()["success"] is False


def test_protected_delete_endpoint_requires_authentication():
    response = requests.delete(
        f"{BASE_URL}/customers/SECURITY_TEST_001"
    )

    assert response.status_code == 401
    assert response.json()["success"] is False