import requests

BASE_URL = "http://127.0.0.1:5000"


def test_auth_login(auth_headers):
    employee_id = "TEST_EMP_AUTH_001"
    user_id = "TEST_USER_AUTH_001"
    username = "testauth_001"
    password = "AuthPassword@123"

    try:
        # 1. Create temporary employee
        employee_response = requests.post(
            f"{BASE_URL}/employees",
            headers=auth_headers,
            json={
                "employee_id": employee_id,
                "full_name": "Auth Test Employee",
                "phone": "9876500044",
                "email": "authtestemployee@example.com",
                "designation": "Auth Test Staff",
                "address": "Test Address",
                "role": "Staff",
                "hire_date": "2026-08-10",
                "salary": 25000.0,
                "status": "Active"
            }
        )

        print("EMPLOYEE STATUS:", employee_response.status_code)
        print("EMPLOYEE BODY:", employee_response.text)

        assert employee_response.status_code == 201
        assert employee_response.json()["success"] is True

        # 2. Create temporary user
        user_response = requests.post(
            f"{BASE_URL}/users",
            headers=auth_headers,
            json={
                "user_id": user_id,
                "employee_id": employee_id,
                "username": username,
                "password": password,
                "role": "Staff",
                "status": "Active"
            }
        )

        print("USER STATUS:", user_response.status_code)
        print("USER BODY:", user_response.text)

        assert user_response.status_code == 201
        assert user_response.json()["success"] is True

        # 3. Valid login
        login_response = requests.post(
            f"{BASE_URL}/login",
            json={
                "username": username,
                "password": password
            }
        )

        assert login_response.status_code == 200
        assert login_response.json()["success"] is True

        authenticated_user = login_response.json()["user"]

        assert authenticated_user["user_id"] == user_id
        assert authenticated_user["username"] == username
        assert authenticated_user["role"] == "Staff"
        assert authenticated_user["status"] == "Active"

        # 4. Wrong password
        wrong_password_response = requests.post(
            f"{BASE_URL}/login",
            json={
                "username": username,
                "password": "WrongPassword@123"
            }
        )

        assert wrong_password_response.status_code == 401
        assert wrong_password_response.json()["success"] is False

        # 5. Invalid username
        invalid_username_response = requests.post(
            f"{BASE_URL}/login",
            json={
                "username": "nonexistent_auth_user",
                "password": password
            }
        )

        assert invalid_username_response.status_code == 401
        assert invalid_username_response.json()["success"] is False

        # 6. Missing username
        missing_username_response = requests.post(
            f"{BASE_URL}/login",
            json={
                "password": password
            }
        )

        assert missing_username_response.status_code == 400
        assert missing_username_response.json()["success"] is False

        # 7. Missing password
        missing_password_response = requests.post(
            f"{BASE_URL}/login",
            json={
                "username": username
            }
        )

        assert missing_password_response.status_code == 400
        assert missing_password_response.json()["success"] is False

        # 8. Empty body
        invalid_body_response = requests.post(
            f"{BASE_URL}/login",
            json={}
        )

        assert invalid_body_response.status_code == 400
        assert invalid_body_response.json()["success"] is False

        # 9. Cleanup temporary user
        cleanup_user = requests.delete(
            f"{BASE_URL}/users/{user_id}",
            headers=auth_headers
        )

        assert cleanup_user.status_code == 200
        assert cleanup_user.json()["success"] is True

        # 10. Cleanup temporary employee
        cleanup_employee = requests.delete(
            f"{BASE_URL}/employees/{employee_id}",
            headers=auth_headers
        )

        assert cleanup_employee.status_code == 200
        assert cleanup_employee.json()["success"] is True

    finally:
        # Safety cleanup if test fails midway
        try:
            requests.delete(
                f"{BASE_URL}/users/{user_id}",
                headers=auth_headers
            )
        except Exception:
            pass

        try:
            requests.delete(
                f"{BASE_URL}/employees/{employee_id}",
                headers=auth_headers
            )
        except Exception:
            pass
        