+++
title = "Automatisation TP"
description = "Cours sur l'automatisation des tests et contrôles sur une base de code"
date = 2024-02-05T00:00:06
tags = ["tox","python","gh-actions","ci-cd"]
header_img= "img/automatetp.svg"
+++

# Qualite, Automatisation et Tests : Environnements de tests et Automatisation

## Exercice 8 : Mise en place de Tox

Mettez en place tox sur votre projet en installant tox via pip et en ajoutant le fichier tox.ini a la racine de votre projet.

=> Aidez vous des parties **Installation** et **Getting started** de la doc

- <a href="https://tox.wiki/en/4.12.1/installation.html">Lien installation</a>
- <a href="https://tox.wiki/en/4.12.1/user_guide.html">Lien user guide</a>

Mettez en place la configuration pour les tests et les différents outils. 

=> Remarque on s'occupera ici que des tests unitaires.



<details>
  <summary><b>Spoiler (clickable)</b></summary>

```toml
[tox]
env_list =py310
minversion = 4.12.1

[testenv:unittest]
description = run the unit tests with unittest
deps =
    unittest2
commands =
    python -m unittest discover -s {toxinidir}/app/test -p "test_cache.py"

[testenv:black]
description = run black
deps =
    black
commands =
    black --check .
    
[testenv:isort]
description = isort
deps =
    isort
commands =
    isort --check --profile black .


[testenv:pylint]
description = pylint
deps =
    pylint
commands =
    pylint {toxinidir}/app
```

</details>

## Exercice 9 : Automatisation du déploiement en continu avec Github Actions

Allez sur l'interface github et ajoutez une nouvelle action a partir d'un template python.

> Vous pouvez également suivre la doc ici : [https://github.com/features/actions](https://github.com/features/actions)

Créez un workflow `XXX.yaml` pour chaque commande dans tox : 
- pylint
- black
- isort
- unittest


<details>
  <summary><b>Spoiler (clickable)</b></summary>
Créer un yaml de ce type par commande : 

```yaml
name: Isort

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11"]
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install tox
      run: |
        python -m pip install --upgrade pip
        pip install tox
    - name: Analysing the code with isort
      run: |
        tox -e isort
```

> isort.yaml


</details>

