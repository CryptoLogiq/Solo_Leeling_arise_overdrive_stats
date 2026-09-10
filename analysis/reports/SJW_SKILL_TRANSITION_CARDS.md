# Sung Jinwoo - Fiches de transitions de rang

Source tables: `ChPCSkill`, `ChPCSkillInfo`, `ChComBuff`, `CharPCSkillTreeNode`, `TextData.byte` via exports JSON existants.

Les conversions numériques des buffs sont indiquées avec un niveau de confiance. `CONFIRMÉ` signifie que la description localisée ou un placeholder indique l'unité; `FORTEMENT PROBABLE` signifie cohérent avec les conventions répétées des tables, mais pas prouvé par cette ligne seule; `HYPOTHÈSE` reste brut.

Transitions exportées: 77.

# Tueur de marcheurs blancs I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.

NOUVEL EFFET
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 621)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 622)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 606)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 162)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 624)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 623)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 163)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 621)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 622)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 606)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 162)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 624)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 623)
- EnhanceBackDamage: +7.5% attaque de dos (FORTEMENT PROBABLE; bonus interne 750, hit/skill 163)

Données sources :
- SkillGroupID avant/après: `1001606000000` → `1001606000100`
- ID avant/après: `1001606000001` → `1001606000101`
- BaseSkillInfoKey avant/après: `1001606000001` → `1001606000101`
- Buff IDs avant: ``
- Buff IDs après: `200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tueur de marcheurs blancs II → III

Dégâts directs        : inchangés
ATK coeff             : 2.29 → 2.38
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.
Lorsque la dague touche la cible, [Tueur de marcheurs blancs] inflige une attaque dans le dos de façon garantie.

NOUVEL EFFET
- attaque de dos garantie pour référence 606 (CONFIRMÉ par description si présente)

Gain réel :
Gain direct :
- ATK coeff: +0.0900002 (+3.93%)
Utilitaire :
- attaque de dos garantie pour référence 606 (CONFIRMÉ par description si présente)

Données sources :
- SkillGroupID avant/après: `1001606000100` → `1001606000200`
- ID avant/après: `1001606000101` → `1001606000201`
- BaseSkillInfoKey avant/après: `1001606000101` → `1001606000201`
- Buff IDs avant: `200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007`
- Buff IDs après: `200020003008,200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tueur de marcheurs blancs III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.
Lorsque la dague touche la cible, [Tueur de marcheurs blancs] inflige une attaque dans le dos de façon garantie.
Les dégâts infligés aux cibles affectées par [Tueur de marcheurs blancs] infligé avec la dague augmentent.

NOUVEL EFFET
- IncreaseDamageByTargetBuff: +10% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 1000, cible 606/200020003010 )

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- IncreaseDamageByTargetBuff: +10% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 1000, cible 606/200020003010 )

Données sources :
- SkillGroupID avant/après: `1001606000200` → `1001606000300`
- ID avant/après: `1001606000201` → `1001606000301`
- BaseSkillInfoKey avant/après: `1001606000201` → `1001606000301`
- Buff IDs avant: `200020003008,200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007`
- Buff IDs après: `200020003008,200020003010,200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007,200020003009`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tueur de marcheurs blancs IV → V

Dégâts directs        : inchangés
ATK coeff             : 2.38 → 2.59
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les dégâts infligés par Jinwoo augmentent lorsqu'il attaque un ennemi par-derrière avec le Surin de Baruka.
Lorsque la dague touche la cible, [Tueur de marcheurs blancs] inflige une attaque dans le dos de façon garantie.
Les dégâts infligés aux cibles affectées par [Tueur de marcheurs blancs] infligé avec la dague augmentent.
L'effet [Vivacité] se déclenche quand la dague touche sa cible.

[Vivacité]
Augmente l'Agilité de Jinwoo de 10 points.
Avec agilité, Jinwoo cible rapidement et précisément les points faibles de l'ennemi. [Tueur de marcheurs blancs] inflige des dégâts aux cibles touchées par la dague avec un Taux de coup critique légèrement augmenté, ainsi que des Dégâts de coup critique augmentés.

NOUVEL EFFET
- StatIncrease: paramètres internes 2, 10, 0
- IncreaseHitCriRate: +10% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1000)
- IncreaseHitCriDam: +10% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1000)

Gain réel :
Gain direct :
- ATK coeff: +0.21 (+8.82%)
Changement de mécanique :
- StatIncrease: paramètres internes 2, 10, 0
- IncreaseHitCriRate: +10% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1000)
- IncreaseHitCriDam: +10% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1000)

Données sources :
- SkillGroupID avant/après: `1001606000300` → `1001606000400`
- ID avant/après: `1001606000301` → `1001606000401`
- BaseSkillInfoKey avant/après: `1001606000301` → `1001606000401`
- Buff IDs avant: `200020003008,200020003010,200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007,200020003009`
- Buff IDs après: `200020003008,200020003010,200020003013,200020003012,200020003001,200020003002,200020003003,200020003004,200020003005,200020003006,200020003007,200020003009,200020003011`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vague de dragon naga I → II

Dégâts directs        : inchangés
ATK coeff             : 3.57 → 3.94
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de cette compétence augmente temporairement l'[Attaque] de Jinwoo et lui confère [Super armure].

NOUVEL EFFET
- Super armure / immunité aux réactions (CONFIRMÉ par description)

Gain réel :
Gain direct :
- ATK coeff: +0.37 (+10.4%)
Gain défensif :
- Super armure / immunité aux réactions (CONFIRMÉ par description)

