import unittest
from unittest.mock import patch, MagicMock
import os
import serial
import sys
from main import detect_serial_port, TEMPSLED, flashLeds

class TestMain(unittest.TestCase):
    @patch('os.path.exists')
    @patch('serial.Serial')
    def test_detect_serial_port_success(self, mock_serial, mock_exists):
        """Test de la détection réussie d'un port série"""
        # Simuler l'existence d'un port
        mock_exists.return_value = True
        # Simuler une connexion série réussie
        mock_serial.return_value.__enter__.return_value = MagicMock()

        # Test avec un système POSIX (Mac/Linux/Raspberry Pi)
        with patch('os.name', 'posix'):
            port = detect_serial_port()
            self.assertIsNotNone(port)
            self.assertIn(port, ["/dev/serial0", "/dev/ttyAMA0", "/dev/ttyS0", 
                               "/dev/tty.Bluetooth-Incoming-Port", "/dev/tty.debug-console"])

    @patch('os.path.exists')
    def test_detect_serial_port_no_ports(self, mock_exists):
        """Test quand aucun port série n'est disponible"""
        # Simuler qu'aucun port n'existe
        mock_exists.return_value = False

        # Test avec un système POSIX
        with patch('os.name', 'posix'):
            port = detect_serial_port()
            self.assertIsNone(port)

    @patch('os.path.exists')
    @patch('serial.Serial')
    def test_detect_serial_port_error(self, mock_serial, mock_exists):
        """Test quand il y a une erreur lors de l'ouverture du port"""
        # Simuler l'existence d'un port
        mock_exists.return_value = True
        # Simuler une erreur lors de l'ouverture
        mock_serial.side_effect = serial.SerialException()

        # Test avec un système POSIX
        with patch('os.name', 'posix'):
            port = detect_serial_port()
            self.assertIsNone(port)

    def test_flash_leds(self):
        """Test de la fonction flashLeds"""
        # Pour l'instant, cette fonction est simulée
        temps = flashLeds()
        self.assertEqual(temps, TEMPSLED)

    @patch('serial.Serial')
    @patch('os.path.exists')
    def test_printer_initialization(self, mock_exists, mock_serial):
        """Test de l'initialisation de l'imprimante"""
        # Test avec port série disponible
        mock_exists.return_value = True
        mock_serial.return_value = MagicMock()
        
        # Sauvegarder les modules importés
        saved_modules = dict(sys.modules)
        
        try:
            # Forcer la réimportation de main
            if 'main' in sys.modules:
                del sys.modules['main']
            import main
            self.assertIsNotNone(main.serial_port)
            self.assertIsNotNone(main.printer)
        finally:
            # Restaurer les modules
            sys.modules.clear()
            sys.modules.update(saved_modules)

    @patch('os.path.exists')
    def test_printer_initialization_no_port(self, mock_exists):
        """Test de l'initialisation sans port série"""
        # Simuler qu'aucun port n'existe
        mock_exists.return_value = False
        
        # Sauvegarder les modules importés
        saved_modules = dict(sys.modules)
        
        try:
            # Forcer la réimportation de main
            if 'main' in sys.modules:
                del sys.modules['main']
            import main
            self.assertIsNone(main.printer)
        finally:
            # Restaurer les modules
            sys.modules.clear()
            sys.modules.update(saved_modules)

if __name__ == '__main__':
    unittest.main() 