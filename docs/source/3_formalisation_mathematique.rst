.. _formalisation-mathematique:

=============================
3. Formalisation Mathématique
=============================

.. contents::
   :local:
   :depth: 2

---

Fondements Théoriques
======================

Cette section formalise les concepts du mécanisme d'attention et définit les métriques de validation.

---

Équation 1 : Scaled Dot-Product Attention
==========================================

La formulation standard du mécanisme d'attention dans les Transformers est :

.. math::
   
   \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V

Notation et Signification
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Symbole
     - Signification
     - Dimension
   * - :math:`Q`
     - **Query matrix** — Représentation de ce que chaque token « cherche »
     - :math:`[n \times d_k]`
   * - :math:`K`
     - **Key matrix** — Représentation de ce que chaque token « offre »
     - :math:`[n \times d_k]`
   * - :math:`V`
     - **Value matrix** — Information à extraire et propager
     - :math:`[n \times d_v]`
   * - :math:`d_k`
     - Dimension des vecteurs clés (généralement 64 pour DistilBERT)
     - Scalaire
   * - :math:`n`
     - Longueur de la séquence (nombre de tokens)
     - Scalaire
   * - :math:`\alpha`
     - Matrice des poids d'attention (sortie)
     - :math:`[n \times n]`

Étapes du Calcul
~~~~~~~~~~~~~~~~

**Étape 1 : Calcul des scores de compatibilité**

.. math::
   
   S = \frac{QK^T}{\sqrt{d_k}}

Le score :math:`S_{ij}` mesure combien le token :math:`i` devrait "regarder" le token :math:`j`.

Le facteur :math:`1/\sqrt{d_k}` normalise pour éviter la saturation de la softmax.

**Étape 2 : Normalisation par softmax**

.. math::
   
   \alpha = \text{softmax}(S) \quad \Rightarrow \quad \alpha_{ij} = \frac{e^{S_{ij}}}{\sum_{k} e^{S_{ik}}}

Propriétés résultantes :

- :math:`\alpha_{ij} \in [0, 1]` — Chaque poids est une probabilité
- :math:`\sum_j \alpha_{ij} = 1` — Distribution normalisée pour chaque requête
- Interprétable comme une distribution de probabilité

**Étape 3 : Agrégation pondérée**

.. math::
   
   \text{Output}_i = \sum_j \alpha_{ij} \cdot V_j

Chaque token reçoit une combinaison pondérée des représentations de valeur.

---

Équation 2 : Calcul Détaillé des Poids d'Attention
===================================================

Pour chaque paire de tokens :math:`(i, j)`, le poids d'attention est :

.. math::
   
   \alpha_{ij} = \frac{\exp\left(\frac{q_i \cdot k_j}{\sqrt{d_k}}\right)}{\sum_{l=1}^{n} \exp\left(\frac{q_i \cdot k_l}{\sqrt{d_k}}\right)}

où :

- :math:`q_i` = vecteur query du token :math:`i`
- :math:`k_j` = vecteur key du token :math:`j`
- :math:`q_i \cdot k_j` = produit scalaire (mesure de similarité)

**Propriétés numériques** :

.. math::
   
   0 < \alpha_{ij} < 1 \quad \text{et} \quad \sum_{j=1}^{n} \alpha_{ij} = 1

**Cas particuliers** :

- Si :math:`q_i \cdot k_j \gg q_i \cdot k_l`, alors :math:`\alpha_{ij} \to 1`
- Si tous les scores sont égaux, :math:`\alpha_{ij} = 1/n` (distribution uniforme)

---

Équation 3 : Multi-Head Attention
==================================

En pratique, les Transformers ne calculent pas une seule tête d'attention, mais plusieurs en parallèle.

Pour :math:`h` têtes d'attention :

.. math::
   
   \text{MultiHead}(Q, K, V) = \text{Concat}(head_1, ..., head_h) W^O

où chaque tête est :

.. math::
   
   head_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)

- :math:`W_i^Q, W_i^K, W_i^V` = projections linéaires spécifiques à la tête :math:`i`
- :math:`W^O` = matrice de projection finale

**Implication pour notre étude** :

Nous devons **agréger** les poids d'attention de :math:`h` têtes différentes :

.. math::
   
   \alpha_{\text{agrégé}} = \frac{1}{h} \sum_{i=1}^{h} \alpha^{(i)}

Cette agrégation **lisse** les poids individuels et peut perdre de la précision.

---

Équation 4 : Agrégation Multi-Couches
======================================

Un modèle DistilBERT a 6 couches d'attention empilées.

Les poids d'attention varient d'une couche à l'autre.

Pour obtenir une vue globale, on agrège :

.. math::
   
   \alpha_{\text{final}} = \frac{1}{L} \sum_{l=1}^{L} \alpha^{(l)}

où :math:`L = 6` (nombre de couches).

**Défi** : Quelle agrégation utiliser ? Moyenne ? Produit ? Maximum ?

