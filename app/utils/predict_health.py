import pickle
import numpy as np
import os

def predict_plant_health(input_data):
    model_path = os.path.join("app", "models", "plant_health_model.pkl")

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Convert input to numpy array
    features = np.array([[
        input_data['Soil_Moisture'],
        input_data['Ambient_Temperature'],
        input_data['Soil_Temperature'],
        input_data['Humidity'],
        input_data['Light_Intensity'],
        input_data['Soil_pH'],
        input_data['Nitrogen_Level'],
        input_data['Phosphorus_Level'],
        input_data['Potassium_Level'],
        input_data['Chlorophyll_Content'],
        input_data['Electrochemical_Signal']
    ]])

    prediction = model.predict(features)[0]
    return {'Plant_Health_Status': prediction}
