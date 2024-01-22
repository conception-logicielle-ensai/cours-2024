+++
title = "Portabilité et configuration "
description = "Configuration externe d'un programme"
date = 2024-01-22T00:00:10
tags = ["","git","python"]
header_img= "/img/settings2.svg"
+++

Assez souvent, lorsque l'on execute un programme, on est amené a le configurer, paramétrer et éventuellement lui adosser des éléments qui dépendent de l'environnement d'où il est lancé.
En effet, qui ne s'est jamais retrouvé a devoir travailler sur des données qui se trouvent dans un repertoire quelque part, ou des paramètres de connexions a une base de données qu'on ne souhaite versionner et divulguer.

Fort heureusement, on peut injecter a un programme certaines variables qui seront ainsi utilisées dans le programme bien qu'étant de la configuration externe.

## Configuration externe d'un programme

Pour l'execution d'un programme, on est assez souvent amenés a externaliser la configuration :

- Dans le cas de l'accès a une ressource avec un mot de passe, vos mots de passe ne devant pas être versionnés.
- Ce qui dépend de l'environnement cible et qui semble configurable : une _URL de base de données_, un lien vers un jeu de données dans un datalake, un chemin de fichier vers un sous dossier externe a l'application, une règle de gestion comme un seuil d'erreur..

Cela s'effectue de plusieurs manières :

- Soit par la lecture de variables d'environnement.
- Soit par l'injection de paramètres au lancement d'un programme.
- Soit par l'ajout de fichiers de configuration dont l'emplacement est connu et attendu par le programme que l'on lance.


**Ce qui reste le plus préconisé, c'est l'utilisation de variable d'environnement dans l'applicatif (cf https://12factor.net)**

Toutefois, les différentes méthodes d'injection existent et sont plus ou moins maintenues selon le language.
### Configuration par fichier de configuration externe

Dans beaucoup de language, il y a un existant de configuration par fichier spécifique : config.toml / application.properties / config.json
En python, historiquement, on utilise des fichiers de configuration dans beaucoup d'endroits et assez souvent dans un format spécifique : le toml.

> Tom’s Obvious Minimal Language

Dans la librairie python de base, il y a le module `configparser` : https://docs.python.org/3/library/configparser.html

```
# config.ini
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[forge.example]
User = hg

[topsecret.server.example]
Port = 50022
ForwardX11 = no
```

Cela s'importe directement avec un parser de config : 

```python
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
```

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Feuilleter la documentation <a href="https://docs.python.org/3/library/configparser.html">https://docs.python.org/3/library/configparser.html</a>
</div>

> Globalement ce ne sera pas utilisé ni présenté plus ici, mais il faut savoir que cela existe dans tous les languages
### Configuration par arguments en ligne de commande

La plupart des programmes qu'ils soient des traitements instantanés ou des serveurs admettent des variables en ligne de commande.

L'on peut récupérer ses paramètres en python a l'aide de modules comme `sys`.

Par exemple si l'on prend le fichier main.py construit précédemment :
En y ajoutant :
```python
import sys
arguments = sys.argv
logging.basicConfig(filename=arguments[1], encoding='utf-8', level=logging.DEBUG)
```

Et en lançant la commande : 
`python main.py toto.log` on écrit la log dans le fichier de log toto.log

> Globalement ce ne sera pas utilisé ni présenté plus ici puisqu'on insistera surtout sur la configuration par variable d'environnement
### Configuration par variable d'environnement

L'injection par variable d'environnement est le cas le plus viable pour un code par une personne extérieure au projet.

En effet, il ne faut plus forcément connaître le formalisme d'injection et l'on peut simplement surcharger la configuration en renseignant des paramètres de type :
`CLE=valeur`

> NB: la notation des variables d'environnement se fait en upper_snakecase

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Variables d'environnement :  <a href="https://kinsta.com/knowledgebase/what-is-an-environment-variable/">https://kinsta.com/knowledgebase/what-is-an-environment-variable/</a>
</div>


Pour cela de nombreuses librairies existent dans tous les languages, en python nous utiliserons la librairie `python-dotenv` pour la lecture du fichier de configuration de l'application **.env** et l'export des variables dans l'environnement.

```
# Configuration des mots par défaut
CHEMIN_FICHIER_LOG=
ENVIRONNEMENT=local
```

> exemple d'un fichier .env

La librairie effectue un simple import du fichier .env dans les variables d'environnement.
```python
from dotenv import load_dotenv

load_dotenv() # Charge toutes les variables du fichier .env dans l'environnement
```


Les variables sont accessibles dans l'environnement, nous utiliserons pour cela la librairie `os` pour accéder a ces données.

On peut également le dispatcher sur différents fichiers, cela permet de ne pas versionner ces fichiers et de mettre des valeurs par défaut : 
```python
load_dotenv()
local_env_path = ".env.local"
if os.path.exists(local_env_path):
    load_dotenv(dotenv_path=local_env_path, override=True)
```
