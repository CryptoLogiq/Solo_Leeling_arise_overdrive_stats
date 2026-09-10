# Reports Rules

Ces règles spécialisent le `AGENTS.md` racine pour les rapports Markdown de
`analysis/reports/`.

## Rapport HUMAN

Ordre principal :

`Système -> Arbre -> Section / NodeGroup -> Nœud visuel / Talent -> Rang(s) internes`

Règles :

- Ne jamais trier la vue principale par stat, rendement ou intérêt de build.
- Les vues transversales par stat sont uniquement des annexes.
- Le rendement est une information du talent, jamais un critère de classement.
- La progression technique `progression_depth`, calculée depuis les parents,
  peut décrire la position d'accès d'un talent logique, mais ne doit jamais
  découper les rangs d'un même talent entre plusieurs sections HUMAN.
- La rangée visuelle `NodeTierY` ne doit pas être présentée comme un mécanisme
  de progression.
- Un `NodeID` est un nœud GameData technique et un nœud visuel potentiel.
  HUMAN ne doit regrouper plusieurs NodeID dans une seule fiche que si un champ
  GameData de rang/niveau ou une preuve validée démontre qu'ils sont les rangs
  internes d'un même talent.
- Ne jamais fusionner plusieurs NodeID en talent logique sur le seul nom.
- Ne jamais déduire un rang interne depuis un suffixe romain dans le nom
  localisé. Une famille/série de talents ne remplace jamais les nœuds du graphe.
- Les détails techniques lourds (`NodeID`, `BuffID`, offsets, raw complexes)
  peuvent rester dans TECHNICAL / GRAPH_DATA.
- Les tableaux de gains / progression doivent rester dans HUMAN.
- Chaque talent doit apparaître exactement une fois dans la représentation
  principale de son arbre.
- La topologie et les gains sont deux dimensions complémentaires : améliorer
  l'une ne doit jamais supprimer l'autre.

### Format recommandé d'une fiche talent

**Position dans l'arbre :** profondeur technique 4 · rangée UI 4 · gauche
**Parent :** Arts verticaux
**Débloque :** Taux critique augmenté II

| Rang | Coût | Effet | Gain | Cumul | Accès |
|---:|---|---|---:|---:|---|
| I | ... | ... | ... | ... | ... |

Ajouter ensuite uniquement les informations utiles : condition, durée,
compétence concernée, confiance, incertitude restante.

## Qualité Markdown / GitHub

Les fichiers Markdown destinés à être lus par un humain doivent être optimisés
pour le rendu GitHub sans sacrifier les données.

Cette règle concerne principalement :

- `*_HUMAN.md`
- rapports d'analyse
- documentation
- vues de talents / builds

Les fichiers TECHNICAL, JSON et données intermédiaires peuvent rester plus
compacts et orientés machine.

### Structure

Pour les documents longs, utiliser une hiérarchie cohérente :

```text
# Titre
## Arbre / système
### Section / NodeGroup
#### Nœud visuel / Talent
##### Détails techniques optionnels
```

Ne jamais utiliser les niveaux de titre uniquement pour obtenir une taille de
police.

### Introduction et sommaire

Chaque gros rapport HUMAN doit commencer par un résumé court indiquant :

- ce que contient le document ;
- son niveau de validation ;
- ce qui reste NON DÉTERMINÉ ;
- éventuellement la version/date des GameData si disponible.

Pour les documents longs, ajouter un sommaire compact avec les grandes sections
seulement. Ne pas créer un sommaire contenant chaque talent.

### Lecture progressive

Présenter l'information dans cet ordre :

1. vue / graphe de l'arbre ;
2. talents logiques dans l'ordre du jeu ;
3. gains et progression ;
4. informations complémentaires ;
5. détails techniques / preuves si nécessaires.

Le lecteur ne doit pas traverser des `NodeID` et `BuffID` pour comprendre ce que
fait un talent.

### Mermaid

Conserver les graphes Mermaid lorsqu'ils améliorent la compréhension.

Ils doivent privilégier :

- nom du talent ;
- niveau de progression ;
- connexions Parent -> Enfant.

Les NodeID peuvent être présents discrètement pour contrôle.

Éviter de surcharger les nœuds avec BuffID, raw values, coûts détaillés ou
longues descriptions.

### Tables

Préférer plusieurs petits tableaux contextualisés à un tableau géant de
nombreuses colonnes.

Une table HUMAN doit rester lisible sur GitHub sans nécessiter de suivre une
ligne sur plusieurs écrans.

### Valeurs inconnues

Éviter de remplir visuellement les tableaux avec des dizaines de
`NON DÉTERMINÉ`.

Lorsque plusieurs informations liées sont inconnues, préférer une note compacte,
par exemple :

> **Non déterminé :** conversion runtime de la valeur raw et rendement.

Ne jamais masquer une incertitude importante.

### Données techniques repliables

Quand des données techniques sont utiles au lecteur mais secondaires, utiliser
avec modération :

```html
<details>
<summary>Données techniques</summary>

- NodeID : ...
- BuffID : ...
- Raw : ...
- Position : ...
- Confiance : ...

</details>
```

### Cohérence visuelle

Conserver les mêmes conventions dans tous les rapports :

- même ordre de colonnes ;
- mêmes noms de champs ;
- mêmes termes ;
- mêmes niveaux de titres ;
- même représentation de la confiance ;
- même format des coûts et pourcentages.

Pour HUMAN en français, privilégier la virgule décimale : `+0,8 %`.

Les valeurs raw techniques peuvent conserver leur représentation source.

### Navigation HUMAN / TECHNICAL

Lorsque pertinent, permettre au lecteur de retrouver les détails techniques sans
les dupliquer.

Ne jamais recopier tout TECHNICAL dans HUMAN.

### Git-friendly

- ordre déterministe ;
- format stable ;
- ne pas modifier arbitrairement les titres ;
- ne pas reformater les parties inchangées ;
- éviter les diffs cosmétiques inutiles ;
- patcher uniquement les blocs concernés.

Objectif : un joueur ouvrant le Markdown sur GitHub doit pouvoir choisir son
arbre, comprendre sa topologie, parcourir les talents dans l'ordre du jeu et
voir immédiatement ce qu'ils apportent.
