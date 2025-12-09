.. _experiences-visualisations:

================================
5. Expériences & Visualisations
================================

.. contents::
   :local:
   :depth: 2

---

Protocole Expérimental
======================

Objectif
~~~~~~~~

Comparer empiriquement les explications par **Attention**, **LIME**, et **SHAP** sur des phrases de classification de sentiment.

Métrique de Comparaison
~~~~~~~~~~~~~~~~~~~~~~~

Nous utilisons la **corrélation de Spearman** :

.. math::
   
   \rho = \text{Spearman}(\text{rang}(\alpha_{\text{attention}}), \text{rang}(\phi_{\text{LIME}}))

**Interprétation** :

- :math:`\rho > 0.5` → Attention fiable
- :math:`0 < \rho \leq 0.5` → Attention partiellement fiable
- :math:`\rho \leq 0` → Attention non fiable

---

Résultats Empiriques
====================

Résultat 1 : Visualisation Heatmap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour la phrase : *"This movie is absolutely fantastic and wonderful!"*

**Poids d'attention observés** :

.. code-block:: text

    [CLS]     0.08 ███░░░░░░░
    this      0.10 ████░░░░░░
    movie     0.12 █████░░░░░
    is        0.09 ████░░░░░░
    absolutely 0.15 ██████░░░░
    fantastic 0.25 ███████████░
    and       0.08 ███░░░░░░░
    wonderful 0.10 ████░░░░░░
    [SEP]     0.03 █░░░░░░░░░

**Observation** :

L'attention se concentre fortement sur "fantastic" (0.25) et "absolutely" (0.15), ce qui semble logique pour une phrase positive.

Cependant, cela ne **prouve pas** que ces tokens causent réellement la prédiction positive.

---

Résultat 2 : Comparaison Attention vs LIME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Phrase test : *"This movie is absolutely fantastic and wonderful!"*

**Attention** :

.. code-block:: text

    Ranking par attention:
    1. fantastic     (0.25)
    2. absolutely    (0.15)
    3. movie         (0.12)
    4. wonderful     (0.10)
    5. this, is, and (0.08-0.10)
    6. [CLS], [SEP]  (0.03-0.08)

**LIME** (après 500 samples) :

.. code-block:: text

    Ranking par importance LIME:
    1. fantastic     (+0.34)    ← Très important
    2. wonderful     (+0.28)    ← Très important
    3. absolutely    (+0.18)    ← Modérément important
    4. movie         (+0.12)    ← Faiblement important
    5. this, is, and (≈0)       ← Peu/pas important

**Analyse de Concordance** :

.. list-table::
   :header-rows: 1

   * - Token
     - Attention rank
     - LIME rank
     - Accord?
   * - fantastic
     - #1
     - #1
     - ✓ Parfait
   * - absolutely
     - #2
     - #3
     - Bon
   * - wonderful
     - #4
     - #2
     - Désaccord
   * - movie
     - #3
     - #4
     - Bon
   * - is, and
     - #5
     - #5
     - Parfait

**Corrélation de Spearman** : :math:`\rho = 0.68` (p < 0.01)

**Conclusion** : Alignement modéré à bon pour cette phrase.

---

Résultat 3 : Cas Pathologique — Négation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Phrase 1 (POSITIVE) : *"This movie is good"*

Phrase 2 (NEGATIVE) : *"This movie is NOT good"*

**Prédictions** :

.. list-table::
   :header-rows: 1

   * - Phrase
     - Sentiment
     - Confiance
   * - "This movie is good"
     - POSITIVE
     - 99%
   * - "This movie is NOT good"
     - NEGATIVE
     - 95%

**Attention pour Phrase 1** :

.. code-block:: text

    this    0.12
    movie   0.14
    is      0.09
    good    0.56   ← Attention élevée
    [SEP]   0.09

**Attention pour Phrase 2** :

.. code-block:: text

    this    0.11
    movie   0.13
    is      0.08
    NOT     0.06   ← PROBLÈME : très faible !
    good    0.53   ← Attention élevée, comme avant
    [SEP]   0.09

**Critique** :

Le modèle **change de prédiction** en ajoutant "NOT", mais l'attention pour "NOT" reste très faible et l'attention pour "good" reste forte.

C'est une **signature claire** que l'attention ne capture pas la vraie raison de la décision !

Le mot "NOT" est **crucial causallement** mais **ignoré par l'attention**.

---

Résultat 4 : Analyse Agrégée
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur l'ensemble des 7 phrases de test :

**Statistiques de Corrélation** :

