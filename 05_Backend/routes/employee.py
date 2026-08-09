"""
Employee Routes Module

This module defines the Flask routes for employee management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from services.employee_service import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee,
)


employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    """Creates a new employee.

    Reads employee details from the request body, validates the input,
    and creates a new employee record through the service layer.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    employee_id = data.get("employee_id")
    full_name = data.get("full_name")
    phone = data.get("phone")
    email = data.get("email")
    designation = data.get("designation")
    address = data.get("address")
    role = data.get("role")
    hire_date = data.get("hire_date")
    salary = data.get("salary")
    status = data.get("status")

    required_string_fields = [
        employee_id,
        full_name,
        role,
        status,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Required fields (employee_id, full_name, role, status) are missing."
        }), 400

    optional_string_fields = [
        phone,
        email,
        designation,
        address,
        hire_date,
    ]

    for field in optional_string_fields:
        if field is not None and not isinstance(field, str):
            return jsonify({
                "success": False,
                "message": "Optional text fields must be strings."
            }), 400

    if salary is not None and salary == "":
        salary = None

    result = add_employee(
        employee_id=employee_id,
        full_name=full_name,
        phone=phone,
        email=email,
        designation=designation,
        address=address,
        role=role,
        hire_date=hire_date,
        salary=salary,
        status=status,
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400


@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    """Retrieves all employees.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_all_employees()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@employee_bp.route("/employees/<employee_id>", methods=["GET"])
def get_employee(employee_id):
    """Retrieves an employee by its ID.

    Args:
        employee_id (str): The unique identifier for the employee.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = get_employee_by_id(employee_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@employee_bp.route("/employees/<employee_id>", methods=["PUT"])
def update_employee_route(employee_id):
    """Updates an existing employee.

    Args:
        employee_id (str): The unique identifier for the employee.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    full_name = data.get("full_name")
    phone = data.get("phone")
    email = data.get("email")
    designation = data.get("designation")
    address = data.get("address")
    role = data.get("role")
    hire_date = data.get("hire_date")
    salary = data.get("salary")
    status = data.get("status")

    required_string_fields = [
        full_name,
        role,
        status,
    ]

    if not all(
        isinstance(field, str) and field.strip()
        for field in required_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Required fields (full_name, role, status) are missing."
        }), 400

    optional_string_fields = [
        phone,
        email,
        designation,
        address,
        hire_date,
    ]

    for field in optional_string_fields:
        if field is not None and not isinstance(field, str):
            return jsonify({
                "success": False,
                "message": "Optional text fields must be strings."
            }), 400

    if salary is not None and salary == "":
        salary = None

    result = update_employee(
        employee_id=employee_id,
        full_name=full_name,
        phone=phone,
        email=email,
        designation=designation,
        address=address,
        role=role,
        hire_date=hire_date,
        salary=salary,
        status=status,
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@employee_bp.route("/employees/<employee_id>", methods=["DELETE"])
def delete_employee_route(employee_id):
    """Deletes an employee by its ID.

    Args:
        employee_id (str): The unique identifier for the employee.

    Returns:
        tuple: A JSON response and the corresponding HTTP status code.
    """
    result = delete_employee(employee_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404