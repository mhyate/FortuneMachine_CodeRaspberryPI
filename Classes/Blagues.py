import requests
import json

class Blagues:
    def __init__(self):
        """Initialisation de l'URL de l'API"""
        self.api_url = "https://v2.jokeapi.dev/joke/Any?lang=fr"

    def getJoke(self):
        """Récupérer une blague aléatoire"""
        try:
            print("Envoi de la requête à l'API...")  # Debug
            response = requests.get(self.api_url)
            print(f"Code de réponse: {response.status_code}")  # Debug

            if response.status_code == 200:
                data = response.json()
                print(f"Données JSON reçues: {json.dumps(data, indent=2)}")  # Debug
                
                if data.get('type') == 'single':
                    # Blague simple
                    joke = data.get('joke', '')
                    formatted_joke = f"😄 Blague :\n{joke}"
                else:
                    # Blague avec setup et punchline
                    setup = data.get('setup', '')
                    delivery = data.get('delivery', '')
                    formatted_joke = f"😄 Question :\n{setup}\n\n😎 Réponse :\n{delivery}"

                print(f"Blague formatée: {formatted_joke}")  # Debug
                return formatted_joke
            
            print(f"Erreur API: {response.status_code}")  # Debug
            return None
        except Exception as e:
            print(f"Erreur lors de la requête: {str(e)}")  # Debug
            return None

    def run(self):
        """Exécuter le processus principal pour obtenir une blague"""
        blague = self.getJoke()
        if blague:
            return blague
        return None

# Test de la classe
if __name__ == "__main__":
    blagues = Blagues()
    resultat = blagues.run()
    print("\nRésultat final:", resultat) 