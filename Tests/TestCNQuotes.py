import unittest
import os
from unittest.mock import patch, MagicMock
from Classes.CNQuotes import CNQuotes
import requests

class TestCNQuotes(unittest.TestCase):
    def setUp(self):
        # Simuler une clé API pour les tests
        os.environ["RAPID_API_KEY"] = "test_api_key"
        self.cnquotes = CNQuotes()

    def test_init(self):
        self.assertEqual(self.cnquotes.url, "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random")
        self.assertIn("X-RapidAPI-Key", self.cnquotes.headers)
        self.assertEqual(self.cnquotes.headers["X-RapidAPI-Key"], "test_api_key")

    @patch('requests.get')
    def test_fetchData_success(self, mock_get):
        # Simuler une réponse réussie de l'API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": "Chuck Norris can divide by zero."}
        mock_get.return_value = mock_response

        result = self.cnquotes.fetchData()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    @patch('requests.get')
    def test_fetchData_empty_response(self, mock_get):
        # Simuler une réponse vide de l'API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": ""}
        mock_get.return_value = mock_response

        result = self.cnquotes.fetchData()
        self.assertEqual(result, "Désolé, pas de citation disponible pour le moment")

    @patch('requests.get')
    def test_fetchData_network_error(self, mock_get):
        # Simuler une erreur réseau
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        result = self.cnquotes.fetchData()
        self.assertEqual(result, "Erreur lors de la récupération de la citation Chuck Norris")

    @patch('requests.get')
    def test_fetchData_unexpected_error(self, mock_get):
        # Simuler une erreur inattendue
        mock_get.side_effect = Exception("Unexpected Error")
        result = self.cnquotes.fetchData()
        self.assertEqual(result, "Une erreur inattendue s'est produite")

    @patch('requests.get')
    def test_translate_to_french(self, mock_get):
        # Simuler une réponse réussie de l'API de traduction
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "responseData": {"translatedText": "Chuck Norris peut diviser par zéro."}
        }
        mock_get.return_value = mock_response

        result = self.cnquotes.translate_to_french("Chuck Norris can divide by zero.")
        self.assertEqual(result, "Chuck Norris peut diviser par zéro.")

    @patch('requests.get')
    def test_translate_error(self, mock_get):
        # Simuler une erreur de traduction
        mock_get.side_effect = Exception("Translation Error")
        text = "Test text"
        result = self.cnquotes.translate_to_french(text)
        self.assertEqual(result, text)  # Devrait retourner le texte original en cas d'erreur

    def tearDown(self):
        # Nettoyer les variables d'environnement après les tests
        if "RAPID_API_KEY" in os.environ:
            del os.environ["RAPID_API_KEY"]

if __name__ == '__main__':
    unittest.main() 