Données sources :
- SkillGroupID avant/après: `1001627000000` → `1001627000100`
- ID avant/après: `1001627000001` → `1001627000101`
- BaseSkillInfoKey avant/après: `1001627000001` → `1001627000101`
- Buff IDs avant: `1420000021`
- Buff IDs après: `200020002015,1420000021,200020002001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vague de dragon naga II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de cette compétence augmente temporairement l'[Attaque] de Jinwoo, et lui confère [Super armure].
Le nombre de coups de lance et de piliers d'eau augmente.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001627000100` → `1001627000200`
- ID avant/après: `1001627000101` → `1001627000201`
- BaseSkillInfoKey avant/après: `1001627000101` → `1001627000201`
- Buff IDs avant: `200020002015,1420000021,200020002001`
- Buff IDs après: `200020002015,1420000021,200020002001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vague de dragon naga III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de cette compétence augmente temporairement l'[Attaque] et le [Taux de récupération des PM] de Jinwoo. Il obtient [Super armure] pendant son exécution, et le nombre de coups de lance et de piliers d'eau augmente.
Lorsqu'il attaque avec cette compétence, a des chances d'augmenter les dégâts élémentaires (cumulable jusqu'à 6 fois).

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001627000200` → `1001627000300`
- ID avant/après: `1001627000201` → `1001627000301`
- BaseSkillInfoKey avant/après: `1001627000201` → `1001627000301`
- Buff IDs avant: `200020002015,1420000021,200020002001`
- Buff IDs après: `200020002015,1420000021,200020002001,200020002003,200020002005`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vague de dragon naga IV → V

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de cette compétence augmente temporairement l'[Attaque] et le [Taux de récupération des PM] de Jinwoo. Il obtient [Super armure] pendant son exécution, et le nombre de coups de lance et de piliers d'eau augmente.
Lorsqu'il attaque avec cette compétence, a des chances d'augmenter les dégâts élémentaires (cumulable jusqu'à 6 fois).
Un pilier d'eau est créé dans la portée du trident lorsque les ennemis sont touchés 5 fois.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001627000300` → `1001627000400`
- ID avant/après: `1001627000301` → `1001627000401`
- BaseSkillInfoKey avant/après: `1001627000301` → `1001627000401`
- Buff IDs avant: `200020002015,1420000021,200020002001,200020002003,200020002005`
- Buff IDs après: `200020002011,200020002015,1420000021,200020002001,200020002003,200020002005`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Entaille ardente I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque Jinwoo est touché alors qu'il adopte la posture [Entaille ardente], les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'[Entaille ardente] augmentent légèrement l'espace d'un instant.

NOUVEL EFFET
- DamReduP: 30% (FORTEMENT PROBABLE; valeur interne 3000)
- Super armure / immunité aux réactions (CONFIRMÉ par description)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain défensif :
- DamReduP: 30% (FORTEMENT PROBABLE; valeur interne 3000)
- Super armure / immunité aux réactions (CONFIRMÉ par description)

Données sources :
- SkillGroupID avant/après: `1001648000000` → `1001648000100`
- ID avant/après: `1001648000001` → `1001648000101`
- BaseSkillInfoKey avant/après: `1001648000001` → `1001648000101`
- Buff IDs avant: ``
- Buff IDs après: `200010005000`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Entaille ardente II → III

Dégâts directs        : inchangés
ATK coeff             : 3.62 → 3.87
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.25 (+6.91%)

Données sources :
- SkillGroupID avant/après: `1001648000100` → `1001648000200`
- ID avant/après: `1001648000101` → `1001648000201`
- BaseSkillInfoKey avant/après: `1001648000101` → `1001648000201`
- Buff IDs avant: `200010005000`
- Buff IDs après: `200010005000`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Entaille ardente III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque Jinwoo est touché alors qu'il adopte la posture [Entaille ardente], les dégâts qu'il subit sont réduits et sa posture n'est pas interrompue. Les dégâts ainsi que l'effet Déséquilibre d'[Entaille ardente] augmentent légèrement l'espace d'un instant.
Lorsque [Entaille ardente] met l'ennemi en état de Déséquilibre, le temps de rechargement de la compétence est réinitialisé et les dégâts d'[Entaille ardente] infligés à la cible augmentent significativement.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001648000200` → `1001648000300`
- ID avant/après: `1001648000201` → `1001648000301`
- BaseSkillInfoKey avant/après: `1001648000201` → `1001648000301`
- Buff IDs avant: `200010005000`
- Buff IDs après: `200010005000,200010005002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Entaille ardente IV → V

Dégâts directs        : inchangés
ATK coeff             : 3.87 → 3.91
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.0400002 (+1.03%)

Données sources :
- SkillGroupID avant/après: `1001648000300` → `1001648000400`
- ID avant/après: `1001648000301` → `1001648000401`
- BaseSkillInfoKey avant/après: `1001648000301` → `1001648000401`
- Buff IDs avant: `200010005000,200010005002`
- Buff IDs après: `200010005000,200010005002,200010005004`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Jugement du Léviathan I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsqu'il utilise cette compétence, Jinwoo bénéficie de [Super armure]
. Lorsque cette compétence touche sa cible, elle lui inflige l'effet [Glace gelée].

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001602000000` → `1001602000100`
- ID avant/après: `1001602000001` → `1001602000101`
- BaseSkillInfoKey avant/après: `1001602000001` → `1001602000101`
- Buff IDs avant: `1200191000,1001602000004`
- Buff IDs après: `1200191000,1001602000004,1001602000001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Jugement du Léviathan II → III

Dégâts directs        : inchangés
ATK coeff             : 4.68 → 4.88
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.2 (+4.27%)

Données sources :
- SkillGroupID avant/après: `1001602000100` → `1001602000200`
- ID avant/après: `1001602000101` → `1001602000201`
- BaseSkillInfoKey avant/après: `1001602000101` → `1001602000201`
- Buff IDs avant: `1200191000,1001602000004,1001602000001`
- Buff IDs après: `1200191000,1001602000004,1001602000001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Jugement du Léviathan III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsqu'il utilise cette compétence, Jinwoo bénéficie de [Super armure]
. Lorsque cette compétence touche sa cible, elle lui inflige l'effet [Glace gelée].
Les ennemis se trouvant dans la zone pluvieuse subissent davantage de dégâts d'[eau].

NOUVEL EFFET
- ChangeDamageOnElementType: +5% dégâts élémentaires conditionnels (FORTEMENT PROBABLE; bonus interne 500, élément/type 1)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- ChangeDamageOnElementType: +5% dégâts élémentaires conditionnels (FORTEMENT PROBABLE; bonus interne 500, élément/type 1)

Données sources :
- SkillGroupID avant/après: `1001602000200` → `1001602000300`
- ID avant/après: `1001602000201` → `1001602000301`
- BaseSkillInfoKey avant/après: `1001602000201` → `1001602000301`
- Buff IDs avant: `1200191000,1001602000004,1001602000001`
- Buff IDs après: `1001602000002,1200191000,1001602000004,1001602000001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Éclat de lumière I → II

Dégâts directs        : inchangés
ATK coeff             : 2.6 → 2.68
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque la première attaque de Jinwoo touche, elle inflige l'effet [Paralysie] à la cible.

NOUVEL EFFET
- Paralysie
- Paralysie/immobilisation 0.06 s (FORTEMENT PROBABLE; interne 60)

Gain réel :
Gain direct :
- ATK coeff: +0.0800002 (+3.08%)
Utilitaire :
- Paralysie/immobilisation 0.06 s (FORTEMENT PROBABLE; interne 60)
Changement de mécanique :
- Paralysie

Données sources :
- SkillGroupID avant/après: `1001626000000` → `1001626000100`
- ID avant/après: `1001626000001` → `1001626000101`
- BaseSkillInfoKey avant/après: `1001626000001` → `1001626000101`
- Buff IDs avant: ``
- Buff IDs après: `200020004001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Éclat de lumière II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque la première attaque de Jinwoo touche, elle inflige l'effet [Paralysie] à la cible.
Augmente les dégâts d'[Éclat de lumière] infligés aux cibles touchées par l'effet [Paralysie].

NOUVEL EFFET
- IncreaseDamageByTargetSpecialState: +50% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 5000, cible 626/22 "paralysis")

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- IncreaseDamageByTargetSpecialState: +50% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 5000, cible 626/22 "paralysis")

Données sources :
- SkillGroupID avant/après: `1001626000100` → `1001626000200`
- ID avant/après: `1001626000101` → `1001626000201`
- BaseSkillInfoKey avant/après: `1001626000101` → `1001626000201`
- Buff IDs avant: `200020004001`
- Buff IDs après: `200020004001,200020004002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Éclat de lumière III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001626000200` → `1001626000300`
- ID avant/après: `1001626000201` → `1001626000301`
- BaseSkillInfoKey avant/après: `1001626000201` → `1001626000301`
- Buff IDs avant: `200020004001,200020004002`
- Buff IDs après: `200020004001,200020004002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vile attaque sournoise I → II

Dégâts directs        : inchangés
ATK coeff             : 1.43 → 1.49
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque les ennemis marchent sur les tuiles empoisonnées, ils déclenchent l'effet [Poison].

NOUVEL EFFET
- AttFR: -10% (FORTEMENT PROBABLE; valeur interne -1000)
- LevelDotDamage: paramètres internes 6, 4000, 0

Gain réel :
Gain direct :
- ATK coeff: +0.0600001 (+4.2%)
Gain conditionnel :
- AttFR: -10% (FORTEMENT PROBABLE; valeur interne -1000)
Changement de mécanique :
- LevelDotDamage: paramètres internes 6, 4000, 0

Données sources :
- SkillGroupID avant/après: `1001706000000` → `1001706000100`
- ID avant/après: `1001706000001` → `1001706000101`
- BaseSkillInfoKey avant/après: `1001706000001` → `1001706000101`
- Buff IDs avant: ``
- Buff IDs après: `200010008001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vile attaque sournoise II → III

Dégâts directs        : inchangés
ATK coeff             : 1.49 → 2.35
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque les ennemis entrent en contact avec le brouillard toxique, ils subissent l'effet [Poison].

Gain réel :
Gain direct :
- ATK coeff: +0.86 (+57.7%)

Données sources :
- SkillGroupID avant/après: `1001706000100` → `1001706000200`
- ID avant/après: `1001706000101` → `1001706000201`
- BaseSkillInfoKey avant/après: `1001706000101` → `1001706000201`
- Buff IDs avant: `200010008001`
- Buff IDs après: `200010008001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Vile attaque sournoise III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque les ennemis entrent en contact avec le brouillard toxique, ils subissent l'effet [Poison].
Les dégâts infligés aux cibles touchées par l'effet [Poison] augmentent.

NOUVEL EFFET
- SkillDamageIncreaseOnBuffedTarget: +10% dégâts contre cible avec buff (FORTEMENT PROBABLE; bonus interne 1000, paramètres 0/75)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- SkillDamageIncreaseOnBuffedTarget: +10% dégâts contre cible avec buff (FORTEMENT PROBABLE; bonus interne 1000, paramètres 0/75)

Données sources :
- SkillGroupID avant/après: `1001706000200` → `1001706000300`
- ID avant/après: `1001706000201` → `1001706000301`
- BaseSkillInfoKey avant/après: `1001706000201` → `1001706000301`
- Buff IDs avant: `200010008001`
- Buff IDs après: `200010008001,200010008002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Incinération I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque l'utilisateur réactive cette compétence au bon moment alors que l'énergie de feu est concentrée, une explosion supplémentaire se déclenche.

NOUVEL EFFET
- SkillChange: remplace/cible skill group 1001720000300 -> 1001720000400
- payload référencé 1001720000101: ATK 1.78, DEF 0, HP 0, CD 35 s, MP 291
- EnhanceElementValue: paramètres internes 1, 100, 720
- SkillChange: remplace/cible skill group 1001720000100 -> 1001720000500
- SkillTreeMpCost: -10% coût MP (FORTEMENT PROBABLE; interne -1000)
- payload référencé 1001720000601: ATK 0.9, DEF 0, HP 0, CD 0 s, MP 0
- Lorsque l'utilisateur applique Éclatement, les effets [Insufflation de points de mana] ou [Récupération de points de mana] s'appliquent selon la quantité de PM restante. Si les PM de l'utilisateur sont de {TriggerOptionValue2,1} % ou plus, l'effet est activé.

Lorsque l'utilisateur applique Éclatement, ses dégâts de compétence augmentent de {Buff,10186,SpecialState1OptionValue2,0.01} %, mais {Buff,10186,SpecialState2OptionValue2,-0.01} % de ses PM max sont consommés. Si les PM de l'utilisateur sont de {Buff,10184,TriggerOptionValue2} % ou moins, l'effet est activé.

L'utilisateur récupère {Buff,10189,SpecialState1OptionValue2,0.01} % de ses PM pour chaque cible touchée par Éclatement.
- SkillChange: remplace/cible skill group 1001720000300 -> 1001720000500
- payload référencé 1001720000201: ATK 1.78, DEF 0, HP 0, CD 35 s, MP 291
- payload référencé 1001720000401: ATK 0, DEF 0, HP 0, CD 0 s, MP 0
- SkillCast: lance skill group 1001720000600
- SkillChange: remplace/cible skill group 1001720000200 -> 1001720000500
- SkillTreeEnhance: +5% dégâts de compétence (FORTEMENT PROBABLE; interne 500)
- SkillChange: remplace/cible skill group 1001720000200 -> 1001720000400
- payload référencé 1001720000301: ATK 1.89, DEF 0, HP 0, CD 35 s, MP 291
- payload référencé 1001720000501: ATK 0, DEF 0, HP 0, CD 0 s, MP 0
- SkillChange: remplace/cible skill group 1001720000100 -> 1001720000400

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Utilitaire :
- SkillChange: remplace/cible skill group 1001720000300 -> 1001720000400
- SkillChange: remplace/cible skill group 1001720000100 -> 1001720000500
- SkillChange: remplace/cible skill group 1001720000300 -> 1001720000500
- SkillCast: lance skill group 1001720000600
- SkillChange: remplace/cible skill group 1001720000200 -> 1001720000500
- SkillChange: remplace/cible skill group 1001720000200 -> 1001720000400
- SkillChange: remplace/cible skill group 1001720000100 -> 1001720000400
Changement de mécanique :
- payload référencé 1001720000101: ATK 1.78, DEF 0, HP 0, CD 35 s, MP 291
- EnhanceElementValue: paramètres internes 1, 100, 720
- SkillTreeMpCost: -10% coût MP (FORTEMENT PROBABLE; interne -1000)
- payload référencé 1001720000601: ATK 0.9, DEF 0, HP 0, CD 0 s, MP 0
- Lorsque l'utilisateur applique Éclatement, les effets [Insufflation de points de mana] ou [Récupération de points de mana] s'appliquent selon la quantité de PM restante. Si les PM de l'utilisateur sont de {TriggerOptionValue2,1} % ou plus, l'effet est activé.

Lorsque l'utilisateur applique Éclatement, ses dégâts de compétence augmentent de {Buff,10186,SpecialState1OptionValue2,0.01} %, mais {Buff,10186,SpecialState2OptionValue2,-0.01} % de ses PM max sont consommés. Si les PM de l'utilisateur sont de {Buff,10184,TriggerOptionValue2} % ou moins, l'effet est activé.

L'utilisateur récupère {Buff,10189,SpecialState1OptionValue2,0.01} % de ses PM pour chaque cible touchée par Éclatement.
- payload référencé 1001720000201: ATK 1.78, DEF 0, HP 0, CD 35 s, MP 291
- payload référencé 1001720000401: ATK 0, DEF 0, HP 0, CD 0 s, MP 0
- SkillTreeEnhance: +5% dégâts de compétence (FORTEMENT PROBABLE; interne 500)
- payload référencé 1001720000301: ATK 1.89, DEF 0, HP 0, CD 35 s, MP 291
- payload référencé 1001720000501: ATK 0, DEF 0, HP 0, CD 0 s, MP 0

Données sources :
- SkillGroupID avant/après: `1001720000000` → `1001720000100`
- ID avant/après: `1001720000001` → `1001720000101`
- BaseSkillInfoKey avant/après: `1001720000001` → `1001720000101`
- Buff IDs avant: ``
- Buff IDs après: `10185,10187`
- SkillChange/SkillCast payload IDs suivis: `1001720000101,1001720000601,1001720000201,1001720000401,1001720000301,1001720000501`
- SkillChange/SkillCast refs brutes: `1001720000300,1001720000400,1001720000100,1001720000500,1001720000300,1001720000500,1001720000600,1001720000200,1001720000500,1001720000200,1001720000400,1001720000100,1001720000400`

# Incinération II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque Jinwoo réactive cette compétence au bon moment alors que l'énergie de feu est concentrée, une explosion supplémentaire se déclenche. Les dégâts de toutes ses compétences de combat passives de [Magicien élémentaire] augmentent et sa consommation de MP diminue.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001720000100` → `1001720000200`
- ID avant/après: `1001720000101` → `1001720000201`
- BaseSkillInfoKey avant/après: `1001720000101` → `1001720000201`
- Buff IDs avant: `10185,10187`
- Buff IDs après: `10185,10187,10183`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Incinération III → IV

Dégâts directs        : inchangés
ATK coeff             : 1.78 → 1.89
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.11 (+6.18%)

Données sources :
- SkillGroupID avant/après: `1001720000200` → `1001720000300`
- ID avant/après: `1001720000201` → `1001720000301`
- BaseSkillInfoKey avant/après: `1001720000201` → `1001720000301`
- Buff IDs avant: `10185,10187,10183`
- Buff IDs après: `10185,10188,10187,10183`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Destruction terrestre I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque cette compétence est utilisée, l'utilisateur obtient un [Bouclier].

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001725000000` → `1001725000100`
- ID avant/après: `1001725000001` → `1001725000101`
- BaseSkillInfoKey avant/après: `1001725000001` → `1001725000101`
- Buff IDs avant: `1420000020`
- Buff IDs après: `1420000020,200010011001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Destruction terrestre II → III

Dégâts directs        : inchangés
ATK coeff             : 2.33 → 0
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque Sung Jinwoo utilise cette compétence, il obtient un [Bouclier] pendant un certain temps.

Gain réel :
Gain direct :
- ATK coeff: -2.33 (-100%)

Données sources :
- SkillGroupID avant/après: `1001725000100` → `1001725000200`
- ID avant/après: `1001725000101` → `1001725000201`
- BaseSkillInfoKey avant/après: `1001725000101` → `1001725000201`
- Buff IDs avant: `1420000020,200010011001`
- Buff IDs après: `1420000020,200010011001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Destruction terrestre III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- payload référencé 1001828000001: ATK 0.07, DEF 0, HP 0, CD 0 s, MP 0
- SkillCast: lance skill group 1001828000000

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Utilitaire :
- SkillCast: lance skill group 1001828000000
Changement de mécanique :
- payload référencé 1001828000001: ATK 0.07, DEF 0, HP 0, CD 0 s, MP 0

Données sources :
- SkillGroupID avant/après: `1001725000200` → `1001725000300`
- ID avant/après: `1001725000201` → `1001725000301`
- BaseSkillInfoKey avant/après: `1001725000201` → `1001725000301`
- Buff IDs avant: `1420000020,200010011001`
- Buff IDs après: `200010011003,1420000020,200010011001`
- SkillChange/SkillCast payload IDs suivis: `1001828000001`
- SkillChange/SkillCast refs brutes: `1001828000000`

# Charge explosive I → II

Dégâts directs        : inchangés
ATK coeff             : 4.66 → 7.06
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo fonce vers l'avant, concentre une énergie puissante et assène une frappe vers le bas.

Gain réel :
Gain direct :
- ATK coeff: +2.4 (+51.5%)

Données sources :
- SkillGroupID avant/après: `1001735000000` → `1001735000100`
- ID avant/après: `1001735000001` → `1001735000101`
- BaseSkillInfoKey avant/après: `1001735000001` → `1001735000101`
- Buff IDs avant: `1420000020`
- Buff IDs après: `1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Charge explosive II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les chances de coup critique de Jinwoo augmentent considérablement, et il inflige un puissant effet de déséquilibre à l'ennemi.

NOUVEL EFFET
- L'effet [Force d'orc] s'applique également en cas de Coup critique réussi.
Augmente les chance qu'Épée longue d'orc inflige un Coup critique de {SpecialState1OptionValue1,0.01} %.
- CriticalRate: +20% (CONFIRMÉ par placeholders 0.01 quand présents; interne 2000)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- L'effet [Force d'orc] s'applique également en cas de Coup critique réussi.
Augmente les chance qu'Épée longue d'orc inflige un Coup critique de {SpecialState1OptionValue1,0.01} %.
- CriticalRate: +20% (CONFIRMÉ par placeholders 0.01 quand présents; interne 2000)

