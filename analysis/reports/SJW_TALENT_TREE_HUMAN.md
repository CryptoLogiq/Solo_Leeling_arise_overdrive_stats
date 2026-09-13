# Résumé de l'arbre

Ce rapport HUMAN présente les arbres de talents de Sung Jinwoo sous une forme lisible sur GitHub: topologie par système, branches, talents logiques, coûts, rangs, gains interprétés et rendements seulement lorsqu'ils sont démontrés.

Validation: nœuds, parents, coûts, rangs, BuffID/SkillID et valeurs raw proviennent du modèle canonique. `ProgressionDepth` est calculé depuis les parents; `VisualRow` conserve la rangée UI source. Les valeurs affichées en pourcentage restent marquées selon leur niveau de confiance; les valeurs brutes sans unité démontrée conservent un gain/rendement `NON DÉTERMINÉ`.

Reste non déterminé: conversion runtime de certaines valeurs raw, ordre d'application des buffs, additivité exacte entre sources différentes, sémantique exacte des convergences multi-parent et exclusivité éventuelle de certaines branches/classes/armes.

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

Lecture: le rapport est trié par arbre, puis branche, puis talent logique dans l'ordre technique. `ProgressionDepth` reste une propriété du graphe technique; `VisualRow` reste une rangée visuelle et ne reconstruit jamais les chemins.

# ARBRES DE CLASSE

## ASSASSIN

### Branche 1 — Attaque sournoise

#### Ruée acérée

**Prérequis :** RACINE
**Débloque :** Embuscade I, Embuscade II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Embuscade I

**Prérequis :** Ruée acérée
**Débloque :** Arts verticaux

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Embuscade II

**Prérequis :** Ruée acérée
**Débloque :** Arts verticaux, Embuscade III - [Effet passif spécial]

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Arts verticaux

