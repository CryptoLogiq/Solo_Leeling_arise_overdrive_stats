# Résumé de l'arbre

Ce rapport HUMAN présente les arbres de talents de Sung Jinwoo sous une forme lisible sur GitHub: topologie par système, branches, talents logiques, coûts, rangs, gains interprétés et rendements seulement lorsqu'ils sont démontrés.

Validation: nœuds, parents, coûts, rangs, BuffID/SkillID et valeurs raw proviennent des GameData décodés. `ProgressionDepth` est calculé depuis les parents; `VisualRow` conserve la rangée UI `NodeTierY`. Les valeurs affichées en pourcentage restent marquées selon leur niveau de confiance; les valeurs brutes sans unité démontrée conservent un gain/rendement `NON DÉTERMINÉ`.

Reste non déterminé: conversion runtime de certaines valeurs raw, ordre d'application des buffs, additivité exacte entre sources différentes et exclusivité éventuelle de certaines branches/classes/armes.

## Sommaire

Arbres de classe:
- Assassin: Attaque sournoise / Frappe vitale / Nœud de classe / Overdrive
- Duelliste: Coup unique / Frappe enragée / Nœud de classe / Overdrive
- Magicien élémentaire: Feu / Glace / Nœud de classe / Overdrive
- Souverain: Changement gravitationnel / Nœud de classe / Overdrive / Toucher

Arbres d'armes:
- Épée: Cœur d'acier / Résistance à la lame
- Dague: Plaie mortelle / Éviction
- Arc: Visée concentrée / Visée sécurisée
- Arme à feu: Arme à feu - Kata / Visée patiente
- Focalisateur: Recherche de PM / Énergie de mana fluide
- Arme d'hast: Fer-de-lance dévié / Frappe brutale
- Arme à deux mains: Contre-offensive et restauration / Ruée de berserker

Améliorations de Jinwoo:
- Physique: Amélioration corporelle I / Amélioration corporelle II
- Éveil du monarque: Libération d'âme / Vision ombrale

Structures non rattachées:
- Critique et pénétration: Critique et pénétration
- Stats principales: Stats principales

Lecture: le rapport est trié par arbre, puis branche, puis talent logique dans l'ordre technique. `ProgressionDepth` reste une propriété du graphe technique; `NodeTierY` reste une rangée visuelle et ne reconstruit jamais les chemins.

# ARBRES DE CLASSE

## ASSASSIN

### Branche 1 — Attaque sournoise

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Ruée acérée | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Embuscade I | profondeur 2, UI 2, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Embuscade II | profondeur 2, UI 2, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Arts verticaux | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Taux de coup critique augmenté | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 14 pts requis |
| Embuscade III - [Effet passif spécial] | profondeur 3, UI 4, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Taux de coup critique augmenté - [Effet passif spécial] | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 18 pts requis |
| Attaque augmentée | profondeur 6, UI 6, X 2 | Attaque: 0,8 % | 1 | 3 SkillPoint | +0,8 % | +0,8 % | 0,27 %/SkillPoint | 23 pts requis |
| Embuscade IV | profondeur 4, UI 6, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 10 pts requis |
| Marque de l'assassin | profondeur 6, UI 7, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 23 pts requis |

### Branche 2 — Frappe vitale

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Lésion interne | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Dévastation I | profondeur 2, UI 2, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Dévastation II | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| À point | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Attaque dans le dos I | profondeur 3, UI 3, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Position d'embuscade | profondeur 4, UI 4, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Ruée de l'ombre | profondeur 4, UI 5, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 10 pts requis |
| Attaque dans le dos II | profondeur 5, UI 5, X 4 | Dégâts dans le dos: 320 | 1 | 5 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 20 pts requis |
| Entailles croissantes | profondeur 5, UI 6, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Intention du prédateur | profondeur 5, UI 7, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 14 pts requis |

### Nœud de classe / Overdrive

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Overdrive | profondeur 1, UI 1, X 4 | Passif / Overdrive | 1 | 1 IdentityPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | Chapitre principal 10301 |

## DUELLISTE

### Branche 1 — Frappe enragée

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Accablement | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Contre-offensive I | profondeur 2, UI 2, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Ombre vive : Contre-attaque | profondeur 2, UI 2, X 4 | Modification de compétence | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Contre-offensive II | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Percussion | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Déséquilibre augmenté | profondeur 3, UI 3, X 4 | Déséquilibre / Break: 320 | 1 | 4 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Défense augmentée | profondeur 4, UI 4, X 3 | Défense: 6,4 % | 1 | 3 SkillPoint | +6,4 % | +6,4 % | 2,13 %/SkillPoint | 14 pts requis |
| Amélioration de contre-attaque | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 22 pts requis |
| Contre-offensive III | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 25 pts requis |
| Déchaînement | profondeur 6, UI 6, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 32 pts requis |
| Champion de la contre-offensive | profondeur 6, UI 7, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 29 pts requis |

