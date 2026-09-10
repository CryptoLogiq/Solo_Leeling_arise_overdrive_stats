# SJW Talent Tree Technical

Ce rapport justifie la reconstruction lisible de `SJW_TALENT_TREE_HUMAN.md`.

## Sources externes secondaires

- Backdash, `Solo Leveling Arise Overdrive Classes and Skill Trees guide`: https://thebackdash.com/gaming/solo-leveling-arise-overdrive-classes-and-skill-trees-guide/
- GuideDragon, `Solo Leveling: Arise Overdrive - Classes & Builds explained`: https://guidedragon.de/en/guides-en/solo-leveling-arise-overdrive-classes-builds-explained-which-class-is-the-best/
- AlcastHQ, `Best Sung Jinwoo Duelist Build Guide`: https://alcasthq.com/slao-duelist-build/
- HaploGamingChef, `Top 5 Game-Changing Updates in Solo Leveling: ARISE Overdrive`: https://haplogamingchef.blogspot.com/2025/06/Top%205%20Game-Changing%20Updates%20in%20Solo%20Leveling%20ARISE%20Overdrive.html

Ces sources ne sont utilisées que pour corroborer la structure visuelle. Les coûts, rangs, effets et valeurs viennent des GameData.

## Modèle

- Le rapport joueur agrège par `LogicalTalentID`, pas directement par `NodeID`.
- Par défaut, un NodeID reste son propre talent logique (`RAW_NODE_ONLY`).
- Plusieurs NodeID ne peuvent partager un talent logique que si une preuve explicite est ajoutée dans `LogicalGroupingEvidence`.
- Les effets multiples d'un même rang logique sont regroupés dans la colonne `Effet`.
- `ProgressionDepth`: profondeur réelle calculée depuis les relations Parent.
- `VisualRow`: valeur GameData `NodeTierY`, utilisée seulement comme rangée visuelle.
- Position horizontale: `NodeTierX`.
- Rang technique: `NodeMaxLevel`; rang logique: `LogicalRank`.
- Les groupes 9/10 ne sont pas forcés dans les classes; ils deviennent des structures non rattachées avec noms déduits.
- Données détaillées vérifiables: `analysis/csv/sjw_talent_tree.csv` et `analysis/csv/sjw_talent_tree_detailed.csv`.

## Talents agrégés

| Système | Talents |
|---|---:|
| weapon | 99 |
| class | 82 |
| jinwoo | 38 |
| unattached | 36 |

## Contrôle qualité

- La partie principale du rapport joueur est triée arbre -> branche -> talent logique dans l'ordre technique.
- Chaque NodeID source appartient à au plus un talent logique.
- Chaque rang logique pointe vers un seul NodeID sauf preuve explicite future.
- Les sections de rendement/statistiques sont déplacées en annexe.
- `NodeID`, `BuffID`, noms de tables et groupes internes sont absents du corps principal.
- Les détails `NodeID`/`BuffID` complets restent dans ce rapport technique, pas dans le rapport HUMAN.
