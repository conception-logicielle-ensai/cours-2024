+++
title = "Création et utilisation d'un webservice"
description = "Notions de client HTTP / serveur HTTP "
date = 2024-02-12T00:00:01
short = true
aliases = ["http","web"]
header_img= "/img/webservice/api-webservice-animate.svg"
+++

Dans cette partie nous allons nous intéresser a l'utilisation d'un webservice et a sa construction.

Pour cela nous allons repartir des enjeux de la mise en place d'un webservice en python.

## Script vs Application

En informatique on distingue souvent 2 types de programmes pour 2 types d'usages :

- Scripts: Un script a une vocation d'usage unique, il s'agit d'un programme executé pour une action ponctuelle. Originellement, les scripts sont executés par des languages interprétés, exemple : `python`.

> Note: il peuvent être executés de manière répétée, mais dans ce cas on appelle cela un Batch. On lance un script tous les X temps, il s'execute et se termine.

- Les applications : d'un code souvent plus construit, les applications se lancent et ont vocation à vivre tant que l'on ne les arrête pas. A l'origine, les applications étaient construites a partir de language compilés, mais ce n'est plus vrai aujourd'hui.

> Dans le cadre de ce TP on va s'intéresser a une application de type api webservice.

## Application et architectures applicatives

Les applications sont définies pour être lancées et répondre a des demandes.

Elles peuvent être utilisables par une interface utilisateur, on appelle cette interface IHM (Interface Homme Machine).

Il existe différents types d'applications :

- Les applications de type `client lourd` : application qui sont hébergées intégralement sur un poste utilisateur (Exemple : application de machine à café pour la machine)
- Les applications de type `client / serveur` : application légères dont les données sont hébergées sur un serveur distant.

=> L'histoire fait que ce modèle est l'un des plus privilégié puisque l'on peut administrer les mises a jour et les données depuis un point central plutôt que sur différents supports.

> C'est ici le cas d'un webservice, il est par design prévu d'être hebergé sur un site distant et de traiter les requêtes en utilisant le protocole HTTP

- Il existe également les applications `n tiers` => On rajoute n couches de client / serveur. C'est le cas des infrastructure microservices. (exemple : SNCF Connect)

> Dans le cas d'une API webservice, on utilise un client http pour interroger notre application. Ce client pouvant être un site web lui même, une application mobile ou un script directement.

## Protocole HTTP

<img src="/img/webservice/TCPUDP.png"/>


Il existe deux façons d'échanger des données. Soit de manière contrôlée et assurée avec le protocole `TCP`, soit de manière plus performantes mais en assurant moins de sécurité le protocole `UDP`.

Ces protocoles sont a la base de la transmission des données entre différents systèmes soit encore entre les applications et les réseaux (LAN, MAN, WAN, PAN).

Le protocole HTTP est un protocole synchrone qui permet la mise a disposition de ressources. 

On peut classiquement requêter un serveur en http en le requêtant a l'aide d'un client http sur son port 80 ou en effectuant une requête en HTTPS (avec les bons certificats) sur le port 443.


<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>  Lien RFC : <a href="https://www.rfc-editor.org/rfc/rfc2616">https://www.rfc-editor.org/rfc/rfc2616</a>
</div>

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>  Three way handshake TCP : <a href="https://fr.wikipedia.org/wiki/Three-way_handshake">https://fr.wikipedia.org/wiki/Three-way_handshake</a>
</div>

### Client HTTP - quelques rappels

<img src="/img/webservice/http.png"/>

Un client HTTP est un programme ou une bibliothèque qui envoie des demandes HTTP à un serveur afin de récupérer des informations ou d'effectuer une action. Quelques exemples de clients HTTP sont les navigateurs web, les outils en ligne de commande comme `curl` et les bibliothèques de programmation comme `requests` pour Python. Ces clients peuvent envoyer différents types de demandes HTTP telles que GET, POST, PUT et DELETE à un serveur, et le serveur répondra avec un code d'état HTTP et éventuellement un corps de message.

