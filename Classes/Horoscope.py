import requests
import random

class Horoscope:
    def __init__(self):
        """Initialisation de l'URL de l'API et des signes du zodiaque"""
        self.api_url = "https://kayoo123.github.io/astroo-api/jour.json"
        self.signes = [
            "belier", "taureau", "gemeaux", "cancer", 
            "lion", "vierge", "balance", "scorpion",
            "sagittaire", "capricorne", "verseau", "poissons"
        ]

    def getRandomSign(self):
        """Choisir un signe aléatoire"""
        return random.choice(self.signes)

    def getHoroscope(self, sign=None):
        """Récupérer l'horoscope pour un signe donné ou aléatoire"""
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                data = response.json()
                signe = sign if sign else self.getRandomSign()
                if signe in data:
                    message = f"Horoscope du {signe.capitalize()} : {data[signe]}"
                    return message
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None

    def run(self, sign=None):
        """Exécuter le processus principal pour obtenir l'horoscope"""
        horoscope = self.getHoroscope(sign)
        if horoscope:
            print(horoscope)  # Pour le debug dans le terminal
            return horoscope
        return None

# Test de la classe
if __name__ == "__main__":
    horoscope = Horoscope()
    horoscope.run() 