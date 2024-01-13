+++
title = "Introduction"
description = "Introduction du cours"
date = 2024-01-15T00:00:01
aliases = ["introduction"]
tags = ["introduction"]
short = true    
+++

# Conception logicielle

Ce cours traite de différents aspects de l'ingénierie du logicielle pour un public de développeurs et de statisticiens.

## Prérequis à installer

Les prérequis à installer sont listés dans la partie [mise en place](/about/mise-en-place/).

On la détaillera par la suite.

## Programme

Ce cours est divisé en différents chapitres :

- Git avancé, environnement de travail: rappels sur l'utilisation de Git, travail collaboratif, issues, merge / pull requests
- Portabilité, configuration, packaging : lancer du code sans IDE, comprendre l'environnement d'exécution, environnements virtuels et gestion de paquets.
- Tests, automatisation et initiation à l'intégration continue: tests unitaires, mocking, automatisation via script sur environnement linux, initiation au principe d'intégration continue
- Application webs et webservices : Présentation des différents enjeux, en tant que client et en tant que serveur.
- Architecture applicative avancée : Zoom sur des concepts plus avancés - ORM et différents types de bases de données, patrons de conceptions et prise de perspective avec la POO, introduction a la programmation fonctionnelle.

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
