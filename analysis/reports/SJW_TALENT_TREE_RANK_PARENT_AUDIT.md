# Audit rangs internes et parents

Audit ciblé généré depuis les GameData normalisées avant tout rendu web.

## Conclusion

- Un suffixe romain/numérique dans le nom localisé ne prouve pas un rang interne.
- Le rang interne provient du même `NodeID` quand le rang maximum source est supérieur à 1.
- `ParentNodeID` référence un `NodeID`, pas un rang interne précis; HUMAN affiche donc une seule relation tant qu'aucun champ GameData ne prouve une condition par rang.
- Une famille/série sémantique peut aider la lecture, mais elle ne remplace jamais la topologie du graphe.

## Échantillons validés

| Zone | Talent / nœud | NodeID | Rangs internes | Prérequis HUMAN | Débloque HUMAN | Détail rang / position |
|---|---|---:|---:|---|---|---|
| Assassin / Attaque sournoise | Embuscade I | 111201 | 1 | Ruée acérée | Arts verticaux | I: Node 111201, UI 2 X2 |
| Assassin / Attaque sournoise | Embuscade II | 111202 | 1 | Ruée acérée | Arts verticaux, Embuscade III - [Effet passif spécial] | I: Node 111202, UI 2 X4 |
| Assassin / Attaque sournoise | Embuscade III - [Effet passif spécial] | 111402 | 1 | Embuscade II | Embuscade IV | I: Node 111402, UI 4 X4 |
| Assassin / Attaque sournoise | Embuscade IV | 111602 | 1 | Embuscade III - [Effet passif spécial] | aucun | I: Node 111602, UI 6 X4 |
| Épée / Cœur d'acier | Hausse des dégâts de compétence à l'épée | 2150102 | 3 | RACINE | Charge frontale | I: Node 2150102, UI 1 X3 / II: Node 2150102, UI 1 X3 / III: Node 2150102, UI 1 X3 |
| Épée / Cœur d'acier | Charge frontale | 2150202 | 1 | Hausse des dégâts de compétence à l'épée | Protection de l'épée | I: Node 2150202, UI 2 X3 |
| Épée / Cœur d'acier | Attaque augmentée | 2150401 | 3 | Protection de l'épée | Cœur d'acier | I: Node 2150401, UI 4 X2 / II: Node 2150401, UI 4 X2 / III: Node 2150401, UI 4 X2 |
| Épée / Cœur d'acier | Défense augmentée | 2150403 | 3 | Protection de l'épée | Cœur d'acier | I: Node 2150403, UI 4 X4 / II: Node 2150403, UI 4 X4 / III: Node 2150403, UI 4 X4 |
| Épée / Cœur d'acier | Cœur d'acier | 2150502 | 1 | Attaque augmentée, Défense augmentée | Affrontement frontal | I: Node 2150502, UI 5 X3 |
| Critique et pénétration / Critique et pénétration | Taux de coup critique 5 | 1110501 | 3 | Taux de coup critique 4 | Taux de coup critique 6 | I: Node 1110501, UI 5 X2 / II: Node 1110501, UI 5 X2 / III: Node 1110501, UI 5 X2 |
| Critique et pénétration / Critique et pénétration | Taux de coup critique 6 | 1110601 | 3 | Taux de coup critique 5 | aucun | I: Node 1110601, UI 6 X2 / II: Node 1110601, UI 6 X2 / III: Node 1110601, UI 6 X2 |
| Stats principales / Stats principales | Attaque augmentée 5 | 119501 | 3 | Attaque augmentée 4 | Attaque augmentée 6 | I: Node 119501, UI 5 X2 / II: Node 119501, UI 5 X2 / III: Node 119501, UI 5 X2 |
| Stats principales / Stats principales | Attaque augmentée 6 | 119601 | 3 | Attaque augmentée 5 | aucun | I: Node 119601, UI 6 X2 / II: Node 119601, UI 6 X2 / III: Node 119601, UI 6 X2 |

## Points non généralisés

- Les familles visibles comme `Embuscade I..IV`, `Taux de coup critique 1..6` ou `Attaque augmentée 1..6` restent des chaînes de nœuds distincts tant qu'aucune preuve de fusion n'existe.
- Les cumuls des structures non rattachées restent marqués par leur confiance existante; cette passe valide le modèle nœud/rang/parent, pas les formules runtime.
