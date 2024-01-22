+++
title = "TP Portabilité configuration : Mise en place"
description = "Mise en place de l'environnement pour le tp"
date = 2024-01-22T00:00:01
aliases = ["python","portabilite"]
header_img= "img/git-and-port.svg"
+++

## Exercice 1 : Git again ?

On devra utiliser pour toute la séance un dépôt git.
Donc soit vous: 
- Repartez du dépôt que vous avez constitué au TP précédent 
- Forkez le dépôt qui sera le dépôt du TP conception logicielle et récupérez le en local (en privé).

N'oubliez pas de le renseigner sur le google docs pour le suivi : https://docs.google.com/spreadsheets/d/1MoswP2Sojl36qDCTHssRbsIf824K1rdEDi18ZMUyr-M/edit#gid=0

Péreinisez votre version en réalisant un tag, soit via l'interface github (un clic) soit avec la commande `git tag`

Exemple : `git tag tp1` puis `git push origin tp1`

Cela permet d'indexer le commit pour pouvoir un jour revenir sur le projet a l'époque du tp1 avec la commande `git checkout tp1`.

## Exercice 2 : Hello world, all around the world

Exécuter, **en respectant l'ensemble des règles fixées dans la partie `Organisation de la séance`**, un code python qui récupère l'heure actuelle a la Réunion 🌋.


**RAPPEL DES REGLES**

- Un code n'est valide que s'il a été exécuté sur au moins 2 environnements différents.
- Tout le code doit être versionné en permanence sur `git`
- Pour transférer le code d'un environnement à l'autre, on passera par git (`git push` sur un des environnements et `git pull` sur les autres). **Tout transfert de code entre les plateformes en utilisant un autre outil (mail, copier / coller, recopie manuelle ...) doit être proscrit**
- Un code n'est valide que s'il est lançable depuis le terminal (donc sans utiliser les boutons de l'IDE).
- Un code n'est valide que s'il est lançable directement après un `git clone`, éventuellement avec une succession de commandes.
- Un code n'est valide que si la succession de commandes nécessaires au lancement est documentée dans un fichier `README.md` à la racine du projet.

