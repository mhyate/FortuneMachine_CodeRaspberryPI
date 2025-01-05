import unittest
from unittest.mock import patch
from Classes.Meteotry import Meteotry

class TestMeteotry(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.meteo = Meteotry()

    def test_init(self):
        """Test de l'initialisation"""
        self.assertEqual(self.meteo.latitude, 47.3941)  # Coordonnées de Tours
        self.assertEqual(self.meteo.longitude, 0.6848)
        self.assertEqual(self.meteo.api_url, "https://api.open-meteo.com/v1/forecast")

    @patch('requests.get')
    def test_getWeather_success(self, mock_get):
        """Test de getWeather avec une réponse réussie"""
        # Simuler une réponse réussie de l'API
        mock_response = {
            'current': {
                'temperature_2m': 20.5,
                'relative_humidity_2m': 65,
                'weather_code': 1
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = self.meteo.getWeather()
        self.assertEqual(result, mock_response)

    @patch('requests.get')
    def test_getWeather_failure(self, mock_get):
        """Test de getWeather avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.meteo.getWeather()
        self.assertIsNone(result)

    def test_get_weather_description(self):
        """Test des descriptions météo"""
        self.assertEqual(self.meteo.get_weather_description(0), "Ciel dégagé")
        self.assertEqual(self.meteo.get_weather_description(1), "Principalement dégagé")
        self.assertEqual(self.meteo.get_weather_description(999), "Conditions météorologiques inconnues")

    @patch('requests.get')
    def test_displayWeather_success(self, mock_get):
        """Test de displayWeather avec une réponse réussie"""
        mock_response = {
            'current': {
                'temperature_2m': 20.5,
                'relative_humidity_2m': 65,
                'weather_code': 1
            }
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = self.meteo.displayWeather()
        self.assertIsNotNone(result)
        self.assertIn("Tours", result)
        self.assertIn("20.5°C", result)
        self.assertIn("65%", result)
        self.assertIn("Principalement dégagé", result)

    @patch('requests.get')
    def test_displayWeather_failure(self, mock_get):
        """Test de displayWeather avec une erreur"""
        mock_get.return_value.status_code = 404
        result = self.meteo.displayWeather()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main() 