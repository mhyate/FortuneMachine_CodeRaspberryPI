import requests
import os
from dotenv import load_dotenv

class Horoscope:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        load_dotenv()  # Charger les variables d'environnement
        self.url = "https://horoscope-astrology.p.rapidapi.com/horoscope"
        self.headers = {
            "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
            "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }

    def get_daily_horoscope(self, sign):
        """Obtenir l'horoscope quotidien pour un signe donné"""
        try:
            querystring = {"day":"today","sunsign":sign}
            response = requests.get(self.url, headers=self.headers, params=querystring, timeout=20)
            
            if response.status_code == 200:
                data = response.json()
                horoscope = data.get("horoscope", "Désolé, l'horoscope n'est pas disponible pour le moment.")
                return self.translate_to_french(horoscope)
            return "Erreur lors de la récupération de l'horoscope."
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return "Erreur de connexion à l'API d'horoscope."

    def translate_to_french(self, text):
        """Traduire le texte en français"""
        try:
            url = "https://api.mymemory.translated.net/get"
            params = {
                'q': text,
                'langpair': 'en|fr'
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data['responseData']['translatedText']
            return text
        except Exception as e:
            print(f"Erreur de traduction: {e}")
            return text

    def run(self, sign):
        """Exécuter le processus principal pour obtenir l'horoscope"""
        horoscope = self.get_daily_horoscope(sign)
        if horoscope:
            print(horoscope)  # Pour le debug dans le terminal
            return horoscope
        return None

# Test de la classe
if __name__ == "__main__":
    horoscope = Horoscope()
    horoscope.run("Taurus") 