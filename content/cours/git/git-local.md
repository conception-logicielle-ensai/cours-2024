+++
title = "Git avancé : Introduction"
description = "Introduction et git en local"
date = 2024-01-15T00:00:03
aliases = ["git"]
header_img= "img/git1.svg"
+++

<style>
@media print
{
img {width:0}
}
</style>


## Approche pédagogique

Comme vous allez le voir, **Git** est un protocole.

Comme tout protocole, il est possible de l'utiliser de différentes manières en utilisant différents logiciels (on parle d'_implémentations_ ou de _clients_).  
Dans tout ce cours, vous serez amenés à n'utiliser que le terminal afin de bien comprendre les commandes que vous allez utiliser et le fonctionnement de git.  
Une fois que vous considérez avoir compris un concept et les commandes associées, libre à vous d'utiliser le client graphique de votre choix (git extensions, plugin visual studio code, git kraken ...).

## Votre environnement de travail

Pour ce chapitre, vous pouvez pratiquer dans l'environnement de votre choix, le seul prérequis est d'avoir `git` installé et accessible dans un terminal. Vous êtes fortement encouragés, dans ce chapitre comme dans les autres, à multiplier les environnements afin de voir différentes possibilités, les points communs et les différences.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle en ayant installé GIT (pour les utilisateurs Windows, une des options : https://git-scm.com/download/win)
- N'importe quel environnement du [SSPCloud](https://datalab.sspcloud.fr/) : Cloudshell, VSCode, Ubuntu, RStudio ...

> **Feuille de commandes utiles git**: https://education.github.com/git-cheat-sheet-education.pdf

## Pourquoi utiliser Git ?

<img src="/img/versionning_problem.png">

### Préambule

Vous avez besoin de Git si :

- Vous désirez travailler a plusieurs
- Vous désirez travailler sur un projet sur la durée
- Vous désirez récupérer du code et y contribuer.

> Donc en soit :
> 
> **Vous avez besoin de Git si vous écrivez une ligne de code.**

### Un système de gestion de version distribué

<img src="/img/version-control-fig3.png" style="border-style:groove">

Git intervient pour répondre aux besoins de versionning d'application et offre une architecture où tous les développeurs disposent de toutes les versions du code. Cela leur permet de revenir sur des versions précédentes pour comprendre l'origine de certaines fonctionnalités ou dysfonctionnements mais également de synchroniser les environnement de travail locaux avec les environnement distants, puisqu'ils sont de même nature (contiennent l'intégralité du projet et de sa vie).


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>doc officielle : <a href="https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control">https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control</a>
</div>

## Rappels sur git

<img src="/img/git-diagram.svg" style="border-style:groove"/>

### Un dossier pour les gouverner tous

Git fonctionne avec un dossier qui lui est propre : le dossier **.git**.

Ce dossier contient toutes les informations permettant à git de fonctionner (configuration du dépôt, historique ...). Il permet par exemple, en conservant les différences entre les différentes version de naviguer d'une version a l'autre.

> Présence d'un dossier .git = dépôt git

> Funfact : le dossier .git est un dossier caché mais ça ne vous empêche pas de le parcourir / d'y toucher. Son format est cependant assez cryptique pour un humain. Allez y faire un tour à l'occasion :)

> Funfact 2 : sur les systèmes d'exploitation respectables, un fichier / dossier dont le nom commence par un `.` est caché (et inversement)

En général lorsque vous allez récupérer un dépôt sur internet par l'intermédiaire de commande du type `git clone XXX`, le dossier sera également embarqué en local.

Dans le cas où vous souhaitez partir de zéro ou travailler sur un dossier local : 

```
git init
```

Cette commande va créer un dossier `.git` minimal et donc, un dépôt Git.

> A noter : la plupart du temps, vos dépôts git seront créés à partir d'un dépôt externe (cf `git clone` plus loin) plutôt qu'à partir d'un dossier local

Pour aller plus loin 

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Documentation officielle des commandes : <br/> <a href="https://git-scm.com/docs/git-init">git init</a> <a href="https://git-scm.com/docs/git-clone">git clone</a>
</div>


### Creation d'une version

<img src="/img/lifecycle.png" style="border-style:groove">

Sur un dépot Git, vous pouvez créer des nouvelles versions en indiquant a Git les fichiers à inclure dans la prochaine version. (staging)

L'objectif de cette fonctionnalité est de vous permettre de travailler en local sans vous soucier du versionning et puis au moment de faire une version, vous pouvez regrouper vos fichier de manière cohérentes.

Exemple :

- Vous travaillez sur un projet avec deux grandes fonctionnalités
   - La récupération des requêtes utilisateurs sur un produit str
   - Le calcul du type de produit en fonction d'un produit str

Vous modifiez votre code, et au moment de mettre a jour votre dépôt, il est d'usage de créer une version par ajout unitaire.
Donc : 
- Changement calcul
- Puis changement recupération


#### Ajout de fichiers

Pour ajouter des fichier pour la prochaine version, la commande classique est **git add**

```
git add fichier
```

ou, pour ajouter tout les fichiers du dossier courant :

```
git add .
```

> Git utilise ce qu'on appelle un index, permettant de faire la transition entre le repertoire de travail (working directory) et la version (commit)

Pour savoir dans quels états sont vos fichiers, vous pouvez également le vérifier :

```
git status
```

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Doc officielle: https://shafiul.github.io/gitbook/1_the_git_index.html
</div>


#### Un commit : Quézako ?

Un commit est un bloc de modifications (ajouts, modifications, suppressions) sauvegardé dans le dépot Git.

Lorsque l'ensemble des fichiers ajoutés est cohérent pour la réalisation d'une version, on réalise donc une nouvelle version en créant un **commit**

```
git commit [options]
```

exemple :

```
git commit -m "message de commit"
```

> Un commit contient, en plus de l'ensemble des modifications, plusieurs métadonnées dont la date, l'auteur (nom et email) et un message.  
> Funfact : ces métadonnées sont déclaratives, rien ne vous empêche d'anti/post dater un commit par exemple :)

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Doc officielle: https://git-scm.com/docs/git-commit
</div>


### Chaine de commits

<img src="/img/medium-reflog.png" style="border-style:groove">

Sur un dépot git existant, vous pourrez donc accéder aux différentes versions du projet, versions délimitées par des commits.

Vous pouvez observer la liste des commit du projet avec la commande **git log** :

```
git log
git log --pretty=oneline

```

Et vous pouvez accéder aux précédentes versions de votre application par l'utilisation d'un **git checkout** :

```
git checkout <commit-hash>

```

```
git checkout <branch>

```



<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>
  Ecrire une belle histoire: <a href="https://hackernoon.com/beginners-guide-to-interactive-rebasing-346a3f9c3a6d">https://hackernoon.com/beginners-guide-to-interactive-rebasing-346a3f9c3a6d</a>
</div>



