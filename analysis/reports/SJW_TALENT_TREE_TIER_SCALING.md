# Résumé

Cette passe sépare explicitement la **profondeur de progression** calculée depuis les parents, la **rangée visuelle** (`NodeTierY`) et le **rang réel** (`NodeMaxLevel`). Les familles sont regroupées par arbre/sous-onglet/branche/stat/nom normalisé, puis comparées sur les nœuds distincts au rang 1.

CSV: `analysis/csv/sjw_talent_tier_scaling.csv`
Lignes numériques exportées: 323.
Familles analysées: 88.

# Profondeur, rangée visuelle et rang

- Profondeur de progression: profondeur réelle du nœud dans le graphe Parent/Enfant.
- Rangée visuelle: position verticale réelle du nœud dans `CharPCSkillTreeNode.NodeTierY`.
- Rang: niveau interne d'un même nœud via `NodeMaxLevel`; il est exporté séparément dans la colonne `Rank`.
- Deux nœuds avec la même stat à deux rangées visuelles différentes sont traités comme des talents distincts, même si leur nom se ressemble.

# Vérification de l'hypothèse de lissage

| Classification | Familles |
|---|---:|
| NON DÉTERMINÉ | 83 |
| D. NON COMPARABLE / IRRÉGULIER | 5 |

## Statistiques globales sur familles répétées

| Mesure | Nombre |
|---|---:|
| Familles répétées analysées | 16 |
| coût et gain proportionnels | 0 |
| rendement constant partiel | 0 |
| coût fixe et gain fixe | 0 |
| coût fixe, gain variable | 0 |
| gain fixe, coût variable | 9 |
| coût croissant, gain moins rapide | 0 |
| coût croissant, gain plus rapide | 0 |
| effet différent selon la rangée visuelle | 0 |
| non comparables directement | 7 |

Conclusion globale: l'observation est **vraie seulement pour certains nœuds**. Plusieurs familles en pourcentage gardent un rendement direct constant, mais les principales séries `+1/+2/+3...` observées ici deviennent irrégulières quand on vérifie toutes leurs rangées visuelles. Les valeurs brutes sans unité démontrée restent non comparables.

# Attaque

## Vérification de l'hypothèse Attaque

| NodeID | Profondeur | Rangée visuelle | Position | Coût | Chemin requis | RawValue | DisplayValue | Gain/point | Parent | BuffID | Stat type | Pattern | Conclusion |
|---:|---:|---:|---:|---|---:|---:|---:|---:|---|---:|---|---|---|
| 111601 | 5 | 6 | 2 | 3 SkillPoint | 23 | 80 | 0.8% | 0.2667 | 111501 | 90000004 | AttFR | NON DÉTERMINÉ | isolé/non comparable |
| 119101 | 0 | 1 | 2 | 2 SkillPoint | 0 | 100 | 1% | 0.5 |  | 100000001 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 119201 | 1 | 2 | 2 | 2 SkillPoint | 2 | 200 | 2% | 1 | 119101 | 100000004 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 119301 | 2 | 3 | 2 | 2 SkillPoint | 4 | 300 | 3% | 1.5 | 119201 | 100000007 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 119401 | 3 | 4 | 2 | 3 SkillPoint | 6 | 400 | 4% | 1.3333 | 119301 | 100000010 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 119501 | 4 | 5 | 2 | 3 SkillPoint | 9 | 500 | 5% | 1.6667 | 119401 | 100000013 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 119601 | 5 | 6 | 2 | 3 SkillPoint | 12 | 600 | 6% | 2 | 119501 | 100000016 | AttFR | D. NON COMPARABLE / IRRÉGULIER | talent distinct |
| 2150401 | 3 | 4 | 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 50 | 0.5% | NON DÉTERMINÉ | 2150302 | 200000004 | AttFR | NON DÉTERMINÉ | isolé/non comparable |
| 2463302 | 2 | 3 | 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 50 | 0.5% | NON DÉTERMINÉ | 2463202 | 200000082 | AttFR | NON DÉTERMINÉ | isolé/non comparable |
| 31100102 | 0 | 1 | 3 | NON DÉTERMINÉ | 0 | 100 | 1% | NON DÉTERMINÉ |  | 200000086 | AttFR | NON DÉTERMINÉ | isolé/non comparable |
| 31100302 | 2 | 3 | 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 100 | 1% | NON DÉTERMINÉ | 31100201,31100203 | 200000089 | AttFR | NON DÉTERMINÉ | isolé/non comparable |
| 31100502 | 4 | 5 | 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 100 | 1% | NON DÉTERMINÉ | 31100401,31100403 | 200000092 | AttFR | NON DÉTERMINÉ | isolé/non comparable |

