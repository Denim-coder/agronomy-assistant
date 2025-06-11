from app.utils.soil import get_soil_data
from app.utils.weather import get_weather

def get_crop_recommendation(city, lat, lon):
    soil = get_soil_data(lat, lon)
    weather = get_weather(city)

    if "error" in soil or "error" in weather:
        return {"error": "Unable to fetch soil or weather data."}

    ph = soil.get("ph_0_5cm") or 7.0
    temp = weather.get("temperature", 25)
    humidity = weather.get("humidity", 50)

    recommendations = []

    # Sample logic
    if 6.0 <= ph <= 7.5 and temp > 25 and humidity > 50:
        recommendations.append("Rice")
    if 6.0 <= ph <= 7.5 and temp < 25:
        recommendations.append("Wheat")
    if 5.5 <= ph <= 6.5 and humidity < 60:
        recommendations.append("Groundnut")
    if 6.0 <= ph <= 7.5 and temp > 20:
        recommendations.append("Sugarcane")

    if not recommendations:
        recommendations.append("No strong match – try adjusting soil or water")

    return {
        "recommended_crops": recommendations,
        "soil_pH": ph,
        "temperature": temp,
        "humidity": humidity
    }