Données sources :
- SkillGroupID avant/après: `1001735000100` → `1001735000200`
- ID avant/après: `1001735000101` → `1001735000201`
- BaseSkillInfoKey avant/après: `1001735000101` → `1001735000201`
- Buff IDs avant: `1420000020`
- Buff IDs après: `10167,10169,1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Charge explosive III → IV

Dégâts directs        : inchangés
ATK coeff             : 7.06 → 7.44
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Les chances de coup critique de Jinwoo augmentent considérablement, et il inflige un puissant effet de déséquilibre à l'ennemi. Lorsque cette compétence est utilisée, Jinwoo bénéficie de l'effet [Immunité aux dégâts].

NOUVEL EFFET
- Immunité aux dégâts (HYPOTHÈSE durée/valeur interne 100)

Gain réel :
Gain direct :
- ATK coeff: +0.38 (+5.38%)
Gain défensif :
- Immunité aux dégâts (HYPOTHÈSE durée/valeur interne 100)

Données sources :
- SkillGroupID avant/après: `1001735000200` → `1001735000300`
- ID avant/après: `1001735000201` → `1001735000301`
- BaseSkillInfoKey avant/après: `1001735000201` → `1001735000301`
- Buff IDs avant: `10167,10169,1420000020`
- Buff IDs après: `10851,10167,10169,1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo obtient [Super armure] pendant l'utilisation de cette compétence.

