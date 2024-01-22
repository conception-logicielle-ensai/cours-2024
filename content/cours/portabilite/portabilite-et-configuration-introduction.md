+++
title = "Portabilité et configuration"
description = "Mise en place"
date = 2024-01-22T00:00:00
tags = ["git","python"]
header_img= "img/port-init.svg"
+++
# Portabilité et Configuration : Introduction

## Approche pédagogique

L'objectif de cette séance est double : il s'agit d'abord de vous sensibiliser à la question de la portabilité des applications et du code puis d'aller plus loin dans l'écriture de code python en développant une application de type "microservice" .

## Votre environnement de travail

Pour ce chapitre, vous avez accès à un grand nombre d'environnements pour exécuter votre code. Le seul prérequis est d'avoir accès à `python` ainsi qu'à `pip`.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle
- Un environnement dans le SSPCloud : Vous avec aussi toujours accès au [Datalab](https://datalab.sspcloud.fr). Le compte à utiliser est le même que celui de la séance précédente : obviously.
## Organisation de la séance

Cette séance est construite sur un rythme cours / TP. Vous êtes toutefois libre d'avancer seul sur les différentes parties.

N'hésitez pas à communiquer sur votre avancement (au travers du lien ici : [LIEN GOOGLE DOCS](https://docs.google.com/spreadsheets/d/1MoswP2Sojl36qDCTHssRbsIf824K1rdEDi18ZMUyr-M/edit?usp=sharing) )
et à partager vos questions / problèmes / réussites.

**En lien avec l'objectif de portabilité des applications illustré par cette séance, on se fixe plusieurs règles pour cette séance (règles généralisables à la vie en général)** :

- Un code n'est valide que s'il a été exécuté sur au moins 2 environnements différents.
- Tout le code doit être versionné en permanence sur `git`
- Pour transférer le code d'un environnement à l'autre, on passera par git (`git push` sur un des environnements et `git pull` sur les autres). **Tout transfert de code entre les plateformes en utilisant un autre outil (mail, copier / coller, recopie manuelle ...) doit être proscrit**
- Un code n'est valide que s'il est lançable depuis le terminal (donc sans utiliser les boutons de l'IDE).
- Un code n'est valide que s'il est lançable directement après un `git clone`, éventuellement avec une succession de commandes.
- Un code n'est valide que si la succession de commandes nécessaires au lancement est documentée dans un fichier `README.md` à la racine du projet.


<div class="alert alert-warning">
  <strong>Remarque</strong> <br/> Cela sera la règle pour l'évaluation de vos projets donc veuillez respecter ces principes.
</div>

