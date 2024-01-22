+++
title = "TP Portabilité configuration : Configuration"
date = 2024-01-22T00:00:12
aliases = ["python","git"]
header_img= "/img/settings.svg"
+++


## Exercice 6: paramétrage et variables en ligne de commande

Pour cet exercice, l'objectif est de rendre paramétrable sans changer le code, le fichier de sortie des logs du traitement.

On souhaite ici le placer en premier argument.

Créez une fonction :
```python
def get_fichier_sortie()
```
qui renvoie le fichier de sortie par rapport au premier argument, en mettant un default a `None`.

Intégrez l'appel de cette fonction a la partie de configuration des logs.
## Exercice 7: paramétrage et variables d'environnement

Adaptez maintenant la fonction get_fichier_sortie() pour qu'il charge des variables d'environnement/

Il vous faudra donc créer un fichier `.env` et configurer son utilisation par le biais d'un paquet comme : https://pypi.org/project/python-dotenv/

> .env
`PATH_FICHIER_SORTIE=output.log`
## Exercice 8 : Versionning et configuration.

Mettez a zéro la config dans le fichier `.env` en laissant une valeur vide :

> .env
`PATH_FICHIER_SORTIE=`

Ajoutez une configuration locale de type : `.env.local` ou `.env.dev`.
Valorisez a nouveau cette configuration et enlevez la du versionnement.

Créez une nouvelle version du code.