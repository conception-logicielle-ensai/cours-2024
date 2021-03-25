# Conception logicielle

Ce cours traite de différents aspects de l'ingénierie du logicielle pour un public de développeurs et de statisticiens.

## Prérequis à installer

Les prérequis à installer sont listés dans le fichier [SETUP.md](SETUP.md).  
Il est demandé de le suivre avant le premier cours.

## Programme

Ce cours est divisé en 6 chapitres :

- [Git avancé](git/README.md) : rappels sur l'utilisation de git, travail collaboratif, issues, merge / pull requests
- [Portabilité](portabilite/README.md) : lancer du code sans IDE, comprendre l'environnement d'exécution, mise en place d'un serveur web
- Reproductibilité / portabilité : gestion des dépendances, externalisation de la configuration
- Introduction aux systèmes Linux : prise en main d'un terminal, commandes classiques
- Intégration continue : automatisation du build, testing, publication de package
- Déploiement : combinaison des chapitres précédents pour aller jusqu'à la mise en production d'une application

## Langage

Ce cours se veut agnostique du langage en illustrant principalement les concepts communs à la plupart des langages. Les mises en pratique seront principalement en `Python` mais des parallèles avec d'autres langages seront faits tout au long du cours.  
Les étudiants sont invités à essayer d'autres langages.

## Approche pédagogique

Ce cours met l'accent sur l'ingénierie de développement pour amèner les étudiants à prendre du recul sur l'écriture mais surtout sur la vie d'un code. Il n'y aura donc que très très peu de code écrit.

> L'important ce n'est pas de savoir quoi écrire mais où l'écrire.

## Fil rouge

Le fil rouge proposé est la réalisation d'un webservice de classification de produits.  
Le périmètre est volontairement très réduit afin de se concentrer sur l'ingénierie de développement.  
Les fragments de code nécessaires à la réalisation de l'application seront fournis (il est évidemment possible d'en dévier autant que vous voulez).  
L'objectif du fil rouge est le suivant :

```
Publier, sur un dépôt public, le code source d'un webservice de classification de produits.
Diffuser publiquement un livrable de l'application, construit automatiquement à partir des sources.
Le livrable devra pouvoir être utilisé tel quel sur différents environnements et configurable pour choisir le modèle et d'autres paramètres.
```
