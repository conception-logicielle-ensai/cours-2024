# Runtime

## Source, compilation, binaire, buildtime, runtime ...

- Source = code humain (`.py`, `.R`, `.java` ...)
- Binaire = langage machine (`.jar`, `.exe` ...)
- Compilation = ensemble de transformations code => binaire
- Buildtime = moment de la compilation (build)
- Runtime = moment de l'exécution

Scénario de référence :

- Le dev écrit du code source
- Le code source est versionné
- La compilation (locale ou automatisée) transforme le code source en binaire
- Le binaire est publié
- En production : runtime + binaire = chocapics

## Hello world
Hello world python, lancer datalab via cli


```
python3 main.py
```

## Versionning
dépot git etc
=> faire tourner sur 3 plateformes différentes (katacoda,ordi perso,innovation)

## Ajout de dépendance

pip install fastapi

pip install uvicorn

pip freeze > requirements.txt

pip install -r requirements.txt

git pull
=> faire tourner sur 3 plateformes différentes (katacoda,ordi perso,innovation)

## Externalisation de la conf 

