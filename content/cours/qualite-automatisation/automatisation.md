+++
title = "Automatisation"
description = "Cours sur l'automatisation des tests et contrôles sur une base de code"
date = 2024-02-05T00:00:05
tags = ["tox","python","gh-actions","ci-cd"]
header_img= "img/automate.svg"
+++

Maintenant qu'on a vu quelques outils, il s'avère pertinent de les lancer le plus souvent possible sur notre code source, et de manière simplifiée.

## Scripting et automatisation : Présentation de Tox

<img src="img/tox.png"/>

Pour cela on va voir quelques outils actuels qui nous permettent d'automatiser la chaine de tests et de qualité de nos développement.

Toute la configuration de ce paquet se fait dans un fichier `tox.ini` a la racine du projet. 

Tox gère les différents environnements virtuels dans ce répertoire.

Cela donne un fichier du type : 
```
[tox]
env_list =py310
minversion = 4.12.1

[testenv:unittest]
description = run the unit tests with unittest
deps =
    unittest2
commands =
    python -m unittest discover -s {toxinidir}/app/test -p "test_cache.py"
```
> tox.ini

> Pour les tests fonctionnels, il est courant de déployer des environnements de tests pour réaliser des tests

Pour finalement lancer les tests, faites la commande : 
`tox -e unittest`

## Gestion des dépendances, matrice de compatibilité et tests 

Les codes sources construit, surtout pour des languages interprétés dépendent de l'environnement d'execution cible. 

On peut se prémunir d'incompatibilités et de bon fonctionnement de nos développements dans un environnement a l'aide de gestionnaires de la configuration dans l'environnement cible.

C'est un des objectif du projet `tox` : <a href="https://tox.wiki/en/4.12.1/index.html">https://tox.wiki/en/4.12.1/index.html</a>

Il offre une configuration des environnements virtuels ainsi qu'une matrice de compatibilité python pour vous permettre de mettre en place des tests sur différentes version de python et également de gérer des groupes de dépendances en fonction de dépendances de run / dépendances de test. 

Il permet également d'aggréger les petites commandes que l'on execute dans des modules scripts, qu'on peut ensuite lancer par une simple commande.

Cela répond donc aux deux problèmes : dépendances spécifiques aux tests et execution automatisée des scripts. Mais depuis un environnement qui a le projet. (donc pour l'instant notre machine).

## L'intégration Continue et Déploiement Continu : CI / CD

Vous avez fait des commandes en terminal durant ce cours, l'idée c'est de généraliser ces commandes dans des scripts à executer souvent pour effectuer des vérifications.

Typiquement : 

Nous avions comme objectif de rendre le code le plus portable possible, c'est bien pour vos collègues mais aussi pour des petits automates qui vont pouvoir faire des vérifications au fur et a mesure de l'avancement du projet.

Et par vérifications on entend (*) : 
- le "Linting" à la main => Voir que le code respecte bien des règles établies.
- le testing (ce qu'on a fait précédemment)

*Puis pas forcément pour le python :* 
- Le build : compilation du code et des dépendances en livrable.
- la release: mise a disposition d'un produit téléchargeable (bin/exe/tar.gz/zip/image docker)

(*) : Après récupération des dépendances projet et avec un environnement qui permet de faire tourner le code



### Cas de github : Github Actions 

Github permet d'executer des workflows lorsque des événements se produisent sur un projet sur github.

Ces workflows sont des scripts executés par des machines au choix : `ubuntu` `windows` ou `macos`.

Ils fonctionnent ainsi : 
- On décrit d'abord dans quel cadre ils doivent être executés. Avec le mot clé : `on`.

- On décrit ensuite différentes phases du traitement qui sont des `jobs`. Ils peuvent être soient des scripts lancés directement sur la machine ou hériter de scripts déjà existants. C'est d'ailleurs un des points forts des actions github.

Ils sont formalisés au format **YAML** ce qui ne devrait pas terrifier des personnes habituées aux structures construites avec des indentations.

Un exemple vaut mieux que mille mots :

```yaml
name: Unittest

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
    - name: Unit testing the code with unittest
      run: |
        tox -e unittest
```

<img src="https://learn.microsoft.com/fr-fr/power-platform/alm/media/github-actions-tutorial/gh-lab-2.80.gif"/>
<div class="alert alert-info">
  <strong> Pour aller plus loin</strong> <br/>  Ensemble des possibles de l'execution : <a href="https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows">https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows</a>
</div>
 

Cela vous permet donc bien de lancer les commandes que vous souhaitez lancer le plus souvent possible sur votre projet : lancer des tests et lancer des contrôles de syntaxes et de qualimétrie du code.

Github surveille les fichiers de type .yaml dans le repertoire .github/workflows de votre projet.
 
<div class="alert alert-info">
  <strong> Pour aller plus loin (notamment les fonc)</strong> <br/> Intégration continue avec gitlab et le gitlab-ci
</div>
 