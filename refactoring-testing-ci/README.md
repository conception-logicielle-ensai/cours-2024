# Refactoring / Testing

## Objectif et organisation de la séance

L'objectif de cette séance est de (re)découvrir des bonnes pratiques de développement. En effet, lorsque l'on conçoit un logiciel, il arrive assez souvent que l'on ait a penser son code sur le long terme, et donc de le rendre le plus lisible, réutilisable et pertinent possible.

C'est une séance centrée sur la lecture et l'écriture de code, donc là vous devez être contents :dancer:

> Petite remarque : Ce qui est présenté dans ce cours n'est pas exhaustif, au cas où il faudrait le préciser.

## Contexte du TP

Vous êtes fraîchement embauchés pour maintenir un projet, mais vous n'aimez pas le code qu'il contient. Du coup vous êtes désireux de faire quelque chose pour régler les problèmes qui le composent.

## Rappels sur les tests

![](https://i.imgur.com/XkaZ8L1.png)

Un test est l'execution d'un programme dans le but de valider le bon fonctionnement du code.

Il peut être effectué pour valider qu'une partie du code s'execute bien (tests unitaires), que l'on répond a une fonctionnalité exprimée (tests d'intégration) ou encore que le code soit résilient (tests de charge ou autre).

### Préambule : Cas d'utilisation des tests

Lorsque les projets grandissent, l'execution d'un workflow complet peut être très couteux et introduire de nombreuses parties incontrolées.

En cela l'environnement de test propose un environnement restreint controllé qui permet de fait de développer de manière plus sécurisée.

De cela on retrouve assez souvent notifié le modèle du Test Driven Development ou encore TDD. L'idée est que si l'on sait ce que doit faire l'application, l'on peut d'abord construire l'environnement de test qui correspond a ces nouveautés, et ensuite gagner du temps a pouvoir faire fonctionner les tests dans cet environnement, ce qui en théorie assure que le développement est valide.

Ensuite, il faut voir le long terme, et c'est un peu l'objectif de cette séance. En effet, lorsqu'on souhaite toucher du code existant, l'on se fie très souvent a des contrats d'API pour ne pas introduire de nouveaux bugs, mais les tests offrent également une visibilité sur l'impact d'ajout/modification de développement dans le code.

### Tests unitaires

Les tests unitaires sont les tests des fonctions de manière **isolée**. On entend ici de cette isolation que le contour des fonctions utilisées soit maitrisé et qu'il n'y ait pas de facteur extérieur pouvant altérer l'issue d'un test.

En cela, cela peut parfois être assez laborieux de tester une fonction, puisque l'on veut pouvoir couvrir unitairement tous les **corner case** qu'elle recouvre.

> Exemple : pour une fonction qui renvoie la date du jour, l'on peut en effet vérifier qu'elle le fait selon le bon format, qu'elle le fait bien pour une année donnée et qu'elle renvoie une erreur si elle ne peut pas s'executer.

Pour ce qui est de la forme des tests, ils reposent sur des **assertions**: on souhaite valider le comportement d'une fonction au regard d'un attendu.

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

Unittest implémente un panel d'assertions que l'on peut faire.

L'usage le plus classique est le `assertEqual()`

Exemple :

````python
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

### Isolation des comportements : Mocking

En programmation orientée objet, les mocks (simulacres ou mock object) sont des objets simulés qui reproduisent le comportement d'objets réels de manière contrôlée.

L'intêret de ces simulacres, c'est que l'on peut du coup isoler les parties des tests, pour que notre test ne teste réellement que la plus petite brique possible.

Un exemple :

J'utilise un webservice météo pour récupérer des infos, et ensuite effectuer un traitement sur ces données météo.

- L'API peut être indisponible, il faut donc un moyen résiliant de tester les fonctions qui l'utilisent.
- La météo change, si je veux pouvoir tester que ma **heatmap** se génère bien par rapport a des données, et donc mettre une clause fixe d'assertion, je suis bloqué. Mais je peux toujours faire en sorte d'interposer un wrapper qui me renvoie les données a un format connu.

