!pip install flask-ngrok
!pip install flask-ngrok --upgrade
!pip install flask==0.12.2
!pip install flask --upgrade

from markupsafe import Markup
from flask_ngrok import run_with_ngrok
from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)
run_with_ngrok(app)
current_dir = os.getcwd()

# Construct the paths to the model and scaler files
model_path = os.path.join(current_dir, 'predictor.pkl')
scaler_path = os.path.join(current_dir, 'scaler.pkl')

# Load the model and scaler using the absolute paths
with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.json

        # Map 'Risk' to numeric values
        risk_mapping = {'Low': 1, 'Medium': 2, 'High': 3}
        risk = risk_mapping.get(data['risk'], 0) # Default to 0 if invalid risk is provided

        # Extract other features
        population = float(data['population'])
        commute = float(data['commute'])
        airport = 1 if data['airport'] == 'Yes' else 0 # Convert Yes/No to binary
        trip = float(data['trip'])

        # Prepare feature array
        features = np.array([risk, population, commute, airport, trip]).reshape(1, -1)

        # Scale and predict
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)

        # Return prediction
        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run()
