+++
title = "Introduction"
description = "Installation du poste de dév"
date = 2024-01-15T17:00:01
aliases = ["introduction"]
tags = ["introduction"]
short = true    
+++

Cette section est écrite pour vous permettre de configurer votre poste convenablement. 

## Ubuntu

Pour les besoins des différents tps. Nous aurons besoin d'installer python3, vscode, git.

Pour cela, il est d'usage d'utiliser des outils pour l'aide a l'installation de paquets indexés. On appelle ce genre d'outil des gestionnaires de paquets.

Ces outils permettent, par le biais d'une CLI d'installer des paquets fonctionnels et prêts a l'usage.

Pour un Ubuntu, nous avons `apt` (debian) et `snap` (ubuntu).

Lors de la première utilisation il est indiqué de rafraichir l'index pour apt : `apt update`. Il pourra ainsi récupérer des paquets parmi les dépôts qu'il a de configuré par défaut.

Cela donne un script d'installation de ce type: 

### Configuration TP1

```text
sudo su
apt update
echo "installation de python3 et git"
apt install -y python3-pip git-all
snap install --classic code
```

### Configuration TP2

Le TP2 nécessite l'installation de docker. Cela en executant le script suivant : 

