"""
Menu Item Routes Module

This module initializes the Flask Blueprint for menu item management in the
Saru POS v1.0 application. It defines the routing namespace and imports the
necessary service functions required to handle operations such as adding,
retrieving, updating, and deleting menu items.
"""

from unittest import result

from flask import Blueprint, request, jsonify

from services.menu_item_service import (
    add_menu_item,
    get_all_menu_items,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item
)

menu_item_bp = Blueprint("menu_item", __name__)

@menu_item_bp.route('/menu-items', methods=['POST'])
def create_menu_item():
    """
    Creates a new menu item.

    Expects a JSON payload with menu_item_id, category_id, item_name, 
    price, description, and availability. Validates the input and calls 
    the service layer to insert the record into the database.

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

    menu_item_id = data.get("menu_item_id")
    category_id = data.get("category_id")
    item_name = data.get("item_name")
    price = data.get("price")
    description = data.get("description")
    availability = data.get("availability")

    if not menu_item_id or not category_id or not item_name or price is None or str(price).strip() == "" or not description or not availability:
        return jsonify({
            "success": False,
            "message": "All fields (menu_item_id, category_id, item_name, price, description, availability) are required."
        }), 400

    result = add_menu_item(
        menu_item_id,
        category_id,
        item_name,
        price,
        description,
        availability
    )

    if result.get("success"):
        return jsonify(result), 201
        return jsonify(result), 400

@menu_item_bp.route('/menu-items', methods=['GET'])
def get_menu_items():
    """
    Retrieves all menu items.

    Calls the service layer to fetch a list of all menu items from the 
    database. If successful, returns the list with a 200 status code. 
    If no items are found or an error occurs, returns a 404 status code.

    Returns:
        tuple: A JSON response containing the success status and the menu 
               items data or an error message, along with the appropriate 
               HTTP status code.
    """
    result = get_all_menu_items()

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@menu_item_bp.route('/menu-items/<menu_item_id>', methods=['GET'])
def get_menu_item(menu_item_id):
    """
    Retrieves a specific menu item by its ID.

    Calls the service layer to fetch the menu item associated with the 
    provided menu_item_id. If successful, returns the menu item data 
    with a 200 status code. If the item is not found or an error occurs, 
    returns a 404 status code.

    Args:
        menu_item_id (str): The unique identifier of the menu item to retrieve.

    Returns:
        tuple: A JSON response containing the success status and the menu 
               item data or an error message, along with the appropriate 
               HTTP status code.
    """
    result = get_menu_item_by_id(menu_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@menu_item_bp.route('/menu-items/<menu_item_id>', methods=['PUT'])
def update_menu_item_route(menu_item_id):
    """
    Updates an existing menu item by its ID.

    Expects a JSON payload with category_id, item_name, price, 
    description, and availability. Validates the input and calls 
    the service layer to update the record in the database.

    Args:
        menu_item_id (str): The unique identifier of the menu item to update.

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

    category_id = data.get("category_id")
    item_name = data.get("item_name")
    price = data.get("price")
    description = data.get("description")
    availability = data.get("availability")

    if not category_id or not item_name or price is None or str(price).strip() == "" or not description or not availability:
        return jsonify({
            "success": False,
            "message": "All fields (category_id, item_name, price, description, availability) are required."
        }), 400

    result = update_menu_item(
        menu_item_id=menu_item_id,
        category_id=category_id,
        item_name=item_name,
        price=price,
        description=description,
        availability=availability
    )

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@menu_item_bp.route('/menu-items/<menu_item_id>', methods=['DELETE'])
def delete_menu_item_route(menu_item_id):
    """
    Deletes an existing menu item by its ID.

    Calls the service layer to remove the menu item associated with the 
    provided menu_item_id from the database. If successful, returns a 
    success message with a 200 status code. If the item is not found, 
    cannot be deleted due to references, or an error occurs, returns a 
    404 status code.

    Args:
        menu_item_id (str): The unique identifier of the menu item to delete.

    Returns:
        tuple: A JSON response containing the success status and message, 
               along with the appropriate HTTP status code.
    """
    result = delete_menu_item(menu_item_id)

    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404