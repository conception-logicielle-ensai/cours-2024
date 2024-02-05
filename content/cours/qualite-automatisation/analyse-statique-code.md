+++
title = "Analyse statique du code"
description = "Analyse statique, qualimétrie."
date = 2024-02-05T00:00:01
tags = ["lint","python","static"]
header_img= "/img/analysestat.svg"
+++
# Qualite, Automatisation et Tests : Analyse statique du code

> L'analyse statique du code consiste à l'analyser SANS le lancer.

## Petite définition

L’analyse du code statique, appelée aussi analyse du code source ou révision du code statique, est le processus consistant à détecter les mauvaises habitudes de codage, les vulnérabilités potentielles et les défauts de sécurité dans le code source d’un logiciel, sans pour autant exécuter ce dernier. Il s’agit d’une forme de testing en boîte blanche.

Ce type d’analyse permet à vos équipes de repérer les bugs ou vulnérabilités que les autres outils et méthodes de test, par exemple les révisions de code manuelles et les compilateurs, ne relèvent généralement pas.

## Quel objectif ?

Se prémunir de problèmes d'execution à venir sur un code écrit, sans avoir a l'executer à partir d'un sous set de règles, de bonnes pratiques et de contrôles sur le code.


## Linting

<img src="/img/linting.jpg">

Pour tous les languages en particulier les languages non fortement typés, il est souvent assez utile d'établir des conditions d'acceptation du code source. Pour cela, on utilise en général des outils de validation ou linter.

En python on utilisera parmi par exemple : `flake8` `pylint` `autopep8`

Dans ces conditions on retrouvera aussi bien des conditions purement stylistiques : utilisation d'espaces plutôt que de tabulations, nommage des méthodes, ...

Quelques règles sont édictées dans des propostions d'amélioration et d'uniformisation de code de python PEP : 
- PEP 7 https://peps.python.org/pep-0007/
- PEP 8 https://peps.python.org/pep-0008/

Les règles sont modulables par projet et vous êtes libre de configurer pour votre projet les règles qu'il vous semble pertinent ou non de garder.

> Fun Fact : Vous utilisez déjà un linter sans le savoir dans les IDE mais non configurés

Mais également la vérification de certaines règles sur le code : 
- Vérification de la présence du package pour réaliser l'import
- Vérification de la validité de l'usage des fonctions par rapport a la signature des méthodes

Exemple d'usages :
```
# exemple avec black
pip3 install pylint
# puis
pylint ./app
```

> Quel intêret me diriez vous : 

Pour le style : La cohérence du code, permettre de se fixer des règles entre développeurs `as code` qui ensuite sont péreinnes et factuelles.
Pour la vérification : Eviter les erreurs au lancement du code, et donc anticiper les bugs 🐛

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>L'usage et les règles appliquées sont bien entendues paramétrables :  ex : <a href="https://www.codeac.io/documentation/pylint-configuration.html">https://www.codeac.io/documentation/pylint-configuration.html</a>
</div>

## Formatting

<img src="/img/formatting.jpg">


Pour répondre aux besoins de bon respect des règles établies en amont (voir linting). Il peut être pertinent de s'équiper d'un formatter, associé généralement a l'IDE (Visual studio code / Pycharm).
Les formatters classiques pour python sont : `black` `yapf` `Python-autopep8` `isort`

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Voir aussi : <a href="https://github.com/life4/awesome-python-code-formatters">https://github.com/life4/awesome-python-code-formatters</a>
</div>

Exemple d'usages : 
```
# exemple avec black
pip3 install black
# puis
black --check app
```
> Quel intêret me diriez vous :

Etablir des changements seulement de contenu et fonctionnels dans le code permet réellement de ne garder que les changements fonctionnels et non de format lors de l'ajout de fonctionnalité.
La relecture est donc facilitée. Et les règles établies lors du linting sont appliquées par défaut.

<div class="alert alert-info">
  <strong> Pour aller plus loin </strong> <br/>Voir aussi : <a href="https://github.com/life4/awesome-python-code-formatters">https://github.com/life4/awesome-python-code-formatters</a>
</div>


## Security testing (SAST : Static application security testing)

<img src="/img/sast.png">

Les Static Application Security Testing (SAST) sont des outils et des techniques utilisés dans le domaine de la sécurité informatique pour identifier les vulnérabilités potentielles dans le code source des applications.

Ils permettent de détecter des problèmes de sécurité dans le code sans l'executer. 

Les SAST peuvent repérer des vulnérabilités telles que les injections SQL, les failles XSS, les erreurs de gestion de la mémoire, etc. Leur utilisation régulière permet de renforcer la sécurité des applications dès leur conception et de réduire les risques de failles de sécurité.

### Securité : quelques rappels


Pour ce cours nous utiliserons l'outil Snyk mais de nombreux outils permettent de couvrir l'analyse de la sécurité des applications.

Différent types d'attaque en sécurité informatique: 
- Injection (SQL, texte, ..) ~50% : on manipule les entrants de l'application pour dépasser les fonctionnalités prévues.
- Cross Site Scripting : On injecte un script dans une application pour qu'elle l'execute ensuite pour effectuer des actions malveillantes
- Failles de sécurité - CVE : Bugs connus contenus dans des librairies et versions des systèmes qui sont ensuites exploités.
- Attaque par déni de service - DDOS: attaque pour surcharger l'usage d'un service au niveau réseau / mémoire pour empêcher tout ou partie de ses usages possibles.
- Man in the middle : récupération des informations utilisateurs pour usurper son identité et donc corrompre un système d'information

<div class="alert alert-info">
  <strong> Pour aller plus loin</strong> <br/> L'outil Sonar, très utilisé pour l'analyse statique et la détection de faille de sécurité a l'INSEE et ailleurs pour des raisons d'installation on premise : <a href="https://www.sonarqube.org/">Lien vers sonar</a>
</div>


