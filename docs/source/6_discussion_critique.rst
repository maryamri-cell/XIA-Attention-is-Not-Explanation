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

1. **Rapidité de calcul**
   
   L'attention est déjà calculée lors de l'inférence et n'entraîne pas de surcoût important.
   
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
   
   **Avantage** : Ordre de grandeur bien plus rapide.

2. **Interprétabilité intuitive**
   
   Les heatmaps d'attention sont faciles à visualiser et à comprendre.
   
   Un utilisateur non technique peut repérer rapidement les tokens "regardés" par le modèle.
   
   Comparaison :
   
   - **Attention** : "Token A a 0.70 d'attention" → Clair
   - **LIME** : "Token A a un coefficient -0.23 dans la régression locale" → Moins intuitif
   - **SHAP** : "Token A a une valeur Shapley de 0.15" → Plus abstrait

3. **Granularité détaillée**
   
   L'attention produit des scores pour :
   
   - Chaque couche (6 niveaux)
   - Chaque tête (12 par couche)
   - Chaque position (séquence entière)
   
   Il est possible d'analyser les motifs à chaque niveau.

4. **Insights structurels**
   
   L'attention révèle des aspects de l'organisation interne du modèle :
   
   - Couches basses : relations locales entre tokens (syntaxe)
   - Couches hautes : intégration du sens global (sémantique)
   
   Cela fournit une fenêtre sur les représentations internes.

5. **Absence de perturbation**
   
   Contrairement à LIME (qui perturbe l'entrée), l'attention n'interfère pas avec le modèle.
   
   → Approche non intrusive par rapport au modèle.

---

Limitations et Risques de l'Attention
=====================================

Les critiques sont plus graves.

1. **Non-causalité fondamentale**
   
   **Problème** : l'attention montre ce que le modèle observe, pas nécessairement ce qui cause la décision.
   
   **Analogie** :
   
       On demande : « Pourquoi pensez-vous que c'est dangereux ? »
       
       Réponse (par observation) : « Je regardais la couleur rouge. »
       
       Explication causale : « La couleur rouge indique un risque biologique. »
   
   En résumé : l'attention n'explique pas automatiquement le « pourquoi ».

2. **Ambiguïté multi-têtes**
   
   Chaque tête produit une distribution d'attention différente.
   
   **Exemple** :
   
   .. code-block:: text
   
       Tête 1: "good" (0.80)
       Tête 2: "movie" (0.70)
       Tête 3: "is" (0.65)
       Tête 4: "!" (0.82)
       ...
   
   **Question** : laquelle utiliser ? Comment les agréger ?
   
   Pas de consensus standard → choix arbitraires.

3. **Biais positionnel**
   
   Les positions initiales et finales reçoivent souvent plus d'attention, indépendamment du contenu.
   
   **Test simple** :
   
   .. code-block:: text
   
       Phrase 1: "film good XYZABC" (mot gibberish à la fin)
       Phrase 2: "film good excellent" (bon mot à la fin)
       
       → L'attention à la fin peut être similaire.
   
   Il s'agit d'un biais de position, et non d'une mesure d'importance sémantique.

4. **Manipulabilité et découplage**
   
   **Expérience de Jain & Wallace (2019)** :
   
   Permuter aléatoirement les poids d'attention d'une phrase peut ne pas changer la prédiction.
   
   .. math::
       
       \text{Si} \quad \alpha' \neq \alpha \quad \text{mais} \quad f(x, \alpha') = f(x, \alpha)
       
       \text{Alors l'attention n'est pas nécessairement causale}
   
   **Implication** : les poids d'attention peuvent être découplés de la décision finale.

5. **Manque de spécificité pour la tâche**
   
   L'attention est généralement entraînée globalement pour la tâche, et non spécifiquement pour chaque classe.
   
   **Exemple** : pour la classification de sentiments
   
   .. code-block:: text
   
       Le même mot "surprising" peut signifier POSITIF ("surprisingly good")
       ou NÉGATIF ("surprisingly bad").
       
       L'attention ne capture pas toujours cette dépendance contextuelle.

6. **Instabilité et sensibilité numériques**
   
   La softmax amplifie les petites différences :
   
   .. math::
       
       \text{score}_1 = 10.0, \quad \text{score}_2 = 9.9 \quad \Rightarrow \quad \alpha_1 = 0.55, \alpha_2 = 0.45
   
   Une petite perturbation (0.1) peut changer légèrement les poids relatifs.
   
   → Risque d'instabilité numérique.

