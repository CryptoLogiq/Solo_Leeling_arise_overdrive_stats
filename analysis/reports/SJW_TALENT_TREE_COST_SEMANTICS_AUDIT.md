# SJW Talent Tree Cost Semantics Audit

Audit ciblé sur `LevelUpCostValue` après contradiction in-game observée sur `LordSkillTree` / `Physique`.

## Conclusion

- Règle runtime de coût par rang: **NON DÉTERMINÉE** pour les nœuds multi-rangs dont `LevelUpCostValue` ne contient qu'une seule valeur.
- Le codec lit bien la valeur brute complète `[1]` pour Physique; ce n'est pas une liste tronquée.
- Le coût interprété n'est plus exporté comme `1 SpecialPoint` par rang pour ces cas; la valeur raw reste conservée séparément.

## Tables contrôlées

- `CharPCSkillTreeNode.byte`: NodeID, parents, placement, `NodeMaxLevel`, `LevelUpCost`, `LevelUpCostValue`.
- `ChComBuff.byte`: effets référencés par `NodeValue`.
- `CharPCSkillTreelMainTab.byte` / `CharPCSkillTreelSubTab.byte`: rattachement d'arbre et section.
- `ChSJWLv.byte` / `SysAccLv.byte`: attribution de points par niveau/compte, sans liaison de coût par NodeID.
- `ContentsUnlock.byte`: conditions d'accès de contenu, sans coût de rang Physique.

## Patterns multi-rangs à liste de coût singleton

| Monnaie raw | Max rank | Raw LevelUpCostValue | Nœuds |
|---|---:|---|---:|
| SpecialPoint | 3 | `[1]` | 19 |
| WeaponPoint | 3 | `[2]` | 20 |
| WeaponPoint | 3 | `[3]` | 18 |

## Physique / NodeGroups 100 et 101

| NodeID | Groupe | Row | Col | Max rank | LevelUpCost | Raw LevelUpCostValue | Parents | NodeValue | IconResource |
|---:|---:|---:|---:|---:|---|---|---|---:|---|
| 31100102 | 100 | 1 | 3 | 3 | SpecialPoint | `[1]` | `[]` | 200000086 | st_attack_add |
| 31100201 | 100 | 2 | 2 | 3 | SpecialPoint | `[1]` | `[31100102]` | 200000087 | st_AddArm |
| 31100203 | 100 | 2 | 4 | 3 | SpecialPoint | `[1]` | `[31100102]` | 200000088 | st_AddMHP |
| 31100302 | 100 | 3 | 3 | 3 | SpecialPoint | `[1]` | `[31100201,31100203]` | 200000089 | st_attack_add |
| 31100401 | 100 | 4 | 2 | 3 | SpecialPoint | `[1]` | `[31100302]` | 200000090 | st_AddArm |
| 31100403 | 100 | 4 | 4 | 3 | SpecialPoint | `[1]` | `[31100302]` | 200000091 | st_AddMHP |
| 31100502 | 100 | 5 | 3 | 3 | SpecialPoint | `[1]` | `[31100401,31100403]` | 200000092 | st_attack_add |
| 31100601 | 100 | 6 | 2 | 3 | SpecialPoint | `[1]` | `[31100502]` | 200000093 | st_AddArm |
| 31100603 | 100 | 6 | 4 | 3 | SpecialPoint | `[1]` | `[31100502]` | 200000094 | st_AddMHP |
| 31101102 | 101 | 1 | 3 | 3 | SpecialPoint | `[1]` | `[]` | 200000095 | st_critical_damage_add |
| 31101201 | 101 | 2 | 2 | 3 | SpecialPoint | `[1]` | `[31101102]` | 200000096 | st_ArmPen |
| 31101203 | 101 | 2 | 4 | 3 | SpecialPoint | `[1]` | `[31101102]` | 200000097 | st_ArmPen |
| 31101302 | 101 | 3 | 3 | 3 | SpecialPoint | `[1]` | `[31101201,31101203]` | 200000098 | st_critical_damage_add |
| 31101401 | 101 | 4 | 2 | 3 | SpecialPoint | `[1]` | `[31101302]` | 200000099 | st_ArmPen |
| 31101403 | 101 | 4 | 4 | 3 | SpecialPoint | `[1]` | `[31101302]` | 200000100 | st_ArmPen |
| 31101501 | 101 | 5 | 2 | 3 | SpecialPoint | `[1]` | `[31101401]` | 200000101 | st_DamRedu |
| 31101503 | 101 | 5 | 4 | 3 | SpecialPoint | `[1]` | `[31101403]` | 200000102 | st_DamRedu |
| 31101601 | 101 | 6 | 2 | 3 | SpecialPoint | `[1]` | `[31101501]` | 200000103 | st_critical_damage_add |
| 31101603 | 101 | 6 | 4 | 3 | SpecialPoint | `[1]` | `[31101503]` | 200000104 | st_critical_damage_add |

## Vérification codec ciblée

| NodeID | Max rank | LevelUpCost | Raw LevelUpCostValue | Remarque |
|---:|---:|---|---|---|
| 31100102 | 3 | SpecialPoint | `[1]` | coût par rang non prouvé |
| 31100302 | 3 | SpecialPoint | `[1]` | coût par rang non prouvé |
| 31100502 | 3 | SpecialPoint | `[1]` | coût par rang non prouvé |
| 31100601 | 3 | SpecialPoint | `[1]` | coût par rang non prouvé |
| 31101102 | 3 | SpecialPoint | `[1]` | coût par rang non prouvé |
| 119101 | 3 | SkillPoint | `[2,3,4]` | une valeur explicite par rang |
| 2150401 | 3 | WeaponPoint | `[2]` | coût par rang non prouvé |

## Checklist in-game à relever

| NodeID | Nom généré | Branche | Position UI | Rang à relever | Raw LevelUpCostValue | Coût affiché in-game |
|---:|---|---|---|---|---|---|
| 31100102 | Attaque augmentée | Amélioration corporelle I | R1 / C3 | I, II, III | `[1]` | à relever |
| 31100201 | Défense augmentée | Amélioration corporelle I | R2 / C2 | I, II, III | `[1]` | à relever |
| 31100302 | Attaque augmentée | Amélioration corporelle I | R3 / C3 | I, II, III | `[1]` | à relever |
| 31100502 | Attaque augmentée | Amélioration corporelle I | R5 / C3 | I, II, III | `[1]` | à relever |
| 31100601 | Défense augmentée | Amélioration corporelle I | R6 / C2 | I, II, III | `[1]` | à relever |
| 31101102 | Taux de coup critique augmenté | Amélioration corporelle II | R1 / C3 | I, II, III | `[1]` | à relever |
| 31101401 | Pénétration de défense augmentée | Amélioration corporelle II | R4 / C2 | I, II, III | `[1]` | à relever |
| 31101603 | Taux de coup critique augmenté | Amélioration corporelle II | R6 / C4 | I, II, III | `[1]` | à relever |
