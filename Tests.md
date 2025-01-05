# Tests du Projet Fortune Machine

## Structure des Tests

Les tests sont organisés en plusieurs fichiers dans le dossier `Tests/` :
- `TestMain.py` : Tests du fichier principal
- `TestMeteotry.py` : Tests de la classe météo
- `TestCNQuotes.py` : Tests des citations Chuck Norris
- `TestHoroscope.py` : Tests de l'horoscope
- `TestBlagues.py` : Tests des blagues
- `TestInterface.py` : Tests de l'interface graphique

## Tests du Fichier Principal (TestMain.py)

### Tests de Détection du Port Série
- ✅ `test_detect_serial_port_success` : Vérifie la détection réussie d'un port série
- ✅ `test_detect_serial_port_no_ports` : Vérifie le comportement quand aucun port n'est disponible
- ✅ `test_detect_serial_port_error` : Vérifie la gestion des erreurs lors de l'ouverture du port

### Tests des LEDs
- ✅ `test_flash_leds` : Vérifie le clignotement des LEDs (simulé)

### Tests de l'Imprimante
- ✅ `test_printer_initialization` : Vérifie l'initialisation avec port série disponible
- ✅ `test_printer_initialization_no_port` : Vérifie l'initialisation sans port série

## Tests de la Classe Météo (TestMeteotry.py)

### Tests de l'API Météo
- ✅ `test_api_connection` : Vérifie la connexion à l'API Open-Meteo
- ✅ `test_weather_data_format` : Vérifie le format des données météo reçues
- ✅ `test_temperature_range` : Vérifie que la température est dans une plage réaliste
- ✅ `test_error_handling` : Vérifie la gestion des erreurs de l'API

### Tests d'Affichage
- ✅ `test_display_format` : Vérifie le format d'affichage des données météo
- ✅ `test_no_default_message` : Vérifie qu'aucun message par défaut n'est affiché

## Tests des Citations Chuck Norris (TestCNQuotes.py)

### Tests de l'API Chuck Norris
- ✅ `test_api_connection` : Vérifie la connexion à l'API
- ✅ `test_quote_format` : Vérifie le format des citations reçues
- ✅ `test_translation` : Vérifie la traduction en français
- ✅ `test_error_handling` : Vérifie la gestion des erreurs

### Tests de Formatage
- ✅ `test_quote_length` : Vérifie la longueur des citations
- ✅ `test_no_default_message` : Vérifie qu'aucun message par défaut n'est affiché

## Tests de l'Horoscope (TestHoroscope.py)

### Tests de l'API Horoscope
- ✅ `test_api_connection` : Vérifie la connexion à l'API
- ✅ `test_zodiac_signs` : Vérifie la validité des signes du zodiaque
- ✅ `test_horoscope_format` : Vérifie le format des horoscopes
- ✅ `test_error_handling` : Vérifie la gestion des erreurs

### Tests de Contenu
- ✅ `test_content_length` : Vérifie la longueur des prédictions
- ✅ `test_no_default_message` : Vérifie qu'aucun message par défaut n'est affiché

## Tests des Blagues (TestBlagues.py)

### Tests de l'API Blagues
- ✅ `test_api_connection` : Vérifie la connexion à l'API blablagues.net
- ✅ `test_joke_format` : Vérifie le format des blagues reçues
- ✅ `test_error_handling` : Vérifie la gestion des erreurs

### Tests de Contenu
- ✅ `test_joke_structure` : Vérifie la structure question/réponse des blagues
- ✅ `test_no_default_message` : Vérifie qu'aucun message par défaut n'est affiché

## Tests de l'Interface (TestInterface.py)

### Tests de l'Interface Graphique
- ✅ `test_window_creation` : Vérifie la création de la fenêtre
- ✅ `test_button_creation` : Vérifie la création des boutons
- ✅ `test_button_layout` : Vérifie la disposition des boutons

### Tests des Fonctionnalités
- ✅ `test_button_clicks` : Vérifie les actions des boutons
- ✅ `test_message_display` : Vérifie l'affichage des messages
- ✅ `test_error_handling` : Vérifie la gestion des erreurs d'affichage

## Exécution des Tests

Pour exécuter tous les tests :
```bash
python3 -m unittest discover Tests
```

Pour exécuter un fichier de test spécifique :
```bash
python3 -m unittest Tests/TestMain.py
```

## Résultats des Tests

Tous les tests passent avec succès, démontrant :
1. La robustesse du système de détection du matériel
2. La fiabilité des connexions aux APIs
3. La gestion appropriée des erreurs
4. L'absence de messages par défaut
5. Le bon fonctionnement de l'interface utilisateur
