import tkinter as tk
import argparse
import os
import signal
from Interface.Interface import InterfaceGraphique
from communication_pic24 import CommunicationPIC24
from gestion_hibernation import GestionHibernation

def parse_arguments():
    parser = argparse.ArgumentParser(description='Fortune Machine')
    parser.add_argument('--test-mode', action='store_true',
                       help='Active le mode test (sans PIC24)')
    parser.add_argument('--port', default='/dev/ttyUSB0',
                       help='Port série pour la communication avec le PIC24')
    return parser.parse_args()

class FortuneMachine:
    def __init__(self, test_mode=False, port='/dev/ttyUSB0'):
        self.test_mode = test_mode
        self.port = port
        self.interface = None
        self.pic24 = CommunicationPIC24(port=port, test_mode=test_mode)
        self.hibernation = GestionHibernation()
        signal.signal(signal.SIGTERM, self.arreter)
        signal.signal(signal.SIGINT, self.arreter)

    def demarrer(self):
        """Démarre la Fortune Machine"""
        print(f"Démarrage en mode {'test' if self.test_mode else 'production'}")
        
        # Connexion avec le PIC24
        if not self.pic24.connecter():
            if not self.test_mode:
                print("Impossible de se connecter au PIC24")
                return
        
        # Démarrage de l'écoute série
        self.pic24.demarrer_ecoute()
        
        while True:
            try:
                # Attente d'une pièce
                print("En attente d'une pièce...")
                if self.pic24.attendre_piece():
                    # Création et affichage de l'interface
                    self.interface = InterfaceGraphique(printer=self.pic24)
                    self.interface.demarrer()
                    
                    # Réinitialisation pour la prochaine pièce
                    self.pic24.reset()
                    
                    # Si l'interface est fermée, on attend la prochaine pièce
                    if hasattr(self, 'interface'):
                        self.interface.root.destroy()
                        self.interface = None
                
            except Exception as e:
                print(f"Erreur : {e}")
                if not self.test_mode:
                    # En production, on continue d'attendre
                    continue
                else:
                    # En mode test, on arrête
                    break

    def arreter(self, signum=None, frame=None):
        """Arrête proprement la Fortune Machine"""
        print("\nArrêt de la Fortune Machine...")
        if self.pic24:
            self.pic24.arreter()
        if self.interface:
            self.interface.root.quit()

if __name__ == "__main__":
    args = parse_arguments()
    fortune_machine = FortuneMachine(test_mode=args.test_mode, port=args.port)
    fortune_machine.demarrer()
