# Sung Jinwoo - Skill Level/Rank Scaling

Source tables: `ChPCSkill`, `ChPCSkillInfo`, `ChComBuff`, `CharPCSkillTreeNode`, `TextData.byte`.

Scope: rows where `ID` and `SkillGroupID` start with `100`, `UIDisplay=True`, and the French skill name contains an explicit Roman rank suffix. This avoids mixing Hunter rows from the same tables.

CSV: `analysis/csv/sjw_skill_level_scaling.csv`

Detected ranked SJW skill groups: 35.
Exported ranked rows: 116.

## Five Most Frequent Improvement Patterns

- Buffs: 39 rank transitions
- DamAttCoeff+Buffs: 20 rank transitions
- DamAttCoeff: 13 rank transitions
- aucun changement numérique explicite: 9 rank transitions
- DamAttCoeff+Cooldown+Buffs: 1 rank transitions

## Group-level Curve Families

- même pourcentage sur DamAttCoeff: 18 skill groups
- pourcentages variables sur DamAttCoeff: 8 skill groups
- aucun changement numérique explicite: 8 skill groups
- pourcentages variables sur DamAttCoeff,Cooldown: 1 skill groups

## Selected Skills

The following 10 skills are the first 10 ranked SJW groups by rank count and internal group order. Empty delta cells mean no previous rank or no explicit numeric value to compare.

### Tueur de marcheurs blancs