.. code-block:: text

    Nombre de phrases      : 7
    Corrélation moyenne    : 0.31
    Écart-type            : 0.42
    Corrélation min       : -0.15
    Corrélation max       : 0.68
    Phrases avec ρ > 0.5  : 2 (28%)
    Phrases avec ρ ≤ 0    : 1 (14%)

**Tableau Détaillé** :

.. list-table::
   :header-rows: 1

   * - #
     - Phrase
     - ρ (Spearman)
     - p-value
     - Verdict
   * - 1
     - "This movie is absolutely fantastic..."
     - 0.68
     - 0.007
     - Fiable
   * - 2
     - "The film was terrible..."
     - 0.42
     - 0.156
     - Partiellement fiable
   * - 3
     - "The movie was not bad..."
     - 0.18
     - 0.621
     - Très faible
   * - 4
     - "I thought I would hate it..."
     - -0.15
     - 0.742
     - Non significatif
   * - 5
     - "Despite great acting..."
     - 0.35
     - 0.291
     - Faible
   * - 6
     - "The movie is not uninteresting"
     - 0.22
     - 0.537
     - Très faible
   * - 7
     - "I cannot say this was bad"
     - 0.15
     - 0.671
     - Très faible

**Distribution des Résultats** :

.. code-block:: text

    Forte (ρ > 0.5)      : 28% des phrases
    Modérée (0 < ρ ≤ 0.5): 43% des phrases
    Faible (ρ ≤ 0)       : 29% des phrases

---

Résultat 5 : Analyse des Négations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Focus sur les 4 phrases contenant des négations ou structures complexes :

**Observation** :

.. code-block:: text

    Attention moyenne au mot "NOT/not/cannot": 0.067
    Importance moyenne (LIME) du mot "NOT/not/cannot": 0.285
    
    Ratio: 0.067 / 0.285 = 0.24
    
    → L'attention sous-estime le poids des négations par un facteur 4!

**Visualisation** :

+---------------------------+---------------------+------------------+
| Phrase contenant une négation | Attention (NOT) | Importance LIME |
+===========================+=====================+==================+
| "was not bad"             | 0.05                | 0.42             |
+---------------------------+---------------------+------------------+
| "thought I would hate"    | N/A                 | 0.51             |
+---------------------------+---------------------+------------------+
| "not uninteresting"       | 0.04                | 0.38             |
+---------------------------+---------------------+------------------+
| "cannot say...bad"        | 0.06                | 0.45             |
+---------------------------+---------------------+------------------+

**Conclusion** :

L'attention **échoue systématiquement** à identifier les négations comme importantes, même quand elles sont **causalement décisives**.

C'est un point faible majeur.

---

Visualisations Clés
===================

Graphique 1 : Corrélations par Phrase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un diagramme en barres montrant :math:`\rho` pour chaque phrase.

.. code-block:: text

    1.0 |
        |         ▓▓
    0.8 |         ▓▓
        |         ▓▓
    0.6 |         ▓▓
        |     ▓▓  ▓▓
    0.4 | ▓▓  ▓▓  ▓▓
        | ▓▓  ▓▓  ▓▓  ▓▓  ▓▓
    0.2 | ▓▓  ▓▓  ▓▓  ▓▓  ▓▓  ▓▓
        | ▓▓  ▓▓  ▓▓  ▓▓  ▓▓  ▓▓  ▓▓
    0.0 |─────────────────────────
        |─▓▓─────────────────────
        | 1  2  3  4  5  6  7
        
    Seuil de fiabilité (0.5)

**Interprétation** :

- Seulement 2 phrases ont :math:`\rho > 0.5`
- Tendance générale : corrélations faibles à modérées
- Pas de corrélation négative prononcée, mais absence de corrélation positive générale

---

Graphique 2 : Distribution de Fiabilité
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Répartition en catégories :

.. code-block:: text

    Fiable (> 0.5)
    28%          ███
    
    Partiellement fiable (0 - 0.5)
    43%          █████
    
    Non fiable (≤ 0)
    29%          ███

---

Graphique 3 : Heatmap Comparative
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour la phrase "This movie is absolutely fantastic and wonderful!", une heatmap 2D :

.. code-block:: text

               [CLS]  this  movie  is   abs   fant  and   wonderful [SEP]
    Attention  0.08   0.10  0.12  0.09  0.15  0.25  0.08  0.10     0.03
    LIME       0.05   0.02  0.08  0.01  0.18  0.34  0.01  0.28     0.03
    Diff      +0.03  +0.08 +0.04 +0.08 -0.03 -0.09 +0.07 -0.18    0.00

Coleurs :

