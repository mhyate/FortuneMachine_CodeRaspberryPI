import subprocess
import time
import os

class GestionHibernation:
    def __init__(self, delai_inactivite=110000, delai_dim=60000):  # 1m50s total, 1m pour dim
        self.delai_inactivite = delai_inactivite  # 110000 ms = 1m50s
        self.delai_dim = delai_dim  # 60000 ms = 1m
        self.derniere_activite = time.time() * 1000  # Conversion en millisecondes
        self.luminosite_normale = 100
        self.luminosite_reduite = 30
        self.ecran_dim = False
        
    def _get_temps_inactif(self):
        """Obtenir le temps d'inactivité en millisecondes"""
        try:
            resultat = subprocess.check_output(['xprintidle']).decode('utf-8').strip()
            return int(resultat)
        except Exception as e:
            print(f"Erreur lors de la vérification de l'inactivité : {e}")
            return 0
    
    def _set_luminosite(self, niveau):
        """Définir la luminosité de l'écran (0-100)"""
        try:
            # Utiliser xrandr pour ajuster la luminosité
            subprocess.run(['xrandr', '--output', 'HDMI-1', '--brightness', str(niveau/100)], 
                         check=True)
            print(f"Luminosité ajustée à {niveau}%")
        except Exception as e:
            print(f"Erreur lors de l'ajustement de la luminosité : {e}")
            
    def verifier_inactivite(self):
        """Vérifier l'inactivité et gérer l'état de l'écran"""
        temps_inactif = self._get_temps_inactif()
        
        # Si le temps d'inactivité dépasse le délai d'hibernation (1m50s)
        if temps_inactif > self.delai_inactivite:
            if not self.ecran_dim:
                print("Mise en veille de l'écran...")
                os.system("xset dpms force off")
                return True
                
        # Si le temps d'inactivité dépasse le délai de diminution de luminosité (1m)
        elif temps_inactif > self.delai_dim and not self.ecran_dim:
            print("Diminution de la luminosité...")
            self._set_luminosite(self.luminosite_reduite)
            self.ecran_dim = True
            
        # Si l'activité reprend avant l'hibernation mais après la diminution
        elif temps_inactif < self.delai_dim and self.ecran_dim:
            print("Restauration de la luminosité normale...")
            self._set_luminosite(self.luminosite_normale)
            self.ecran_dim = False
            
        return False
    
    def reactiver_ecran(self):
        """Réactiver l'écran et restaurer la luminosité normale"""
        try:
            # Rallumer l'écran
            os.system("xset dpms force on")
            # Restaurer la luminosité normale
            self._set_luminosite(self.luminosite_normale)
            self.ecran_dim = False
            print("Écran réactivé avec luminosité normale")
        except Exception as e:
            print(f"Erreur lors de la réactivation de l'écran : {e}")
    
    def reset_timer(self):
        """Réinitialiser le timer d'inactivité"""
        self.derniere_activite = time.time() * 1000
        if self.ecran_dim:
            self.reactiver_ecran() 