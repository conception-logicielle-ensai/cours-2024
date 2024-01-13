+++
title = "Git avancé : dépôt distant"
description = "Git sur dépôt distant"
date = 2024-01-15T00:00:07
short = true
aliases = ["git"]
header_img= "img/git2.svg"
+++

## Git, gitlab, github ...

<img src="/img/git-gitlab-github-bitbucket.jpeg">

Avec la réussite de Git, des outils appelées Forges Logicielles sont apparues. Elles permettent de proposer l'hébergement du code source d'application publiques et privées de manière gratuite et offrent d'autres services de gestion ainsi que des interfaces clients appréciables.

On distingue 2 catégories de forges : les forges "As A Service" qui sont mises à disposition par des entreprises tierces et dont les données sont hébergées chez ces fournisseurs et les forges "On premise" qui sont hébergées directement dans les organisations qui les utilisent.

Exemples de forges "As A Service" :

- [Github.com](https://github.com) est un des leaders du marché, hébergeant une grande partie du code open source et des grands projets ouverts. Github a été racheté par Microsoft en 2018 pour 7.5 milliards de dollars. Le code source de github n'est pas public.
- [Gitlab.com](https://gitlab.com) est un concurrent très actif. Le code qui sous-tend gitlab.com est en très grande partie libre : https://gitlab.com/gitlab-org/gitlab
  Important : `gitlab.com` est une installation particulière du logiciel gitlab sur les serveurs de l'entreprise gitlab. Vous rencontrerez, dans votre carrière, d'autres installations du logiciel gitlab sur d'autres serveurs (cf "On premise"). Attention donc à ne pas confondre le service `gitlab.com`, le logiciel gitlab et les différentes installations de gitlab que vous rencontrerez.
- [Bitbucket.org](https://bitbucket.org/) : moins utilisé, il appartient à Atlassian (connu pour son outil de gestion de projet / ticket `Jira`)

Exemples de forges "On premise" :

- [Gitlab sspcloud](https://git.lab.sspcloud.fr)
- [Gitlab INSEE](https://gitlab.insee.fr) : accessible uniquement depuis le réseau INSEE
- [FramaGIT](https://framagit.org/explore/projects)

De nos jours, la plupart des forges "on premise" sont des installations du logiciel gitlab mais il existe des alternatives. Citons par exemple https://gogs.io/ et https://fusionforge.org/

### Dépôts centraux

<img src="/img/basic-remote-workflow.png" width="100%">

Les dépôt centraux se présentent comme des dépôt locaux hébergés sur des serveurs distants.

Il s'agit là de versions "canoniques" qui peuvent être récupérées par des développeurs habilités, ou par tout le monde. On parle alors de dépôt public (et non pas forcément d'opensource).

On peut intéragir avec eux a l'aide de commandes dédiées qui permettent de mettre a jour un dépôt, local ou distant, par rapport a un autre.



### Récupération d'un projet

<img src="/img/pull.png" width="100%">

Votre projet local peut être rattaché a un projet distant, vous pouvez interagir en ce sens par la commande **git remote**

```git
git remote -v
git remote add origin <https://url-du-projet>
```

Si vous voulez simplement récupérer un projet hébergé sur un dépôt distant.

```git
git clone <https://url-du-projet>
```


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Authentification : ssh/https -  <a href="https://gist.github.com/Ragatzino/791caa39f7522dc3001ba3b24372507c">https://gist.github.com/Ragatzino/791caa39f7522dc3001ba3b24372507c</a>
</div>


### Travailler a distance

<img src="/img/ez-pull-push.png">

#### **Récuperer des changements**

Pour récupérer les changements effectués sur le dépôt la commande la plus utilisée est :

```
git pull
```

Elle permet de récupérer les changements (commit) et de les ajouter a la copie de travail en local

> Remarque : c'est une opération que l'on effectue souvent avant de vouloir ajouter notre code pour qu'il n'y ait pas de fichiers dont git ne saurait pas quel version prendre


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Récuperer des changements sans les intégrer : <a href="https://www.atlassian.com/git/tutorials/syncing/git-fetch">https://www.atlassian.com/git/tutorials/syncing/git-fetch</a>
</div>



#### **Envoyer des changements**

Pour envoyer vos changements sur un dépot déclaré en remote, on utilise la commande **git push**:

_Cas d'usages classiques_

```bash
# envoyer vos changements (commits) à votre origin
git push
# envoyer votre code a votre origin et déclarer une branche origin/branch
git push --set-upstream origin branch
# envoyer votre code (commits) a votre origin en pushant la branche master
git push -u origin master
```


