# Portabilité

## Approche pédagogique

L'objectif de cette séance est double : il s'agit d'abord de vous sensibiliser à la question de la portabilité des applications et du code puis d'aller plus loin dans l'écriture de code python en développant un premier webservice.

## Votre environnement de travail

Pour ce chapitre, vous avez accès à un grand nombre d'environnements pour exécuter votre code. Le seul prérequis est d'avoir accès à `python` ainsi qu'à `pip`.

Quelques exemples d'environnements pouvant être utilisés :

- Votre machine personnelle
- Un environnement dans le SSPCloud : profitez en pour tester `Che` : https://che.lab.sspcloud.fr/ , une installation du logiciel opensource [Eclipse Che](https://github.com/eclipse/che). Vous avec aussi toujours accès au [Datalab](https://datalab.sspcloud.fr). Le compte à utiliser est le même.
- [Katacoda](https://www.katacoda.com/courses/python/playground) : un bac à sable avec python préinstallé (attention, `python` correspond au binaire `python 2`, utilisez `python3` à la place)

## Organisation de la séance

Cette séance va être beaucoup plus orientée TP que la séance précédente. Vous êtes libres d'avancer à votre rythme, en autonomie. N'hésitez pas à communiquer sur votre avancement et à partager vos questions / problèmes / réussites.

**En lien avec l'objectif de portabilité des applications illustré par cette séance, on se fixe plusieurs règles pour cette séance (règles généralisables à la vie en général)** :

- Un code n'est valide que s'il a été exécuté sur au moins 3 environnements différents.
- Tout le code doit être versionné en permanence sur `git`
- Pour transférer le code d'un environnement à l'autre, on passera par git (`git push` sur un des environnements et `git pull` sur les autres). **Tout transfert de code entre les plateformes en utilisant un autre outil (mail, copier / coller, recopie manuelle ...) doit être proscrit**
- Un code n'est valide que s'il est lançable depuis le terminal (donc sans utiliser les boutons de l'IDE).
- Un code n'est valide que s'il est lançable directement après un `git clone`, éventuellement avec une succession de commandes.
- Un code n'est valide que si la succession de commandes nécessaires au lancement est documentée dans un fichier `README.md` à la racine du projet.

## Runtime

Python appartient à la catégorie des langages interprétés (tout comme Javascript et R, par exemple).  
Un langage interprété possède un interpréteur (on parle aussi de `runtime`)
Pour exécuter un code d'un langage interprété, il faut 2 choses :

- Le code source à exécuter
- Un interpréteur (on parle aussi de `runtime`). Pour python, il s'agit de la commande `python` (`python3` sur certains systèmes pour le distinguer de python 2, `python.exe` sur certains systèmes d'exploitation inférieurs)

Pour vérifier que l'interpréteur `python` est bien disponible sur le système, on peut lancer la commande

```
python --version
```

Sidequest : si vous vous demandez où `python` est installé, vous pouvez utiliser la commande `which` (ou `where` pour les systèmes Windows)

> Source + Runtime = chocapics

Il est maintenant temps de lancer notre programme python :

```
python main.py
```

## Exercice 1 - Hello all around the world

Exécuter, **en respectant l'ensemble des règles fixées dans la partie `Organisation de la séance`**, un code python affichant `Hello world`.

## Exercice 2 - Ajout de dépendance

<img src="img/package.jpg"/>

Une dépendance est un module, disposant de fonctions développées dans d'autres projets.

> Vous connaissez probablement les dépendances : psycopg2, requests.

Les dépendances elles même peuvent avoir des dépendances, ce qui peut devenir pénible pour l'import a la main.

### Qu'est ce que pip

**pip** c'est un gestionnaire de paquets pour python

C'est l'installer de premier choix quand il s'agit d'ajouter des dépendances à un projet python.

- Maven/Gradle pour Java
- Npm/Yarn pour Javascript
- ...

### Qu'est ce qu'un gestionnaire de paquets

Lorsque vous voulez travailler avec des fichiers informatiques, les gestionnaires de paquets sont là pour vous.

Ils permettent :

- d'installer/mettre à jour/désinstaller des logiciels/outils/code

<a href="https://pip.pypa.io/en/stable/reference/pip_install/">

```
pip install <package>
```

</a>

<a href="https://pip.pypa.io/en/stable/reference/pip_uninstall/">

```
pip uninstall <package>
```

</a>

> Remarque la commande peut également être pip3 selon votre environnement.

- Créer des paquets pour les partager

> Pour aller plus loin : [créer des paquets pour les partager avec pip](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/)

> \+ des petites verifications pour éviter de télécharger les mauvaises dépendances

### Ajout d'une dépendance - fuzzy wuzzy

Pour importer une dépendance et l'utiliser :

```
from fuzzywuzzy import fuzz
```

puis

```
fuzz.ratio("bonjour","bonsoir")
```

Après l'avoir importé, changez donc le print hello world par un print du ratio de la différence entre les chaines de caractères
"cours de conception logicielle" et "portabilité"

<details><summary>AIDE</summary>
<p>

Plus qu'une aide, on espère que votre écran était tout rouge avant d'arriver ici, sinon bien joué, vous avez esquivé une piètre tentative de notre part de vous faire lire une console.

Vous n'avez probablement pas utilisé pip ou sinon votre config est "particulière", utilisez donc pip pour installer fuzzywuzzy ou criez très fort (exemple de cri : "HA"/"HO"/"A l'aide")

> Remarque pour la suite, n'hésitez pas a utiliser votre moteur de recherche préféré, en informatique il y a beaucoup de ressources en ligne :)

</p>
</details>

### Synchroniser les environnements

Synchronisez maintenant les différents environnements sur lesquels vous travaillez pour valider l'exercice, en respectant les règles !

### Canoniser l'environnement d'execution

<img src="img/pip-freeze.jpeg"/>
Pour mieux partager un environnement qui permet de faire tourner le code, pip propose de sanctuariser les dépendances dans un fichier **requirements.txt**. C'est l'équivalent des fichiers `package.json` en Javascript (npm), `pom.xml` (Java / maven) ...

Il permet de le générer en faisant à la racine du projet (note : ce fichier peut aussi être créé / modifié à la main) :

```
pip freeze > requirements.txt
```

Et d'installer toutes les dépendances venant d'un fichier de ce type, encore a la racine

```
pip install -r requirements.txt
```  

**Le fichier requirements.txt doit être versionné avec votre code sur git**

## Exercice 3 - Mise en place d'une API

### Serveur web

![](img/client-server.png)

https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

```
GET / HTTP/1.1
Host: www.example.com
```

```
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 155
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"
Accept-Ranges: bytes
Connection: close

<html>
  <head>
    <title>An Example Page</title>
  </head>
  <body>
    <p>Hello World, this is a very simple HTML document.</p>
  </body>
</html>
```

### API / Webservice

Application Programming Interface : interface de programmation `applicative`.  
Diffuser des données et des services à destination d'autres applications.

Chez l'ophtalmo :

Est ce que c'est mieux, comme ça ?

```html
<li class="list__item">
  <a class="block__link block__link_img" href="/270229/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <img
        class="pub__img"
        alt="Apollo World Live en live streaming Apollo Théâtre - Salle Apollo 360"
        title="Apollo World Live en live streaming Apollo Théâtre - Salle Apollo 360"
        src="/zg/r115-165-0/vz-F46C96DB-9F48-44B1-9297-A85CBDD9FF1B.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>10€</span
        >
      </div>
    </picture></a
  >
  <a href="/270229/evt.htm" class="block__link block__link_title">
    <span>
      <b style="color:#1A2E41"> Apollo World Live en live streaming </b>
    </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/270099/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <img
        class="pub__img"
        alt="Impro Visio en Live Streaming My Digital Arena"
        title="Impro Visio en Live Streaming My Digital Arena"
        src="/zg/r115-165-0/vz-0196DA94-7B3F-4164-B114-6B54405395ED.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>12€</span
        >
      </div>
    </picture></a
  >
  <a href="/270099/evt.htm" class="block__link block__link_title">
    <span> Impro Visio en Live Streaming </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/269015/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <img
        class="pub__img"
        alt="Le Roi Lion Théâtre de la Tour Eiffel"
        title="Le Roi Lion Théâtre de la Tour Eiffel"
        src="/zg/r115-165-0/vz-577747CF-85FB-4504-87E8-0B1B585E9324.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>23€</span
        >
      </div>
    </picture></a
  >
  <a href="/269015/evt.htm" class="block__link block__link_title">
    <span> Le Roi Lion </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/267124/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <img
        class="pub__img"
        alt="Docteur Alil &amp; Mister Vardar Café de la Danse"
        title="Docteur Alil &amp; Mister Vardar Café de la Danse"
        src="/zg/r115-165-0/vz-A6CEA98B-A4ED-4C48-96A0-B69FB7FC404F.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>16€</span
        >
        <span class="block__offers block__offers_discount"
          ><span class="text__mini">Jusqu'à</span>43%</span
        >
      </div>
    </picture></a
  >
  <a href="/267124/evt.htm" class="block__link block__link_title">
    <span> Docteur Alil &amp; Mister Vardar </span>
  </a>
</li>
<li class="list__item">
  <a class="block__link block__link_img" href="/230940/evt.htm">
    <picture>
      <source
        media="(min-width: 650px)"
        srcset="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <source
        media="(max-width: 649px)"
        srcset="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <img
        class="pub__img"
        alt="Maxime Gasteuil arrive en ville Le Grand Point Virgule - Salle Majuscule"
        title="Maxime Gasteuil arrive en ville Le Grand Point Virgule - Salle Majuscule"
        src="/zg/r115-165-0/vz-84D515BB-5496-4E47-A805-331301C25D1D.jpeg"
      />
      <div class="block__offers-container">
        <span class="block__offers block__offers_price"
          ><span class="text__mini">Á partir de</span>21€</span
        >
      </div>
    </picture></a
  >
  <a href="/230940/evt.htm" class="block__link block__link_title">
    <span> Maxime Gasteuil arrive en ville </span>
  </a>
</li>
```

Ou comme ça ?

```json
{
  "top": [
    {
      "id": 270229,
      "titre": "Apollo World Live en live streaming"
    },
    {
      "id": 270099,
      "titre": "Impro Visio en Live Streaming"
    },
    {
      "id": 269015,
      "titre": "Le Roi Lion"
    },
    {
      "id": 267124,
      "titre": "Docteur Alil & Mister Vardar"
    },
    {
      "id": 230940,
      "titre": "Maxime Gasteuil arrive en ville"
    }
  ]
}
```

Différence entre site web (données + présentation, à destination des humains) et webservice (données brutes, à destination d'autres applications).

**Une API c'est votre rêve de statisticien**

### FastApi

https://fastapi.tiangolo.com/

Framework python pour écrire des API  
Alternatives : Django, Flask

Quickstart :

Dépendances nécessaires : `uvicorn` & `fastapi`

`main.py`

```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"result": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```
python main.py
```

Ouvrir le navigateur sur `http://localhost:8080` :thumbsup:

## Pour aller plus loin

### Associer son environnement python au projet: venv

<img src="img/venv.png">

En local, vous allez vouloir isoler votre projet pour être sur que tout fonctionne. En fait, les paquets installés globalement (sur votre ordinateur pour un autre projet) peuvent être incompatibles avec les paquets du projet.

Python propose pour cela d'isoler l'environnement d'execution local via la création d'un environnement virtuel

=> A la racine d'un projet :

```
python -m venv environnement-virtuel
```

puis activer le script activate.bat qui se trouve dans

> /environnement-virtuel/Scripts/
> Et hop vous voilà dans l'environnement virtuel

- 2 moyens de le vérifier :
  - pip list --local (il n'y a pas grand chose)
  - Vous avez maintenant une parenthèse vous indiquant que vous êtes bien dans votre venv

:boom: Attention à ne pas le versionner toutefois, réferez vous au .gitignore du chapitre git pour plus d'informations

:checkered_flag: maintenant vous pouvez mettre en place l'environnement via pip install -r requirements.txt par exemple
