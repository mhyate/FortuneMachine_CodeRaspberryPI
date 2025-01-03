import requests
import random
import json
import re

class UrbanDico:
    def __init__(self):
        """Initialisation de l'URL de l'API et des en-têtes requis"""
        self.base_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        self.headers = {
            "X-RapidAPI-Key": "a1892cd212msh8d5e1cbeb4e4215p1ec1f6jsn839276332c9f",
            "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        self.terms = ["Cool", "Space", "Love", "Peace", "Happy", "Sad", "Home"]
        self.all_sentences = []

    def chooseRdmTerm(self):
        """Choisir un terme aléatoire de la liste des termes"""
        return random.choice(self.terms)

    def findDescription(self):
        """Trouver une description pour un terme choisi aléatoirement et obtenir une citation traduite."""
        try:
            term = self.chooseRdmTerm()
            response = self.fetchDefinition(term)
            if response:
                return self.getQuote(response)
            else:
                return None #self.defaultMessage()
        except Exception as e:
            print(f"Erreur dans findDescription: {e}")
            return self.defaultMessage()

    def fetchDefinition(self, term):
        """Récupérer la définition du terme à partir de l'API Urban Dictionary."""
        try:
            querystring = {"term": term}
            response = requests.get(self.base_url, headers=self.headers, params=querystring)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur de requête : {e}")
            return None

    def getQuote(self, response):
        """Extraire et retourner une citation traduite à partir de la réponse de l'API."""
        try:
            descriptions = [item['definition'] for item in response.get('list', [])]
            sentences = self.extractSentences(descriptions)
            if sentences:
                random_sentence = random.choice(sentences).strip()
                clean_sentence = self.clean_sentence(random_sentence)
                return clean_sentence
            else:
                return self.defaultMessage()
        except KeyError as e:
            print(f"Erreur de clé : {e}")
            return self.defaultMessage()

    def extractSentences(self, descriptions):
        """Extraire et nettoyer les phrases à partir de la liste des descriptions."""
        sentences = []
        for description in descriptions:
            sentences.extend(description.split('.'))
        return sentences

    def clean_sentence(self, sentence):
        """Nettoyer une phrase en supprimant les parenthèses et crochets."""
        sentence = re.sub(r'\[.*?\]|\(.*?\)', '', sentence)
        sentence = sentence.strip()
        return sentence

    def defaultMessage(self):
        """Retourner un message par défaut."""
        return "Coucou !"

    def run(self):
        """Exécuter le processus principal pour obtenir citation traduite."""
        description = self.findDescription()
        print(description)

# Utilisation de la classe UrbanDico avec une interface
if __name__ == "__main__":
    urban_dico = UrbanDico()
    urban_dico.run()