- Base group: `100160600`
- Pattern: pourcentages variables sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Tueur de marcheurs blancs I | 1001606000001 | 0 | 2.29 | 0 | 0 | 22 | 183/0 |  |  |
| 2 | Tueur de marcheurs blancs II | 1001606000101 | 0 | 2.29 | 0 | 0 | 22 | 183/0 | buffs modifiés |  |
| 3 | Tueur de marcheurs blancs III | 1001606000201 | 0 | 2.38 | 0 | 0 | 22 | 183/0 | DamAttCoeff: 0.0900002 (3.93014%); buffs modifiés |  |
| 4 | Tueur de marcheurs blancs IV | 1001606000301 | 0 | 2.38 | 0 | 0 | 22 | 183/0 | buffs modifiés |  |
| 5 | Tueur de marcheurs blancs V | 1001606000401 | 0 | 2.59 | 0 | 0 | 22 | 183/0 | DamAttCoeff: 0.21 (8.82352%); buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001606000001`: Jinwoo lance sa dague, se téléporte jusqu'à l'ennemi touché, puis effectue une puissante entaille.
- Rang 2 `1001606000101`: Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.
  Buffs: 200020003001 | states EnhanceBackDamage(621,750,0) || 200020003002 | states EnhanceBackDamage(622,750,0) || 200020003003 | states EnhanceBackDamage(623,750,0) || 200020003004 | states EnhanceBackDamage(624,750,0) || 200020003005 | states EnhanceBackDamage(606,750,0) || 200020003006 | states EnhanceBackDamage(162,750,0) || 200020003007 | states EnhanceBackDamage(163,750,0)
- Rang 3 `1001606000201`: Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.\nLorsque la dague touche la cible, <color=#FAC800>[Tueur de marcheurs blancs]</color> inflige une attaque dans le dos de façon garantie.
  Buffs: 200020003008 | states ForceBackAttack(606,0,0) || 200020003001 | states EnhanceBackDamage(621,750,0) || 200020003002 | states EnhanceBackDamage(622,750,0) || 200020003003 | states EnhanceBackDamage(623,750,0) || 200020003004 | states EnhanceBackDamage(624,750,0) || 200020003005 | states EnhanceBackDamage(606,750,0) || 200020003006 | states EnhanceBackDamage(162,750,0) || 200020003007 | states EnhanceBackDamage(163,750,0)
- Rang 4 `1001606000301`: Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.\nLorsque la dague touche la cible, <color=#FAC800>[Tueur de marcheurs blancs]</color> inflige une attaque dans le dos de façon garantie.\nLes dégâts infligés aux cibles affectées par <color=#FAC800>[Tueur de marcheurs blancs]</color> infligé avec la dague augmentent.
  Buffs: 200020003008 | states ForceBackAttack(606,0,0) || 200020003010 || 200020003001 | states EnhanceBackDamage(621,750,0) || 200020003002 | states EnhanceBackDamage(622,750,0) || 200020003003 | states EnhanceBackDamage(623,750,0) || 200020003004 | states EnhanceBackDamage(624,750,0) || 200020003005 | states EnhanceBackDamage(606,750,0) || 200020003006 | states EnhanceBackDamage(162,750,0) || 200020003007 | states EnhanceBackDamage(163,750,0) || 200020003009 | states IncreaseDamageByTargetBuff(606,200020003010,1000)
- Rang 5 `1001606000401`: Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.\nLorsque la dague touche la cible, <color=#FAC800>[Tueur de marcheurs blancs]</color> inflige une attaque dans le dos de façon garantie.\nLes dégâts infligés aux cibles affectées par <color=#FAC800>[Tueur de marcheurs blancs]</color> infligé avec la dague augmentent.\nL'effet <color=#64FAC8>[Vivacité]</color> se déclenche quand la dague touche sa cible.\n\n<color=#64FAC8>[Vivacité]</color>\nAugmente l'Agilité de Jinwoo de <color=#FFDF7D>10</color> points.\nAvec agilité, Jinwoo cible rapidement et précisément les points faibles de l'ennemi. <color=#FAC800>[Tueur de marcheurs blancs] inflige des dégâts aux cibles touchées par la dague avec un Taux de coup critique légèrement augmenté, ainsi que des Dégâts de coup critique augmentés</color>.
  Buffs: 200020003008 | states ForceBackAttack(606,0,0) || 200020003010 || 200020003013 | states IncreaseHitCriRate(1000,606,0), IncreaseHitCriDam(1000,606,0) || 200020003012 | states StatIncrease(2,10,0) || 200020003001 | states EnhanceBackDamage(621,750,0) || 200020003002 | states EnhanceBackDamage(622,750,0) || 200020003003 | states EnhanceBackDamage(623,750,0) || 200020003004 | states EnhanceBackDamage(624,750,0) || 200020003005 | states EnhanceBackDamage(606,750,0) || 200020003006 | states EnhanceBackDamage(162,750,0) || 200020003007 | states EnhanceBackDamage(163,750,0) || 200020003009 | states IncreaseDamageByTargetBuff(606,200020003010,1000) || 200020003011

### Vague de dragon naga

- Base group: `100162700`
- Pattern: même pourcentage sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Vague de dragon naga I | 1001627000001 | 0 | 3.57 | 0 | 0 | 29 | 241/0 |  |  |
| 2 | Vague de dragon naga II | 1001627000101 | 0 | 3.94 | 0 | 0 | 29 | 241/0 | DamAttCoeff: 0.37 (10.3641%); buffs modifiés |  |
| 3 | Vague de dragon naga III | 1001627000201 | 0 | 3.94 | 0 | 0 | 29 | 241/0 |  |  |
| 4 | Vague de dragon naga IV | 1001627000301 | 0 | 3.94 | 0 | 0 | 29 | 241/0 | buffs modifiés |  |
| 5 | Vague de dragon naga V | 1001627000401 | 0 | 3.94 | 0 | 0 | 29 | 241/0 | buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001627000001`: Jinwoo fait tournoyer sa lance pour invoquer une vague en forme de dragon qui s'élève avant de s'abattre pour infliger des dégâts.
  Buffs: 1420000021 | stats PrecisionP=1200, DamP=-800
- Rang 2 `1001627000101`: L'utilisation de cette compétence augmente temporairement l'<color=#64FAC8>[Attaque]</color> de Jinwoo et lui confère <color=#64FAC8>[Super armure]</color>.
  Buffs: 200020002015 | states ReactionImmune(16,0,0) || 1420000021 | stats PrecisionP=1200, DamP=-800 || 200020002001
- Rang 3 `1001627000201`: L'utilisation de cette compétence augmente temporairement l'<color=#64FAC8>[Attaque]</color> de Jinwoo, et lui confère <color=#64FAC8>[Super armure]</color>.\nLe nombre de coups de lance et de piliers d'eau augmente.
  Buffs: 200020002015 | states ReactionImmune(16,0,0) || 1420000021 | stats PrecisionP=1200, DamP=-800 || 200020002001
