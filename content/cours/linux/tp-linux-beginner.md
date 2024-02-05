+++
title = "TP - Bonus découverte de linux"
description = "Explorer un OS linux et découvrir la ligne de commande"
date = 2024-02-05T00:00:12
short = true
aliases = ["git"]
header_img= "img/linux.svg"
+++

## Linux

### Principes de la ligne de commande

La ligne de commande (on parle aussi de terminal) est un environnement intéractif dans lequel vous pouvez exécuter des instructions et obtenir le résultat.  
Quelques informations / conseils avant de commencer :
* La touche `tab` de votre clavier va devenir votre meilleur allié. Cette touche permet d'autocompléter une commande à partir du contexte. N'hésitez pas à en abuser !
* Une commande accepte en général des paramètres (comme une fonction) ainsi que des options qui sont préfixées par `-` (pour les options raccourcies dont le nom tient en un caractère) ou `--` (pour les options de plusieurs caractères).
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
* `touch monfichier.ext` : créer un fichier vide (https://man7.org/linux/man-pages/man1/touch.1.html)

#### Exercice : petit tour du propriétaire

* La racine d'un système linux est `/`. Quels sont les dossiers présents à la racine du système ? Comparer la structure à https://www.linux.com/training-tutorials/linux-filesystem-explained/

<details><summary>aide</summary><p>

Vous pouvez vous déplacer a la racine du système avec la commande `cd`

```
cd /
```
Et observer les fichiers disponibles là ou on se trouve avec la commande `ls`

```
ls
```

<img src="https://lcom.static.linuxfound.org/sites/lcom/files/standard-unix-filesystem-hierarchy.png" />

Quelques dossiers exemple :
/bin : Là ou les commandes utilisateur sont installées
/home : l'espace utilisateur

</p></details>


### Lancement de programmes

Depuis un terminal, vous pouvez lancer une commande directement en tapant le nom du programme.  
Par exemple, si vous voulez appeler python et qu'il est installé, vous pouvez simplement taper `python` suivi des éventuels paramètres.

> Par défaut sur linux, en général python correspond a la version de python 2 (que l'on retrouve aussi en tapant python2), pour un python 3.X.X il faudra en général taper python3


### Note sur les permissions

Contrairement à d'autres sytèmes d'exploitation qui ne seront pas mentionnés ici, les systèmes Linux appliquent des politiques strictes de gestion des droits et permissions.

Un terminal est toujours ouvert en tant qu'un certain utilisateur.  
La commande `id` (https://man7.org/linux/man-pages/man1/id.1.html) permet d'avoir des informations sur l'utilisateur courant.

On obtient le numéro et le nom de l'utilisateur connécté ainsi que ses éventuels groupes.

> Il existe un super-utilisateur : `root` possédant l'id `0`.  
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

Nous vous proposons d'utiliser Terminus, ce jeu en ligne de commande est disponible sur :
https://luffah.xyz/bidules/Terminus/

L'objectif est de débloquer des commandes linux simples pour pouvoir les appliquer et finir le jeu.

> Vous êtes invités a essayer mais pas nécessairement à tout faire.

> Utilisez [TAB] pour voir le champ des possibles

<details><summary>Solution partie par partie</summary><p>

Vous disposez au départ des commandes :
- `cat` pour interagir avec les éléments
- `cd` pour vous déplacer d'un endroit a l'autre
- `ls` pour lister les éléments présents
<details><summary>Aide 1 : Premiers pas</summary><p>

- Vous pouvez aller apprendre dans le BoisDesLutins/AcadémieDesBots/Cours la commande `mv` pour déplacer des objets
- Vous pourrez donc déplacer le rocher qui se trouvera sur votre chemin dans
  `Prairie/Montagnes/Cave/SombreCorridor/Cellier/` vers le `Prairie/Montagnes/Cave/SombreCorridor/Cellier/PetitRenfoncement`

</p></details>

<details><summary>Aide 2 : Le village</summary><p>

> Bibliotheque
- Arrivés au village, vous êtes invités a aller dans la Bibliothèque pour en apprendre d'avantage, le livre ToutSurLesSorts vous indiquera comment activer l'IntrigantLevier.

- Ce levier donnera accès a une salle secrète, et un petit elfe nommé Grep vous donnera la commande `grep`, utile pour trouver une chaine de caractère dans un fichier. Le bibliothécaire vous donnera un indice pour la suite.

> Place du marché

- Le vendeur n'est pas très malin, il a laissé un sac plein d'argent, vous serez chatiés, mais au moins vous aurez appris des commandes nécessaires pour la suite :). Vous debloquez `rm` et `mkdir`.


> Boutique Artisanale


- vous allez ensuite devoir visiter la BoutiqueArtisanale, ou une artisante vous apprend a créer et copier des objets en tout genre.
- Pouvant donc créer tout type d'objets, vous devriez pouvoir passer sur le PontCassé/

</p></details>

<details><summary>Aide 3 : A la poursuite de Mandi</summary><p>

> CheminEnPierre
- Aidez le fermier qui se trouve de l'autre côté du pont de pierre, un rocher s'y trouve, vous pouvez vous en débarasser non ?


> PontCassé
- Vous allez vous retrouver face à un pont cassé, vous pouvez toujours construire une planche pour y passer. Détruisez les ronces qui bloquent le passage.
- Des trolls vous attendent, il faut vous débarasser de celui qui bloque le toboggan.
- Débloquez la commande sudo, dans le Prospectus, et lisez les Instructions.
- Ensuite vous allez devoir retrouver un mot de passe parmi tous les fichiers dispatchés dans "PlusDeFichiersNoyau"

> Paradis

Vous venez de vous bruler, et malgré le vol, vous avez un accès premium pour le paradis, allez-y et **profit**
</p></details>
</p></details>

### Pour aller plus loin : système de permissions des fichiers

https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/
