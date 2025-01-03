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
        with open("Datas/request_data.json", "r") as file:
            data = json.load(file)
            ingredients_text = data.get('product', {}).get('ingredients_text_en', '')

            if ingredients_text:
                keywords = [word.strip() for word in ingredients_text.split(',')]
               #keywords = [word.strip() for word in keywords_list.replace("ingredients_text_en':", "").replace("'", "").replace("(", "").replace(")", "").split(",")]
                random_keyword = random.choice(keywords).strip()

                fortune = f"Ajouter du {random_keyword} à votre recette aujourd'hui apportera une saveur inoubliable et une touche de magie !"
                print(fortune)
            else:
                print("La mention 'ingredients_text_en' n'a pas été trouvée dans le fichier.")

    def fetchData(self):
        """Récupérer les données de l'API"""
        try:
            response = requests.get(self.url, timeout=20)
            if response.status_code == 200:
                data = response.json()

                self.WFichier(data)
                self.findIngredient()
            else:
                print("La requête a échoué avec le code de statut:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête:", e)
            return None

    def getQuote(self):
        """Obtenir et traduire une citation"""
        quote = self.fetchData()
        if quote:
                print(quote)
                self.WFichier(quote)
        else:
            self.WFichier(quote)

    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "Food"

    def run(self):
        """Exécution code principal pour obtenir requète."""
        sante = FoodOK()
        description = sante.getQuote()
        if description:
            print(description)
        #else:
            #print(self.defaultMessage())    

if __name__ == "__main__":
    api = FoodOK()
    api.getQuote()

    








