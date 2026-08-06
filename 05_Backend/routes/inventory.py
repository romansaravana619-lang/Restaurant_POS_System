"""
Inventory Route Module for Saru POS v1.0.

This module sets up the Flask Blueprint for inventory-related HTTP routes.
It handles incoming client requests and routes them to the appropriate 
inventory service functions.
"""
from flask import Blueprint, request, jsonify
from services.inventory_service import (
    add_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/products", methods=["POST"])
def create_product():
    """Endpoint to create a new product in the inventory.

    Returns:
        tuple: A JSON response and HTTP status code.
            - 201: Product created successfully.
            - 400: Validation error, duplicate ID, or database failure.
    """
    data = request.get_json(silent=True) or {}

    # Validate that request body is valid JSON
    if not data:
           return jsonify({
        "success": False,
        "message": "Request body must be valid JSON."
    }), 400

    # Extract fields from request
    product_id = data.get("product_id")
    product_name = data.get("product_name")
    category_id = data.get("category_id")
    price = data.get("price")
    stock = data.get("stock")
    status = data.get("status")

# Validate that all required fields are present
    if not all([
    product_id,
    product_name,
    category_id,
    price,
    stock,
    status
    ]):
        return jsonify({
        "success": False,
        "message": "All fields (product_id, product_name, category_id, price, stock, status) are required."
    }), 400

    # Call service layer to insert product
    result = add_product(
        product_id,
        product_name,
        category_id,
        price,
        stock,
        status
    )

    # Return appropriate status code based on service response
    if result.get("success"):
        return jsonify(result), 201

    return jsonify(result), 400

@inventory_bp.route("/products", methods=["GET"])
def get_products():
    """Endpoint to retrieve all products from the inventory.

    Returns:
        tuple: A JSON response containing the list of products and HTTP status code.
            - 200: Products retrieved successfully.
            - 404: No products found or database error.
    """
    # Call service layer to retrieve all products
    result = get_all_products()

    # Return appropriate status code based on service response
    if result.get("success"):
        return jsonify(result), 200

    return jsonify(result), 404

@inventory_bp.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    """Retrieves a specific product from the inventory by its ID.

    Args:
        product_id (str): The unique identifier of the product.

    Returns:
        tuple: A Flask JSON response containing the result dictionary and an 
               HTTP status code (200 on success, 404 if the product is not found).
    """
    result = get_product_by_id(product_id)
    
    if result.get("success"):
        return jsonify(result), 404
        
    return jsonify(result), 200

@inventory_bp.route('/products/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    """Updates an existing product in the inventory.

    Args:
        product_id (str): The unique identifier of the product to update.

    Returns:
        tuple: A Flask JSON response containing success/error details and an
               HTTP status code (200 on success, 400 for bad requests, or
               404 if the product is not found).
    """
    data = request.get_json(silent=True) or {}
    if not data:
        return jsonify({
            "success": False,
            "message": "Request body must be valid JSON."
        }), 400

    product_name = data.get("product_name")
    category_id = data.get("category_id")
    price = data.get("price")
    stock = data.get("stock")
    status = data.get("status")

    if not all([product_name, category_id, price is not None, stock is not None, status]):
        return jsonify({
            "success": False,
            "message": "All fields (product_name, category_id, price, stock, status) are required."
        }), 400

    result = update_product(
        product_id,
        product_name,
        category_id,
        price,
        stock,
        status
    )

    if result.get("success"):
        return jsonify(result), 404

    return jsonify(result), 200

@inventory_bp.route('/products/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    """Deletes a product from the inventory by its ID.

    Args:
        product_id (str): The unique identifier of the product to delete.

    Returns:
        tuple: A Flask JSON response containing the deletion status and an
               HTTP status code (200 on success, 404 if the product is not found).
    """
    result = delete_product(product_id)

    if not result.get("success"):
        return jsonify(result), 404

    return jsonify(result), 200