**Prérequis :** Embuscade I, Embuscade II (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Taux de coup critique augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique augmenté

**Prérequis :** Arts verticaux
**Débloque :** Taux de coup critique augmenté - [Effet passif spécial]

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Embuscade III - [Effet passif spécial]

**Prérequis :** Embuscade II
**Débloque :** Embuscade IV

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique augmenté - [Effet passif spécial]

**Prérequis :** Taux de coup critique augmenté
**Débloque :** Attaque augmentée, Marque de l'assassin

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque augmentée

**Prérequis :** Taux de coup critique augmenté - [Effet passif spécial]
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Attaque: 0,8 % | +0,8 % | 0,8 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE |

#### Embuscade IV

**Prérequis :** Embuscade III - [Effet passif spécial]
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 10 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Marque de l'assassin

**Prérequis :** Taux de coup critique augmenté - [Effet passif spécial]
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Frappe vitale

#### Lésion interne

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Dévastation I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Dévastation I

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Lésion interne
**Débloque :** Dévastation II, À point, Attaque dans le dos I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Dévastation II

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Dévastation I
**Débloque :** Ruée de l'ombre

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### À point

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Dévastation I
**Débloque :** Position d'embuscade

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque dans le dos I

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Dévastation I
**Débloque :** Attaque dans le dos II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Position d'embuscade

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** À point
**Débloque :** Attaque dans le dos II, Entailles croissantes

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Ruée de l'ombre

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 2
**Prérequis :** Dévastation II
**Débloque :** Intention du prédateur

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 10 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque dans le dos II

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Attaque dans le dos I, Position d'embuscade (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Dégâts dans le dos: 320 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Entailles croissantes

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 3
**Prérequis :** Position d'embuscade
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Intention du prédateur

**Position dans l'arbre :** profondeur technique 5, rangée UI 7, X 2
**Prérequis :** Ruée de l'ombre
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 14 pts requis | CONFIRMÉ PAR LES GAMEDATA |

### Nœud de classe / Overdrive

#### Overdrive

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 IdentityPoint | Passif / Overdrive | Non chiffré | Non chiffré | Chapitre principal 10301 | NON DÉTERMINÉ |

## DUELLISTE

### Branche 1 — Frappe enragée

#### Accablement

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Contre-offensive I, Ombre vive : Contre-attaque

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Contre-offensive I

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Accablement
**Débloque :** Contre-offensive II, Percussion

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Ombre vive : Contre-attaque

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Accablement
**Débloque :** Percussion, Déséquilibre augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Modification de compétence | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Contre-offensive II

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Contre-offensive I
**Débloque :** Contre-offensive III

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Percussion

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Contre-offensive I, Ombre vive : Contre-attaque (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Défense augmentée, Amélioration de contre-attaque

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Déséquilibre augmenté

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Ombre vive : Contre-attaque
**Débloque :** Amélioration de contre-attaque

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Déséquilibre / Break: 320 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Percussion
**Débloque :** Contre-offensive III, Déchaînement

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Défense: 6,4 % | +6,4 % | 6,4 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE |

#### Amélioration de contre-attaque

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Percussion, Déséquilibre augmenté (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Contre-offensive III

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Contre-offensive II, Défense augmentée (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Déchaînement, Champion de la contre-offensive

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Déchaînement

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Défense augmentée, Contre-offensive III (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Champion de la contre-offensive

**Position dans l'arbre :** profondeur technique 6, rangée UI 7, X 2
**Prérequis :** Contre-offensive III
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Coup unique

#### Bris d'armure

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Combo I, Smash I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Combo I

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Bris d'armure
**Débloque :** Annihilation

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Smash I

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Bris d'armure
**Débloque :** Annihilation

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Annihilation

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Combo I, Smash I (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Déséquilibre augmenté - [Effet passif spécial]

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Déséquilibre augmenté - [Effet passif spécial]

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Annihilation
**Débloque :** Augmentation des PV, Fougue

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Déséquilibre / Break: 160 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Augmentation des PV

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Déséquilibre augmenté - [Effet passif spécial]
**Débloque :** Combo II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | PV: 6,4 % | +6,4 % | 6,4 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE |

#### Fougue

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Déséquilibre augmenté - [Effet passif spécial]
**Débloque :** Smash II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Combo II

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Augmentation des PV
**Débloque :** Force amplifiée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Smash II

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** Fougue
**Débloque :** Force amplifiée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Force amplifiée

**Position dans l'arbre :** profondeur technique 7, rangée UI 7, X 3
**Prérequis :** Combo II, Smash II (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Nœud de classe / Overdrive

#### Overdrive

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 IdentityPoint | Dégâts de compétence: 20000; Buff périodique | NON DÉTERMINÉ | NON DÉTERMINÉ | Chapitre principal 10301 | CONFIRMÉ PAR LES GAMEDATA |

## MAGICIEN ÉLÉMENTAIRE

### Branche 1 — Glace

#### Tempête glacée

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Augmentation des dégâts de chaîne

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Augmentation des dégâts de chaîne

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Tempête glacée
**Débloque :** Iceberg

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Iceberg

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Augmentation des dégâts de chaîne
**Débloque :** Amélioration de Magicien élémentaire : Gel I, Augmentation de la Pénétration de défense, Lame de glace

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Amélioration de Magicien élémentaire : Gel I

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Iceberg
**Débloque :** Amélioration de Magicien élémentaire : Gel II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Augmentation de la Pénétration de défense

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Iceberg
**Débloque :** Infusion élémentaire

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Pénétration: 80 | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Lame de glace

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 3
**Prérequis :** Iceberg
**Débloque :** Infusion élémentaire, Anneau gelé

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Amélioration de Magicien élémentaire : Gel II

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 2
**Prérequis :** Amélioration de Magicien élémentaire : Gel I
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Infusion élémentaire

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 4
**Prérequis :** Augmentation de la Pénétration de défense, Lame de glace (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Harmonie de givrefeu

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Anneau gelé

**Position dans l'arbre :** profondeur technique 5, rangée UI 7, X 3
**Prérequis :** Lame de glace
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Harmonie de givrefeu

**Position dans l'arbre :** profondeur technique 6, rangée UI 8, X 4
**Prérequis :** Infusion élémentaire
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Feu

#### Dague de tempête de feu

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Coup bonus

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Coup bonus

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dague de tempête de feu
**Débloque :** Feu sauvage

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Feu sauvage

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Coup bonus
**Débloque :** Pénétration de défense augmentée, Amélioration de Magicien élémentaire : Feu I, Armure en fusion

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Feu sauvage
**Débloque :** Boost élémentaire

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Pénétration: 80 | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Amélioration de Magicien élémentaire : Feu I

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Feu sauvage
**Débloque :** Amélioration de Magicien élémentaire : Feu II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Armure en fusion

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 3
**Prérequis :** Feu sauvage
**Débloque :** Boost élémentaire, Annihilation

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Boost élémentaire

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 2
**Prérequis :** Pénétration de défense augmentée, Armure en fusion (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Paume embrasée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Amélioration de Magicien élémentaire : Feu II

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 4
**Prérequis :** Amélioration de Magicien élémentaire : Feu I
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Annihilation

**Position dans l'arbre :** profondeur technique 5, rangée UI 7, X 3
**Prérequis :** Armure en fusion
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Compétence active | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Paume embrasée

**Position dans l'arbre :** profondeur technique 6, rangée UI 8, X 2
**Prérequis :** Boost élémentaire
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Nœud de classe / Overdrive

#### Overdrive

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 IdentityPoint | Passif / Overdrive | Non chiffré | Non chiffré | Chapitre principal 10301 | NON DÉTERMINÉ |

## SOUVERAIN

### Branche 1 — Toucher

#### Toucher du maître

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Efficacité de la subsistance

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Efficacité de la subsistance

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Toucher du maître
**Débloque :** Suppression I, Roue de pleine lune

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Suppression I

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Efficacité de la subsistance
**Débloque :** Suppression II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Roue de pleine lune

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Efficacité de la subsistance
**Débloque :** Mépris

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Mépris

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Roue de pleine lune
**Débloque :** Festin des faibles

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Festin des faibles

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Mépris
**Débloque :** Suppression II, Trou noir

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Suppression II

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Suppression I, Festin des faibles (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Champ de bataille de la domination

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Trou noir

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** Festin des faibles
**Débloque :** Champ de bataille de la domination

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 17 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Champ de bataille de la domination

**Position dans l'arbre :** profondeur technique 7, rangée UI 7, X 3
**Prérequis :** Suppression II, Trou noir (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Main de célérité

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Main de célérité

**Position dans l'arbre :** profondeur technique 8, rangée UI 8, X 3
**Prérequis :** Champ de bataille de la domination
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Changement gravitationnel

#### Dispersion

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Dégâts augmentés contre les cibles à terre

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Dégâts augmentés contre les cibles à terre

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dispersion
**Débloque :** Libération

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Dégâts contre réaction: 480 | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Libération

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Dégâts augmentés contre les cibles à terre
**Débloque :** Désintégration, Aspiration gravitationnelle

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Désintégration

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Libération
**Débloque :** Désintégration multipliée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Aspiration gravitationnelle

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Libération
**Débloque :** Attaque finale

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 5 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque finale

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Aspiration gravitationnelle
**Débloque :** Changement gravitationnel

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Compétence active | Non chiffré | Non chiffré | 13 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Changement gravitationnel

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Attaque finale
**Débloque :** Désintégration multipliée, Posture parfaite

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 15 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Désintégration multipliée

**Position dans l'arbre :** profondeur technique 7, rangée UI 7, X 2
**Prérequis :** Désintégration, Changement gravitationnel (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Posture parfaite

**Position dans l'arbre :** profondeur technique 7, rangée UI 7, X 4
**Prérequis :** Changement gravitationnel
**Débloque :** Armée de conquête

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 19 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Armée de conquête

**Position dans l'arbre :** profondeur technique 8, rangée UI 8, X 4
**Prérequis :** Posture parfaite
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 4 SkillPoint | Effet déclenché | Non chiffré | Non chiffré | 23 pts requis | CONFIRMÉ PAR LES GAMEDATA |

### Nœud de classe / Overdrive

#### Overdrive

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 IdentityPoint | Passif / Overdrive | Non chiffré | Non chiffré | Chapitre principal 10501 | NON DÉTERMINÉ |

# ARBRES D'ARMES

## ÉPÉE

### Branche 1 — Cœur d'acier

#### Hausse des dégâts de compétence à l'épée

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Charge frontale

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Charge frontale

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Hausse des dégâts de compétence à l'épée
**Débloque :** Protection de l'épée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts dans le dos: -750; Dégâts de compétence: 450 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Protection de l'épée

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Charge frontale
**Débloque :** Attaque augmentée, Défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Protection de l'épée
**Débloque :** Cœur d'acier

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Attaque: 0,5 % | +0,5 % | 0,5 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Attaque: 0,5 % | +0,5 % | 1 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Attaque: 0,5 % | +0,5 % | 1,5 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Protection de l'épée
**Débloque :** Cœur d'acier

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Défense: 1 % | +1 % | 1 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Défense: 1 % | +1 % | 2 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Défense: 1 % | +1 % | 3 % | 9 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Cœur d'acier

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Attaque augmentée, Défense augmentée (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Affrontement frontal

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Affrontement frontal

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Cœur d'acier
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Résistance à la lame

#### Hausse des dégâts de compétence à l'épée

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Épée gardienne, Attaquer et bloquer

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Épée gardienne

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Hausse des dégâts de compétence à l'épée
**Débloque :** Précision augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaquer et bloquer

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Hausse des dégâts de compétence à l'épée
**Débloque :** Précision augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Précision augmentée

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Épée gardienne, Attaquer et bloquer (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Précision: 0,5 % | +0,5 % | 0,5 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1,5 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Précision augmentée
**Débloque :** Lancement de contre-attaque

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,25 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,5 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,75 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Lancement de contre-attaque

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Frappe maîtrisée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe maîtrisée

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Lancement de contre-attaque
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

## DAGUE

### Branche 1 — Plaie mortelle

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Plaie mortelle

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,25 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,5 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,75 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Dégâts de coup critique augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** Plaie mortelle

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,25 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,5 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,75 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Plaie mortelle

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Taux de coup critique augmenté, Dégâts de coup critique augmentés (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Taux de coup critique augmenté, Dégâts de coup critique augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Plaie mortelle
**Débloque :** Amplification de la douleur

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,25 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,5 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,75 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Dégâts de coup critique augmentés

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Plaie mortelle
**Débloque :** Approche violente

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,25 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,5 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,75 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Amplification de la douleur

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Frappe préparée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts contre cible affectée: 3 % | +3 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE |

#### Approche violente

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Dégâts de coup critique augmentés
**Débloque :** Frappe préparée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence: 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe préparée

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Amplification de la douleur, Approche violente (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Éviction

#### Dégâts de compétence à la dague augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Attaque en embuscade

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Dégâts des attaques dans le dos augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** Attaque en embuscade

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts dans le dos: 150 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts dans le dos: 150 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts dans le dos: 150 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Attaque en embuscade

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à la dague augmentés, Dégâts des attaques dans le dos augmentés (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Dégâts de Foulée de l'ombre augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts dans le dos: 750; Dégâts de compétence: -300 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Dégâts de Foulée de l'ombre augmentés

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Attaque en embuscade
**Débloque :** Frappe de l'ombre, Faille de l'ombre

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence: 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe de l'ombre

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Dégâts de Foulée de l'ombre augmentés
**Débloque :** Coup dans le dos

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Faille de l'ombre

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Dégâts de Foulée de l'ombre augmentés
**Débloque :** Coup dans le dos

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Coup dans le dos

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Frappe de l'ombre, Faille de l'ombre (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

## ARC

### Branche 1 — Visée sécurisée

#### Dégâts de compétence à l'arc augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Précision augmentée, Tir d'esquive

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Précision augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à l'arc augmentés
**Débloque :** Tir en pleine tête

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Précision: 0,5 % | +0,5 % | 0,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Tir d'esquive

**Position dans l'arbre :** profondeur technique 2, rangée UI 3, X 2
**Prérequis :** Dégâts de compétence à l'arc augmentés
**Débloque :** Visée sécurisée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Tir en pleine tête

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Précision augmentée
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Tir en pleine tête
**Débloque :** Visée sécurisée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,25 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,5 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,75 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Visée sécurisée

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Tir d'esquive, Pénétration de défense augmentée (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Distance parfaite

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts infligés: 5,5 %; Dégâts selon distance: -1550 | +5,5 % | 5,5 % | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA; FORTEMENT PROBABLE |

#### Distance parfaite

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Visée sécurisée
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Visée concentrée

#### Dégâts de compétence à l'arc augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** Taux de coup critique augmenté, Tir en reculant

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 3 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à l'arc augmentés
**Débloque :** Frappe calculée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,25 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Taux critique: 0,25 % | +0,25 % | 0,75 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Frappe calculée

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Dégâts de coup critique augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Tir en reculant

**Position dans l'arbre :** profondeur technique 2, rangée UI 3, X 4
**Prérequis :** Dégâts de compétence à l'arc augmentés
**Débloque :** Frappe véloce

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence: 1500 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Dégâts de coup critique augmentés

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Frappe calculée
**Débloque :** Frappe véloce

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,25 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,5 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,75 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Frappe véloce

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Tir en reculant, Dégâts de coup critique augmentés (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Veille funeste

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Conversion stat -> dégâts: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Veille funeste

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Frappe véloce
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

## ARME À FEU

### Branche 1 — Visée patiente

#### Rechargement

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 1
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Dégâts de compétence à l'arme à feu augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à l'arme à feu augmentés
**Débloque :** Munitions concentrées

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,25 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,75 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Munitions concentrées

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Munitions concentrées
**Débloque :** Flux balistique

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,25 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,5 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Pénétration: 0,25 % | +0,25 % | 0,75 % | 8 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Flux balistique

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Tir relais

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 10 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Tir relais

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 1
**Prérequis :** Flux balistique
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 13 pts requis | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Arme à feu - Kata

#### Dégâts de compétence à l'arme à feu augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Massacre

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 4 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Attaque rapide

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Massacre

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 1
**Prérequis :** Dégâts de compétence à l'arme à feu augmentés
**Débloque :** Tir à bout portant

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Tir à bout portant

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Massacre
**Débloque :** Massacre II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Massacre II

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 1
**Prérequis :** Tir à bout portant
**Débloque :** Coup d'esquive

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Coup d'esquive

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Massacre II
**Débloque :** Tir critique

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Tir critique

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Coup d'esquive
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 15 pts requis | CONFIRMÉ PAR LES GAMEDATA |

## FOCALISATEUR

### Branche 1 — Énergie de mana fluide

#### Dégâts de compétence de Concentration augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Amélioration de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Dégâts de compétence de Concentration augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** Amélioration de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Amélioration de mana

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence de Concentration augmentés
**Débloque :** Augmente les PM max

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence d'arme: 7; Réduction coût MP: -2000 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Augmente les PM max

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Amélioration de mana
**Débloque :** Combo de mana, Carnage de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | PM max: 66 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | PM max: 66 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | PM max: 66 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Combo de mana

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Augmente les PM max
**Débloque :** Afflux d'énergie de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Carnage de mana

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Augmente les PM max
**Débloque :** Afflux d'énergie de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Afflux d'énergie de mana

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Combo de mana, Carnage de mana (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Recherche de PM

#### Dégâts de compétence de Concentration augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Détection de faiblesse

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 7 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Détection de faiblesse

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence de Concentration augmentés
**Débloque :** Amélioration d'accablement, Amélioration de chaos

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de faiblesse élémentaire: 150 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Amélioration d'accablement

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Détection de faiblesse
**Débloque :** Recherche d'élément

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Amélioration de chaos

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Détection de faiblesse
**Débloque :** Onde de mana

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Accumulation élémentaire: 1 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Recherche d'élément

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Amélioration d'accablement
**Débloque :** Énergie de mana dissimulée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Valeur élémentaire: 150 | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Onde de mana

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Amélioration de chaos
**Débloque :** Énergie de mana dissimulée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Conversion stat -> dégâts: 2 | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Énergie de mana dissimulée

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Recherche d'élément, Onde de mana (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

## ARME D'HAST

### Branche 1 — Fer-de-lance dévié

#### Dégâts de compétence à l'arme d'hast augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Smash

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Smash

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à l'arme d'hast augmentés
**Débloque :** Parade d'arme

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Déséquilibre / Break: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Déséquilibre / Break: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Déséquilibre / Break: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Parade d'arme

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Smash
**Débloque :** Attaque pulvérisante

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Attaque pulvérisante

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Parade d'arme
**Débloque :** Fer-de-lance dévié, Frappe initiale

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts contre état spécial: 3 % | +3 % | 3 % | 8 pts requis | FORTEMENT PROBABLE |

#### Fer-de-lance dévié

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Attaque pulvérisante
**Débloque :** Brèche exploitée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 11 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe initiale

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Attaque pulvérisante
**Débloque :** Brèche exploitée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 11 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Brèche exploitée

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Fer-de-lance dévié, Frappe initiale (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Frappe brutale

#### Dégâts de compétence à l'arme d'hast augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Chair forgée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 5 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Chair forgée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence à l'arme d'hast augmentés
**Débloque :** Physique endurant, Amélioration des PV

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Physique endurant

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Chair forgée
**Débloque :** Dégâts déviés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Réduction des dégâts subis: 0,5 % | +0,5 % | 0,5 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Réduction des dégâts subis: 0,5 % | +0,5 % | 1 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Réduction des dégâts subis: 0,5 % | +0,5 % | 1,5 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Amélioration des PV

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Chair forgée
**Débloque :** Dégâts déviés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | PV: 1 % | +1 % | 1 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | PV: 1 % | +1 % | 2 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | PV: 1 % | +1 % | 3 % | 6 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Dégâts déviés

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Physique endurant, Amélioration des PV (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Contre-offensive

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Contre-offensive

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Dégâts déviés
**Débloque :** Frappe de riposte

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe de riposte

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Contre-offensive
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

## ARME À DEUX MAINS

### Branche 1 — Ruée de berserker

#### Dégâts de compétence d'arme à deux mains augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Dégâts de coup critique augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Dégâts de coup critique augmentés

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence d'arme à deux mains augmentés
**Débloque :** Berserker, Porte de la mort

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,25 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Dégâts critiques: 0,25 % | +0,25 % | 0,75 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Berserker

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Dégâts de coup critique augmentés
**Débloque :** Posture offensive

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Porte de la mort

**Position dans l'arbre :** profondeur technique 3, rangée UI 4, X 4
**Prérequis :** Dégâts de coup critique augmentés
**Débloque :** Frappe sanglante

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence d'arme: 8; ShieldModifier | NON DÉTERMINÉ | NON DÉTERMINÉ | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Posture offensive

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 2
**Prérequis :** Berserker
**Débloque :** Échange équivalent

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts infligés: 4 %; Réduction des dégâts subis: -2,5 % | +4 % / -2,5 % | -2,5 % / 4 % | 8 pts requis | FORTEMENT PROBABLE |

#### Frappe sanglante

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 4
**Prérequis :** Porte de la mort
**Débloque :** Échange équivalent

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Échange équivalent

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 3
**Prérequis :** Posture offensive, Frappe sanglante (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Contre-offensive et restauration

#### Dégâts de compétence d'arme à deux mains augmentés

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Précision augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| II | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |
| III | 3 WeaponPoint/rang - par rang probable | Dégâts de compétence d'arme: 8 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA; coût FORTEMENT PROBABLE |

#### Précision augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de compétence d'arme à deux mains augmentés
**Débloque :** Attaque augmentée, Blessure régénérante

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Précision: 0,5 % | +0,5 % | 0,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Précision: 0,5 % | +0,5 % | 1,5 % | 3 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Attaque augmentée

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Précision augmentée
**Débloque :** Récupération de force

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 WeaponPoint - par rang probable | Attaque: 0,5 % | +0,5 % | 0,5 % | 5 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 2 WeaponPoint/rang - par rang probable | Attaque: 0,5 % | +0,5 % | 1 % | 5 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 2 WeaponPoint/rang - par rang probable | Attaque: 0,5 % | +0,5 % | 1,5 % | 5 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Blessure régénérante

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Précision augmentée
**Débloque :** Frappe de rage

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 5 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Récupération de force

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Attaque augmentée
**Débloque :** Seconde chance

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 7 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Frappe de rage

**Position dans l'arbre :** profondeur technique 4, rangée UI 5, X 4
**Prérequis :** Blessure régénérante
**Débloque :** Seconde chance

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | 8 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Seconde chance

**Position dans l'arbre :** profondeur technique 5, rangée UI 6, X 3
**Prérequis :** Récupération de force, Frappe de rage (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 WeaponPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

# AMÉLIORATIONS DE JINWOO

## PHYSIQUE

### Branche 1 — Amélioration corporelle I

#### Attaque augmentée

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Défense augmentée, PV augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Attaque: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Défense augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Attaque augmentée
**Débloque :** Attaque augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Défense: 1 % | +1 % | 1 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 2 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 3 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### PV augmentés

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Attaque augmentée
**Débloque :** Attaque augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | PV: 1 % | +1 % | 1 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 2 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 3 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Attaque augmentée

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Défense augmentée, PV augmentés (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Défense augmentée, PV augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Attaque: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Attaque augmentée
**Débloque :** Attaque augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Défense: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### PV augmentés

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Attaque augmentée
**Débloque :** Attaque augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | PV: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Attaque augmentée

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Défense augmentée, PV augmentés (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Défense augmentée, PV augmentés

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Attaque: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Attaque: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Défense augmentée

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Attaque augmentée
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Défense: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Défense: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### PV augmentés

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** Attaque augmentée
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | PV: 1 % | +1 % | 1 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 2 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | PV: 1 % | +1 % | 3 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

### Branche 2 — Amélioration corporelle II

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,33 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,66 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,99 % | 0 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Taux de coup critique augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,33 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,66 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,99 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Taux de coup critique augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,33 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,66 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,99 % | 1 pts requis | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Pénétration de défense augmentée

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Dégâts subis réduits

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Pénétration de défense augmentée

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Taux de coup critique augmenté
**Débloque :** Dégâts subis réduits

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Pénétration: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Dégâts subis réduits

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Taux de coup critique augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Dégâts subis réduits

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Pénétration de défense augmentée
**Débloque :** Taux de coup critique augmenté

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Réduction des dégâts subis: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Dégâts subis réduits
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

#### Taux de coup critique augmenté

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** Dégâts subis réduits
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 1 SpecialPoint - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,33 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| II | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,66 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |
| III | 1 SpecialPoint/rang - par rang probable | Taux critique: 0,33 % | +0,33 % | 0,99 % | NON DÉTERMINÉ (convergence multi-parent) | FORTEMENT PROBABLE; coût FORTEMENT PROBABLE |

## ÉVEIL DU MONARQUE

### Branche 1 — Vision ombrale

#### L'Aube du règne I

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** L'Aube du règne II, L'Aube du règne III

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | EXRecovery | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### L'Aube du règne II

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** L'Aube du règne I
**Débloque :** L'Aube du règne IV

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Gain de jauge: 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### L'Aube du règne III

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** L'Aube du règne I
**Débloque :** L'Aube du règne IV

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Gain de jauge: 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### L'Aube du règne IV

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** L'Aube du règne II, L'Aube du règne III (convergence: condition exacte NON DÉTERMINÉE)
**Débloque :** Lame vampirique, Tranchant des ombres I, Tempête d'ombre I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Gain de jauge: 2000 | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Lame vampirique

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** L'Aube du règne IV
**Débloque :** Ruée de l'ombre

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Tranchant des ombres I

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** L'Aube du règne IV
**Débloque :** Tranchant des ombres II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Tempête d'ombre I

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** L'Aube du règne IV
**Débloque :** Tempête d'ombre II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Ruée de l'ombre

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Lame vampirique
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Tranchant des ombres II

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Tranchant des ombres I
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Modification de compétence | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

#### Tempête d'ombre II

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Tempête d'ombre I
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | NON DÉTERMINÉ (convergence multi-parent) | CONFIRMÉ PAR LES GAMEDATA |

### Branche 2 — Libération d'âme

#### Cape du monarque

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Acte des ombres I, Acte des ombres II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Acte des ombres I

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Cape du monarque
**Débloque :** Âme du clair de lune I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Acte des ombres II

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Cape du monarque
**Débloque :** Enchaînement d'ombre I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 3 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Âme du clair de lune I

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Acte des ombres I
**Débloque :** Âme du clair de lune II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Modification de compétence | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Enchaînement d'ombre I

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Acte des ombres II
**Débloque :** Enchaînement d'ombre II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Âme du clair de lune II

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Âme du clair de lune I
**Débloque :** Présage de destruction I

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Enchaînement d'ombre II

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Enchaînement d'ombre I
**Débloque :** Présage de destruction II

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Présage de destruction I

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Âme du clair de lune II
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Effet déclenché | Non chiffré | Non chiffré | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Présage de destruction II

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Enchaînement d'ombre II
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SpecialPoint | Dégâts de compétence: 1000 | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

# STRUCTURES NON RATTACHÉES

## CRITIQUE ET PÉNÉTRATION

### Branche 1 — Critique et pénétration - nom déduit

#### Taux de coup critique 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Taux de coup critique 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Taux critique: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Taux critique: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Taux critique: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Dégâts de coup critique 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Dégâts critiques: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Dégâts critiques: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Dégâts critiques: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** Pénétration de défense 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Pénétration: 100 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 3 SkillPoint/rang | Pénétration: 100 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 4 SkillPoint/rang | Pénétration: 100 | NON DÉTERMINÉ | NON DÉTERMINÉ | 0 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Taux de coup critique 1
**Débloque :** Taux de coup critique 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Taux critique: 2 % | +2 % | 2 % | 2 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Taux critique: 2 % | +2 % | 4 % | 2 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Taux critique: 2 % | +2 % | 6 % | 2 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Dégâts de coup critique 1
**Débloque :** Dégâts de coup critique 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Dégâts critiques: 2 % | +2 % | 2 % | 2 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Dégâts critiques: 2 % | +2 % | 4 % | 2 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Dégâts critiques: 2 % | +2 % | 6 % | 2 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** Pénétration de défense 1
**Débloque :** Pénétration de défense 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Pénétration: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 3 SkillPoint/rang | Pénétration: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 4 SkillPoint/rang | Pénétration: 200 | NON DÉTERMINÉ | NON DÉTERMINÉ | 2 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Taux de coup critique 2
**Débloque :** Taux de coup critique 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Taux critique: 3 % | +3 % | 3 % | 4 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Taux critique: 3 % | +3 % | 6 % | 4 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Taux critique: 3 % | +3 % | 9 % | 4 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Dégâts de coup critique 2
**Débloque :** Dégâts de coup critique 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Dégâts critiques: 3 % | +3 % | 3 % | 4 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Dégâts critiques: 3 % | +3 % | 6 % | 4 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Dégâts critiques: 3 % | +3 % | 9 % | 4 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** Pénétration de défense 2
**Débloque :** Pénétration de défense 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Pénétration: 300 | NON DÉTERMINÉ | NON DÉTERMINÉ | 4 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 3 SkillPoint/rang | Pénétration: 300 | NON DÉTERMINÉ | NON DÉTERMINÉ | 4 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 4 SkillPoint/rang | Pénétration: 300 | NON DÉTERMINÉ | NON DÉTERMINÉ | 4 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Taux de coup critique 3
**Débloque :** Taux de coup critique 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Taux critique: 4 % | +4 % | 4 % | 6 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Taux critique: 4 % | +4 % | 8 % | 6 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Taux critique: 4 % | +4 % | 12 % | 6 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Dégâts de coup critique 3
**Débloque :** Dégâts de coup critique 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Dégâts critiques: 4 % | +4 % | 4 % | 6 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Dégâts critiques: 4 % | +4 % | 8 % | 6 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Dégâts critiques: 4 % | +4 % | 12 % | 6 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** Pénétration de défense 3
**Débloque :** Pénétration de défense 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Pénétration: 400 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 4 SkillPoint/rang | Pénétration: 400 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 5 SkillPoint/rang | Pénétration: 400 | NON DÉTERMINÉ | NON DÉTERMINÉ | 6 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Taux de coup critique 4
**Débloque :** Taux de coup critique 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Taux critique: 5 % | +5 % | 5 % | 9 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Taux critique: 5 % | +5 % | 10 % | 9 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Taux critique: 5 % | +5 % | 15 % | 9 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Dégâts de coup critique 4
**Débloque :** Dégâts de coup critique 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Dégâts critiques: 5 % | +5 % | 5 % | 9 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Dégâts critiques: 5 % | +5 % | 10 % | 9 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Dégâts critiques: 5 % | +5 % | 15 % | 9 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** Pénétration de défense 4
**Débloque :** Pénétration de défense 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Pénétration: 500 | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 4 SkillPoint/rang | Pénétration: 500 | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 5 SkillPoint/rang | Pénétration: 500 | NON DÉTERMINÉ | NON DÉTERMINÉ | 9 pts requis | CONFIRMÉ PAR LES GAMEDATA |

#### Taux de coup critique 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Taux de coup critique 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Taux critique: 6 % | +6 % | 6 % | 12 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Taux critique: 6 % | +6 % | 12 % | 12 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Taux critique: 6 % | +6 % | 18 % | 12 pts requis | FORTEMENT PROBABLE |

#### Dégâts de coup critique 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Dégâts de coup critique 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Dégâts critiques: 6 % | +6 % | 6 % | 12 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Dégâts critiques: 6 % | +6 % | 12 % | 12 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Dégâts critiques: 6 % | +6 % | 18 % | 12 pts requis | FORTEMENT PROBABLE |

#### Pénétration de défense 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** Pénétration de défense 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Pénétration: 600 | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| II | 4 SkillPoint/rang | Pénétration: 600 | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |
| III | 5 SkillPoint/rang | Pénétration: 600 | NON DÉTERMINÉ | NON DÉTERMINÉ | 12 pts requis | CONFIRMÉ PAR LES GAMEDATA |

## STATS PRINCIPALES

### Branche 1 — Stats principales - nom déduit

#### Attaque augmentée 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 2
**Prérequis :** RACINE
**Débloque :** Attaque augmentée 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Attaque: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Attaque: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Attaque: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 3
**Prérequis :** RACINE
**Débloque :** Défense augmentée 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Défense: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Défense: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Défense: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 1

**Position dans l'arbre :** profondeur technique 1, rangée UI 1, X 4
**Prérequis :** RACINE
**Débloque :** PV augmentés 2

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | PV: 1 % | +1 % | 1 % | 0 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | PV: 1 % | +1 % | 2 % | 0 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | PV: 1 % | +1 % | 3 % | 0 pts requis | FORTEMENT PROBABLE |

#### Attaque augmentée 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 2
**Prérequis :** Attaque augmentée 1
**Débloque :** Attaque augmentée 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Attaque: 2 % | +2 % | 2 % | 2 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Attaque: 2 % | +2 % | 4 % | 2 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Attaque: 2 % | +2 % | 6 % | 2 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 3
**Prérequis :** Défense augmentée 1
**Débloque :** Défense augmentée 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Défense: 2 % | +2 % | 2 % | 2 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Défense: 2 % | +2 % | 4 % | 2 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Défense: 2 % | +2 % | 6 % | 2 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 2

**Position dans l'arbre :** profondeur technique 2, rangée UI 2, X 4
**Prérequis :** PV augmentés 1
**Débloque :** PV augmentés 3

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | PV: 2 % | +2 % | 2 % | 2 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | PV: 2 % | +2 % | 4 % | 2 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | PV: 2 % | +2 % | 6 % | 2 pts requis | FORTEMENT PROBABLE |

#### Attaque augmentée 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 2
**Prérequis :** Attaque augmentée 2
**Débloque :** Attaque augmentée 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Attaque: 3 % | +3 % | 3 % | 4 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Attaque: 3 % | +3 % | 6 % | 4 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Attaque: 3 % | +3 % | 9 % | 4 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 3
**Prérequis :** Défense augmentée 2
**Débloque :** Défense augmentée 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | Défense: 3 % | +3 % | 3 % | 4 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | Défense: 3 % | +3 % | 6 % | 4 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | Défense: 3 % | +3 % | 9 % | 4 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 3

**Position dans l'arbre :** profondeur technique 3, rangée UI 3, X 4
**Prérequis :** PV augmentés 2
**Débloque :** PV augmentés 4

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 2 SkillPoint | PV: 3 % | +3 % | 3 % | 4 pts requis | FORTEMENT PROBABLE |
| II | 3 SkillPoint/rang | PV: 3 % | +3 % | 6 % | 4 pts requis | FORTEMENT PROBABLE |
| III | 4 SkillPoint/rang | PV: 3 % | +3 % | 9 % | 4 pts requis | FORTEMENT PROBABLE |

#### Attaque augmentée 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 2
**Prérequis :** Attaque augmentée 3
**Débloque :** Attaque augmentée 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Attaque: 4 % | +4 % | 4 % | 6 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Attaque: 4 % | +4 % | 8 % | 6 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Attaque: 4 % | +4 % | 12 % | 6 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 3
**Prérequis :** Défense augmentée 3
**Débloque :** Défense augmentée 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Défense: 4 % | +4 % | 4 % | 6 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Défense: 4 % | +4 % | 8 % | 6 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Défense: 4 % | +4 % | 12 % | 6 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 4

**Position dans l'arbre :** profondeur technique 4, rangée UI 4, X 4
**Prérequis :** PV augmentés 3
**Débloque :** PV augmentés 5

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | PV: 4 % | +4 % | 4 % | 6 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | PV: 4 % | +4 % | 8 % | 6 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | PV: 4 % | +4 % | 12 % | 6 pts requis | FORTEMENT PROBABLE |

#### Attaque augmentée 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 2
**Prérequis :** Attaque augmentée 4
**Débloque :** Attaque augmentée 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Attaque: 5 % | +5 % | 5 % | 9 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Attaque: 5 % | +5 % | 10 % | 9 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Attaque: 5 % | +5 % | 15 % | 9 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 3
**Prérequis :** Défense augmentée 4
**Débloque :** Défense augmentée 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Défense: 5 % | +5 % | 5 % | 9 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Défense: 5 % | +5 % | 10 % | 9 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Défense: 5 % | +5 % | 15 % | 9 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 5

**Position dans l'arbre :** profondeur technique 5, rangée UI 5, X 4
**Prérequis :** PV augmentés 4
**Débloque :** PV augmentés 6

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | PV: 5 % | +5 % | 5 % | 9 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | PV: 5 % | +5 % | 10 % | 9 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | PV: 5 % | +5 % | 15 % | 9 pts requis | FORTEMENT PROBABLE |

#### Attaque augmentée 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 2
**Prérequis :** Attaque augmentée 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Attaque: 6 % | +6 % | 6 % | 12 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Attaque: 6 % | +6 % | 12 % | 12 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Attaque: 6 % | +6 % | 18 % | 12 pts requis | FORTEMENT PROBABLE |

#### Défense augmentée 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 3
**Prérequis :** Défense augmentée 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | Défense: 6 % | +6 % | 6 % | 12 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | Défense: 6 % | +6 % | 12 % | 12 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | Défense: 6 % | +6 % | 18 % | 12 pts requis | FORTEMENT PROBABLE |

#### PV augmentés 6

**Position dans l'arbre :** profondeur technique 6, rangée UI 6, X 4
**Prérequis :** PV augmentés 5
**Débloque :** aucun

| Rang | Coût | Effet | Gain | Cumul | Accès | Confiance |
|---:|---|---|---|---|---|---|
| I | 3 SkillPoint | PV: 6 % | +6 % | 6 % | 12 pts requis | FORTEMENT PROBABLE |
| II | 4 SkillPoint/rang | PV: 6 % | +6 % | 12 % | 12 pts requis | FORTEMENT PROBABLE |
| III | 5 SkillPoint/rang | PV: 6 % | +6 % | 18 % | 12 pts requis | FORTEMENT PROBABLE |

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
- Export canonique web-ready: `analysis/data/sjw_talent_tree.json`.

