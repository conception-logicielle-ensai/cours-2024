+++
title = "Automatisation"
description = "Cours sur l'automatisation des tests et contrôles sur une base de code"
date = 2024-02-05T00:00:05
tags = ["tox","python","gh-actions","ci-cd"]
header_img= "img/automate.svg"
+++

Maintenant qu'on a vu quelques outils, il s'avère pertinent de les lancer le plus souvent possible sur notre code source, et de manière simplifiée.

Pour cela on va voir un exemple d'outils actuels qui nous permettent d'automatiser la chaine de tests et de qualité de nos développement.


## L'intégration Continue et Déploiement Continu : CI / CD

Vous avez fait des commandes en terminal durant ce cours, l'idée c'est de généraliser ces commandes dans des scripts à executer souvent pour effectuer des vérifications.

Typiquement : 

Nous avions comme objectif de rendre le code le plus portable possible, c'est bien pour vos collègues mais aussi pour des petits automates qui vont pouvoir faire des vérifications au fur et a mesure de l'avancement du projet.

Et par vérifications on entend (*) : 
- le "Linting" à la main => Voir que le code respecte bien des règles établies.
- le testing (ce qu'on a fait précédemment)

*Puis pas forcément pour le python :* 
- Le build : compilation du code et des dépendances en livrable.
- la release: mise a disposition d'un produit téléchargeable (bin/exe/tar.gz/zip/image docker)

(*) : Après récupération des dépendances projet et avec un environnement qui permet de faire tourner le code



### Cas de github : Github Actions 


<div class="alert alert-info">
  <strong> Pour aller plus loin</strong> <br/> Un manager d'environnement virtuel pour les tests et l'installation : tox
</div>
 