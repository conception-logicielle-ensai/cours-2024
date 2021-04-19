# Consolidation

## Objectif et organisation de la séance  

L'objectif de cette séance est de consolider, en pratiquant, les concepts vus dans les séances précédentes.  
Pour cela, vous allez construire une application, en partant de zéro, qui utiliser les données de l'API [OpenFoodFacts](https://world.openfoodfacts.org/data) afin de déterminer si des produits sont vegan ou non.

Le TP est volontairement bien garni, vous êtes libres d'avancer à votre rythme

## Votre environnement de travail

Pour ce chapitre, vous avez accès à un grand nombre d'environnements pour écrire, versionner et exécuter votre code. Les seuls prérequis sont d'avoir accès à `python`, `pip` et `git`.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle
- Un environnement dans le SSPCloud : [Datalab](https://datalab.sspcloud.fr) ou [Che](https://che.lab.sspcloud.fr).  
- [Katacoda](https://www.katacoda.com/courses/python/playground) : un bac à sable avec python préinstallé (attention, `python` correspond au binaire `python 2`, utilisez `python3` à la place)  

## Mise en place du dépôt Git

:label: Cette partie reprend les concepts du TP1 et TP2

Les instructions ci dessous sont applicables globalement à n'importe quel projet que vous pourriez débuter de zéro.

<details><summary>
Se créer un petit dossier depuis votre repertoire
</summary>
<p>

```
mkdir tp5-ensai
cd tp5-ensai
```

</p>
</details>


<details><summary>Puis initier un dépôt git en créant un fichier README.md</summary>
<p>

```
git init
echo "# TP5-conception-logicielle" > README.md
git add . 
git commit -m "init depot"
git remote add origin <url-https>
git push -u origin --all
```

</p>
</details>

Communiquez le dépot gitlab via google docs ! 


<details><summary>Ajoutez le gitignore disponible ici  : <a href="https://github.com/github/gitignore/blob/master/Python.gitignore">https://github.com/github/gitignore/blob/master/Python.gitignore</a></summary>
<p>

```
curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
git add .gitignore
git commit -m "add gitignore"
git push
```

</p>
</details>


## Objectif projet => Dépendances projet

![](https://i.imgur.com/lzFqgzp.png)


:label: Cette partie reprend les concepts du TP2 et TP3

### Contexte

Comme on vous l'a précisé précedemment, l'objectif du tp est de récuperer et traiter des données sur provenant de l'API [OpenFoodFacts](https://world.openfoodfacts.org/data).

Cela implique assez naturellement de récupérer des dépendances permettant de récupérer des données depuis une api : 

- On proposera pour ce tp d'utiliser la librairie **requests**
https://docs.python-requests.org/en/master/

Et pour la partie exposition des résultats (webservice) : 

- On proposera pour ce tp d'utiliser la librairie fastapi 
https://fastapi.tiangolo.com/ 

=> La documentation précise l'usage d'un serveur 
> You will also need an ASGI server, for production such as Uvicorn or Hypercorn.

- On se propose donc d'utiliser uvicorn 
https://www.uvicorn.org/

### Détails

2 Solutions globalement menant au même résultat: 


- partir d'un environnement python vierge (voir venv ci dessous ) puis : 

```
pip install requests
pip install fastapi
pip install uvicorn
```

Et enfin utiliser la commande :
```
pip freeze > requirements.txt
```
pour sauvegarder les dépendances de l'environnement maintenant plus vierge, dans un fichier de configuration.



- Créer le fichier requirements.txt "à la main", puis installer depuis celui là.  

```
pip install -r requirements.txt
```

### Optionnel 


<details><summary>
Mettre en place un environnement virtuel python dédié</summary>
<p>

```bash
python3 -m venv venv
## windows
.\venv\Scripts\activate
## linux
source venv/bin/activate
```

Si vous faites cela, il serait favorable d'ajouter le fichier venv au gitignore puisque cette environnement n'est pas à versionner.

=> Importez le fichier gitignore suggéré pour python ici : 
https://github.com/github/gitignore/blob/master/Python.gitignore

</p>
</details>

## Mise en place de la partie API
![](https://i.imgur.com/4W2xjqO.png)

:label: Cette partie reprend les concepts du TP3

Comme pour toute dépendance, on vous conseille principalement de vous référer à la documentation officielle : 
https://fastapi.tiangolo.com/ 

Partez directement du fichier **main.py** d'exemple et lancez le avec la commande précisez dans la documentation.

Ajoutez une documentation dans votre README.md sur comment lancer votre code (en français ou en anglais)

Ajoutez cela a votre historique projet 

```
git add . 
git commit -m "mise en place de fastapi"
git push
```

## Exemple de requête sur une api sans authentification 

![](https://i.imgur.com/t6QTIWf.png)

:label: Cette partie reprend les concepts vu a l'ENSAI en projet 2A 

### Exploration de l'API  

![](https://i.imgur.com/Blucxk5.png)

Des documentations de l'API sont disponibles ici : https://wiki.openfoodfacts.org/API  
et ici : https://documenter.getpostman.com/view/8470508/SVtN3Wzy  

- Tester, depuis votre navigateur, la récupération des informations sur un produit :  
https://world.openfoodfacts.org/api/v0/product/3256540001305  
- Bien que le navigateur soit un client HTTP pratique pour naviguer sur le Web, il existe des clients permettant de construire exactement la requête HTTP que vous souhaitez ce qui se révèle très pratique pour des tests un peu plus avancés (par exemple pour l'envoi d'informations au serveur ou pour l'automatisation). Les plus connus sont probablement [Insomnia](https://insomnia.rest/download) et [Postman](https://www.postman.com/downloads/)

### Import de dépendance
Afin de consommer les données depuis Python, il nous faut un client HTTP en Python.  
Pour cette partie on se propose de travailler avec la librairie requests : 

https://docs.python-requests.org/en/master/

Importez la via pip
<details><summary>spoiler</summary><p>

```
pip install requests
pip freeze > requirements.txt
```

</p></details>

Cette librairie permet de faire des requêtes http sur des webservices via une api : 

### Mise en pratique

```python=
requete = requests.get("https://world.openfoodfacts.org/api/v0/product/3256540001305.json")
print(requete.status_code)
print(requete.json)
```

Créez une fonction qui récupère les données et les print pour le produit 3256540001305 et ajoutez là à votre endpoint "/"

## Tests unitaires sur vos fonctions d'ajouts
![](https://i.imgur.com/bnRBprR.png)


:label: Cette partie reprend les concepts du TP3 - TP4

:question: Petit point : L'objectif est de développer une fonction qui permet de savoir si un aliment est vegan ou non en l'ayant récupéré sur l'api : 

On retrouve cela dans les balises : "product" => "ingredients" => "vegan" 
qui peut prendre la valeur : 'no' | 'maybe' | 'yes'

Donc après avoir récupéré les données : on peut s'imaginer vouloir développer une fonction qui prend en entrée un tel format de données et renvoie un booléen : 

Dans votre main.py ajoutez la fonction isVegan : 
```python
def isVegan(requestAsJson):
    ingredients = requestAsJson["product"]["ingredients"]
    print(ingredients)
    return True
```

### Import de dépendance

Pytest, unitest : pour l'exemple pytest

id des produits tests exemple :
- [3468570116601](https://world.openfoodfacts.org/api/v0/product/3468570116601.json)
- [3256540001305](https://world.openfoodfacts.org/api/v0/product/3256540001305.json)

Pytest fonctionne de manière classique par nommage : 
Une classe de test doit commencer avec un test_ et les fonction qui sont des tests par des test_

Exemple du tp précédent : 
```python
# test_portefeuille.py
def test_constructeur_portefeuille(portefeuille):
    assert portefeuille.balance == 20
```

Créez un fichier test_openfoodfacts.py avec la fonction suivante : 

```python
import pytest

def test_2_egal_2():
  assert 2==2
```

Vous pouvez maintenant lancer les tests avec la commande pytest

### Importer des données 

![](https://i.imgur.com/XY4RDIl.png)

Une idée quand vous travaillez avec ce genre de données peut être de récupérer un jeu de données minime pour l'intégrer à vos tests:

```python
import json
def load_params_from_json(json_path):
    with open(json_path) as f:
        return json.load(f)
```
Cette fonction permet par exemple de charger en tant que dictionnaire un json qui se trouve dans le "json_path" de votre projet.


Et une fois intégré de commencer a travailler sur vos fonctions depuis ces données de test 
> Cela vous permettra ensuite de faire évoluer vos fonctions tout en respectant les règles d'usage que vous vous étiez fixé en amont.

Vous pouvez maintenant mettre du sens aux tests que vous voulez effectuer:

- Récupérez les données des requêtes précedentes que vous stockerez dans des fichiers .json
- Puis vous pouvez du coup écrire les tests suivants : 

```python=
from main import isVegan

def test_rozana_isVegan_true():
    rozana_data=load_params_from_json('rozana.json')
    assert isVegan(rozana_data) == True

def test_brioche_isVegan_false():
    brioche_data=load_params_from_json('brioche.json')
    assert isVegan(brioche_data) == False
```

> En gros : La rozana c'est vegan, la brioche ce n'est pas vegan

### Un peu de python

Modifiez donc votre fonction isVegan dans la main.py pour que les tests passent.

<details><summary>spoiler</summary>
<p>

```python=
def isVegan(requestAsJson):
    ingredients = requestAsJson["product"]["ingredients"]
    for ingredient in ingredients:
        if 'vegan' in ingredient:
          if ingredient["vegan"]=='no' or ingredient["vegan"]=='maybe':
            return False
    return True
```

</p></details>


**Optionnel:** Changez la réponse HTTP de hello world : vers {"isVegan": True} ou {"isVegan": False}

**Optionnel 2:** Paramétrisez le endpoint pour pouvoir customiser le choix des ingrédients via l'id de l'article attendu sur l'api world openfoodfacts

## Intégration continue

![](https://i.imgur.com/rafowsq.png)

Reprenez ce qui a été fait la semaine dernière pour intégrer les tests en continue sur le projet.

<details><summary>spoiler</summary>
<p>

Créez un fichier : 

.gitlab-ci.yml

```yaml=
tests:
    image: ubuntu:20.04
    script:
    - apt update 
    - apt install -y python3-pip
    - pip3 install -r requirements.txt
    - pytest
```

à la racine du dépot git
</p>
</details>

### Pour aller plus loin : Cas concret Api (hors tp)

Changez d'api et fonctionner par exemple avec l'api twitter. 
:warning: Attention : Cette api requiert Authentification
=> Authentification 
  => Externalisation de la configuration : un token c'est votre identité.
  => Il ne faut surtout pas versionner votre token, donc il faut externaliser votre configuration

L'idée pour externaliser la configuration c'est par exemple d'utiliser les variables environnement système : 

```python=
import os

token = os.getenv('TWITTER_API_TOKEN')
```

Vous pouvez donc par exemple partir de cette configuration, l'adapter pour utiliser le token avec **requests** et ajouter votre token dans votre configuration.

=> Vous êtes prêt à travailler avec des données twitter ...

