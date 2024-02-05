+++
title = "Automatisation - Bonus gitlab"
description = "Bonus du cours sur l'automatisation"
date = 2024-02-05T00:00:09
tags = ["tox","python","gitlab","ci-cd"]
header_img= "img/automate.svg"
+++



## Configuration de l'intégration continue sur Gitlab (gitlab-ci)

<img src="https://i.imgur.com/JEsaCtp.png"/>

Gitlab propose une offre d'intégration continue qui se présente au global comme cela : 

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



#### Création d'étapes

On peut effectivement créer des étapes différentes qui fonctionneront de manière successives : d'abord echo1 puis echo2 

=> 

```yaml
stages:
  - echo1
  - echo2

hello-world:
    stage: echo1
    image: ubuntu:20.04
    script:
    - echo "hello world"

hello-world2:
    stage: echo2
    image: ubuntu:20.04
    script:
    - echo "hello world"
```

Dans notre cas on voudra plutôt étudier le linting puis le testing, adaptez donc les étapes.

<details><summary>spoiler</summary>
<p>
ça pourrait donner quelque chose de la forme : 

```yaml
stages:
  - lint
  - test

lint-python-application:
    stage: lint
    image: ubuntu:20.04
    script:
    - echo "hello world"
    
test-python-application:
    stage: test
    image: ubuntu:20.04
    script:
    - echo "hello world"
```

</p></details>

#### Mise a niveau des scripts

Le champ script attend une liste de scripts suivis les un des autres avec des tirets : 

```yaml
stages:
  - echo1
  - echo2

somme-2-2:
    stage: echo1
    image: ubuntu:20.04
    script:
    - echo "2+2="
    - echo "2+2=4"

somme-4-4:
    stage: echo2
    image: ubuntu:20.04
    script:
    - echo "4+4="
    - echo "8"
```

Adaptez donc en rajoutant autant d'étapes que nécessaires pour partir d'un ubuntu et de votre dépot git, avoir un environnement avec pip, installer les dépendances, lancer les tests (toujours en echo)

<details><summary>spoiler</summary>
<p>
ça pourrait donner quelque chose de la forme : 

```yaml
stages:
  - lint
  - test

lint-python-application:
    stage: lint
    image: ubuntu:20.04
    script:
    - echo "recuperer pip"
    - echo "installer les dependances"
    - echo "lancer le linting"
    
test-python-application:
    stage: test
    image: ubuntu:20.04
    script:
    - echo "recuperer pip"
    - echo "installer les dependances"
    - echo "lancer les tests"
```

</p></details>

:boom: Ajoutez donc tout cela a votre dépot git via un add/commit/push


#### Finalisation 
Précedemment, on a vu que via la ligne de commande on pouvait effectivement lancer les tests et le lint dans un environnement qui contient python3 et pip.

Il faut donc adapter les scripts pour, en partant d'un ubuntu version 20.04, récupérer le packet python3-pip puis faire les opérations en ligne de commande successives dans le script permettant de faire en sorte que du linting soit lancé et que des tests le soient également.

:warning: Pour l'usage d'apt : utilisez l'option -y, cela permet de dire oui à tout et donc de permettre le téléchargement sans encombre.

Faites le nécessaire en changeant les lignes de script nécessaires. Comme vous le feriez sur un ubuntu en partant de 0.

Cela donnerait au final : 
```yaml
stages:
  - lint
  - test

lint-python-application:
    stage: lint
    image: ubuntu:20.04
    script:
    - apt update
    - apt install -y python3-pip
    - pip3 install --user tox
    - tox -e pylint

check-format-python-application:
    stage: lint
    image: ubuntu:20.04
    script:
    - apt update
    - apt install -y python3-pip
    - pip3 install --user tox
    - tox -e black
    - tox -e isort
    
test-python-application:
    stage: test
    image: ubuntu:20.04
    script:
    - apt update
    - apt install -y python3-pip
    - pip3 install --user tox
    - tox -e unittest
```

