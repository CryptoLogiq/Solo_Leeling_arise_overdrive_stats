# Sung Jinwoo - Point Progression

Sources primaires: `ChSJWLv` pour les gains par niveau, `SysConst` pour la limite de niveau, `sjw_talent_tree.json` pour les coûts de talents.

## Résumé

- Niveau max SJW: `75` (`ChSJWLv.Level` max, recoupé avec `SysConst.Common.SungjinwooMaxLevel`).
- Niveau de départ SJW: `1` (`SysConst.BeginSetting.SJWLevel`).
- Exemple demandé niveau 30: Skill `18`, Weapon `20`, Special `20`, Identity `0`.
- Maximum niveau 75: Skill `48`, Weapon `50`, Special `50`, Identity `0`.

Les valeurs de `ChSJWLv` sont traitées comme des gains marginaux par niveau; les totaux ci-dessous sont calculés par cumul.

## Sources par monnaie

| Monnaie | Source gain niveau | Pattern | Total max | Confiance | WIP |
|---|---|---|---:|---|---|
| `SkillPoint` | `ChSJWLv.SkillPoint` | +2 aux niveaux 4, 7, 10, 13, 16, 19, ... 70, 73 | 48 | CONFIRMÉ PAR LES GAMEDATA | non |
| `WeaponPoint` | `ChSJWLv.WeaponPoint` | +2 aux niveaux 2, 5, 8, 11, 14, 17, ... 71, 74 | 50 | CONFIRMÉ PAR LES GAMEDATA | non |
| `SpecialPoint` | `ChSJWLv.SpecialPoint` | +2 aux niveaux 3, 6, 9, 12, 15, 18, ... 72, 75 | 50 | CONFIRMÉ PAR LES GAMEDATA | non |
| `IdentityPoint` | `ChSJWLv.IdentityPoint` | aucun gain par niveau trouvé | 0 | CONFIRMÉ POUR LE LEVEL-UP; SOURCE D'ACQUISITION NON DÉTERMINÉE | oui |

## Paliers utiles

| Niveau | SkillPoint | WeaponPoint | SpecialPoint | IdentityPoint |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 30 | 18 | 20 | 20 | 0 |
| 75 | 48 | 50 | 50 | 0 |

## Demande brute des talents

Cette table additionne les coûts connus de tous les rangs de talents présents dans le modèle canonique. Elle sert à comparer un budget maximum à une demande brute, pas à valider une route optimale.

| Monnaie | Coût connu total | Rangs connus | Rangs coût WIP | Confiance |
|---|---:|---:|---:|---|
| `IdentityPoint` | 4 | 4 | 0 | CALCULÉ À PARTIR DES GAMEDATA |
| `SkillPoint` | 662 | 189 | 0 | CALCULÉ À PARTIR DES GAMEDATA |
| `SpecialPoint` | 76 | 38 | 38 | CALCULÉ SUR COÛTS CONNUS; COÛTS PARTIELLEMENT NON DÉTERMINÉS |
| `WeaponPoint` | 277 | 99 | 76 | CALCULÉ SUR COÛTS CONNUS; COÛTS PARTIELLEMENT NON DÉTERMINÉS |

## Points non résolus

- `IdentityPoint`: 4 nœuds de talent consomment chacun 1 point, mais `ChSJWLv.IdentityPoint` reste à 0 du niveau 1 au niveau 75. La source d'acquisition n'est donc pas le level-up dans cette table et reste WIP.
- `TotalExp`: le champ existe dans `ChSJWLv`, mais le décodage actuel produit des flottants extrêmement petits. Ne pas utiliser cette courbe XP pour planifier tant qu'elle n'est pas vérifiée.
- `ProvideSkillSet`: présent dans `ChSJWLv`, mais vaut 0 sur les lignes décodées actuelles.

CSV complet: `analysis/csv/sjw_point_progression.csv`
JSON planner: `analysis/data/sjw_point_progression.json`
