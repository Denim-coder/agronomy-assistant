import streamlit as st
import requests

API_URL = "https://agronomy-backend.onrender.com"

st.set_page_config(page_title="AI-Powered Agronomy Assistant")
st.title("🌾 AI-Powered Agronomy Assistant")

# ✅ Step 3: Sidebar
selected_feature = st.sidebar.selectbox(
    "Select a feature",
    (
        "🌾 Crop Health Prediction",
        "💧 Irrigation Alert",
        "☁️ Weather Info",
        "🌱 Crop Recommendation",
        "🔔 Notifications",
        "🗣️ Farmer Feedback",
        "📊 Field Health Dashboard",
        "📟 Real-Time Sensor Alert"


    )
)

# Now, use this selection to conditionally load feature sections
if selected_feature == "🌾 Crop Health Prediction":
    # import or write your Crop Health UI code here
    st.subheader("🌾 Crop Health Prediction")

    Soil_Moisture = st.slider("Soil Moisture (%)", 0, 100)
    Ambient_Temperature = st.slider("Ambient Temperature (°C)", 0, 50)
    Soil_Temperature = st.slider("Soil Temperature (°C)", 0, 50)
    Humidity = st.slider("Humidity (%)", 0, 100)
    Light_Intensity = st.slider("Light Intensity (lux)", 0, 20000)
    Soil_pH = st.slider("Soil pH", 0.0, 14.0)
    Nitrogen_Level = st.slider("Nitrogen Level (ppm)", 0, 500)
    Phosphorus_Level = st.slider("Phosphorus Level (ppm)", 0, 500)
    Potassium_Level = st.slider("Potassium Level (ppm)", 0, 500)
    Chlorophyll_Content = st.slider("Chlorophyll Content", 0, 100)
    Electrochemical_Signal = st.slider("Electrochemical Signal", 0, 100)

    if st.button("Predict Health"):
        response = requests.post(f"{API_URL}/predict_health", json={
            "Soil_Moisture": Soil_Moisture,
            "Ambient_Temperature": Ambient_Temperature,
            "Soil_Temperature": Soil_Temperature,
            "Humidity": Humidity,
            "Light_Intensity": Light_Intensity,
            "Soil_pH": Soil_pH,
            "Nitrogen_Level": Nitrogen_Level,
            "Phosphorus_Level": Phosphorus_Level,
            "Potassium_Level": Potassium_Level,
            "Chlorophyll_Content": Chlorophyll_Content,
            "Electrochemical_Signal": Electrochemical_Signal
        })

        if response.ok:
            st.success(f"Predicted Health: {response.json()['predicted_health_status']}")
        else:
            st.error("Prediction failed.")

elif selected_feature == "💧 Irrigation Alert":
    # your irrigation alert code
    st.subheader("💧 Irrigation Alert System")

    soil_moisture_input = st.slider("Select current soil moisture value (%)", 0, 100)

    if st.button("Check Irrigation Status"):
        response = requests.post(f"{API_URL}/irrigation_alert", json={"Soil_Moisture": soil_moisture_input})
        if response.ok:
            st.success(response.json()['irrigation_alert'])
        else:
            st.error("Failed to get irrigation alert.")
            
elif selected_feature == "☁️ Weather Info":
    st.subheader("☁️ Weather Information")

    city = st.text_input("Enter City Name")
    if st.button("Get Weather"):
        response = requests.get(f"{API_URL}/weather_info?city={city}")
        if response.ok:
            weather = response.json()
            st.write(f"**Temperature:** {weather['temperature']} °C")
            st.write(f"**Humidity:** {weather['humidity']}%")
            st.write(f"**Condition:** {weather['description']}")
        else:
            st.error("Failed to fetch weather data.")

elif selected_feature == "🌱 Crop Recommendation":
    st.subheader("🌱 Crop Recommendation System")

    nitrogen = st.slider("Nitrogen (N)", 0, 150)
    phosphorus = st.slider("Phosphorus (P)", 0, 150)
    potassium = st.slider("Potassium (K)", 0, 150)
    temperature = st.slider("Temperature (°C)", 0, 50)
    humidity = st.slider("Humidity (%)", 0, 100)
    ph = st.slider("pH", 0.0, 14.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 300.0)

    if st.button("Recommend Crop"):
        response = requests.post(f"{API_URL}/recommend_crop", json={
            "N": nitrogen,
            "P": phosphorus,
            "K": potassium,
            "temperature": temperature,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        })
        if response.ok:
            st.success(f"Recommended Crop: 🌾 {response.json()['recommended_crop']}")
        else:
            st.error("Failed to get recommendation.")
   

