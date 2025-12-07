.. _discussion-critique:

=======================
6. Discussion Critique
=======================

.. contents::
   :local:
   :depth: 2

---

Synthèse des Résultats
======================

Avant de critiquer, récapitulons nos résultats empiriques :

**Résultat Principal**

    Corrélation de Spearman moyenne entre attention et LIME : :math:`\rho = 0.31`
    
    Cela indique une faible corrélation global, insuffisante pour garantir la fiabilité de l'attention.

**Résultats Secondaires**

- Forte variabilité entre phrases (:math:`\rho \in [-0.15, 0.68]`)
- Dépendance claire du contexte (certaines structures marchent, d'autres non)
- Négations systématiquement sous-estimées par l'attention

---

Forces de l'Attention comme Explication
========================================

Bien que critique, l'attention a des avantages réels.

1. **Rapidité de Calcul** ⚡
   
   L'attention est déjà calculée lors de l'inférence → pas de surcoût.
   
   Comparaison :
   
   .. list-table::
      :header-rows: 1
      
      * - Méthode
        - Temps pour 1000 phrases
      * - Attention
        - ~1 seconde
      * - LIME
        - ~30 minutes (500 samples)
      * - SHAP
        - ~2 heures (combinaisons)
   
   **Avantage** : Ordre de magnitude plus rapide.

2. **Interprétabilité Intuitive** 🎨
   
   Les heatmaps d'attention sont faciles à visualiser et comprendre.
   
   Un utilisateur non-technique peut voir « le modèle regarde ce mot » sans calculs complexes.
   
   Comparaison :
   
   - **Attention** : "Token A a 0.70 d'attention" → Clair
   - **LIME** : "Token A a un coefficient -0.23 dans la régression locale" → Confus
   - **SHAP** : "Token A a une valeur Shapley de 0.15" → Abstrait

3. **Granularité Détaillée** 🔬
   
   L'attention produit des scores par :
   
   - Chaque couche (6 niveaux)
   - Chaque tête (12 par couche)
   - Chaque position (séquence entière)
   
   On peut analyser les patterns à chaque niveau.

4. **Insights Structurels** 🧠
   
   L'attention révèle comment le modèle organise l'information :
   
   - Couches basses : relationner tokens adjacents (syntaxe)
   - Couches hautes : capturer le sens global (sémantique)
   
   Cela donne une fenêtre sur les représentations internes.

5. **Absence de Perturbation** ✓
   
   Contrairement à LIME (qui perturbe l'entrée), l'attention n'interfère pas avec le modèle.
   
   → Plus proche de la véritable explication.

---

Limitations et Risques de l'Attention
=====================================

Les critiques sont plus graves.

1. **Non-Causalité Fondamentale** ⚠️
   
   **Problème** : L'attention montre ce que le modèle "observe", pas ce qui *cause* la décision.
   
   **Analogue humaine** :
   
       Vous demandez : « Pourquoi tu crois que c'est dangereux ? »
       
       Réponse (par "attention") : « Je regardais la couleur rouge. »
       
       Explication causale réelle : « La couleur rouge signale un risque biologique. »
   
   L'attention n'explique pas le "pourquoi".

2. **Ambiguïté Multi-Têtes** 🎭
   
   Chaque tête produit une distribution d'attention différente.
   
   **Exemple** :
   
   .. code-block:: text
   
       Tête 1: "good" (0.80)
       Tête 2: "movie" (0.70)
       Tête 3: "is" (0.65)
       Tête 4: "!" (0.82)
       ...
   
   **Question** : Laquelle prendre ? Comment agréger ?
   
   Pas de consensus standard → choix arbitraires.

3. **Biais Positionnel** 📍
   
   Les positions initiales et finales reçoivent souvent plus d'attention, indépendamment du contenu.
   
   **Test simple** :
   
   .. code-block:: text
   
       Phrase 1: "film good XYZABC" (mot gibberish à la fin)
       Phrase 2: "film good excellent" (bon mot à la fin)
       
       → L'attention à la fin peut être similaire !
   
   C'est un **biais de position**, pas d'importance sémantique.

4. **Manipulabilité et Découplage** 🎪
   
   **Expérience de Jain & Wallace (2019)** :
   
   Permuter aléatoirement les poids d'attention d'une phrase ne change pas la prédiction.
   
   .. math::
       
       \text{Si} \quad \alpha' \neq \alpha \quad \text{mais} \quad f(x, \alpha') = f(x, \alpha)
       
       \text{Alors l'attention n'est pas causale}
   
   **Implication** : Les poids d'attention sont **décuplés** de la décision réelle.

5. **Manque de Spécificité pour la Tâche** 🎯
   
   L'attention est entraînée globalement sur la tâche, pas spécifiquement pour chaque classe.
   
   **Exemple** : Pour la classification de sentiments
   
   .. code-block:: text
   
       Même mot "surprising" peut signifier POSITIF ("surprisingly good")
       ou NÉGATIF ("surprisingly bad")
       
       L'attention ne capture pas cette dépendance au contexte de classe.

6. **Instabilité et Sensibilité Numériques** 🔀
   
   La softmax amplifie les petites différences :
   
   .. math::
       
       \text{score}_1 = 10.0, \quad \text{score}_2 = 9.9 \quad \Rightarrow \quad \alpha_1 = 0.55, \alpha_2 = 0.45
   
   Une petite perturbation de 0.1 change le classement de 5%.
   
   → Instabilité numérique.

7. **Agrégation Arbitraire** 🔧
   
   Pour chaque couche et tête, on obtient une attention différente.
   
   Comment les combiner ?
   
   - Moyenne ? Max ? Produit ?
   - Poids par importance ? Basé sur quoi ?
   
   Chaque choix donne des résultats différents.

---

Comparaison Empirique : Attention vs LIME vs SHAP
==================================================

Tableau Comparatif Complet
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15, 12, 12, 12

   * - Critère
     - Attention
     - LIME
     - SHAP
   * - **Coût calcul**
     - Gratuit (inférence)
     - 30 min / 1000
     - 2 heures / 1000
   * - **Fidélité empirique**
     - Modérée (~0.3)
     - Bonne (~0.6)
     - Très bonne (~0.75)
   * - **Garantie théorique**
     - Aucune
     - Locale seulement
     - Fondée (Shapley)
   * - **Causalité**
     - Non
     - Approximative
     - Valeurs causales
   * - **Stabilité**
     - Variable
     - Stochastique
     - Déterministe
   * - **Interprétabilité**
     - Excellente
     - Bonne
     - Moyenne
   * - **Multi-classe**
     - Ambigu
     - Clair
     - Clair
   * - **Utilité pratique**
     - Exploration
     - Validation
     - Production

**Conclusions du Tableau** :

- Si **rapidité** → Attention ✓
- Si **exactitude** → SHAP ✓
- Pour **production responsable** → LIME + SHAP ✓

---

Cas Où l'Attention Fonctionne Bien
==================================

L'attention n'est pas inutile. Elle fonctionne dans certains cas.

Cas 1 : Phrases Simples avec Sentiments Explicites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    "This movie is absolutely fantastic and wonderful!"

Ici, l'attention se concentre sur les adjectifs positifs ("fantastic", "wonderful").

LIME confirme : ces adjectifs sont effectivement les plus importants.

**Corrélation** : :math:`\rho = 0.68` ✓

**Pourquoi ça marche** :

- Tokens importants sont syntaxiquement/sémantiquement explicites
- Pas de negation pour compliquer
- Structure linéaire simple

---

Cas 2 : Tâches Simples et Claires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

L'attention fonctionne mieux pour :

- Reconnaissance d'entités nommées (NER)
- Question-réponse (passage pertinent clair)
- Traduction (alignement token-to-token)

Mais échoue pour :

- Sentiment analysis (nécessite compréhension contextuelle)
- Inférence logique (sujet d'étude)
- Langues morphologiquement complexes

---

Cas Où l'Attention Échoue
==========================

Cas 1 : Négations
~~~~~~~~~~~~~~~~~

.. code-block:: text

    Phrase A: "This is good"           → POSITIF
    Phrase B: "This is not good"       → NÉGATIF

Différence clé : un seul mot ("NOT").

**Attention** :

- Pour A : "good" = 0.56 ✓
- Pour B : "good" = 0.53, "NOT" = 0.06 ✗

L'attention **ne détecte pas** que "NOT" change tout.

**LIME** :

- Pour A : "good" = +0.34
- Pour B : "good" = -0.35, "NOT" = -0.42 ✓

LIME capture la dépendance au contexte et la négation.

---

Cas 2 : Ambiguïtés Pragmatiques
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    "I thought I would hate it, but surprisingly I loved it."

Structure complexe :

- "hate" → tendance négative, mais negé par contexte
- "surprisingly" → inversion d'attente
- "loved" → sentiment réel positif

**Attention** :

Peut se concentrer sur "hate" ou "loved" selon la tête de l'attention.

Inconsistent et pas clairement causal.

**LIME** :

Identifie "loved" comme positif et "hate" comme contextuellement négatif (mais neutralisé).

---

Cas 3 : Double Négation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    "The movie is not uninteresting"

Double négation = approximativement positif.

**Attention** :

Poids faible pour "not" et "uninteresting" → Désacord avec la logique.

**LIME** :

Capture la double négation correctement (avec stochastique).

---

Recommandations Pratiques
==========================

Pour les Praticiens
~~~~~~~~~~~~~~~~~~~

1. **Ne pas utiliser l'attention seule comme explication** ❌
   
   Utilisez-la comme **outil exploratoire** pour déboguer et comprendre le modèle.

2. **Toujours valider avec LIME ou SHAP** ✓
   
   Avant de publier une explication, validez avec une méthode indépendante.

3. **Transparence** 🎯
   
   Si vous utilisez l'attention, dites clairement à l'utilisateur :
   
       "Ces heatmaps montrent où le modèle regarde, pas nécessairement pourquoi."

4. **Trier les cas** 📊
   
   - Phrases simples → Attention peut suffire (avec caveats)
   - Phrases complexes, négations → Utilisez LIME/SHAP
   - Production responsable → Always LIME/SHAP

5. **Multi-Méthodes** 🔄
   
   Croiser :
   
   - Attention (rapide, intuitive)
   - LIME (locale, empirique)
   - SHAP (théorique, globale)
   
   Si les trois concordent → confidence élevée.

Pour les Chercheurs
~~~~~~~~~~~~~~~~~~~

1. **Développer des métriques de fiabilité** 🔬
   
   Créer des scores quantitatifs pour quand l'attention est trustworthy.

2. **Attention améliorée** 🚀
   
   - Attention orientée vers la tâche (task-aware attention)
   - Attention avec contraintes de causalité
   - Attention robuste aux adversaires

3. **Tester sur plus de tâches** 🧪
   
   NLP (récente), Vision (important), Autres domaines.

4. **Comprendre les failure modes** 🐛
   
   Pourquoi l'attention échoue-t-elle sur les négations ?
   
   Est-ce l'architecture ? Le données ? L'optimisation ?

---

Vue Globale : Supporter Jain & Wallace vs Wiegreffe & Pinter
=============================================================

**Jain & Wallace (2019)** : "Attention is Not Explanation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notre étude soutient partiellement cette critique.

✓ **Points confirmés** :

- Corrélation moyenne faible (0.31) avec LIME
- Négations mal traitées
- Discovélage entre attention et décision

⚠ **Points à nuancer** :

- Certains cas marchent bien (ρ = 0.68)
- Attention utile pour exploration, pas pour explication finale
- Différence entre "pas d'explication causale" et "pas d'explication du tout"

---

**Wiegreffe & Pinter (2019)** : "Attention is Not Not Explanation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notre étude soutient partiellement cette réponse.

✓ **Points confirmés** :

- Les tests trop stricts de Jain ne reflètent pas tous les usages
- Attention peut aider en contexte (exploration, débugage)
- Distinction entre explication et explication fidèle importante

⚠ **Cependant** :

- L'attention seule **ne suffit pas** pour une explication fidèle
- Peut être tromperie si utilisée naïvement
- Requiert validation empirique (LIME/SHAP)

---

Synthèse : Position Nuancée
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    **Notre conclusion** : 
    
    L'attention n'est ni une explication complète, ni complètement inutile.
    
    C'est un **outil exploratoire puissant** qui :
    
    - ✓ Offre des insights rapides et visuellement intuitifs
    - ✗ Ne garantit pas la causalité
    - ⚠ Peut être trompeuse si mal interprétée
    - ✓ Reste utile quand validée par d'autres méthodes

---

Prochaines Étapes
==================

Nous concluons avec une synthèse et des recommendations finales.

.. button-ref:: 7_conclusion_points_cles
   :color: primary
   :outline:

   Vers la Conclusion →

---
