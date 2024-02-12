+++
title = "Interface web et Webscraping"
description = "Applications web  et Webscraping avec python"
date = 2024-02-12T00:00:05
short = true
aliases = ["webscraping","web"]
header_img= "/img/webservice/web-scraping.svg"
+++

Avec la possibilité de parcourir des pages par script a été mis en place un mode de collecte et d'analyse des données brutes sur le Web, le `web scraping`.
Le principe : récupérer le contenu de pages entières rendues pour les utilisateurs humains (au format html) et en récupérer les données importantes pour alimenter des jeux de données ou autre.
La communauté Python a mis au point des outils de web scraping assez puissants qui permettent justement de récupérer des données des sites.

> https://github.com/adonistividad/web-scrapin

## Interface web et sites web - Contexte

Avant d'être rendu comme une belle page côté utilisateur, un site web utilise différents fichiers.

- Les fichiers `HTML` : Ils décrivent la structure logique d'une page web, définissent le contenu des pages. Ils s'écrivent a l'aide de balises `Markup` de manière plutôt verbeuse.
```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
        domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
> example.org
- Les fichiers `CSS` : fichiers de style, ils gèrent l'apparence des balises présentées.
```css
body {
    background-color: #f0f0f2;
    margin: 0;
    padding: 0;
    font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
div {
    width: 600px;
    margin: 5em auto;
    padding: 2em;
    background-color: #fdfdff;
    border-radius: 0.5em;
    box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
}
a:link, a:visited {
    color: #38488f;
    text-decoration: none;
}
@media (max-width: 700px) {
    div {
        margin: 0 auto;
        width: auto;
    }
}
```
- Les fichiers `javascript` : éléments de scripts du site, permettent de réaliser des actions sur des éléments Html ou css.

```html
<button id="button"type="button">Affichage d'un nombre aléatoire</button>
<div id="affichage"></div>
```

```javascript
document.getElementById("button").onclick = function() {
    document.getElementById("affichage").innerHTML = Math.random();
};
```

<button id="button" type="button">Affichage d'un nombre aléatoire</button>
<div id="affichage"></div>
<script>document.getElementById("button").onclick = function() {
    document.getElementById("affichage").innerHTML = Math.random();
};</script>

> Nous allons donc ici nous intéresser au contenu des pages rendues et donc aux fichiers `html` récupérés par requêtage des sites.


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>
    Un petit historique : La plupart des applications web "anciennes" sont en PHP 
 + JS + HTML + CSS pour utiliser la flexibilité du php pour la construction de pages `templatisées`. En python des applications du même type peuvent être construites avec le framework <b>Django</b>.
</div>

## Traitement du contenu des sites web : cas d'école du parsing de string

La récupération des données issues d'un site au format `html` est possible par différents outils de type client `HTTP`. Ces données ne sont pas exploitables telles quelles, elle nécessitent a minima un retraitement par rapport a tous les éléments d'affichage inutiles pour l'exploitation des données.

Ce retraitement peut se fait de manière manuelle dans les str, avec les fonctions `split` ou `find`

exemple pour récupérer le nombre de parties du cours envoyées sur le site : 
```python
import requests

reponse_requete_http = requests.get("https://conception-logicielle.abrunetti.fr/cours/")
r = requests.get(url)
html = r.text
url = "http://localhost:1313/cours/"
get_h2_parties_du_cours_beginning_index = html.find("<h2 id=\"parties-du-cours\"")
html_apres_parties = html[get_h2_parties_du_cours_beginning_index::]
get_liste_parties_du_cours_start_index = html_apres_parties.find("<ul>") + 4
get_liste_parties_du_cours_end_index = html_apres_parties.find("</ul>")
html_parties_du_cours = html_apres_parties[get_liste_parties_du_cours_start_index:get_liste_parties_du_cours_end_index]
print("nombre de parties du cours : "+str(len(html_parties_du_cours.split("<li>")) - 1))
```


### Regex, Expressions régulières : Isoler et capturer dans des chaines caractères

<img src="/img/webservice/regex.jpg">
Les expressions régulières, ou regex pour faire court, sont des motifs que vous pouvez utiliser pour rechercher du texte dans une chaîne de caractères. 
On parle assez souvent de `pattern` `matching`. On va donc ici élaborer des patterns pour récupérer les ensembles cohérents de chaine de caractères qui respectent ce pattern.

Quel intêret ? Ici l'on va parcourir des balises html diverses `div` `ul` et l'on va vouloir par exemple récupérer les métadonnées contenues dans ces balises.

Python prend en charge les expressions régulières grâce au module `re` déjà présent dans sa bibliothèque standard.

> C'est un concept qui est présent dans la plupart des languages. Il est donc réutilisable lors de problématiques de traitement de données au format `str`

### Syntaxe 

| Ancres | Description                                               |
|--------|-----------------------------------------------------------|
| ^      | Début de ligne. Correspond au début d'une chaîne de caractères. |
| $      | Fin de ligne. Correspond à la fin d'une chaîne de caractères. |
| \b     | Limite de mot. Correspond à la position entre un caractère de mot (\w) et un caractère qui n'est pas un caractère de mot. |

| Symbole spécial | Description                                               |
|-----------------|-----------------------------------------------------------|
| .               | Correspond à n'importe quel caractère, sauf un saut de ligne. |
| *               | Correspond à zéro ou plusieurs occurrences du caractère précédent. |
| \d              | Correspond à un chiffre. Équivalent à [0-9].              |
| \D              | Correspond à tout caractère qui n'est pas un chiffre. Équivalent à [^0-9]. |
| \w              | Correspond à un caractère alphanumérique (lettres, chiffres, souligné). Équivalent à [a-zA-Z0-9_]. |
| \W              | Correspond à tout caractère qui n'est pas alphanumérique. Équivalent à [^a-zA-Z0-9_]. |
| \s              | Correspond à un caractère d'espacement (espace, tabulation, retour à la ligne). |
| \S              | Correspond à tout caractère qui n'est pas un caractère d'espacement. |

Exemples d'utilisation : 

- **^abc** : Correspond à la chaîne "abc" au début de la ligne.
- **xyz$** : Correspond à la chaîne "xyz" à la fin de la ligne.
- **\d{3}** : Correspond à trois chiffres consécutifs.
- **\w+** : Correspond à un ou plusieurs caractères alphanumériques.
- **^toto.*** récupère toute la ligne si elle contient toto au début
### Groupes de Capture :
Les groupes de capture sont utilisés pour capturer une partie spécifique d'une correspondance d'expression régulière. Ils sont délimités par des parenthèses.

| Expression régulière | Description                                |
|----------------------|--------------------------------------------|
| (.*)                 | Capture toute la chaine                    |
| `<li>(.*?)</li>`     | Capture tout ce qui est entre la balise li |

On peut ensuite utiliser les groupes de capture avec `\1` ou `\0`

Exemple avec le support du cours
```python
import requests
url = "https://conception-logicielle.abrunetti.fr/cours/"
r = requests.get(url)
html = r.text
print(html)
import re
pattern_regex = "<li><a href=\/cours/(.*?)\>"
matches = re.findall(pattern_regex,html)
print(matches)
# [' title=Cours', 'introduction', 'introduction', 'git/', 'portabilite/', 'qualite-automatisation/']
```
## Traitement des données avec un Parser HTML : Exemple de beautiful soup

<img src="/img/webservice/beautifulsoup.jpg">

Beautiful Soup permet d'encapsuler l'arborescence des éléments html dans un objet afin de pouvoir assez facilement le parcourir.

C'est une librairie externe on doit l'installer avec `pip` : `pip3 install beautifulsoup4`
```python
from bs4 import BeautifulSoup
import requests

url = "https://conception-logicielle.abrunetti.fr/cours/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")
```

L'objectif de ce parser est de pouvoir réaliser du parsing de html et donc de s'abstraire de toutes les règles de style interne a la page html elle même. En effet, certains pourraient vouloir sauter des lignes pour séparer différentes sections alors que d'autres non. Cette information pollue la récupération de données et donc il est de bon ton de la contrôler.

Ainsi une page comme celle ci : 

devient après parsing : 

Beautiful soup permet également le requêtage des données récupérées: 
```python
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
title_element = job_element.find("h2", class_="title")
print(title_element.text)
```


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>
    Doc officielle : <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">https://www.crummy.com/software/BeautifulSoup/bs4/doc/</a>
</div>

## Automatisation avec Selenium

<img src="/img/webservice/selenium.webp">
Selenium est un outil qui permet d'executer des tests et des actions comme un robot sur des interfaces web. On peut l'utiliser aussi bien pour la réalisation de tests fonctionnels : `je me connecte a tel doctolib, je m'attends a trouver 10 profils différents de médecins dans l'affichage`

C'est un outil qui est très utilisé dans différents languages : java, python, javascript,.. 

ça s'installe avec pip : `pip3 install selenium`

Regardons ensemble le **getting started** de la doc officielle : <a href="https://selenium-python.readthedocs.io/getting-started.html"> https://selenium-python.readthedocs.io/getting-started.html
</a>