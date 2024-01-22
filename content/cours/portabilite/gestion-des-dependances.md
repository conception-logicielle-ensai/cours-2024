+++
title = "Portabilité et configuration : Dépendances et runtime"
description = "Gestion des dépendances et runtime"
date = 2024-01-22T00:00:02
tags = ["python","pip"]
header_img= "/img/portabilite.svg"
+++


## Interpréteur/Compilateur

<img src="/img/compiler_interpreter.png">

Python appartient à la catégorie des langages interprétés (tout comme Javascript et R, par exemple).  
Un langage interprété possède un interpréteur (on parle aussi de `runtime`)
Pour exécuter un code d'un langage interprété, il faut 2 choses :

- Le code source à exécuter : votre fichier `main.py` par exemple
- Un interpréteur : Pour python, il s'agit de la commande `python` (`python3` sur certains systèmes pour le distinguer de python 2, `python.exe` sur certains systèmes d'exploitation inférieurs)

Pour vérifier que l'interpréteur `python` est bien disponible sur le système, on peut lancer la commande

```
python --version
```

Sidequest : si vous vous demandez où `python` est installé, vous pouvez utiliser la commande `which` (ou `where` pour les systèmes Windows)

<div class="alert alert-info">
  <strong>Pour aller plus loin</strong> <br/> 

Pour les languages compilés, il faut un compilateur qui nous permet depuis notre language a un autre language, souvent de plus bas niveau, executable soit directement par la machine soit par un autre interpréteur.

Pour python, on entend souvent parler de cython : <a href="https://cython.org/">"https://cython.org/"</a>
</div>

<div class="alert alert-info">
  <strong>Pour aller plus loin</strong> <br/> 
   Il existe également des transpileurs, pour convertir des languages en autres languages : ex pour javascript : <a href="https://fr.javascript.info/polyfills"> https://fr.javascript.info/polyfills </a>
</div>

## Environnement d'execution : runtime


Cette partie s'attele a présenter ce qu'on appelle l'environnement d'execution. 
### Qu'est ce que pip

**pip** c'est un gestionnaire de paquets pour python

C'est l'installer de premier choix quand il s'agit d'ajouter des dépendances à un projet python.

- Maven/Gradle pour Java
- Npm/Yarn pour Javascript
- ...

Mais avant cela...


### Qu'est ce qu'un gestionnaire de paquets

Lorsque vous voulez travailler avec des fichiers informatiques, les gestionnaires de paquets sont là pour vous.

Ils permettent :

- d'installer/mettre à jour/désinstaller des logiciels/outils/code

```
pip install <package>
```

<a href="https://pip.pypa.io/en/stable/cli/pip_install/">
Lien vers la référence de la commande
</a>

```
pip uninstall <package>
```

<a href="https://pip.pypa.io/en/stable/cli/pip_uninstall/">
Lien vers la référence de la commande
</a>

**Tout cela avec des petites verifications pour éviter de télécharger les mauvaises dépendances**

> Remarque la commande peut également être pip3 selon votre environnement.


## Wheel : Le format de référence


Lorsque vous installez des packages par l'extérieur vous utilisez déjà probablement des fichiers wheel ou `.whl`.

Une wheel est essentiellement un zip, ou tar qui a un nom qui peut être parsé par pip pour lui permettre de l'installer de manière adaptée sur votre environnement cible.

Regardez plutôt : `{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl`

> Exemple : <a href="https://files.pythonhosted.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl">`requests-2.31.0-py3-none-any.whl`</a>

> Ce qui donne: `{requests}-{2.31.0}-{py3}-{none}-{any}`

Ce genre de spécification est commune a tous les languages dignes de ce noms, puisqu'harmoniser un mode de livraison pour un gestionnaire de paquets harmonisés et cohérents, cela permet une compatibilité assurée entre les différents outils qui les utilisent.
<div class="alert alert-info">
  <strong>Pour aller plus loin : lisez de la doc, c'est bien</strong> <br/> 

Les PEP ou Python Enhancement Proposal sont les évolutions et propositions d'évolutions du language.

Les principales propositions d'améliorations de python qui concernent le packaging sont les suivantes :

