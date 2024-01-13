+++
title = "TP Git en local"
description = "Tp sur git en local"
date = 2024-01-15T00:00:04
short = true
aliases = ["git"]
header_img= "img/git11.svg"
+++

Ce TP reprend différents concepts de base de la partie "git en local".

On part sur la création des premières fonctions pour notre projet de webservice.

On souhaite créer une fonctionnalité qui permet de journaliser la requête d'un utilisateur en créant une fonction qui récupère la date d'appel de celle ci.

### Exercice 1

Pour ce premier exercice, écrivons ensemble l'histoire suivante :

- Créer un dossier pour votre projet : tp1-conception-logicielle
- Créer un petit programme en python qui renvoie  l'heure actuelle dans la console au format "HH:MM:SS" dans un fichier main.py (:pray: on renvoit la date puis __str__() )
- Ajoutez ce fichier dans l'index et créer une nouvelle version. (commit)
- Ajout d'un second fichier, vide, `README.md`  
  A quelle heure le dernier commit a t'il été écrit ? Quel est son _hash_ (identifiant) ?
- Ajoutez un zonage sur la date pour récupérer l'heure qu'il est a La Réunion, et un zonage pour récupérer l'heure qu'il est. Faites de même pour l'heure de Paris . Créez un commit avec le message "ajout zonage".

> Indice pour les timezone : Indian/Reunion et Europe/Paris

Félicitations ! Vous avez un joli dépôt git contenant une première histoire.

> NB: si vous n'avez pas d'idées sur comment on peut réaliser certaines parties du tp, des aides sont disponibles dans des sections dédiées

<details>
  <summary>Aide 1</summary>

```python
from datetime import datetime

current_time = datetime.now()
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted)
```

> main.py (première version)

```python
from datetime import datetime
import pytz # $ pip install pytz

timezone_paris = pytz.timezone('Europe/Paris')
current_time = datetime.now(timezone)
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted))
```

</details>


### Exercice 2

- Déplacez-vous sur le premier commit de votre dépot.

<details>
  <summary>Aide 2</summary>

```
git log
```

puis

```
git checkout
```

</details>
