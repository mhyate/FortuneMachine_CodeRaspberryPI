import requests

class CNQuotes:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
        self.headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": "a1892cd212msh8d5e1cbeb4e4215p1ec1f6jsn839276332c9f",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }
        self.translate_url = "https://api.mymemory.translated.net/get"

    def translate_to_french(self, text):
        """Traduire le texte en français en utilisant l'API MyMemory"""
        try:
            params = {
                'q': text,
                'langpair': 'en|fr'
            }
            response = requests.get(self.translate_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data['responseData']['translatedText']
            return text
        except Exception as e:
            print(f"Erreur de traduction: {e}")
            return text

    def fetchData(self):
        try:
            response = requests.get(self.url, headers=self.headers, timeout=20)
            if response.status_code == 200:
                data = response.json()
                quote = data.get("value", "")
                if quote:
                    translated_quote = self.translate_to_french(quote)
                    return translated_quote
            return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None

    def run(self):
        """Exécuter le processus principal pour obtenir une citation traduite"""
        quote = self.fetchData()
        if quote:
            print(quote)  # Pour le debug dans le terminal
            return quote
        return None

# Test de la classe
if __name__ == "__main__":
    chuck = CNQuotes()
    chuck.run()