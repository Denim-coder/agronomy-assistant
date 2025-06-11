from flask import Blueprint, request, jsonify
from app.utils.weather import get_weather
from app.utils.soil import get_soil_data

import joblib
import numpy as np

import os

from app.ml.irrigation_alert import generate_irrigation_alert


from app.utils.recommendation import get_crop_recommendation
from app.utils.predict_health import predict_plant_health

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({"message": "Welcome to the AI-Powered Agronomy Assistant API"})

@main.route('/weather_info', methods=['GET'])
def weather_info():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    data = get_weather(city)
    return jsonify(data)




@main.route('/soil', methods=['GET'])
def soil():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({"error": "Latitude and longitude are required"}), 400
    data = get_soil_data(lat, lon)
    return jsonify(data)




@main.route('/recommend_crop', methods=['POST'])
def recommend_crop():
    print("recommend_crop route hit")
    print(data)


    try:
        data = request.get_json()
        nitrogen = data.get("N")
        phosphorus = data.get("P")
        potassium = data.get("K")
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        ph = data.get("ph")
        rainfall = data.get("rainfall")

        # Call your crop recommendation logic (this can be ML-based or rule-based)
        crop = get_crop_recommendation(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall)

        return jsonify({"recommended_crop": crop})
    except Exception as e:
        return jsonify({"error": str(e)})




 # 👈 This is the Blueprint

@main.route('/predict_health', methods=['POST'])  # 👈 The prediction route
def predict_health():
    try:
        data = request.get_json()

        features = [
            data['Soil_Moisture'],
            data['Ambient_Temperature'],
            data['Soil_Temperature'],
            data['Humidity'],
            data['Light_Intensity'],
            data['Soil_pH'],
            data['Nitrogen_Level'],
            data['Phosphorus_Level'],
            data['Potassium_Level'],
            data['Chlorophyll_Content'],
            data['Electrochemical_Signal']
        ]
        print("Current working directory:", os.getcwd())
        print("Files in ml:", os.listdir('app/ml'))
        
        model = joblib.load('app/ml/health_model.pkl')
        
        prediction = model.predict([features])[0]

        return jsonify({'predicted_health_status': str(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)})




@main.route('/irrigation_alert', methods=['POST'])
def irrigation_alert():
    try:
        data = request.get_json()
        soil_moisture = data.get('Soil_Moisture')

        from app.ml.irrigation_alert import generate_irrigation_alert
        alert = generate_irrigation_alert(soil_moisture)

        return jsonify({'irrigation_alert': alert})
    except Exception as e:
        return jsonify({'error': str(e)})



@main.route('/notifications', methods=['GET'])
def get_notifications():
    try:
        notifications = [
            "🌧️ Rain expected in next 24 hours. Delay irrigation.",
            "⚠️ High disease risk detected in field 3.",
            "💧 Soil moisture dropped below optimal range in field 2."
        ]
        return jsonify({"notifications": notifications})
    except Exception as e:
        return jsonify({"error": str(e)}), 500




feedback_list = []  # Store feedback temporarily

@main.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.get_json()
        feedback = data.get("feedback")

        if not feedback:
            return jsonify({"error": "Feedback text is required"}), 400

        feedback_list.append(feedback)
        return jsonify({"message": "Feedback submitted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify({"feedbacks": feedback_list})



@main.route('/sensor_alert', methods=['POST'])
def sensor_alert():
    try:
        data = request.get_json()
        alerts = []

        if data.get("Soil_Moisture", 50) < 30:
            alerts.append("💧 Soil moisture is critically low!")

        if data.get("Soil_Temperature", 25) > 40:
            alerts.append("🌡️ Soil temperature is too high!")

        if data.get("Soil_pH", 7) < 5.5 or data.get("Soil_pH", 7) > 8:
            alerts.append("⚠️ Soil pH is out of optimal range!")

        if not alerts:
            alerts.append("✅ All sensor readings are within optimal range.")

        return jsonify({"sensor_alerts": alerts})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
