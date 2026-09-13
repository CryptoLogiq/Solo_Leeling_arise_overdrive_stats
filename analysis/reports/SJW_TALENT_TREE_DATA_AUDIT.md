# SJW Talent Tree Data Audit

Audit global généré depuis le modèle canonique `analysis/data/sjw_talent_tree.json`.

## Comptes

- Systèmes: 4
- Arbres / onglets: 15
- Sections / branches: 28
- NodeID visibles source: 258
- NodeID exportés JSON: 258
- NodeID exportés CSV: 258
- Lignes CSV: 453
- Talents/nœuds avec rangs internes (`NodeMaxLevel > 1`): 93
- Racines: 41
- Bifurcations: 41
- Convergences: 32
- Liens Parent -> Child: 249

## Contrôles de régression

- Assassin / Attaque sournoise: arêtes exactes validées.
- Assassin / Frappe vitale: arêtes exactes validées.

## Anomalies

- Aucune anomalie bloquante détectée.

## NON DÉTERMINÉ

- Conversion runtime exacte de certaines valeurs raw.
- Additivité exacte entre sources de stats différentes.
- Rôle final de sjw_talent_tree_detailed.csv: copie de compatibilité du CSV canonique tant qu'aucune vue détaillée distincte n'est définie.

## Notes

- `VisualColumn` expose `NodeTierX` pour le futur rendu web.
- `NodeOffset` expose `NodeOffset` brut; il aide au placement mais ne prouve aucune relation.
- `ParentNodeID` reste une relation de nœud à nœud; les rangs internes ne multiplient pas les arêtes.
