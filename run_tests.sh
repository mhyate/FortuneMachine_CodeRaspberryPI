#!/bin/bash

# Détection de la plateforme
platform=$(uname)

echo "Exécution des tests sur $platform..."

# Activation de l'environnement virtuel
source venv/bin/activate

# Installation des dépendances de test
pip install -r requirements.txt

# Configuration des variables d'environnement pour les tests
export TESTING=true
export MOCK_HARDWARE=true  # Pour simuler le matériel sur MacOS

if [ "$platform" = "Darwin" ]; then
    echo "Exécution des tests sur MacOS..."
    # Exclure les tests spécifiques à Raspberry Pi
    pytest -v -m "not raspberry_only and not integration" Tests/
elif [ "$platform" = "Linux" ]; then
    if [ -f /etc/rpi-issue ]; then
        echo "Exécution des tests sur Raspberry Pi..."
        # Exécuter tous les tests
        pytest -v Tests/
    else
        echo "Exécution des tests sur Linux (non-Raspberry Pi)..."
        # Exclure les tests spécifiques à Raspberry Pi
        pytest -v -m "not raspberry_only and not integration" Tests/
    fi
else
    echo "Plateforme non supportée"
    exit 1
fi

# Génération du rapport de couverture
coverage html

echo "Tests terminés. Consultez le rapport de couverture dans htmlcov/index.html" 