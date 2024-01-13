+++
title = "Git avancé"
description = "Concepts plus avancés sur Git"
date = 2024-01-15T00:00:09
short = true
aliases = ["git"]
header_img= "img/git3.svg"
+++

Cette partie présente des concepts avancés importants pour le travail collaboratif sur Git.
## Quoi versionner ?

<img src="/img/quoi-versionner.png">

Une fois qu'on en vient a versionner, une question légitime qui intervient est le "quoi versionner". En effet, une fois mis dans un gestionnaire de version, un mot de passe est donc disponible puisque l'on peut accéder aux anciens commits. C'est donc un risque. De même pour les fichiers de type **Office suite** ou **Libre Office** qui sont des fichiers compressés et pour lesquelles le fonctionnement par différences ne fonctionne pas correctement, git ne peut pas voir la différence au sens de l'ajout d'une ligne sur ce genre de fichiers vu qu'ils sont compressés.

L'idée étant de faire un état des lieux sur différents cas d'usages pour différents types de fichiers.

### Type de fichiers et versionning

#### **Texte vs binaire**

Git est un gestionnaire de versions qui fonctionne en différences.

Il utilise les différences entre les lignes de différents fichiers pour permettre d'identifier les différences. Les différences entre 2 binaires sont donc toujours de l'ordre de l'intégralité du fichier, a cause du formatage binaire.

Pour tous les fichiers textes que sont le code, les fichiers .txt, les fichiers de configuration non sensibles (voir plus bas), git permet une gestion facilitée du versionning puisque les différences relèvent d'ajouts de quelques ko entre différents fichiers, ce qui fait que c'est très peu cher d'avoir tout le dépôt sur le poste de chacun.

#### **Output**

Les fichiers de types output n'ont aucun intêret a être versionné, puisqu'ils sont destinés a être jetables ou sont déjà reconstruisibles par le projet par exemple.

#### **Pas d'information locale / personnelle / secrète**

Toutes les informations personnelles, mais également les informations de configuration de python spécifiques au poste de travail n'ont pas lieu, un versionning doit donc se penser comme agnostique de l'environnement pour des enjeux de portabilité, de reproductibilité et de sécurité.

### Mettre en place des règles sur le versionning

Git permet a juste titre de limiter les fichiers versionnés par l'ajout d'un fichier **.gitignore** à la racine du dépot (au même niveau que le dossier .git).

Ce fichier **.gitignore** liste, au travers d'expressions régulières sur chacunes des lignes, les fichiers qu'il est convenu de ne pas versionner dans le projet.

Voici par exemple un fichier gitignore pour python : https://github.com/github/gitignore/blob/master/Python.gitignore


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Git LFS : référencer les fichiers lourds et non versionnables via des fichiers plus légers
</div>


## Gitflow : Branches et Feature branch

<img src="/img/git-flow.png">

L'objectif du gitflow est de déterminer un mode de fonctionnement en projet, permettant de découper le travail en degré de maturité :

- Une version stable de l'application / qui peut tourner et est fonctionnelle (derniere version livrée)
- Une version en cours de l'application, qui peut tourner mais demande probablement un travail avant l'intégration ou attend que certaines fonctionnalités soient existantes
- Des versions temporaires de l'application, pour lesquelles des fonctionnalités sont en cours de développement : ex correction d'un bug ou ajout d'un endpoint

Pour cela il est nécessaire de s'intéresser aux branches.

### Branche

<img src="/img/gitbranche.png">

Une branche sur git est une ligne du temps indépendante des autres, elle démarre d'une version/commit précis(e). Elle permet de travailler sur des tâches plus grandes et également de travailler a distance en équipe sur des tâches identifiées.

> [lien vers une documentation avec plus de précisions](https://www.atlassian.com/git/tutorials/using-branches#:~:text=Git%20branches%20are%20effectively%20a%20pointer%20to%20a%20snapshot%20of%20your%20changes.&text=Instead%20of%20copying%20files%20from,not%20a%20container%20for%20commits.)

A partir du commit/de la version ou vous vous trouvez vous pouvez créer une branche sur cette version avec la commande git branch:

```bash
# Creer une branche appelée nouvelle-branche
git branch nouvelle-branche
# Supprimer la branche nouvelle-branche en local
git branch -d nouvelle-branche
```

Vous pouvez également vous déplacer sur les branches avec la même commande que pour le déplacement sur les commits :

```bash
# Si nouvelle-branche existe
git checkout nouvelle-branche
# Créer une branche nouvelle-branche et s'y déplacer
git checkout -b nouvelle-branche
```

### Merge

Pour intégrer des changements issus des branches en les mixant avec nos changements, une commande existe : **git merge**

Pour intégrer des changements de la branche nouvelle-branche

```
git merge nouvelle-branche
```

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Conflits git :  <a href="https://opensource.com/article/20/4/git-merge-conflict">https://opensource.com/article/20/4/git-merge-conflict</a>
</div>


### Rebase

<img src="/img/rebase-vs-merge.png">

Pour faire avancer une branche jusqu'a un autre commit (en y déplaçant les changements de l'histoire), vous pouvez réaliser une opération de rebase. 
Cela vous permet de ne pas créer d'histoires parallèles puisqu'il n'y a qu'une ligne du temps.

### Feature / stable branches

<img src="/img/gitflowexample.jpg">
Une idée est donc de créer des branches pour les différents niveau de maturité du projet. Pour cela au niveau du Gitflow, on entendra parler de :

#### **Branches stables**

- Master/main est la branche de référence, stable et contenant la version la plus stable possible du projet
- release-1 / release-2 ..., sont des branches qui intègrent des changements depuis le développement
- develop est une branche contenant le travail en cours sanctuarisé/stabilisé

#### **Features branches**

- Hotfix

> souvent hotfix-\*\*

Ce sont des branches qui permettent de faire des changements brutaux et urgents dans les versions stables suite a des reports de bugs de sécurité par exemple.

- Feature

> souvent topic-\*\*

Les feature branches sont des branches sur lesquels les développement de nouvelles fonctionnalités sont fait.

Workflow classique :

Un développement est fait, il est proposé au review pour l'équipe du projet et puis il est ensuite ajouté a la dernière version de develop.

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Petit guide de workflows classique de travail :  <a href="  https://gist.github.com/blackfalcon/8428401">  https://gist.github.com/blackfalcon/8428401</a>
</div>


## Ecosystème Git : issues, pull requests, forks

Un écosystème s'est construit autour de ces concepts, et certains outils/concepts sont apparus au sein des gestionnaires de version permettant une organisation plus macro.

### Glossaire

**issue**: déclaration d'un bug / d'une nouvelle fonctionnalité demandée : se fait par l'intermédiaire de petits tickets intégrés à Github ou Gitlab par exemple

**pull request**: création d'une demande d'intégration d'une branche (**merge**) pour y effectuer une/des review(s) et y proposer des corrections.

**fork**: copie d'un dépot git.
cas d'usage :

- contribution à un projet où l'on a pas les droits, pour travailler sur la copie et proposer les changements sur le projet (ex: correction bug, opensource, etc..)
- récupération d'un projet qui va passer dans le domaine privé par une personne ou une communauté (c'est pour cela qu'on parle souvent de fork)