### Branche 2 — Coup unique

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Bris d'armure | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Combo I | profondeur 2, UI 2, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Smash I | profondeur 2, UI 2, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Annihilation | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Déséquilibre augmenté - [Effet passif spécial] | profondeur 4, UI 4, X 3 | Déséquilibre / Break: 160 | 1 | 5 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 14 pts requis |
| Augmentation des PV | profondeur 5, UI 5, X 2 | PV: 6,4 % | 1 | 3 SkillPoint | +6,4 % | +6,4 % | 2,13 %/SkillPoint | 19 pts requis |
| Fougue | profondeur 5, UI 5, X 4 | Effet déclenché | 1 | 3 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |
| Combo II | profondeur 6, UI 6, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 22 pts requis |
| Smash II | profondeur 6, UI 6, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 22 pts requis |
| Force amplifiée | profondeur 7, UI 7, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 38 pts requis |

### Nœud de classe / Overdrive

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Overdrive | profondeur 1, UI 1, X 4 | Dégâts de compétence: 20000; Buff périodique | 1 | 1 IdentityPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | Chapitre principal 10301 |

## MAGICIEN ÉLÉMENTAIRE

### Branche 1 — Glace

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Tempête glacée | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Augmentation des dégâts de chaîne | profondeur 2, UI 2, X 3 | Accumulation élémentaire: 1 | 1 | 4 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis |
| Iceberg | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Amélioration de Magicien élémentaire : Gel I | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Augmentation de la Pénétration de défense | profondeur 4, UI 4, X 4 | Pénétration: 80 | 1 | 3 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis |
| Lame de glace | profondeur 4, UI 5, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Amélioration de Magicien élémentaire : Gel II | profondeur 5, UI 6, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Infusion élémentaire | profondeur 5, UI 6, X 4 | Effet déclenché | 1 | 3 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 17 pts requis |
| Anneau gelé | profondeur 5, UI 7, X 3 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Harmonie de givrefeu | profondeur 6, UI 8, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 20 pts requis |

### Branche 2 — Feu

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dague de tempête de feu | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Coup bonus | profondeur 2, UI 2, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Feu sauvage | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 2 | Pénétration: 80 | 1 | 3 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis |
| Amélioration de Magicien élémentaire : Feu I | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Armure en fusion | profondeur 4, UI 5, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Boost élémentaire | profondeur 5, UI 6, X 2 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 17 pts requis |
| Amélioration de Magicien élémentaire : Feu II | profondeur 5, UI 6, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Annihilation | profondeur 5, UI 7, X 3 | Compétence active | 1 | 3 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Paume embrasée | profondeur 6, UI 8, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 22 pts requis |

### Nœud de classe / Overdrive

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Overdrive | profondeur 1, UI 1, X 4 | Passif / Overdrive | 1 | 1 IdentityPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | Chapitre principal 10301 |

## SOUVERAIN

### Branche 1 — Toucher

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Toucher du maître | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Efficacité de la subsistance | profondeur 2, UI 2, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 2 pts requis |
| Suppression I | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Roue de pleine lune | profondeur 3, UI 3, X 4 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Mépris | profondeur 4, UI 4, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Festin des faibles | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Suppression II | profondeur 6, UI 6, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 25 pts requis |
| Trou noir | profondeur 6, UI 6, X 4 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 17 pts requis |
| Champ de bataille de la domination | profondeur 7, UI 7, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 36 pts requis |
| Main de célérité | profondeur 8, UI 8, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 40 pts requis |

### Branche 2 — Changement gravitationnel

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dispersion | profondeur 1, UI 1, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Dégâts augmentés contre les cibles à terre | profondeur 2, UI 2, X 3 | Dégâts contre réaction: 480 | 1 | 4 SkillPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis |
| Libération | profondeur 3, UI 3, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Désintégration | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Aspiration gravitationnelle | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 5 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Attaque finale | profondeur 5, UI 5, X 3 | Compétence active | 1 | 2 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 13 pts requis |
| Changement gravitationnel | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 15 pts requis |
| Désintégration multipliée | profondeur 7, UI 7, X 2 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 25 pts requis |
| Posture parfaite | profondeur 7, UI 7, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |
| Armée de conquête | profondeur 8, UI 8, X 4 | Effet déclenché | 1 | 4 SkillPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 23 pts requis |

### Nœud de classe / Overdrive

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Overdrive | profondeur 1, UI 1, X 4 | Passif / Overdrive | 1 | 1 IdentityPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | Chapitre principal 10501 |

# ARBRES D'ARMES

## ÉPÉE

### Branche 1 — Cœur d'acier

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Hausse des dégâts de compétence à l'épée | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 2 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Charge frontale | profondeur 2, UI 2, X 3 | Dégâts dans le dos: -750; Dégâts de compétence: 450 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| Protection de l'épée | profondeur 3, UI 3, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Attaque augmentée | profondeur 4, UI 4, X 2 | Attaque: 0,5 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 9 pts requis |
| Défense augmentée | profondeur 4, UI 4, X 4 | Défense: 1 % | 3 | 2 WeaponPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 9 pts requis |
| Cœur d'acier | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 16 pts requis |
| Affrontement frontal | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

