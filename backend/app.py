from flask import Flask, jsonify, request
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Mock inventory data
inventory = [
    {"id": 1, "product": "Widget A", "quantity": 100},
    {"id": 2, "product": "Widget B", "quantity": 50},
]

# AI-based demand forecasting (mock example)
def forecast_demand():
    products = ["Widget A", "Widget B"]
    sales = np.random.randint(50, 150, size=len(products))
    return [{"product": product, "forecast": sale} for product, sale in zip(products, sales)]

# Sync inventory (POST method)
@app.route("/sync", methods=["POST"])
def sync_inventory():
    new_data = request.json  # The incoming data (e.g., from the frontend)
    for item in new_data:
        for inv in inventory:
            if inv["id"] == item["id"]:
                inv["quantity"] = item["quantity"]
    return jsonify({"message": "Inventory synced successfully!", "inventory": inventory})

# Get demand prediction (GET method)
@app.route("/predict", methods=["GET"])
def predict():
    predictions = forecast_demand()
    return jsonify(predictions)

# Root endpoint
@app.route("/")
def home():
    return jsonify({"message": "SmartSync Backend is running!"})

if __name__ == "__main__":
    app.run(debug=True)
