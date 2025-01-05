import unittest
from unittest.mock import patch
from Classes.Blagues import Blagues

class TestBlagues(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.blagues = Blagues()

    def test_init(self):
        """Test de l'initialisation"""
        self.assertEqual(self.blagues.api_url, "https://v2.jokeapi.dev/joke/Any?lang=fr")

    @patch('requests.get')
    def test_getJoke_success_single(self, mock_get):
        """Test de getJoke avec une blague simple"""
        mock_response = {
            "error": False,
            "type": "single",
            "joke": "Une blague simple"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = self.blagues.getJoke()
        self.assertIsNotNone(result)
        self.assertIn("Une blague simple", result)
        self.assertIn("😄", result)

    @patch('requests.get')
    def test_getJoke_success_twopart(self, mock_get):
        """Test de getJoke avec une blague en deux parties"""
        mock_response = {
            "error": False,
            "type": "twopart",
            "setup": "La question",
            "delivery": "La réponse"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = self.blagues.getJoke()
        self.assertIsNotNone(result)
        self.assertIn("La question", result)
        self.assertIn("La réponse", result)
        self.assertIn("😄", result)
        self.assertIn("😎", result)

    @patch('requests.get')
    def test_getJoke_failure(self, mock_get):
        """Test de getJoke avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.blagues.getJoke()
        self.assertIsNone(result)

    @patch('requests.get')
    def test_run_success(self, mock_get):
        """Test de run avec une réponse réussie"""
        mock_response = {
            "error": False,
            "type": "single",
            "joke": "Une blague simple"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = self.blagues.run()
        self.assertIsNotNone(result)
        self.assertIn("Une blague simple", result)

    @patch('requests.get')
    def test_run_failure(self, mock_get):
        """Test de run avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.blagues.run()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 