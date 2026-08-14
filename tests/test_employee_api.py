import requests

BASE_URL = "http://127.0.0.1:5000"


def test_employee_crud(auth_headers):
    employee_id = "TEST_EMP_001"

    # 1. Create Employee
    create_response = requests.post(
        f"{BASE_URL}/employees",
        headers=auth_headers,
        json={
            "employee_id": employee_id,
            "full_name": "Automated Test Employee",
            "phone": "9876500001",
            "email": "testemployee@example.com",
            "designation": "Test Staff",
            "address": "Test Address",
            "role": "Staff",
            "hire_date": "2026-08-10",
            "salary": 25000.0,
            "status": "Active"
        }
    )

    print("EMPLOYEE STATUS:", create_response.status_code)
    print("EMPLOYEE BODY:", create_response.text)

    assert create_response.status_code == 201
    assert create_response.json()["success"] is True

    # 2. Get Employee
    get_response = requests.get(
        f"{BASE_URL}/employees/{employee_id}",
        headers=auth_headers
    )

    assert get_response.status_code == 200
    assert get_response.json()["success"] is True
    assert get_response.json()["employee"]["employee_id"] == employee_id

    # 3. Update Employee
    update_response = requests.put(
        f"{BASE_URL}/employees/{employee_id}",
        headers=auth_headers,
        json={
            "full_name": "Updated Test Employee",
            "phone": "9876500002",
            "email": "updatedemployee@example.com",
            "designation": "Senior Test Staff",
            "address": "Updated Test Address",
            "role": "Manager",
            "hire_date": "2026-08-10",
            "salary": 30000.0,
            "status": "Active"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # 4. Verify Update
    verify_response = requests.get(
        f"{BASE_URL}/employees/{employee_id}",
        headers=auth_headers
    )

    assert verify_response.status_code == 200

    updated_employee = verify_response.json()["employee"]

    assert updated_employee["full_name"] == "Updated Test Employee"
    assert updated_employee["phone"] == "9876500002"
    assert updated_employee["email"] == "updatedemployee@example.com"
    assert updated_employee["designation"] == "Senior Test Staff"
    assert updated_employee["role"] == "Manager"
    assert updated_employee["salary"] == 30000.0

    # 5. Delete Employee
    delete_response = requests.delete(
        f"{BASE_URL}/employees/{employee_id}",
        headers=auth_headers
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

    # 6. Verify Delete
    deleted_response = requests.get(
        f"{BASE_URL}/employees/{employee_id}",
        headers=auth_headers
    )

    assert deleted_response.status_code == 404
    assert deleted_response.json()["success"] is False