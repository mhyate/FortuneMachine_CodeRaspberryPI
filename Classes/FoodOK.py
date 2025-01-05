import random
import requests
import os
import json

class FoodOK:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"

    def WFichier(self, data):
        """Écriture des données dans un fichier"""
        os.makedirs("Datas", exist_ok=True)
        with open("Datas/request_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def findIngredient(self):
        """Trouver un ingrédient aléatoire et générer un message"""
        try:
            with open("Datas/request_data.json", "r") as file:
                data = json.load(file)
                ingredients_text = data.get('product', {}).get('ingredients_text_en', '')

                if ingredients_text:
                    keywords = [word.strip() for word in ingredients_text.split(',')]
                    random_keyword = random.choice(keywords).strip()
                    fortune = f"Ajouter du {random_keyword} à votre recette aujourd'hui apportera une saveur inoubliable et une touche de magie !"
                    print(fortune)  # Pour le debug
                    return fortune
                else:
                    return self.defaultMessage()
        except Exception as e:
            print(f"Erreur lors de la lecture des ingrédients: {e}")
            return self.defaultMessage()

    def fetchData(self):
        """Récupérer les données de l'API"""
        try:
            response = requests.get(self.url, timeout=20)
            if response.status_code == 200:
                data = response.json()
                self.WFichier(data)
                return self.findIngredient()
            else:
                print("La requête a échoué avec le code de statut:", response.status_code)
                return self.defaultMessage()
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête:", e)
            return self.defaultMessage()

    def getQuote(self):
        """Obtenir un conseil santé"""
        message = self.fetchData()
        print(message)  # Pour le debug
        return message

    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "Serveur momentanément indisponible"

    def run(self):
        """Exécution code principal pour obtenir requète."""
        message = self.getQuote()
        if message:
            print("Message santé:", message)  # Pour le debug
            return message
        return self.defaultMessage()

if __name__ == "__main__":
    api = FoodOK()
    api.getQuote()

    








