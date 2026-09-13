# Tools Rules

Ces règles spécialisent le `AGENTS.md` racine pour les scripts de `tools/`.

## Données et normalisation

- Maintenir une représentation normalisée unique quand un script reconstruit des
  systèmes exploités par plusieurs sorties.
- Pour les arbres de talents, générer le modèle canonique machine-readable avant
  les vues de rendu. CSV, HUMAN, TECHNICAL, Mermaid et futur WEB doivent rester
  des consommateurs de ce contrat, pas des sources de vérité concurrentes.
- Construire des index réutilisables :
  - `NodeID -> node`
  - `LogicalTalentID -> logical_talent`
  - `BuffID -> buff`
  - `SkillID -> skill`
  - `ParentID -> children`
  - `NodeGroup -> nodes`
- Ne pas rescanner ou redécoder toute la GameData si la représentation
  normalisée contient déjà l'information nécessaire.
- Les sorties doivent être déterministes : à données identiques, deux
  générations doivent produire le même ordre et le même contenu fonctionnel.

## Arbres de talents : modèle structurel

Un arbre de talents est un **graphe orienté**, pas une liste par rangée visuelle.

- Les relations `Parent` définissent les chemins de progression.
- Les enfants doivent être dérivés automatiquement depuis les `Parent`.
- `progression_depth` indique la profondeur réelle calculée depuis `Parent`.
- `visual_row` conserve la valeur GameData `NodeTierY`.
- `NodeTierY` ne définit jamais à lui seul le chemin.
- Un lien Parent peut sauter un ou plusieurs `NodeTierY` ; ce n'est pas une
  erreur.
- Ne jamais créer de connexion implicite entre deux talents uniquement parce
  qu'ils appartiennent à des rangées visuelles successives.
- Préserver les racines, bifurcations, convergences et feuilles / chemins
  terminaux.
- `PALIER != RANG`.
- Deux `NodeID` différents restent deux nœuds techniques distincts même si leur
  texte est identique.
- Plusieurs `NodeID` peuvent appartenir au même talent logique seulement si les
  GameData, références communes, champs de rang ou observations validées le
  démontrent.
- Ne jamais fusionner des `NodeID` uniquement par suffixe romain, préfixe de nom
  ou similarité de texte.
- Plusieurs effets appartenant au même `NodeID` restent **un seul talent
  multi-effets**.
- Ne pas confondre `NodeGroup` / section UI avec un chemin linéaire.
- Ne pas supposer qu'un talent, une branche ou une classe est mutuellement
  exclusif sans preuve.
- Si l'exclusivité n'est pas démontrée : `NON DÉTERMINÉ`.

### Nœuds spéciaux

Un nœud spécial comme Overdrive ne doit pas être rattaché artificiellement à une
section simplement parce qu'il partage un `NodeGroup` technique ou une proximité
de coordonnées.

La structure UI validée par screenshots peut servir à corriger cette
représentation, sans remplacer les GameData comme source primaire.

## Position, coordonnées et graphes

Conserver pour chaque nœud :

- `NodeID`
- `LogicalTalentID`
- `LogicalRank`
- `NodeGroup`
- `NodeTierY`
- `progression_depth`
- `visual_row`
- position X/Y
- `VisualColumn`
- offsets
- Parent(s)

Ces données constituent la source structurelle des Mermaid et autres
visualisations.

Règles :

- Les coordonnées brutes peuvent être masquées dans HUMAN mais ne doivent jamais
  être supprimées.
- Un écart entre `progression_depth` et `visual_row` n'est pas une erreur.
- Un lien Parent qui saute une ou plusieurs rangées visuelles n'est pas une
  erreur.
- Les Mermaid doivent être générés depuis la même source normalisée que les
  rapports.
- Ne pas maintenir manuellement deux versions indépendantes de la topologie.
- Les screenshots servent à valider la représentation des GameData, pas à
  remplacer les GameData.
- Une convention visuelle validée sur un arbre ne doit pas être généralisée aux
  autres sans vérification.
- Les offsets peuvent être conservés pour reproduire la disposition visuelle,
  mais ils ne prouvent jamais une relation Parent/Enfant.

## Talents, effets et progression

Chaque talent HUMAN généré doit permettre de comprendre :

- où il se trouve ;
- son/ses parent(s) ;
- ce qu'il débloque ;
- son coût ;
- son effet réel ;
- ses rangs ;
- sa progression ;
- son gain marginal ;
- son cumul ;
- son rendement si démontré.

Une simple description comme `Effet déclenché` ou `Compétence active` est un
**dernier recours**.

Suivre les `BuffID`, `SkillID` et références liées pour récupérer autant que
possible :

- stat / effet concerné ;
- valeur ;
- condition ;
- durée ;
- cooldown ;
- stacks ;
- multiplicateur ;
- compétence concernée ;
- cible ;
- chance de déclenchement ;
- autres effets disponibles.

## Talents multi-rangs

Conserver séparément :

- coût de chaque rang ;
- raw ;
- valeur affichée ;
- gain marginal ;
- cumul.

Ne jamais supposer que la valeur affichée au rang N est le gain ajouté par ce
rang.

Conserver les phénomènes de cumul / faux lissage déjà observés.

Exemple conceptuel :

| Rang | Valeur affichée | Gain marginal | Cumul |
|---:|---:|---:|---:|
| 1 | +1 % | +1 % | +1 % |
| 2 | +2 % | +1 % | +2 % |
| 3 | +3 % | +1 % | +3 % |

Si cette interprétation n'est pas démontrée, marquer le gain marginal
`NON DÉTERMINÉ`.

## Coûts et rendement

- Si les coûts apparaissent sous forme `2 / 3 / 4`, ne pas les additionner
  automatiquement.
- Ne pas supposer qu'il s'agit forcément d'un coût par rang.
- `SkillPoint`, `WeaponPoint`, `SpecialPoint`, `IdentityPoint`, etc. sont des
  monnaies distinctes et non directement comparables.
- Calculer un rendement uniquement si :
  1. le coût est compris ;
  2. l'unité du gain est comprise ;
  3. le gain marginal est compris ;
  4. la division produit une métrique réellement interprétable.
- Une valeur raw comme `320` ne doit pas devenir automatiquement `64/pt` parce
  que le coût vaut 5.

## Contrôles automatiques

À chaque génération pertinente vérifier :

- aucun NodeID perdu ;
- aucun NodeID dupliqué ;
- tous les Parent valides sauf racines ;
- children cohérents avec Parent ;
- absence de cycles inattendus ;
- profondeur de progression calculable pour chaque nœud représenté ;
- chaque NodeID appartient à au plus un talent logique ;
- chaque rang logique est unique dans son talent logique ;
- le regroupement HUMAN ne crée aucune relation Parent/Enfant inexistante ;
- nombre de nœuds source = nombre de nœuds normalisés ;
- nombre de nœuds normalisés = nombre de nœuds représentés ;
- aucune donnée précédemment disponible supprimée par une nouvelle version.
