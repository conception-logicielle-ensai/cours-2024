# Un peu plus loin

## Objectif et organisation de la séance  

L'objectif de cette séance est d'aller un peu plus loin en zoomant sur le protocole HTTP, en s'intéressant à la configuration d'une application et à sa publication.

## Votre environnement de travail

Pour ce chapitre, vous avez accès à un grand nombre d'environnements pour écrire, versionner et exécuter votre code. Les seuls prérequis sont d'avoir accès à `python`, `pip` et `git`.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle
- Un environnement dans le SSPCloud : [Datalab](https://datalab.sspcloud.fr) ou [Che](https://che.lab.sspcloud.fr).  
- [Katacoda](https://www.katacoda.com/courses/python/playground) : un bac à sable avec python préinstallé (attention, `python` correspond au binaire `python 2`, utilisez `python3` à la place)  

## Zoom sur HTTP  

### C'est quoi HTTP ?

HTTP ([Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)) est un protocole simple de communication client-serveur.  

![](https://formations.levitt.fr/univers-java/images/client-server.png)

On peut retenir les propriétés importantes suivantes :  
* Les échanges sont toujours à l'initiative du client  
* Le client fait une requête, le serveur répond à la requête  
* Client et serveur ne parlent jamais en même temps : le client parle puis écoute tandis que le serveur écoute puis parle
* HTTP est un protocole "déconnécté", chaque requête est indépendante  

### Pourquoi on vous en (re)parle

HTTP est le protocole le plus répandu. Sa simplicité en a fait un incontournable pour le partage de données, l'exposition de services et l'intéropérabilité.  
Vous serez amenés, dans votre carrière de statisticien ou d'informaticien, à manipuler quotidiennement HTTP que ça soit pour consommer des données / services (donc écrire un client HTTP) ou pour exposer vos données / modèles (donc écrire un serveur HTTP - un webservice -).

### Anatomie d'un échange HTTP  

Le client envoie une requête HTTP, le serveur répond.  

**Une requête**

* Première ligne  

```
GET /page.html HTTP/1.1
```  

Un verbe d'action (GET, POST, DELETE, PUT, HEAD, PATCH, OPTIONS, TRACE, CONNECT)  
La ressource demandée  
La version du protocole

* Headers

```
Host: example.com
Referer: http://example.com/
User-Agent: CERN-LineMode/2.15 libwww/2.17b3
Toto: tata
```

Liste de clés / valeurs **déclaratives** et **arbitraires**. [Certaines sont standardisées](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) mais rien n'empêche d'en ajouter.

* Body (contenu)  

Pour les requêtes POST / PATCH / PUT, il est possible d'ajouter un contenu à la requête. Par exemple, dans le cas d'une API de gestion d'utilisateurs, ajouter un utilisateur se fera souvent avec un body JSON :  

```
{
 "nom": "lebricoleur",
 "prenom": "bobette",
 "role": "admin"
}
```

Quelques exemples de requêtes complètes :  

```
GET /page.html HTTP/1.1
Host: example.com
Referer: http://example.com/
User-Agent: CERN-LineMode/2.15 libwww/2.17b3
```  

```
POST /user HTTP/1.1
Host: foo.example
Content-Type: application/json
Content-Length: 65

{
 "nom": "lebricoleur",
 "prenom": "bobette",
 "role": "admin"
}
```

**Une réponse**  

* Status line  

```
HTTP/1.1 404 Not Found
```  

Le protocole utilisé par la réponse  
Le code du statut HTTP (https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP)  
Le message correspondant au code HTTP  

* Headers  

```
Access-control-allow-headers: Content-Type, api_key, Authorization
Access-control-allow-methods: GET, POST, DELETE, PUT
Access-control-allow-origin: *
Content-type: application/json
Date: Mon, 03 May 2021 09:44:22 GMT
Server: Jetty(9.2.9.v20150224)
Bonjour: salut
```  

Même idée que les headers de la requête : liste de clés / valeurs **déclaratives** et **arbitraires**  

* Body (contenu)  

Le serveur peut renvoyer un contenu (ce n'est pas obligatoire) et ce contenu peut être de n'importe quel type (texte brut, HTML, JSON, image, pdf ...).  

```
[
 {
  "nom": "elgato",
  "prenom": "titi",
 }
]
```

### HTTP en action  

Il est temps de voir par vous même. Baladez vous sur internet comme vous le feriez normalement tout en gardant l'onglet `network` (réseau) des outils de développement (F12 en général) de votre navigateur ouvert.  
Regardez les différentes requêtes et réponses échangées par votre navigateur avec les différents serveurs.  

![](https://i.imgur.com/vzq2K7B.png)

### Aller plus loin  

Spécification HTTP : https://tools.ietf.org/html/rfc7231
HTTPS : comme HTTP mais avec une couche de confidentialité supplémentaire https://fr.wikipedia.org/wiki/HyperText_Transfer_Protocol_Secure

## Client / serveur HTTP  

![](https://i.imgur.com/0zyQpDw.png)


L'architecture client serveur est une architecture qui régit un grand nombre d'interactions sur des réseaux, .

L'objectif de cette partie est de s'approprier les outils pour comprendre et pouvoir interagir avec les services web, que ce soit directement ou via des clients divers.

Pour effectuer des requêtes http, il faut donc s'outiller en conséquence:
Typiquement:
- un navigateur web
- un client ([curl](https://curl.se/),[insomnia](https://insomnia.rest/products/insomnia),[postman](https://www.postman.com/))
- Directement via l'utilisation d'api (au sens d'interfaces fonctionnelles) dans le language de votre choix, et éventuellement avec des librairies tierces. 

### Client HTTP (CURL/Insomnia)


![](https://i.imgur.com/w9n0AUR.png)


- Curl est disponible https://curl.se/windows/ pour windows, disponible directement sur les autres plateformes linux
- Insomnia est disponible ici : https://insomnia.rest/products/insomnia

:open_book: **TP**
Installez un des deux clients, puis faites une requête GET sur l'api : https://randomfox.ca/floof/


### Mise en pratique python
L'idée de cette partie est donc de développer 2 applications:
- une première application étant un serveur web exposant des données
- une seconde application étant un client http python consommant ces données  

Côté python, de nombreuses librairies existent mais pour le coup, vous êtes invités a travailler avec *fastapi* et *requests*

- https://fastapi.tiangolo.com/
- https://docs.python-requests.org/en/master/

:open_book: **TP**


1. Commencez tout d'abord par créer deux dossiers 1 pour chaque projet du tp, créez un dépot gitlab associé
2. Ensuite créez un fichier main.py pour l'api contenant une api aux endpoints basiques:
    - Un endpoint sur ("/mots") acceptant des requêtes GET renvoyant tous les mots* disponibles sur le serveur
    - Un endpoint sur ("/mot") acceptant des requêtes POST permettant d'ajouter un mot*

*Un mot est un ensemble id, caracteres
```python=
class Mot(BaseModel):
    id:int
    caracteres:str
    def __init__(self,id,caracteres):
        self.id=id
        self.caracteres=caracteres
```

> Remarque la definition des types pour Pydantic et donc FastApi se fait via l'héritage de la classe BaseModel : https://pydantic-docs.helpmanual.io/usage/models/ . Cela vous permet de "Parser" vos objets pour les exposer via FastApi.


Exemple pour faire des endpoint avec request body avec fastapi : https://fastapi.tiangolo.com/tutorial/body/

3. Créez maintenant dans un autre dossier un fichier main.py, ici il sera question de faire un client HTTP pour ce serveur permettant : 
    - Créer une fonction get_mots() qui permet de récupérer tous les mots disponibles sur l'api
    - Créer une fonction add_mot(mot:Mot) qui permet d'ajouter un mot sur le serveur.

Documentation requests : https://docs.python-requests.org/en/master/user/quickstart/#more-complicated-post-requests


### Bonus: TP dans le TP

![](https://i.imgur.com/6HnO6g8.png)


L'idée ici est de mettre en place un webservice de pendu, webservice accessible via http sur les endpoints : 
- /init en GET permettant de récupérer le premier GUESS par le serveur
- /guess en POST pour tester un guess, la réponse permettant de continuer avec ce mot 
- /mots en GET voir plus haut
- /mot en POST pour ajouter un mot a la liste des mots proposable par l'application pendant que le serveur tourne (acceptant donc un Mot en Request Body)

Cela fait donc appel a 2 objets : 
```python=
class Mot(BaseModel):
    id:int
    caracteres:str
    def __init__(self,id,caracteres):
        self.id=id
        self.caracteres=caracteres
```

```python=
class Guess(BaseModel):
    mot:Mot
    erreurs:int
    letter:str
    def __init__(self,mot,erreurs,letter):
        self.mot=mot
        self.erreurs=erreurs
        self.letter=letter
```

Plus de précisions : 
- GET /init renvoie un random guess, avec un mot caché au sens que tous ses caractères sont cachés (par des '-'), mais que l'id est le même que le vrai mot
- POST /guess renvoie un Guess après avoir récupéré un Guess en entrée dans le request body : 
  - Soit il incrémente le nombre d'erreur de 1
  - Soit il remplace les - du mot correspondant a la lettre en entrée s'il y a correspondance

### Pour aller plus loin
- Créer un service qui répond a la place du serveur, et donc travailler avec un serveur pour les tests du client pendant le développement: https://www.mockapi.io/
- Mettre en place des tests qui fonctionnent si une partie du traitement dépend d'une ressource externe, concept de Mock : exemple avec unittest.mock
    - https://docs.python.org/3/library/unittest.mock.html
    - https://realpython.com/python-mock-library/
    
## Configuration  

![](https://i.imgur.com/TvvJSq0.jpg)


Dans un contexte d'usage plus large, il faut envisager ce qui est adhérent à l'environnement de ce qui ne l'est pas pour une meilleure portabilité.

Dans le cadre de ce tp, nous envisagerons l'utilisation de la librairie python https://pypi.org/project/python-dotenv/ pour répondre à ces besoins de configuration de l'environnement d'execution.

- Il est très envisageable que le client ne soit pas nécessairement sur la même machine que le serveur, par exemple si le serveur est déployé sur internet ou accessible

> Il faut donc envisager un paramétrage spécifique au projet client pour lui permettre d'accéder au serveur peu importe ce qu'il se passe

- Il est également classique que les données brutes utilisées par le serveur soient externalisées sur un autre serveur de stockage ou directement dans un espace de fichier local au serveur, il convient donc de paramétriser cela.


> Il faut donc envisager un paramétrage spécifique au serveur pour lui permettre d'accéder a des jeux de données de test par exemple en local, mais éventuellement des jeux de données massif pour un travail dans un environnement déporté (type cloud)


- mais également que l'on puisse définir des variables internes à la configurations des services : Nombre de requêtes max / taille de la réponse ...

> Là est encore une fois un bon usage, définir des paramétrages propres a l'environnement pour par exemple pouvoir répondre a des besoins d'usage variés et donc contribuer a une bonne portabilité du code (typiquement pour de l'Opensource)


lien : https://12factor.net/config

=> L'idée est donc de configurer tout ce qui est adhérent de l'environnement (notamment du déploiement) dans des variables d'environnement et dans des fichiers a configurer et a importer dans les différents fichiers python

Typiquement on créer un fichier .env qui contient la liste des variables paramétrisées par l'environnement:

```bash=
cat .env
> API_URL=https://entreprise.data.gouv.fr/api/sirene/v3/
> API_TOKEN=eyJhbGciOiJIUazeÃ©&zI1NiIsInR5cXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
:open_book: **TP**
1. Pour le client python, ajoutez dans la configuration un fichier .env
```bash=
# Development settings
SERVER_URL=http://localhost:8000
```
Puis importez cette variable via dotenv GETTING STARTED : https://pypi.org/project/python-dotenv/

Utilisez là pour la configuration des requêtes effectuées via requests.

2. Pour le serveur python : configurez l'utilisation de variables initiales via un json

=> Créez un fichier dev_data.json contenant : 
```json=
[
  {
    "id": 0,
    "ingredients": "conception"
  },
  {
    "id": 1,
    "ingredients": "logicielle"
  },
  {
    "id": 2,
    "ingredients": "ensai"
  }
]

```

3. Ensuite importer ce jeu de données comme une liste de Mot, et assurez vous que cela fonctionne.

> Dans des environnements différents, les applicatifs peuvent être amenés a travailler avec différents jeux de données, l'idée étant donc de paramétriser tout cela.

4. Créez donc un fichier .env qui donne l'endroit ou se trouve le fichier pour le serveur, la paramétrisation du port est également très classique.
```bash=
# Development settings
STARTUP_DATA=dev_data.json
TARGET_PORT=8000
```
Puis importez ces variable via dotenv pour paramétrer le port de l'application et le jeu de données de startup

5. Testez en téléchargeant : https://minio.lab.sspcloud.fr/conception-logicielle/lorem-ipsum_mots.json,

Et en faisant tourner votre serveur avec le fichier de configuration .env : 
```bash=
# Development settings
STARTUP_DATA=lorem-ipsum_mots.json
TARGET_PORT=8001
```

6. Aller plus loin : Industrialisation

https://medium.com/bcggamma/data-science-python-best-practices-fdb16fdedf82



## Packaging pypi

![](https://i.imgur.com/CFtnwaO.png)


Aller plus loin : https://packaging.python.org/tutorials/packaging-projects/
