# Sung Jinwoo - Talent Tree / Skill Tree

Sources: `CharPCSkillTreeNode`, `CharPCSkillTreelMainTab`, `CharPCSkillTreelSubTab`, `CharPCStatAbility`, `ChComBuff`, `ChComStatDesc`, `TextData.byte`, `SysConst`.

CSV: `analysis/csv/sjw_talent_tree.csv`

Nœuds affichés reconstruits: 258.
Nœuds avec effet numérique/stat lisible: 84.

Progression: `ProgressionDepth` est calculé depuis les relations Parent. `VisualRow` conserve la valeur GameData `NodeTierY` et décrit seulement la rangée dans l'interface.
Talent logique: `LogicalTalentID` ajoute une couche au-dessus des NodeID. Par défaut, chaque NodeID reste son propre talent logique; un regroupement multi-NodeID exige une preuve explicite dans `LogicalGroupingEvidence`.

## Réponse immédiate: Attaque 1/3 -> 3/3

- Rang 1/3: gain marginal 1%, cumul 1%, coût 1 SpecialPoint, buff `200000086`.
- Rang 2/3: gain marginal 1%, cumul 2%, coût 1 SpecialPoint, buff `200000086`.
- Rang 3/3: gain marginal 1%, cumul 3%, coût 1 SpecialPoint, buff `200000086`.

Lecture: le nœud `31100102` applique le buff `200000086`, `AttFR=100`, `NodeMaxLevel=3`. La conversion d'affichage `0.01` est fortement appuyée par les textes de buffs du jeu: `100` correspond à `1%`. Le rang 3/3 donne donc `3%` cumulés si le moteur applique une instance/stack par rang.

Statut: **FORTEMENT PROBABLE** pour `+1% par rang / +3% au rang 3`; **NON DÉTERMINÉ** pour l'ordre d'application runtime, l'additivité exacte entre sources différentes et la base exacte d'attaque affectée.

## Structure globale

| Arbre principal | Lignes exportées |
|---|---:|
| GSSkillTree | 182 |
| SJWSkillTree | 87 |
| LordSkillTree | 76 |
| Groupe 9 | 54 |
| Groupe 10 | 54 |

## 5 patterns d'amélioration les plus fréquents

- passif à rang unique avec gain numérique: 165 nœuds
- 3 rangs, gain marginal fixe, coût plat: 57 nœuds
- 3 rangs, gain marginal fixe, coût croissant: 36 nœuds

## Effets de stat détectés

| Effet | Lignes |
|---|---:|
| Taux de coup critique (`CriticalP`) | 39 |
| Attaque (`AttFR`) | 34 |
| Défense (`ArmFR`) | 31 |
| PV (`IncreaseMHP`) | 31 |
| Dégâts de coup critique (`CriDamP`) | 30 |
| Pénétration de défense (`ArmPenP`) | 24 |
| Pénétration de défense (`ArmPen`) | 20 |
| Réduction des dégâts (`DamReduP`) | 10 |
| Précision (`PrecisionP`) | 9 |
| PM max (`AddMMP`) | 3 |
| Dégâts infligés (`DamP`) | 2 |
| Dégâts conditionnels (`IncreaseDamageByTargetSpecialState`) | 2 |
| Dégâts conditionnels (`IncreaseDamageByTargetBuff`) | 1 |

## Talents de stats principaux

