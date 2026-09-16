# Solo Leveling ARISE OVERDRIVE — Project Rules

## Objectif du projet

Ce repository doit devenir progressivement une ressource GitHub fiable,
vérifiable, lisible directement sur GitHub, compréhensible par un joueur,
exploitable techniquement par d'autres développeurs et réutilisable par la
communauté **Solo Leveling: ARISE OVERDRIVE**.

Le projet documente les mécaniques de **Solo Leveling: ARISE OVERDRIVE PC/Steam**
à partir des GameData réelles, notamment les arbres de talents, leur topologie,
les coûts, les rangs, les gains, les conditions d'activation, les compétences et
buffs associés, les statistiques, les formules démontrables, les données
techniques de vérification, puis les builds lorsque les données sont fiables.

Le repository doit avoir deux niveaux de lecture complémentaires :

1. une couche HUMAN destinée aux joueurs et lecteurs GitHub ;
2. une couche TECHNICAL / DATA destinée à la vérification, au reverse engineering
   et aux futurs outils.

La couche HUMAN ne doit être ni un dump des GameData, ni une simple copie
textuelle de l'interface du jeu. Elle doit apporter une vraie valeur :
topologie, progression, gains, coûts, relations entre talents et informations
utiles à la compréhension du système.

Pour les planners et vues interactives, une information brute vérifiée vaut
mieux qu'une absence d'information. Un talent doit afficher ce qu'il apporte
même si la conversion exacte runtime reste inconnue: ID, champ source, valeur
raw, description GameData, cooldown, coûts de ressource, coefficients, gains
EX / jauge, buffs liés, conditions, durée, stacks et effets déclenchés doivent
être exposés quand ils existent. Toute valeur affichée sans formule validée doit
porter un indicateur `WIP` / `NON DÉTERMINÉ` au niveau du champ concerné.

La couche TECHNICAL doit permettre de retrouver les données sources,
identifiants, valeurs raw, relations et niveaux de confiance ayant conduit aux
informations HUMAN.

La présentation GitHub fait partie du produit final du projet. La fiabilité reste
cependant prioritaire : une donnée jolie mais non démontrée est moins utile
qu'une donnée explicitement marquée `NON DÉTERMINÉE`.

## 1. Périmètre et sources

- Projet exclusivement consacré à **Solo Leveling: ARISE OVERDRIVE PC/Steam**.
- Ne jamais importer une mécanique du jeu mobile sans preuve explicite qu'elle
  existe dans OVERDRIVE.
- Ordre de confiance :
  1. GameData décodés
  2. screenshots / observations utilisateur
  3. sources web explicitement OVERDRIVE
  4. communauté
- Ne jamais compléter une information manquante "par logique".
- Une valeur qui semble correspondre n'est pas une preuve.
- En cas de contradiction, conserver et signaler la contradiction au lieu de
  choisir arbitrairement.

### Niveaux de confiance

Utiliser selon le cas :

- `CONFIRMÉ PAR LES GAMEDATA`
- `CALCULÉ À PARTIR DES GAMEDATA`
- `FORTEMENT PROBABLE`
- `HYPOTHÈSE`
- `NON DÉTERMINÉ`

La confiance doit pouvoir être attribuée **par champ**, pas seulement au talent
entier.

## 2. Données brutes et interprétation

Toujours conserver séparément :

- valeur brute GameData ;
- valeur interprétée ;
- valeur affichée / observée ;
- niveau de confiance.
- statut `WIP` si la valeur est utile au planner mais que sa conversion,
  formule, unité ou application runtime n'est pas encore déterminée.

Règles :

- Ne jamais écraser une donnée brute par son interprétation.
- Ne jamais convertir automatiquement une valeur raw en `%`.
- Ne jamais forcer une formule pour faire correspondre un screenshot.
- Ne jamais calculer un rendement si l'unité, le coût ou le gain marginal ne
  sont pas démontrés.
- Ne jamais masquer une valeur raw utile au planner uniquement parce que son
  rendement ou son pourcentage réel n'est pas encore démontré; l'afficher avec
  ses ID sources et un statut `WIP`.
- Des valeurs raw de familles différentes ne sont pas directement comparables.
- Une formule validée pour une statistique ne doit pas être généralisée aux
  autres sans preuve.
- Ne jamais inventer les champs absents.

## 3. Conservation des données

Une représentation normalisée doit conserver au minimum :

- NodeID
- logical_talent_id
- logical_rank
- système
- arbre
- section
- progression_depth
- visual_row
- position
- parents
- coûts
- rangs
- BuffID / SkillID
- effets
- valeurs raw
- valeurs interprétées
- confiance

HUMAN, TECHNICAL, Mermaid et futurs calculateurs doivent dériver d'une source
commune quand elle existe. Une perte d'information lors d'une amélioration est
une **régression**.

Le planner web doit disposer d'une base machine-readable dédiée aux effets
résolus (`BuffID`, `SkillID`, références actives, buffs déclenchés et champs raw)
afin d'afficher les détails et tooltips sans relire les tables GameData
complètes. Cette base doit rester dérivée des GameData normalisés/décodés.

Pour les arbres de talents, l'export canonique machine-readable doit être généré
depuis les GameData normalisés avant les vues de rendu :

```text
GameData décodés
    ↓
modèle canonique
    ↓
HUMAN / TECHNICAL / CSV / futur WEB
```

Le futur frontend web doit consommer le modèle canonique sans reconstruire ni
deviner les parents, enfants, rangs internes ou positions visuelles.

Un `NodeID` est un nœud technique GameData, pas forcément un talent HUMAN.
Deux `NodeID` différents restent toujours deux nœuds techniques distincts et ne
doivent jamais être fusionnés dans les données brutes. En revanche, plusieurs
`NodeID` peuvent appartenir à un même talent logique seulement s'il est démontré
qu'ils représentent ses rangs ou upgrades successifs.

