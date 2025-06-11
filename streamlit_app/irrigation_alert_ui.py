import streamlit as st
import requests

API_URL = "http://localhost:5000"  # Change this if deployed

st.title("🌾 AI-Powered Agronomy Assistant")
st.subheader("💧 Irrigation Alert System")

soil_moisture_input = st.slider("Select current soil moisture value (%)", 0, 100)

if st.button("Check Irrigation Status"):
    response = requests.post(f"{API_URL}/irrigation_alert", json={"Soil_Moisture": soil_moisture_input})
    if response.ok:
        st.success(response.json()['irrigation_alert'])
    else:
        st.error("Failed to get irrigation alert.")
