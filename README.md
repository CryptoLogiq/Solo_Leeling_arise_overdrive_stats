# Solo Leveling: ARISE OVERDRIVE GameData Notes

Ressource communautaire en cours de construction pour documenter les mécaniques
de **Solo Leveling: ARISE OVERDRIVE PC/Steam** à partir des GameData décodés.

## Objectif

Le dépôt sépare deux niveaux de lecture :

- **HUMAN** : rapports Markdown lisibles directement sur GitHub pour comprendre
  les arbres, coûts, rangs, gains et incertitudes.
- **TECHNICAL / DATA** : CSV, tables décodées et scripts permettant de vérifier
  les conclusions.

La fiabilité passe avant la présentation : une valeur non démontrée doit rester
marquée `NON DÉTERMINÉ`.

## Points d'entrée

- [Arbre de talents HUMAN](analysis/reports/SJW_TALENT_TREE_HUMAN.md)
- [Talent planner web](planner/)
- [Détails techniques de l'arbre](analysis/reports/SJW_TALENT_TREE_TECHNICAL.md)
- [Export canonique JSON des arbres](analysis/data/sjw_talent_tree.json)
- [Audit data des arbres](analysis/reports/SJW_TALENT_TREE_DATA_AUDIT.md)
- [Graphe Assassin validé](analysis/reports/SJW_ASSASSIN_TALENT_GRAPH.md)
- [Transitions de rang des compétences](analysis/reports/SJW_SKILL_TRANSITION_CARDS.md)
- [CSV générés](analysis/csv/)
- [Scripts d'analyse](tools/)

## Sources et confiance

La priorité des preuves est définie dans [AGENTS.md](AGENTS.md) :

1. GameData décodés
2. screenshots / observations utilisateur
3. sources web explicitement OVERDRIVE
4. communauté

Ne pas importer de mécanique du jeu mobile sans preuve explicite qu'elle existe
dans OVERDRIVE.
