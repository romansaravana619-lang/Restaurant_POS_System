import requests


BASE_URL = "http://127.0.0.1:5000"


def test_user_crud():
    employee_id = "TEST_EMP_USER_001"
    user_id = "TEST_USER_001"

    # 1. Create temporary employee
    employee_response = requests.post(
        f"{BASE_URL}/employees",
        json={
            "employee_id": employee_id,
            "full_name": "User Test Employee",
            "phone": "9876500011",
            "email": "usertestemployee@example.com",
            "designation": "Test Staff",
            "address": "Test Address",
            "role": "Staff",
            "hire_date": "2026-08-10",
            "salary": 25000.0,
            "status": "Active"
        }
    )

    assert employee_response.status_code == 201
    assert employee_response.json()["success"] is True

    # 2. Create User
    create_response = requests.post(
        f"{BASE_URL}/users",
        json={
            "user_id": user_id,
            "employee_id": employee_id,
            "username": "testuser_001",
            "password": "TestPassword@123",
            "role": "Staff",
            "status": "Active"
        }
    )

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 3. Get User
    get_response = requests.get(
        f"{BASE_URL}/users/{user_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True

    user = get_response.json()["user"]

    assert user["user_id"] == user_id
    assert user["employee_id"] == employee_id
    assert user["username"] == "testuser_001"

    # Password must not be stored as plaintext
    assert user["password"] != "TestPassword@123"

    # 4. Update User
    update_response = requests.put(
        f"{BASE_URL}/users/{user_id}",
        json={
            "employee_id": employee_id,
            "username": "updated_testuser_001",
            "password": "UpdatedPassword@123",
            "role": "Manager",
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 5. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/users/{user_id}"
    )

    assert verify_response.status_code == 200

    updated_user = verify_response.json()["user"]

    assert updated_user["username"] == "updated_testuser_001"
    assert updated_user["role"] == "Manager"
    assert updated_user["status"] == "Active"
    assert updated_user["employee_id"] == employee_id

    # Updated password must also be hashed
    assert updated_user["password"] != "UpdatedPassword@123"

    # 6. Delete User
    delete_response = requests.delete(
        f"{BASE_URL}/users/{user_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 7. Verify User Deleted
    deleted_response = requests.get(
        f"{BASE_URL}/users/{user_id}"
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False

    # 8. Cleanup temporary employee
    cleanup_employee = requests.delete(
        f"{BASE_URL}/employees/{employee_id}"
    )

    assert cleanup_employee.status_code == 200
    assert cleanup_employee.json()["success"] is True