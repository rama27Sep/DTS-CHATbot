import requests

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 51.5072,
        "longitude": -0.1276,
        "current_weather": True
    }

    response = requests.get(url, params=params, timeout=5)
    return response.json()