elif selected_feature == "🔔 Notifications":
    st.subheader("Real-time Alerts")
    if st.button("Fetch Latest Alerts"):
        response = requests.get(f"{API_URL}/notifications")
        if response.ok:
            for alert in response.json()["notifications"]:
                st.warning(alert)
        else:
            st.error("Failed to fetch notifications.")

elif selected_feature == "🗣️ Farmer Feedback":
    st.subheader("🗣️ Submit Feedback")

    name = st.text_input("Your Name")
    category = st.selectbox("Feedback Type", ["Prediction", "Alert", "General"])
    feedback = st.text_area("Your Feedback")

    if st.button("Submit Feedback"):
        if not name or not feedback:
            st.error("Please fill in all fields.")
        else:
            response = requests.post(f"{API_URL}/feedback", json={
                "name": name,
                "category": category,
                "feedback": feedback
            })
            if response.ok:
                st.success("Feedback submitted. Thank you!")
            else:
                st.error("Error submitting feedback.")





elif selected_feature == "📊 Field Health Dashboard":
    st.subheader("📊 Field Health Dashboard")

    st.markdown("Enter live sensor data to see real-time field status.")

    Soil_Moisture = st.slider("Soil Moisture (%)", 0, 100)
    Ambient_Temperature = st.slider("Ambient Temperature (°C)", 0, 50)
    Soil_Temperature = st.slider("Soil Temperature (°C)", 0, 50)
    Humidity = st.slider("Humidity (%)", 0, 100)
    Light_Intensity = st.slider("Light Intensity (lux)", 0, 20000)
    Soil_pH = st.slider("Soil pH", 0.0, 14.0)
    Nitrogen_Level = st.slider("Nitrogen Level (ppm)", 0, 500)
    Phosphorus_Level = st.slider("Phosphorus Level (ppm)", 0, 500)
    Potassium_Level = st.slider("Potassium Level (ppm)", 0, 500)
    Chlorophyll_Content = st.slider("Chlorophyll Content", 0, 100)
    Electrochemical_Signal = st.slider("Electrochemical Signal", 0, 100)

    if st.button("Analyze Field Health"):
        # Prediction
        health_res = requests.post(f"{API_URL}/predict_health", json={
            "Soil_Moisture": Soil_Moisture,
            "Ambient_Temperature": Ambient_Temperature,
            "Soil_Temperature": Soil_Temperature,
            "Humidity": Humidity,
            "Light_Intensity": Light_Intensity,
            "Soil_pH": Soil_pH,
            "Nitrogen_Level": Nitrogen_Level,
            "Phosphorus_Level": Phosphorus_Level,
            "Potassium_Level": Potassium_Level,
            "Chlorophyll_Content": Chlorophyll_Content,
            "Electrochemical_Signal": Electrochemical_Signal
        })

        irrigation_res = requests.post(f"{API_URL}/irrigation_alert", json={
            "Soil_Moisture": Soil_Moisture
        })

        if health_res.ok and irrigation_res.ok:
            health = health_res.json()['predicted_health_status']
            irrigation = irrigation_res.json()['irrigation_alert']

            st.success(f"🩺 Predicted Crop Health: **{health}**")
            st.info(f"💧 Irrigation Suggestion: **{irrigation}**")

            # Overall field condition
            if health.lower() == "healthy" and "no" in irrigation.lower():
                st.success("✅ Field Status: **Optimal** 🌿")
            elif "irrigate" in irrigation.lower() or health.lower() != "healthy":
                st.warning("⚠️ Field Status: **Needs Attention** 🧑‍🌾")
            else:
                st.error("🚨 Field Status: **Critical** ❌")

        else:
            st.error("Failed to fetch prediction or irrigation alert.")



elif selected_feature == "📟 Real-Time Sensor Alert":
    st.subheader("📡 Real-Time Sensor Monitoring")

    sm = st.slider("Soil Moisture (%)", 0, 100)
    stemp = st.slider("Soil Temperature (°C)", 0, 60)
    sph = st.slider("Soil pH", 0.0, 14.0)

    if st.button("Check Sensor Status"):
        response = requests.post(f"{API_URL}/sensor_alert", json={
            "Soil_Moisture": sm,
            "Soil_Temperature": stemp,
            "Soil_pH": sph
        })

        if response.ok:
            for msg in response.json()["sensor_alerts"]:
                if "⚠️" in msg or "💧" in msg or "🌡️" in msg:
                   st.warning(msg)
                else:
                  st.success(msg)

        else:
            st.error("Error checking sensor alerts.")
