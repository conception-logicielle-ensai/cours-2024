# Git, Git avancé

## Approche pédagogique

Comme vous allez le voir, Git est un protocole. Comme tout protocole, il est possible de l'utiliser de différentes manières en utilisant différents logiciels (on parle d'_implémentations_ ou de _clients_).  
Dans tout ce cours, vous serez amenés à n'utiliser que le terminal (ne paniquez pas, ça va bien se passer) afin de bien comprendre les commandes que vous allez utiliser et le fonctionnement de git.  
Une fois que vous considérez avoir compris un concept et les commandes associées, libre à vous d'utiliser le client graphique de votre choix (git extensions, plugin visual studio code, git kraken ...).

## Votre environnement de travail

Pour ce chapitre, vous pouvez pratiquer dans l'environnement de votre choix, le seul prérequis est d'avoir `git` installé et accessible dans un terminal. Vous êtes fortement encouragés, dans ce chapitre comme dans les autres, à multiplier les environnements afin de voir différentes possibilités, les points communs et les différences.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle en ayant installé GIT (pour les utilisateurs Windows, une des options : https://git-scm.com/download/win)
- N'importe quel environnement du [SSPCloud](https://datalab.sspcloud.fr/) : Cloudshell, VSCode, Ubuntu, RStudio ...
- [Katacoda](https://www.katacoda.com/courses/git) (nécessite inscription / authentification) : des tutoriaux interactifs avec mise à disposition d'environnements éphémères
- [Gitpod](https://www.gitpod.io) (nécessite inscription a partir d'un compte gitlab/github) : permet d'initier un environnement de travail a partir d'un dépot.

**Feuille de commandes utiles git**: https://education.github.com/git-cheat-sheet-education.pdf
## Pourquoi Git ?

<img src="img/versionning_problem.png">

### Préambule

Vous avez besoin de Git si :

- Vous désirez travailler a plusieurs
- Vous désirez travailler sur un projet sur la durée
- Vous désirez récupérer du code et y contribuer.

Donc en soit :

Vous avez besoin de Git si :

- Vous écrivez au moins une ligne de code

### Un système de gestion de version distribué

<img src="img/version-control-fig3.png" style="border-style:groove">

Git intervient pour répondre aux besoins de versionning d'application et offre une architecture où tous les développeurs disposent de toutes les versions du code. Cela leur permet de revenir sur des versions précédentes pour comprendre l'origine de certaines fonctionnalités ou dysfonctionnements mais également de synchroniser les environnement de travail locaux avec les environnement distants, puisqu'ils sont de même nature (contiennent l'intégralité du projet et de sa vie).

Pour aller plus loin : https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

## Rappels de Git

<img src="img/git-diagram.svg" style="border-style:groove"/>

### Un dossier pour les gouverner tous

Git fonctionne avec un dossier qui lui est propre : le dossier **.git**. Ce dossier contient toutes les informations permettant à git de fonctionner (configuration du dépôt, historique ...). Il permet par exemple, en conservant les différences entre les différentes version de naviguer d'une version a l'autre.

> Présence d'un dossier .git = dépôt git

> Funfact : le dossier .git est un dossier caché mais ça ne vous empêche pas de le parcourir / d'y toucher. Son format est cependant assez cryptique pour un humain. Allez y faire un tour à l'occasion :)

> Funfact 2 : sur les systèmes d'exploitation respectables, un fichier / dossier dont le nom commence par un `.` est caché (et inversement)

Si vous voulez créer un dépôt git dans un dossier :

```
git init
```

Cette commande va créer un dossier `.git` minimal et donc, un dépôt Git.

> A noter : la plupart du temps, vos dépôts git seront créés à partir d'un dépôt externe (cf `git clone` plus loin) plutôt qu'à partir d'un dossier local

Documentation officielle de la commande : https://git-scm.com/docs/git-init

### Creation d'une version

<img src="img/lifecycle.png" style="border-style:groove">

Sur un dépot Git, vous pouvez créer des nouvelles versions en indiquant a Git les fichiers à inclure dans la prochaine version. (staging)

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

Pour aller plus loin : https://shafiul.github.io/gitbook/1_the_git_index.html

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

Pour aller plus loin : https://git-scm.com/docs/git-commit

### Exercice 1

Pour ce premier exercice, écrivons ensemble l'histoire suivante :

- Créer un dossier pour votre projet : tp1-conception-logicielle
- Créer un petit programme en python qui renvoie l'heure actuelle dans la console au format "HH:MM:SS" dans un fichier main.py
- Ajoutez ce fichier dans l'index et créer une nouvelle version. (commit)
- Ajout d'un second fichier, vide, `README.md`  
  A quelle heure le dernier commit a t'il été écrit ? Quel est son _hash_ (identifiant) ?
- Ajoutez un zonage sur la date pour récupérer l'heure qu'il est a New York. Créez un commit avec le message "ajout zonage".

Félicitations ! Vous avez un joli dépôt git contenant une première histoire.

> NB: si vous n'avez pas d'idées sur comment on peut réaliser certaines parties du tp, des aides sont disponibles dans des sections dédiées

<details>
  <summary>Aide 1</summary>

```python
from datetime import datetime

current_time = datetime.now()
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted)
```

> main.py (première version)

```python
from datetime import datetime
import pytz # $ pip install pytz

timezone = pytz.timezone('America/New_York')
current_time = datetime.now(timezone)
current_time_formatted = current_time.strftime("%H:%M:%S")
print(current_time_formatted))
```

</details>

### Chaine de commits

<img src="img/medium-reflog.png" style="border-style:groove">

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

### Aller plus loin

- [Git mystery](https://github.com/nivbend/gitstery)
  > Projet git d'enquête sur un meurtre mobilisant diverses compétences sur Git, sympathique pour comprendre les notions et la navigation entre les versions via Git.
- écrire une belle histoire: https://hackernoon.com/beginners-guide-to-interactive-rebasing-346a3f9c3a6d

### Exercice 2

- Déplacez vous sur le premier commit de votre dépot.

<details>
  <summary>Aide 2</summary>

```
git log
```

puis

```
git checkout
```

</details>

## Git, gitlab, github ...

<img src="img/git-gitlab-github-bitbucket.jpeg">

Avec la réussite de Git, des outils appelées Forges Logicielles sont apparues. Elles permettent de proposer l'hébergement du code source d'application publiques et privées de manière gratuite et offrent d'autres services de gestion ainsi que des interfaces clients appréciables.

On distingue 2 catégories de forges : les forges "As A Service" qui sont mises à disposition par des entreprises tierces et dont les données sont hébergées chez ces fournisseurs et les forges "On premise" qui sont hébergées directement dans les organisations qui les utilisent.

Exemples de forges "As A Service" :

- [Github.com](https://github.com) est un des leaders du marché, hébergeant une grande partie du code open source et des grands projets ouverts. Github a été racheté par Microsoft en 2018 pour 7.5 milliards de dollars. Le code source de github n'est pas public.
- [Gitlab.com](https://gitlab.com) est un concurrent très actif. Le code qui sous-tend gitlab.com est en très grande partie libre : https://gitlab.com/gitlab-org/gitlab
  Important : `gitlab.com` est une installation particulière du logiciel gitlab sur les serveurs de l'entreprise gitlab. Vous rencontrerez, dans votre carrière, d'autres installations du logiciel gitlab sur d'autres serveurs (cf "On premise"). Attention donc à ne pas confondre le service `gitlab.com`, le logiciel gitlab et les différentes installations de gitlab que vous rencontrerez.
- [Bitbucket.org](https://bitbucket.org/) : moins utilisé, il appartient à Atlassian (connu pour son outil de gestion de projet / ticket `Jira`)

Exemples de forges "On premise" :

- [Gitlab sspcloud](https://git.lab.sspcloud.fr)
- [Gitlab INSEE](https://gitlab.insee.fr) : accessible uniquement depuis le réseau INSEE
- [FramaGIT](https://framagit.org/explore/projects)

De nos jours, la plupart des forges "on premise" sont des installations du logiciel gitlab mais il existe des alternatives. Citons par exemple https://gogs.io/ et https://fusionforge.org/

### Dépôts centraux

<img src="img/basic-remote-workflow.png" width="100%">

Pour git, un écosystème de forges logicielle s'est développé permettant le partage de code facilité pour les développeurs et proposant différents services : interface graphique, ressources pour héberger de la documentation ou encore intégration continue.

Les plus célèbres sont probablement GitHub, Gitlab et BitBucket. Proposant pour Github une communauté plus importante mais pour Gitlab qui est un projet OpenSource, une integration facilité dans une infrastructure interne.

### Récupération d'un projet

<img src="img/pull.png" width="100%">

Votre projet local peut être rattaché a un projet distant, vous pouvez interagir en ce sens par la commande **git remote**

```git
git remote -v
git remote add origin <https://url-du-projet>
```

Si vous voulez simplement récupérer un projet hébergé sur un dépôt distant.

```git
git clone <https://url-du-projet>
```

Pour aller plus loin :

- Authentification : ssh/https - https://gist.github.com/grawity/4392747

### Exercice 3

1. Commencez par utiliser un compte existant / créer un compte sur https://gitlab.com/

2. Une fois connecté, créez un nouveau dépot appelé mon-tp1-conception-logicielle

3. Ajoutez le dépot distant a votre projet (relier)

4. Récupérez également, dans un autre dossier,le code du dépôt https://gitlab.com/conception-logicielle/tp1-conception-logicielle

### Travailler a distance

<img src="img/ez-pull-push.png">

#### **Récuperer des changements**

Pour récupérer les changements effectués sur le dépôt la commande la plus utilisée est :

```
git pull
```

Elle permet de récupérer les changements (commit) et de les ajouter a la copie de travail en local

> Remarque : c'est une opération que l'on effectue souvent avant de vouloir ajouter notre code pour qu'il n'y ait pas de fichiers dont git ne saurait pas quel version prendre

Pour aller plus loin : récuperer des changements sans les intégrer - [git fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch)

#### **Envoyer des changements**

Pour envoyer vos changements sur un dépot déclaré en remote, on utilise la commande **git push**:

_Cas d'usages classiques_

```bash
# envoyer vos changements (commits) à votre origin
git push
# envoyer votre code a votre origin et déclarer une branche origin/branch
git push --set-upstream origin branch
# envoyer votre code (commits) a votre origin en pushant la branche master
git push -u origin master
```

### Exercice 4

- Envoyez le code construit au TP1 sur votre dépôt distant.

## Quoi versionner ?

<img src="img/quoi-versionner.png">

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

### Exercice 5

C'est votre premier jour de boulot ! A votre arrivée, on vous remet une clé USB contenant le code de l'application/des données.

Choisir, dans la liste ci-dessous, l'émoji le plus approprié à la situation :

- :pensive:
- :cry:
- :scream:
- :thumbsup:
- :thumbsdown:
- :runner:

Pour chacun des cas suivants, créer un dépôt Git en respectant les règles / bonnes pratiques de versionning.

- [Cas 1](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-1.zip)
- [Cas 2](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-2.zip)
- [Cas 3](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-3.zip)
- Bonus : [Cas 4](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-4.zip)

Pour récupérer depuis un environnement vscode :
```
curl --output exo3-1.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-1.zip
curl --output exo3-2.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-2.zip
curl --output exo3-3.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-3.zip
curl --output exo3-4.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-4.zip
### Aller plus loin

- Git LFS : référencer les fichiers lourds et non versionnables via des fichiers plus légers

## Gitflow : Feature branch

<img src="img/git-flow.png">

L'objectif du gitflow est de déterminer un mode de fonctionnement en projet, permettant de découper le travail en degré de maturité :

- Une version stable de l'application / qui peut tourner et est fonctionnelle (derniere version livrée)
- Une version en cours de l'application, qui peut tourner mais demande probablement un travail avant l'intégration ou attend que certaines fonctionnalités soient existantes
- Des versions temporaires de l'application, pour lesquelles des fonctionnalités sont en cours de développement : ex correction d'un bug ou ajout d'un endpoint

Pour cela il est nécessaire de s'intéresser aux branches.

### Branche

<img src="img/gitbranche.png">

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

Pour intégrer des changements issus des branches, une commande existe : **git merge**

Pour intégrer des changements de la branche nouvelle-branche

```
git merge nouvelle-branche
```

Pour aller plus loin : [conflits git](https://opensource.com/article/20/4/git-merge-conflict)

### Rebase

<img src="img/rebase-vs-merge.png">

Pour faire avancer une branche jusqu'a un autre commit (en y déplaçant les changements de l'histoire), vous pouvez réaliser une opération de rebase.

### Feature / stable branches

<img src="img/gitflowexample.jpg">
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

### Aller plus loin

- Petit guide de workflows classique de travail:
  https://gist.github.com/blackfalcon/8428401

## Ecosystème Git : issues, merge requests, forks

Un écosystème s'est construit autour de ces concepts, et certains outils/concepts sont apparus au sein des gestionnaires de version permettant une organisation plus macro.

### Glossaire

**issue**: déclaration d'un bug / d'une nouvelle fonctionnalité demandée : se fait par l'intermédiaire de petits tickets intégrés à Github ou Gitlab par exemple

**merge request/pull request**: création d'une demande d'intégration d'une branche (**merge**) pour y effectuer une/des review(s) et y proposer des corrections.

**fork**: copie d'un dépot git.
cas d'usage :

- contribution à un projet où l'on a pas les droits, pour travailler sur la copie et proposer les changements sur le projet (ex: correction bug, opensource, etc..)
- récupération d'un projet qui va passer dans le domaine privé par une personne ou une communauté (c'est pour cela qu'on parle souvent de fork)

### Exemple avec Gitlab

#### **Signaler un bug via issue**

<img src=img/gif-issue.gif>

#### **Workflow pull request / merge request**

<img src=img/pr.png>

#### **Cloner un projet via fork**

<img src=img/git-fork.gif>

### Exercice 6

Mise en contexte :
Vous désirez permettre a des utilisateurs de savoir l'heure qu'il est dans un pays, a partir de l'heure qu'il est au moment de leur demande. Deux collègues sont super emballés par le projet, et sont désireux de développer la solution qui s'en rapproche. Vous devez donc faire un choix.

1. Sur le dépot git que vous avez récupéré, vous trouverez une branche `exercice-6-develop`, déplacez vous y.
2. Forkez le dépot dans votre espace (sous votre nom).
3. Vous constatez qu'il y a 2 développeurs qui ont fait des développements : Roger Roger, et Adrien Délicat. Et une branche Hotfix, qui règle une erreur typographique. Mergez là.

```
git merge <branch>
```

4. Lisez le code des deux développeurs et proposer une merge request de leur code vers la branche `exercice-6-develop` puis choisissez quelle version est selon vous la plus appropriée pour un projet.
