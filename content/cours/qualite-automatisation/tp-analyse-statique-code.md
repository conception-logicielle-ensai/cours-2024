+++
title = "Analyse statique du code TP"
description = "Analyse statique, qualimétrie."
date = 2024-02-05T00:00:02
tags = ["git","python"]
header_img= "img/analysestattp.svg"
+++
# Qualite, Automatisation et Tests : Analyse statique du code

Pour ce TP on partira cette fois ci d'un projet déjà élaboré par une équipe au sein du ssplab. Prédicat.

**https://github.com/InseeFrLab/predicat.git**

Pour faciliter la vie des gens, j'ai forké ce projet dans le groupe `conception logicielle ensai` sur github, si vous ne voulez pas notifier la personne que vous forkez son projet.

<a href="https://github.com/conception-logicielle-ensai/predicat.git"> https://github.com/conception-logicielle-ensai/predicat.git </a> 


## Exercice 1 : Mise en place 

> (Wait it's git again ? :OOO)

1. Forkez le projet : <a href="https://github.com/conception-logicielle-ensai/predicat.git">https://github.com/conception-logicielle-ensai/predicat.git</a>, pour les gens qui ne sont pas sur github, clonez le directement (passez donc la partie 2)

2. Cloner le repository dans un sous dossier de votre TP, dans votre environnement de travail préféré

3. Depuis le dépot récupéré, suivre les instructions pour l'installation via le README.md, veuillez toutefois a bien faire cela dans le repertoire **app** du dépot git, par défaut : **predicat/app**

4. Lancez l'application via la commande `uvicorn main:app`, pensez bien a installer les dépendances au préalable, et vous pouvez utiliser un environnement virtuel.

<details><summary><b>AIDE 1 (clickable): Comment savoir les dépendances nécessaires à l'exécution de l'application ?</b></summary>
<p>
Rappel : 

Pour un projet python, les dépendances sont en général gérées par pip (https://packaging.python.org/tutorials/installing-packages/) et sont listées dans le fichier requirements.txt

```python
pip install -r requirements.txt
```

</p>
</details>

<details><summary><b>AIDE 2 (clickable) : Comment débugguer si l'application qui ne se lance pas / crash ? </b></summary>
<p>

Vous avez probablement mal lu le README.md.

Pour résoudre le problème, vous aurez besoin d'un modèle. On pourra utiliser le modèle de test disponible ici : https://minio.lab.sspcloud.fr/conception-logicielle/model_na2008.bin

Vous devez ensuite enlever du fichier de configuration yaml, les lignes concernant les modèles qui ne sont pas le modèle 2020_old.

Une fois l'application lancée, vous pouvez la requêter avec votre c lient HTTP préféré et adapté à votre environnement de travail (curl, navigateur web, insomnia ...) : [http://localhost:8000/label?q=confiture](http://localhost:8000/label?q=confiture) ou encore [http://localhost:8000/label?q=omelette%20du%20fromage](http://localhost:8000/label?q=omelette%20du%20fromage)

Si ça ne resoud pas, cherchez par rapport a l'erreur renvoyée par la console.

</p>
</details>


## Exercice 2 : Analyse statique du code - Linting / Formatting

Pour cette partie on va analyser le code de l'application prédicat.

Installons les paquets black, isort et pylint.

=> `pip3 install black isort pylint`

- Lancez pylint sur le projet (il applique par défaut la config de la PEP8) 

`pylint app` (app étant le dossier de l'appli, si vous y êtes déjà `pylint *.py`)

> Que constatez vous ? Est ce qu'il y a des erreurs? De quel type ?

=> Petit tour d'horizon des erreurs possibles : <a href="https://pylint.readthedocs.io/en/stable/user_guide/messages/messages_overview.html" </a>

- Appliquez le formattage avec black et isort

`black app` et `isort --profile black app`

Réappliquez votre linter sur l'application. Constatez vous un changement dans la notation du code ? 

> Pour valider un dépôt de code on peut par exemple se dire qu'on n'autorise pas une note inférieure a 7 pour le projet et s'y tenir.

## Exercice 3 : Analyse de la sécurité du code et de ses dépendances

- Créez un compte sur Snyk
- Paramétrez l'accès a votre projet sur l'application par l'onglet :
 Projects => Github => `{user}/predicat`
- Profit !

Si vous avez du temps vous pouvez regarder un peu les résultats sur le projet.