NOUVEL EFFET
- Super armure
- Super armure / immunité aux réactions (CONFIRMÉ par description)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain défensif :
- Super armure / immunité aux réactions (CONFIRMÉ par description)
Changement de mécanique :
- Super armure

Données sources :
- SkillGroupID avant/après: `1001745000000` → `1001745000100`
- ID avant/après: `1001745000001` → `1001745000101`
- BaseSkillInfoKey avant/après: `1001745000001` → `1001745000101`
- Buff IDs avant: ``
- Buff IDs après: `1200191000`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo obtient [Super armure] pendant l'utilisation de cette compétence.
Déclenche l'effet [Pénétration de défense augmentée] pendant l'utilisation de cette compétence.

NOUVEL EFFET
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Données sources :
- SkillGroupID avant/après: `1001745000100` → `1001745000200`
- ID avant/après: `1001745000101` → `1001745000201`
- BaseSkillInfoKey avant/après: `1001745000101` → `1001745000201`
- Buff IDs avant: `1200191000`
- Buff IDs après: `1200191000,200010012001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo obtient [Super armure] pendant l'utilisation de cette compétence.
Déclenche l'effet [Pénétration de défense augmentée] pendant l'utilisation de cette compétence.
Augmente les dégâts infligés aux cibles déséquilibrées pendant l'utilisation de cette compétence.

NOUVEL EFFET
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Données sources :
- SkillGroupID avant/après: `1001745000200` → `1001745000300`
- ID avant/après: `1001745000201` → `1001745000301`
- BaseSkillInfoKey avant/après: `1001745000201` → `1001745000301`
- Buff IDs avant: `1200191000,200010012001`
- Buff IDs après: `1200191000,200010012001,200010012002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tir rapide de phénix I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de [Tir rapide de phénix] augmente les dégâts d'[Embrasement] pendant un certain temps.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001755010000` → `1001755010100`
- ID avant/après: `1001755010001` → `1001755010101`
- BaseSkillInfoKey avant/après: `1001755010001` → `1001755010101`
- Buff IDs avant: ``
- Buff IDs après: `10770`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tir rapide de phénix II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de [Tir rapide de phénix] augmente les dégâts d'[Embrasement] pendant un certain temps.
Le nombre de phénix tirés avec [Frappe en chaîne] augmente.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001755010100` → `1001755010200`
- ID avant/après: `1001755010101` → `1001755010201`
- BaseSkillInfoKey avant/après: `1001755010101` → `1001755010201`
- Buff IDs avant: `10770`
- Buff IDs après: `10770`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tir rapide de phénix III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
L'utilisation de [Tir rapide de phénix] augmente les dégâts d'[Embrasement] pendant un certain temps.
Le nombre de phénix tirés avec [Frappe en chaîne] augmente.
Après l'utilisation de [Tir rapide de phénix], les dégâts de la [Frappe en chaîne] de l'Âme de phénix augmentent pendant un certain temps.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001755010200` → `1001755010300`
- ID avant/après: `1001755010201` → `1001755010301`
- BaseSkillInfoKey avant/après: `1001755010201` → `1001755010301`
- Buff IDs avant: `10770`
- Buff IDs après: `10770,10772`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Barrage d'aiguilles empoisonnées I → II

