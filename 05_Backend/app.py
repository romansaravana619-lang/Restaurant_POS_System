"""
app.py

Main Flask application entry point for Saru POS v1.0.
"""

from flask import Flask, jsonify
from routes.auth import auth_bp
from routes.customer import customer_bp

# Initialize Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)

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