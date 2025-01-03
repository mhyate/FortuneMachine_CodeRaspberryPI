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

    def WFichier(self, quote):
        """Écriture de la citation dans un fichier"""
        with open("Datas/request_data.txt", "w") as file:
            file.write(quote)

    def fetchData(self):
        try:
            # Envoi de la requête à l'API Chuck Norris
            response = requests.get(self.url, headers=self.headers, timeout=20)
            if response.status_code == 200:
                data = response.json()
                return data.get("value", "") 
            else:
                print("La requête a échoué avec le code de statut:", response.status_code)
                return self.defaultMessage()  
        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête:", e)
            return self.defaultMessage()  
        return None


    def getQuote(self):
        # Récupération de la citation de Chuck Norris et affichage
        quote = self.fetchData()
        if quote:
            print(quote)
            self.WFichier(quote)

    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "N'oubliez pas d'etre heureux !"
    

# Utilisation de la classe ChuckNorrisQuotes
if __name__ == "__main__":
    chuck = CNQuotes()
    chuck.getQuote()
