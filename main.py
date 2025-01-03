import tkinter as tk
from ControlePiece import LecteurPiece
from ImpressionTicket import TicketPrinter
import adafruit_thermal_printer
import serial
import os
from Interface.Interface import InterfaceGraphique

if __name__ == "__main__":
    interface = InterfaceGraphique()
    interface.demarrer()

# Détection automatique du port série
def detect_serial_port():
    if os.name == 'posix':  # Pour Mac ou Linux (incluant Raspberry Pi)
        possible_ports = ["/dev/serial0", "/dev/ttyAMA0", "/dev/ttyS0", "/dev/tty.Bluetooth-Incoming-Port", "/dev/tty.debug-console"]
        for port in possible_ports:
            if os.path.exists(port):
                try:
                    # Teste si le port peut être ouvert
                    with serial.Serial(port, baudrate=19200, timeout=1) as test_port:
                        return port
                except serial.SerialException:
                    continue
    return None

# Détection et configuration du port série
serial_port = detect_serial_port()
if not serial_port:
    print("Aucun port série valide détecté. Vérifiez les connexions.")
    serial_port = None

if serial_port:
    print(f"Port série détecté : {serial_port}")
    uart = serial.Serial(serial_port, baudrate=19200, timeout=3000)
else:
    print("Aucun port série disponible. L'interface fonctionnera sans le matériel.")

TEMPSLED = 3

def flashLeds():
    print("Clignotement des LEDs simulé.")  # Pour l'instant, c'est une simulation
    return TEMPSLED

# Initialisation de l'imprimante thermique
if serial_port:
    ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
    printer = ThermalPrinter(uart)
else:
    printer = None

if __name__ == "__main__":
    lecteur = LecteurPiece()

    if lecteur:
        # Lancement de l'interface pour le choix du thème
        theme_choisi = DisplayChoixTheme()

        # Demander ce qu'il faut faire (afficher ou imprimer)
        handle_fortune_request(theme_choisi, printer)
    else:
        # Si aucune pièce n'est détectée
        print("Aucune pièce détectée.")
