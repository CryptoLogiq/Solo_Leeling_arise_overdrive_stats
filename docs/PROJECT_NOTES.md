# Notes Projet

Ce fichier garde les informations utiles au développement du dépôt, séparées du
README destiné aux joueurs.

## Objectif technique

Le dépôt documente les mécaniques de **Solo Leveling: ARISE OVERDRIVE PC/Steam**
à partir des GameData décodés.

Il conserve deux niveaux de lecture :

- **HUMAN** : rapports Markdown lisibles sur GitHub ;
- **TECHNICAL / DATA** : JSON, CSV et scripts permettant de vérifier les données.

La fiabilité passe avant la présentation : une valeur non démontrée doit rester
marquée `NON DÉTERMINÉ` ou `WIP` selon le contexte d'affichage.

## Sources et confiance

Ordre de priorité des preuves :

1. GameData décodés
2. screenshots / observations utilisateur
3. sources web explicitement OVERDRIVE
4. communauté

Ne pas importer de mécanique du jeu mobile sans preuve explicite qu'elle existe
dans OVERDRIVE.

## Points d'entrée techniques

- [Export canonique JSON des arbres](../analysis/data/sjw_talent_tree.json)
- [Base effets / buffs / skills](../analysis/data/sjw_effect_database.json)
- [Progression des points](../analysis/data/sjw_point_progression.json)
- [CSV générés](../analysis/csv/)
- [Scripts d'analyse](../tools/)

## Publication GitHub Pages

Le planner est statique et peut être publié sans workflow GitHub Actions.

Configuration recommandée dans GitHub :

- **Settings** -> **Pages**
- **Source** : `Deploy from a branch`
- **Branch** : `main`
- **Folder** : `/(root)`

La page racine du dépôt redirige ensuite vers `/planner/`.