Comment packager ? => Wheels : [PEP 427](https://peps.python.org/pep-0427/).

Comment sont construit les numeros de version. Par quelle sémantique ? => [PEP 440](https://peps.python.org/pep-0440/) 

Définir les dépendances d'un package pour permettre la résolution des dépendances mutuelles : [PEP 508](https://peps.python.org/pep-0508/)

Comment build ? [PEP 517](https://peps.python.org/pep-0517)
</div>


### Environnements virtuels dans python

<img src="/img/python-virtualenv-project-structure.jpg"/>

Pour une isolation des paquets installés, et ne pas utiliser tout ce qui existe déjà sur un poste, python permet l'utilisation d'environnements virtuels (virtualenv ou venv).

Ils s'installent au travers du module venv ex :

`python3 -m venv ./venv`

> Cela installe un environnement dans le sous dossier ./venv par rapport au terminal executant le module.

> Note: cet environnement ne doit pas être versionné et donc votre gitignore doit bien le gérer.

Une fois mis en place, vous pouvez le lancer en utiliser la commande en fonction de l'OS:

| Environnement | Terminal   | commande                       |
| ------------- | ---------- | ------------------------------ |
| MacOs         | bash       | `source <venv>/bin/activate`   |
| Linux         | bash       | `source <venv>/bin/activate`   |
| Windows       | cmd.exe    | ` <venv>\Scripts\activate.bat` |
| Windows       | powershell | ` <venv>\Scripts\Activate.ps1` |

- 2 moyens de le vérifier :
    - pip list --local (il n'y a pas grand chose)
    - Vous avez maintenant une parenthèse vous indiquant que vous êtes bien dans votre venv

:boom: Attention à ne pas le versionner toutefois, réferez vous au .gitignore du chapitre git pour plus d'informations

:checkered_flag: maintenant vous pouvez mettre en place l'environnement via pip install -r requirements.txt par exemple

### Pip : Canoniser l'environnement d'execution

<img src="/img/pip-freeze.jpeg"/>

Pour mieux partager un environnement qui permet de faire tourner le code, pip propose de sanctuariser les dépendances dans un fichier **requirements.txt**. C'est l'équivalent des fichiers `package.json` en Javascript (npm), `pom.xml` (Java / maven) ...

Il permet de le générer en faisant à la racine du projet (note : ce fichier peut aussi être créé / modifié à la main) :

```
pip freeze > requirements.txt

```

Et d'installer toutes les dépendances venant d'un fichier de ce type, encore a la racine

```
pip install -r requirements.txt

```

**Le fichier requirements.txt doit être versionné avec votre code sur git**

> Remarque, pip freeze ne fait que des opérations très basiques (lister l'environnement et le sortir dans un message). Il faut donc soit partir d'un environnement d'abord propre (environnement virtuel puis installation de toutes les dépendances), ou utiliser une autre librairie - par exemple pipreqs

En complément on pourra utiliser l'outil `pipreqs` qui fait de l'analyse statique de code (on verra a la prochaine session de quoi il s'agit). Il permet de récupérer les dépendances a partir des imports d'un projet.


exemple d'utilisation depuis un projet
```
pipreqs --print .
```

> Cela va afficher les dépendances trouvées dans tous les sous repertoire du répertoire courant

<div class="alert alert-info">
  <strong>Pour aller plus loin</strong> <br/> 
Doc du paquet pipreqs: <a href="https://pypi.org/project/pipreqs/">https://pypi.org/project/pipreqs/</a>
</div>


## Creation d'un package

Les gestionnaires de paquets permettent a la fois d'utiliser des paquets existants, mais vous le devinez bien, il est possible d'en créer vous même.

Les dépots de packets peuvent être :

- privés - c'est le cas dans les entreprises en général
- publics :
  - c'est le cas du dépôt pypi https://pypi.org/ , vers lequel pointe par défaut une installation de pip.
  - mais également du dépôt de test : https://test.pypi.org/

L'idée de la création d'un package est de créer une brique réutilisable de composants fonctionnels.

Cela peut être par exemple la réutilisation de classes entre différents projets ou la sauvegarde d'un sous ensemble de fonctions utiles que vous aimez utiliser sur les différents projets sur lesquels vous travaillez.

Un package en python a cette forme :

```
projet
├── LICENSE
├── src/
│   └── package
│       ├── __init__.py
│       └── t.py
├──  tests/
├── README.md
└── pyproject.toml
```

A la racine du package se trouve :

- un fichier pyproject.toml, qui contient des métadonnées sur la version, le nom de l'application, etc..
  => Il s'agit d'un fichier python qui permet ensuite de construire un "livrable" au sens de python, prêt a être envoyé.
- Un fichier LICENSE pour préciser le mode d'usage et de partage du package
- un fichier README pour décrire l'usage

Puis il faut, dans cet ordre :

- construire le livrable (avec un outil comme `buildtools`)
- envoyer le livrable (avec un outil comme `twine`)


<div class="alert alert-info">
  <strong>Pour aller plus loin</strong> <br/> 
Comment packager un projet ? : <br/><a href="https://packaging.python.org/en/latest/tutorials/packaging-projects/">https://packaging.python.org/en/latest/tutorials/packaging-projects/</a>
</div>




## Poetry : une alternative sérieuse simplifiant la gestion des dépendances

> https://github.com/python-poetry/poetry

Projet plus récent, répondant a des besoins d'usage non couverts/ mal couverts par pip.

Plusieurs limites existent dans l'utilisation de pip pour un projet de taille réelle :

- Gestion des conflits dans l'installation de packages
- Mauvaise gestion des versions de python // paquets
- Praticité de la réalisation de package sur Pypi
- Gestion fine des dépendances pour les environnements d'execution du code (on ne veut pas les dépendances liées au tests ou a des lignes de commandes qu'on souhaite lancer sur le projet par exemple)
- Gestion des venv pour le projet par rapport aux prérequis (version de python etc..)
- Perennité dans l'installation de package figeant dans le temps une version fonctionnelle du code.

Ici, poetry intègre les notions de versionning, de versions courantes fonctionnelles et crée un lien entre packages et environnement virtuel où l'on execute, ce qui limite naturellement quelques eceuils.

Pour ce qui est du packaging, poetry est un facilitateur dans la mise en place de la configuration pour le déploiement de package. Tout est dans un fichier qui est le même que le fichier de versionning du projet, mais également tout s'effectue d'un seul coup et avec un seul outil.

Pour démarrer il faut l'installer
```
pip install poetry
```

et pour démarrer une config pour poetry : 
```
poetry init
```

Ensuite pour ajouter des package a un projet poetry :
et pour démarrer une config pour poetry : 
```
poetry add requests
```