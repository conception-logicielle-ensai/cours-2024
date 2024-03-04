+++
title = "Sujets de projet"
description = "Section sur les sujets proposés pour le cours de conception logicielle"
date = 2024-03-04T00:00:00
aliases = ["cours"]
tags = ["projets","git","python"]
header_img= "img/sujets.svg"
+++

Cette rubrique contient les sujets proposés pour la session 2024 du cours de conception logicielle.

## Sujet 1 : Génération de cartes pour un jeu de société quizz musical

<img src="https://cf.geekdo-images.com/R4aQbIo0KZ6npxfhUc7ZYw__itemrep/img/HrmPHltfGRp2SsKiE8fYkA6uKQ8=/fit-in/246x300/filters:strip_icc()/pic6958739.png"/>

Ce sujet est proposé par rapport au jeu : `Hister` - [https://hitstergame.com](https://hitstergame.com)
### Concept

Hitster est un jeu de quizz musical dans lequel on doit retrouver le titre et l'artiste de différents titres `populaires` de différentes époques.

Il faut ensuite ordonner les titres ainsi retrouvés dans l'ordre chronologique a la manière d'un jeu `timeline`.

Pour fonctionner le jeu est constitué de cartes qui sur une face ont un `QRCODE` contenant un lien vers un extrait audio disponible sur spotify et sur le côté face la réponse soit : une année, un artiste et le nom du titre.

Nous souhaitons constituer notre propre jeu `hitster` puisque le jeu de base est assez limité en cartes.

### Implémentation

Pour cela nous allons nous appuyer sur l'API spotify (vous pouvez également vous appuyer sur l'API deezer ou autre..). 

Pour constituer la playlist attendue en sortie du traitement nous allons extraire depuis wikipedia :

- [https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France](Liste des single numero un en france dans le top 50 depuis 1984)

De cette playlist, on souhaitera, pour chaque `titre` récupérer la date et lancer une recherche spotify pour y récupérer l'extrait audio.

Enfin on souhaitera générer pour chaque extrait un fichier pdf contenant le qrcode qui est un lien vers l'extrait et de l'autre côté les informations suivantes : artiste, nom du titre et date de l'oeuvre.

L'application pourra donc, a partir d'un jeton d'api spotify / deezer .. Générer un ensemble de fichiers prêts a imprimer pour jouer.

## Sujet 2 :  Un jeu de carte en ligne - Texas Hold Em Poker : Client / Serveur

Le principe de ce sujet est d'implémenter un jeu de poker bien connu : le texas hold'em - <a href="https://en.wikipedia.org/wiki/Texas_hold_%27em"> https://en.wikipedia.org/wiki/Texas_hold_%27em </a>
<img src="/img/texas.png"/>
Le principe de ce projet repose sur l'utilisation de l'api documentée ici:
https://deckofcardsapi.com/
Cette API met a disposition des decks de 52 de cartes classiques. Elle propose également de nombreuses opérations détaillées dans la documentation.

Cela permet de ne pas avoir a redévelopper toute la logique de tirage de cartes et de distribution.

> Pour pimenter votre application vous pouvez bien évidemment utiliser plusieurs paquets, les mélanger les remettre a zéro comme vous le souhaitez
## Concept

Le Texas Hold em est une variante du poker très populaire et vous souhaitez en implémenter un jeu.

A partir d'un tirage de 2 cartes, chaque **joueur** décide ou non de s'engager dans la manche en misant des jetons. 

Au cours d'une manche, chaque joueur peut miser

Il existe 5 manches de mise en suite, avec la révelation de cartes supplémentaires (et la destruction): 
- 1 manche après la distribution des 2 cartes propres a chaque joueur.
> Puis distribution de 3 cartes communes a chaque joueur (**flop**)
- 1 manche de mise
> Puis distribution d'1 carte avant la manche suivante (**river**)
- 1 manche de mise
> Puis distribution d'1 carte avant la derniere phase d'enchère (**turn**)
- 1 manche de mise
> Révélation des cartes des joueurs restant et attribution des jetons.

Pour chaque manche, il faut que les joueurs (qui sont encore en lice) misent, suivent, `check`si il n'y a pas de mise ou quittent la table

A la fin de la dernière manche on révèle les cartes des joueurs

Les joueurs seront sauvegardés avec leurs jetons, parties en cours,  dans la base de données. 
Les parties permettent de retrouver les jetons de chaque joueur dans la partie et les différentes mènes.
Les mênes contiennent les cartes.
Les cartes contiennent des valeur, couleur, joueur et une référence a la mêne