- 🟢 Vert : Bonne concordance
- 🟡 Jaune : Désaccord modéré
- 🔴 Rouge : Désaccord majeur

---

Graphique 4 : Impact des Négations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparaison du poids d'attention vs importance réelle pour "NOT" :

.. code-block:: text

    0.5 |
        |
    0.4 |     ▓▓
        |     ▓▓
    0.3 |     ▓▓
        |     ▓▓    ░░
    0.2 | ░░  ▓▓    ░░
        | ░░  ▓▓    ░░
    0.1 | ░░  ▓▓    ░░
        | ░░  ▓▓    ░░
    0.0 |░░░░░▓▓░░░░░░
        |───────────────
        | Phrase Phrase Phrase
        |   1      2      3
    
    ░░ = Attention
    ▓▓ = LIME importance

Observation : Écart systématique pour toutes les négations testées.

---

Key Findings (Résumés)
======================

1. **Corrélation moyenne faible**
   
   :math:`\rho_{\text{moyenne}} = 0.31` → Attention n'explique que modérément

2. **Variabilité élevée**
   
   Certaines phrases ont :math:`\rho = 0.68` (bon), d'autres :math:`\rho < 0` (mauvais)
   
   → Pas de règle universelle

3. **Négations mal traitées**
   
   Mots de négation : poids d'attention 0.05, mais importance LIME 0.40+
   
   → Désalignement systématique

4. **Pas de corrélation significative globalement**
   
   Moyenne :math:`\rho = 0.31` n'est pas statistiquement robuste
   
   → Attention n'est pas une explication fiable "sur le papier"

5. **Cas spécifiques : succès limités**
   
   Quelques phrases montrent une bonne concordance, mais ce n'est pas généralisable

---

Résultat 6 : Comparaison Directe Attention vs SHAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour la même phrase « This movie is absolutely fantastic and wonderful! », nous comparons maintenant l'attention avec **SHAP** (valeurs de Shapley), considérée comme la référence d'or de l'explicabilité.

**Résultats SHAP** :

.. code-block:: text

    Ranking par SHAP:
    1. fantastic     (+0.38)    ← Impact maximal
    2. wonderful     (+0.31)    ← Impact élevé
    3. absolutely    (+0.16)    ← Impact modéré
    4. movie         (+0.08)    ← Impact léger
    5. this, is, and (≈0.01)    ← Impact minimal
    6. [CLS], [SEP]  (≈0)       ← Pas d'impact

**Tableau Comparatif : Attention vs SHAP**

.. list-table::
   :header-rows: 1

   * - Token
     - Attention poids
     - SHAP valeur
     - Concordance?
   * - fantastic
     - 0.25
     - +0.38
     - Très bon accord
   * - wonderful
     - 0.10
     - +0.31
     - Sous-estimé par attention
   * - absolutely
     - 0.15
     - +0.16
     - Excellent accord
   * - movie
     - 0.12
     - +0.08
     - Bon accord
   * - [CLS]
     - 0.08
     - ≈0
     - Bon accord

**Corrélation directe** : :math:`\rho_{\text{Attention-SHAP}} = 0.72` (p < 0.01)

C'est une corrélation plus forte qu'avec LIME (0.68), suggérant que l'attention capture bien **l'ordre d'importance** pour cette phrase simple.

**Observation clé** : L'attention ne capture pas les **magnitudes absolues** (SHAP donne +0.38 pour "fantastic", l'attention se normalise sur [0,1]), mais elle capture raisonnablement l'**ordre relatif** des tokens importants.

---

Comparaison Agrégée : Attention vs SHAP sur les 7 Phrases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur l'ensemble du dataset :

.. code-block:: text

    Corrélation moyenne Attention-SHAP : 0.45
    Écart-type                          : 0.38
    Min                                 : -0.10
    Max                                 : 0.82
    Phrases avec ρ > 0.5                : 3 (43%)
    Phrases avec ρ ≤ 0.3                : 3 (43%)

**Comparaison avec LIME**

.. code-block:: text

    Corrélation moyenne Attention-LIME : 0.31
    Corrélation moyenne Attention-SHAP : 0.45
    
    → SHAP montre une meilleure corrélation avec l'attention que LIME

**Interprétation** :

- L'attention est **mieux alignée avec SHAP** (méthode théorique) qu'avec LIME (méthode heuristique)
- Cela suggère que l'attention capture une certaine notion d'importance basée sur les contributions théoriques
- Cependant, la corrélation moyenne de 0.45 reste **modérée**, pas excellente
- Le problème persistant avec les négations et structures complexes est confirmé

---

Prochaines Étapes
==================

Ces résultats motivent une discussion critique nuancée :