| Arbre | Sous-onglet | Branche | Talent | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Effet | Gain marginal | Cumul | Confiance |
|---|---|---|---|---:|---:|---:|---:|---|---|---:|---:|---|
| SJWSkillTree | Assassin | Attaque sournoise | Attaque augmentée | 111601 | 5 | 6 | 1/1 | 3 SkillPoint | Attaque | 0.8% | 0.8% | FORTEMENT PROBABLE |
| SJWSkillTree | Duelliste | Frappe enragée | Défense augmentée | 113401 | 3 | 4 | 1/1 | 3 SkillPoint | Défense | 6.4% | 6.4% | FORTEMENT PROBABLE |
| SJWSkillTree | Duelliste | Coup unique | Augmentation des PV | 114501 | 4 | 5 | 1/1 | 3 SkillPoint | PV | 6.4% | 6.4% | FORTEMENT PROBABLE |
| SJWSkillTree | Magicien élémentaire | Glace | Augmentation de la Pénétration de défense | 115402 | 3 | 4 | 1/1 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| SJWSkillTree | Magicien élémentaire | Feu | Pénétration de défense augmentée | 116401 | 3 | 4 | 1/1 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 1 1/3 | 119101 | 0 | 1 | 1/3 | 2 SkillPoint | Attaque | 1% | 1% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 1 2/3 | 119101 | 0 | 1 | 2/3 | 3 SkillPoint | Attaque | 1% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 1 3/3 | 119101 | 0 | 1 | 3/3 | 4 SkillPoint | Attaque | 1% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 1 1/3 | 119102 | 0 | 1 | 1/3 | 2 SkillPoint | Défense | 1% | 1% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 1 2/3 | 119102 | 0 | 1 | 2/3 | 3 SkillPoint | Défense | 1% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 1 3/3 | 119102 | 0 | 1 | 3/3 | 4 SkillPoint | Défense | 1% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 1 1/3 | 119103 | 0 | 1 | 1/3 | 2 SkillPoint | PV | 1% | 1% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 1 2/3 | 119103 | 0 | 1 | 2/3 | 3 SkillPoint | PV | 1% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 1 3/3 | 119103 | 0 | 1 | 3/3 | 4 SkillPoint | PV | 1% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 2 1/3 | 119201 | 1 | 2 | 1/3 | 2 SkillPoint | Attaque | 2% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 2 2/3 | 119201 | 1 | 2 | 2/3 | 3 SkillPoint | Attaque | 2% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 2 3/3 | 119201 | 1 | 2 | 3/3 | 4 SkillPoint | Attaque | 2% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 2 1/3 | 119202 | 1 | 2 | 1/3 | 2 SkillPoint | Défense | 2% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 2 2/3 | 119202 | 1 | 2 | 2/3 | 3 SkillPoint | Défense | 2% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 2 3/3 | 119202 | 1 | 2 | 3/3 | 4 SkillPoint | Défense | 2% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 2 1/3 | 119203 | 1 | 2 | 1/3 | 2 SkillPoint | PV | 2% | 2% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 2 2/3 | 119203 | 1 | 2 | 2/3 | 3 SkillPoint | PV | 2% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 2 3/3 | 119203 | 1 | 2 | 3/3 | 4 SkillPoint | PV | 2% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 3 1/3 | 119301 | 2 | 3 | 1/3 | 2 SkillPoint | Attaque | 3% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 3 2/3 | 119301 | 2 | 3 | 2/3 | 3 SkillPoint | Attaque | 3% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 3 3/3 | 119301 | 2 | 3 | 3/3 | 4 SkillPoint | Attaque | 3% | 9% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 3 1/3 | 119302 | 2 | 3 | 1/3 | 2 SkillPoint | Défense | 3% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 3 2/3 | 119302 | 2 | 3 | 2/3 | 3 SkillPoint | Défense | 3% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 3 3/3 | 119302 | 2 | 3 | 3/3 | 4 SkillPoint | Défense | 3% | 9% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 3 1/3 | 119303 | 2 | 3 | 1/3 | 2 SkillPoint | PV | 3% | 3% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 3 2/3 | 119303 | 2 | 3 | 2/3 | 3 SkillPoint | PV | 3% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 3 3/3 | 119303 | 2 | 3 | 3/3 | 4 SkillPoint | PV | 3% | 9% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 4 1/3 | 119401 | 3 | 4 | 1/3 | 3 SkillPoint | Attaque | 4% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 4 2/3 | 119401 | 3 | 4 | 2/3 | 4 SkillPoint | Attaque | 4% | 8% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 4 3/3 | 119401 | 3 | 4 | 3/3 | 5 SkillPoint | Attaque | 4% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 4 1/3 | 119402 | 3 | 4 | 1/3 | 3 SkillPoint | Défense | 4% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 4 2/3 | 119402 | 3 | 4 | 2/3 | 4 SkillPoint | Défense | 4% | 8% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 4 3/3 | 119402 | 3 | 4 | 3/3 | 5 SkillPoint | Défense | 4% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 4 1/3 | 119403 | 3 | 4 | 1/3 | 3 SkillPoint | PV | 4% | 4% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 4 2/3 | 119403 | 3 | 4 | 2/3 | 4 SkillPoint | PV | 4% | 8% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 4 3/3 | 119403 | 3 | 4 | 3/3 | 5 SkillPoint | PV | 4% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 5 1/3 | 119501 | 4 | 5 | 1/3 | 3 SkillPoint | Attaque | 5% | 5% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 5 2/3 | 119501 | 4 | 5 | 2/3 | 4 SkillPoint | Attaque | 5% | 10% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 5 3/3 | 119501 | 4 | 5 | 3/3 | 5 SkillPoint | Attaque | 5% | 15% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 5 1/3 | 119502 | 4 | 5 | 1/3 | 3 SkillPoint | Défense | 5% | 5% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 5 2/3 | 119502 | 4 | 5 | 2/3 | 4 SkillPoint | Défense | 5% | 10% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 5 3/3 | 119502 | 4 | 5 | 3/3 | 5 SkillPoint | Défense | 5% | 15% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 5 1/3 | 119503 | 4 | 5 | 1/3 | 3 SkillPoint | PV | 5% | 5% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 5 2/3 | 119503 | 4 | 5 | 2/3 | 4 SkillPoint | PV | 5% | 10% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 5 3/3 | 119503 | 4 | 5 | 3/3 | 5 SkillPoint | PV | 5% | 15% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 6 1/3 | 119601 | 5 | 6 | 1/3 | 3 SkillPoint | Attaque | 6% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 6 2/3 | 119601 | 5 | 6 | 2/3 | 4 SkillPoint | Attaque | 6% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Attaque augmentée 6 3/3 | 119601 | 5 | 6 | 3/3 | 5 SkillPoint | Attaque | 6% | 18% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 6 1/3 | 119602 | 5 | 6 | 1/3 | 3 SkillPoint | Défense | 6% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 6 2/3 | 119602 | 5 | 6 | 2/3 | 4 SkillPoint | Défense | 6% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | Défense augmentée 6 3/3 | 119602 | 5 | 6 | 3/3 | 5 SkillPoint | Défense | 6% | 18% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 6 1/3 | 119603 | 5 | 6 | 1/3 | 3 SkillPoint | PV | 6% | 6% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 6 2/3 | 119603 | 5 | 6 | 2/3 | 4 SkillPoint | PV | 6% | 12% | FORTEMENT PROBABLE |
| Groupe 9 |  | Groupe 9 | PV augmentés 6 3/3 | 119603 | 5 | 6 | 3/3 | 5 SkillPoint | PV | 6% | 18% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 1 1/3 | 1110101 | 0 | 1 | 1/3 | 2 SkillPoint | Taux de coup critique | 1% | 1% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 1 2/3 | 1110101 | 0 | 1 | 2/3 | 3 SkillPoint | Taux de coup critique | 1% | 2% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 1 3/3 | 1110101 | 0 | 1 | 3/3 | 4 SkillPoint | Taux de coup critique | 1% | 3% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 1 1/3 | 1110102 | 0 | 1 | 1/3 | 2 SkillPoint | Dégâts de coup critique | 1% | 1% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 1 2/3 | 1110102 | 0 | 1 | 2/3 | 3 SkillPoint | Dégâts de coup critique | 1% | 2% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 1 3/3 | 1110102 | 0 | 1 | 3/3 | 4 SkillPoint | Dégâts de coup critique | 1% | 3% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 1 1/3 | 1110103 | 0 | 1 | 1/3 | 2 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 1 2/3 | 1110103 | 0 | 1 | 2/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 1 3/3 | 1110103 | 0 | 1 | 3/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 2 1/3 | 1110201 | 1 | 2 | 1/3 | 2 SkillPoint | Taux de coup critique | 2% | 2% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 2 2/3 | 1110201 | 1 | 2 | 2/3 | 3 SkillPoint | Taux de coup critique | 2% | 4% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 2 3/3 | 1110201 | 1 | 2 | 3/3 | 4 SkillPoint | Taux de coup critique | 2% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 2 1/3 | 1110202 | 1 | 2 | 1/3 | 2 SkillPoint | Dégâts de coup critique | 2% | 2% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 2 2/3 | 1110202 | 1 | 2 | 2/3 | 3 SkillPoint | Dégâts de coup critique | 2% | 4% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 2 3/3 | 1110202 | 1 | 2 | 3/3 | 4 SkillPoint | Dégâts de coup critique | 2% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 2 1/3 | 1110203 | 1 | 2 | 1/3 | 2 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 2 2/3 | 1110203 | 1 | 2 | 2/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 2 3/3 | 1110203 | 1 | 2 | 3/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 3 1/3 | 1110301 | 2 | 3 | 1/3 | 2 SkillPoint | Taux de coup critique | 3% | 3% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 3 2/3 | 1110301 | 2 | 3 | 2/3 | 3 SkillPoint | Taux de coup critique | 3% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 3 3/3 | 1110301 | 2 | 3 | 3/3 | 4 SkillPoint | Taux de coup critique | 3% | 9% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 3 1/3 | 1110302 | 2 | 3 | 1/3 | 2 SkillPoint | Dégâts de coup critique | 3% | 3% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 3 2/3 | 1110302 | 2 | 3 | 2/3 | 3 SkillPoint | Dégâts de coup critique | 3% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 3 3/3 | 1110302 | 2 | 3 | 3/3 | 4 SkillPoint | Dégâts de coup critique | 3% | 9% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 3 1/3 | 1110303 | 2 | 3 | 1/3 | 2 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 3 2/3 | 1110303 | 2 | 3 | 2/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 3 3/3 | 1110303 | 2 | 3 | 3/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 4 1/3 | 1110401 | 3 | 4 | 1/3 | 3 SkillPoint | Taux de coup critique | 4% | 4% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 4 2/3 | 1110401 | 3 | 4 | 2/3 | 4 SkillPoint | Taux de coup critique | 4% | 8% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 4 3/3 | 1110401 | 3 | 4 | 3/3 | 5 SkillPoint | Taux de coup critique | 4% | 12% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 4 1/3 | 1110402 | 3 | 4 | 1/3 | 3 SkillPoint | Dégâts de coup critique | 4% | 4% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 4 2/3 | 1110402 | 3 | 4 | 2/3 | 4 SkillPoint | Dégâts de coup critique | 4% | 8% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 4 3/3 | 1110402 | 3 | 4 | 3/3 | 5 SkillPoint | Dégâts de coup critique | 4% | 12% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 4 1/3 | 1110403 | 3 | 4 | 1/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 4 2/3 | 1110403 | 3 | 4 | 2/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 4 3/3 | 1110403 | 3 | 4 | 3/3 | 5 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 5 1/3 | 1110501 | 4 | 5 | 1/3 | 3 SkillPoint | Taux de coup critique | 5% | 5% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 5 2/3 | 1110501 | 4 | 5 | 2/3 | 4 SkillPoint | Taux de coup critique | 5% | 10% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 5 3/3 | 1110501 | 4 | 5 | 3/3 | 5 SkillPoint | Taux de coup critique | 5% | 15% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 5 1/3 | 1110502 | 4 | 5 | 1/3 | 3 SkillPoint | Dégâts de coup critique | 5% | 5% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 5 2/3 | 1110502 | 4 | 5 | 2/3 | 4 SkillPoint | Dégâts de coup critique | 5% | 10% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 5 3/3 | 1110502 | 4 | 5 | 3/3 | 5 SkillPoint | Dégâts de coup critique | 5% | 15% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 5 1/3 | 1110503 | 4 | 5 | 1/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 5 2/3 | 1110503 | 4 | 5 | 2/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 5 3/3 | 1110503 | 4 | 5 | 3/3 | 5 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 6 1/3 | 1110601 | 5 | 6 | 1/3 | 3 SkillPoint | Taux de coup critique | 6% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 6 2/3 | 1110601 | 5 | 6 | 2/3 | 4 SkillPoint | Taux de coup critique | 6% | 12% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Taux de coup critique 6 3/3 | 1110601 | 5 | 6 | 3/3 | 5 SkillPoint | Taux de coup critique | 6% | 18% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 6 1/3 | 1110602 | 5 | 6 | 1/3 | 3 SkillPoint | Dégâts de coup critique | 6% | 6% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 6 2/3 | 1110602 | 5 | 6 | 2/3 | 4 SkillPoint | Dégâts de coup critique | 6% | 12% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Dégâts de coup critique 6 3/3 | 1110602 | 5 | 6 | 3/3 | 5 SkillPoint | Dégâts de coup critique | 6% | 18% | FORTEMENT PROBABLE |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 6 1/3 | 1110603 | 5 | 6 | 1/3 | 3 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 6 2/3 | 1110603 | 5 | 6 | 2/3 | 4 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| Groupe 10 |  | Groupe 10 | Pénétration de défense 6 3/3 | 1110603 | 5 | 6 | 3/3 | 5 SkillPoint | Pénétration de défense | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA |
| GSSkillTree | Épée | Cœur d'acier | Attaque augmentée 1/3 | 2150401 | 3 | 4 | 1/3 | 2 WeaponPoint | Attaque | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Cœur d'acier | Attaque augmentée 2/3 | 2150401 | 3 | 4 | 2/3 | 2 WeaponPoint | Attaque | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Cœur d'acier | Attaque augmentée 3/3 | 2150401 | 3 | 4 | 3/3 | 2 WeaponPoint | Attaque | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Cœur d'acier | Défense augmentée 1/3 | 2150403 | 3 | 4 | 1/3 | 2 WeaponPoint | Défense | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Cœur d'acier | Défense augmentée 2/3 | 2150403 | 3 | 4 | 2/3 | 2 WeaponPoint | Défense | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Cœur d'acier | Défense augmentée 3/3 | 2150403 | 3 | 4 | 3/3 | 2 WeaponPoint | Défense | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Précision augmentée 1/3 | 2151302 | 2 | 3 | 1/3 | 2 WeaponPoint | Précision | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Précision augmentée 2/3 | 2151302 | 2 | 3 | 2/3 | 2 WeaponPoint | Précision | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Précision augmentée 3/3 | 2151302 | 2 | 3 | 3/3 | 2 WeaponPoint | Précision | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Pénétration de défense augmentée 1/3 | 2151402 | 3 | 4 | 1/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Pénétration de défense augmentée 2/3 | 2151402 | 3 | 4 | 2/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Épée | Résistance à la lame | Pénétration de défense augmentée 3/3 | 2151402 | 3 | 4 | 3/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 1/3 | 2252101 | 0 | 1 | 1/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 2/3 | 2252101 | 0 | 1 | 2/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 3/3 | 2252101 | 0 | 1 | 3/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 1/3 | 2252103 | 0 | 1 | 1/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 2/3 | 2252103 | 0 | 1 | 2/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 3/3 | 2252103 | 0 | 1 | 3/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 1/3 | 2252301 | 2 | 3 | 1/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 2/3 | 2252301 | 2 | 3 | 2/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Taux de coup critique augmenté 3/3 | 2252301 | 2 | 3 | 3/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 1/3 | 2252303 | 2 | 3 | 1/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 2/3 | 2252303 | 2 | 3 | 2/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Dégâts de coup critique augmentés 3/3 | 2252303 | 2 | 3 | 3/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Dague | Plaie mortelle | Amplification de la douleur | 2252401 | 3 | 4 | 1/1 | 3 WeaponPoint | Dégâts conditionnels | 3% | 3% | FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Taux de coup critique augmenté 1/3 | 2254202 | 1 | 2 | 1/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Taux de coup critique augmenté 2/3 | 2254202 | 1 | 2 | 2/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Taux de coup critique augmenté 3/3 | 2254202 | 1 | 2 | 3/3 | 2 WeaponPoint | Taux de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Dégâts de coup critique augmentés 1/3 | 2254402 | 3 | 4 | 1/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Dégâts de coup critique augmentés 2/3 | 2254402 | 3 | 4 | 2/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée concentrée | Dégâts de coup critique augmentés 3/3 | 2254402 | 3 | 4 | 3/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Précision augmentée 1/3 | 2255202 | 1 | 2 | 1/3 | 2 WeaponPoint | Précision | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Précision augmentée 2/3 | 2255202 | 1 | 2 | 2/3 | 2 WeaponPoint | Précision | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Précision augmentée 3/3 | 2255202 | 1 | 2 | 3/3 | 2 WeaponPoint | Précision | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Pénétration de défense augmentée 1/3 | 2255402 | 3 | 4 | 1/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Pénétration de défense augmentée 2/3 | 2255402 | 3 | 4 | 2/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Pénétration de défense augmentée 3/3 | 2255402 | 3 | 4 | 3/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arc | Visée sécurisée | Visée sécurisée | 2255501 | 4 | 5 | 1/1 | 3 WeaponPoint | Dégâts infligés | 5.5% | 5.5% | FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 1/3 | 2357202 | 1 | 2 | 1/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 2/3 | 2357202 | 1 | 2 | 2/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 3/3 | 2357202 | 1 | 2 | 3/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 1/3 | 2357402 | 3 | 4 | 1/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 2/3 | 2357402 | 3 | 4 | 2/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à feu | Visée patiente | Pénétration de défense augmentée 3/3 | 2357402 | 3 | 4 | 3/3 | 2 WeaponPoint | Pénétration de défense | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Focalisateur | Énergie de mana fluide | Augmente les PM max 1/3 | 2359402 | 2 | 3 | 1/3 | 2 WeaponPoint | PM max | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| GSSkillTree | Focalisateur | Énergie de mana fluide | Augmente les PM max 2/3 | 2359402 | 2 | 3 | 2/3 | 2 WeaponPoint | PM max | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| GSSkillTree | Focalisateur | Énergie de mana fluide | Augmente les PM max 3/3 | 2359402 | 2 | 3 | 3/3 | 2 WeaponPoint | PM max | NON DÉTERMINÉ | NON DÉTERMINÉ | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Fer-de-lance dévié | Attaque pulvérisante | 2460403 | 3 | 4 | 1/1 | 3 WeaponPoint | Dégâts conditionnels | 3% | 3% | FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Fer-de-lance dévié | Attaque pulvérisante | 2460403 | 3 | 4 | 1/1 | 3 WeaponPoint | Dégâts conditionnels | 3% | 3% | FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Physique endurant 1/3 | 2461401 | 2 | 3 | 1/3 | 3 WeaponPoint | Réduction des dégâts | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Physique endurant 2/3 | 2461401 | 2 | 3 | 2/3 | 3 WeaponPoint | Réduction des dégâts | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Physique endurant 3/3 | 2461401 | 2 | 3 | 3/3 | 3 WeaponPoint | Réduction des dégâts | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Amélioration des PV 1/3 | 2461403 | 2 | 3 | 1/3 | 2 WeaponPoint | PV | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Amélioration des PV 2/3 | 2461403 | 2 | 3 | 2/3 | 2 WeaponPoint | PV | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme d'hast | Frappe brutale | Amélioration des PV 3/3 | 2461403 | 2 | 3 | 3/3 | 2 WeaponPoint | PV | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Ruée de berserker | Dégâts de coup critique augmentés 1/3 | 2462202 | 1 | 2 | 1/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.25% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Ruée de berserker | Dégâts de coup critique augmentés 2/3 | 2462202 | 1 | 2 | 2/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Ruée de berserker | Dégâts de coup critique augmentés 3/3 | 2462202 | 1 | 2 | 3/3 | 2 WeaponPoint | Dégâts de coup critique | 0.25% | 0.75% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Ruée de berserker | Posture offensive | 2462501 | 3 | 5 | 1/1 | 3 WeaponPoint | Réduction des dégâts | -2.5% | -2.5% | FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Ruée de berserker | Posture offensive | 2462501 | 3 | 5 | 1/1 | 3 WeaponPoint | Dégâts infligés | 4% | 4% | FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Précision augmentée 1/3 | 2463202 | 1 | 2 | 1/3 | 2 WeaponPoint | Précision | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Précision augmentée 2/3 | 2463202 | 1 | 2 | 2/3 | 2 WeaponPoint | Précision | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Précision augmentée 3/3 | 2463202 | 1 | 2 | 3/3 | 2 WeaponPoint | Précision | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Attaque augmentée 1/3 | 2463302 | 2 | 3 | 1/3 | 2 WeaponPoint | Attaque | 0.5% | 0.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Attaque augmentée 2/3 | 2463302 | 2 | 3 | 2/3 | 2 WeaponPoint | Attaque | 0.5% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| GSSkillTree | Arme à deux mains | Contre-offensive et restauration | Attaque augmentée 3/3 | 2463302 | 2 | 3 | 3/3 | 2 WeaponPoint | Attaque | 0.5% | 1.5% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 1/3 | 31100102 | 0 | 1 | 1/3 | 1 SpecialPoint | Attaque | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 2/3 | 31100102 | 0 | 1 | 2/3 | 1 SpecialPoint | Attaque | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 3/3 | 31100102 | 0 | 1 | 3/3 | 1 SpecialPoint | Attaque | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 1/3 | 31100201 | 1 | 2 | 1/3 | 1 SpecialPoint | Défense | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 2/3 | 31100201 | 1 | 2 | 2/3 | 1 SpecialPoint | Défense | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 3/3 | 31100201 | 1 | 2 | 3/3 | 1 SpecialPoint | Défense | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 1/3 | 31100203 | 1 | 2 | 1/3 | 1 SpecialPoint | PV | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 2/3 | 31100203 | 1 | 2 | 2/3 | 1 SpecialPoint | PV | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 3/3 | 31100203 | 1 | 2 | 3/3 | 1 SpecialPoint | PV | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 1/3 | 31100302 | 2 | 3 | 1/3 | 1 SpecialPoint | Attaque | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 2/3 | 31100302 | 2 | 3 | 2/3 | 1 SpecialPoint | Attaque | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 3/3 | 31100302 | 2 | 3 | 3/3 | 1 SpecialPoint | Attaque | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 1/3 | 31100401 | 3 | 4 | 1/3 | 1 SpecialPoint | Défense | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 2/3 | 31100401 | 3 | 4 | 2/3 | 1 SpecialPoint | Défense | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 3/3 | 31100401 | 3 | 4 | 3/3 | 1 SpecialPoint | Défense | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 1/3 | 31100403 | 3 | 4 | 1/3 | 1 SpecialPoint | PV | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 2/3 | 31100403 | 3 | 4 | 2/3 | 1 SpecialPoint | PV | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 3/3 | 31100403 | 3 | 4 | 3/3 | 1 SpecialPoint | PV | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 1/3 | 31100502 | 4 | 5 | 1/3 | 1 SpecialPoint | Attaque | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 2/3 | 31100502 | 4 | 5 | 2/3 | 1 SpecialPoint | Attaque | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Attaque augmentée 3/3 | 31100502 | 4 | 5 | 3/3 | 1 SpecialPoint | Attaque | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 1/3 | 31100601 | 5 | 6 | 1/3 | 1 SpecialPoint | Défense | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 2/3 | 31100601 | 5 | 6 | 2/3 | 1 SpecialPoint | Défense | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | Défense augmentée 3/3 | 31100601 | 5 | 6 | 3/3 | 1 SpecialPoint | Défense | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 1/3 | 31100603 | 5 | 6 | 1/3 | 1 SpecialPoint | PV | 1% | 1% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 2/3 | 31100603 | 5 | 6 | 2/3 | 1 SpecialPoint | PV | 1% | 2% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle I | PV augmentés 3/3 | 31100603 | 5 | 6 | 3/3 | 1 SpecialPoint | PV | 1% | 3% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 1/3 | 31101102 | 0 | 1 | 1/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 2/3 | 31101102 | 0 | 1 | 2/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 3/3 | 31101102 | 0 | 1 | 3/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 1/3 | 31101201 | 1 | 2 | 1/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 2/3 | 31101201 | 1 | 2 | 2/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 3/3 | 31101201 | 1 | 2 | 3/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 1/3 | 31101203 | 1 | 2 | 1/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 2/3 | 31101203 | 1 | 2 | 2/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 3/3 | 31101203 | 1 | 2 | 3/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 1/3 | 31101302 | 2 | 3 | 1/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 2/3 | 31101302 | 2 | 3 | 2/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 3/3 | 31101302 | 2 | 3 | 3/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 1/3 | 31101401 | 3 | 4 | 1/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 2/3 | 31101401 | 3 | 4 | 2/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 3/3 | 31101401 | 3 | 4 | 3/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 1/3 | 31101403 | 3 | 4 | 1/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 2/3 | 31101403 | 3 | 4 | 2/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Pénétration de défense augmentée 3/3 | 31101403 | 3 | 4 | 3/3 | 1 SpecialPoint | Pénétration de défense | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 1/3 | 31101501 | 4 | 5 | 1/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 2/3 | 31101501 | 4 | 5 | 2/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 3/3 | 31101501 | 4 | 5 | 3/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 1/3 | 31101503 | 4 | 5 | 1/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 2/3 | 31101503 | 4 | 5 | 2/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Dégâts subis réduits 3/3 | 31101503 | 4 | 5 | 3/3 | 1 SpecialPoint | Réduction des dégâts | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 1/3 | 31101601 | 5 | 6 | 1/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 2/3 | 31101601 | 5 | 6 | 2/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 3/3 | 31101601 | 5 | 6 | 3/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 1/3 | 31101603 | 5 | 6 | 1/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.33% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 2/3 | 31101603 | 5 | 6 | 2/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.66% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| LordSkillTree | Physique | Amélioration corporelle II | Taux de coup critique augmenté 3/3 | 31101603 | 5 | 6 | 3/3 | 1 SpecialPoint | Taux de coup critique | 0.33% | 0.99% | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

