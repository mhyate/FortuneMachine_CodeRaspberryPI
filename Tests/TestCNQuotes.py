import unittest
from unittest.mock import patch
from Classes.CNQuotes import CNQuotes

class TestCNQuotes(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.cnquotes = CNQuotes()

    def test_init(self):
        """Test de l'initialisation"""
        self.assertEqual(self.cnquotes.url, "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random")
        self.assertIn("X-RapidAPI-Key", self.cnquotes.headers)
        self.assertIn("X-RapidAPI-Host", self.cnquotes.headers)

    @patch('requests.get')
    def test_fetchData_success(self, mock_get):
        """Test de fetchData avec une réponse réussie"""
        mock_response = {
            "value": "Chuck Norris can divide by zero."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Simuler la traduction
        with patch.object(self.cnquotes, 'translate_to_french') as mock_translate:
            mock_translate.return_value = "Chuck Norris peut diviser par zéro."
            result = self.cnquotes.fetchData()
            self.assertEqual(result, "Chuck Norris peut diviser par zéro.")

    @patch('requests.get')
    def test_fetchData_failure(self, mock_get):
        """Test de fetchData avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.cnquotes.fetchData()
        self.assertIsNone(result)

    def test_translate_to_french(self):
        """Test de la traduction"""
        test_text = "Hello"
        with patch('requests.get') as mock_get:
            mock_response = {
                'responseData': {
                    'translatedText': 'Bonjour'
                }
            }
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            
            result = self.cnquotes.translate_to_french(test_text)
            self.assertEqual(result, "Bonjour")

    @patch('requests.get')
    def test_run_success(self, mock_get):
        """Test de run avec une réponse réussie"""
        mock_response = {
            "value": "Chuck Norris can divide by zero."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        with patch.object(self.cnquotes, 'translate_to_french') as mock_translate:
            mock_translate.return_value = "Chuck Norris peut diviser par zéro."
            result = self.cnquotes.run()
            self.assertEqual(result, "Chuck Norris peut diviser par zéro.")

    @patch('requests.get')
    def test_run_failure(self, mock_get):
        """Test de run avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.cnquotes.run()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 