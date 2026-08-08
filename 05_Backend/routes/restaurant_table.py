"""
Restaurant Table Routes Module

This module initializes the Flask Blueprint for restaurant table management in 
the Saru POS v1.0 application. It defines the routing namespace and imports 
the necessary service functions required to handle operations such as adding, 
retrieving, updating, and deleting restaurant tables.
"""

from flask import Blueprint, request, jsonify
from services.restaurant_table_service import (
    add_restaurant_table,
    get_all_restaurant_tables,
    get_restaurant_table_by_id,
    update_restaurant_table,
    delete_restaurant_table
)

restaurant_table_bp = Blueprint("restaurant_table", __name__)

@restaurant_table_bp.route('/restaurant-tables', methods=['POST'])
def create_restaurant_table():
    """
    Creates a new restaurant table.

    Expects a JSON payload with table_id, table_number, capacity, 
    and status. Validates the input and calls the service layer to 
    insert the record into the database.

    Returns:
        tuple: A JSON response containing the success status and message, 
               along with the appropriate HTTP status code (201 on success, 
               400 on bad request or failure).
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    table_id = data.get("table_id")
    table_number = data.get("table_number")
    capacity = data.get("capacity")
    status = data.get("status")

    if not table_id or not table_number or capacity is None or str(capacity).strip() == "" or not status:
        return jsonify({
            "success": False,
            "message": "All fields (table_id, table_number, capacity, status) are required."
        }), 400

    result = add_restaurant_table(
        table_id,
        table_number,
        capacity,
        status
    )

    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400

@restaurant_table_bp.route('/restaurant-tables', methods=['GET'])
def get_restaurant_tables():
    """
    Retrieves all restaurant tables.

    Calls the service layer to fetch a list of all restaurant tables
    from the database. If successful, returns the list with a 200
    status code. If no tables are found or an error occurs, returns
    a 404 status code.

    Returns:
        tuple: A JSON response containing the success status and the
        restaurant tables data or an error message, along with the
        appropriate HTTP status code.
    """
    result = get_all_restaurant_tables()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@restaurant_table_bp.route('/restaurant-tables/<table_id>', methods=['GET'])
def get_restaurant_table(table_id):
    """
    Retrieves a specific restaurant table by its ID.

    Calls the service layer to fetch the restaurant table associated with 
    the provided table_id. If successful, returns the restaurant table data 
    with a 200 status code. If the table is not found or an error occurs, 
    returns a 404 status code.

    Args:
        table_id (str): The unique identifier of the restaurant table to retrieve.

    Returns:
        tuple: A JSON response containing the success status and the restaurant 
               table data or an error message, along with the appropriate 
               HTTP status code.
    """
    result = get_restaurant_table_by_id(table_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@restaurant_table_bp.route('/restaurant-tables/<table_id>', methods=['PUT'])
def update_restaurant_table_route(table_id):
    """
    Updates an existing restaurant table by its ID.

    Expects a JSON payload with table_number, capacity, and status. 
    Validates the input and calls the service layer to update the 
    record in the database.

    Args:
        table_id (str): The unique identifier of the restaurant table to update.

    Returns:
        tuple: A JSON response containing the success status and message, 
               along with the appropriate HTTP status code (200 on success, 
               400 on bad request, or 404 if not found/error).
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    table_number = data.get("table_number")
    capacity = data.get("capacity")
    status = data.get("status")

    if not table_number or capacity is None or str(capacity).strip() == "" or not status:
        return jsonify({
            "success": False,
            "message": "All fields (table_number, capacity, status) are required."
        }), 400

    result = update_restaurant_table(
        table_id=table_id,
        table_number=table_number,
        capacity=capacity,
        status=status
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@restaurant_table_bp.route('/restaurant-tables/<table_id>', methods=['DELETE'])
def delete_restaurant_table_route(table_id):
    """
    Deletes an existing restaurant table by its ID.

    Calls the service layer to remove the restaurant table associated with 
    the provided table_id from the database. If successful, returns a 
    success message with a 200 status code. If the table is not found, 
    cannot be deleted due to references, or an error occurs, returns a 
    404 status code.

    Args:
        table_id (str): The unique identifier of the restaurant table to delete.

    Returns:
        tuple: A JSON response containing the success status and message, 
               along with the appropriate HTTP status code.
    """
    result = delete_restaurant_table(table_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404