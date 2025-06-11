import requests


def get_soil_data(lat, lon):
    url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={lon}&lat={lat}&property=phh2o&depth=0-5cm"
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            layers = data['properties']['layers']
            ph_layer = next((layer for layer in layers if layer['name'] == 'phh2o'), None)
            
            if not ph_layer:
                raise KeyError("phh2o not found in layers")

            depths = ph_layer['depths']
            ph = depths[0]['values'].get('mean')

            if ph is None:
                raise ValueError("ph mean value not found")

            return {
                "latitude": lat,
                "longitude": lon,
                "ph_0_5cm": ph / 10  # Convert from *10 format
            }

        except Exception as e:
            print("❌ Error extracting ph data:", e)
            return {"error": "Soil pH data not available for this location"}
    else:
        return {"error": "Could not retrieve soil data"}