Ces clients peuvent gérer les requêtes HTTP, en fonction de la ressource cible a l'aide de méthodes ou verbes, les plus utilisées sont:

- `GET`: Retrouve une représentation de la ressource demandée au serveur.

- `POST`: Ajoute une représentation de la ressource au serveur. C'est souvent le cas pour un formulaire ou un JSON body a envoyer au serveur.

- `PUT`: Ajoute ou met a jour une représentation de la ressource au serveur.

- `DELETE`: Supprime la ressource si elle existe côté serveur.

Ces méthodes permettent d'interagir avec des serveurs HTTP pour y soumettre ou récupérer des informations.

Exemple : `curl` `requests` `insomnia`

```
curl localhost:8000
```

```
reponse = requests.get('http://google.com')
# Si json
# print(reponse.json())
# Si texte
# print(reponse.text)
```

Les navigateurs web sont des clients http qui effectuent des requêtent HTTP GET en parcourant les pages, POST en soumettant des formulaires. 

Ainsi : On peut automatiser programmatiquement des scénarios décrits sur des navigateurs par l'intermédiaire de clients http.

## Intuition sur l'intêret des webservices :


Application Programming Interface (`API`) : interface de programmation `applicative`.

**Objectif:**
Diffuser des données et des services à destination d'autres applications.

**HOOK**:

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

> Les API sont également une belle prouesse pour `l'interoperabilité` des services, en effet, elles répondent a une norme agnostique au language.

> Exemple: j'aime bien python pour du ML et je suis plus a l'aise avec R pour des regressions, je peux faire un site web qui récupère les résultats des 2 pour avoir le meilleur des 2 mondes pour moi.




### Qu'est ce qu'une API - webservice ?

Une API est une application qui permet l'exposition de services a travers des ressources. Ces services sont appelés `endpoint` ou `resources` et regroupent l'éxécution de fonctions dans le code a la demande d'un utilisateur.

> Exemple : endpoint `/` accessible par requête GET pour dire **hello world** sur une application lancée

Cette application écoute les requêtes HTTP et les traite a la demande de manière synchrone.

Les fonctions sous respectent un contrat d'interface fonctionnelle strict et sont censées répondre de manière adéquate au traitement de la requête demandée a l'aide de code retours appropriés.

- Code retours `2XX`: `200`, `201` ... - La requête s'est bien passée et elle a eu un effet dans le système. 
- Code retours `3XX`: `300`,`301`,`302` ... -  La requête est entrée dans le système et a été redirigée.
- Code retours `4XX`: `400`,`401`,`402`,`403`,`404` ... => La requête a été rejetée par le système car l'utilisateur de l'API n'a pas effectué une action valide. (non authentifié, demande de ressources non présentes)
- Code retours `5XX`: `500`, `502` - La requête a été rejetée par l'application pour des raisons internes au système : plantage interne, le serveur n'était pas prêt, etc...

En Python 🐍 il existe différents framework ou package permettant de mettre en place des API webservice : 
- Django : Très grand framework pour des grands projets intégrant des briques préconstruites pour l'interaction avec les bases de données, outils d'authentification...
- Flask : Projet plus ancien permettant la mise en place rapide d'un service http : service statique ou api webservice
- Fastapi : Projet récent qui permet notamment une autodocumentation et sérialisation / désérialisation facilitée.

> Dans ce cours nous verrons fastapi, mais dans vos projets professionnels et personnels vous serez sûrement amenés a utiliser chaque librairies.

Les API respectent le protocole HTTP et répondent avec des formats de données agnostique du language : 

- Le `json` très souvent, puisque le javascript est quasi omniprésent dans les interfaces et depuis peu dans les implémentations de serveur web

