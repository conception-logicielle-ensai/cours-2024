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