### Branche 2 — Résistance à la lame

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Hausse des dégâts de compétence à l'épée | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 2 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Épée gardienne | profondeur 2, UI 2, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Attaquer et bloquer | profondeur 2, UI 2, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Précision augmentée | profondeur 3, UI 3, X 3 | Précision: 0,5 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 12 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 3 | Pénétration: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 14 pts requis |
| Lancement de contre-attaque | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 16 pts requis |
| Frappe maîtrisée | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

## DAGUE

### Branche 1 — Plaie mortelle

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Taux de coup critique augmenté | profondeur 1, UI 1, X 2 | Taux critique: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 0 pts requis |
| Dégâts de coup critique augmentés | profondeur 1, UI 1, X 4 | Dégâts critiques: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 0 pts requis |
| Plaie mortelle | profondeur 2, UI 2, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 4 pts requis |
| Taux de coup critique augmenté | profondeur 3, UI 3, X 2 | Taux critique: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 7 pts requis |
| Dégâts de coup critique augmentés | profondeur 3, UI 3, X 4 | Dégâts critiques: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 7 pts requis |
| Amplification de la douleur | profondeur 4, UI 4, X 2 | Dégâts contre cible affectée: 3 % | 1 | 3 WeaponPoint | +3 % | +3 % | 1 %/WeaponPoint | 9 pts requis |
| Approche violente | profondeur 4, UI 4, X 4 | Dégâts de compétence: 1500 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Frappe préparée | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 20 pts requis |

### Branche 2 — Éviction

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à la dague augmentés | profondeur 1, UI 1, X 2 | Dégâts de compétence d'arme: 1 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Dégâts des attaques dans le dos augmentés | profondeur 1, UI 1, X 4 | Dégâts dans le dos: 150 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Attaque en embuscade | profondeur 2, UI 2, X 3 | Dégâts dans le dos: 750; Dégâts de compétence: -300 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Dégâts de Foulée de l'ombre augmentés | profondeur 3, UI 3, X 3 | Dégâts de compétence: 1500 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Frappe de l'ombre | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Faille de l'ombre | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Coup dans le dos | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 21 pts requis |

## ARC

### Branche 1 — Visée sécurisée

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à l'arc augmentés | profondeur 1, UI 1, X 2 | Dégâts de compétence d'arme: 3 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Précision augmentée | profondeur 2, UI 2, X 3 | Précision: 0,5 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 3 pts requis |
| Tir d'esquive | profondeur 2, UI 3, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Tir en pleine tête | profondeur 3, UI 3, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 3 | Pénétration: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 8 pts requis |
| Visée sécurisée | profondeur 5, UI 5, X 2 | Dégâts infligés: 5,5 %; Dégâts selon distance: -1550 | 1 | 3 WeaponPoint | +5,5 % | +5,5 % | 1,83 %/WeaponPoint | 16 pts requis |
| Distance parfaite | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

### Branche 2 — Visée concentrée

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à l'arc augmentés | profondeur 1, UI 1, X 4 | Dégâts de compétence d'arme: 3 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Taux de coup critique augmenté | profondeur 2, UI 2, X 3 | Taux critique: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 3 pts requis |
| Frappe calculée | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Tir en reculant | profondeur 2, UI 3, X 4 | Dégâts de compétence: 1500 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| Dégâts de coup critique augmentés | profondeur 4, UI 4, X 3 | Dégâts critiques: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 8 pts requis |
| Frappe véloce | profondeur 5, UI 5, X 4 | Conversion stat -> dégâts: 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 16 pts requis |
| Veille funeste | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

## ARME À FEU

### Branche 1 — Visée patiente

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Rechargement | profondeur 1, UI 1, X 1 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Dégâts de compétence à l'arme à feu augmentés | profondeur 1, UI 1, X 2 | Dégâts de compétence d'arme: 4 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Pénétration de défense augmentée | profondeur 2, UI 2, X 3 | Pénétration: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 3 pts requis |
| Munitions concentrées | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 3 | Pénétration: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 8 pts requis |
| Flux balistique | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 10 pts requis |
| Tir relais | profondeur 6, UI 6, X 1 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 13 pts requis |

### Branche 2 — Arme à feu - Kata

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à l'arme à feu augmentés | profondeur 1, UI 1, X 2 | Dégâts de compétence d'arme: 4 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Attaque rapide | profondeur 1, UI 1, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Massacre | profondeur 2, UI 2, X 1 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Tir à bout portant | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Massacre II | profondeur 4, UI 4, X 1 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 9 pts requis |
| Coup d'esquive | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Tir critique | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 15 pts requis |

## FOCALISATEUR

