+++
title = "Analyse dynamique du code : TP"
description = "TP qualités et tests"
date = 2024-02-05T00:00:04
tags = ["unittest","selenium","python","locust"]
header_img= "img/dynamiquetp.svg"
+++
# Qualite, Automatisation et Tests : Analyse dynamique du code

Pour tester quelque chose, nous n'allons pas ici s'intéresser a tester un existant mais bien a développer une nouvelle fonctionnalité pour l'API predicat.

Cette fonctionnalité sera une fonctionnalité de cache sur la réponse de la prédiction, afin de gagner en efficacité.

> En informatique moderne, pour répondre a un lot important de requêtes utilisateurs, différentes solutions existent (dénormalisation, cache)..

L'objectif du cache est de sauvegarder une réponse a une demande existante pour ne pas recalculer la réponse mais simplement renvoyer la réponse précédement émise.

Ce que ça donne c'est donc, dans le contexte global : définition d'un dictionnaire. Et alimentation de ce dictionnaire pendant le run et bypass de fonction si cela a déjà été calculé.

> Exemple basique :
```python
cache = {}
def get_in_cache_else_return(function_call, function_name, argument):
    cache_key=f"{function_name}-{argument}"
    if cache_key in cache:
        print("cache exists")
        return cache[cache_key]
    else:
        cache[cache_key] = function_call
        return cache[cache_key]

def a(b:int):
    return b+1

print(get_in_cache_else_return(a(1),"a","b"))
# 3
print(get_in_cache_else_return(a(1),"a","b"))
# Cache exist | 3
```
## Exercice 4 : Ajout de la fonctionnalité

- 1 - On va faire un petit refactor : on va prendre l'intégralité du code ici :
```python
    if n == "all":
        n = [i for i in config["models"]]
    if type(n) == str:
        n = [n]
    output = {}

    for nomenclature in n:
        output[nomenclature] = {}
        descriptions = sorted(set(q), key=q.index)
        preprocessed_descriptions = [
            preprocess_text(description) for description in descriptions
        ]
        preds = predict_using_model(
            preprocessed_descriptions, model=models[nomenclature], k=k
        )
        if v:
            for pred in preds:
                for pred_k in pred:
                    pred_k["label"] += " | " + full_dict.get(pred_k["label"], "")
        for description, pred in zip(descriptions, preds):
            output[nomenclature][description] = pred

```

Et le déplacer dans une fonction dédiée : 

```python
def predict_label_core(q:str,k:int,v:Optional[bool],n:Literal["na2008", "coicop", "na2008_old", "all"]):
    if n == "all":
        n = [i for i in config["models"]]
    if type(n) == str:
        n = [n]
    output = {}

    for nomenclature in n:
        output[nomenclature] = {}
        descriptions = sorted(set(q), key=q.index)
        preprocessed_descriptions = [
            preprocess_text(description) for description in descriptions
        ]
        preds = predict_using_model(
            preprocessed_descriptions, model=models[nomenclature], k=k
        )
        if v:
            for pred in preds:
                for pred_k in pred:
                    pred_k["label"] += " | " + full_dict.get(pred_k["label"], "")
        for description, pred in zip(descriptions, preds):
            output[nomenclature][description] = pred
```

Ainsi :  

```
async def predict_label(
    q: List[str] = Query(
        ...,
        title="query string",
        description="Description of the product to be classified",
    ),
    k: int = Query(
        1, title="top-K", description="Specify number of predictions to be displayed"
    ),
    v: Optional[bool] = Query(
        False, title="verbosity", description="If True, add the label of code category"
    ),
    n: Literal["na2008", "coicop", "na2008_old", "all"] = Query(
        "all", title="nomenclature", description="Classification system desired"
    ),
):
    if n == "all":
        n = [i for i in config["models"]]
    if type(n) == str:
        n = [n]
    output = {}

    for nomenclature in n:
        output[nomenclature] = {}
        descriptions = sorted(set(q), key=q.index)
        preprocessed_descriptions = [
            preprocess_text(description) for description in descriptions
        ]
        preds = predict_using_model(
            preprocessed_descriptions, model=models[nomenclature], k=k
        )
        if v:
            for pred in preds:
                for pred_k in pred:
                    pred_k["label"] += " | " + full_dict.get(pred_k["label"], "")
        for description, pred in zip(descriptions, preds):
            output[nomenclature][description] = pred

    return output
```