Conclusion Attaque: **Observation vraie seulement pour certains nœuds**. Les nœuds `119101` à `119601` sont des talents distincts par rangée visuelle avec valeurs +1% à +6%, mais leur coût de rang 1 n'est pas toujours proportionnel à cette rangée. Les nœuds `31100102`, `31100302` et `31100502` répètent le même +1% marginal, mais leur coût par rang reste `NON DÉTERMINÉ` parce que `LevelUpCostValue=[1]` n'est pas une liste explicite par rang.

# Critique

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110101 | 0 | 1 | 1 | 2 SkillPoint | 0 | 1% | 0.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110102 | 0 | 1 | 1 | 2 SkillPoint | 0 | 1% | 0.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110201 | 1 | 2 | 1 | 2 SkillPoint | 2 | 2% | 1 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110202 | 1 | 2 | 1 | 2 SkillPoint | 2 | 2% | 1 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110301 | 2 | 3 | 1 | 2 SkillPoint | 4 | 3% | 1.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110302 | 2 | 3 | 1 | 2 SkillPoint | 4 | 3% | 1.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110401 | 3 | 4 | 1 | 3 SkillPoint | 6 | 4% | 1.3333 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110402 | 3 | 4 | 1 | 3 SkillPoint | 6 | 4% | 1.3333 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110501 | 4 | 5 | 1 | 3 SkillPoint | 9 | 5% | 1.6667 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110502 | 4 | 5 | 1 | 3 SkillPoint | 9 | 5% | 1.6667 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique | 1110601 | 5 | 6 | 1 | 3 SkillPoint | 12 | 6% | 2 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique | 1110602 | 5 | 6 | 1 | 3 SkillPoint | 12 | 6% | 2 | D. NON COMPARABLE / IRRÉGULIER |
| GSSkillTree / Dague / Plaie mortelle / Taux critique / Taux de coup critique augmenté | 2252101 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Plaie mortelle / Dégâts critiques / Dégâts de coup critique augmentés | 2252103 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Plaie mortelle / Taux critique / Taux de coup critique augmenté | 2252301 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Plaie mortelle / Dégâts critiques / Dégâts de coup critique augmentés | 2252303 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée concentrée / Taux critique / Taux de coup critique augmenté | 2254202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée concentrée / Dégâts critiques / Dégâts de coup critique augmentés | 2254402 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / Dégâts critiques / Dégâts de coup critique augmentés | 2462202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Taux critique / Taux de coup critique augmenté | 31101102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Taux critique / Taux de coup critique augmenté | 31101302 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Taux critique / Taux de coup critique augmenté | 31101601 | 5 | 6 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Taux critique / Taux de coup critique augmenté | 31101603 | 5 | 6 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |

# Pénétration

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| SJWSkillTree / Magicien élémentaire / Glace / Pénétration de défense / Augmentation de la Pénétration de défense | 115402 | 3 | 4 | 1 | 3 SkillPoint | 8 | 80 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Magicien élémentaire / Feu / Pénétration de défense / Pénétration de défense augmentée | 116401 | 3 | 4 | 1 | 3 SkillPoint | 8 | 80 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110103 | 0 | 1 | 1 | 2 SkillPoint | 0 | 100 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110203 | 1 | 2 | 1 | 2 SkillPoint | 2 | 200 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110303 | 2 | 3 | 1 | 2 SkillPoint | 4 | 300 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110403 | 3 | 4 | 1 | 3 SkillPoint | 6 | 400 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110503 | 4 | 5 | 1 | 3 SkillPoint | 9 | 500 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense | 1110603 | 5 | 6 | 1 | 3 SkillPoint | 12 | 600 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Épée / Résistance à la lame / Pénétration de défense % / Pénétration de défense augmentée | 2151402 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée sécurisée / Pénétration de défense % / Pénétration de défense augmentée | 2255402 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à feu / Visée patiente / Pénétration de défense % / Pénétration de défense augmentée | 2357202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à feu / Visée patiente / Pénétration de défense % / Pénétration de défense augmentée | 2357402 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.25% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Pénétration de défense % / Pénétration de défense augmentée | 31101201 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Pénétration de défense % / Pénétration de défense augmentée | 31101203 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Pénétration de défense % / Pénétration de défense augmentée | 31101401 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Pénétration de défense % / Pénétration de défense augmentée | 31101403 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |

# Précision

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| GSSkillTree / Épée / Résistance à la lame / Précision / Précision augmentée | 2151302 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.5% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée sécurisée / Précision / Précision augmentée | 2255202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.5% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Contre-offensive et restauration / Précision / Précision augmentée | 2463202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.5% | NON DÉTERMINÉ | NON DÉTERMINÉ |

# Défense

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| SJWSkillTree / Duelliste / Frappe enragée / Défense / Défense augmentée | 113401 | 3 | 4 | 1 | 3 SkillPoint | 14 | 6.4% | 2.1333 | NON DÉTERMINÉ |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119102 | 0 | 1 | 1 | 2 SkillPoint | 0 | 1% | 0.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119202 | 1 | 2 | 1 | 2 SkillPoint | 2 | 2% | 1 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119302 | 2 | 3 | 1 | 2 SkillPoint | 4 | 3% | 1.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119402 | 3 | 4 | 1 | 3 SkillPoint | 6 | 4% | 1.3333 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119502 | 4 | 5 | 1 | 3 SkillPoint | 9 | 5% | 1.6667 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / Défense / Défense augmentée | 119602 | 5 | 6 | 1 | 3 SkillPoint | 12 | 6% | 2 | D. NON COMPARABLE / IRRÉGULIER |
| GSSkillTree / Épée / Cœur d'acier / Défense / Défense augmentée | 2150403 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / Défense / Défense augmentée | 31100201 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / Défense / Défense augmentée | 31100401 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / Défense / Défense augmentée | 31100601 | 5 | 6 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |

# PV

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| SJWSkillTree / Duelliste / Coup unique / PV / Augmentation des PV | 114501 | 4 | 5 | 1 | 3 SkillPoint | 19 | 6.4% | 2.1333 | NON DÉTERMINÉ |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119103 | 0 | 1 | 1 | 2 SkillPoint | 0 | 1% | 0.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119203 | 1 | 2 | 1 | 2 SkillPoint | 2 | 2% | 1 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119303 | 2 | 3 | 1 | 2 SkillPoint | 4 | 3% | 1.5 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119403 | 3 | 4 | 1 | 3 SkillPoint | 6 | 4% | 1.3333 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119503 | 4 | 5 | 1 | 3 SkillPoint | 9 | 5% | 1.6667 | D. NON COMPARABLE / IRRÉGULIER |
| Groupe 9 / Groupe 9 / PV / PV augmentés | 119603 | 5 | 6 | 1 | 3 SkillPoint | 12 | 6% | 2 | D. NON COMPARABLE / IRRÉGULIER |
| GSSkillTree / Arme d'hast / Frappe brutale / PV / Amélioration des PV | 2461403 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / PV / PV augmentés | 31100203 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / PV / PV augmentés | 31100403 | 3 | 4 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle I / PV / PV augmentés | 31100603 | 5 | 6 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1% | NON DÉTERMINÉ | NON DÉTERMINÉ |

# Autres stats