Dégâts directs        : inchangés
ATK coeff             : 1.62 → 1.64
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Si l'utilisateur est touché en plein air pendant l'utilisation de cette compétence, cela déclenche [Évasion extrême].

Gain réel :
Gain direct :
- ATK coeff: +0.02 (+1.23%)

Données sources :
- SkillGroupID avant/après: `1001603000000` → `1001603000100`
- ID avant/après: `1001603000001` → `1001603000101`
- BaseSkillInfoKey avant/après: `1001603000001` → `1001603000101`
- Buff IDs avant: ``
- Buff IDs après: ``
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Barrage d'aiguilles empoisonnées II → III

Dégâts directs        : inchangés
ATK coeff             : 1.64 → 2.14
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Si l'utilisateur est touché en plein air pendant l'utilisation de cette compétence, cela déclenche [Évasion extrême].
Traverser la zone toxique déclenche l'effet [Poison mortel d'Arachné].

NOUVEL EFFET
- Poison mortel d'Arachné
- AttFR: -10% (FORTEMENT PROBABLE; valeur interne -1000)
- LevelDotDamage: paramètres internes 6, 4000, 0

Gain réel :
Gain direct :
- ATK coeff: +0.5 (+30.5%)
Gain conditionnel :
- AttFR: -10% (FORTEMENT PROBABLE; valeur interne -1000)
Changement de mécanique :
- Poison mortel d'Arachné
- LevelDotDamage: paramètres internes 6, 4000, 0

Données sources :
- SkillGroupID avant/après: `1001603000100` → `1001603000200`
- ID avant/après: `1001603000101` → `1001603000201`
- BaseSkillInfoKey avant/après: `1001603000101` → `1001603000201`
- Buff IDs avant: ``
- Buff IDs après: `200010001001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Feu destructeur I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo bénéficie d'une [Immunité aux dégâts] pendant l'utilisation de cette compétence.
Lorsque cette compétence touche sa cible, les dégâts de [Déséquilibre] subis augmentent pendant un certain temps.
Plus les PV de Jinwoo sont bas, plus sa rage s'intensifie, ce qui augmente les dégâts de [Feu destructeur].

NOUVEL EFFET
- RemainHpDamageUp: paramètres internes 6000, 604, 0

EFFET SUPPRIMÉ
- MonsterGradeDamage: paramètres internes 3, 1000, 0
- MonsterGradeDamage: paramètres internes 2, 1000, 0

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- RemainHpDamageUp: paramètres internes 6000, 604, 0

Données sources :
- SkillGroupID avant/après: `1001604000000` → `1001604000100`
- ID avant/après: `1001604000001` → `1001604000101`
- BaseSkillInfoKey avant/après: `1001604000001` → `1001604000101`
- Buff IDs avant: `200032003002,2999000804,200032003001,1420000020`
- Buff IDs après: `200032003002,200032003001,200032003003,1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Feu destructeur II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo bénéficie d'une [Immunité aux dégâts] pendant l'utilisation de cette compétence.
Lorsque cette compétence touche sa cible, les dégâts de [Déséquilibre] subis augmentent pendant un certain temps.
Plus les PV de Jinwoo sont bas, plus sa rage s'intensifie, ce qui augmente les dégâts de [Feu destructeur].
Lorsque sa frappe descendante touche la cible, les dégâts de Météorite augmentent.

NOUVEL EFFET
- EnhanceSkillDamageFix: paramètres internes 604, 12000, 1

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- EnhanceSkillDamageFix: paramètres internes 604, 12000, 1

Données sources :
- SkillGroupID avant/après: `1001604000100` → `1001604000200`
- ID avant/après: `1001604000101` → `1001604000201`
- BaseSkillInfoKey avant/après: `1001604000101` → `1001604000201`
- Buff IDs avant: `200032003002,200032003001,200032003003,1420000020`
- Buff IDs après: `200032003002,200032003004,200032003001,200032003003,1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Énergie d'épée à 3 millions de wons I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque Jinwoo utilise cette compétence, les effets [Attaque augmentée] et [Défense augmentée] sont déclenchés.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001605000000` → `1001605000100`
- ID avant/après: `1001605000001` → `1001605000101`
- BaseSkillInfoKey avant/après: `1001605000001` → `1001605000101`
- Buff IDs avant: ``
- Buff IDs après: `200010002001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Énergie d'épée à 3 millions de wons II → III

Dégâts directs        : inchangés
ATK coeff             : 3.18 → 4.64
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +1.46 (+45.9%)

Données sources :
- SkillGroupID avant/après: `1001605000100` → `1001605000200`
- ID avant/après: `1001605000101` → `1001605000201`
- BaseSkillInfoKey avant/après: `1001605000101` → `1001605000201`
- Buff IDs avant: `200010002001`
- Buff IDs après: `200010002001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tueur de marcheurs blancs III → IV

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001606010200` → `1001606010300`
- ID avant/après: `1001606010201` → `1001606010301`
- BaseSkillInfoKey avant/après: `1001606010201` → `1001606010301`
- Buff IDs avant: ``
- Buff IDs après: ``
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tueur de marcheurs blancs IV → V

Dégâts directs        : inchangés
ATK coeff             : 2.38 → 2.59
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.21 (+8.82%)

Données sources :
- SkillGroupID avant/après: `1001606010300` → `1001606010400`
- ID avant/après: `1001606010301` → `1001606010401`
- BaseSkillInfoKey avant/après: `1001606010301` → `1001606010401`
- Buff IDs avant: ``
- Buff IDs après: ``
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Chasse à mort I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Plus Jinwoo est éloigné de l'ennemi, plus [Chasse à mort] inflige de dégâts ; à l'inverse, ses dégâts diminuent à courte portée. Lorsqu'il enchaîne les frappes, un effet [Flux] augmentant progressivement l'Attaque s'active pendant un certain temps. Plus il réussit de coups consécutifs, plus la durée de l'effet [Flux] s'allonge.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001607000000` → `1001607000100`
- ID avant/après: `1001607000001` → `1001607000101`
- BaseSkillInfoKey avant/après: `1001607000001` → `1001607000101`
- Buff IDs avant: `200010003001`
- Buff IDs après: `200010003001,200010003002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Chasse à mort II → III

Dégâts directs        : inchangés
ATK coeff             : 2.88 → 3.05
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Plus Jinwoo est éloigné de l'ennemi, plus [Chasse à mort] inflige de dégâts ; à l'inverse, ses dégâts diminuent à courte portée. Lorsqu'il enchaîne les frappes, un effet [Flux] augmentant progressivement l'Attaque s'active pendant un certain temps. Plus il réussit de coups consécutifs, plus la durée de l'effet [Flux] s'allonge. L'effet de [Flux] est grandement amélioré, ce qui facilite son activation.

Gain réel :
Gain direct :
- ATK coeff: +0.17 (+5.9%)

Données sources :
- SkillGroupID avant/après: `1001607000100` → `1001607000400`
- ID avant/après: `1001607000101` → `1001607000401`
- BaseSkillInfoKey avant/après: `1001607000101` → `1001607000401`
- Buff IDs avant: `200010003001,200010003002`
- Buff IDs après: `200010003001,200010003005`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Bourrasque glaciale I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
[Gel] se déclenche lorsque cette compétence touche sa cible.
Lorsque Jinwoo utilise cette compétence, les [dégâts infligés aux monstres normaux] augmentent.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001629000000` → `1001629000100`
- ID avant/après: `1001629000001` → `1001629000101`
- BaseSkillInfoKey avant/après: `1001629000001` → `1001629000101`
- Buff IDs avant: ``
- Buff IDs après: `200020006003,200020006011`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Bourrasque glaciale II → III