- Rang 4 `1001627000301`: L'utilisation de cette compétence augmente temporairement l'<color=#64FAC8>[Attaque]</color> et le <color=#64FAC8>[Taux de récupération des PM]</color> de Jinwoo. Il obtient <color=#64FAC8>[Super armure]</color> pendant son exécution, et le nombre de coups de lance et de piliers d'eau augmente.\nLorsqu'il attaque avec cette compétence, a des chances d'augmenter les <color=#64FAC8>dégâts élémentaires</color> <color=#b0c6db>(cumulable jusqu'à 6 fois)</color>.
  Buffs: 200020002015 | states ReactionImmune(16,0,0) || 1420000021 | stats PrecisionP=1200, DamP=-800 || 200020002001 || 200020002003 || 200020002005
- Rang 5 `1001627000401`: L'utilisation de cette compétence augmente temporairement l'<color=#64FAC8>[Attaque]</color> et le <color=#64FAC8>[Taux de récupération des PM]</color> de Jinwoo. Il obtient <color=#64FAC8>[Super armure]</color> pendant son exécution, et le nombre de coups de lance et de piliers d'eau augmente.\nLorsqu'il attaque avec cette compétence, a des chances d'augmenter les <color=#64FAC8>dégâts élémentaires</color> <color=#b0c6db>(cumulable jusqu'à 6 fois)</color>.\nUn pilier d'eau est créé dans la portée du trident lorsque les ennemis sont touchés <color=#FFDF7D>5 fois</color>.
  Buffs: 200020002011 || 200020002015 | states ReactionImmune(16,0,0) || 1420000021 | stats PrecisionP=1200, DamP=-800 || 200020002001 || 200020002003 || 200020002005

### Entaille ardente

