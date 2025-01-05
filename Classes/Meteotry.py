import requests
from datetime import datetime

class Meteotry:
    def __init__(self):
        """Initialisation de l'URL de l'API"""
        self.api_url = "https://api.open-meteo.com/v1/forecast"
        # Coordonnées de Tours
        self.latitude = 47.3941
        self.longitude = 0.6848

    def getWeather(self):
        """Récupérer les données météo"""
        try:
            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "current": ["temperature_2m", "relative_humidity_2m", "precipitation", "weather_code"]
            }
            response = requests.get(self.api_url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Erreur lors de la requête météo: {e}")
            return None

    def get_weather_description(self, code):
        """Convertir le code météo en description en français"""
        weather_codes = {
            0: "Ciel dégagé",
            1: "Principalement dégagé",
            2: "Partiellement nuageux",
            3: "Couvert",
            45: "Brumeux",
            48: "Brouillard givrant",
            51: "Bruine légère",
            53: "Bruine modérée",
            55: "Bruine dense",
            61: "Pluie légère",
            63: "Pluie modérée",
            65: "Pluie forte",
            71: "Neige légère",
            73: "Neige modérée",
            75: "Neige forte",
            77: "Grains de neige",
            80: "Averses légères",
            81: "Averses modérées",
            82: "Averses violentes",
            85: "Averses de neige légères",
            86: "Averses de neige fortes",
            95: "Orage",
            96: "Orage avec grêle légère",
            99: "Orage avec grêle forte"
        }
        return weather_codes.get(code, "Conditions météorologiques inconnues")

    def displayWeather(self):
        """Formater le message météo"""
        data = self.getWeather()
        if not data or 'current' not in data:
            return None

        current = data['current']
        temp = current.get('temperature_2m')
        humidity = current.get('relative_humidity_2m')
        weather_code = current.get('weather_code')
        weather_desc = self.get_weather_description(weather_code)

        message = f"Météo actuelle à Tours:\n"
        message += f"🌡️ {temp}°C\n"
        message += f"💧 Humidité: {humidity}%\n"
        message += f"🌤️ {weather_desc}"

        return message

    def run(self):
        """Exécuter le processus principal"""
        return self.displayWeather()

# Test de la classe
if __name__ == "__main__":
    meteo = Meteotry()
    print(meteo.run())
