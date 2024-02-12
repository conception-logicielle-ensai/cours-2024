+++
title = "TP API et webservice"
description = "TP client serveur HTTP"
date = 2024-02-12T00:00:03
short = true
aliases = ["http","web"]
header_img= "/img/webservice/api-webservice-animate-tp.svg"
+++

Le principe de ce TP va être d'explorer et de fournir un service autour des produits de consommation.

Un peu autour du principe de ce petit cas d'exemple de la doc : https://openfoodfacts.github.io/openfoodfacts-server/api/tutorial-dev-journey/

Le cas d'usage : On désire récupérer un ensemble de produit sur le site https://carrefour.fr pour évaluer différentes informations nutritionnelles, leur prix et autre.
## Exploration de l'API qu'on va utiliser dans ce cours
![](https://i.imgur.com/Blucxk5.png)

Des documentations de l'API sont disponibles ici : https://wiki.openfoodfacts.org/API  
et ici : https://openfoodfacts.github.io/api-documentation/

La v1/v2/v3 de l'API nécessite l'authentification des utilisateurs. Pour des raisons pratiques on va plutôt utiliser la V0.

=> Documentation ici : https://world.openfoodfacts.org/files/api-documentation.html


- Tester, depuis votre navigateur, la récupération des informations sur un produit :  
  https://world.openfoodfacts.org/api/v0/product/3256540001305
- Bien que le navigateur soit un client HTTP pratique pour naviguer sur le Web, il existe des clients permettant de construire exactement la requête HTTP que vous souhaitez ce qui se révèle très pratique pour des tests un peu plus avancés (par exemple pour l'envoi d'informations au serveur ou pour l'automatisation). Les plus connus sont probablement [Insomnia](https://insomnia.rest/download) et [Postman](https://www.postman.com/downloads/).

Pour le coup on privilegiera plutôt soit le navigateur soit le client python requests pour différentes requêtes rapides a l'api.

## Exercice 1 : Scénario "a la main"

- Lancez votre navigateur
- Allez sur le site https://www.carrefour.fr/ rayon petit déjeuner : https://www.carrefour.fr/r/epicerie-sucree/petit-dejeuner
- Choisissez un produit et déplacez vous y : exemple `Céréales bio tout chocolat CARREFOUR BIO` => https://www.carrefour.fr/p/cereales-bio-tout-chocolat-carrefour-bio-3560071407711?t=2204

Que constatez vous sur l'url sur laquelle vous êtes allé ? 

> Spoiler : Carrefour utilise le code barre comme identifiant unique des produits, code barre également utilisé pour requêter l'api open food facts

- Testez donc votre produit en allant sur : https://world.openfoodfacts.org/api/v0/product/3560071407711 (en changeant avec l'id de votre produit)

> Vous récupérez une myriade d'information sur celui ci 

Exemple ici (en gardant que certains sous éléments) : 
```json
{
  "code": "3560071407711",
  "product": {
    "traces": "en:milk,en:nuts,en:sesame-seeds,en:soybeans",
    "allergens_from_ingredients": "en:gluten"
  }
}
```

On voit donc que le produit contient des allergènes et des traces.

On aimerait bien scripter pour qu'a partir d'un produit et de différentes intolérances, on puisse savoir si il est consommable ou pas. 
## Exercice 2 - Scripting - Client HTTP

1. Créez un dépot git pour le TP ou repartez du dépot TP conception logicielle du cours 1 et 2
2. Dans ce dépot, créez un dossier `tp4`
3. Initiez un environnement virtuel python `python -m venv venv`
4. Créez un script app.py

> Vous utiliserez la librairie `requests` 

Puis vous ferez le script suivant : A partir d'un code bar on va chercher sur l'api openfoodfacts, les données. 
Puis dans une autre fonction, a partir d'un produit désérialisé en python, on traite simplement si une intolérance est parmi une liste de str d'intolérances en entrée.

> On a maintenant un script qui vérifie les informations par rapport a une demande unitaire
## Exercice 3 - création d'un webservice

On souhaite maintenant rendre ces informations plus automatisables en encapsulant notre script précédent avec une API, qui exposera une ressource en `GET` sur le endpoint `/allergens/{barcode}`

La subtilité est de définir **bar_code** en `PATH_PARAMETER` et **allergens** en `QUERY_PARAMETERS`. Pour bar_code il faudra le mettre en paramètre et dans l'url, pour allergens il faudra utiliser la valeur par défaut : allergens:List[str]  = Query(None)

- Créez une api répondant `hello-world` lorsqu'on la requête sur le endpoint `/allergens` a partir du tutoriel ici : https://fastapi.tiangolo.com/#example
> Remarque : une fois lancée vous pouvez y accéder sur localhost:8000 sur votre navigateur et avec l'interface **swagger** sur localhost:8000/docs
> Vous pouvez également configurer une configuration pour pouvoir passer en mode **debug** https://fastapi.tiangolo.com/tutorial/debugging/?h=debug et lancer l'application avec python 
- Paramétrez votre API pour qu'elle utilise le code de la partie précédente
- Essayez avec différents paramètres

## Spoilers

<details>
  <summary>Spoiler1</summary>

```python
from typing import List

import requests

class FoodInfo:
    def __init__(self,code:str,traces:str,allergens:str):
        self.code = code
        self.traces = traces
        self.allergens = allergens

    def __str__(self):
        return f"'code':{self.code},'traces':{self.traces},'allergens':{self.allergens}"
def get_infos_from_barcode(barcode:str,openfoodfacts_url:str = "https://world.openfoodfacts.org/api/v0") -> FoodInfo:
    try:
        response = requests.get(f"{openfoodfacts_url}/product/{barcode}")
        if response.status_code == 200:
            data_as_json = response.json()
            return FoodInfo(code=data_as_json["code"],traces=data_as_json["product"]["traces"],allergens=data_as_json["product"]["allergens_from_ingredients"])
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

def contains_allergens(food_info:FoodInfo, allergens:List[str]) -> bool:
    for allergen in allergens:
        if allergen in food_info.allergens or allergen in food_info.traces:
            return True
    return False

if __name__ == "__main__":
    infos = get_infos_from_barcode(barcode="3560071407711")
    print(infos)
    has_gluten = contains_allergens(infos,["gluten"])
    print(has_gluten)
```

</details>


<details>
  <summary>Spoiler2</summary>

```python
from typing import List

import requests
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


class FoodInfo:
    def __init__(self,code:str,traces:str,allergens:str):
        self.code = code
        self.traces = traces
        self.allergens = allergens

    def __str__(self):
        return f"'code':{self.code},'traces':{self.traces},'allergens':{self.allergens}"
def get_infos_from_barcode(barcode:str,openfoodfacts_url:str = "https://world.openfoodfacts.org/api/v0") -> FoodInfo:
    try:
        response = requests.get(f"{openfoodfacts_url}/product/{barcode}")
        if response.status_code == 200:
            data_as_json = response.json()
            return FoodInfo(code=data_as_json["code"],traces=data_as_json["product"]["traces"],allergens=data_as_json["product"]["allergens_from_ingredients"])
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)

def contains_allergens(food_info:FoodInfo, allergens:List[str]) -> bool:
    for allergen in allergens:
        if allergen in food_info.allergens or allergen in food_info.traces:
            return True
    return False
@app.get("/allergens/{bar_code}")
def does_contain_allegerns(bar_code:str,allergens:List[str]  = Query(None)) -> bool:
    food_infos = get_infos_from_barcode(barcode=bar_code)
    return contains_allergens(food_infos,allergens)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

</details>

