+++
title = "Portabilité et configuration : conteneurisation "
description = "Construction d'un livrable unique"
date = 2024-01-22T00:00:15
tags = ["","git","python"]
header_img= "/img/Docker_(container_engine)_logo.svg"
+++

## L'arrivée de docker

Avec l'arrivée de l'isolation des processus, qui permet donc de contrôler les interactions entre les différentes tâches du système. (2006) 

On a pu changer d'approche sur le mode de livraison pour les traitements et applications en livrant des boîtes qui sont isolées du reste du système où elles sont hébergées et qui réalisent des traitements.

L'idée est donc pour un traitement en python de constituer des livrables qui contiennent a la fois le code applicatif, mais également les librairies python et éventuellement des paquets propres a un système d'exploitation (ex : ubuntu).

On appelle un tel livrable une `image docker`. C'est un énorme zip qui contient tout ce qui permet a votre application de se lancer. Ainsi la question de la portabilité est par design simplifiée puisque si ce paquet isolé tourne sur votre machine, il tournera sur la machine d'un autre.

## Image docker et Dockerfile

Regardez donc un fichier de configuration pour un environnement :

```Dockerfile
# On part d'un environnement ubuntu 22.04, connu.
FROM ubuntu:22.04
# on installe python comme sur un ubuntu
RUN apt-get update && apt-get install -y python3-pip
# On copie les fichier de notre projet dans le zip
COPY . .
# On installe les dépendances du fichier requirements.txt qui est dans notre projet dans l'image
RUN pip install -r requirements.txt
# On lance notre application
CMD ["python","main.py"]
```

## Daemon et ligne de commande