7. **Agrégation arbitraire**
   
   Pour chaque couche et tête, on obtient une distribution d'attention distincte.
   
   Comment les combiner ?
   
   - Moyenne, max ou produit ?
   - Moyens de pondération ? Sur quelles bases ?
   
   Chaque stratégie d'agrégation produit des résultats différents.

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

- Si **rapidité** → Attention
- Si **exactitude** → SHAP
- Pour **production responsable** → LIME + SHAP

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

**Corrélation** : :math:`\rho = 0.68`

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

- Pour A : "good" = 0.56
- Pour B : "good" = 0.53, "NOT" = 0.06

L'attention **ne détecte pas** que "NOT" change tout.

**LIME** :

- Pour A : "good" = +0.34
- Pour B : "good" = -0.35, "NOT" = -0.42

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

1. **Ne pas utiliser l'attention seule comme explication**
   
   Utilisez-la comme outil exploratoire pour déboguer et comprendre le modèle.

2. **Toujours valider avec LIME ou SHAP**
   
   Avant de publier une explication, validez cette explication avec une méthode indépendante.

3. **Transparence**
   
   Si vous utilisez l'attention, informez clairement l'utilisateur :
   
       "Ces heatmaps montrent où le modèle regarde, pas nécessairement pourquoi."

4. **Trier les cas**
   
   - Phrases simples → l'attention peut suffire (avec réserves)
   - Phrases complexes, négations → utiliser LIME/SHAP
   - Production responsable → systématiquement LIME/SHAP

5. **Multi-méthodes**
   
   Combiner :
   
   - Attention (rapide, intuitive)
   - LIME (locale, empirique)
   - SHAP (théorique, globale)
   
   Si les trois méthodes concordent → confiance accrue.

Pour les Chercheurs
~~~~~~~~~~~~~~~~~~~

1. **Développer des métriques de fiabilité**
   
   Créer des scores quantitatifs pour prédire quand l'attention est digne de confiance.

2. **Attention améliorée**
   
   - Attention orientée vers la tâche (task-aware attention)
   - Attention avec contraintes de causalité
   - Attention robuste aux adversaires

3. **Tester sur plus de tâches**
   
   NLP, vision et autres domaines.

4. **Comprendre les failure modes** 🐛
   
   Pourquoi l'attention échoue-t-elle sur les négations ?
   
   Est-ce l'architecture ? Le données ? L'optimisation ?

---

Vue Globale : Supporter Jain & Wallace vs Wiegreffe & Pinter
=============================================================

**Jain & Wallace (2019)** : "Attention is Not Explanation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notre étude soutient partiellement cette critique.

✓ **Points validés** :

- Corrélation moyenne modérée-faible (0.31) avec LIME
- Négations mal traitées par l'attention
- Découplage observé entre attention et décision

**Points nuancés** :

- Certains cas présentent une bonne corrélation (ρ = 0.68)
- L'attention reste utile pour exploration, non pour explication finale
- Distinction importante : « pas d'explication causale » n'égale pas « complètement inutile »

---

**Wiegreffe & Pinter (2019)** : "Attention is Not Not Explanation"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notre étude soutient partiellement cette réponse.

✓ **Points soutenant cette critique** :

- Les tests trop stricts de Jain ne reflètent pas tous les usages
- L'attention peut aider en contexte (exploration, débugage)
- Distinction entre explication et explication fidèle importante

**Points de réserve** :

- L'attention seule ne suffit pas pour une explication fiable
- Peut être trompeuse si utilisée sans discernement
- Requiert validation empirique (LIME/SHAP)

---

Synthèse : Position Nuancée
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    **Notre conclusion** :
    
    L'attention n'est ni une explication complète, ni complètement inutile.
    
    C'est un outil exploratoire puissant qui :
    
    - Offre des insights rapides et visuellement intuitifs
    - Ne garantit pas la causalité
    - Peut être trompeuse si mal interprétée
    - Reste utile quand validée par d'autres méthodes

---

Prochaines Étapes
==================

Nous concluons avec une synthèse et des recommandations finales.

Continuez vers la conclusion : :ref:`conclusion-points-cles`

---