| Famille | NodeID | Profondeur | Rangée visuelle | Rang | Coût | Chemin | Gain | Gain/point | Pattern |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|
| SJWSkillTree / Assassin / Frappe vitale / EnhanceBackDamage / Attaque dans le dos II | 112502 | 4 | 5 | 1 | 5 SkillPoint | 20 | 320 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Duelliste / Frappe enragée / PeriodGiveBuff / Overdrive | 113100 | 0 | 1 | 1 | 1 IdentityPoint | 0 | 92000201 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Duelliste / Frappe enragée / EnhanceSkillDamage / Overdrive | 113100 | 0 | 1 | 1 | 1 IdentityPoint | 0 | 20000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Duelliste / Frappe enragée / SkillChange / Ombre vive : Contre-attaque | 113202 | 1 | 2 | 1 | 4 SkillPoint | 2 | 1001204300000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Duelliste / Frappe enragée / BreakModifier / Déséquilibre augmenté | 113303 | 2 | 3 | 1 | 4 SkillPoint | 6 | 320 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Duelliste / Coup unique / BreakModifier / Déséquilibre augmenté\n[Effet passif spécial] | 114401 | 3 | 4 | 1 | 5 SkillPoint | 14 | 160 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Magicien élémentaire / Glace / ElementCumulativeDam / Augmentation des dégâts de chaîne | 115201 | 1 | 2 | 1 | 4 SkillPoint | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Magicien élémentaire / Glace / ElementCumulativeDam / Augmentation des dégâts de chaîne | 115201 | 1 | 2 | 1 | 4 SkillPoint | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| SJWSkillTree / Souverain / Changement gravitationnel / DamageOnReaction / Dégâts augmentés contre les cibles à terre | 118201 | 1 | 2 | 1 | 4 SkillPoint | 2 | 480 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Épée / Cœur d'acier / IncreaseDamageByEquipGs / Hausse des dégâts de compétence à l'épée | 2150102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 2 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Épée / Cœur d'acier / EnhanceSkillDamage / Charge frontale | 2150202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 450 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Épée / Cœur d'acier / EnhanceBackDamage / Charge frontale | 2150202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -750 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Épée / Résistance à la lame / IncreaseDamageByEquipGs / Hausse des dégâts de compétence à l'épée | 2151102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 2 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Plaie mortelle / Hausse des dégâts conditionnelle / Amplification de la douleur | 2252401 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 3% | 1 | NON DÉTERMINÉ |
| GSSkillTree / Dague / Plaie mortelle / EnhanceSkillDamage / Approche violente | 2252403 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Éviction / IncreaseDamageByEquipGs / Dégâts de compétence à la dague augmentés | 2253101 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Éviction / EnhanceBackDamage / Dégâts des attaques dans le dos augmentés | 2253103 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 150 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Éviction / EnhanceSkillDamage / Attaque en embuscade | 2253202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -300 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Éviction / EnhanceBackDamage / Attaque en embuscade | 2253202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 750 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Dague / Éviction / EnhanceSkillDamage / Dégâts de Foulée de l'ombre augmentés | 2253302 | 2 | 3 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée concentrée / IncreaseDamageByEquipGs / Dégâts de compétence à l'arc augmentés | 2254103 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 3 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée concentrée / EnhanceSkillDamage / Tir en reculant | 2254303 | 1 | 3 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée concentrée / BaseStatConversionOnSkillDamage / Frappe véloce | 2254503 | 4 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 2 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée sécurisée / IncreaseDamageByEquipGs / Dégâts de compétence à l'arc augmentés | 2255101 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 3 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée sécurisée / Hausse des dégâts / Visée sécurisée | 2255501 | 4 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 5.5% | 1.8333 | NON DÉTERMINÉ |
| GSSkillTree / Arc / Visée sécurisée / DamageByDistance / Visée sécurisée | 2255501 | 4 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -1550 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à feu / Arme à feu - Kata / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme à feu augmentés | 2356101 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 4 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à feu / Visée patiente / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme à feu augmentés | 2357102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 4 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / IncreaseDamageByEquipGs / Dégâts de compétence de Concentration augmentés | 2358102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 7 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / WeaknessElementDamage / Détection de faiblesse | 2358202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 150 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / ElementCumulativeDam / Amélioration d'accablement | 2358301 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / ElementCumulativeDam / Amélioration de chaos | 2358303 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / EnhanceElementValue / Recherche d'élément | 2358501 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 150 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Recherche de PM / BaseStatConversionOnSkillDamage / Onde de mana | 2358503 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 2 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Énergie de mana fluide / IncreaseDamageByEquipGs / Dégâts de compétence de Concentration augmentés | 2359101 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 7 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Énergie de mana fluide / IncreaseDamageByEquipGs / Dégâts de compétence de Concentration augmentés | 2359103 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 7 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Énergie de mana fluide / MPCostReduP / Amélioration de mana | 2359202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -2000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Énergie de mana fluide / IncreaseDamageByEquipGs / Amélioration de mana | 2359202 | 1 | 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 7 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Focalisateur / Énergie de mana fluide / PM max / Augmente les PM max | 2359402 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.66% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Fer-de-lance dévié / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme d'hast augmentés | 2460102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 5 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Fer-de-lance dévié / BreakModifier / Smash | 2460202 | 1 | 2 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 200 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Fer-de-lance dévié / Hausse des dégâts conditionnelle / Attaque pulvérisante | 2460403 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 3% | 1 | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Fer-de-lance dévié / Hausse des dégâts conditionnelle / Attaque pulvérisante | 2460403 | 3 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 3% | 1 | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Frappe brutale / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme d'hast augmentés | 2461102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 5 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme d'hast / Frappe brutale / Réduction des dégâts / Physique endurant | 2461401 | 2 | 3 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.5% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Dégâts de compétence d'arme à deux mains augmentés | 2462102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 8 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Porte de la mort | 2462403 | 2 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 8 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / ShieldModifier / Porte de la mort | 2462403 | 2 | 4 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -2000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / Réduction des dégâts / Posture offensive | 2462501 | 3 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | -2.5% | -0.8333 | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / Hausse des dégâts / Posture offensive | 2462501 | 3 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 4% | 1.3333 | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Frappe sanglante | 2462503 | 3 | 5 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | 8 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| GSSkillTree / Arme à deux mains / Contre-offensive et restauration / IncreaseDamageByEquipGs / Dégâts de compétence d'arme à deux mains augmentés | 2463102 | 0 | 1 | 1 | NON DÉTERMINÉ | 0 | 8 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Réduction des dégâts / Dégâts subis réduits | 31101501 | 4 | 5 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Physique / Amélioration corporelle II / Réduction des dégâts / Dégâts subis réduits | 31101503 | 4 | 5 | 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0.33% | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Vision ombrale / EXRecovery / L'Aube du règne I | 31102102 | 0 | 1 | 1 | 3 SpecialPoint | 0 | 1000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne II | 31102201 | 1 | 2 | 1 | 3 SpecialPoint | 3 | 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne III | 31102203 | 1 | 2 | 1 | 3 SpecialPoint | 3 | 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne IV | 31102302 | 2 | 3 | 1 | 3 SpecialPoint | 12 | 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Vision ombrale / SkillChange / Tranchant des ombres II | 31102502 | 4 | 5 | 1 | 3 SpecialPoint | 18 | 1001117000000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Libération d'âme / SkillChange / Âme du clair de lune I | 31103301 | 2 | 3 | 1 | 3 SpecialPoint | 6 | 1001112000000 | NON DÉTERMINÉ | NON DÉTERMINÉ |
| LordSkillTree / Éveil du monarque / Libération d'âme / EnhanceSkillDamage / Présage de destruction II | 31103503 | 4 | 5 | 1 | 3 SpecialPoint | 12 | 1000 | NON DÉTERMINÉ | NON DÉTERMINÉ |

