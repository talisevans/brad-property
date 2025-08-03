# app.py
from flask import Flask, jsonify, request
from functions import *

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the endpoint '/' that accepts GET requests
@app.route('/', methods=['GET'])
def home():
    """This function handles requests to the home page."""

    calculatedResult = 4*4
    # Return a JSON response
    return jsonify({"message": "Hello, World! Brad Property", "calculatedResult": calculatedResult})

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)


# Define a route for the endpoint '/' that accepts GET requests
@app.route('/user', methods=['GET'])
def home_user():
    """This function handles requests to the home page."""
    # Return a JSON response
    return jsonify({"message": "Hello, World! Talis"})

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)


# New endpoint that accepts POST requests with a user name
@app.route('/report', methods=['POST'])
def greet_user():
    """Handle POST requests containing a user's name in the payload."""
    # Get JSON data from request
    data = request.get_json()
    
    # Extract the name from the payload
    if data and 'name' in data:
        name = data['name']
        address = data['address']
        purchasePrice = data['purchase_price']
        return jsonify(
            {
                "message": greet_user_function(name, address),
                "value": purchasePrice,
                "ROI": 28.5
            }
        )
    else:
        return jsonify({"error": "Missing name parameter in request"}), 400

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)