### Branche 1 — Énergie de mana fluide

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence de Concentration augmentés | profondeur 1, UI 1, X 2 | Dégâts de compétence d'arme: 7 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Dégâts de compétence de Concentration augmentés | profondeur 1, UI 1, X 4 | Dégâts de compétence d'arme: 7 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Amélioration de mana | profondeur 2, UI 2, X 3 | Dégâts de compétence d'arme: 7; Réduction coût MP: -2000 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Augmente les PM max | profondeur 3, UI 3, X 3 | PM max: 66 | 3 | 2 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Combo de mana | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 11 pts requis |
| Carnage de mana | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 11 pts requis |
| Afflux d'énergie de mana | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

### Branche 2 — Recherche de PM

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence de Concentration augmentés | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 7 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Détection de faiblesse | profondeur 2, UI 2, X 3 | Dégâts de faiblesse élémentaire: 150 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| Amélioration d'accablement | profondeur 3, UI 3, X 2 | Accumulation élémentaire: 1 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Amélioration de chaos | profondeur 3, UI 3, X 4 | Accumulation élémentaire: 1 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Recherche d'élément | profondeur 4, UI 4, X 2 | Valeur élémentaire: 150 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Onde de mana | profondeur 4, UI 4, X 4 | Conversion stat -> dégâts: 2 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Énergie de mana dissimulée | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 21 pts requis |

## ARME D'HAST

### Branche 1 — Fer-de-lance dévié

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à l'arme d'hast augmentés | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 5 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Smash | profondeur 2, UI 2, X 3 | Déséquilibre / Break: 200 | 3 | 2 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| Parade d'arme | profondeur 3, UI 3, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Attaque pulvérisante | profondeur 4, UI 4, X 3 | Dégâts contre état spécial: 3 % | 1 | 3 WeaponPoint | +3 % | +3 % | 1 %/WeaponPoint | 8 pts requis |
| Fer-de-lance dévié | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 11 pts requis |
| Frappe initiale | profondeur 5, UI 5, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 11 pts requis |
| Brèche exploitée | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 20 pts requis |

### Branche 2 — Frappe brutale

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence à l'arme d'hast augmentés | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 5 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Chair forgée | profondeur 2, UI 2, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Physique endurant | profondeur 3, UI 3, X 2 | Réduction des dégâts subis: 0,5 % | 3 | 3 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 6 pts requis |
| Amélioration des PV | profondeur 3, UI 3, X 4 | PV: 1 % | 3 | 2 WeaponPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 6 pts requis |
| Dégâts déviés | profondeur 4, UI 4, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 14 pts requis |
| Contre-offensive | profondeur 5, UI 5, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 17 pts requis |
| Frappe de riposte | profondeur 6, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 20 pts requis |

## ARME À DEUX MAINS

### Branche 1 — Ruée de berserker

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence d'arme à deux mains augmentés | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 8 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Dégâts de coup critique augmentés | profondeur 2, UI 2, X 3 | Dégâts critiques: 0,25 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,25 % | +0,75 % | NON DÉTERMINÉ | 3 pts requis |
| Berserker | profondeur 3, UI 3, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Porte de la mort | profondeur 3, UI 4, X 4 | Dégâts de compétence d'arme: 8; ShieldModifier | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 5 pts requis |
| Posture offensive | profondeur 4, UI 5, X 2 | Dégâts infligés: 4 %; Réduction des dégâts subis: -2,5 % | 1 | 3 WeaponPoint | +4 % / -2,5 % | +4 % / -2,5 % | NON DÉTERMINÉ | 8 pts requis |
| Frappe sanglante | profondeur 4, UI 5, X 4 | Dégâts de compétence d'arme: 8 | 1 | 3 WeaponPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis |
| Échange équivalent | profondeur 5, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 19 pts requis |

### Branche 2 — Contre-offensive et restauration

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Dégâts de compétence d'arme à deux mains augmentés | profondeur 1, UI 1, X 3 | Dégâts de compétence d'arme: 8 | 3 | 3 WeaponPoint/rang - par rang probable | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Précision augmentée | profondeur 2, UI 2, X 3 | Précision: 0,5 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 3 pts requis |
| Attaque augmentée | profondeur 3, UI 3, X 3 | Attaque: 0,5 % | 3 | 2 WeaponPoint/rang - par rang probable | +0,5 % | +1,5 % | NON DÉTERMINÉ | 5 pts requis |
| Blessure régénérante | profondeur 3, UI 3, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 5 pts requis |
| Récupération de force | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 7 pts requis |
| Frappe de rage | profondeur 4, UI 5, X 4 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 8 pts requis |
| Seconde chance | profondeur 5, UI 6, X 3 | Effet déclenché | 1 | 3 WeaponPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 18 pts requis |

# AMÉLIORATIONS DE JINWOO

## PHYSIQUE

