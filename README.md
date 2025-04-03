# Simulation de Messages CAN pour Véhicules Électriques à partir de Données CSV

Bienvenue dans le projet **Simulation de Messages CAN pour Véhicules Électriques**. Ce projet permet de simuler et de tester les messages CAN utilisés dans les systèmes de contrôle des véhicules électriques. Il utilise des données provenant de fichiers CSV pour générer et envoyer les messages CAN, facilitant ainsi les tests et la simulation des comportements du véhicule.

## Prérequis

Avant de commencer, vous devez installer **pipx** et **Poetry**, qui vous permettront de gérer facilement l'environnement de développement et les dépendances du projet.

### 1. Installer pipx
pipx est un gestionnaire d'environnements Python isolés. Installez-le globalement pour mieux gérer Poetry et d'autres outils Python.

`pip install pipx`

### 2. Installer Poetry
Poetry est un outil de gestion de dépendances et d'environnements virtuels pour Python. Il simplifie l'installation et la gestion des bibliothèques.

`pip install poetry`

### 3. Créer un Environnement Virtuel avec Poetry
Poetry gère automatiquement l'environnement virtuel pour vous. Il suffit d'exécuter la commande suivante pour activer l'environnement du projet :


`poetry shell`

### 4. Installer les Dépendances
Une fois l'environnement virtuel activé, installez toutes les dépendances nécessaires au projet, y compris celles de développement :

`poetry install`

### 5. Lancer le code
`python Test.py`

Cela vous permettra de disposer de toutes les bibliothèques nécessaires pour tester et simuler les messages CAN.

