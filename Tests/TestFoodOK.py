import unittest
from unittest.mock import patch, mock_open
import requests
from Classes.FoodOK import FoodOK  # Assurez-vous que votre fichier de classe FoodOK s'appelle FoodOK.py

class TestFoodOK(unittest.TestCase):
    def setUp(self):
        """Initialise les conditions avant chaque test"""
        self.foodok = FoodOK()

    @patch("builtins.open", new_callable=mock_open, read_data='{"product": {"ingredients_text_en": "sugar, salt, pepper"}}')
    def test_findIngredient(self, mock_file):
        """Tester la méthode findIngredient"""
        self.foodok.findIngredient()
        # Nous ne pouvons pas vérifier la sortie console directement avec unittest
        # Cependant, nous pouvons tester le flux de travail et les appels de fonctions
        # Vous pouvez étendre ce test pour vérifier les traductions si besoin

    @patch("requests.get")
    def test_fetchData_success(self, mock_get):
        """Tester fetchData avec une réponse réussie"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"product": {"ingredients_text_en": "sugar, salt, pepper"}}
        self.foodok.fetchData()
        # Vérifier que les données sont écrites correctement
        with open("Datas/request_data.json", "r") as file:
            data = file.read()
            self.assertIn("sugar", data)

    @patch("requests.get")
    def test_fetchData_failure(self, mock_get):
        """Tester fetchData avec une réponse échouée"""
        mock_get.return_value.status_code = 404
        self.foodok.fetchData()
        # Vous pouvez vérifier si la sortie console affiche l'erreur

    @patch("googletrans.Translator.translate")
    def test_translateFortune(self, mock_translate):
        """Tester la méthode translateFortune"""
        mock_translate.return_value.text = "sucre"
        result = self.foodok.translateFortune("sugar")
        self.assertEqual(result, "sucre")

if __name__ == "__main__":
    unittest.main()
