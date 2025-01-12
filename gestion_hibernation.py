import subprocess
import time
import os

class GestionHibernation:
    def __init__(self, delai_inactivite=300000):  # 5 minutes par défaut
        self.delai_inactivite = delai_inactivite
        self.derniere_activite = 0
        
    def verifier_inactivite(self):
        try:
            # Utilise xprintidle pour obtenir le temps d'inactivité
            resultat = subprocess.check_output(['xprintidle']).decode('utf-8').strip()
            temps_inactif = int(resultat)
            
            if temps_inactif > self.delai_inactivite:
                print("Mise en veille de l'écran...")
                # Éteindre l'écran
                os.system("xset dpms force off")
                return True
            return False
            
        except Exception as e:
            print(f"Erreur lors de la vérification de l'inactivité : {e}")
            return False
    
    def reactiver_ecran(self):
        try:
            # Rallumer l'écran
            os.system("xset dpms force on")
            print("Écran réactivé")
        except Exception as e:
            print(f"Erreur lors de la réactivation de l'écran : {e}")
    
    def reset_timer(self):
        self.derniere_activite = time.time()
        self.reactiver_ecran() 