```json
{"employees":[
  { "firstName":"John", "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":"Peter", "lastName":"Jones" }
]}
```
- Le `xml` dans des systèmes plus anciens et historiques.
```xml
<?XML VERSION="1.0" STANDALONE="yes" ?>
<employees>
    <employee>
        <firstName>John</firstName> <lastName>Doe</lastName>
    </employee>
    <employee>
        <firstName>Anna</firstName> <lastName>Smith</lastName>
    </employee>
    <employee>
        <firstName>Peter</firstName> <lastName>Jones</lastName>
    </employee>
</employees>
```

Remarque : une fois `pythonisés` ces formats seront récupérés comme des objets ou des dictionnaires. Mais pour cela il faut parler de sérialisation / désérialisation.

### Serialisation / Déserialisation

<img src="/img/webservice/serialisation-deserialisation.webp" />
Un des enjeux du travail avec des ressources externes d'un programme est de savoir convertir les entrants d'un programme en des formes connues de notre programme mais également de pouvoir exposer des objets connus de notre programme dans un format utilisable par les autres programmes.

En python vous êtes plutôt habitués a utiliser la sérialisation avec le module intégré `json`.

<img src="/img/webservice/format.webp"/>

Cette logique est a intégrer dans la conception de vos logiciels : toujours contrôler les entrants et les convertir en un format connu du système.

Par exemple, en programmation orientée objet, il sera attendu qu'entre 2 couches de séparation architecturale vous introduisiez des objets de type : `DTO` ou `data transfer object`. Qui permettent une conversion et donc de pereinniser le modèle dans chacune des couches de votre système.

<img src="/img/webservice/dto.jpg"/>

> Exemple dans le cas d'une application `frontend`

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>  Architecture hexagonale => Gérer les entrées sorties => <a href="https://alistair.cockburn.us/hexagonal-architecture/">https://alistair.cockburn.us/hexagonal-architecture/</a>
</div>


### Synchronicité / Asynchronicité

Lorsque l'on souhaite passer a l'échelle dans l'utilisation de services externes, puisqu'on souhaite pouvoir continuer a faire fonctionner notre application pendant le traitement d'une requête par exemple.

L'asynchronisme est particulièrement utile lorsqu'on travaille avec des appels à des services Web, car cela permet à votre programme de continuer à fonctionner pendant que vous attendez la réponse du service.

> Imaginons que vous ayez un programme qui doit faire plusieurs appels à des services Web pour récupérer des données. Si vous effectuez ces appels de manière synchrone, c'est-à-dire un par un dans l'ordre, votre programme va devoir attendre la réponse de chaque appel avant de passer au suivant. Cela peut prendre beaucoup de temps, surtout si les appels prennent du temps à répondre.

> En revanche, en utilisant l'asynchronisme, vous pouvez lancer plusieurs appels à des services Web en même temps, sans attendre que chacun se termine avant de passer au suivant. Cela permet à votre programme de continuer à s'exécuter pendant que les appels sont en cours, et de traiter les réponses dès qu'elles arrivent.

Dès que vous avez besoin du résultat de la requête asynchrone, vous pouvez utiliser l'opération `await` qui attendra que toutes les fonctions asynchrones précédentes aient fini.
Exemple en python avec la librairie `asyncio` :

```python
import asyncio

# Fonction simulant une requête asynchrone à une API
async def fetch_data():
    print("Début de la requête...")
    # Simuler une attente de 2 secondes pour la réponse de l'API
    await asyncio.sleep(2)
    print("Données récupérées !")
    return {"data": "Données importantes"}

# Fonction pour traiter les données
async def process_data():
    print("Traitement des données...")
    # Simuler une attente de 1 seconde pour le traitement
    await asyncio.sleep(1)
    print("Données traitées !")

# Fonction principale asynchrone
async def main():
    # Utilisation de await pour appeler fetch_data de manière asynchrone
    data = await fetch_data()
    # Utilisation de await pour appeler process_data de manière asynchrone
    await process_data()
    print("Processus terminé !")

# Exécution de la fonction principale
asyncio.run(main())
```

<div class="alert alert-warning">
  Attention en un sens, introduire de l'asynchronicité dans des fonctions ou cela n'est pas nécessaire peut être lourd
</div>




