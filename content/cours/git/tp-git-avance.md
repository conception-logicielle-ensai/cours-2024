+++
title = "TP Git avancé"
description = "TP git avancé"
date = 2024-01-15T00:00:10
short = true
aliases = ["git"]
header_img= "img/git33.svg"
+++

### Exercice 5

C'est votre premier jour de boulot ! A votre arrivée, on vous remet une clé USB contenant le code de l'application/des données.

Choisir, dans la liste ci-dessous, l'émoji le plus approprié à la situation :

- :pensive:
- :cry:
- :scream:
- :thumbsup:
- :thumbsdown:
- :runner:

Pour chacun des cas suivants, ajoutez (ou non) les fichiers a votre dépôt git dans un sous dossier **tmp** si ils sont valides selon les règles présentées dans la partie
- [Cas 1](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-1.zip)
- [Cas 2](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-2.zip)
- [Cas 3](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-3.zip)
-  [Cas 4](https://minio.lab.sspcloud.fr/conception-logicielle/exo3-4.zip)

Pour récupérer depuis un environnement vscode on peut utiliser le client HTTP en ligne de commande curl:
```
curl --output exo3-1.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-1.zip
curl --output exo3-2.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-2.zip
curl --output exo3-3.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-3.zip
curl --output exo3-4.zip https://minio.lab.sspcloud.fr/conception-logicielle/exo3-4.zip
```

### Exercice 5b

Dans votre dépôt, introduisez un fichier de configuration vous permettant d'ignorer la plupart des fichiers a ne pas versionner pour un projet python.

### Exercice 6

Mise en contexte :
Vous désirez permettre a des utilisateurs de variabiliser, dans un client dédié. Deux collègues sont super emballés par le projet, et sont désireux de développer la solution qui s'en rapproche. Vous devez donc faire un choix.

1. Forkez le dépôt https://github.com/conception-logicielle-ensai/TP1-git-avance
2. Sur le dépot git que vous avez ainsi construit, vous trouverez une branche `exercice-6-develop`, déplacez vous y.
3. Vous constatez qu'il y a 2 développeurs qui ont fait des développements : Roger Roger, et Adrien Délicat. Et une branche Hotfix, qui règle une erreur typographique. Mergez là.

```
git merge <branch>
```

4. Lisez le code des deux développeurs et proposer une `pull request` de leur code vers la branche `exercice-6-develop`.

Quel solution souhaiteriez vous voir intégrer ? Quels sont les points de blocage dans les 2 codes proposés?