- Base group: `100164800`
- Pattern: pourcentages variables sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Entaille ardente I | 1001648000001 | 0 | 3.62 | 0 | 0 | 35 | 291/0 |  |  |
| 2 | Entaille ardente II | 1001648000101 | 0 | 3.62 | 0 | 0 | 35 | 291/0 | buffs modifiés |  |
| 3 | Entaille ardente III | 1001648000201 | 0 | 3.87 | 0 | 0 | 35 | 291/0 | DamAttCoeff: 0.25 (6.90608%) |  |
| 4 | Entaille ardente IV | 1001648000301 | 0 | 3.87 | 0 | 0 | 35 | 291/0 | buffs modifiés |  |
| 5 | Entaille ardente V | 1001648000401 | 0 | 3.91 | 0 | 0 | 35 | 291/0 | DamAttCoeff: 0.0400002 (1.0336%); buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001648000001`: Jinwoo concentre son énergie, dégaine rapidement son épée et frappe violemment devant lui.
- Rang 2 `1001648000101`: Lorsque Jinwoo est touché alors qu'il adopte la posture <color=#FAC800>[Entaille ardente]</color>, les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'<color=#FAC800>[Entaille ardente]</color> augmentent légèrement l'espace d'un instant.
  Buffs: 200010005000 | stats DamReduP=3000 | states ReactionImmune(16,0,0)
- Rang 3 `1001648000201`: Lorsque Jinwoo est touché alors qu'il adopte la posture <color=#FAC800>[Entaille ardente]</color>, les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'<color=#FAC800>[Entaille ardente]</color> augmentent légèrement l'espace d'un instant.
  Buffs: 200010005000 | stats DamReduP=3000 | states ReactionImmune(16,0,0)
- Rang 4 `1001648000301`: Lorsque Jinwoo est touché alors qu'il adopte la posture <color=#FAC800>[Entaille ardente]</color>, les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'<color=#FAC800>[Entaille ardente]</color> augmentent légèrement l'espace d'un instant.\nLorsque <color=#FAC800>[Entaille ardente]</color> met l'ennemi en état de <color=#FF8741>Déséquilibre</color>, le temps de rechargement de la compétence est réinitialisé et les dégâts d'<color=#FAC800>[Entaille ardente]</color> infligés à la cible augmentent significativement.
  Buffs: 200010005000 | stats DamReduP=3000 | states ReactionImmune(16,0,0) || 200010005002
- Rang 5 `1001648000401`: Lorsque Jinwoo est touché alors qu'il adopte la posture <color=#FAC800>[Entaille ardente]</color>, les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'<color=#FAC800>[Entaille ardente]</color> augmentent légèrement l'espace d'un instant.\nLorsque <color=#FAC800>[Entaille ardente]</color> met l'ennemi en état de <color=#FF8741>Déséquilibre</color>, le temps de rechargement de la compétence est réinitialisé et les dégâts d'<color=#FAC800>[Entaille ardente]</color> infligés à la cible augmentent significativement.
  Buffs: 200010005000 | stats DamReduP=3000 | states ReactionImmune(16,0,0) || 200010005002 || 200010005004

### Jugement du Léviathan

- Base group: `100160200`
- Pattern: même pourcentage sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Jugement du Léviathan I | 1001602000001 | 0 | 4.68 | 0 | 0 | 38 | 316/0 |  |  |
| 2 | Jugement du Léviathan II | 1001602000101 | 0 | 4.68 | 0 | 0 | 38 | 316/0 | buffs modifiés |  |
| 3 | Jugement du Léviathan III | 1001602000201 | 0 | 4.88 | 0 | 0 | 38 | 316/0 | DamAttCoeff: 0.2 (4.27351%) |  |
| 4 | Jugement du Léviathan IV | 1001602000301 | 0 | 4.88 | 0 | 0 | 38 | 316/0 | buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001602000001`: Lorsqu'il utilise cette compétence, Jinwoo bénéficie de <color=#64FAC8>[Super armure]</color>.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure || 1001602000004 | stats CriDamP=4000
- Rang 2 `1001602000101`: Lorsqu'il utilise cette compétence, Jinwoo bénéficie de <color=#64FAC8>[Super armure]</color>\n. Lorsque cette compétence touche sa cible, elle lui inflige l'effet <color=#64FAC8>[Glace gelée]</color>.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure || 1001602000004 | stats CriDamP=4000 || 1001602000001
- Rang 3 `1001602000201`: Lorsqu'il utilise cette compétence, Jinwoo bénéficie de <color=#64FAC8>[Super armure]</color>\n. Lorsque cette compétence touche sa cible, elle lui inflige l'effet <color=#64FAC8>[Glace gelée]</color>.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure || 1001602000004 | stats CriDamP=4000 || 1001602000001
- Rang 4 `1001602000301`: Lorsqu'il utilise cette compétence, Jinwoo bénéficie de <color=#64FAC8>[Super armure]</color>\n. Lorsque cette compétence touche sa cible, elle lui inflige l'effet <color=#64FAC8>[Glace gelée]</color>.\nLes ennemis se trouvant dans la zone pluvieuse subissent davantage de dégâts d'<color=#4B96FA>[eau]</color>.
  Buffs: 1001602000002 | states ChangeDamageOnElementType(1,500,0) || 1200191000 | states ReactionImmune(16,0,0) | Super armure || 1001602000004 | stats CriDamP=4000 || 1001602000001

### Éclat de lumière

- Base group: `100162600`
- Pattern: même pourcentage sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Éclat de lumière I | 1001626000001 | 0 | 2.6 | 0 | 0 | 28 | 233/0 |  |  |
| 2 | Éclat de lumière II | 1001626000101 | 0 | 2.68 | 0 | 0 | 28 | 233/0 | DamAttCoeff: 0.0800002 (3.07693%); buffs modifiés |  |
| 3 | Éclat de lumière III | 1001626000201 | 0 | 2.68 | 0 | 0 | 28 | 233/0 | buffs modifiés |  |
| 4 | Éclat de lumière IV | 1001626000301 | 0 | 2.68 | 0 | 0 | 28 | 233/0 |  |  |

**Buffs et description localisée**

