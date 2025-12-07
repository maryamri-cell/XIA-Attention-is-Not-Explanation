.. _contexte-motivation:

============================
1. Contexte & Motivation
============================

.. contents::
   :local:
   :depth: 2

---

Le Problème Fondamental
========================

Les modèles **Transformer** modernes (BERT, GPT, RoBERTa, etc.) utilisent un mécanisme appelé **Self-Attention** pour traiter et analyser les séquences textuelles.

Ce mécanisme produit des **poids d'attention** : des probabilités indiquant le "degré d'intérêt" du modèle pour chaque token de l'entrée.

.. note::
   
   **En théorie** : Ces poids d'attention devraient révéler quels tokens influencent la prédiction du modèle.
   
   **En pratique** : Cela ne fonctionne pas toujours !

---

Le Débat Scientifique : Deux Visions Opposées
==============================================

En 2019, deux articles majeurs ont lancé un débat académique intense sur la fiabilité de l'attention comme outil d'explication.

Article 1 : « Attention is Not Explanation »
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Auteurs** : Sarthak Jain & Byron C. Wallace  
**Conférence** : NAACL 2019  
**ArXiv** : https://arxiv.org/abs/1902.10186

**Thèse principale** :

    Les poids d'attention ne constituent **pas** des explications fiables des décisions du modèle.

**Arguments clés** :

1. **Test de permutation** : Permuter aléatoirement les poids d'attention ne change souvent pas la prédiction
   
   .. math::
      
      \text{Si} \quad \sigma(\alpha) = \sigma(\alpha') \quad \text{mais} \quad \alpha \neq \alpha'
      
      \text{Alors l'attention ne capture pas les décisions causales}

2. **Distributions alternatives** : D'autres distributions de poids produisent des résultats identiques

3. **Faible corrélation gradient** : Corrélation faible entre attention et gradients (mesure établie d'importance)

4. **Métaphore du "où" vs "pourquoi"** : L'attention montre **où** le modèle regarde, pas **pourquoi** il décide

**Impact** : Article très influent ayant semé le doute sur la validité de visualiser les heatmaps d'attention.

---

Article 2 : « Attention is Not Not Explanation »
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Auteurs** : Sarah Wiegreffe & Yuval Pinter  
**Conférence** : EMNLP 2019  
**ArXiv** : https://arxiv.org/abs/1908.04626

**Thèse principale** :

    L'attention **peut** constituer une explication valide, sous certaines conditions et interprétations appropriées.

**Contre-arguments clés** :

1. **Critique méthodologique** : Les tests de Jain & Wallace sont trop stricts et artificiels

2. **Dépendance contextuelle** : L'interprétabilité dépend du type de modèle, de tâche et de données

3. **Explication vs Explication fidèle** : Distinction importante entre :
   
   - **Explication** : Attribution de causalité logique
   - **Explication fidèle** : Attribution mathématiquement garantie
   
   L'attention peut être une explication sans être une explication fidèle.

4. **Validation empirique** : Certains cas montrent une bonne corrélation entre attention et importance réelle

**Impact** : Apporte une nuance importante : le problème n'est pas binaire, mais dépend fortement du contexte.

---

Où se Situe ce Projet ?
~~~~~~~~~~~~~~~~~~~~~~~

Ce projet **prend du recul** et propose une **analyse critique autonome** :

.. image:: _static/debate_spectrum.txt
   :align: center
   :alt: Spectrum du débat

- ✗ Nous ne défendons pas l'une ou l'autre position absolue
- ✓ Nous **reproduisons expérimentalement** les critiques des deux camps
- ✓ Nous **quantifions empiriquement** la fiabilité de l'attention via LIME et SHAP
- ✓ Nous **développons un jugement critique** nuancé

---

Objectifs du Projet
====================

| Objectif | Description | Métrique |
|:---------|:-----------|----------|
| **Analyser** | Examiner si l'attention capture l'importance réelle | Corrélation de Spearman |
| **Comparer** | Confronter attention, LIME et SHAP | Visualisations comparatives |
| **Démontrer** | Identifier des cas pathologiques | Cas d'étude (négations, etc.) |
| **Critiquer** | Développer un jugement nuancé | Discussion qualitative |

---

Questions de Recherche
======================

Cette étude tente de répondre à :

1. **Q1** : Quelle est la corrélation entre les poids d'attention et les mesures d'importance établies (LIME, SHAP) ?

2. **Q2** : L'attention gère-t-elle correctement les structures linguistiques complexes (négations, conjonctions) ?

3. **Q3** : Existe-t-il des heuristiques pour identifier quand l'attention est fiable vs trompeuse ?

4. **Q4** : Comment utiliser l'attention de manière responsable dans une pipeline XAI ?

---

Caractéristiques de l'Étude
============================

.. list-table::
   :header-rows: 1

   * - Propriété
     - Valeur
   * - **Type d'explication**
     - Locale (per-instance)
   * - **Domaine**
     - NLP / Analyse de sentiments
   * - **Modèle étudié**
     - DistilBERT fine-tuné (SST-2)
   * - **Tâche**
     - Classification binaire (Positif/Négatif)
   * - **Sortie**
     - Scores d'importance par token
   * - **Famille XAI**
     - Gradient-free + Attention-based
   * - **Nombre de cas**
     - 7+ phrases de test
   * - **Méthodes de validation**
     - LIME, SHAP, corrélation de Spearman

---

Enjeux Pratiques
=================

Pourquoi cette question est-elle importante ?

1. **Trustworthiness** 🔐
   
   Si l'attention est trompeuse, visualiser des heatmaps augmente faussement la confiance des utilisateurs.

2. **Responsabilité** ⚖️
   
   Les systèmes de recommandation ou de classification doivent reposer sur des explications **réelles**, pas superficielles.

3. **Recherche** 🔬
   
   Le débat affecte comment on interprète les résultats des modèles Transformer.

4. **Adoption** 📈
   
   Savoir quand faire confiance à l'attention guidera son utilisation en production.

---

Contribution du Projet
======================

Ce projet contribue :

✓ **Reproduction** des critiques scientifiques dans un cadre unifié  
✓ **Validation empirique** sur des cas français et anglais  
✓ **Identification** de points de basculement (quand l'attention faillit)  
✓ **Recommandations** pratiques pour l'usage responsable  
✓ **Code ouvert** pour étudier d'autres modèles/tâches  

---

Structure de la Suite
=====================

La documentation progresse comme suit :

1. **Intuition** → Explication conceptuelle facile à comprendre
2. **Théorie** → Formalismes mathématiques rigoureux
3. **Implémentation** → Code reproductible et détaillé
4. **Résultats** → Expériences et visualisations
5. **Critique** → Analyse nuancée et recommandations
6. **Conclusion** → Synthèse et perspectives

---

Prérequis
=========

Pour suivre ce projet, il est utile de connaître :

- **NLP de base** : Tokens, embeddings, transformer
- **Python** : Pandas, NumPy, PyTorch
- **Visualisation** : Matplotlib, Seaborn
- **Statistiques** : Corrélation, p-values
- **XAI** : LIME, SHAP (brèves explications fournies)

.. note::
   
   Pas de panique ! Chaque concept est expliqué progressivement.

---

Prochaines Étapes
==================

Prêt à plonger ? Commencez par :

1. **Lire** l'intuition de la méthode (section 2)
2. **Maîtriser** la formalisation mathématique (section 3)
3. **Exécuter** le code (section 4)
4. **Analyser** les résultats (section 5)

.. button-ref:: 2_intuition_methode
   :color: primary
   :outline:

   Continuer vers l'Intuition →

---
