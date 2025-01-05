import requests

class Blagues:
    def __init__(self):
        """Initialisation de l'URL de l'API et du token"""
        self.api_url = "https://www.blagues-api.fr/api/random"
        self.headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTY5ODg1NTM1NTI5NzE4NTI4MCIsImxpbWl0IjoxMDAsImtleSI6ImlCNEFyTUdYZERZWUhzTDhpb0J6UHV2VGxBVWJHN0tJVWxmZDd2VjBGU2JISVpwWWpOIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDEtMjlUMTY6NDI6MzUrMDA6MDAiLCJpYXQiOjE3MDY1NDc3NTV9.dxDQn8NHbHqwcQqwPqUVNXQCAYGGPvZyEoXXtGNMxYY"
        }

    def getJoke(self):
        """Récupérer une blague aléatoire"""
        try:
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                data = response.json()
                joke = f"{data['joke']}\n- {data['answer']}"
                return joke
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None

    def run(self):
        """Exécuter le processus principal pour obtenir une blague"""
        blague = self.getJoke()
        if blague:
            print(blague)  # Pour le debug dans le terminal
            return blague
        return None

# Test de la classe
if __name__ == "__main__":
    blagues = Blagues()
    blagues.run() 