Dégâts directs        : inchangés
ATK coeff             : 5.19 → 0
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : 35 s → 27 s
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: -5.19 (-100%)
Utilitaire :
- Cooldown: 35 s -> 27 s

Données sources :
- SkillGroupID avant/après: `1001629000100` → `1001629000200`
- ID avant/après: `1001629000101` → `1001629000201`
- BaseSkillInfoKey avant/après: `1001629000101` → `1001629000201`
- Buff IDs avant: `200020006003,200020006011`
- Buff IDs après: `200020006011`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Faucon du jugement I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
La durée d'Évasion extrême d'[Attaque de combo de ruée] augmente significativement et, lorsqu'Évasion extrême est utilisée, le temps de rechargement de [Faucon du jugement] est réduit de 2 secondes.

NOUVEL EFFET
- payload référencé 1001406000401: ATK 1.33, DEF 0, HP 0, CD 0 s, MP 0
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000400

EFFET MODIFIÉ
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000100 -> SkillChange: remplace/cible skill group 1001101000000 -> 1001406000400

EFFET SUPPRIMÉ
- payload référencé 1001406000101: ATK 1.33, DEF 0, HP 0, CD 0 s, MP 0
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000100

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Utilitaire :
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000400
Changement de mécanique :
- payload référencé 1001406000401: ATK 1.33, DEF 0, HP 0, CD 0 s, MP 0

Données sources :
- SkillGroupID avant/après: `1001639000000` → `1001639000300`
- ID avant/après: `1001639000001` → `1001639000301`
- BaseSkillInfoKey avant/après: `1001639000001` → `1001639000301`
- Buff IDs avant: `200020007001`
- Buff IDs après: `200020007002,200020007007`
- SkillChange/SkillCast payload IDs suivis: `1001406000401,1001406000101`
- SkillChange/SkillCast refs brutes: `1001101000000,1001406000400,1001101000000,1001406000100`

# Faucon du jugement II → III

Dégâts directs        : inchangés
ATK coeff             : 2.66 → 2.81
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
La durée d'Évasion extrême d'une [Attaque de combo de ruée] augmente significativement et, lorsqu'Évasion extrême est utilisée, elle réduit le temps de rechargement de [Faucon du jugement] de 2 secondes. Les dégâts de l'utilisateur augmentent aussi significativement pendant une courte période, et les ennemis touchés subissent l'effet [Paralysie].

NOUVEL EFFET
- payload référencé 1001406000701: ATK 1.4, DEF 0, HP 0, CD 0 s, MP 0
- Paralysie/immobilisation 0.03 s (FORTEMENT PROBABLE; interne 30)
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000700

EFFET MODIFIÉ
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000400 -> SkillChange: remplace/cible skill group 1001101000000 -> 1001406000700

EFFET SUPPRIMÉ
- payload référencé 1001406000401: ATK 1.33, DEF 0, HP 0, CD 0 s, MP 0
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000400

Gain réel :
Gain direct :
- ATK coeff: +0.15 (+5.64%)
Utilitaire :
- Paralysie/immobilisation 0.03 s (FORTEMENT PROBABLE; interne 30)
- SkillChange: remplace/cible skill group 1001101000000 -> 1001406000700
Changement de mécanique :
- payload référencé 1001406000701: ATK 1.4, DEF 0, HP 0, CD 0 s, MP 0

Données sources :
- SkillGroupID avant/après: `1001639000300` → `1001639000600`
- ID avant/après: `1001639000301` → `1001639000601`
- BaseSkillInfoKey avant/après: `1001639000301` → `1001639000601`
- Buff IDs avant: `200020007002,200020007007`
- Buff IDs après: `200020007005,200020007008,200020007006`
- SkillChange/SkillCast payload IDs suivis: `1001406000701,1001406000401`
- SkillChange/SkillCast refs brutes: `1001101000000,1001406000700,1001101000000,1001406000400`

# Rémanence I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Si Jinwoo utilise cette compétence juste après avoir changé d'arme, l'effet [Foudre] l'entoure pendant un certain temps, augmentant fortement son Taux de coup critique. Les cibles touchées par la foudre subissent également l'effet [Paralysie] pendant un court instant.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001653000000` → `1001653000100`
- ID avant/après: `1001653000001` → `1001653000101`
- BaseSkillInfoKey avant/après: `1001653000001` → `1001653000101`
- Buff IDs avant: ``
- Buff IDs après: `10292`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Rémanence II → III

Dégâts directs        : inchangés
ATK coeff             : 2.82 → 5.99
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Si Jinwoo utilise cette compétence juste après avoir changé d'arme, l'effet [Foudre] l'entoure pendant un certain temps, augmentant fortement son Taux de coup critique. Les cibles touchées par la foudre subissent également l'effet [Paralysie] pendant un certain temps.

Gain réel :
Gain direct :
- ATK coeff: +3.17 (+112%)

Données sources :
- SkillGroupID avant/après: `1001653000100` → `1001653000200`
- ID avant/après: `1001653000101` → `1001653000201`
- BaseSkillInfoKey avant/après: `1001653000101` → `1001653000201`
- Buff IDs avant: `10292`
- Buff IDs après: `10294`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Transpercement de lézard I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque la troisième [Attaque de base] de l'utilisateur touche sa cible, elle augmente les dégâts de [Transpercement de lézard]

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001658000000` → `1001658000100`
- ID avant/après: `1001658000001` → `1001658000101`
- BaseSkillInfoKey avant/après: `1001658000001` → `1001658000101`
- Buff IDs avant: `1420000021`
- Buff IDs après: `1420000021,200010006001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Transpercement de lézard II → III

Dégâts directs        : inchangés
ATK coeff             : 3.24 → 5.67
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +2.43 (+75%)

Données sources :
- SkillGroupID avant/après: `1001658000100` → `1001658000200`
- ID avant/après: `1001658000101` → `1001658000201`
- BaseSkillInfoKey avant/après: `1001658000101` → `1001658000201`
- Buff IDs avant: `1420000021,200010006001`
- Buff IDs après: `1420000021,200010006001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo obtient [Super armure] en appuyant longuement sur ce bouton.
Augmente les Dégâts de coup critique et le Taux de coup critique de [Récolte d'esprits].

NOUVEL EFFET
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Données sources :
- SkillGroupID avant/après: `1001696000000` → `1001696000100`
- ID avant/après: `1001696000001` → `1001696000101`
- BaseSkillInfoKey avant/après: `1001696000001` → `1001696000101`
- Buff IDs avant: `200020005101,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits II → III

Dégâts directs        : inchangés
ATK coeff             : 1.14 → 1.76
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +0.62 (+54.4%)

Données sources :
- SkillGroupID avant/après: `1001696000100` → `1001696000200`
- ID avant/après: `1001696000101` → `1001696000201`
- BaseSkillInfoKey avant/après: `1001696000101` → `1001696000201`
- Buff IDs avant: `200020005101,200020005102,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Données sources :
- SkillGroupID avant/après: `1001696010000` → `1001696010100`
- ID avant/après: `1001696010001` → `1001696010101`
- BaseSkillInfoKey avant/après: `1001696010001` → `1001696010101`
- Buff IDs avant: `200020005101,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits II → III

Dégâts directs        : inchangés
ATK coeff             : 8.04 → 12.35
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +4.31 (+53.6%)

