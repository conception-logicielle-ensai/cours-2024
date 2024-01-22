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


## Conteneurs : concepts clés
**Container runtime**

<img src="/img/conteneur-runtime.drawio.png"/>

- Hébergement  = OS + Un ensemble de processus
- Arrivée Namespace 2002: Isolation des processus (communication avec les autres process) + changement le propriétaire du process
- Arrivée des Cgroups 2006 : Restreindre l'accès a certaines ressource

> Container runtime : héberger un ensemble de processus indépendant isolés sur un OS.

**Image Docker**

![conteneur](/img/conteneur-image.drawio.png)



Une image est un paquet autonome contenant tout le nécessaire pour executer des applications. Une image est le patron utilisé pour créer des conteneurs.

- C'est un binaire qui comprend un ensemble de données.
- Il est construit en couches (layers) avec une relation entre chaque image de parent / enfant
- Partage d'image facilité : une image n'est qu'une feuille de l'arbre des images.
- Une image c'est un blueprint pour créer un environnement d'execution fonctionnel

**Conteneur**

![conteneur](/img/conteneur-environnement.drawio.png)

- La CLI demande le déploiement du conteneur
- Le registry cache va chercher l'ensemble des images nécéssaires à notre conteneur
- Le daemon démarre le conteneur avec l'ensemble des images récupérées
- Si besoin de volumes, modification des cgroups/namespaces

**Dockerfile**

![dockerfile](/img/dockfile.jpg)

Un fichier texte avec sa syntaxe propre permettant la constitution d'image docker. Il décrit l'ensemble des opérations (sur l'environnement de build).

Il regroupe la customisation de l'environnement de départ (**FROM**), et des paramètres de lancement. Par défaut il est d'usage de paramétrer l'**ENTRYPOINT** via le Dockerfile. Il définit la commande lancée au démarrage du container.


> Remarque : Dans le monde des conteneurs, tout est processus et un processus doit être pensé sans état interne.

## Constitution d'une image docker

Pour construire une image docker, il faut choisir a partir de quel base l'on souhaite construire l'image.

Puis l'on doit `tagger` l'image, en lui donnant une version. Exemple :

`docker build -t monimage:v1 .`

Cette commande permet de construire une image `monimage` taguée `v1` a partir d'un fichier Dockerfile présent à la racine.
