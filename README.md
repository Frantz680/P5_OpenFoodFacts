# P5_OpenFoodFacts

-----------------

Le concept de l'application ?

Le programme va récupérer des informations sur les aliments via l'API d'OpenFoodFacts. Il va comparer votre produit que vous avez selectionnez et vous proposer un subsitut plus sains.

-----------------

Avez vous déjà l'application Python ? 

Pour ouvrir cette application coder en Python, il vous faudra l'installer.
Rendez-vous sur le [site de Python](https://www.python.org/) pour l'installation.


**Comment lancer l'application ?**

Il vous faut tout d'abord créer un environnement virtuel.
Explication:

Il faut accéder à l'invite de commande:
Dans le champ de recherche du menu Démarrer taper la commande suivante:

-`cmd`
Ceci permet d'accéder a l'invite de commande.

-`pip install virtualenv`
Ceci est l'installation d'un environnement virtuel.

-`virtualenv -p python3 env`
Ceci va vous créer un dossier ''env''.

-`source env/bin/activate`
Ceci active un environnement virtuel.

-----------------

**Installation des différentes exigences**


Ensuite, il vous faudra installer les différentes exigences pour la bonne utilisation du jeu.
Explication :

-`python3 -m pip install -r requirements.txt`
Ceci installera les differentes exigences du jeu.

-----------------

**MySQL**

Remplacez les identifiant MySQL dans le fichier glob.py par les vôtres.

-----------------

**Lancement de l'application**

-`python main.py`
Ceci vous lancera automatiquement l'application.

-----------------

##Description de l'application

L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants:

Menu connection

Press 1 for create database.
Press 2 to connect to the existing database.
Press 3 for exit.

L'utilisateur sélectionne 1.

*Le programme créer la base de données.

L'utilisateur sélectionne 2.

*Le programme ce connecte à la base de donnée qui est déjà créer.

L'utilisateur sélectionne 3.

*Le programme s'arrete.

Menu

Press 1 for research substituted.
Press 2 for my substituted foods.
Press 3 for exit.

L'utilisateur sélectionne 1. Le porgramme pose les questions suivantes à l'utilisateur et ce dernier sélectione les réponses:

* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

Je vous laisse découvrir la suite.