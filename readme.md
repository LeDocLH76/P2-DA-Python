## Pour tester le code, cloner le dépot, créer un environnement virtuel et installer les dépendances:

#### - Prérequis.

Python3.6 mini doit être installé

#### - Créer l'environnement.

Ouvrir l'invite de commande.
Se placer dans le repertoire racine du code cloné.
Créer l'environnement `Python -m venv env`.
Activer l'environnement `env\Scripts\activate`

#### - Installer les dépendances

`python -m pip install -r requirements.txt`

#### Executer le code

`python entry_point.py`

#### Quiter l'environnement

`deactivate`

#### Visualisation des données

Deux répertoires ont été créés à la racine du projet.
csv_files pour les fichiers csv par catégorie, et pictures pour les images sous un répertoire par catégorie.
Pour les fichiers csv un tableur comme excel permet de voir et manipuler les données.
Pour les images, le nom correspond au code UPC de façon à facilement les mettre en relation avec les données dans une base de données relationnelle.