La librairie unittest propose une implémentation de Mock.
Voici un exemple de ce que cela donnerait :

```python
import unittest
from unittest.mock import MagicMock
import requests

import incredible_fun
class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.get_patcher = unittest.mock.patch('requests.get')
        self.mock_get = self.get_patcher.start()

    def tearDown(self):
        self.get_patcher.stop()

    def test_get_weather(self):
        self.mock_get.return_value.json.return_value = {'temperature': 72, 'condition': 'sunny'}
        weather = get_weather('San Francisco')
        self.assertEqual(weather, {'temperature': 72, 'condition': 'sunny'})

def generate_heatmap(city):
    response = requests.get(f'https://weather.com/{city}')
    weather = response.json()
    return incredible_fun(weather)
```

### Tests fonctionnels

L'idée des tests fonctionnels est de vérifier si l'application fonctionne et répond a un besoin exprimé.

Ils sont en général spécifiés comme des scénarios d'utilisation de l'application. Ils s'executent sur des environnements plus grands et sont donc plus difficiles a définir (souvent pour des cas plus généraux).

Typiquement cela reviendrait a lancer le serveur et a faire une requete dessus dans un processus parallele

exemple

```python
import subprocess
import requests

server = subprocess.Popen(['python', 'manage.py', 'runserver'])
body = {"first": 1, "operation": "+", "second": 2}
response = requests.post('http://127.0.0.1:8000/')
print(response.status_code)
print(response.content)
server.terminate()
```

### Pour aller plus loin : Lancer des scripts sur un navigateur avec selenium

