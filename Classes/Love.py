import requests
import random

class Love:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.url = "https://love-calculator.p.rapidapi.com/getPercentage"
        self.headers = {
            "X-RapidAPI-Key": "a1892cd212msh8d5e1cbeb4e4215p1ec1f6jsn839276332c9f",
            "X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
        }
        self.liste_de_noms = [
            "Alice", "Bob", "Charlie", "David", "Eva",
            "Fabrice", "Gabrielle", "Hector", "Isabelle", "Jack",
            "Kevin", "Léa", "Marianne", "Nicolas", "Olivia",
            "Pierre", "Quentin", "Roxane", "Simon", "Tatiana",
            "Ulysse", "Valentine", "Wendy", "Xavier", "Yasmine",
            "Zoé", "Arthur", "Bérénice", "Cédric", "Daphné",
            "Étienne", "Flora", "Gaston", "Hélène", "Ignace",
            "Jade", "Kilian", "Lola", "Maxime", "Nadège",
            "Olivier", "Pauline", "Quentin", "Rachel", "Sébastien",
            "Thaïs", "Ugo", "Victor", "Wendy", "Xavier",
            "Yann", "Zélie"
        ]

    def chooseRdmName(self):
        return random.choice(self.liste_de_noms)

    def getQuote(self, name1=None, name2=None):
        if not name1:
            name1 = self.chooseRdmName()
        if not name2:
            name2 = self.chooseRdmName()
        querystring = {"sname": name1, "fname": name2}
        try:
            response = requests.get(self.url, headers=self.headers, params=querystring, timeout=10)
            response.raise_for_status()  # Ensure an HTTPError is raised for bad responses
            data = response.json()
            
            return {
                "percentage": data.get("percentage"),
                "result": data.get("result")
            }
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête: {e}")
            return None

    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "Serveur momentanément indisponible"
    
    def run(self):
        """Exécuter le processus principal pour obtenir la prédiction d'amour."""
        result = self.getQuote()
        if result and 'result' in result:
            message = f"Compatibilité amoureuse : {result['percentage']}% - {result['result']}"
            print(message)
            return message
        else:
            message = "L'amour est dans l'air ! Gardez votre cœur ouvert aux possibilités."
            print(message)
            return message


if __name__ == "__main__":
    love_calculator = Love()
    love_result = love_calculator.getQuote()
    if love_result and 'result' in love_result:
        print(f"We wish you {love_result['result']}")
    else:
        print(love_calculator.defaultMessage())
