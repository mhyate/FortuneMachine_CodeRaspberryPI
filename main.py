import tkinter as tk
from ControlePiece import LecteurPiece
from ImpressionTicket import TicketPrinter
import adafruit_thermal_printer
import serial
import os
import threading
import time
from Interface.Interface import InterfaceGraphique
from gestion_hibernation import GestionHibernation

# Détection automatique du port série
def detect_serial_port():
    if os.name == 'posix':  # Pour Mac ou Linux (incluant Raspberry Pi)
        possible_ports = ["/dev/serial0", "/dev/ttyAMA0", "/dev/ttyS0", "/dev/tty.Bluetooth-Incoming-Port", "/dev/tty.debug-console"]
        for port in possible_ports:
            if os.path.exists(port):
                try:
                    with serial.Serial(port, baudrate=19200, timeout=1) as test_port:
                        return port
                except serial.SerialException:
                    continue
    return None

class CommunicationPIC24:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.piece_validee = False
        
    def connecter(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connexion établie avec le PIC24 sur {self.port}")
            return True
        except Exception as e:
            print(f"Erreur de connexion avec le PIC24: {e}")
            return False
    
    def lire_piece(self):
        if not self.serial:
            return False
        try:
            if self.serial.in_waiting:
                message = self.serial.readline().decode('utf-8').strip()
                if message == "PIECE_VALIDEE":
                    self.piece_validee = True
                    return True
            return False
        except Exception as e:
            print(f"Erreur de lecture: {e}")
            return False
    
    def envoyer_commande_impression(self, message):
        if not self.serial:
            return False
        try:
            commande = f"IMPRIMER:{message}\n"
            self.serial.write(commande.encode('utf-8'))
            return True
        except Exception as e:
            print(f"Erreur d'envoi: {e}")
            return False

def surveillance_inactivite(gestion_hibernation):
    while True:
        gestion_hibernation.verifier_inactivite()
        time.sleep(10)  # Vérifier toutes les 10 secondes

# Configuration initiale
serial_port = detect_serial_port()
if serial_port:
    print(f"Port série détecté : {serial_port}")
    uart = serial.Serial(serial_port, baudrate=19200, timeout=3000)
    printer = adafruit_thermal_printer.get_printer_class(2.69)(uart)
else:
    print("Aucun port série disponible. L'interface fonctionnera sans le matériel.")
    printer = None

# Initialisation de la gestion d'hibernation
gestion_hibernation = GestionHibernation(delai_inactivite=300000)  # 5 minutes

# Démarrage du thread de surveillance d'inactivité
thread_surveillance = threading.Thread(target=surveillance_inactivite, args=(gestion_hibernation,), daemon=True)
thread_surveillance.start()

if __name__ == "__main__":
    # Initialisation de la communication avec le PIC24
    pic24_com = CommunicationPIC24("/dev/ttyUSB0")  # Ajuster le port selon votre configuration
    if pic24_com.connecter():
        print("Communication établie avec le PIC24")
    
    # Création et démarrage de l'interface
    interface = InterfaceGraphique(printer)
    
    # Fonction de vérification périodique des pièces
    def verifier_piece():
        if pic24_com.lire_piece():
            gestion_hibernation.reset_timer()  # Réinitialiser le timer d'hibernation
            interface.afficher_menu()  # Afficher l'interface quand une pièce est détectée
        interface.root.after(100, verifier_piece)  # Vérifier toutes les 100ms
    
    verifier_piece()  # Démarrer la vérification
    interface.demarrer()