### Branche 1 — Amélioration corporelle I

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Attaque augmentée | profondeur 1, UI 1, X 3 | Attaque: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| Défense augmentée | profondeur 2, UI 2, X 2 | Défense: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 1 pts requis |
| PV augmentés | profondeur 2, UI 2, X 4 | PV: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 1 pts requis |
| Attaque augmentée | profondeur 3, UI 3, X 3 | Attaque: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 4 pts requis |
| Défense augmentée | profondeur 4, UI 4, X 2 | Défense: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 5 pts requis |
| PV augmentés | profondeur 4, UI 4, X 4 | PV: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 5 pts requis |
| Attaque augmentée | profondeur 5, UI 5, X 3 | Attaque: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 8 pts requis |
| Défense augmentée | profondeur 6, UI 6, X 2 | Défense: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 9 pts requis |
| PV augmentés | profondeur 6, UI 6, X 4 | PV: 1 % | 3 | 1 SpecialPoint/rang - par rang probable | +1 % | +3 % | NON DÉTERMINÉ | 9 pts requis |

### Branche 2 — Amélioration corporelle II

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Taux de coup critique augmenté | profondeur 1, UI 1, X 3 | Taux critique: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 0 pts requis |
| Pénétration de défense augmentée | profondeur 2, UI 2, X 2 | Pénétration: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 1 pts requis |
| Pénétration de défense augmentée | profondeur 2, UI 2, X 4 | Pénétration: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 1 pts requis |
| Taux de coup critique augmenté | profondeur 3, UI 3, X 3 | Taux critique: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 4 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 2 | Pénétration: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 5 pts requis |
| Pénétration de défense augmentée | profondeur 4, UI 4, X 4 | Pénétration: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 5 pts requis |
| Dégâts subis réduits | profondeur 5, UI 5, X 2 | Réduction des dégâts subis: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 6 pts requis |
| Dégâts subis réduits | profondeur 5, UI 5, X 4 | Réduction des dégâts subis: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 6 pts requis |
| Taux de coup critique augmenté | profondeur 6, UI 6, X 2 | Taux critique: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 7 pts requis |
| Taux de coup critique augmenté | profondeur 6, UI 6, X 4 | Taux critique: 0,33 % | 3 | 1 SpecialPoint/rang - par rang probable | +0,33 % | +0,99 % | NON DÉTERMINÉ | 7 pts requis |

## ÉVEIL DU MONARQUE

### Branche 1 — Vision ombrale

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| L'Aube du règne I | profondeur 1, UI 1, X 3 | EXRecovery | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| L'Aube du règne II | profondeur 2, UI 2, X 2 | Gain de jauge: 2000 | 1 | 3 SpecialPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| L'Aube du règne III | profondeur 2, UI 2, X 4 | Gain de jauge: 2000 | 1 | 3 SpecialPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis |
| L'Aube du règne IV | profondeur 3, UI 3, X 3 | Gain de jauge: 2000 | 1 | 3 SpecialPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis |
| Lame vampirique | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 15 pts requis |
| Tranchant des ombres I | profondeur 4, UI 4, X 3 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 15 pts requis |
| Tempête d'ombre I | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 15 pts requis |
| Ruée de l'ombre | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 18 pts requis |
| Tranchant des ombres II | profondeur 5, UI 5, X 3 | Modification de compétence | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 18 pts requis |
| Tempête d'ombre II | profondeur 5, UI 5, X 4 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 18 pts requis |

### Branche 2 — Libération d'âme

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Cape du monarque | profondeur 1, UI 1, X 3 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 0 pts requis |
| Acte des ombres I | profondeur 2, UI 2, X 2 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Acte des ombres II | profondeur 2, UI 2, X 4 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 3 pts requis |
| Âme du clair de lune I | profondeur 3, UI 3, X 2 | Modification de compétence | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Enchaînement d'ombre I | profondeur 3, UI 3, X 4 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 6 pts requis |
| Âme du clair de lune II | profondeur 4, UI 4, X 2 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 9 pts requis |
| Enchaînement d'ombre II | profondeur 4, UI 4, X 4 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 9 pts requis |
| Présage de destruction I | profondeur 5, UI 5, X 2 | Effet déclenché | 1 | 3 SpecialPoint | Non chiffré | Non chiffré | NON DÉTERMINÉ | 12 pts requis |
| Présage de destruction II | profondeur 5, UI 5, X 4 | Dégâts de compétence: 1000 | 1 | 3 SpecialPoint | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis |

# STRUCTURES NON RATTACHÉES

## CRITIQUE ET PÉNÉTRATION

