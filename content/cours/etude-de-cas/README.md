+++
author = "Hugo Authors"
title = "Markdown Syntax Guide"
date = "2020-03-11"
description = "Sample article showcasing basic Markdown syntax and formatting for HTML elements."
tags = [
    "markdown",
    "css",
    "html",
]
categories = [
    "themes",
    "syntax",
]
series = ["Themes Guide"]
aliases = ["migrate-from-jekyll"]
toc = true
+++

# Etude de cas

## Objectif et organisation de la séance

Pour cette séance, on se propose de réaliser une étude de cas d'une application développée par le lab de l'Insee : [`Prédicat`](https://github.com/InseeFrLab/predicat.git).  
Il s'agit d'un petit webservice (rappel : webservice = application répondant à des requêtes HTTP pour mettre à disposition des données / services dans un format intéropérable comme XML ou JSON) de classification de produits se basant sur un modèle.

L'objectif est de voir par cet exemple différents concepts de conception logicielle qu'on va voir / revoir dans cette séance.

Exemple de sortie de l'application :  
Requête : http://localhost:8000/label?q=confiture  
Réponse :

```JSON
{
  "confiture": [
    {
      "label": "Transformation_et_conservation_de_fruits_et_légumes_C10C",
      "proba": "1.000",
      "confiance": "0.997"
    }
  ]
}
```

Bien que le sujet statistique sous-jacent soit très intéressant, notre étude va porter sur le code, son architecture, sa portabilité, sa reproductibilité ...

A noter que, bien que cette application soit fonctionnelle, elle ne doit pas être considéree comme à l'état de l'art. C'est le résultat d'un POC (Proof Of Concept) et non le résultat final d'un projet. C'est d'ailleurs pour ça qu'elle a été choisie pour cette étude de cas, il y a de nombreux axes d'amélioration et vous êtes d'ailleurs fortement encouragés à proposer aux développeurs du projet (via des issues ou des pull requests) vos trouvailles et améliorations.

La suite de ce document propose différents axes d'analyse et d'exercices associés à ce projet mais vous êtes libres d'aborder le projet sous un angle différent si vous le souhaitez.

## Votre environnement de travail

Pour ce chapitre, vous avez accès à un grand nombre d'environnements pour exécuter votre code. Le seul prérequis est d'avoir accès à `python` ainsi qu'à `pip`.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle
- Un environnement dans le SSPCloud : [Datalab](https://datalab.sspcloud.fr).
- [Katacoda](https://www.katacoda.com/courses/python/playground) : un bac à sable avec python préinstallé (attention, `python` correspond au binaire `python 2`, utilisez `python3` à la place)

## Script vs Application

En informatique on distingue souvent 2 types de programmes pour 2 types d'usages :

- Scripts: Un script a une vocation d'usage unique, il s'agit d'un programme executé pour une action ponctuelle. Originellement, les scripts sont executés par des languages interprétés, exemple : `python`.

> Note: il peuvent être executés de manière répétée, mais dans ce cas on appelle cela un Batch. On lance un script tous les X temps, il s'execute et se termine.

- Les applications : d'un code souvent plus construit, les applications se lancent et ont vocation à vivre tant que l'on ne les arrête pas. A l'origine, les applications étaient construites a partir de language compilés, mais ce n'est plus vrai aujourd'hui.

> Dans le cadre de ce TP on va s'intéresser a une application de type api webservice.

## Qu'est ce qu'un API - webservice ?

<img src="../../../static/etude-cas/img/http.png"/>

Application Programming Interface : interface de programmation `applicative`.  
Diffuser des données et des services à destination d'autres applications.

Chez l'ophtalmo :

Est ce que c'est mieux, comme ça ?

```html
<li class="list__item">
  <a class="block__link block__link_img" href="/270229/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <img
        class="pub__img"
        alt="Apollo World Live en live streaming Apollo Théâtre - Salle Apollo 360"
        title="Apollo World Live en live streaming Apollo Théâtre - Salle Apollo 360"
        src="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>10€</span
        >
      </div>
    </picture></a
  >
  <a href="/270229/evt.htm" class="block__link block__link_title">
    <span>
      <b style="color:#1A2E41"> Apollo World Live en live streaming </b>
    </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/270099/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <img
        class="pub__img"
        alt="Impro Visio en Live Streaming My Digital Arena"
        title="Impro Visio en Live Streaming My Digital Arena"
        src="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>12€</span
        >
      </div>
    </picture></a
  >
  <a href="/270099/evt.htm" class="block__link block__link_title">
    <span> Impro Visio en Live Streaming </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/269015/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <img
        class="pub__img"
        alt="Le Roi Lion Théâtre de la Tour Eiffel"
        title="Le Roi Lion Théâtre de la Tour Eiffel"
        src="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>23€</span
        >
      </div>
    </picture></a
  >
  <a href="/269015/evt.htm" class="block__link block__link_title">
    <span> Le Roi Lion </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/267124/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <img
        class="pub__img"
        alt="Docteur Alil &amp; Mister Vardar Café de la Danse"
        title="Docteur Alil &amp; Mister Vardar Café de la Danse"
        src="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>16€</span
        >
        <span class="block__offers block__offers_discount"
          ><span class="text__mini">Jusqu'à</span>43%</span
        >
      </div>
    </picture></a
  >
  <a href="/267124/evt.htm" class="block__link block__link_title">
    <span> Docteur Alil &amp; Mister Vardar </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/230940/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <img
        class="pub__img"
        alt="Maxime Gasteuil arrive en ville Le Grand Point Virgule - Salle Majuscule"
        title="Maxime Gasteuil arrive en ville Le Grand Point Virgule - Salle Majuscule"
        src="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>21€</span
        >
      </div>
    </picture></a
  >
  <a href="/230940/evt.htm" class="block__link block__link_title">
    <span> Maxime Gasteuil arrive en ville </span>
  </a>
</li>
```

Ou comme ça ?

```json
{
  "top": [
    {
      "id": 270229,
      "titre": "Apollo World Live en live streaming"
    },
    {
      "id": 270099,
      "titre": "Impro Visio en Live Streaming"
    },
    {
      "id": 269015,
      "titre": "Le Roi Lion"
    },
    {
      "id": 267124,
      "titre": "Docteur Alil & Mister Vardar"
    },
    {
      "id": 230940,
      "titre": "Maxime Gasteuil arrive en ville"
    }
  ]
}
```

Différence entre site web (données + présentation, à destination des humains) et webservice (données brutes, à destination d'autres applications).

**Une API c'est votre rêve de statisticien**

> Les API sont également une belle prouesse pour `l'interoperabilité` des services, en effet, elles répondent a une norme agnostique au language.

> Exemple: j'aime bien python pour du ML et je suis plus a l'aise avec R pour des regressions, je peux faire un site web qui récupère les résultats des 2 pour avoir le meilleur des 2 mondes pour moi.

> Lien RFC : https://www.rfc-editor.org/rfc/rfc2616

### Son API WS en python avec FastApi

Pour la réalisation d'API en python, on utilise dans beaucoup de projets FastApi.

`https://fastapi.tiangolo.com/`

> Framework python pour écrire des API  
> Alternatives : Django, Flask

**A priori vous y êtes déjà sensibilisés**

## Client HTTP - quelques rappels

Un client HTTP est un programme ou une bibliothèque qui envoie des demandes HTTP à un serveur afin de récupérer des informations ou d'effectuer une action. Quelques exemples de clients HTTP sont les navigateurs web, les outils en ligne de commande comme curl et les bibliothèques de programmation comme celle incluses dans Python. Ces clients peuvent envoyer différents types de demandes HTTP telles que GET, POST, PUT et DELETE à un serveur, et le serveur répondra avec un code d'état HTTP et éventuellement un corps de message.

Ces clients peuvent gérer les requêtes HTTP, en fonction de la ressource cible a l'aide de méthodes ou verbes, les plus utilisées sont:

- `GET`: Retrouve une représentation de la ressource demandée au serveur.

- `POST`: Ajoute une représentation de la ressouce au serveur. C'est souvent le cas pour un formulaire ou un JSON body a envoyer au serveur.

- `PUT`: Ajoute ou met a jour une représentation de la ressource au serveur.

- `DELETE`: Supprime la ressource si elle existe côté serveur.

Ces méthodes permettent d'interagir avec des serveurs HTTP pour y soumettre ou récupérer des informations.

Exemple : `curl` `requests` `insomnia`

```
curl localhost:8000
```

```
reponse = requests.get('http://google.com')
# Si json
# print(reponse.json())
# Si texte
# print(reponse.text)
```

## Exercice 1 - Petit échauffement

1. Créez un dépot git pour le TP
2. Dans ce dépot, créez un dossier `ex1`
3. Créez une API WS avec Fastapi :

- Dépendances nécessaires : `uvicorn` & `fastapi`
- un fichier `main.py` qui contient tout le nécessaire

<details><summary>AIDE : En cliquant sur cette aide vous admettez ne pas avoir tapé sur google : `fastapi hello world tutorial`</summary>
<p>

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"result": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

</p>
</details>

```
python main.py
```

4. Dans un autre processus (soit autre terminal, soit navigateur), et a l'aide d'un client HTTP (navigateur, `curl`, `python avec requests`), accédez a l'application sur le port 8000 de votre machine, soit encore `localhost:8000`

## Analyse du code

Afin de prendre connaissance du code, on se propose de l'analyser, à la fois de façon statique mais aussi de façon dynamique.

### Analyse statique

![](https://i.imgur.com/vrZTjBy.jpg)

L'analyse statique du code consiste à l'analyser SANS le lancer.  
**Commencer par parcourir le code.**

Il faut savoir qu'il y a des règles universelles et propres aux projets en ce qui concerne "comment" coder. (Ce "comment" sous entend principalement des justification de mise en forme, de nommage et de bonnes pratiques basiques)
Il existe différents outils pour automatiser l'analyse statique :

`** Linting **`

Pour tous les languages en particulier les languages non fortement typés, il est souvent assez utile d'établir des conditions d'acceptation du code source. Pour cela, on utilise en général des outils de validation ou **linter**. Cela permet également de juger d'usages douteux du code : imports non utilisés etc..

> Exemples courants : flake8 pylint autopep8

```bash
# exemple avec flake8
pip3 install flake8
# puis
flake8 ./predicat/app
```

`** Formatting **`

Pour répondre aux besoins de bon respect des règles établies en amont (voir linting). Il peut être pertinent de s'équiper d'un formatter, associé généralement a l'IDE (Visual studio code / Pycharm).

> Exemples de plugins : black, flake8, PyFormat, Python-autopep8

```bash
# exemple avec black
pip3 install black
# puis
black --check predicat/app
```

> Projet black : https://pypi.org/project/black/

:boom: N'hésitez pas à configurer le format on save.

> La semaine dernière on a utilisé pipreqs : c'était de l'analyse statique de dépendances : https://github.com/bndr/pipreqs
> Aller plus loin : [Sonar](https://www.sonarqube.org/)

### Analyse dynamique : execution


L'analyse dynamique consiste à lancer l'application.

#### **Petits rappels sur les exceptions**

Les exceptions sont des événements qui se produisent pendant l'exécution d'un programme qui peuvent perturber le flux normal de ce dernier. Les exceptions peuvent être levées (lancées) par le programme lui-même ou par des bibliothèques utilisées par celui-ci. On peut également créer des exceptions personnalisées.

Par défaut, une exception fait arrêter le programme. Pour gérer les exceptions, l'on utilise des blocs try-except.

```python
try:
  print(x)
except:
  print("An exception occurred")
```

Si une exception est levée dans le bloc try, le programme saute immédiatement au bloc except correspondant pour gérer l'exception. Si aucune exception n'est levée, le code dans le bloc except n'est jamais exécuté.

#### **Stacktrace ou encore : "il y a du rouge partout"**

Lorsqu'un programme est lancé, il utilise la mémoire pour pouvoir fonctionner.

- La **pile** ou **stack** est une zone mémoire qui sert pour stocker les variables et fonctions. C'est littéralement une pile, lors de l'execution d'un programme les fonctions a executer sont successivement placées au dessus de la pile avant d'être dépilées.

Exemple :

```python
def a():
    b()

def b():
    c()

def c():
    erreur()

a()
```

Une **stacktrace** est un listing des fonctions qui sont sur le point d'être executée sur la pile. Il s'avère que ce listing est souvent indiqué quand un programme vient de s'interrompre, et donc, dans l'ordre inverse d'execution (il faut lire de bas en haut).

Exemple :

```
Traceback (most recent call last):
  File "tb.py", line 10, in <module>
    a()
  File "tb.py", line 2, in a
    b()
  File "tb.py", line 5, in b
    c()
  File "tb.py", line 8, in c
    erreur()
NameError: global name 'erreur' is not defined
```

- La seconde partie de la mémoire est la **heap**, il s'agit d'un fond de mémoire alloué de manière dynamique (on vide et on remplit la mémoire), c'est ici que vivent tous les objets (dictionnaires, chunk de données compris)

## Exercice 2 : Tour d'horizon du projet

![](https://i.imgur.com/WGk3SvJ.png)

A partir d'ici, le dépot qu'on utilisera tout au long du TP est ici :
https://github.com/InseeFrLab/predicat

1. Cloner le repository dans un sous dossier de votre TP, dans votre environnement de travail préféré

2. Depuis le dépot récupéré, suivre les instructions pour l'installation via le README.md, veuillez toutefois a bien faire cela dans le repertoire **app** du dépot git, par défaut : **predicat/app**

3. Lancez l'application via la commande `uvicorn main:app`, pensez bien a installer les dépendances au préalable, et vous pouvez utiliser un environnement virtuel.

<details><summary>AIDE 1 : Comment savoir les dépendances nécessaires à l'exécution de l'application ?</summary>
<p>

Pour un projet python, les dépendances sont en général gérées par pip (https://packaging.python.org/tutorials/installing-packages/) et sont listées dans le fichier requirements.txt

```python
pip install -r requirements.txt
```

</p>
</details>

<details><summary>AIDE 2 : Comment débugguer si l'application qui ne se lance pas / crash ?</summary>
<p>

Vous avez probablement mal lu le README.md.

Pour résoudre le problème, vous aurez besoin d'un modèle. On pourra utiliser le modèle de test disponible ici : https://minio.lab.sspcloud.fr/conception-logicielle/model_na2008.bin

Vous devez ensuite enlever du fichier de configuration yaml, les lignes concernant les modèles qui ne sont pas le modèle 2020_old.

Une fois l'application lancée, vous pouvez la requêter avec votre c lient HTTP préféré et adapté à votre environnement de travail (curl, navigateur web, insomnia ...) : [http://localhost:8000/label?q=confiture](http://localhost:8000/label?q=confiture) ou encore [http://localhost:8000/label?q=omelette%20du%20fromage](http://localhost:8000/label?q=omelette%20du%20fromage)

Si ça ne resoud pas, cherchez par rapport a l'erreur renvoyée par la console.

</p>
</details>

## Ajout d'une fonctionnalité : persistance de données

On se propose d'étendre le code actuel de cette application pour y ajouter une nouvelle fonctionnalité : on souhaite garder un historique de toutes les requêtes qui ont été faites (à des fins par exemple d'audit, de statistiques ou d'améliorations du modèle).  
Actuellement, l'application ne propose pas du tout de persistance de la donnée. C'est à dire que, lorsque l'application s'arrête (soit volontairement soit involontairement :fire:), toutes les données (variables) en mémoire disparaissent.  
On se propose donc d'ajouter une couche de persistance à cette application.

### Choix du (des) systèmes de persistances

Il existe différents formats de stockage de données persistantes :

- Les fichiers plats dans un format arbitraire maison (s'il vous plait, ne faites jamais ça)
- Les fichiers plats dans un format standard (**JSON** / **XML** ...)
- Les bases de données relationnelles - citons **postgresql**, **oracle**, **sqlite** - (cf SQL, les théories sur la normalisation et les formes normales)
- Les bases de données noSQL qui remettent en question le culte de la normalisation au profit d'une plus grande flexibilité (mais au détriment des avantages de la normalisation, dont la lutte contre la redondance). Citons **mongoDB**, **couchbase** et **redis** -

Les langages proposent tous des connecteurs et des APIs (au sens bibliothèques) pour ces différents modes de stockage.  
**Dans la suite, on se propose de se connecter à des bases de données relationnelles**.

> Aller plus loin : Vous êtes évidemment libres d'expérimenter les autres types de stockage ainsi que les façons (interfaces) de faire cohabiter dynamiquement plusieurs systèmes de stockage.

![](https://i.imgur.com/oN2fmBy.jpg)

#### Choix du modèle pour le TP

En règle générale, il faut se poser quelques questions :

- est ce que les données sur lesquelles je travaille sont d'un format fixe ?

=> J'utilise une base de données SQL.

- Est ce que je vais simplement chercher mes données par une clé identifiant ?

=> Base de données NoSQL

Sinon autre.

> Ici, on sait le format de la requête, il est fixe et donc on va utiliser une bdd SQL : SQLite

### SQLite, à la main

[SQLite](https://www.sqlite.org/index.html) est un système de base de données embarqué. A la différence des systèmes de base de données classiques (type postgresql, oracle, mysql ...), l'architecture de SQLite ne contient pas de serveur. C'est l'application elle même qui écrit et lit les données à partir d'un fichier `.sqlite` contenant l'ensemble des données.  
SQLite est un moteur de base de données fantastique, utilisé dans des milliards d'appareil (vous venez de regarder vos SMS ? Votre smartphone a utilisé SQLite. Vous venez de regarder le ciel ? Le satellite que vous voyez a très probablement des bases de données sqlite en lui). Si le sujet vous intéresse, cette conférence est formidable : https://www.youtube.com/watch?v=gpxnbly9bz4  
![](../../../static/etude-cas/img/sqlite.png)

Pour nous, le principal avantage de SQLite va venir de son architecture simplifiée, il n'y a pas besoin de faire tourner de base de données indépendante.

Tutorial d'utilisation de sqlite :  
https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

### Exercice 3 : Persistence de données

L'objectif de cet exercice est enregistrez dans une base de données embarquée sqlite3 une observation par requête HTTP faite sur le endpoint `/label` en incluant le texte de la requête (paramètre `q`) ainsi qu'éventuellement la date correspondante.

1. Créez une méthode init() qui crée une table Requete dans la base de données sqlite3, qui contient un id,  un label et une date (aide: https://www.sqlitetutorial.net/sqlite-create-table/)
2. Créez une méthode add_request qui ajoute une requete dans la bdd. (requete = label + date)
3. Faites une methode get_requests qui recupère les requetes dans la bdd

Remarque: Pour lancer une requête a une bdd, on utilise des connexions. Pour le client sqlite3 on ouvre une connexion a la bdd avec la methode `sqlite3.connect('db')` et on la ferme lorsque l'on termine une transaction avec `connection.commit()`


<details><summary>Spoiler</summary>
<p>

```python
import sqlite3


# On peut choisir différents types de date pour sqlLite https://www.sqlitetutorial.net/sqlite-date/
class SQLRequestsLogger:
  def init(self):
    connection = sqlite3.connect('db')
    cursor = connection.cursor()
    requetecreationTableRequete = """CREATE TABLE IF NOT EXISTS requete(requete_id INTEGER PRIMARY KEY AUTOINCREMENT,label text,  date_text text)"""
    cursor.execute(requetecreationTableRequete)
    connection.commit()
  def add_request(self,label):
    connection = sqlite3.connect('db')
    cursor = connection.cursor()
    requeteLogTable=f"""INSERT INTO requete(label,date_text) VALUES('{label}',datetime('now'))"""
    cursor.execute(requeteLogTable)
    connection.commit()
  def get_all_requests(self):
    connection = sqlite3.connect('db')
    cursor = connection.cursor()
    requeteLogTable="""SELECT * from requete"""
    res = cursor.execute(requeteLogTable)
    data = res.fetchall()
    connection.commit()
    return data

if __name__ == "__main__":
    logger = SQLRequestsLogger()
    logger.init()
    logger.add_request("confiture")
    req = logger.get_all_requests()
    print(req)
```

</p>
</details>

\*\*Où (quand) appeler la fonction `init` ? Ou (quand) appeler la fonction `insertRequestIntoDB`

### SQLAlchemy, un exemple d'interface agnostique du SGBD

![](https://i.imgur.com/1fr6KcC.png)

Ce qui arrivera souvent lorsque vous voulez intéragir avec une base de données c'est que vous allez avoir 2 choix : Soit passer directement par une librairie spécifique, soit passer par une ressource "ENGINE" qui permet de requeter sur des bases de nature différentes via des interfaces fonctionnelles, en gros via un driver.

_=> Un enjeu très fort : La portabilité._

> Typiquement : JDBC pour java ..

Dans le cadre de ce tp on vous présentera SQLAlchemy.

Le principe étant que SQLAlchemy propose une spécification que nous allons utiliser pour requêter de notre côté, et que l'implémentation est elle adhérente au gestionnaire de base de données qu'on souhaite utiliser sur le moment.

C'est un pilier de la programmation fonctionnelle : le principe **d'interface fonctionnelle**

Cet engine utilise du coup un driver via la méthode [create_engine('dialect')](https://docs.sqlalchemy.org/en/14/core/engines.html)

Exemple de code :

```python=
from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:')

    with engine.connect() as connection:

        connection.execute('DROP TABLE IF EXISTS requete')
        connection.execute('''CREATE TABLE requete(requete_id INTEGER PRIMARY KEY AUTOINCREMENT, date_text text)''')

        data = (
          { "requete_id": 1, "date_text": "2022-03-15 11:35:58"},
          {"requete_id":2,"date_text":"2022-03-15 12:46:38" }
        )

        for line in data:
            connection.execute("""INSERT INTO requete(requete_id, date_text)
            VALUES(:requete_id, :date_text)""", **line)

        result = connection.execute('''SELECT * from requete''')

        for row in result:
            print(row)
```

> Note : j'ai enlevé le label pour simplifier un peu

#### (Aller plus loin) : concept d'Object Relationnal Mapping

![](https://i.imgur.com/LyE4fkY.png)

Dans le monde du développement vous serez souvent amené a utiliser ce que l'on appelle un ORM : Object Relationnal Mapper.

Le principe étant que vous allez toujours travailler avec des **objets** python, et donc prendre encore plus de distance avec le type de base de données avec lequel vous travaillez puisque de votre côté il ne s'agira que de faire appel a des fonctions qui concernent vos objets python.

SQLAlchemy propose également des fonctionnalités d'ORM.

exemple de code:

```python=
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Sequence

Base = declarative_base()

class Requete(Base):
    __tablename__ = 'requete'
    requete_id = Column(Integer, Sequence('requete_id_seq'), primary_key=True)
    date_text = Column(String(50))
```

**Exercice** : Adaptez votre code précédent pour qu'il fonctionne pour sqlite3 mais qu'il soit agnostique de la base de données (endpoint : `GET : /label`)

## Journalisation/Logging

**![](https://i.imgur.com/HK2C53j.png)**

En général pour afficher les informations dans la console/dans un fichier on utilise des moteurs de génération de log, ils permettent principalement de centraliser le fonctionnement de la log par rapport a un print ainsi que de définir des niveau de log :

- Debug : pour les gens qui adorent spammer les print, ça permet de définir des messages qui aideront a débuguer
- Info / information : donnent des infos => exemple connection OK au serveur..
- warning : signaler un problème non bloquant : " le retour a l'air étrange"
- error : alerte bloquante
- critical : bon.. là c'est la fin

Typiquement en python on pourrait utiliser logging :

`logging` étant une librairie intégrée dans python3, pas besoin de l'installer.

doc officielle : https://docs.python.org/fr/3/howto/logging.html

Rajoutez donc des niveaux de logs correspondants sur vos différentes endpoint :

> exemple

```python=
logging.info("le resultat est :"+valeur)
```

L'idée pour le fichier output étant de le définir via la config :

```python=
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
```

avec comme niveau minimal DEBUG ici par exemple

### Exercice 4 : Logging, c'est quand même plus adapté.

- Adaptez le code précédent en faisant une classe abstraite : l'idée est que l'on répond a un besoin fonctionnel équivalent que se soit par la base de données ou le logging. Faites hériter la partie SQL.
- Adaptez le code précédent en faisant une nouvelle implémentation de cette classe abstraite.
- Journalisez tout cela dans un fichier **date-call.log**, faites le nécessaire au niveau versionning (.gitignore).
- (bonus) Créez un fichier .env pour paramétrer ou seront écrites les logs
- (bonus) Créez un fichier .env pour paramétrer quelle version de la classe abstraite on choisit en fonction d'un champ : `LOGGER_IMPL=NATIVE_LOGGER` ou `LOGGER_IMPL=SQL_LOGGER`