devient :

```python
async def predict_label(
    q: List[str] = Query(
        ...,
        title="query string",
        description="Description of the product to be classified",
    ),
    k: int = Query(
        1, title="top-K", description="Specify number of predictions to be displayed"
    ),
    v: Optional[bool] = Query(
        False, title="verbosity", description="If True, add the label of code category"
    ),
    n: Literal["na2008", "coicop", "na2008_old", "all"] = Query(
        "all", title="nomenclature", description="Classification system desired"
    ),
):
    return predict_label_core(q=q,k=k,v=v,n=n)
```

Ensuite il faut qu'on fasse notre cache : 
```python
cache = {}
def get_in_cache_else_return(function_call, function_name, argument):
    cache_key=f"{function_name}-{argument}"
    if cache_key in cache:
        return cache[cache_key]
    else:
        cache[cache_key] = function_call
        return cache[cache_key]

async def predict_label(
    q: List[str] = Query(
        ...,
        title="query string",
        description="Description of the product to be classified",
    ),
    k: int = Query(
        1, title="top-K", description="Specify number of predictions to be displayed"
    ),
    v: Optional[bool] = Query(
        False, title="verbosity", description="If True, add the label of code category"
    ),
    n: Literal["na2008", "coicop", "na2008_old", "all"] = Query(
        "all", title="nomenclature", description="Classification system desired"
    ),
):
    return get_in_cache_else_return(predict_label_core(q=q,k=k,v=v,n=n),"predict_label_core",q)
```
## Exercice 5 : Test unitaire

La fonction de cache comme vu dans l'exemple plus haut, se teste indépendamment de la fonction appelée si non présent dans le cache.

- Implémentez un test avec une fonction que vous développerez pour vérifier que le cache est fonctionnel.


<details><summary><b>AIDE 1 (clickable): Aide avec spoiler </b></summary>
<p>

ça donne un truc du genre avec une fonction mock
```python
import unittest
from unittest.mock import Mock

cache = {}
def get_in_cache_else_return(function_call, function_name, argument):
    cache_key = f"{function_name}-{argument}"
    if cache_key in cache:
       return cache[cache_key]
    else:
       cache[cache_key] = function_call
       return cache[cache_key]
class TestCache(unittest.TestCase):

    def test_get_cache_else_return_ok(self):
        mock_function = Mock(side_effect=[1,2])
        self.assertEqual(1,get_in_cache_else_return(mock_function(),"mock_func",None))
        self.assertEqual(1,get_in_cache_else_return(mock_function(), "mock_func", None))
```

> On notera bien qu'il y a un problème avec le fait que la fonction dépend du contexte et donc il manque l'implémentation d'une fonction statique.

</p></details>

## Exercice 6 - test de l'API - test fonctionnel

Implémentez un test qui démarre votre API puis lance une requête dessus et vérifie que le résultat est cohérent.

> Quels problèmes peuvent être rencontrés dans l'usage d'un tel test ?

<details><summary><b>=> Solution (clickable) </b></summary>
<p>


```python
import unittest
import requests
class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import subprocess
        cls.apiprocess = subprocess.Popen(["uvicorn", "main:app"])
        cls.wait_for_api()
    @classmethod
    def tearDownClass(cls):
        cls.apiprocess.terminate()
    @classmethod
    def wait_for_api(cls):
        import time
        url = "http://localhost:8000/"
        delay = 1
        attempts = 100
        for _ in range(attempts):
            try:
                requests.get(url)
                break
            except requests.ConnectionError:
                time.sleep(delay)
        else:
            raise TimeoutError(f"API didn't start in {delay*attempts} seconds")
    def test_get_label_confiture_ok(self):
        response_http = requests.get("http://localhost:8000/")
        self.assertEqual(response_http.status_code,200)
```

</p>
</details>

## Exercice 7 - Montée en charge de l'API

S'exercer sur locust a partir de la documentation disponible ici : 

https://docs.locust.io/en/stable/index.html

A partir du volet get_started, démarrer un serveur locust qui peut effectuer une requête sur le endpoint `/` d'une application web.

Testez ensuite sur votre application lancée en local en mode **headless**

<a href="https://docs.locust.io/en/stable/quickstart.html#direct-command-line-usage-headless">https://docs.locust.io/en/stable/quickstart.html#direct-command-line-usage-headless</a>