### Branche 1 — Critique et pénétration - nom déduit

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Taux de coup critique 1 | profondeur 1, UI 1, X 2 | Taux critique: 1 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| Dégâts de coup critique 1 | profondeur 1, UI 1, X 3 | Dégâts critiques: 1 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| Pénétration de défense 1 | profondeur 1, UI 1, X 4 | Pénétration: 100 | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis |
| Taux de coup critique 2 | profondeur 2, UI 2, X 2 | Taux critique: 2 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +2 % | +6 % | NON DÉTERMINÉ | 2 pts requis |
| Dégâts de coup critique 2 | profondeur 2, UI 2, X 3 | Dégâts critiques: 2 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +2 % | +6 % | NON DÉTERMINÉ | 2 pts requis |
| Pénétration de défense 2 | profondeur 2, UI 2, X 4 | Pénétration: 200 | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis |
| Taux de coup critique 3 | profondeur 3, UI 3, X 2 | Taux critique: 3 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +3 % | +9 % | NON DÉTERMINÉ | 4 pts requis |
| Dégâts de coup critique 3 | profondeur 3, UI 3, X 3 | Dégâts critiques: 3 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +3 % | +9 % | NON DÉTERMINÉ | 4 pts requis |
| Pénétration de défense 3 | profondeur 3, UI 3, X 4 | Pénétration: 300 | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 4 pts requis |
| Taux de coup critique 4 | profondeur 4, UI 4, X 2 | Taux critique: 4 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +4 % | +12 % | NON DÉTERMINÉ | 6 pts requis |
| Dégâts de coup critique 4 | profondeur 4, UI 4, X 3 | Dégâts critiques: 4 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +4 % | +12 % | NON DÉTERMINÉ | 6 pts requis |
| Pénétration de défense 4 | profondeur 4, UI 4, X 4 | Pénétration: 400 | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis |
| Taux de coup critique 5 | profondeur 5, UI 5, X 2 | Taux critique: 5 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +5 % | +15 % | NON DÉTERMINÉ | 9 pts requis |
| Dégâts de coup critique 5 | profondeur 5, UI 5, X 3 | Dégâts critiques: 5 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +5 % | +15 % | NON DÉTERMINÉ | 9 pts requis |
| Pénétration de défense 5 | profondeur 5, UI 5, X 4 | Pénétration: 500 | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis |
| Taux de coup critique 6 | profondeur 6, UI 6, X 2 | Taux critique: 6 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +6 % | +18 % | NON DÉTERMINÉ | 12 pts requis |
| Dégâts de coup critique 6 | profondeur 6, UI 6, X 3 | Dégâts critiques: 6 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +6 % | +18 % | NON DÉTERMINÉ | 12 pts requis |
| Pénétration de défense 6 | profondeur 6, UI 6, X 4 | Pénétration: 600 | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis |

## STATS PRINCIPALES

### Branche 1 — Stats principales - nom déduit

| Talent | Position | Effet | Rangs | Coût | Gain/rang | Bonus max | Rendement | Accès |
|---|---|---|---:|---|---|---|---|---|
| Attaque augmentée 1 | profondeur 1, UI 1, X 2 | Attaque: 1 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| Défense augmentée 1 | profondeur 1, UI 1, X 3 | Défense: 1 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| PV augmentés 1 | profondeur 1, UI 1, X 4 | PV: 1 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +1 % | +3 % | NON DÉTERMINÉ | 0 pts requis |
| Attaque augmentée 2 | profondeur 2, UI 2, X 2 | Attaque: 2 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +2 % | +6 % | NON DÉTERMINÉ | 2 pts requis |
| Défense augmentée 2 | profondeur 2, UI 2, X 3 | Défense: 2 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +2 % | +6 % | NON DÉTERMINÉ | 2 pts requis |
| PV augmentés 2 | profondeur 2, UI 2, X 4 | PV: 2 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +2 % | +6 % | NON DÉTERMINÉ | 2 pts requis |
| Attaque augmentée 3 | profondeur 3, UI 3, X 2 | Attaque: 3 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +3 % | +9 % | NON DÉTERMINÉ | 4 pts requis |
| Défense augmentée 3 | profondeur 3, UI 3, X 3 | Défense: 3 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +3 % | +9 % | NON DÉTERMINÉ | 4 pts requis |
| PV augmentés 3 | profondeur 3, UI 3, X 4 | PV: 3 % | 3 | 2 / 3 / 4 SkillPoint - interprétation NON DÉTERMINÉE | +3 % | +9 % | NON DÉTERMINÉ | 4 pts requis |
| Attaque augmentée 4 | profondeur 4, UI 4, X 2 | Attaque: 4 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +4 % | +12 % | NON DÉTERMINÉ | 6 pts requis |
| Défense augmentée 4 | profondeur 4, UI 4, X 3 | Défense: 4 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +4 % | +12 % | NON DÉTERMINÉ | 6 pts requis |
| PV augmentés 4 | profondeur 4, UI 4, X 4 | PV: 4 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +4 % | +12 % | NON DÉTERMINÉ | 6 pts requis |
| Attaque augmentée 5 | profondeur 5, UI 5, X 2 | Attaque: 5 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +5 % | +15 % | NON DÉTERMINÉ | 9 pts requis |
| Défense augmentée 5 | profondeur 5, UI 5, X 3 | Défense: 5 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +5 % | +15 % | NON DÉTERMINÉ | 9 pts requis |
| PV augmentés 5 | profondeur 5, UI 5, X 4 | PV: 5 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +5 % | +15 % | NON DÉTERMINÉ | 9 pts requis |
| Attaque augmentée 6 | profondeur 6, UI 6, X 2 | Attaque: 6 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +6 % | +18 % | NON DÉTERMINÉ | 12 pts requis |
| Défense augmentée 6 | profondeur 6, UI 6, X 3 | Défense: 6 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +6 % | +18 % | NON DÉTERMINÉ | 12 pts requis |
| PV augmentés 6 | profondeur 6, UI 6, X 4 | PV: 6 % | 3 | 3 / 4 / 5 SkillPoint - interprétation NON DÉTERMINÉE | +6 % | +18 % | NON DÉTERMINÉ | 12 pts requis |