Dans cette étude : **moyenne arithmétique** (choix standard et transparent).

---

Équation 5 : Métriques d'Importance Alternatives
=================================================

Pour comparer avec l'attention, nous utilisons deux méthodes établies.

LIME : Local Interpretable Model-agnostic Explanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LIME estime l'importance de chaque feature en perturbant l'entrée localement.

**Formulation** :

.. math::
   
   \text{importance}_{\text{LIME}} = \arg\min_g \sum_{i=1}^{m} \left[ f(x_i) - g(z_i) \right]^2 \pi(x_i)

où :

- :math:`f` = modèle original
- :math:`g` = modèle linéaire local
- :math:`z_i` = perturbations de l'entrée
- :math:`\pi(x_i)` = poids de proximité
- :math:`m` = nombre d'échantillons

**En pratique** : Les coefficients de régression :math:`\beta_j` estimés reflètent l'importance de chaque token.

SHAP : SHapley Additive exPlanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SHAP calcule les valeurs de Shapley à partir de la théorie des jeux coopératifs.

**Formulation** :

.. math::
   
   \text{SHAP}_j = \sum_{S \subseteq F \setminus \{j\}} \frac{|S|!(|F|-|S|-1)!}{|F|!} \left[ f(S \cup \{j\}) - f(S) \right]

où :

- :math:`F` = ensemble de toutes les features
- :math:`S` = sous-ensemble de features
- :math:`f(S)` = prédiction du modèle avec features dans :math:`S`

**Propriétés** :

- Satisfait l'efficacité (somme des contributions = prédiction)
- Satisfait la symétrie (features symétriques reçoivent des valeurs identiques)
- Coûteux en calcul (:math:`2^{|F|}` combinaisons)

---

Équation 6 : Corrélation de Spearman
=====================================

Pour quantifier l'alignement entre attention et importance réelle :

.. math::
   
   \rho_{\text{Spearman}} = 1 - \frac{6 \sum_i (R_i - R'_i)^2}{n(n^2-1)}

où :

- :math:`R_i` = rang de la i-ème feature dans l'ordre d'attention
- :math:`R'_i` = rang de la i-ème feature dans l'ordre LIME/SHAP
- :math:`n` = nombre de features

**Interprétation** :

.. math::
   
   \rho \in [-1, 1]

.. list-table::
   :header-rows: 1

   * - Valeur de :math:`\rho`
     - Interprétation
   * - :math:`\rho \approx 1`
     - Forte corrélation positive (attention = explication fiable)
   * - :math:`\rho \approx 0.5`
     - Corrélation modérée (résultats mitigés)
   * - :math:`\rho \approx 0`
     - Absence de corrélation (attention indépendante)
   * - :math:`\rho < 0`
     - Corrélation négative (attention trompeuse)

**Significance** : Test statistique pour vérifier si :math:`\rho` est significatif via p-valeur

.. math::
   
   p\text{-value} = P(|\rho| \geq \rho_{\text{obs}})

Seuil : :math:`p < 0.05` → corrélation significative.

---

Équation 7 : Hypothèses Testables
==================================

Hypothèse nulle (:math:`H_0`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::
   
   H_0 : \rho(\alpha_{\text{attention}}, \phi_{\text{importance réelle}}) = 0

L'attention et l'importance réelle sont **indépendantes**.

Hypothèse alternative (:math:`H_1`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::
   
   H_1 : \rho(\alpha_{\text{attention}}, \phi_{\text{importance réelle}}) \neq 0

L'attention et l'importance réelle sont **corrélées**.

**Plan de test** :

1. Calculer :math:`\rho` sur nos données
2. Comparer la p-valeur au seuil :math:`\alpha = 0.05`
3. Accepter ou rejeter :math:`H_0`

---

Équation 8 : Matrice de Confusion pour Cas Pathologiques
=========================================================

Pour les cas comme les négations, on utilise une matrice de confusion :

.. math::
   
   \begin{bmatrix}
   TP & FP \\
   FN & TN
   \end{bmatrix}

où :

- **TP** (True Positive) : Attention élevée + Impact réel élevé
- **FP** (False Positive) : Attention élevée + Impact réel faible ← Problème !
- **FN** (False Negative) : Attention faible + Impact réel élevé ← Problème !
- **TN** (True Negative) : Attention faible + Impact réel faible

**Métrique** :

.. math::
   
   \text{Précision} = \frac{TP}{TP + FP}
   
   \text{Rappel} = \frac{TP}{TP + FN}
   
   F_1 = 2 \cdot \frac{\text{Précision} \times \text{Rappel}}{\text{Précision} + \text{Rappel}}

Un :math:`F_1` élevé (~0.8+) indique que l'attention classe correctement les features importantes.

---

Prochaines Étapes
==================

Avec ces équations en tête, passons à l'implémentation pratique.

L'étape suivante explore le code reproductible et les détails techniques de l'exécution.