- Rang 1 `1001626000001`: Jinwoo traîne son arme au sol pour provoquer une puissante explosion, puis recule et tire une salve de flèches de lumière.
- Rang 2 `1001626000101`: Lorsque la première attaque de Jinwoo touche, elle inflige l'effet <color=#64FAC8>[Paralysie]</color> à la cible.
  Buffs: 200020004001 | Paralysie | states BodyStop(60,0,0) | Immobilise la cible.\nDurée : <color=#FFDF7D>{Duration,0.001} seconde(s)</color>
- Rang 3 `1001626000201`: Lorsque la première attaque de Jinwoo touche, elle inflige l'effet <color=#64FAC8>[Paralysie]</color> à la cible.\nAugmente les dégâts d'<color=#FAC800>[Éclat de lumière]</color> infligés aux cibles touchées par l'effet <color=#64FAC8>[Paralysie]</color>.
  Buffs: 200020004001 | Paralysie | states BodyStop(60,0,0) | Immobilise la cible.\nDurée : <color=#FFDF7D>{Duration,0.001} seconde(s)</color> || 200020004002 | states IncreaseDamageByTargetSpecialState(626,22,5000)
- Rang 4 `1001626000301`: Lorsque la première attaque de Jinwoo touche, elle inflige l'effet <color=#64FAC8>[Paralysie]</color> à la cible.\nAugmente les dégâts d'<color=#FAC800>[Éclat de lumière]</color> infligés aux cibles touchées par l'effet <color=#64FAC8>[Paralysie]</color>.
  Buffs: 200020004001 | Paralysie | states BodyStop(60,0,0) | Immobilise la cible.\nDurée : <color=#FFDF7D>{Duration,0.001} seconde(s)</color> || 200020004002 | states IncreaseDamageByTargetSpecialState(626,22,5000)

### Vile attaque sournoise

- Base group: `100170600`
- Pattern: pourcentages variables sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Vile attaque sournoise I | 1001706000001 | 0 | 1.43 | 0 | 0 | 22 | 183/0 |  |  |
| 2 | Vile attaque sournoise II | 1001706000101 | 0 | 1.49 | 0 | 0 | 22 | 183/0 | DamAttCoeff: 0.0600001 (4.19581%); buffs modifiés |  |
| 3 | Vile attaque sournoise III | 1001706000201 | 0 | 2.35 | 0 | 0 | 22 | 183/0 | DamAttCoeff: 0.86 (57.7181%) |  |
| 4 | Vile attaque sournoise IV | 1001706000301 | 0 | 2.35 | 0 | 0 | 22 | 183/0 | buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001706000001`: Jinwoo se téléporte au-dessus de la tête de l'ennemi et le frappe d'une seule main.
- Rang 2 `1001706000101`: Lorsque les ennemis marchent sur les tuiles empoisonnées, ils déclenchent l'effet <color=#64FAC8>[Poison]</color>.
  Buffs: 200010008001 | stats AttFR=-1000 | states LevelDotDamage(6,4000,0)
- Rang 3 `1001706000201`: Lorsque les ennemis entrent en contact avec le brouillard toxique, ils subissent l'effet <color=#64FAC8>[Poison]</color>.
  Buffs: 200010008001 | stats AttFR=-1000 | states LevelDotDamage(6,4000,0)
- Rang 4 `1001706000301`: Lorsque les ennemis entrent en contact avec le brouillard toxique, ils subissent l'effet <color=#64FAC8>[Poison]</color>.\nLes dégâts infligés aux cibles touchées par l'effet <color=#64FAC8>[Poison]</color> augmentent.
  Buffs: 200010008001 | stats AttFR=-1000 | states LevelDotDamage(6,4000,0) || 200010008002 | states SkillDamageIncreaseOnBuffedTarget(0,75,1000)

### Incinération

- Base group: `100172000`
- Pattern: même pourcentage sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Incinération I | 1001720000001 | 0 | 1.78 | 0 | 0 | 35 | 291/0 |  |  |
| 2 | Incinération II | 1001720000101 | 0 | 1.78 | 0 | 0 | 35 | 291/0 | buffs modifiés |  |
| 3 | Incinération III | 1001720000201 | 0 | 1.78 | 0 | 0 | 35 | 291/0 | buffs modifiés |  |
| 4 | Incinération IV | 1001720000301 | 0 | 1.89 | 0 | 0 | 35 | 291/0 | DamAttCoeff: 0.11 (6.17978%); buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001720000001`: Jinwoo concentre une énergie de feu intense et la fait exploser devant lui.
- Rang 2 `1001720000101`: Lorsque l'utilisateur réactive cette compétence au bon moment alors que l'énergie de feu est concentrée, une explosion supplémentaire se déclenche.
  Buffs: 10185 | states SkillChange(1001720000100,1001720000500,0), SkillChange(1001720000200,1001720000500,0), SkillChange(1001720000300,1001720000500,0) || 10187 | states SkillChange(1001720000100,1001720000400,0), SkillChange(1001720000200,1001720000400,0), SkillChange(1001720000300,1001720000400,0)
