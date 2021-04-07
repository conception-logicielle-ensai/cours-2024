# Etude de cas 

## Objectif et organisation de la séance  

Pour cette séance, on se propose de réaliser une étude de cas d'une application développée par le lab de l'Insee : [`Prédicat`](https://github.com/InseeFrLab/predicat.git).  
Il s'agit d'un petit webservice (rappel : webservice = application répondant à des requêtes HTTP pour mettre à disposition des données / services dans un format intéropérable comme XML ou JSON) de classification de produits se basant sur un modèle.  

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

## Récupération du projet
![](https://i.imgur.com/WGk3SvJ.png)

https://github.com/InseeFrLab/predicat

** Cloner le repository dans votre environnement de travail préféré **

## Analyse du code

Afin de prendre connaissance du code, on se propose de l'analyser, à la fois de façon statique mais aussi de façon dynamique.

### Analyse statique  

![](https://i.imgur.com/vrZTjBy.jpg)

L'analyse statique du code consiste à l'analyser SANS le lancer.  
**Commencer par parcourir le code.**  

Il existe différents outils pour automatiser l'analyse statique :  

`** Linting **`  

Pour tous les languages en particulier les languages non fortement typés, il est souvent assez utile d'établir des conditions d'acceptation du code source. Pour cela, on utilise en général des outils de validation ou **linter**.

> Exemples courants : flake8 pylint autopep8

```bash
# exemple avec flake 8
pip3 install flake8
# puis
flake8
``` 

`** Formatting **`

Pour répondre aux besoins de bon respect des règles établies en amont (voir linting). Il peut être pertinent de s'équiper d'un formatter, associé généralement a l'IDE (Visual studio code / Pycharm).

> Exemples de plugins : Python, flake8, PyFormat, Python-autopep8

<details><summary>aide</summary><p>

![](https://i.imgur.com/redSw5Y.png)

</p></details>
:boom: N'hésitez pas à configurer le format on save.

Aller plus loin : [Sonar](https://www.sonarqube.org/)

### Analyse dynamique

![](https://i.imgur.com/XkaZ8L1.png)

L'analyse dynamique consiste à lancer l'application.  
**Comment savoir les dépendances nécessaires à l'exécution de l'application ?**  
<details><summary>Spoiler</summary>
<p>

Les dépendances sont en général gérées par pip (https://packaging.python.org/tutorials/installing-packages/) et sont listées dans le fichier requirements.txt

</p>
</details>  

**Comment installer facilement les dépendances nécessaires à l'exécution de l'application ?**  

<details><summary>Spoiler</summary>
<p>
pip install -r requirements.txt
</p>
</details>  

Certains projets, un peu plus complexes, préfèrent personnaliser la ligne de commande nécessaire au lancement.  
Pour ce projet, une façon de le lancer est d'utiliser `uvicorn` :  
```
cd app
uvicorn main:app
```  

L'application ne semble pas se lancer.  
**Comment débugguer une application qui ne se lance pas / crash ?**  

**A partir de la log, diagnostiquer le problème.**  

Pour résoudre le problème, vous aurez besoin d'un modèle. On pourra utiliser le modèle de test disponible ici : https://minio.lab.sspcloud.fr/conception-logicielle/model_na2008.bin  

Une fois l'application lancée, vous pouvez la requêter avec votre client HTTP préféré et adapté à votre environnement de travail (curl, navigateur web, insomnia ...) : [http://localhost:8000/label?q=confiture](http://localhost:8000/label?q=confiture) ou encore [http://localhost:8000/label?q=omelette%20du%20fromage](http://localhost:8000/label?q=omelette%20du%20fromage)

Au final, il a fallu faire un certain nombre de modifications et de configurations sur le projet avant de pouvoir le lancer.  
Il serait intéressant de documenter ces différentes étapes afin d'aider les générations futures.  
**Où ajouteriez vous cette documentation ?**  
**Sidequest** : faire une `issue` et / ou une `pull request` pour proposer aux développeurs du projet `predicat` cette documentation.

## Ajout d'une fonctionnalité : persistance de données  

On se propose d'étendre le code actuel de cette application pour y ajouter une nouvelle fonctionnalité : on souhaite garder un historique de toutes les requêtes qui ont été faites (à des fins par exemple d'audit, de statistiques ou d'améliorations du modèle).  
Actuellement, l'application ne propose pas du tout de persistance de la donnée. C'est à dire que, lorsque l'application s'arrête (soit volontairement soit involontairement :fire:), toutes les données (variables) en mémoire disparaissent.  
On se propose donc d'ajouter une couche de persistance à cette application.

### Choix du (des) systèmes de persistances 

Il existe différents formats de stockage de données persistantes : 

- Les fichiers plats dans un format arbitraire maison (s'il vous plait, ne faites jamais ça)  
- Les fichiers plats dans un format standard (JSON / XML ...)
- Les bases de données relationnelles - citons postgresql, oracle, sqlite - (cf SQL, les théories sur la normalisation et les formes normales)
- Les bases de données noSQL qui remettent en question le culte de la normalisation au profit d'une plus grande flexibilité (mais au détriment des avantages de la normalisation, dont la lutte contre la redondance). Citons mongoDB, couchbase et redis -

Les langages proposent tous des connecteurs et des APIs (au sens bibliothèques) pour ces différents modes de stockage.  
**Dans la suite, on se propose de se connecter à des bases de données relationnelles**. 
Aller plus loin : Vous êtes évidemment libres d'expérimenter les autres types de stockage ainsi que les façons (interfaces) de faire cohabiter dynamiquement plusieurs systèmes de stockage.

![](https://i.imgur.com/oN2fmBy.jpg)

### SQLite, à la main  

[SQLite](https://www.sqlite.org/index.html) est un système de base de données embarqué. A la différence des systèmes de base de données classiques (type postgresql, oracle, mysql ...), l'architecture de SQLite ne contient pas de serveur. C'est l'application elle même qui écrit et lit les données à partir d'un fichier `.sqlite` contenant l'ensemble des données.  
SQLite est un moteur de base de données fantastique, utilisé dans des milliards d'appareil (vous venez de regarder vos SMS ? Votre smartphone a utilisé SQLite. Vous venez de regarder le ciel ? Le satellite que vous voyez a très probablement des bases de données sqlite en lui). Si le sujet vous intéresse, cette conférence est formidable : https://www.youtube.com/watch?v=gpxnbly9bz4  
![](img/sqlite.png)  

Pour nous, le principal avantage de SQLite va venir de son architecture simplifiée, il n'y a pas besoin de faire tourner de base de données indépendante.

Tutorial d'utilisation de sqlite :  
https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

**Exercice** : enregistrez dans une base de données embarquée sqlite3 une observation par requête HTTP faite sur le endpoint `/label` en incluant le texte de la requête (paramètre `q`) ainsi qu'éventuellement la date correspondante.  
<details><summary>Spoiler</summary>
<p>


```python
import sqlite3


# On peut choisir différents types de date pour sqlLite https://www.sqlitetutorial.net/sqlite-date/

def init:
  connection = sqlite3.connect('db')
  cursor = connection.cursor()
  requetecreationTableRequetes = """CREATE TABLE IF NOT EXISTS requetes(requete_id INTEGER PRIMARY KEY AUTOINCREMENT, date_text text)"""
  cursor.execute(requetecreationTableRequetes)
  connection.commit()
def insertRequestIntoDB():
  connection = sqlite3.connect('db')
  cursor = connection.cursor()
  requeteLogTable="""INSERT INTO requetes(date_text) VALUES(datetime('now'))"""
  cursor.execute(requeteLogTable)
  connection.commit()
```

</p>
</details>

**Où (quand) appeler la fonction `init` ? Ou (quand) appeler la fonction `insertRequestIntoDB` 



### SQLAlchemy, un exemple d'interface agnostique du SGBD

![](https://i.imgur.com/1fr6KcC.png)

Ce qui arrivera souvent lorsque vous voulez intéragir avec une base de données c'est que vous allez avoir 2 choix : Soit passer directement par une librairie spécifique, soit passer par une ressource "ENGINE" qui permet de requeter sur des bases de nature différentes via des interfaces fonctionnelles, en gros via un driver.


*=> Un enjeu très fort : La portabilité.*

> Typiquement : JDBC pour java..

Dans le cadre de ce tp on vous présentera SQLAlchemy.

Le principe étant que SQLAlchemy propose une spécification que nous allons utiliser pour requêter de notre côté, et que l'implémentation est elle adhérente au gestionnaire de base de données qu'on souhaite utiliser sur le moment.

C'est un pilier de la programmation fonctionnelle : le principe **d'interface fonctionnelle**



Cet engine utilise du coup un driver via la méthode [create_engine('dialect')](https://docs.sqlalchemy.org/en/14/core/engines.html)


Exemple de code : 
```python=
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

with engine.connect() as connection:
    
    connection.execute(text('DROP TABLE IF EXISTS Cars'))
    connection.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY, 
                 Name TEXT, Price INTEGER)'''))
                 
   data = ( { "Id": 1, "Name": "Audi", "Price": 52642 },
             { "Id": 2, "Name": "Mercedes", "Price": 57127 },
             { "Id": 3, "Name": "Skoda", "Price": 9000 },
             { "Id": 4, "Name": "Volvo", "Price": 29000 },
             { "Id": 5, "Name": "Bentley", "Price": 350000 },
             { "Id": 6, "Name": "Citroen", "Price": 21000 },
             { "Id": 7, "Name": "Hummer", "Price": 41400 },
             { "Id": 8, "Name": "Volkswagen", "Price": 21600 }
    )
    
    for line in data:
        con.execute(text("""INSERT INTO Cars(Id, Name, Price) 
            VALUES(:Id, :Name, :Price)"""), **line)
```

#### Aller plus loin : concept d'Object Relationnal Mapping

![](https://i.imgur.com/LyE4fkY.png)

Dans le monde du développement vous serez souvent amené a utiliser ce que l'on appelle un ORM : Object Relationnal Mapper.

Le principe étant que vous allez toujours travailler avec des **objets** python, et donc prendre encore plus de distance avec le type de base de données avec lequel vous travaillez puisque de votre côté il ne s'agira que de faire appel a des fonctions qui concernent vos objets python.


SQLAlchemy propose également des fonctionnalités d'ORM.

exemple de code: 
```python=
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
```


**Exercice** : Adaptez votre code précédent pour qu'il fonctionne pour sqlite3 mais qu'il soit agnostique de la base de données (endpoint : `GET : /label`)


## Mise en place de tests 

![](https://i.imgur.com/h9GnwDQ.jpg)

Python est un langage de script et il peut être pertinent de vérifier si syntaxiquement il est possible d'executer tel ou tel script py, on parle ici de **linting**.

Pour cela, dans l'écosystème python on utilise des outils.


L'objectif étant de détecter le code mort, d'établir des règles pour le projet et éventuellement de déceler des problèmes avant le lancement du code.

### Tests unitaires : pytest unitest

![](https://i.imgur.com/o4150tm.jpg)


Idée générale: tester une partie infime d'une application 

exemple pour l'application de classification verification que la lecture d'un csv ce fait normalement : 

Soit encore => Qu'un fichier csv en entrée pour la nomenclature : 
```csv
code;intitule
A01Z;Culture et production animale, chasse et services annexes
```

Retourne bien après la fonction read_dict(file):
=> 
```python
expectedDict:dict ={'code': 'intitule', 'A01Z': 'Culture et production animale, chasse et services annexes'}
```

Exercice : 

- Crée un repertoire test
- Dans ce repertoire créer un fichier test_app.py
- importer la fonction read_dict de app.main

> petit code snippet :
<details><summary>Spoiler</summary>
<p>

- Créer un fichier nomenclature_NA2008.csv dans tests/nomenclatures/

puis adapter le code suivant pour tests/test_app.py: 
```python
from app.main import read_dict
def test_read_dict():
    expectedDict:dict = {'code': 'intitule', 'A01Z': 'Culture et production animale, chasse et services annexes'}
    assert read_dict('tests/nomenclatures/nomenclature_NA2008.csv') == expectedDict


if __name__ == "__main__":
    test_read_dict()
    print("Everything passed")
```

Là il n'y a pas de framework de test, adaptez avec un framework de type unittest ou pytest, ils permettent une méta gestion des tests de l'application

</p>
</details>

Lancez les tests via les commandes adaptées.

## Journalisation/Logging 

**![](https://i.imgur.com/HK2C53j.png)**

En général pour afficher les informations dans la console/dans un fichier on utilise des moteurs de génération de log, ils permettent principalement de centraliser le fonctionnement de la log par rapport a un print ainsi que de définir des niveau de log : 
- Debug : pour les gens qui adorent spammer les print, ça permet de définir des messages qui aideront a débuguer
- Info / information : donnent des infos => exemple connection OK au serveur..
- warning : signaler un problème non bloquant : " le retour a l'air étrange"
- error : alerte bloquante
- critical : bon.. là c'est la fin

Typiquement en python on pourrait utiliser logging : 
```
pip install logging
```

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

**Exercice**
Adaptez le code précédent en supprimant l'approche bdd et en journalisant dans un fichier **date-call.log**, faites le nécessaire au niveau versionning (.gitignore).
