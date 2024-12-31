# Projet TC-Room-Finder

## Objectif

Ce projet permet de trouver les salles disponibles en TC en se basant sur un emploi du temps et une liste de salles. Il permet de vérifier, pour une plage horraire donnée, quelles salles ne sont pas occupées par des cours.

## Fonctionnement

1. **Chargement des données** : Le programme charge les emplois du temps des différents groupes sous forme de fichiers `.ical` (format iCalendar).
2. **Traitement des événements** : Chaque événement (cours) est analysé pour déterminer son créneau horaire, ainsi que la salle dans laquelle il se déroule.
3. **Vérification des disponibilités** : Pour une plage horaire de la journée donnée (de 8h00 à 18h00), le programme vérifie si la salle est libre ou occupée par un cours.
4. **Affichage des résultats** : À la fin, il affiche les salles disponibles.

## Prérequis

- Python 3.x
- Les bibliothèques suivantes doivent être installées :
  - `icalendar` : pour lire et traiter les fichiers `.ical`.
  - `datetime` : pour manipuler les horaires et dates.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers.
2. Installez les dépendances via pip :
   ```bash
   pip install icalendar
   ```

## Utilisation

1. Créez un fichier texte "link.txt", collez y le lien de téléchargement du ical (ce lien se trouve bas de la page TC-net). Remplacez dans le lien par : promo={promo}&groupe={group}
2. Dans le script principal, modifiez la variable `date` et la variable `span` pour définir la date et la durée pour lesquelles vous souhaitez vérifier les disponibilités des salles. (span = 2 signifie deux tranches de 30 minutes, donc 1h).
3. Pour une première execution, mettez UPDATE = True pour télécharger les .ical. 
4. Exécutez le script Python pour obtenir la liste des salles disponibles pour cette date.

```bash
python room_finder_ical.py
```

Le programme va afficher, les salles qui sont disponibles et ne sont pas occupées par des cours.
---
