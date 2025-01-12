import requests
import json
import os
from dotenv import load_dotenv

class CNQuotes:
    def __init__(self):
        load_dotenv()  # Chargement des variables d'environnement
        self.url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
        self.headers = {
            "X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
            "accept": "application/json"
        }

    def translate_to_french(self, text):
        url = "https://mymemory.translated.net/api/get"
        params = {
            "q": text,
            "langpair": "en|fr"
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()["responseData"]["translatedText"]
        except Exception as e:
            print(f"Erreur lors de la traduction: {e}")
            return text

    def fetchData(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            quote = data.get("value", "")
            if quote:
                return self.translate_to_french(quote)
            return "Désolé, pas de citation disponible pour le moment"
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return "Erreur lors de la récupération de la citation Chuck Norris"
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            return "Une erreur inattendue s'est produite"

    def run(self):
        quote = self.fetchData()
        print(quote)  # Pour le debug dans le terminal
        return quote

if __name__ == "__main__":
    cnquotes = CNQuotes()
    cnquotes.run()