- Rang 3 `1001720000201`: Lorsque Jinwoo réactive cette compétence au bon moment alors que l'énergie de feu est concentrée, une explosion supplémentaire se déclenche. Les dégâts de toutes ses compétences de combat passives de <color=#64FAC8>[Magicien élémentaire]</color> augmentent et sa consommation de MP diminue.
  Buffs: 10185 | states SkillChange(1001720000100,1001720000500,0), SkillChange(1001720000200,1001720000500,0), SkillChange(1001720000300,1001720000500,0) || 10187 | states SkillChange(1001720000100,1001720000400,0), SkillChange(1001720000200,1001720000400,0), SkillChange(1001720000300,1001720000400,0) || 10183 | states SkillTreeMpCost(3,-1000,0), SkillTreeEnhance(3,500,0) | Lorsque l'utilisateur applique <color=#FAC800>Éclatement</color>, les effets <color=#64FAC8>[Insufflation de points de mana]</color> ou <color=#64FAC8>[Récupération de points de mana]</color> s'appliquent selon la quantité de PM restante. <BuffIcon,10185>Si les PM de l'utilisateur sont de <color=#FFDF7D>{TriggerOptionValue2,1} %</color> ou plus, l'effet est activé.\n\nLorsque l'utilisateur applique <color=#FAC800>Éclatement</color>, ses dégâts de compétence augmentent de <color=#FFDF7D>{Buff,10186,SpecialState1OptionValue2,0.01} %</color>, mais <color=#FFDF7D>{Buff,10186,SpecialState2OptionValue2,-0.01} %</color> de ses PM max sont consommés.</BuffIcon> <BuffIcon,10187>Si les PM de l'utilisateur sont de <color=#FFDF7D>{Buff,10184,TriggerOptionValue2} %</color> ou moins, l'effet est activé.\n\nL'utilisateur récupère <color=#FFDF7D>{Buff,10189,SpecialState1OptionValue2,0.01} %</color> de ses PM pour chaque cible touchée par <color=#FAC800>Éclatement</color>.</BuffIcon>
- Rang 4 `1001720000301`: Lorsque Jinwoo réactive cette compétence au bon moment alors que l'énergie de feu est concentrée, une explosion supplémentaire se déclenche. Les dégâts de toutes ses compétences de combat passives de <color=#64FAC8>[Magicien élémentaire]</color> augmentent et sa consommation de MP diminue.
  Buffs: 10185 | states SkillChange(1001720000100,1001720000500,0), SkillChange(1001720000200,1001720000500,0), SkillChange(1001720000300,1001720000500,0) || 10188 | states EnhanceElementValue(1,100,720) || 10187 | states SkillChange(1001720000100,1001720000400,0), SkillChange(1001720000200,1001720000400,0), SkillChange(1001720000300,1001720000400,0) || 10183 | states SkillTreeMpCost(3,-1000,0), SkillTreeEnhance(3,500,0) | Lorsque l'utilisateur applique <color=#FAC800>Éclatement</color>, les effets <color=#64FAC8>[Insufflation de points de mana]</color> ou <color=#64FAC8>[Récupération de points de mana]</color> s'appliquent selon la quantité de PM restante. <BuffIcon,10185>Si les PM de l'utilisateur sont de <color=#FFDF7D>{TriggerOptionValue2,1} %</color> ou plus, l'effet est activé.\n\nLorsque l'utilisateur applique <color=#FAC800>Éclatement</color>, ses dégâts de compétence augmentent de <color=#FFDF7D>{Buff,10186,SpecialState1OptionValue2,0.01} %</color>, mais <color=#FFDF7D>{Buff,10186,SpecialState2OptionValue2,-0.01} %</color> de ses PM max sont consommés.</BuffIcon> <BuffIcon,10187>Si les PM de l'utilisateur sont de <color=#FFDF7D>{Buff,10184,TriggerOptionValue2} %</color> ou moins, l'effet est activé.\n\nL'utilisateur récupère <color=#FFDF7D>{Buff,10189,SpecialState1OptionValue2,0.01} %</color> de ses PM pour chaque cible touchée par <color=#FAC800>Éclatement</color>.</BuffIcon>