# Familles à rendement constant


# Familles à rendement décroissant


# Familles à rendement croissant


# Talents non comparables

- GSSkillTree / Arc / Visée concentrée / BaseStatConversionOnSkillDamage / Frappe véloce: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée concentrée / Dégâts critiques / Dégâts de coup critique augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée concentrée / EnhanceSkillDamage / Tir en reculant: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée concentrée / IncreaseDamageByEquipGs / Dégâts de compétence à l'arc augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée concentrée / Taux critique / Taux de coup critique augmenté: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée sécurisée / DamageByDistance / Visée sécurisée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée sécurisée / Hausse des dégâts / Visée sécurisée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée sécurisée / IncreaseDamageByEquipGs / Dégâts de compétence à l'arc augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée sécurisée / Précision / Précision augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arc / Visée sécurisée / Pénétration de défense % / Pénétration de défense augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Fer-de-lance dévié / BreakModifier / Smash: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Fer-de-lance dévié / Hausse des dégâts conditionnelle / Attaque pulvérisante: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Fer-de-lance dévié / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme d'hast augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Frappe brutale / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme d'hast augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Frappe brutale / PV / Amélioration des PV: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme d'hast / Frappe brutale / Réduction des dégâts / Physique endurant: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Contre-offensive et restauration / Attaque / Attaque augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Contre-offensive et restauration / IncreaseDamageByEquipGs / Dégâts de compétence d'arme à deux mains augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Contre-offensive et restauration / Précision / Précision augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / Dégâts critiques / Dégâts de coup critique augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / Hausse des dégâts / Posture offensive: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Dégâts de compétence d'arme à deux mains augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Frappe sanglante: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / IncreaseDamageByEquipGs / Porte de la mort: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / Réduction des dégâts / Posture offensive: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à deux mains / Ruée de berserker / ShieldModifier / Porte de la mort: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à feu / Arme à feu - Kata / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme à feu augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à feu / Visée patiente / IncreaseDamageByEquipGs / Dégâts de compétence à l'arme à feu augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Arme à feu / Visée patiente / Pénétration de défense % / Pénétration de défense augmentée: NON DÉTERMINÉ (gain ou coût absent)
- GSSkillTree / Dague / Plaie mortelle / Dégâts critiques / Dégâts de coup critique augmentés: NON DÉTERMINÉ (gain ou coût absent)
- GSSkillTree / Dague / Plaie mortelle / EnhanceSkillDamage / Approche violente: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Plaie mortelle / Hausse des dégâts conditionnelle / Amplification de la douleur: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Plaie mortelle / Taux critique / Taux de coup critique augmenté: NON DÉTERMINÉ (gain ou coût absent)
- GSSkillTree / Dague / Éviction / EnhanceBackDamage / Attaque en embuscade: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Éviction / EnhanceBackDamage / Dégâts des attaques dans le dos augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Éviction / EnhanceSkillDamage / Attaque en embuscade: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Éviction / EnhanceSkillDamage / Dégâts de Foulée de l'ombre augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Dague / Éviction / IncreaseDamageByEquipGs / Dégâts de compétence à la dague augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / BaseStatConversionOnSkillDamage / Onde de mana: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / ElementCumulativeDam / Amélioration d'accablement: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / ElementCumulativeDam / Amélioration de chaos: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / EnhanceElementValue / Recherche d'élément: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / IncreaseDamageByEquipGs / Dégâts de compétence de Concentration augmentés: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Recherche de PM / WeaknessElementDamage / Détection de faiblesse: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Énergie de mana fluide / IncreaseDamageByEquipGs / Amélioration de mana: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Énergie de mana fluide / IncreaseDamageByEquipGs / Dégâts de compétence de Concentration augmentés: NON DÉTERMINÉ (gain ou coût absent)
- GSSkillTree / Focalisateur / Énergie de mana fluide / MPCostReduP / Amélioration de mana: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Focalisateur / Énergie de mana fluide / PM max / Augmente les PM max: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Cœur d'acier / Attaque / Attaque augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Cœur d'acier / Défense / Défense augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Cœur d'acier / EnhanceBackDamage / Charge frontale: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Cœur d'acier / EnhanceSkillDamage / Charge frontale: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Cœur d'acier / IncreaseDamageByEquipGs / Hausse des dégâts de compétence à l'épée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Résistance à la lame / IncreaseDamageByEquipGs / Hausse des dégâts de compétence à l'épée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Résistance à la lame / Précision / Précision augmentée: NON DÉTERMINÉ (une seule occurrence)
- GSSkillTree / Épée / Résistance à la lame / Pénétration de défense % / Pénétration de défense augmentée: NON DÉTERMINÉ (une seule occurrence)
- Groupe 10 / Groupe 10 / Dégâts critiques / Dégâts de coup critique: D. NON COMPARABLE / IRRÉGULIER (rendement non monotone ou série irrégulière)
- Groupe 10 / Groupe 10 / Pénétration de défense / Pénétration de défense: NON DÉTERMINÉ (gain ou coût absent)
- Groupe 10 / Groupe 10 / Taux critique / Taux de coup critique: D. NON COMPARABLE / IRRÉGULIER (rendement non monotone ou série irrégulière)
- Groupe 9 / Groupe 9 / Attaque / Attaque augmentée: D. NON COMPARABLE / IRRÉGULIER (rendement non monotone ou série irrégulière)
- Groupe 9 / Groupe 9 / Défense / Défense augmentée: D. NON COMPARABLE / IRRÉGULIER (rendement non monotone ou série irrégulière)
- Groupe 9 / Groupe 9 / PV / PV augmentés: D. NON COMPARABLE / IRRÉGULIER (rendement non monotone ou série irrégulière)
- LordSkillTree / Physique / Amélioration corporelle I / Attaque / Attaque augmentée: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Physique / Amélioration corporelle I / Défense / Défense augmentée: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Physique / Amélioration corporelle I / PV / PV augmentés: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Physique / Amélioration corporelle II / Pénétration de défense % / Pénétration de défense augmentée: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Physique / Amélioration corporelle II / Réduction des dégâts / Dégâts subis réduits: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Physique / Amélioration corporelle II / Taux critique / Taux de coup critique augmenté: NON DÉTERMINÉ (gain ou coût absent)
- LordSkillTree / Éveil du monarque / Libération d'âme / EnhanceSkillDamage / Présage de destruction II: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Libération d'âme / SkillChange / Âme du clair de lune I: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne II: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne III: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Vision ombrale / EXGainRateAdd / L'Aube du règne IV: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Vision ombrale / EXRecovery / L'Aube du règne I: NON DÉTERMINÉ (une seule occurrence)
- LordSkillTree / Éveil du monarque / Vision ombrale / SkillChange / Tranchant des ombres II: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Assassin / Attaque sournoise / Attaque / Attaque augmentée: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Assassin / Frappe vitale / EnhanceBackDamage / Attaque dans le dos II: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Coup unique / BreakModifier / Déséquilibre augmenté\n[Effet passif spécial]: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Coup unique / PV / Augmentation des PV: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Frappe enragée / BreakModifier / Déséquilibre augmenté: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Frappe enragée / Défense / Défense augmentée: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Frappe enragée / EnhanceSkillDamage / Overdrive: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Frappe enragée / PeriodGiveBuff / Overdrive: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Duelliste / Frappe enragée / SkillChange / Ombre vive : Contre-attaque: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Magicien élémentaire / Feu / Pénétration de défense / Pénétration de défense augmentée: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Magicien élémentaire / Glace / ElementCumulativeDam / Augmentation des dégâts de chaîne: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Magicien élémentaire / Glace / Pénétration de défense / Augmentation de la Pénétration de défense: NON DÉTERMINÉ (une seule occurrence)
- SJWSkillTree / Souverain / Changement gravitationnel / DamageOnReaction / Dégâts augmentés contre les cibles à terre: NON DÉTERMINÉ (une seule occurrence)

# Conséquences pour le build EXP

- La priorité directe peut utiliser `GainPerPoint` uniquement quand l'unité du gain est démontrée, pas sur les valeurs brutes.
- Deux nœuds donnant le même gain par point ont la même rentabilité directe; une rangée visuelle plus basse n'est pas automatiquement meilleure.
- `RequiredPathCost` sépare le coût d'accès du coût direct. Il reste `NON DÉTERMINÉ` dès qu'un coût direct du chemin n'est pas démontré.
- Les familles à rendement constant sont de bons candidats de remplissage stable pour leveling; les familles à rendement croissant peuvent devenir intéressantes une fois le chemin déjà ouvert.
- Les effets conditionnels, bruts ou non comparables doivent être évalués selon le style de jeu et les conditions d'activation, pas uniquement par une formule gain/coût.
