+++
title = "Introduction"
description = "Section sur le contour du cours"
date = "2023-12-30"
aliases = ["about-us", "about-hugo", "contact"]
tags = ["introduction"]
+++

# Conception logicielle

Ce cours traite de différents aspects de l'ingénierie du logicielle pour un public de développeurs et de statisticiens.

## Prérequis à installer

Les prérequis à installer sont listés dans le fichier [SETUP.md](about/prerequis.md).  
Il est demandé de le suivre avant le premier cours.

## Programme

Ce cours est divisé en différents chapitres :

- [Git avancé, environnement de travail](cours/git/README.md) : rappels sur l'utilisation de git, travail collaboratif, issues, merge / pull requests
- [Portabilité, configuration](../cours/portabilite-configuration/README.md) : lancer du code sans IDE, comprendre l'environnement d'exécution
- [Etude de cas](../cours/etude-de-cas/README.md) : étude de cas d'une application sous différents aspects (code, architecture, reproductibilité ...)
- [Tests, automatisation et initiation à l'intégration continue](../cours/refactoring-testing-ci/README.md) : tests unitaires, automatisation via script sur environnement linux, initiation au principe d'intégration continue
- [Consolidation](../cours/consolidation/README.md) : TP de consolidation reprenant tous les concepts précédents
- [Plus loin](plusloin/README.md) : Zoom sur des concepts plus avancés.

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