Données sources :
- SkillGroupID avant/après: `1001696010100` → `1001696010200`
- ID avant/après: `1001696010101` → `1001696010201`
- BaseSkillInfoKey avant/après: `1001696010101` → `1001696010201`
- Buff IDs avant: `200020005101,200020005102,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Changement de mécanique :
- CriticalDamage: paramètres internes 5000, 696, 0
- CriticalRate: +15% (CONFIRMÉ par placeholders 0.01 quand présents; interne 1500)

Données sources :
- SkillGroupID avant/après: `1001696020000` → `1001696020100`
- ID avant/après: `1001696020001` → `1001696020101`
- BaseSkillInfoKey avant/après: `1001696020001` → `1001696020101`
- Buff IDs avant: `200020005101,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Récolte d'esprits II → III

Dégâts directs        : inchangés
ATK coeff             : 2.29 → 3.53
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- ATK coeff: +1.24 (+54.1%)

Données sources :
- SkillGroupID avant/après: `1001696020100` → `1001696020200`
- ID avant/après: `1001696020101` → `1001696020201`
- BaseSkillInfoKey avant/après: `1001696020101` → `1001696020201`
- Buff IDs avant: `200020005101,200020005102,1420000021`
- Buff IDs après: `200020005101,200020005102,1420000021`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Éclair final I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo bénéficie d'une [Immunité aux dégâts] pendant l'utilisation de cette compétence.
Lorsque cette compétence touche sa cible, cela déclenche l'effet [Électrocution] sur cette dernière.
Augmente les dégâts d'[Éclair final] infligés aux cibles affectées par l'effet [Électrocution].

NOUVEL EFFET
- IncreaseDamageByTargetBuff: +90% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 9000, cible 716/200030001001 )

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- IncreaseDamageByTargetBuff: +90% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 9000, cible 716/200030001001 )

Données sources :
- SkillGroupID avant/après: `1001716000000` → `1001716000100`
- ID avant/après: `1001716000001` → `1001716000101`
- BaseSkillInfoKey avant/après: `1001716000001` → `1001716000101`
- Buff IDs avant: `200030001001,200030001003`
- Buff IDs après: `200030001001,200030001002,200030001003`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Éclair final II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001716000100` → `1001716000200`
- ID avant/après: `1001716000101` → `1001716000201`
- BaseSkillInfoKey avant/après: `1001716000101` → `1001716000201`
- Buff IDs avant: `200030001001,200030001002,200030001003`
- Buff IDs après: `200030001001,200030001002,200030001003`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Yeux luisants I → II

Dégâts directs        : inchangés
ATK coeff             : 2.93 → 3.09
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque le sol explose, une seconde détonation se produit aléatoirement pendant un certain temps.

Gain réel :
Gain direct :
- ATK coeff: +0.16 (+5.46%)

Données sources :
- SkillGroupID avant/après: `1001740000000` → `1001740000100`
- ID avant/après: `1001740000001` → `1001740000101`
- BaseSkillInfoKey avant/après: `1001740000001` → `1001740000101`
- Buff IDs avant: ``
- Buff IDs après: ``
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Yeux luisants II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lors d'une explosion, une seconde détonation se produit aléatoirement pendant un certain temps.
Les cibles touchées par cette détonation subissent davantage de dégâts de [lumière].

NOUVEL EFFET
- ChangeDamageOnElementType: +0.27% dégâts élémentaires conditionnels (FORTEMENT PROBABLE; bonus interne 27, élément/type 1)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- ChangeDamageOnElementType: +0.27% dégâts élémentaires conditionnels (FORTEMENT PROBABLE; bonus interne 27, élément/type 1)

Données sources :
- SkillGroupID avant/après: `1001740000100` → `1001740000200`
- ID avant/après: `1001740000101` → `1001740000201`
- BaseSkillInfoKey avant/après: `1001740000101` → `1001740000201`
- Buff IDs avant: ``
- Buff IDs après: `200010010001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé II → III

Dégâts directs        : inchangés
ATK coeff             : 2.16 → 2.22
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Gain réel :
Gain direct :
- ATK coeff: +0.0599999 (+2.78%)
Gain conditionnel :
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Données sources :
- SkillGroupID avant/après: `1001745010100` → `1001745010200`
- ID avant/après: `1001745010101` → `1001745010201`
- BaseSkillInfoKey avant/après: `1001745010101` → `1001745010201`
- Buff IDs avant: `1200191000`
- Buff IDs après: `1200191000,200010012001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé III → IV

Dégâts directs        : inchangés
ATK coeff             : 2.22 → 3.55
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Gain réel :
Gain direct :
- ATK coeff: +1.33 (+59.9%)
Gain conditionnel :
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Données sources :
- SkillGroupID avant/après: `1001745010200` → `1001745010300`
- ID avant/après: `1001745010201` → `1001745010301`
- BaseSkillInfoKey avant/après: `1001745010201` → `1001745010301`
- Buff IDs avant: `1200191000,200010012001`
- Buff IDs après: `1200191000,200010012001,200010012002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé II → III

Dégâts directs        : inchangés
ATK coeff             : 0.54 → 0.55
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Gain réel :
Gain direct :
- ATK coeff: +0.00999999 (+1.85%)
Gain conditionnel :
- ArmPenP: 15% (FORTEMENT PROBABLE; valeur interne 1500)

Données sources :
- SkillGroupID avant/après: `1001745020100` → `1001745020200`
- ID avant/après: `1001745020101` → `1001745020201`
- BaseSkillInfoKey avant/après: `1001745020101` → `1001745020201`
- Buff IDs avant: `1200191000`
- Buff IDs après: `1200191000,200010012001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Tonnerre ébranlé III → IV

Dégâts directs        : inchangés
ATK coeff             : 0.55 → 0.88
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Gain réel :
Gain direct :
- ATK coeff: +0.33 (+60%)
Gain conditionnel :
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/201 )
- IncreaseDamageByTargetSpecialState: +60% dégâts conditionnels (FORTEMENT PROBABLE; bonus interne 6000, cible 745/20 )

Données sources :
- SkillGroupID avant/après: `1001745020200` → `1001745020300`
- ID avant/après: `1001745020201` → `1001745020301`
- BaseSkillInfoKey avant/après: `1001745020201` → `1001745020301`
- Buff IDs avant: `1200191000,200010012001`
- Buff IDs après: `1200191000,200010012001,200010012002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Rédemption de la Terre I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque l'[Attaque de base] de Jinwoo touche un allié, il récupère une petite quantité de PV. Lors de l'utilisation de cette compétence, il obtient un grand [Bouclier]. Lorsqu'il entame un combat, les dégâts subis par Sung Jinwoo diminuent considérablement.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001839000000` → `1001839000200`
- ID avant/après: `1001839000001` → `1001839000201`
- BaseSkillInfoKey avant/après: `1001839000001` → `1001839000201`
- Buff IDs avant: `1420000020`
- Buff IDs après: `1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Rédemption de la Terre II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001839000200` → `1001839000400`
- ID avant/après: `1001839000201` → `1001839000401`
- BaseSkillInfoKey avant/après: `1001839000201` → `1001839000401`
- Buff IDs avant: `1420000020`
- Buff IDs après: `200030019005,1420000020`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Rage obscure I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque [Rage obscure], [Frappe en chaîne] ou [Attaque lourde : Attaque niveau 2] touche une cible, elle subit temporairement [Flamme noire].
[Flamme noire] : augmente légèrement les dégâts subis.

NOUVEL EFFET
- temp//적에게 적용
- DamReduP: -8% (FORTEMENT PROBABLE; valeur interne -800)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain défensif :
- DamReduP: -8% (FORTEMENT PROBABLE; valeur interne -800)
Changement de mécanique :
- temp//적에게 적용

Données sources :
- SkillGroupID avant/après: `1001843000000` → `1001843000100`
- ID avant/après: `1001843000001` → `1001843000101`
- BaseSkillInfoKey avant/après: `1001843000001` → `1001843000101`
- Buff IDs avant: ``
- Buff IDs après: `200011000001`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Rage obscure II → III