### Destruction terrestre

- Base group: `100172500`
- Pattern: même pourcentage sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Destruction terrestre I | 1001725000001 | 0 | 2.33 | 0 | 0 | 31 | 258/0 |  |  |
| 2 | Destruction terrestre II | 1001725000101 | 0 | 2.33 | 0 | 0 | 31 | 258/0 | buffs modifiés |  |
| 3 | Destruction terrestre III | 1001725000201 | 0 | 0 | 0 | 0 | 31 | 258/0 | DamAttCoeff: -2.33 (-100%) |  |
| 4 | Destruction terrestre IV | 1001725000301 | 0 | 0 | 0 | 0 | 31 | 258/0 | buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001725000001`: Après avoir tournoyé dans les airs, Jinwoo frappe le sol avec force. Maintenez le bouton enfoncé pour prolonger son temps dans les airs.
  Buffs: 1420000020 | stats PrecisionP=-3000, DamP=3000
- Rang 2 `1001725000101`: Lorsque cette compétence est utilisée, l'utilisateur obtient un <color=#64FAC8>[Bouclier]</color>.
  Buffs: 1420000020 | stats PrecisionP=-3000, DamP=3000 || 200010011001
- Rang 3 `1001725000201`: Lorsque Sung Jinwoo utilise cette compétence, il obtient un <color=#64FAC8>[Bouclier]</color> pendant un certain temps.
  Buffs: 1420000020 | stats PrecisionP=-3000, DamP=3000 || 200010011001
- Rang 4 `1001725000301`: Lorsque Sung Jinwoo utilise cette compétence, il obtient un <color=#64FAC8>[Bouclier]</color> pendant un certain temps.
  Buffs: 200010011003 | states SkillCast(1001828000000,0,0) || 1420000020 | stats PrecisionP=-3000, DamP=3000 || 200010011001

### Charge explosive

- Base group: `100173500`
- Pattern: pourcentages variables sur DamAttCoeff

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Charge explosive I | 1001735000001 | 0 | 4.66 | 0 | 0 | 34 | 283/0 |  |  |
| 2 | Charge explosive II | 1001735000101 | 0 | 7.06 | 0 | 0 | 34 | 283/0 | DamAttCoeff: 2.4 (51.5021%) |  |
| 3 | Charge explosive III | 1001735000201 | 0 | 7.06 | 0 | 0 | 34 | 283/0 | buffs modifiés |  |
| 4 | Charge explosive IV | 1001735000301 | 0 | 7.44 | 0 | 0 | 34 | 283/0 | DamAttCoeff: 0.38 (5.38244%); buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001735000001`: Jinwoo fonce vers l'avant et assène une frappe vers le bas à la cible.
  Buffs: 1420000020 | stats PrecisionP=-3000, DamP=3000
- Rang 2 `1001735000101`: Jinwoo fonce vers l'avant, concentre une énergie puissante et assène une frappe vers le bas.
  Buffs: 1420000020 | stats PrecisionP=-3000, DamP=3000
