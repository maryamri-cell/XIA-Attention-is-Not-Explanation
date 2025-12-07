.. _glossaire:

==========
Glossaire
==========

.. contents::
   :local:
   :depth: 2

---

Termes Fondamentaux
====================

**Attention**
    Mécanisme dans les Transformers qui pondère l'importance relative de chaque token d'une séquence.
    Calculé via Query-Key-Value à travers la formule : Softmax(QK^T/√d_k) × V

**Transformer**
    Architecture de réseau de neurones basée uniquement sur des mécanismes d'attention.
    Introduit en 2017 par Vaswani et al., remplace les RNN/LSTM dans la plupart des applications NLP modernes.

**Token**
    Unité de texte après tokenization (mot, sous-mot, caractère selon la méthode).
    Exemple : "wonderful" → ["wonder", "##ful"] (2 tokens avec tokenizer BERT)

**Self-Attention**
    Attention où les Queries, Keys et Values proviennent de la même séquence.
    Permet à chaque token d'"regarder" tous les autres tokens.

**Cross-Attention**
    Attention où Queries proviennent d'une séquence et Keys/Values d'une autre.
    Utilisée en traduction (attending source language quand générant target).

---

Concepts XAI
============

**XAI (Explainable AI / Explicabilité de l'IA)**
    Domaine visant à rendre les décisions des modèles de machine learning compréhensibles aux humains.
    Critique pour les applications réglementées (médecine, justice, finance).

**LIME (Local Interpretable Model-agnostic Explanations)**
    Méthode XAI qui explique une prédiction en perturbant l'entrée localement et entraînant un modèle linéaire simple.
    Agnostique au modèle (fonctionne avec n'importe quel classifieur).

**SHAP (SHapley Additive exPlanations)**
    Méthode XAI basée sur les valeurs de Shapley de la théorie des jeux.
    Fournit des explications théoriquement fondées avec garanties mathématiques (efficacité, symétrie).

**Feature Importance**
    Mesure de l'importance relative de chaque feature (token, pixel, etc.) pour une prédiction donnée.
    Peut être calculée via gradients, perturbations, ou valeurs de Shapley.

**Explication Causale**
    Explication révélant les vraies causes d'une décision (intervention-based).
    Contraste avec "explication observationnelle" qui montre seulement la corrélation.

**Explication Fidèle**
    Explication qui correspond exactement aux mécanismes décisionnels du modèle.
    SHAP vise la fidélité, LIME vise une approximation locale.

**Heatmap**
    Visualisation d'une matrice 2D où les couleurs indiquent l'intensité des valeurs.
    En XAI, souvent utilisée pour visualiser l'importance des tokens (attention, gradients, etc.).

---

Architecture & Modèles
======================

**BERT (Bidirectional Encoder Representations from Transformers)**
    Modèle pré-entraîné basé sur Transformer avec 12 couches et 110M paramètres.
    Fine-tuné pour diverses tâches NLP (classification, QA, NER, etc.).

**DistilBERT**
    Version compressée de BERT avec 6 couches (au lieu de 12) et 66M paramètres.
    Conserve 97% des performances avec 40% moins de paramètres et 60% plus rapide.

**RoBERTa**
    Improvement sur BERT avec meilleur pré-entraînement et optimisation.
    Plus performant sur la plupart des benchmarks.

**GPT**
    Série de modèles pré-entraînés utilisant l'architecture Transformer (seulement décodeur).
    Optimisés pour la génération de texte.

**Multi-Head Attention**
    Variante de l'attention utilisant h têtes d'attention en parallèle.
    Permet au modèle de regarder différentes positions/représentations simultanément.

---

Statistiques & Métriques
========================

**Corrélation de Spearman (ρ)**
    Mesure de corrélation entre les rangs de deux variables.
    Robuste aux outliers contrairement à Pearson.
    Intervalle : [-1, 1] (1 = corrélation parfaite, 0 = indépendance).

**p-value**
    Probabilité observant une statistique aussi extrême par chance si H0 est vraie.
    Conventionnellement : p < 0.05 → résultat significatif.

**Softmax**
    Fonction de normalisation convertissant des scores en probabilités.
    Formula : softmax(x_i) = exp(x_i) / Σ_j exp(x_j)

**Cross-Entropy Loss**
    Fonction de perte pour la classification multi-classe.
    Mesure la divergence entre distribution prédite et distribution vraie.

**Ranking**
    Ordre des éléments par importance/magnitude.
    Important pour Spearman (qui compare les rangs, pas les valeurs absolues).

---

Concepts d'Entraînement
=======================

**Fine-tuning**
    Entraîner un modèle pré-entraîné sur une tâche spécifique avec données annotées.
    Généralement plus efficace que d'entraîner from scratch.

**Pré-entraînement (Pre-training)**
    Entraînement initial d'un modèle sur un grand corpus non-annoté (next-word prediction, masked language, etc.).
    Fournit des représentations générales utiles pour le fine-tuning.

**Overfitting**
    Quand un modèle mémorise les données d'entraînement et ne généralise pas.
    Solution : régularization, dropout, early stopping.

**Regularization**
    Technique pour réduire l'overfitting en ajoutant des contraintes à l'apprentissage.
    Exemples : L1/L2 penalty, dropout, weight decay.

---

Concepts NLP
============

**Tokenization**
    Découpage du texte en tokens (mots, sous-mots, caractères).
    Important pour le modèle qui fonctionne avec des indices, pas des caractères bruts.

**Embedding**
    Représentation vecteur d'un token/phrase dans un espace continu.
    Exemple : "good" → [0.3, -0.5, 0.1, ...] (en 768 dimensions pour BERT).

**Contexte Bidirectionnel**
    Information provenant des tokens avant ET après le token courant.
    Utilisé par BERT (masked language modeling).

**Contexte Unidirectionnel (Auto-régressive)**
    Information seulement des tokens précédents.
    Utilisé par GPT (next-word prediction).

**Sentiment Analysis**
    Tâche NLP d'identifier le sentiment (positif, négatif, neutre) du texte.
    Utilisée dans cette étude (SST-2 dataset).

**Négation**
    Mot ou structure inversant le sens (not, no, never, etc.).
    Challenge majeur identifié dans cette étude : l'attention les sous-estime systématiquement.

---

Termes Méthodologiques
======================

**Validation Croisée (Cross-Validation)**
    Technique d'évaluation utilisant plusieurs splits train/test.
    K-fold CV : découper données en K parties, entraîner K fois.

**Perturbation**
    Modification de l'entrée (masquer, supprimer, inverser) pour tester l'impact sur la prédiction.
    Utilisée par LIME.

**Model-Agnostic**
    Méthode fonctionnant avec n'importe quel modèle (boîte noire).
    LIME et SHAP sont model-agnostic.

**Post-Hoc Explanation**
    Explication générée après que le modèle ait fait sa prédiction.
    Contraste avec "interpretable-by-design" (architecture conçue pour être explicable).

**Benchmark**
    Dataset standardisé pour évaluer et comparer des modèles.
    Exemples : GLUE (9 tâches NLP), ImageNet (vision).

---

Concepts Académiques
====================

**Paper (ou Article Scientifique)**
    Document de recherche rapportant des résultats scientifiques.
    Domaines : conferences (ACL, NeurIPS) ou journals (ACM TIST, IEEE TNNLS).

**Conference Proceeding**
    Article accepté et présenté à une conférence scientifique.
    Exemple : "NAACL 2019" (conférence annuelle).

**ArXiv**
    Serveur de preprints ouvert pour les articles pré-review.
    Souvent les articles modernes sont soumis d'abord à arXiv.

**Reproducibilité**
    Capacité à reproduire les résultats d'un article en utilisant le code et données fournis.
    Critique pour la science ouverte.

**State-of-the-Art (SOTA)**
    Performance meilleure que tous les résultats publiés précédemment sur un benchmark donné.

---

Termes Réglementaires
====================

**GDPR (General Data Protection Regulation)**
    Régulation européenne sur la protection des données.
    Article 22 : droit à l'explication pour les décisions automatisées.

**CCPA (California Consumer Privacy Act)**
    Régulation californienne sur la vie privée des données.
    Similaire à GDPR mais moins stricte.

**Right to Explanation**
    Droit légal d'une personne à obtenir une explication pour une décision automatisée.
    Motivé à utiliser des méthodes XAI dans les systèmes réglementés.

---

Acronymes Courants
===================

.. list-table::
   :header-rows: 1

   * - Acronyme
     - Signification
   * - AI
     - Artificial Intelligence
   * - ML
     - Machine Learning
   * - NLP
     - Natural Language Processing
   * - XAI
     - Explainable AI
   * - BERT
     - Bidirectional Encoder Representations from Transformers
   * - RNN
     - Recurrent Neural Network
   * - LSTM
     - Long Short-Term Memory
   * - GRU
     - Gated Recurrent Unit
   * - CNN
     - Convolutional Neural Network
   * - FC/MLP
     - Fully Connected / Multi-Layer Perceptron
   * - BLIP
     - Bidirectional Language-Image Pre-training
   * - GPT
     - Generative Pre-trained Transformer
   * - QA
     - Question Answering
   * - NER
     - Named Entity Recognition
   * - POS
     - Part-of-Speech
   * - SVM
     - Support Vector Machine
   * - SVM
     - Support Vector Machine

---

Symboles Mathématiques
======================

.. list-table::
   :header-rows: 1

   * - Symbole
     - Signification
   * - Q
     - Query matrix en attention
   * - K
     - Key matrix en attention
   * - V
     - Value matrix en attention
   * - α
     - Attention weights / Poids d'attention
   * - ρ
     - Spearman correlation coefficient
   * - σ
     - Softmax function / Écart-type
   * - ∇
     - Gradient (dérivée)
   * - λ
     - Paramètre de régularisation
   * - θ
     - Paramètres du modèle
   * - ℒ
     - Loss function
   * - p(x)
     - Probabilité de x
   * - E[·]
     - Espérance mathématique
   * - ||·||
     - Norme (magnitude)

---

Ressources pour Approfondir
============================

- **Glossaire complet XAI** : https://www.explainableai.org/glossary
- **Terme ML** : https://developers.google.com/machine-learning/glossary
- **Université Stanford** : https://cs224n.stanford.edu/ (cours NLP)

---