Ne jamais déduire un rang interne depuis un suffixe romain dans le nom localisé
du talent. Des libellés comme `Talent I`, `Talent II`, `Talent III` peuvent être
des nœuds visuels distincts, une série/famille de talents, ou de vrais rangs
internes seulement si un champ GameData de rang/niveau du même nœud le démontre.
Une famille/série sémantique ne doit jamais remplacer la topologie `NodeID` /
Parent du graphe.

`progression_depth` est calculé depuis les relations Parent/Enfant.
`visual_row` conserve la rangée verticale GameData/UI (`NodeTierY`). Ne jamais
utiliser `NodeTierY` comme chemin de progression.

## 4. Builds et optimisation

Ne pas optimiser les builds avant validation de :

1. topologie ;
2. coûts ;
3. effets ;
4. rangs / progression ;
5. conditions d'activation ;
6. formules ;
7. coûts de chemin.

Pour les futures analyses :

- comparer des **chemins d'investissement**, pas seulement des talents isolés ;
- distinguer coût direct, seuil d'accès et coût de chemin ;
- ne pas classer globalement un talent profond uniquement sur son rendement
  direct ;
- raisonner séparément sur :
  - classe / spécialisation ;
  - arme équipée 1 ;
  - arme équipée 2 ;
  - systèmes communs ;
- le fait que deux armes soient équipées ne prouve pas que seuls deux arbres
  d'armes peuvent recevoir des points ;
- ne jamais supposer une exclusivité de classe, branche ou arme sans preuve.

## 5. Workflow

- Travailler par delta.
- Modifier uniquement les données / sections concernées.
- Ne pas régénérer une section inchangée.
- Ne pas reformater inutilement les fichiers.
- Garder un ordre déterministe pour produire des diffs Git propres.
- Tester une nouvelle interprétation sur un petit échantillon avant de la
  généraliser.
- Une convention validée sur Assassin reste `CONFIRMÉE POUR ASSASSIN` tant
  qu'elle n'est pas vérifiée ailleurs.
- Ne pas refaire une recherche déjà résolue si les données normalisées suffisent.
- Élargir le scope uniquement si une dépendance réelle l'impose.
- Quand la tâche demandée est terminée : STOP.
- Ne pas lancer spontanément une autre analyse ou refactorisation.

## 6. Git / sauvegarde des interventions

Avant toute tâche susceptible de modifier le repository :

1. exécuter `git status --short` ;
2. mémoriser l'état initial du worktree ;
3. considérer les modifications déjà présentes comme appartenant à
   l'utilisateur sauf preuve contraire ;
4. ne jamais les écraser, restaurer ou inclure silencieusement dans le commit
   final.

Après chaque tâche utilisateur terminée qui a réellement modifié le repository :

1. vérifier les fichiers modifiés ;
2. exécuter les validations/tests pertinents ;
3. vérifier le diff correspondant à la tâche ;
4. créer un commit Git local contenant uniquement les modifications de cette
   tâche ;
5. utiliser un message de commit court, clair et descriptif ;
6. vérifier ensuite l'état du worktree.

Le commit marque la fin réussie de l'intervention.

Ne pas créer de commit si :

- aucun fichier n'a été modifié ;
- la tâche est incomplète ;
- une erreur connue importante reste non résolue ;
- les validations nécessaires échouent.

Ne jamais :

- utiliser `git add -A` aveuglément si des modifications préexistantes non liées
  sont présentes ;
- mélanger plusieurs tâches indépendantes dans le même commit ;
- amender un ancien commit sauf demande explicite ;
- faire `git reset --hard` ;
- faire `git clean` pour obtenir artificiellement un worktree propre ;
- supprimer ou restaurer des modifications utilisateur préexistantes ;
- committer credentials, caches, fichiers temporaires ou artefacts qui ne
  doivent pas appartenir au repository ;
- faire de push distant sauf demande explicite.

Si des modifications non liées existaient avant l'intervention :

- les préserver ;
- exclure autant que possible leurs fichiers/hunks du commit ;
- laisser ces modifications intactes après le commit ;
- les signaler dans le résumé final.

Si un même fichier contient à la fois des modifications utilisateur
préexistantes et des modifications nécessaires à la tâche Codex, examiner le
diff et utiliser une méthode sûre pour ne committer que les changements
appartenant à la tâche, si cela est possible. Si la séparation n'est pas sûre,
ne pas risquer de modifier ou committer le travail utilisateur et signaler le
conflit.

## 7. Réponses Codex et économie de tokens

Par défaut, répondre uniquement avec :

- fichiers modifiés ;
- delta effectué ;
- validations ;
- incertitudes restantes.

Ne pas :

- recopier les rapports complets ;
- recopier les Mermaid complets si quelques lignes changent ;
- réexpliquer longuement les règles déjà validées ;
- réimprimer des tables inchangées.

Pour les Mermaid et rapports déjà corrects :

1. comparer l'existant ;
2. identifier le delta ;
3. patcher uniquement les nœuds / arêtes / blocs concernés ;
4. résumer le changement sans recopier le contenu complet.

Si une règle globale du générateur change, modifier le générateur puis régénérer
les fichiers nécessaires sur disque, mais ne montrer dans la réponse qu'un
extrait de contrôle et le résumé du delta.

Après une intervention ayant produit un commit, la réponse doit rester courte et
indiquer seulement :

- commit : `<hash court> <message>` ;
- fichiers modifiés ;
- validations effectuées ;
- éventuelles incertitudes ou modifications utilisateur restées hors commit.

Ne pas recopier le diff complet sauf demande explicite.
