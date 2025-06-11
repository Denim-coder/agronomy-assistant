import streamlit as st
import requests

st.title("🌾 Crop Health Predictor")

# Input fields for all features
features = {
    "Soil_Moisture": st.number_input("Soil Moisture", min_value=0.0),
    "Ambient_Temperature": st.number_input("Ambient Temperature", min_value=-10.0),
    "Soil_Temperature": st.number_input("Soil Temperature", min_value=-10.0),
    "Humidity": st.number_input("Humidity", min_value=0.0),
    "Light_Intensity": st.number_input("Light Intensity", min_value=0.0),
    "Soil_pH": st.number_input("Soil pH", min_value=0.0),
    "Nitrogen_Level": st.number_input("Nitrogen Level", min_value=0.0),
    "Phosphorus_Level": st.number_input("Phosphorus Level", min_value=0.0),
    "Potassium_Level": st.number_input("Potassium Level", min_value=0.0),
    "Chlorophyll_Content": st.number_input("Chlorophyll Content", min_value=0.0),
    "Electrochemical_Signal": st.number_input("Electrochemical Signal", min_value=0.0)
}

if st.button("Predict Health Status"):
    try:
        response = requests.post("http://127.0.0.1:5000/predict_health", json=features)

        if response.status_code == 200:
            prediction = response.json().get("predicted_health_status")
            st.success(f"🌱 Predicted Health Status: **{prediction}**")
        else:
            st.error(f"Error from server: {response.json().get('error')}")

    except Exception as e:
        st.error(f"Request failed: {e}")
