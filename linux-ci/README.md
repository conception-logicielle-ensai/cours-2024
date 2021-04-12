# Ligne de commande / Automatisation

## Objectif et organisation de la séance  

L'objectif de cette séance est de (re)découvrir l'automatisation en abordant 2 sujets importants :  
- Les systèmes linux et la ligne de commande  
- L'intégration continue (CI : Continuous Integration) : automatisation de tâches depuis un dépôt GIT  

Pour ces 2 chapitres, la phase de théorie sera réduite au minimum (objectif 15 minutes), une grande place sera laissée pour la **pratique en autonomie**

## Votre environnement de travail

Pour la première partie, il vous suffit d'avoir accès à un terminal sur un environnement linux.  
Vous pouvez par exemple utiliser :  

- Votre machine personnelle s'il s'agit d'un Linux ou un MacOS (les commandes sur un terminal MacOS sont très proches des commandes Linux). Si vous êtes sur Windows vous avez la possibilité d'installer une machine virtuelle ou d'utiliser WSL (Windows Subsystem for Linux). 
- Un environnement dans le SSPCloud : [Datalab](https://datalab.sspcloud.fr) ou [Che](https://che.lab.sspcloud.fr) (attention, Che ne fournit pas d'accès root / administrateur sur les environnements).
- [Katacoda](https://katacoda.com/scenario-examples/courses/environment-usages/ubuntu-2004) : un bac à sable dans un système Ubuntu (20.04).  

Pour la seconde partie, vous n'aurez besoin que d'un accès (et d'un compte) à [Gitlab](https://gitlab.com).  
Il est cependant conseillé d'être équipé d'un Visual Studio Code avec le plugin YAML (`redhat.vscode-yaml`) afin de bénéficier d'aide à l'écriture (autocomplétion, documentation) du code.

## Linux

### Principes de la ligne de commande  

La ligne de commande (on parle aussi de terminal) est un environnement intéractif dans lequel vous pouvez exécuter des instructions et obtenir le résultat.  
Quelques informations / conseils avant de commencer :  
* La touche `tab` de votre clavier va devenir votre meilleur allié. Cette touche permet d'autocompléter une commande à partir du contexte. N'hésitez pas à en abuser !  
* Un grand pouvoir implique de grandes responsabilités : les commandes que vous allez exécuter peuvent avoir un impact (limité par les droits que vous possédez sur la machine). Sur les sytèmes linux, à partir du moment où vous avez le droit de faire quelque chose, linux ne vous empêchera jamais de le faire. Bonne nouvelle pour vous si vous utilisez un environnement dans le cloud (`SSPCloud`, `Katacoda` ...), ces environnements sont en général très isolés et le casser n'a pas d'impact sur le reste, les autres utilisateurs ...  

Les 2 principaux types d'opérations réalisables dans un terminal sont :  
* Opérations sur les fichiers (lister, lire, supprimer, déplacer)  
* Lancement de programmes  

### Opérations sur les fichiers

* `ls` : lister les fichiers dans le dossier courant (https://man7.org/linux/man-pages/man1/ls.1.html)  
* `rm nomdufichier` : supprimer (ReMove) un fichier (https://man7.org/linux/man-pages/man1/rm.1.html)  
* `mv fichierdedepart fichierdarrivee` : déplacer (MoVe) un fichier (https://linux.die.net/man/1/mv)  
* `cp fichierdedepart fichierdarrivee` : copier (CoPy) un fichier (https://linux.die.net/man/1/cp)  
* `cd chemin` : changer (Change Directory) de dossier courant (https://linuxcommand.org/lc3_man_pages/cdh.html)  
* `pwd` : afficher le chemin du dossier courant (Print Working Directory) (https://linux.die.net/man/1/pwd)  
* `cat fichier` : lire contenu du fichier (https://man7.org/linux/man-pages/man1/cat.1.html)  
* `mkdir dossier` : créer un dossier (MaKe DIRectory) (https://man7.org/linux/man-pages/man1/mkdir.1.html)  

#### Exercice : petit tour du propriétaire  

* La racine d'un système linux est `/`. Quels sont les dossiers présents à la racine du système ?  

### Lancement de programmes

Depuis un terminal, vous pouvez lancer une commande directement en tapant le nom du programme.  
Par exemple, si vous voulez appeler python et qu'il est installé, vous pouvez simplement taper `python` suivi des éventuels paramètres.

### Note sur les permissions  

Contrairement à d'autres sytèmes d'exploitation qui ne seront pas mentionnés ici, les systèmes Linux appliquent des politiques stricts de gestion des droits et permissions.  

Un terminal est toujours ouvert en tant qu'un certain utilisateur.  
La commande `id` (https://man7.org/linux/man-pages/man1/id.1.html) permet d'avoir des informations sur l'utilisateur courant.  
On obtient le numéro et le nom de l'utilisateur connécté ainsi que ses éventuels groupes.  

Il existe un super-utilisateur : `root` possédant l'id `0`.  
Ce super-utilisateur possède tous les droits sur le système.  
**Il est vivement recommandé de ne pas utiliser le compte `root` au quotidien mais de ne l'utiliser qu'occasionnellement, lorsqu'on a besoin d'exécuter une commande avec des droits élevés.**
La commande `su nouvelutilisateur` permet de changer d'utilisateur actif, à partir du moment où l'on connait son mot de passe.  
La commande `sudo command` permet d'exécuter une unique commande en tant que `root`. https://xkcd.com/149/  

### Gestionnaire de paquet

Les distributions Linux contiennent en général un gestionnaire de paquets permettant d'installer (et mettre à jour / désinstaller) des nouvelles applications / commandes facilement  
Dans la suite, on va manipuler `apt` (aussi appelé `apt-get`) qui est le gestionnaire de paquets de `Debian` et de ses dérivés (Ubuntu, Linux mint ...)

Pour installer un paquet, il suffit d'appeler la commande `install` de `apt` :  
`apt install nomdupaquet`  

Il peut être nécessaire de d'abord mettre à jour la liste des paquets disponibles : `apt update`  

Note : l'utilisation d'`apt` requiert les droits super-utilisateur (root). Vous allez donc généralement préfixer la commande par `sudo`

#### Exercices : petites commandes entre amis

* Que fait `figlet hello` ?  
* Que fait `cmatrix` ?  
* Tester `telnet towel.blinkenlights.nl`

(Au besoin, installer les paquets nécessaires)

### Une mise en pratique ludique  

https://luffah.xyz/bidules/Terminus/

### Pour aller plus loin : système de permissions des fichiers 

https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/

## Intégration continue


![](https://i.imgur.com/Mkjq6jX.png =500x)

### Concepts 

Vous avez fait des commandes en terminal durant ce cours, l'idée c'est de généraliser ces commandes dans des scripts a executer souvent pour effectuer des vérifications.

Typiquement : 

Nous avions comme objectif de rendre le code le plus portable possible, c'est bien pour vos collègues mais aussi pour des petits automates qui vont pouvoir faire des vérifications au fur et a mesure de l'avancement du projet.

Et par vérifications on entend*: 
- le "Linting" à la main => Voir que le code respecte bien des règles établies.
- le testing 
     - Rappel tests unitaires : Vérifications des briques élémentaires du projet : ex la fonction ajoutMajuscule(mot) renvoie bien 'Conception' si on lui donne 'conception' en entrée.
     - *(pour aller plus loin)* Tests fonctionnels : Vérifications que les fonctionnalités au sens plus global fonctionnent : ex [Selenium](https://fr.wikipedia.org/wiki/Selenium_(informatique)#:~:text=Selenium%20est%20un%20framework%20de,un%20utilisateur%20de%20l'application.) [Cucumber](https://en.wikipedia.org/wiki/Cucumber_(software))

Puis pas forcément pour le python : 
- Le build : compilation du code et des dépendances en livrable.
- la release: mise a disposition d'un produit téléchargeable (bin/exe/tar.gz/zip)

*(Après récupération des dépendances projet et avec un environnement qui permet de faire tourner le code)

### Pratique

Pour cette partie vous aurez donc besoin d'un dépot git.

- Commencez par récupérer le dépot : https://gitlab.com/MDZP17/projet-pytest

- Puis créer votre dépôt et notifiez le :100: 

:warning: Les tests ont été effectués avec pytest, c'est une application pas trop complexe, donc ça devrait le faire.

- Ensuite, après l'avoir récupéré de votre côté, effectuez en ligne de commandes les operations nécessaires pour linter et tester depuis zéro l'application (notamment la partie pip)

**Rappel** linters d'exemple : autopep8, flake8, pylint

:bomb: - Ajouter la dépendance vers votre linter (flake8, autopep8,..) et faites une nouvelle version via git 

<details>(add,commit,push)</details>

<br/> 

- Puis lancez tests et linter


> Vous pouvez effectivement constater qu'il y a des erreurs dans les tests et potentiellement dans le lint : corrigez les

Sauvegarder les commandes sur le côté, rappelez vous juste de ce qu'il vous a fallu pour faire vos manipulations

<details><summary>Aide</summary>
<p>

- Un environnement avec python 3
- Installer les requirements : 
```
pip3 install -r requirements.txt
```
- Lancer le linting via ligne de commande (exemple pour flake8)
```
flake8
```
- Tester le code : 
```
pytest
```

=> Ce qui donnerait mis a la suite : 
:sunny: Environnement avec Python3 d'installé et script a passer : 
```
pip3 install -r requirements.txt
flake8
pytest
``` 
</p></details>


### Configuration de l'intégration continue sur Gitlab (gitlab-ci)

![](https://i.imgur.com/JEsaCtp.png)

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

Créez donc un tel fichier et copiez cet exemple sur votre dépot distant

:boom: Ajoutez donc tout cela a votre dépot git via un add/commit/push


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

:boom: Ajoutez donc tout cela a votre dépot git via un add/commit/push
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

<details><summary>semi-spoiler</summary>
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
    - apt update
    - apt install -y python3-pip
    - pip3 install -r requirements.txt
    - flake8
    
test-python-application:
    stage: test
    image: ubuntu:20.04
    script:
    - echo "hello-world"
```

</p></details>

:boom: Ajoutez donc tout cela a votre dépot git via un add/commit/push 