## Ce que les données confirment

- **CONFIRMÉ PAR LES GAMEDATA**: `NodeValue` référence un buff ou une compétence; pour les talents de stat, le buff contient le type d'effet et la valeur brute.
- **FORTEMENT PROBABLE**: pour les stats `AttFR`, `ArmFR`, `CriticalP`, `CriDamP`, `DamP`, `PrecisionP` et `IncreaseMHP`, la valeur affichée utilise `raw * 0.01%`, car de nombreux textes de buffs utilisent explicitement `{...,0.01}%`.
- **FORTEMENT PROBABLE**: quand `NodeMaxLevel=3` et que le buff a une seule valeur brute, chaque rang réapplique le même gain marginal; le cumul est donc `raw * rang`.
- **NON DÉTERMINÉ**: les données GameData seules ne prouvent pas si plusieurs sources de même stat sont additionnées avant ou après d'autres multiplicateurs runtime.
- **NON DÉTERMINÉ**: la base exacte affectée par `AttFR` est nommée comme Attaque finale/ratio dans les tables (`FR`), mais l'ordre exact par rapport à attaque de base, arme, artefacts ou buffs temporaires n'est pas prouvé ici.
- Les colonnes `LogicalTalentID`, `LogicalTalentName`, `LogicalRank` et `LogicalGroupingEvidence` séparent nœud GameData, talent logique et rang logique sans fusionner par nom.
- Quand deux lignes CSV ont le même `NodeID`, le même rang et le même effet, cela correspond à plusieurs slots de buff/special state dans `ChComBuff`; les colonnes demandées ne prévoient pas de champ slot/cible séparé.
- Les groupes `9` et `10` existent dans `CharPCSkillTreeNode`, mais aucun sous-onglet de `CharPCSkillTreelSubTab` ne les référence explicitement; ils restent donc libellés `Groupe 9/10` au lieu d'être rattachés artificiellement.

## CharPCStatAbility

`CharPCStatAbility` contient des courbes liées aux attributs de Jinwoo (`StrAbilityRate`, `VitAbilityRate`, etc.). Aucune liaison directe `NodeID -> CharPCStatAbility.ID` n'est présente dans `CharPCSkillTreeNode`; elle est donc référencée comme contexte, pas utilisée pour inventer des valeurs de talent.
