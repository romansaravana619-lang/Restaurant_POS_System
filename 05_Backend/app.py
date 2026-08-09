"""
app.py

Main Flask application entry point for Saru POS v1.0.
"""

from flask import Flask, jsonify
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

# Initialize Flask application
app = Flask(__name__)

# Register blueprints
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

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "application": "Saru POS",
        "version": "1.0",
        "status": "Running"
    })

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )
