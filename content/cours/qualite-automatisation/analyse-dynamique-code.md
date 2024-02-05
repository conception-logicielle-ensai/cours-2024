+++
title = "Analyse dynamique du code "
description = "qualités et tests"
date = 2024-02-05T00:00:03
tags = ["unittest","selenium","python","locust"]
header_img= "img/dynamique.svg"
+++
# Analyse dynamique du code

Pour s'assurer du bon fonctionnement, on peut également décider de l'executer de plusieurs manières.
- Executer une fonction isolément dans autres en controllant les input et en vérifiant qu'un output est bien l'attendu : on parle alors de tests unitaires.
- Executer un scénario de test sur une chaine plus grande: si je demande confiture, alors l'application doit me renvoyer la bonne réponse. On parle alors de tests d'intégration.
- Executer un scénario de test concret: si je demande confiture, alors l'application doit me renvoyer la bonne réponse. On parle alors de tests fonctionnels si on est dans un environnement fermé ou test end to end en condition réelle.
- Executer un scénario de montée en charge : Si toutes les secondes quelqu'un demande a mon application différents objets, est ce que l'application va tenir le coup ou est ce que le service va s'arrêter. On parle alors de test de charge.
- Executer un scénario en évaluant la performance : Si je demande a l'application de la confiture, elle doit me répondre en moins de 1 secondes. C'est ici un test de performances.

## Tests unitaires

Les tests unitaires sont les tests des fonctions de manière **isolée**. On entend ici de cette isolation que le contour des fonctions utilisées soit maitrisé et qu'il n'y ait pas de facteur extérieur pouvant altérer l'issue d'un test.

En cela, cela peut parfois être assez laborieux de tester une fonction, puisque l'on veut pouvoir couvrir unitairement tous les **corner case** qu'elle recouvre.

> Exemple : pour une fonction qui renvoie la date du jour, l'on peut en effet vérifier qu'elle le fait selon le bon format, qu'elle le fait bien pour une année donnée et qu'elle renvoie une erreur si elle ne peut pas s'executer.

Pour ce qui est de la forme des tests, ils reposent sur des **assertions**: on souhaite valider le comportement d'une fonction au regard d'un attendu.

```python
assert sum([1, 2, 3]) == 6, "Should be 6")
```

Unittest implémente un panel d'assertions que l'on peut faire.

L'usage le plus classique est le `assertEqual()`

Exemple :

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
```

> Unittest permet l'extension de sa classe TestCase pour récupérer toutes les fonctions qui nous seront utiles dans le testing

Pour lancer les tests il faut effectuer la commande : 
`python3 -m unittest discover -s test -p "test_*.py"`
### Isolation des comportements : Mocking

En programmation , les mocks (simulacres ou mock object) sont des objets simulés qui reproduisent le comportement d'objets réels de manière contrôlée.

L'intêret de ces simulacres, c'est que l'on peut du coup isoler les parties des tests, pour que notre test ne teste réellement que la plus petite brique possible.

Un exemple :

J'utilise un webservice météo pour récupérer des infos, et ensuite effectuer un traitement sur ces données météo.

- L'API peut être indisponible, il faut donc un moyen résiliant de tester les fonctions qui l'utilisent.
- La météo change, si je veux pouvoir tester que ma fonction **get_condition** fonctionne bien par rapport a des données, et donc mettre une clause fixe d'assertion, je suis bloqué. 

=> Mais je peux toujours faire en sorte d'interposer un wrapper qui me renvoie les données a un format connu.

La librairie unittest propose une implémentation du concept de Mock.
Voici un exemple de ce que cela donnerait :

```python
import unittest
from unittest.mock import MagicMock
import requests

def get_condition(city):
    response = requests.get(f'https://weather.com/{city}')
    weather = response.json()
    return weather["condition"]

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.get_patcher = unittest.mock.patch('requests.get')
        self.mock_get = self.get_patcher.start()

    def tearDown(self):
        self.get_patcher.stop()

    def test_get_weather(self):
        self.mock_get.return_value.json.return_value = {'temperature': 72, 'condition': 'sunny'}
        weather = get_condition('San Francisco')
        self.assertEqual(weather, 'sunny')
```

> Pour les objets, il y a également la possibilité d'utiliser MagicMock, ce qui vous permet de reconstruire un objet custom avec fonctions et retours custom

## Tests fonctionnels et End to End

L'idée des tests fonctionnels est de vérifier si l'application fonctionne et répond a un besoin exprimé.

Ils sont en général spécifiés comme des scénarios d'utilisation de l'application. Ils s'executent sur des environnements plus grands et sont donc plus difficiles a définir (souvent pour des cas plus généraux).

Typiquement cela reviendrait a lancer le serveur et a faire une requete dessus dans un processus parallèle.

- Cela peut s'executer simplement directement avec des outils comme requests et unittest : 

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

Cela fonctionne pour une API. On pourrait également utiliser l'implémentation `TestClient` de FASTAPI our des tests fonctionnels et end to end (en condition réelles).

<div class="alert alert-info">
  <strong> Pour info </strong>:
  On verra la semaine prochaine l'outil selenium qui permet de tester les applications web et sites web. On aurait pu également l'utiliser ici mais c'est un peu overkill. Selenium est un outil qui permet de simuler des comportements utilisateurs en utilisant des drivers de navigateurs.
</div>

> Fun fact : le saviez vous ? Vous faites des requêtes HTTP a chaque fois que vous parcourez des pages web. 


## Tests de charge

<img src="/img/loadtest.webp"/>
Les tests de charge permettent d'évaluer les performances d'un système, d'une application ou d'un site web en simulant une charge maximale ou une activité intense.
L'objectif principal est de déterminer comment l'applicatif réagit sous une pression ou une charge importante, en termes de temps de réponse, de capacité à gérer les demandes et de stabilité.
Bien évidemment on ne peut pas nécessairement être aussi proche d'un usage normal qu'en utilisant l'application (on parle alors d'atelier `stress test` ) mais l'objectif est de vérifier la capacité de montée en charge (nombre d'utilisateur) d'un applicatif.

Il existe une myriade d'outils pour effectuer des tests de charge sur les applicatifs. Dans le monde Java par exemple, l'option Jmeter et sa configuration XML est souvent choisi.


Pour python, il existe quelques projets et nous choisirons d'utiliser `locust` : <a href="https://locust.io/">https://locust.io/</a> qui est un projet assez récent et assez pratique à prendre en main pour réaliser des tests.

Locust permet de définir des **tasks** qui sont des templates de script python que l'on peut ensuite executer au travers d'une application web et faire monter en charge.

```
from locust import HttpUser, between, task

class WebsiteTest(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def index(self):
        self.client.get("/")
```

L'objectif de ces outils de tests de charge est de vous permettre de tester sur des environnements réels l'arrivée de plus en plus massive d'utilisateur et de suivre les temps de réponse afin de repérer des limites.
<div class="alert alert-info">
  <strong> Pour aller plus loin</strong> <br/> 
Il est de bon ton lorsqu'on réalise ce genre de tests de s'outiller parallelement avec des outils de monitoring. De nombreux outils existent, et en python on pourra par exemple utiliser l'outil <b>sentry</b> :
<a href="https://github.com/getsentry/sentry">https://github.com/getsentry/sentry</a>
</div>
