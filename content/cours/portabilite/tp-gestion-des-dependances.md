+++
title = "TP Portabilité configuration : Gestion des dépendances"
date = 2024-01-22T00:00:03
aliases = ["python","pip","poetry","package manager"]
header_img= "img/pack.svg"
+++

### Exercice 3 : Ajout d'une dépendance - Logging

<img src="/img/log.svg" />

**Enoncé et concept**
Une part importante du code et de son execution est de pouvoir suivre son execution. Vous connaissez probablement print, mais dans le monde informatique il est d'usage d'utiliser ce qu'on appelle du logging.


En général pour afficher les informations dans la console/dans un fichier on utilise des moteurs de génération de log, ils permettent principalement de centraliser le fonctionnement de la log par rapport a un print ainsi que de définir des niveau de log :

- Debug : pour les gens qui adorent spammer les print, ça permet de définir des messages qui aideront a débuguer
- Info / information : donnent des infos => exemple connection OK au serveur..
- warning : signaler un problème non bloquant : " le retour a l'air étrange"
- error : alerte bloquante
- critical : bon.. là c'est la fin

Le module logging de Python est une implémentation python de ce concept.

doc officielle : https://docs.python.org/fr/3/howto/logging.html

Le logging se configure par ailleurs (en amont)
L'idée pour le fichier output étant de le définir via la config :

**TODO**

Rajoutez donc une config de base : 
```python
logging.basicConfig(filename=None, encoding='utf-8', level=logging.DEBUG)
```

Rajoutez donc des niveaux de logs correspondants dans votre traitement :

```python
logging.info(f"Lancement du traitement")
```

```python
logging.debug(f"Demande d'heure sur le timezone : {timezone}")
```

et 

```python
if timezone is None:
    logging.error("aucune timezone n'a été renseignée")
    raise ValueError("aucune timezone n'a été renseignée")
```

Créez/modifier un fichier `requirements.txt` qui vous permet d'arriver a un lancement fonctionnel de votre projet.
Une fois que vous avez fait tout cela, ajoutez et créez un commit sur votre dépôt git local et envoyez les changements.
Veuillez tester sur un autre environnement votre code (ssplab, collègue).

### Exercice 4 : Création d'un environnement virtuel et changement de la structure du projet

- Créez un environnement virtuel a la racine du projet
- Installez les dépendances nécessaires au fonctionnement du projet
- Déplacez les fichiers `*.py` vers le repertoire `src/datensai-unnomunique`
### Exercice 5 : Utilisation de poetry et construction d'un package wheel et publication sur PyPi

Dans cette partie nous allons utiliser poetry plutôt que pip, vous pouvez toutefois utiliser pip si vous le souhaitez en vous référant a un tutoriel dédié de ce type :
https://packaging.python.org/en/latest/tutorials/packaging-projects/.

L'objectif ici est de livrer un paquet python sur https://test.pypi.org/ qui est une instance de pypi

**Step 1: Pypi**

- Créez un compte sur https://test.pypi.org/ à l'url https://test.pypi.org/account/register/


**Step 2: Installation de poetry sur le projet**

```
pip install poetry
```

- Configurez votre projet pour utiliser poetry (depuis la racine de votre projet)

soit :

```
poetry init
```

> Remarque veillez a bien avoir le nom du projet poetry égal au nom du dossier dans src/XXX

puis 

```
poetry install
```

**Step 3: ajout de la config pypi sur le projet**
```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
# récupérer un token sur https://test.pypi.org/manage/account/token/
poetry config pypi-token.test-pypi pypi-XXXXXXXXXXXXXXXXXXXXX
```

**Step 4: enjoy**
- Construisez votre livrable:

```
poetry build
```

- Envoyez votre livrable sur votre dépôt:

```
poetry publish -r test-pypi
```


Vous pouvez maintenant tester : 

Exemple :
```
pip install -i https://test.pypi.org/simple/ datensaiabrunetti
python -m datensaiabrunetti.main
```