- Rang 3 `1001735000201`: Les chances de coup critique de Jinwoo augmentent considérablement, et il inflige un puissant effet de déséquilibre à l'ennemi.
  Buffs: 10167 | stats PrecisionP=-3000 || 10169 | states CriticalRate(2000,735,0) | L'effet <color=#64FAC8>[Force d'orc]</color> s'applique également en cas de Coup critique réussi.\nAugmente les chance qu'<color=#FAC800>Épée longue d'orc</color> inflige un Coup critique de <color=#FFDF7D>{SpecialState1OptionValue1,0.01} %</color>. || 1420000020 | stats PrecisionP=-3000, DamP=3000
- Rang 4 `1001735000301`: Les chances de coup critique de Jinwoo augmentent considérablement, et il inflige un puissant effet de déséquilibre à l'ennemi. Lorsque cette compétence est utilisée, Jinwoo bénéficie de l'effet <color=#64FAC8>[Immunité aux dégâts]</color>.
  Buffs: 10851 | states Invincible(100,0,0) || 10167 | stats PrecisionP=-3000 || 10169 | states CriticalRate(2000,735,0) | L'effet <color=#64FAC8>[Force d'orc]</color> s'applique également en cas de Coup critique réussi.\nAugmente les chance qu'<color=#FAC800>Épée longue d'orc</color> inflige un Coup critique de <color=#FFDF7D>{SpecialState1OptionValue1,0.01} %</color>. || 1420000020 | stats PrecisionP=-3000, DamP=3000

### Tonnerre ébranlé

- Base group: `100174500`
- Pattern: aucun changement numérique explicite

| Rang | Nom rang | ID interne | TotalDamage | ATK | DEF | HP | CD | MP coût/gain | Gain réel | Coût amélioration |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | Tonnerre ébranlé I | 1001745000001 | 0 | 0 | 0 | 0 | 24 | 200/0 |  |  |
| 2 | Tonnerre ébranlé II | 1001745000101 | 0 | 0 | 0 | 0 | 24 | 200/0 | buffs modifiés |  |
| 3 | Tonnerre ébranlé III | 1001745000201 | 0 | 0 | 0 | 0 | 24 | 200/0 | buffs modifiés |  |
| 4 | Tonnerre ébranlé IV | 1001745000301 | 0 | 0 | 0 | 0 | 24 | 200/0 | buffs modifiés |  |

**Buffs et description localisée**

- Rang 1 `1001745000001`: Jinwoo frappe l'ennemi avec force. Maintenez le bouton enfoncé pour prolonger l'attaque.
- Rang 2 `1001745000101`: Jinwoo obtient <color=#64FAC8>[Super armure]</color> pendant l'utilisation de cette compétence.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure
- Rang 3 `1001745000201`: Jinwoo obtient <color=#64FAC8>[Super armure]</color> pendant l'utilisation de cette compétence.\nDéclenche l'effet <color=#64FAC8>[Pénétration de défense augmentée]</color> pendant l'utilisation de cette compétence.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure || 200010012001 | stats ArmPenP=1500
- Rang 4 `1001745000301`: Jinwoo obtient <color=#64FAC8>[Super armure]</color> pendant l'utilisation de cette compétence.\nDéclenche l'effet <color=#64FAC8>[Pénétration de défense augmentée]</color> pendant l'utilisation de cette compétence.\nAugmente les dégâts infligés aux cibles déséquilibrées pendant l'utilisation de cette compétence.
  Buffs: 1200191000 | states ReactionImmune(16,0,0) | Super armure || 200010012001 | stats ArmPenP=1500 || 200010012002 | states IncreaseDamageByTargetSpecialState(745,20,6000), IncreaseDamageByTargetSpecialState(745,201,6000)

## Interpretation

- Les améliorations ne suivent pas une courbe unique dans les données exportées.
- Beaucoup de rangs modifient seulement les textes/buffs ou des propriétés non listées, sans changer les coefficients numériques explicites.
- Quand les coefficients changent, les gains peuvent être fixes sur certains pas, absents sur d'autres, ou concentrés sur un rang précis.
- Les coûts d'amélioration directs de `ChPCSkill` sont souvent vides/0 pour ces rangs SJW; les coûts disponibles proviennent surtout des nœuds `CharPCSkillTreeNode` qui déverrouillent un `SkillGroupID`.
- Aucun ordre d'application des buffs n'est déduit ici; le CSV liste uniquement les buffs explicitement référencés.
