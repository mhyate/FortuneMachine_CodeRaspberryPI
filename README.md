# Fortune Machine

## Objectif du Projet
La Fortune Machine est un projet interactif qui délivre des "fortunes" (messages) aux utilisateurs via une interface graphique et une imprimante thermique. Le projet propose quatre types de fortunes :
- **Météo** : Affiche la météo actuelle à Tours
- **Citations Chuck Norris** : Génère des citations humoristiques de Chuck Norris traduites en français
- **Horoscope** : Fournit des prédictions astrologiques quotidiennes
- **Blagues** : Raconte des blagues en français

## Installation et Gestion des Dépendances

### Prérequis
- Python 3.x
- pip (gestionnaire de paquets Python)
- venv (module de création d'environnements virtuels)

### Configuration de l'Environnement de Développement

1. Créer un environnement virtuel :
```bash
python3 -m venv venv
```

2. Activer l'environnement virtuel :
- Sur macOS/Linux :
```bash
source venv/bin/activate
```

3. Installer les dépendances :
```bash
python3 -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Notes pour le Développement sur MacBook
- Certains modules comme `RPi.GPIO` ne sont pas compatibles avec macOS
- L'imprimante thermique sera simulée
- Les ports GPIO ne seront pas accessibles
- Le programme fonctionnera en mode simulation

### Exécution sur MacBook
```bash
python3 main.py
```

## Déploiement sur Raspberry Pi

### Installation Automatique (recommandée)

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-repo/FortuneMachine_CodeRaspberryPI.git
cd FortuneMachine_CodeRaspberryPI
```

2. Exécutez le script d'installation :
```bash
sudo chmod +x install.sh
sudo ./install.sh
```

Le script effectuera automatiquement :
- L'installation des dépendances système
- La création de l'environnement virtuel Python
- L'installation des dépendances Python
- La configuration des permissions
- L'installation du service systemd
- La configuration des ports série
- La configuration de l'affichage

### Installation Manuelle sur Raspberry Pi

Si vous préférez installer manuellement :

1. Installez les dépendances système :
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv xprintidle python3-tk xserver-xorg
```

2. Créez et activez l'environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Installez les dépendances Python :
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

4. Configurez les permissions :
```bash
sudo usermod -a -G dialout pi
sudo chmod +x main.py
```

5. Installez le service systemd :
```bash
sudo cp fortune-machine.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable fortune-machine
```

6. Activez le port série :
```bash
echo "enable_uart=1" | sudo tee -a /boot/config.txt
```

## Guide de Dépannage

### 1. Problèmes d'Environnement Virtuel
Si vous rencontrez des erreurs de modules manquants :
1. Désactiver l'environnement virtuel actuel : `deactivate`
2. Supprimer l'ancien environnement : `rm -rf venv`
3. Créer un nouvel environnement : `python3 -m venv venv`
4. Activer l'environnement : `source venv/bin/activate`
5. Installer les dépendances : `pip install -r requirements.txt`

### 2. Erreurs Courantes et Solutions
- **ModuleNotFoundError: No module named 'dotenv'** :
```bash
pip install python-dotenv
```

- **Erreur avec googletrans** :
```bash
pip install googletrans==3.1.0a0
```

### 3. Problèmes Spécifiques à la Raspberry Pi

1. Si l'écran ne s'allume pas :
```bash
xset dpms force on
```

2. Si le port série n'est pas détecté :
```bash
ls -l /dev/tty*
sudo chmod 666 /dev/ttyUSB0  # Ajustez selon votre port
```

3. Si le service ne démarre pas :
```bash
sudo systemctl status fortune-machine
sudo journalctl -u fortune-machine -n 50
```

## Maintenance

### Mise à jour du logiciel
```bash
git pull
source venv/bin/activate
pip install -r requirements.txt
```

Sur Raspberry Pi, ajoutez :
```bash
sudo systemctl restart fortune-machine
```

### Tests

### Exécution des Tests

Pour exécuter tous les tests appropriés à votre plateforme :
```bash
chmod +x run_tests.sh
./run_tests.sh
```

Le script détectera automatiquement votre plateforme et exécutera les tests appropriés :
- Sur MacBook : tests unitaires et tests d'API (sans matériel)
- Sur Raspberry Pi : tous les tests, y compris les tests d'intégration

### Types de Tests

1. **Tests Unitaires** (`@pytest.mark.unit`)
   - Tests de base ne nécessitant pas de matériel
   - Fonctionnent sur toutes les plateformes
   - Exemple : tests des classes de base, validations, etc.

2. **Tests d'API** (`@pytest.mark.api`)
   - Tests des appels API externes
   - Nécessitent une connexion Internet
   - Utilisent le mocking pour les tests hors ligne

3. **Tests d'Intégration** (`@pytest.mark.integration`)
   - Tests avec le matériel réel
   - Uniquement sur Raspberry Pi
   - Exemple : tests de l'imprimante, des GPIO, etc.

4. **Tests Spécifiques à la Plateforme**
   - `@pytest.mark.mac_only` : tests uniquement pour MacOS
   - `@pytest.mark.raspberry_only` : tests uniquement pour Raspberry Pi

### Rapports de Tests

Après l'exécution des tests, vous trouverez :
- Rapport de couverture HTML : `htmlcov/index.html`
- Rapport console détaillé
- Logs des tests dans `Tests/logs/`

### Bonnes Pratiques pour les Tests

1. **Développement sur MacBook**
   - Utiliser les mocks pour simuler le matériel
   - Tester principalement la logique métier
   - Utiliser `@pytest.mark.mac_only` pour les tests spécifiques

2. **Tests sur Raspberry Pi**
   - Tester l'intégration avec le matériel réel
   - Vérifier les communications série
   - Tester les scénarios d'erreur matérielle

3. **Tests Continus**
   - Exécuter les tests avant chaque commit
   - Maintenir une couverture de code > 80%
   - Documenter les cas de test particuliers

### Bonnes Pratiques
1. **Gestion des Dépendances** :
   - Toujours utiliser un environnement virtuel
   - Maintenir `requirements.txt` à jour
   - Spécifier les versions exactes des packages

2. **Gestion des APIs** :
   - Stocker les clés API dans un fichier `.env`
   - Implémenter des timeouts appropriés
   - Gérer les erreurs de connexion

3. **Tests** :
   - Exécuter les tests avant chaque déploiement
   - Vérifier la connexion aux APIs
   - Tester avec et sans imprimante

## Sécurité

- Les ports série sont configurés avec les permissions minimales nécessaires
- Le service s'exécute avec l'utilisateur pi
- L'interface graphique est protégée contre les accès non autorisés

## Contribution
Pour contribuer au projet :
1. Créer une branche pour votre fonctionnalité
2. Ajouter des tests pour les nouvelles fonctionnalités
3. Vérifier que tous les tests passent
4. Soumettre une pull request

## Licence
Ce projet est sous licence MIT. 