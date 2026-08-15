"""
Employee Routes Module

This module defines the Flask routes for employee management
in the Saru POS v1.0 application.
"""

from flask import Blueprint, request, jsonify

from utils.auth_middleware import require_auth, require_role
from utils.validation import is_non_empty_string, is_number

from services.employee_service import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee,
)


employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees", methods=["POST"])
@require_auth
@require_role("Admin", "Manager")
def create_employee():
    """Creates a new employee."""

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body cannot be empty."
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

    if not all(is_non_empty_string(field) for field in required_string_fields):
        return jsonify({
            "success": False,
            "message": (
                "Required fields (employee_id, full_name, "
                "role, status) are missing or invalid."
            )
        }), 400

    optional_string_fields = [
        phone,
        email,
        designation,
        address,
        hire_date,
    ]

    if not all(
        field is None or is_non_empty_string(field)
        for field in optional_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Optional text fields must be non-empty strings."
        }), 400

    if salary is not None and not is_number(salary):
        return jsonify({
            "success": False,
            "message": "Salary must be a valid number."
        }), 400

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
@require_auth
@require_role("Admin", "Manager")
def get_employees():
    """Retrieves all employees."""

    result = get_all_employees()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@employee_bp.route("/employees/<employee_id>", methods=["GET"])
@require_auth
@require_role("Admin", "Manager")
def get_employee(employee_id):
    """Retrieves an employee by its ID."""

    result = get_employee_by_id(employee_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404


@employee_bp.route("/employees/<employee_id>", methods=["PUT"])
@require_auth
@require_role("Admin", "Manager")
def update_employee_route(employee_id):
    """Updates an existing employee."""

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body cannot be empty."
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

    if not all(is_non_empty_string(field) for field in required_string_fields):
        return jsonify({
            "success": False,
            "message": (
                "Required fields (full_name, role, "
                "status) are missing or invalid."
            )
        }), 400

    optional_string_fields = [
        phone,
        email,
        designation,
        address,
        hire_date,
    ]

    if not all(
        field is None or is_non_empty_string(field)
        for field in optional_string_fields
    ):
        return jsonify({
            "success": False,
            "message": "Optional text fields must be non-empty strings."
        }), 400

    if salary is not None and not is_number(salary):
        return jsonify({
            "success": False,
            "message": "Salary must be a valid number."
        }), 400

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
@require_auth
@require_role("Admin", "Manager")
def delete_employee_route(employee_id):
    """Deletes an employee by its ID."""

    result = delete_employee(employee_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404