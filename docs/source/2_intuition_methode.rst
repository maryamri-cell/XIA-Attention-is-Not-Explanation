Remove standalone '---' separators to avoid small dashes in HTML output.

.. _intuition-methode:

=========================
2. Intuition de la Méthode
=========================

.. contents::
   :local:
   :depth: 2

L'Idée en Termes Simples
========================

Imaginez un **lecteur humain** qui doit déterminer si un avis de film est positif ou négatif.

En lisant la phrase, ce lecteur va naturellement **focaliser son attention** sur certains mots :

.. code-block:: text

    "Le film est absolument [fantastique] et [merveilleux] !"
                              ^^^^^^^^^^^     ^^^^^^^^^^^
                         → Mots clés observés

Ces mots clés (adjectifs, négations, intensifieurs) influencent directement sa conclusion.

**La question fondamentale** : Les modèles Transformer reproduisent-ils ce comportement humain de manière fiable ? Les poids d'attention correspondent-ils réellement aux mots qui causent la prédiction ?

Le Mécanisme d'Attention Expliqué
==================================

Structure Générale
~~~~~~~~~~~~~~~~~~~

Le Self-Attention fonctionne en trois étapes :

.. code-block:: text

    INPUT
      ↓
    [1] Calcul des Scores (Query × Key)
      ↓
    [2] Normalisation par Softmax (probabilités)
      ↓
    [3] Pondération des Valeurs
      ↓
    OUTPUT

Exemple Concret
~~~~~~~~~~~~~~~

Considérons la phrase :

.. code-block:: text

    "The film is good"

Tokenizée comme :

.. code-block:: text

    [CLS] the film is good [SEP]
      0    1   2   3   4    5

**Étape 1 : Calcul des scores**

Pour le token "good" (position 4), le modèle calcule des "scores d'attention" vers tous les autres tokens :

.. math::
   
   	ext{score}_{4 \to j} = query_4 \cdot key_j \quad \forall j

**Étape 2 : Normalisation**

Ces scores sont passés dans une fonction softmax pour obtenir des probabilités :

.. math::
   
   \alpha_{4,j} = \frac{e^{\text{score}_{4 \to j}}}{\sum_k e^{\text{score}_{4 \to k}}}

Résultat :

.. code-block:: text

    Position: [CLS]  the   film   is   good  [SEP]
    Attention: 0.10  0.15  0.20  0.15  0.25  0.15
                                        ↑
                        Le token "good" s'auto-observe fortement

**Étape 3 : Pondération des valeurs**

La sortie agrège les informations des autres tokens selon ces poids :

.. math::
   
   	ext{output}_4 = \sum_j \alpha_{4,j} \cdot value_j

Visualisation du Processus
==========================

Voici un diagramme du flux d'attention dans un Transformer :

