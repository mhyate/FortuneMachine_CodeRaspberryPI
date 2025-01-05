import unittest
from unittest.mock import patch
from Classes.Horoscope import Horoscope

class TestHoroscope(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.horoscope = Horoscope()

    def test_init(self):
        """Test de l'initialisation"""
        self.assertEqual(self.horoscope.api_url, "https://kayoo123.github.io/astroo-api/jour.json")
        self.assertIsInstance(self.horoscope.signes, list)
        self.assertIn("belier", self.horoscope.signes)
        self.assertIn("poissons", self.horoscope.signes)

    def test_getRandomSign(self):
        """Test de la sélection aléatoire d'un signe"""
        signe = self.horoscope.getRandomSign()
        self.assertIn(signe, self.horoscope.signes)

    @patch('requests.get')
    def test_getHoroscope_success(self, mock_get):
        """Test de getHoroscope avec une réponse réussie"""
        mock_response = {
            "belier": "Votre journée sera excellente.",
            "taureau": "Une belle surprise vous attend."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        with patch.object(self.horoscope, 'getRandomSign') as mock_sign:
            mock_sign.return_value = "belier"
            result = self.horoscope.getHoroscope()
            self.assertIn("Horoscope du Belier", result)
            self.assertIn("Votre journée sera excellente", result)

    @patch('requests.get')
    def test_getHoroscope_failure(self, mock_get):
        """Test de getHoroscope avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.horoscope.getHoroscope()
        self.assertIsNone(result)

    @patch('requests.get')
    def test_run_success(self, mock_get):
        """Test de run avec une réponse réussie"""
        mock_response = {
            "belier": "Votre journée sera excellente.",
            "taureau": "Une belle surprise vous attend."
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        with patch.object(self.horoscope, 'getRandomSign') as mock_sign:
            mock_sign.return_value = "belier"
            result = self.horoscope.run()
            self.assertIsNotNone(result)
            self.assertIn("Horoscope du Belier", result)

    @patch('requests.get')
    def test_run_failure(self, mock_get):
        """Test de run avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.horoscope.run()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 