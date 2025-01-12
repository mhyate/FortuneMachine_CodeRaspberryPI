# Fortune Machine

## Objectif du Projet
La Fortune Machine est un projet interactif qui délivre des "fortunes" (messages) aux utilisateurs via une interface graphique et une imprimante thermique. Le projet propose quatre types de fortunes :
- **Météo** : Affiche la météo actuelle à Tours
- **Citations Chuck Norris** : Génère des citations humoristiques de Chuck Norris traduites en français
- **Horoscope** : Fournit des prédictions astrologiques quotidiennes
- **Blagues** : Raconte des blagues en français

## Installation

### Prérequis
- Python 3.8 ou supérieur (éviter Python 3.13 qui a des problèmes de compatibilité)
- pip (gestionnaire de paquets Python)
- Connexion Internet pour les APIs
- Imprimante thermique (optionnelle)

### Installation Recommandée
1. Créer un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate  # Sur macOS/Linux
.\venv\Scripts\activate   # Sur Windows
```

2. Installer les dépendances :
```bash
pip3 install -r requirements.txt
```

Note : Sur macOS, l'installation de `RPi.GPIO` échouera car c'est une bibliothèque spécifique à Raspberry Pi. Cela n'empêche pas le fonctionnement du programme en mode simulation.

## Guide de Dépannage

### 1. Problèmes d'Environnement Virtuel
Si vous rencontrez des erreurs de modules manquants :
1. Désactiver l'environnement virtuel actuel : `deactivate`
2. Supprimer l'ancien environnement : `rm -rf venv`
3. Créer un nouvel environnement : `python3 -m venv venv`
4. Activer l'environnement : `source venv/bin/activate`
5. Installer les dépendances : `pip3 install -r requirements.txt`

### 2. Erreurs Courantes et Solutions
- **ModuleNotFoundError: No module named 'dotenv'** :
  ```bash
  pip3 install python-dotenv
  ```

- **Erreur avec googletrans** :
  ```bash
  pip3 install googletrans==3.1.0a0
  ```

- **Problèmes avec Python 3.13** :
  - Utiliser Python 3.8-3.11 pour une meilleure compatibilité
  - Certains modules comme `cgi` ne sont plus disponibles dans Python 3.13

### 3. Bonnes Pratiques
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

### 4. Vérifications Préalables
Avant de lancer le programme, vérifier :
1. L'environnement virtuel est activé
2. Toutes les dépendances sont installées
3. Le fichier `.env` est configuré (si nécessaire)
4. La connexion Internet est active
5. Les permissions sont correctes (sudo sur Raspberry Pi)

## Exécution du Programme

### Sur macOS
```bash
python3 main.py
```
Le programme fonctionnera en mode simulation (sans imprimante).

### Sur Raspberry Pi
```bash
sudo python3 main.py
```
Les droits sudo sont nécessaires pour accéder au port série et aux GPIO.

## Tests
Pour exécuter tous les tests :
```bash
python3 -m unittest discover Tests
```

Pour exécuter un test spécifique :
```bash
python3 -m unittest Tests/TestMain.py
```

## Contribution
Pour contribuer au projet :
1. Créer une branche pour votre fonctionnalité
2. Ajouter des tests pour les nouvelles fonctionnalités
3. Vérifier que tous les tests passent
4. Soumettre une pull request

## Licence
Ce projet est sous licence MIT. 