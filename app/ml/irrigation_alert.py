# app/ml/irrigation_alert.py

# ✅ Step 1: Define thresholds
LOW_MOISTURE_THRESHOLD = 20
HIGH_MOISTURE_THRESHOLD = 80

# ✅ Step 2: Alert logic
def generate_irrigation_alert(soil_moisture):
    if soil_moisture < LOW_MOISTURE_THRESHOLD:
        return "Low soil moisture detected. Irrigation is recommended."
    elif soil_moisture > HIGH_MOISTURE_THRESHOLD:
        return "High soil moisture detected. Overwatering risk!"
    else:
        return "Soil moisture is within optimal range. No action needed."