# Annexe - Index par statistique

## Attaque

- Assassin / Attaque sournoise / profondeur technique 6: Attaque augmentée (+0,8 %, 0,27 %/SkillPoint)
- Physique / Amélioration corporelle I / profondeur technique 1: Attaque augmentée (+1 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle I / profondeur technique 3: Attaque augmentée (+1 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle I / profondeur technique 5: Attaque augmentée (+1 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 1: Attaque augmentée 1 (+1 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 2: Attaque augmentée 2 (+2 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 3: Attaque augmentée 3 (+3 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 4: Attaque augmentée 4 (+4 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 5: Attaque augmentée 5 (+5 %, NON DÉTERMINÉ)
- Stats principales / Stats principales / profondeur technique 6: Attaque augmentée 6 (+6 %, NON DÉTERMINÉ)
- Arme à deux mains / Contre-offensive et restauration / profondeur technique 3: Attaque augmentée (+0,5 %, NON DÉTERMINÉ)
- Épée / Cœur d'acier / profondeur technique 4: Attaque augmentée (+0,5 %, NON DÉTERMINÉ)

## Dégâts contre cible affectée

- Dague / Plaie mortelle / profondeur technique 4: Amplification de la douleur (+3 %, 1 %/WeaponPoint)

## Dégâts contre réaction

- Souverain / Changement gravitationnel / profondeur technique 2: Dégâts augmentés contre les cibles à terre (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Dégâts contre état spécial

- Arme d'hast / Fer-de-lance dévié / profondeur technique 4: Attaque pulvérisante (+3 %, 1 %/WeaponPoint)

## Dégâts critiques

- Critique et pénétration / Critique et pénétration / profondeur technique 1: Dégâts de coup critique 1 (+1 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 2: Dégâts de coup critique 2 (+2 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 3: Dégâts de coup critique 3 (+3 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 4: Dégâts de coup critique 4 (+4 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 5: Dégâts de coup critique 5 (+5 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 6: Dégâts de coup critique 6 (+6 %, NON DÉTERMINÉ)
- Arc / Visée concentrée / profondeur technique 4: Dégâts de coup critique augmentés (+0,25 %, NON DÉTERMINÉ)
- Arme à deux mains / Ruée de berserker / profondeur technique 2: Dégâts de coup critique augmentés (+0,25 %, NON DÉTERMINÉ)
- Dague / Plaie mortelle / profondeur technique 1: Dégâts de coup critique augmentés (+0,25 %, NON DÉTERMINÉ)
- Dague / Plaie mortelle / profondeur technique 3: Dégâts de coup critique augmentés (+0,25 %, NON DÉTERMINÉ)

## Dégâts dans le dos

- Assassin / Frappe vitale / profondeur technique 5: Attaque dans le dos II (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Éviction / profondeur technique 1: Dégâts des attaques dans le dos augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Éviction / profondeur technique 2: Attaque en embuscade (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Épée / Cœur d'acier / profondeur technique 2: Charge frontale (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Dégâts de compétence

- Duelliste / Nœud de classe / Overdrive / profondeur technique 1: Overdrive (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Éveil du monarque / Libération d'âme / profondeur technique 5: Présage de destruction II (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arc / Visée concentrée / profondeur technique 2: Tir en reculant (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Plaie mortelle / profondeur technique 4: Approche violente (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Éviction / profondeur technique 2: Attaque en embuscade (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Éviction / profondeur technique 3: Dégâts de Foulée de l'ombre augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Épée / Cœur d'acier / profondeur technique 2: Charge frontale (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Dégâts de compétence d'arme

- Arc / Visée concentrée / profondeur technique 1: Dégâts de compétence à l'arc augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arc / Visée sécurisée / profondeur technique 1: Dégâts de compétence à l'arc augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme d'hast / Fer-de-lance dévié / profondeur technique 1: Dégâts de compétence à l'arme d'hast augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme d'hast / Frappe brutale / profondeur technique 1: Dégâts de compétence à l'arme d'hast augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à deux mains / Contre-offensive et restauration / profondeur technique 1: Dégâts de compétence d'arme à deux mains augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à deux mains / Ruée de berserker / profondeur technique 1: Dégâts de compétence d'arme à deux mains augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à deux mains / Ruée de berserker / profondeur technique 3: Porte de la mort (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à deux mains / Ruée de berserker / profondeur technique 4: Frappe sanglante (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à feu / Arme à feu - Kata / profondeur technique 1: Dégâts de compétence à l'arme à feu augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme à feu / Visée patiente / profondeur technique 1: Dégâts de compétence à l'arme à feu augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Dague / Éviction / profondeur technique 1: Dégâts de compétence à la dague augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Focalisateur / Recherche de PM / profondeur technique 1: Dégâts de compétence de Concentration augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Focalisateur / Énergie de mana fluide / profondeur technique 1: Dégâts de compétence de Concentration augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Focalisateur / Énergie de mana fluide / profondeur technique 1: Dégâts de compétence de Concentration augmentés (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Focalisateur / Énergie de mana fluide / profondeur technique 2: Amélioration de mana (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Épée / Cœur d'acier / profondeur technique 1: Hausse des dégâts de compétence à l'épée (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Épée / Résistance à la lame / profondeur technique 1: Hausse des dégâts de compétence à l'épée (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Dégâts de faiblesse élémentaire

- Focalisateur / Recherche de PM / profondeur technique 2: Détection de faiblesse (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Dégâts infligés

- Arc / Visée sécurisée / profondeur technique 5: Visée sécurisée (+5,5 %, 1,83 %/WeaponPoint)
- Arme à deux mains / Ruée de berserker / profondeur technique 4: Posture offensive (+4 % / -2,5 %, NON DÉTERMINÉ)

## Déséquilibre / Break

- Duelliste / Coup unique / profondeur technique 4: Déséquilibre augmenté - [Effet passif spécial] (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Duelliste / Frappe enragée / profondeur technique 3: Déséquilibre augmenté (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arme d'hast / Fer-de-lance dévié / profondeur technique 2: Smash (NON DÉTERMINÉ, NON DÉTERMINÉ)

## Précision

- Arc / Visée sécurisée / profondeur technique 2: Précision augmentée (+0,5 %, NON DÉTERMINÉ)
- Arme à deux mains / Contre-offensive et restauration / profondeur technique 2: Précision augmentée (+0,5 %, NON DÉTERMINÉ)
- Épée / Résistance à la lame / profondeur technique 3: Précision augmentée (+0,5 %, NON DÉTERMINÉ)

## Pénétration

- Magicien élémentaire / Feu / profondeur technique 4: Pénétration de défense augmentée (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Magicien élémentaire / Glace / profondeur technique 4: Augmentation de la Pénétration de défense (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 2: Pénétration de défense augmentée (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 2: Pénétration de défense augmentée (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 4: Pénétration de défense augmentée (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 4: Pénétration de défense augmentée (+0,33 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 1: Pénétration de défense 1 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 2: Pénétration de défense 2 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 3: Pénétration de défense 3 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 4: Pénétration de défense 4 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 5: Pénétration de défense 5 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 6: Pénétration de défense 6 (NON DÉTERMINÉ, NON DÉTERMINÉ)
- Arc / Visée sécurisée / profondeur technique 4: Pénétration de défense augmentée (+0,25 %, NON DÉTERMINÉ)
- Arme à feu / Visée patiente / profondeur technique 2: Pénétration de défense augmentée (+0,25 %, NON DÉTERMINÉ)
- Arme à feu / Visée patiente / profondeur technique 4: Pénétration de défense augmentée (+0,25 %, NON DÉTERMINÉ)
- Épée / Résistance à la lame / profondeur technique 4: Pénétration de défense augmentée (+0,25 %, NON DÉTERMINÉ)

## Taux critique

- Physique / Amélioration corporelle II / profondeur technique 1: Taux de coup critique augmenté (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 3: Taux de coup critique augmenté (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 6: Taux de coup critique augmenté (+0,33 %, NON DÉTERMINÉ)
- Physique / Amélioration corporelle II / profondeur technique 6: Taux de coup critique augmenté (+0,33 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 1: Taux de coup critique 1 (+1 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 2: Taux de coup critique 2 (+2 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 3: Taux de coup critique 3 (+3 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 4: Taux de coup critique 4 (+4 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 5: Taux de coup critique 5 (+5 %, NON DÉTERMINÉ)
- Critique et pénétration / Critique et pénétration / profondeur technique 6: Taux de coup critique 6 (+6 %, NON DÉTERMINÉ)
- Arc / Visée concentrée / profondeur technique 2: Taux de coup critique augmenté (+0,25 %, NON DÉTERMINÉ)
- Dague / Plaie mortelle / profondeur technique 1: Taux de coup critique augmenté (+0,25 %, NON DÉTERMINÉ)
- Dague / Plaie mortelle / profondeur technique 3: Taux de coup critique augmenté (+0,25 %, NON DÉTERMINÉ)

# Annexe - Traçabilité technique

- Talents représentés dans la vue principale: 258.
- Détails techniques complets: `SJW_TALENT_TREE_TECHNICAL.md`.
- Données sources normalisées: `analysis/csv/sjw_talent_tree.csv` et `analysis/csv/sjw_talent_tree_detailed.csv`.

