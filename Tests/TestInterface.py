import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from Interface.Interface import InterfaceGraphique

class TestInterface(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.interface = InterfaceGraphique()

    def tearDown(self):
        """Nettoyage après chaque test"""
        if hasattr(self, 'interface'):
            self.interface.root.destroy()

    def test_init(self):
        """Test de l'initialisation"""
        self.assertIsInstance(self.interface.root, tk.Tk)
        self.assertEqual(self.interface.root.title(), "Choisissez le thème de votre fortune")
        self.assertIsInstance(self.interface.canvas, tk.Canvas)
        self.assertIsInstance(self.interface.button_frame, tk.Frame)

    def test_afficher_message(self):
        """Test de l'affichage d'un message"""
        test_message = "Test message"
        self.interface.afficher_message(test_message)
        
        # Vérifier que le message est affiché
        widgets = self.interface.button_frame.winfo_children()
        self.assertTrue(any(isinstance(w, tk.Label) and w.cget("text") == test_message for w in widgets))
        
        # Vérifier que le bouton retour est présent
        self.assertTrue(any(isinstance(w, tk.Button) and w.cget("text") == "Retour" for w in widgets))

    def test_recuperer_message_api(self):
        """Test de la récupération des messages des APIs"""
        # Test de la météo
        message_meteo = self.interface.recuperer_message_api("Météo")
        self.assertIsNotNone(message_meteo)
        self.assertIn("Tours", message_meteo)
        self.assertIn("°C", message_meteo)
        self.assertIn("Humidité", message_meteo)

        # Test de Chuck Norris
        message_cn = self.interface.recuperer_message_api("Chuck Norris")
        self.assertIsNotNone(message_cn)

        # Test de l'horoscope
        message_horoscope = self.interface.recuperer_message_api("Horoscope")
        self.assertIsNotNone(message_horoscope)
        self.assertIn("Horoscope", message_horoscope)

        # Test des blagues
        message_blague = self.interface.recuperer_message_api("Blagues")
        self.assertIsNotNone(message_blague)

    def test_imprimer_fortune(self):
        """Test de l'impression d'une fortune"""
        # Test sans imprimante
        test_message = "Test message"
        self.interface.imprimer_fortune(test_message)
        
        # Vérifier le message d'erreur
        widgets = self.interface.button_frame.winfo_children()
        self.assertTrue(any(isinstance(w, tk.Label) and "Aucune imprimante connectée" in w.cget("text") for w in widgets))

        # Test avec une imprimante mock
        mock_printer = MagicMock()
        self.interface.printer = mock_printer
        self.interface.imprimer_fortune(test_message)
        
        mock_printer.print.assert_called_once_with(test_message)
        mock_printer.feed.assert_called_once_with(2)

    def test_reinitialiser_interface(self):
        """Test de la réinitialisation de l'interface"""
        # D'abord afficher un message
        self.interface.afficher_message("Test message")
        
        # Puis réinitialiser
        self.interface.reinitialiser_interface()
        
        # Vérifier que les boutons des thèmes sont présents
        widgets = self.interface.button_frame.winfo_children()
        themes = ["Météo", "Chuck Norris", "Horoscope", "Blagues"]
        for theme in themes:
            self.assertTrue(any(isinstance(w, tk.Button) and w.cget("text") == theme for w in widgets))

if __name__ == '__main__':
    unittest.main() 