Dégâts directs        : inchangés
ATK coeff             : 4.09 → 0
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Lorsque [Rage obscure], [Frappe en chaîne] ou [Attaque lourde : Attaque niveau 2] touche une cible, elle subit temporairement [Flamme noire].
[Flamme noire] : augmente légèrement les dégâts subis.

[Rage obscure] se transforme en compétence à effet de charge, augmentant ses dégâts proportionnellement au temps de charge.
L'utilisation de [Rage obscure] disperse des flammes noires autour de l'utilisateur, infligeant les effets [Flamme noire] et des dégâts.
Infliger de nouveau [Flamme noire] à la cible invoque un météore qui s'abat sur elle, inflige des dégâts et dissipe tous les effets [Flamme noire] existants de la cible.

NOUVEL EFFET
- temp//성진우에게 적용
- temp//성진우에게 적용
- temp//성진우에게 적용

EFFET SUPPRIMÉ
- temp//적에게 적용
- DamReduP: -8% (FORTEMENT PROBABLE; valeur interne -800)

Gain réel :
Gain direct :
- ATK coeff: -4.09 (-100%)
Changement de mécanique :
- temp//성진우에게 적용
- temp//성진우에게 적용
- temp//성진우에게 적용

Données sources :
- SkillGroupID avant/après: `1001843000100` → `1001843000200`
- ID avant/après: `1001843000101` → `1001843000201`
- BaseSkillInfoKey avant/après: `1001843000101` → `1001843000201`
- Buff IDs avant: `200011000001`
- Buff IDs après: `200011000201,200011000202,200011000203`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Apocalypse I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Consomme des PM supplémentaires pour activer [Frappe en chaîne : Attaque niveau 2].
Augmente la Pénétration de défense d'[Apocalypse] et [Frappe en chaîne].

NOUVEL EFFET
- ArmPenP: 10% (FORTEMENT PROBABLE; valeur interne 1000)

Gain réel :
Gain direct :
- 0 % dégâts directs explicites
Gain conditionnel :
- ArmPenP: 10% (FORTEMENT PROBABLE; valeur interne 1000)

Données sources :
- SkillGroupID avant/après: `1001851000000` → `1001851000100`
- ID avant/après: `1001851000001` → `1001851000101`
- BaseSkillInfoKey avant/après: `1001851000001` → `1001851000101`
- Buff IDs avant: `200030024001,200030024101`
- Buff IDs après: `200030024204,200030024001,200030024101,200030024201`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Apocalypse II → III

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Consomme des PM supplémentaires pour activer [Frappe en chaîne : Attaque niveau 2].
Augmente la Pénétration de défense d'[Apocalypse] et [Frappe en chaîne].

La réactivation de la compétence pendant l'utilisation d'[Apocalypse] fait bondir Jinwoo en arrière et tire une balle spéciale supplémentaire. Ensuite, [Frappe en chaîne] est améliorée, augmentant temporairement la consommation de PM et la distance de recul, mais aussi les dégâts infligés.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001851000100` → `1001851000200`
- ID avant/après: `1001851000101` → `1001851000201`
- BaseSkillInfoKey avant/après: `1001851000101` → `1001851000201`
- Buff IDs avant: `200030024204,200030024001,200030024101,200030024201`
- Buff IDs après: `200030024204,200030024001,200030024003,200030024101,200030024201`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Fleur de prunier : Vol prompt I → II

Dégâts directs        : inchangés
ATK coeff             : 4.96 → 5.04
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

NOUVEL EFFET
- payload référencé 1001608000101: ATK 5.04, DEF 0, HP 0, CD 26 s, MP 216
- Dispel: paramètres internes 0, 200030005010, 0
- payload référencé 1001608000201: ATK 4, DEF 0, HP 0, CD 0 s, MP 0
- SkillChange: remplace/cible skill group 1001608000100 -> 1001608000200

Gain réel :
Gain direct :
- ATK coeff: +0.0799999 (+1.61%)
Utilitaire :
- SkillChange: remplace/cible skill group 1001608000100 -> 1001608000200
Changement de mécanique :
- payload référencé 1001608000101: ATK 5.04, DEF 0, HP 0, CD 26 s, MP 216
- Dispel: paramètres internes 0, 200030005010, 0
- payload référencé 1001608000201: ATK 4, DEF 0, HP 0, CD 0 s, MP 0

Données sources :
- SkillGroupID avant/après: `1001608000000` → `1001608000100`
- ID avant/après: `1001608000001` → `1001608000101`
- BaseSkillInfoKey avant/après: `1001608000001` → `1001608000101`
- Buff IDs avant: `1200191000,200030005001,200030005003,200030005006`
- Buff IDs après: `1200191000,200030005011,200030005001,200030005014,200030005006,200030005012`
- SkillChange/SkillCast payload IDs suivis: `1001608000101,1001608000201`
- SkillChange/SkillCast refs brutes: `1001608000100,1001608000200`

# Anneau mortel I → II

Dégâts directs        : inchangés
ATK coeff             : 1.49 → 1.58
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Rattraper la faux qui revient réinitialise le temps de rechargement de la compétence et octroie 1 cumul de l'effet associé pendant 6 secondes.
Quand Jinwoo relance la compétence au bout de 3 cumuls, il lance la faux devant lui ; elle ne revient pas, mais prolonge les dégâts infligés.
Chaque fois que Jinwoo utilise [Anneau mortel], des [Anneaux en spirale] apparaissent autour de lui.
À chaque utilisation d'[Anneau mortel], des [Anneaux en spirale] volent avec lui pour infliger des dégâts supplémentaires.
Vous pouvez cumuler des [Anneaux en spirale] jusqu'à 3 fois.

Gain réel :
Gain direct :
- ATK coeff: +0.09 (+6.04%)

Données sources :
- SkillGroupID avant/après: `1001711000000` → `1001711000200`
- ID avant/après: `1001711000001` → `1001711000201`
- BaseSkillInfoKey avant/après: `1001711000001` → `1001711000201`
- Buff IDs avant: `200010013001,200010013003,1420000021`
- Buff IDs après: `200010013001,200010013003,1420000021,200010013008`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Frappe de l'Ordre céleste I → II

Dégâts directs        : inchangés
ATK coeff             : inchangés
DEF coeff             : inchangés
HP coeff              : inchangés
Cooldown              : inchangés
MP                    : inchangés
Gain MP               : inchangés

DESCRIPTION MODIFIÉE
Jinwoo peut charger cette compétence jusqu'au niveau 5. À chaque niveau de charge, il active [Concentration d'énergie de mana].
S'il est touché par un ennemi pendant la charge, il se téléporte vers cet ennemi et attaque avec l'effet [Concentration d'énergie de mana] au maximum.
Lorsqu'il utilise cette compétence, il obtient un [Bouclier] pendant un certain temps.

[Concentration d'énergie de mana]
Augmente légèrement les dégâts de [Frappe de l'Ordre céleste] pendant un certain temps.

Gain réel :
Gain direct :
- 0 % dégâts directs explicites

Données sources :
- SkillGroupID avant/après: `1001840000000` → `1001840000300`
- ID avant/après: `1001840000001` → `1001840000301`
- BaseSkillInfoKey avant/après: `1001840000001` → `1001840000301`
- Buff IDs avant: `1200191001,1420000021,200030018002`
- Buff IDs après: `1200191001,1420000021,200030018002`
- SkillChange/SkillCast payload IDs suivis: ``
- SkillChange/SkillCast refs brutes: ``

# Synthèse - 5 patterns les plus fréquents

- aucun changement explicite: 22 transitions
- direct: 19 transitions
- conditionnel: 10 transitions
- mécanique: 6 transitions
- direct+conditionnel: 4 transitions