### Technique

- Ce sujet est plus classique mais il est pertinent d'expérimenter avec SQLAlchemy / Django les différents types de drivers de base de données. En effet, il est plus pratique de travailler avec une base de donnée locale simple `type SQLite`.

> Remarque: il est attendu que suite a la documentation pour démarrer l'application, la base de données soit prête a l'utilisation (donc script sql ou commandes spécifiques attendues)

- Il est proposé deux architectures cible : soit une application web (site web avec backend intégré) donc en utilisant django. Soit une application client serveur avec une API pour gérer le jeu et l'état du jeu et la création d'un client (soit un client ligne de commande (que vous connaissez), soit un site web, soit un client python ex `tkinter`)

### Attendus de test

Il est ici attendu de tester différentes mains face a d'autres mains et de s'assurer que la règle de calcul pour la victoire est bien vérifiée.

## Sujet 3 : Webservice de génération de données de test

<img src="/img/data-generato.png"/>

Dans le cadre de la réalisation de tests de programmes, on est souvent amenés a utiliser des jeux de données fictives.  

Jsongenerator.io est un site qui permet la génération de données avec des formats de données de manière assez rapide : <a href="https://www.jsongenerator.io/">https://www.jsongenerator.io/</a>

### Concept

Pour répondre à ce besoin, vous envisagez de constituer un produit qui permet de générer des données de tests pour des statisticiens et développeurs en herbe.

Les utilisateurs de cette API pourront renseigner des types de données pour la génération à partir d'un language dédié : 
Par exemple :
- définir un type SEXE qui ne prendrait que les valeurs M,F ou A

```json 
"SEXE":"'M'|'F'|'A'"
```


- ou définir un type composé VOITURE qui prendrait les valeurs composées : 
```json
{
    "VOITURE": {
	"nb_roues": "INT",
	"COULEUR": "'rouge'|'vert'|'bleu'"
    }
}
```

Les utilisateurs de l'application définiront ensuite des schémas de données permettant de gérer les métadonnées nécessaires à la génération de données. Ces informations seront stockées en base de données.

Par exemple : 
```json
{
	"sexe": {
		"type": "SEXE",
		"remplissage": 100
	},
	"age": {
		"type": "18|19|20",
		"remplissage": 100
	},
	"prenom": {
		"type": "NAME",
		"remplissage": 88.4
	},
	"nom": {
		"type": "NAME|'dupont'"
		"remplissage": 85
	}
}
```
On pourra créer une configuration par requête `POST` sur le endpoint : `/generator/`. Cette requête sauvegardera la configuration en base de données et renverra l'identifiant du generateur crée pour l'utilisation.

On pourra récupérer la liste des générateurs par requête `GET` sur le endpoint : `/generator/`.

La génération de vos données se fera sur un endpoint accessible par requête HTTP `GET` :
> Par défaut `/generate/{generator_id}`

La génération fera donc ici par exemple pour 2 entrées : 
```json
{
  "data": [
    {
      "sexe":"M",
      "prenom":"jean",
      "nom":"dupont",
      "age":18
    },
    {
      "sexe":"F",
      "prenom":null,
      "nom":"Roger",
      "age":19
    }
  ]
}
```
Cette requête de generation sera paramétrable avec un paramètre `limit` qui par défaut sera a 5. 

**REMARQUE** : Cela reste votre projet, vous pouvez tout a fait proposer une autre implémentation des jsons.

### Technique

- Le point d'entrée et port de votre API doivent être customisable par des variables d'environnement, cela permet ainsi d'adapter en fonction de l'api que l'on souhaite reproduire.
- Votre application devra renvoyer un JSON valide.
- Aucun traitement des corrélations n'est demandé pour la réalisation.

### Attendus de test
Tester a partir d'un schéma défini programmatiquement, la bonne génération d'un jeu de donnée avec une graine fixée.

## Sujet 4 : Votre Projet ?

Vous pouvez également proposer un projet qui vous tient a coeur : 
- une automatisation qui pourrait être utile a votre vie : ex une Application pour réserver des cours ou des billeteries. Une application de suivi des prix ? 🐀
- un projet utile pour l'école : Une application de reservation de jeu de société pour le club ludik ? Une application pour réserver la salle de musique? Une application "buzzer" pour vos BDE ? (et pour découvrir les websocket?)

### Attendus de test

Tester les fonctionnalités `coeur de métier`: 
> Exemples: est ce que si j'ai déjà un formulaire récupéré de cette forme alors j'arrive bien a le renseigner avec mon programme.