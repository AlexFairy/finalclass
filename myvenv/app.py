from app import create_app
from app.models import db
from app.blueprints.customers import customer_bp

from flask import send_from_directory, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import logging

app = create_app('development')

logging.basicConfig(level=logging.DEBUG)
app.logger.info("Flask app initialized with development configuration.")

#for CORS
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
app.logger.info("CORS enabled for cross-origin requests with credentials support.")

#for CORS. Cors was being very annoying so i had to use developers tools for edge to see the issue
app.url_map.strict_slashes = False
app.logger.info("Disabled strict slashes to avoid unnecessary redirects.")


try:
    app.register_blueprint(customer_bp, url_prefix='/customers', name='unique_customer_bp')
    app.logger.info("Blueprint 'customer_bp' registered successfully.")
except ValueError as e:
    app.logger.error(f"Error while registering blueprint: {str(e)}")

@app.route('/swagger.yaml')
def swagger_file():
    try:
        return send_from_directory('static', 'swagger.yaml')
    except FileNotFoundError:
        app.logger.error("Swagger YAML file not found.")
        return jsonify({"error": "Swagger file not found!"}), 404


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)

try:
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL, name='unique_swagger_bp')
    app.logger.info("Swagger UI Blueprint registered successfully.")
except ValueError as e:
    app.logger.error(f"Error while registering Swagger UI blueprint: {str(e)}")

with app.app_context():
    try:
        #this wasnt working for me so i have to FORCE the program to drop tables this way if i want to reset db
        # db.session.remove()  # Forcefully remove the session (for development only)
        # db.drop_all()  # Drop all tables (for development only)
        db.create_all()  # Create all tables based on models
        app.logger.info("Database tables created successfully.")
    except Exception as e:
        app.logger.error(f"Error while initializing the database: {str(e)}")

if __name__ == "__main__":
    app.logger.info("Starting Flask application...")
    app.run()

# I don’t want to type this over and over so copy and paste this is easier!

# Virtual environment activation
# .\module_1_VEproject\Scripts\activate

# Upgrade Python
# python -m pip install --upgrade pip

# Clean cache
# Get-ChildItem -Path . -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force

# Python tests
# python -m unittest tests.test_customers 
# python -m unittest tests.test_mechanics
# python -m unittest tests.test_service_tickets
# python -m unittest tests.test_inventory
# python -m unittest discover -s tests

# For Swagger UI
# python -m pip install flask-swagger-ui

# For Flask CORS
# pip show flask-cors
# Method 1: Force update Flask and Werkzeug
# pip install --upgrade flask Werkzeug
# pip uninstall flask-cors pip install flask-cors
# Method 2: Reinstall Flask-CORS
# pip uninstall flask-cors
# pip install flask-cors --force-reinstall