#!/bin/bash

# Attendre que le système soit complètement démarré
sleep 10

# Aller dans le répertoire du projet
cd /home/pi/FortuneMachine_CodeRaspberryPI-main

# Activer l'environnement virtuel Python (à ajuster selon votre installation)
source venv/bin/activate

# Démarrer l'application
python3 main.py 