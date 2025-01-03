import requests
import json
import random


class Hearth:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cardbacks"
        self.headers = {
            "X-RapidAPI-Key": "a1892cd212msh8d5e1cbeb4e4215p1ec1f6jsn839276332c9f",
            "X-RapidAPI-Host": "omgvamp-hearthstone-v1.p.rapidapi.com"
        }
 
    def findDescription(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                with open("Datas/hearth_data.txt", "w", encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                return self.getQuote()
            else:
                print("La requête a échoué avec le code de statut:", response.status_code)
                return self.defaultMessage()
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête:", e)
            return self.defaultMessage()

    def getQuote(self):
        quotes = []
        try:
            with open("Datas/hearth_data.txt", "r", encoding='utf-8') as file:
                data = json.load(file)

            for item in data:
                if len(quotes) >= 9:  # Arrêter la recherche lorsque 9 descriptions sont trouvées
                    break
                if 'description' in item:
                    quote = item['description'].strip()
                    quotes.append(quote)

        except FileNotFoundError:
            print("Le fichier n'a pas été trouvé.")
            return self.defaultMessage()
        except Exception as e:
            print(f"Une erreur est survenue: {e}")
            return self.defaultMessage()

        if not quotes:
            return None  # self.defaultMessage()

        selected_quote = random.choice(quotes)
        return selected_quote



    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "Hearth"

    def run(self):
        """Exécuter le processus principal pour obtenir citation traduite."""
        description = self.findDescription()

        if description:
            print("description",description)
        #else:
            #print(self.defaultMessage())
        
# Utilisation de la classe HearthStone
if __name__ == "__main__":
    cartes = Hearth()
    description = cartes.findDescription()

    if description:
        print(description)
        