[Selenium](<https://fr.wikipedia.org/wiki/Selenium_(informatique)#:~:text=Selenium%20est%20un%20framework%20de,un%20utilisateur%20de%20l'application.>)

Selenium est un outil qui permet d'automatiser les actions qui s'effectuent dans un navigateur. L'idée est de permettre de générer des scénarios de tests au plus proche de l'utilisateur final :

- Je me connecte a google.com
- Je saisis la valeur "google"
- Je lance une recherche

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("google search through python")
search.send_keys(Keys.RETURN) #
browser.quit()
```

## Exercice 1: Tests sur un projet existant.

- Pour ce TP on utilisera un projet d'une appli web développée en python : une calculatrice en ligne disponible ici : https://gitlab.com/conception-logicielle/tp4-conception-logicielle

1. Réalisez un Fork de ce projet (vous pouvez toujours vous référer à la séance 1)
2. Clonez le projet a partir de votre Fork
3. Suivez la procédure d'installation du `README.md`
4. Lancez les tests: pour lancer les tests unittest utilise un mécanisme de discovery : essayez la commande `python -m discover application/tests -p  "*_test.py"`
5. On se propose de tester que la fonction soustraction de la classe Calculette() renvoie 2 pour 3-1, réalisez ce test

<details><summary>
L'interpreteur vérifie la syntaxe puis délègue l'execution du calcul a la Calculette. Les tests côté interpreteur sont ils unitaires ?</summary>
<p>

6. Modifiez le code du test pour que cela ne soit plus le cas.

</p>
</details>

## Automatisation - Scripting

### Environnements temporaires - Linux

L'objectif ici est de discuter de l'environnement d'execution.

Dans le cadre de ce cours, on a pu utiliser les environnements virtualisés du SSPCloud mais d'autres environnement existent. Ils reposent en partie sur des technologies de virtualisation :
Machines virtuelles / Conteneurs.

Pour ce qui est des environnements de bureautique, le grand gagnant historique est Windows.

Par contre en ce qui concerne les serveurs et environnement d'executions de traitements, il s'agit en général de distributions linux.

**Besoins d'automatisation**

Pour notre cas, l'objectif est d'établir un environnement reproductible et qui peut faire tourner notre code : donc un environnement qui possède pip & python pour pouvoir executer le reste de nos scripts.

**Gestionnaire de paquet**
Les distributions Linux contiennent en général un gestionnaire de paquets permettant d'installer (et mettre à jour / désinstaller) des nouvelles applications / commandes facilement
Dans la suite, on va manipuler `apt` (aussi appelé `apt-get`) qui est le gestionnaire de paquets de `Debian` et de ses dérivés (Ubuntu, Linux mint ...)

Pour installer un paquet, il suffit d'appeler la commande `install` de `apt` :
`apt install nomdupaquet`

Il peut être nécessaire de d'abord mettre à jour la liste des paquets disponibles : `apt update`

> Note : l'utilisation d'`apt` requiert les droits super-utilisateur (root). Vous allez donc généralement préfixer la commande par `sudo`

Ainsi pour installer python et pip sur un environnement qui a apt

### (pour aller plus loin) Tox

https://tox.wiki/en/latest/user_guide.html

Tox est un gestionnaire d'environnement d'execution pour automatiser des scripts. Il permet de mieux déclarer l'environnement d'execution des tests, de standardiser les prérequis a l'execution des tests pour simplifier la prise en main et renvoie les résultats de tests sous forme de rapports.

Il permet de changer la configuration de :

- Quelques scripts dans un README.md

à

- Un script unique pour les gouverner tous `tox`

## Exercice 2: Automatisation - Scripting

Pour cette exercice, on va travailler sur un environnement linux.

Pour cela on se propose d'utiliser un ubuntu en ligne du sspcloud ou votre machine, si c'est un linux.

**Scripting**

1. Créez un service en ligne ubuntu ou skippez cette étape.

2. Lancez un terminal, essayer les commandes `python` `python3`

> Spoiler: elles ne sont pas installées

3. Nous allons les installer:

Mettons tout d'abord a jour les dépendances : `sudo apt update` => traduction `sudo` en tant que super utilisateur, `apt update` je met a jour ce que voit mon gestionnaire de paquet

Ensuite installons python3 et pip :
`sudo apt install python3-pip`

4. Clonez votre dépot

5. Lancez vos tests

6. Mettez toutes les commandes que vous avez utilisé dans un fichier. (la commande `history` peut s'avérer utile)

### Intégration continue

<img src=https://i.imgur.com/Mkjq6jX.png width="500"/>

### Concepts

Vous avez fait des commandes en terminal durant ce cours, l'idée c'est de généraliser ces commandes dans des scripts à executer souvent pour effectuer des vérifications.

Typiquement :

Nous avions comme objectif de rendre le code le plus portable possible, c'est bien pour vos collègues mais aussi pour des petits automates qui vont pouvoir faire des vérifications au fur et a mesure de l'avancement du projet.

Et par vérifications on entend (\*) :

- le "Linting" à la main => Voir que le code respecte bien des règles établies.
- le testing (comme on a vu plus haut)

Puis pas forcément pour le python :

- Le build : compilation du code et des dépendances en livrable.
- la release: mise a disposition d'un produit téléchargeable (bin/exe/tar.gz/zip) / déploiement d'un paquet sur Pypi par ex

(\*) : Après récupération des dépendances projet et avec un environnement qui permet de faire tourner le code)

### Configuration de l'intégration continue sur Gitlab (gitlab-ci)

![](https://i.imgur.com/JEsaCtp.png)

Gitlab propose une offre d'intégration continue qui se présente au global comme cela :

> Remarque, si vous n'avez que récemment eu un compte sur gitlab, vous n'aurez potentiellement pas l'option

1. Vous partez d'un dépot qui contient exactement votre dépot git via git clone puis cd depot.

2. Définition d'étapes d'intégration : linting / test / build / release / deploiement (nom libre)

3. Précision de ces étapes en petits scripts qui correspondent aux operations que vous voulez faire et dans quel environnement vous voulez les lancer : (python avec un C++, ubuntu,...).

#### Un exemple

exemple pour une étape d'affichage d'un message dans la console d'un ubuntu 20.04 :

```yaml
stages:
  - echo

hello-world:
  stage: echo
  image: ubuntu:20.04
  script:
    - echo "hello world"
```

Tout cela dans un fichier .gitlab-ci.yml situé à la racine du dépot git (là ou se trouve le .git).

## Exercice 3: Automatisation des tests sur le projet.

1. Créez un fichier .gitlab-ci.yml a la racine de votre projet sur gitlab

```yml
stages:
  - echo

hello-world:
  stage: echo
  image: ubuntu:20.04
  script:
    - echo "hello world"
```

2. Commitez ce fichier, et envoyez le sur le dépot distant, une petite bulle devrait avoir apparu sur votre dépot.

3. A partir du script de l'exercice 2, vous pouvez créer un script qui a partir d'une ubuntu 20.04 lance les tests sur le projet

```yml
stages:
  - test

hello-world:
  stage: test
  image: ubuntu:20.04
  script:
    - sudo apt ...
    - sudo apt ...
    - pip ...
    - python ...
```

## Qualité de code, un vaste sujet

### Nommage et cohérence

Lors de la séance précédente, l'on a présenté le linting et PEP8. C'est une spécification pour le nommage. L'objectif est de toujours bien nommer les fonctions par rapport a ce qu'elle font.

```python
def q(a:int,b:int):
    """
    effectue le quotient entre a et b
    """
    return a/b
```

```python
def quotient(numerateur:int,denominateur:int):
    return numerateur/denominateur
```

Une règle pour vous peut être de limiter au stricte minimum les commentaires, en effet si vous ressentez un besoin de commenter c'est que le code n'est probablement pas suffisament clair.

**règles de nommages et typage : cas des booléens**
Lorsque vous écrivez des champs ou des fonctions qui résultent en un booléen, la pratique est d'utiliser un nommage sous la forme d'une question.

```python
  def sup_a_2(nombre:int):
    return nombre > 2
```

```python
  def est_superieur_a_2(nombre:int):
    return nombre > 2
```

### Single Responsibility Principle

Le principe est que chaque fonction ou classe ne doit faire qu'une seule chose. Il est en effet plus simple d'assembler des modules simples que de manipuler des modules plus grands.

**Notamment** : Une fonction qui renvoie une valeur, ne doit pas renvoyer un message. Elle doit raise une exception, le type de retour doit être le plus fixe possible.

### Magic numbers : valeurs sans contexte

Les magic number ou nombre magiques en français sont des constantes non nommées. Elles introduisent de la complexité surtout pour la relecture et l'utilisation du code par une personne n'ayant pas développé la fonctionnalité.

Exemple

```python
def check_threshold(value):
    if value > 0.5:
        print(value, "is above the threshold.")
    else:
        print(value, "is below the threshold.")

if __name__ == "__main__":
    check_threshold(0.3)
    check_threshold(0.6)
```

vs

```python
# Threshold Value Example
THRESHOLD_VALUE = 0.5

def check_threshold(value):
    if value > THRESHOLD_VALUE:
        print(value, "is above the threshold.")
    else:
        print(value, "is below the threshold.")

if __name__ == "__main__":
    check_threshold(0.3)
    check_threshold(0.6)
```

### (Aller plus loin) Immutabilité des fonctions

Le principe de l'immutabilité des fonctions est de ne pas altérer les champs passés en paramètres a la fonction, afin de ne pas créer d'effet de bord.

Par défaut en python, les types simples (int,str,bool) sont immutables, contrairement aux autres.

Cela donne:

```python
def somme(a:int,b:int):
    a=a+b
    return a
a = 1
b = 2
c = somme(a,b)
print(a) # 1
print(c) # 3
```

Alors que

```python
    def somme(int_list: list[int]):
        for i in range(1, len(int_list)):
            int_list[0] = int_list[0] + int_list[i]
        return int_list[0]

    list = [1, 2]
    c = somme(list)
    print(list[0])  # 2
    print(list[1])  # 3
```

C'est au coeur de la programmation fonctionnelle

> On oublie pas ce qu'on a vu : portabilité

## Exercice 4 : Refactoring

1. Nommage : La classe NoParenthesesInterpreteur a des fonctions booléenes au mauvais format, changez les.

2. Single Responsability Principle : Un test est désactivé dans la classe de test CalculetteTest(), réactivez le et résolvez le problème.

3. Magic number : proposez une solution permettant de ne pas avoir partout dans le code, les symboles "+" "-" "\*" "/". L'on souhaite changer le symbole de multiplication en "x", constatez l'intêret.
