import serial
import time
import threading

class CommunicationPIC24:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600, test_mode=False):
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.test_mode = test_mode
        self.piece_detectee = False
        self.running = True
        self._thread = None

    def connecter(self):
        """Établit la connexion série avec le PIC24"""
        if self.test_mode:
            print("Mode test : Communication PIC24 simulée")
            return True
            
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            print(f"Connexion établie avec le PIC24 sur {self.port}")
            return True
        except Exception as e:
            print(f"Erreur de connexion avec le PIC24: {e}")
            return False

    def demarrer_ecoute(self):
        """Démarre l'écoute des messages du PIC24 dans un thread séparé"""
        self._thread = threading.Thread(target=self._ecoute_serie, daemon=True)
        self._thread.start()

    def _ecoute_serie(self):
        """Boucle d'écoute des messages du PIC24"""
        while self.running:
            if self.test_mode:
                time.sleep(1)
                continue

            try:
                if self.serial and self.serial.in_waiting:
                    message = self.serial.readline().decode('utf-8').strip()
                    self._traiter_message(message)
            except Exception as e:
                print(f"Erreur lecture série: {e}")
                time.sleep(1)

    def _traiter_message(self, message):
        """Traite les messages reçus du PIC24"""
        if message == "PIECE_VALIDEE":
            self.piece_detectee = True
            print("Pièce détectée !")

    def attendre_piece(self):
        """Attend qu'une pièce soit insérée"""
        if self.test_mode:
            print("Mode test : Simulation d'attente de pièce (5 secondes)")
            time.sleep(5)
            self.piece_detectee = True
            return True

        while not self.piece_detectee and self.running:
            time.sleep(0.1)
        return self.piece_detectee

    def envoyer_commande_impression(self, message):
        """Envoie une commande d'impression au PIC24"""
        if self.test_mode:
            print(f"Mode test : Simulation d'impression : {message}")
            return True

        try:
            if self.serial:
                commande = f"IMPRIMER:{message}\n"
                self.serial.write(commande.encode('utf-8'))
                return True
        except Exception as e:
            print(f"Erreur envoi commande impression: {e}")
        return False

    def reset(self):
        """Réinitialise l'état de détection de pièce"""
        self.piece_detectee = False

    def arreter(self):
        """Arrête la communication"""
        self.running = False
        if self.serial:
            self.serial.close() 