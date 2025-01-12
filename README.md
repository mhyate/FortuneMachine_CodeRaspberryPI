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

### Configuration de l'Environnement

1. Créer un environnement virtuel :
```bash
python3 -m venv venv
```

2. Activer l'environnement virtuel :
- Sur macOS/Linux :
```bash
source venv/bin/activate
```
- Sur Windows :
```bash
.\venv\Scripts\activate
```

3. Mettre à jour pip et les outils de base :
```bash
python3 -m pip install --upgrade pip setuptools wheel
```

4. Installer les dépendances :
```bash
pip install -r requirements.txt
```

### Résolution des Problèmes Courants

1. Si vous rencontrez une erreur `ModuleNotFoundError` :
   - Vérifiez que l'environnement virtuel est activé
   - Réinstallez les dépendances avec : `pip install -r requirements.txt`

2. En cas d'erreur avec `python-dotenv` ou d'autres modules :
   ```bash
   # Supprimer l'environnement virtuel existant
   rm -rf venv
   
   # Recréer un environnement propre
   python3 -m venv venv
   source venv/bin/activate
   
   # Installer les dépendances
   python3 -m pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
   ```

3. Sur macOS, certains modules comme `RPi.GPIO` ne sont pas compatibles :
   - Ces modules sont ignorés sur macOS
   - Ils seront installés uniquement sur Raspberry Pi

### Notes Importantes
- Toujours utiliser l'environnement virtuel pour exécuter le projet
- Les versions des dépendances sont fixées pour assurer la compatibilité
- Le fichier `.env` doit être créé localement pour les clés API (voir section Configuration)

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