.. code-block:: text

    ┌──────────────────────────────────────────┐
    │      TOKEN INPUT                         │
    │  "The film is good"                      │
    └──────────────────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────┐
    │   QUERY × KEY SCORES                     │
    │  [Combien chaque token regarde l'autre]  │
    └──────────────────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────┐
    │   SOFTMAX NORMALIZATION                  │
    │  [Conversion en probabilités]            │
    └──────────────────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────┐
    │   ATTENTION WEIGHTS                      │
    │   [Poids finaux: 0.10, 0.15, ...]        │
    └──────────────────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────┐
    │   VALUE WEIGHTING                        │
    │  [Agrégation pondérée des infos]         │
    └──────────────────────────────────────────┘
                          │
                          ▼
    ┌──────────────────────────────────────────┐
    │   OUTPUT EMBEDDING                       │
    │  [Nouvelle représentation du token]      │
    └──────────────────────────────────────────┘

Le Piège de l'Interprétation Naïve
==================================

Interprétation Courante (INCORRECTE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un praticien observe :

.. code-block:: text

    Poids d'attention pour la classe POSITIVE :
    
    "The"     → 0.05  [faible]
    "film"    → 0.10  [faible]
    "is"      → 0.08  [faible]
    "good"    → 0.70  [TRÈS ÉLEVÉ] ✓
    [SEP]     → 0.07  [faible]

Et conclut naïvement :

    « Le modèle regarde le mot "good", donc c'est ce mot qui explique la prédiction POSITIVE. »

Pourquoi c'est Trompeur
~~~~~~~~~~~~~~~~~~~~~~~~

Cette interprétation confond **observation** avec **causalité**.

Les poids d'attention élevés ne garantissent **pas** que le token influe réellement sur la décision. 

Les raisons incluent :

1. **Biais syntaxique**
   
   L'attention peut se concentrer sur des tokens importants syntaxiquement (verbes, noms) sans lien réel avec la décision de classification.

2. **Rôle contextuel**
   
   Un token peut être important pour construire la représentation latente du modèle sans pour autant influencer la classification finale.

3. **Dépendance positionnelle**
   
   Les positions du début ou fin de phrase reçoivent parfois plus d'attention indépendamment de leur contenu sémantique.

4. **Bruit d'optimisation**
   
   Pendant l'entraînement, les poids d'attention peuvent se stabiliser sur des patterns non causaux, résultant d'artefacts numériques.

Illustration avec un Exemple Problématique
===========================================

Considérez deux phrases :

.. code-block:: text

    Phrase A: "This movie is NOT good"
    Phrase B: "This movie is good"

**Prédiction du modèle** : Phrase A → NEGATIVE, Phrase B → POSITIVE (prédictions correctes)

**Attention observée** :

.. code-block:: text

    Phrase A:
    "This"  → 0.12
    "movie" → 0.15
    "is"    → 0.10
    "NOT"   → 0.08  ← PROBLÈME ! Poids faible
    "good"  → 0.55  ← Attention élevée pour "good"
    
    Phrase B:
    "This"  → 0.12
    "movie" → 0.15
    "is"    → 0.10
    "good"  → 0.56  ← Poids similaire !

**Conclusion** :

Le mot "NOT" devrait logiquement être **crucial** pour inverser le sentiment de "good" en sentiment négatif. Pourtant, l'attention ne lui donne pas de poids correspondant. C'est une signature claire d'un décalage entre attention et causalité réelle.

Pourquoi l'Attention Peut Échouer
==================================

Facteurs d'Erreur
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Facteur
     - Mécanisme
     - Conséquence
   * - **Multi-têtes**
     - Différentes têtes d'attention peuvent capturer des patterns contradictoires
     - Agrégation arbitraire masque les véritables causas
   * - **Biais positionnel**
     - L'attention privilégie certaines positions (début, fin) indépendamment du contenu
     - Faux positifs pour les tokens positionnés favorablement
   * - **Rôle distributionnel**
     - Un token important pour la syntaxe peut ne pas influencer la classification
     - Confusion entre importance structurelle et prédictive
   * - **Découplage**
     - Modifier les poids d'attention ne change pas la prédiction (de manière prévisible)
     - Poids d'attention ≠ réellement causal
   * - **Non-spécificité de la tâche**
     - L'attention est globale, pas spécifiquement orientée vers la tâche de classification
     - Bruit non pertinent pour la décision
   * - **Instabilité numérique**
     - Softmax rend difficile la distinction entre poids importants et moins importants
     - Amplification artificielle des petites différences

Comparison : Attention vs Explication Réelle
============================================

Analogie Humaine
~~~~~~~~~~~~~~~~

Imaginez demander à quelqu'un :

    « Pourquoi tu crois que ce film est bon ? »

**Réponse par "attention"** (ce qu'il regarde) :

    « Je regardais surtout l'action et les effets spéciaux. »
    
    (Mais cela ne dit pas si ces éléments ont **réellement** influencé son opinion)

**Réponse par "explication causale"** (ce qui cause vraiment) :

    « La raison principale, c'est la qualité du scénario, suivi par les acteurs. »
    
    (Cela révèle les véritables leviers de la décision)

Les deux ne sont **pas équivalentes** !


Langage Technique
~~~~~~~~~~~~~~~~~~

Points-clés :

- **Nature** : l'attention indique la consultation d'autres tokens, alors que l'explication causale décrit l'influence réelle sur la prédiction.
- **Fiabilité** : l'attention peut être contextuelle et incertaine ; l'explication causale nécessite une validation empirique.
- **Manipulation** : modifier des poids d'attention n'implique pas nécessairement un changement de prédiction.
- **Intérprétabilité** : l'attention est visuellement intuitive, l'explication causale est plus difficile à extraire mais plus informative.
- **Exemple** : attention → "le modèle regarde ce mot" ; causalité → "ce mot change la décision"

La Nécessité d'une Validation Empirique
========================================

Face à cette ambiguïté, une seule solution : **tester empiriquement** !

Approche
~~~~~~~~

1. **Extraire** les poids d'attention du modèle
2. **Comparer** avec des méthodes d'explication établies (LIME, SHAP)
3. **Calculer** une corrélation statistique
4. **Tirer** des conclusions sur la fiabilité de l'attention

Si :

.. math::
   
   	ext{Corrélation(Attention, LIME)} \approx 1 \quad \Rightarrow \quad \text{Attention est fiable}
   
   	ext{Corrélation(Attention, LIME)} \approx 0 \quad \Rightarrow \quad \text{Attention n'explique rien}

Roadmap de l'Étude
==================

Pour tester ces hypothèses, nous suivons cette progression :

1. **Section 3** : Formalisation mathématique des concepts clés
2. **Section 4** : Code et implémentation pratique
3. **Section 5** : Expériences et résultats empiriques
4. **Section 6** : Analyse critique et recommandations
