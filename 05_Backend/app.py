"""
app.py

Main Flask application entry point for Saru POS v1.0.
"""

import os

from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

# Route blueprints
from routes.auth import auth_bp
from routes.customer import customer_bp
from routes.supplier import supplier_bp
from routes.inventory import inventory_bp
from routes.category import category_bp
from routes.menu_item import menu_item_bp
from routes.restaurant_table import restaurant_table_bp
from routes.billing import billing_bp
from routes.bill_item import bill_item_bp
from routes.payment import payment_bp
from routes.employee import employee_bp
from routes.settings import settings_bp
from routes.user import user_bp
from routes.dining_session import dining_session_bp

# Database initialization
from create_tables import (
    create_users_table,
    create_employees_table,
    create_categories_table,
    create_menu_items_table,
    create_customers_table,
    create_restaurant_tables_table,
    create_dining_sessions_table,
    create_bills_table,
    create_bill_items_table,
    create_payments_table,
    create_suppliers_table,
    create_inventory_items_table,
    create_settings_table,
)

from seed_data import seed_default_data


# ============================================================
# Initialize Flask application
# ============================================================

app = Flask(__name__)


# ============================================================
# Database Initialization
# ============================================================

# Create all required database tables
create_users_table()
create_employees_table()
create_categories_table()
create_menu_items_table()
create_customers_table()
create_restaurant_tables_table()
create_dining_sessions_table()
create_bills_table()
create_bill_items_table()
create_payments_table()
create_suppliers_table()
create_inventory_items_table()
create_settings_table()

# Insert default admin and initial application data
seed_default_data()


# ============================================================
# CORS Configuration
# ============================================================

frontend_url = os.getenv(
    "SARU_POS_FRONTEND_URL",
    "http://localhost:5173"
)

CORS(
    app,
    origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        frontend_url,
    ],
)


# ============================================================
# Error Handlers
# ============================================================

@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({
        "success": False,
        "message": error.description
    }), error.code


@app.errorhandler(Exception)
def handle_unexpected_exception(error):
    return jsonify({
        "success": False,
        "message": "An internal server error occurred."
    }), 500


# ============================================================
# Register Blueprints
# ============================================================

app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(inventory_bp)
app.register_blueprint(category_bp)
app.register_blueprint(menu_item_bp)
app.register_blueprint(restaurant_table_bp)
app.register_blueprint(billing_bp)
app.register_blueprint(bill_item_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(user_bp)
app.register_blueprint(dining_session_bp)


# ============================================================
# Health Check
# ============================================================

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "application": "Saru POS",
        "version": "1.0",
        "status": "Running"
    })


# ============================================================
# Local / Production Server
# ============================================================

if __name__ == "__main__":

    debug_mode = os.getenv(
        "SARU_POS_DEBUG",
        "false"
    ).lower() == "true"

    app.config["DEBUG"] = debug_mode

    app.run(
        debug=debug_mode,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000))
    )