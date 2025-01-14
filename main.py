import tkinter as tk
import argparse
import os
import signal
import platform
import traceback
from Interface.Interface import InterfaceGraphique
from communication_pic24 import CommunicationPIC24
from gestion_hibernation import GestionHibernation

def parse_arguments():
    parser = argparse.ArgumentParser(description='Fortune Machine')
    parser.add_argument('--port', help='Port série pour la communication avec le PIC24')
    return parser.parse_args()

class FortuneMachine:
    def __init__(self, port=None):
        print("Initialisation de la Fortune Machine...")
        try:
            # Détermination automatique du port selon le système
            if port is None:
                if platform.system() == 'Darwin':  # macOS
                    port = '/dev/tty.usbserial'  # Port par défaut sur Mac
                else:  # Raspberry Pi
                    port = '/dev/ttyUSB0'  # Port par défaut sur Raspberry
            print(f"Port sélectionné : {port}")
            
            self.port = port
            self.interface = None
            print("Initialisation de la communication PIC24...")
            self.pic24 = CommunicationPIC24(port=port, test_mode=True)
            print("Initialisation de la gestion d'hibernation...")
            self.hibernation = GestionHibernation()
            
            # Configuration des gestionnaires de signaux
            signal.signal(signal.SIGTERM, self.arreter)
            signal.signal(signal.SIGINT, self.arreter)
            print("Initialisation terminée.")
            
        except Exception as e:
            print(f"Erreur lors de l'initialisation : {e}")
            print(traceback.format_exc())
            raise

    def demarrer(self):
        """Démarre la Fortune Machine"""
        try:
            print("\nDémarrage de la Fortune Machine...")
            
            # Connexion avec le PIC24 (simulée pour le moment)
            print("\nTentative de connexion au PIC24...")
            if not self.pic24.connecter():
                print("Mode test : continue sans PIC24")
            
            # Démarrage de l'écoute série
            print("\nDémarrage de l'écoute série...")
            self.pic24.demarrer_ecoute()
            
            print("\nFortune Machine prête !")
            
            while True:
                try:
                    # Attente d'une pièce (simulée pour le moment)
                    print("\nEn attente d'une pièce...")
                    if self.pic24.attendre_piece():
                        print("\nPièce détectée, lancement de l'interface...")
                        # Création et affichage de l'interface
                        self.interface = InterfaceGraphique(printer=self.pic24)
                        self.interface.demarrer()
                        
                        # Réinitialisation pour la prochaine pièce
                        print("\nRéinitialisation pour la prochaine pièce...")
                        self.pic24.reset()
                        
                        # Si l'interface est fermée, on attend la prochaine pièce
                        if hasattr(self, 'interface'):
                            print("\nFermeture de l'interface...")
                            self.interface.root.destroy()
                            self.interface = None
                    
                except Exception as e:
                    print(f"\nErreur pendant l'exécution : {e}")
                    print(traceback.format_exc())
                    continue

        except Exception as e:
            print(f"\nErreur fatale : {e}")
            print(traceback.format_exc())
            self.arreter()

    def arreter(self, signum=None, frame=None):
        """Arrête proprement la Fortune Machine"""
        print("\nArrêt de la Fortune Machine...")
        try:
            if self.pic24:
                print("Arrêt de la communication PIC24...")
                self.pic24.arreter()
            if self.interface:
                print("Fermeture de l'interface...")
                self.interface.root.quit()
        except Exception as e:
            print(f"Erreur lors de l'arrêt : {e}")
            print(traceback.format_exc())

if __name__ == "__main__":
    try:
        print("\n=== Démarrage du programme Fortune Machine ===\n")
        args = parse_arguments()
        fortune_machine = FortuneMachine(port=args.port)
        fortune_machine.demarrer()
    except Exception as e:
        print(f"\nErreur critique du programme : {e}")
        print(traceback.format_exc())
        exit(1)
