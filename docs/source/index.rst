.. XAI Attention is Not Explanation documentation master file

==========================================================
XAI Mini-Projet : Attention is Not Explanation
==========================================================

.. image:: _static/banner.txt
   :align: center
   :alt: Project Banner

**Analyse Critique du Mécanisme d'Attention comme Outil d'Explicabilité**

Une étude expérimentale basée sur les travaux de `Jain & Wallace (2019) <https://arxiv.org/abs/1902.10186>`_ 
et `Wiegreffe & Pinter (2019) <https://arxiv.org/abs/1908.04626>`_

.. note::
   **Type du projet** : NLP / Explicabilité de l'IA (XAI)  
   **Date** : Décembre 2025  
   **Cours** : Explicabilité de l'IA  
   **Étudiants** : [Nom Étudiant 1] & [Nom Étudiant 2]

---

Table des Matières
==================

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Documentation

   1_contexte_motivation
   2_intuition_methode
   3_formalisation_mathematique
   4_implementation_pratique
   5_experiences_visualisations
   6_discussion_critique
   7_conclusion_points_cles
   8_references

---

Présentation Générale
=====================

Ce projet exploite une question fondamentale en explicabilité de l'IA :

    **Les poids d'attention des Transformers constituent-ils de véritables explications ?**

Les modèles Transformer (BERT, GPT, etc.) utilisent des mécanismes d'attention pour pondérer l'importance relative des tokens. 
Nombreux sont les praticiens qui interprètent ces poids comme des **explications** de la décision du modèle.

Cependant, deux articles majeurs proposent des perspectives diamétralement opposées :

- **Jain & Wallace (2019)** : L'attention est fondamentalement insuffisante comme outil d'explication
- **Wiegreffe & Pinter (2019)** : L'attention peut fournir des explications valides sous certaines conditions

Ce projet **reproduit expérimentalement ce débat** et développe une analyse critique de ces positions.

---

Aperçu Rapide
=============

**Problématique** 
   Les mécanismes d'attention ne reflètent pas nécessairement les éléments qui influencent la décision finale du modèle.

**Objectifs**
   ✓ Analyser la fiabilité de l'attention comme explication  
   ✓ Comparer avec LIME et SHAP  
   ✓ Identifier des cas pathologiques  
   ✓ Développer un esprit critique sur les heatmaps d'attention

**Méthode**
   - Fine-tuned DistilBERT (SST-2, sentiment analysis)
   - Extraction des poids d'attention
   - Comparaison avec LIME et SHAP
   - Analyse de corrélation (Spearman)
   - Cas d'étude : négations et structures complexes

**Résultats Clés**
   - Corrélation moyenne faible (~0.3) avec LIME
   - Attention mal adaptée aux négations
   - L'attention est un **outil exploratoire**, pas une **explication causale**

---

Accès Rapide
============

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: **Commencer**
      :link: 1_contexte_motivation
      :link-type: doc

      Comprenez le contexte scientifique et les motivations du projet.

   .. grid-item-card:: **Concepts Théoriques**
      :link: 3_formalisation_mathematique
      :link-type: doc

      Équations et formalismes mathématiques du mécanisme d'attention.

   .. grid-item-card:: **Code & Implémentation**
      :link: 4_implementation_pratique
      :link-type: doc

      Installation, configuration et code pour exécuter les expériences.

   .. grid-item-card:: **Résultats**
      :link: 5_experiences_visualisations
      :link-type: doc

      Visualisations, analyses et résultats empiriques.

   .. grid-item-card:: **Critique & Discussion**
      :link: 6_discussion_critique
      :link-type: doc

      Forces, limites et recommandations pratiques.

   .. grid-item-card:: **Conclusion**
      :link: 7_conclusion_points_cles
      :link-type: doc

      Points clés et perspectives futures.

---

Comment Utiliser Cette Documentation
====================================

Cette documentation est organisée en 8 sections :

1. **Contexte & Motivation** : Présentation du débat scientifique
2. **Intuition de la Méthode** : Explication conceptuelle du problème
3. **Formalisation Mathématique** : Équations et métriques
4. **Implémentation Pratique** : Guide d'installation et code
5. **Expériences & Visualisations** : Résultats et analyses
6. **Discussion Critique** : Avantages et limitations
7. **Conclusion** : Synthèse et recommandations
8. **Références** : Bibliographie complète

.. tip::
   Vous pouvez naviguer linéairement ou directement consulter les sections qui vous intéressent.

---

Environnement Requis
====================

.. code-block:: bash

   Python >= 3.8
   PyTorch >= 1.9
   Transformers >= 4.0
   SHAP >= 0.40
   LIME >= 0.2
   Matplotlib & Seaborn

Installation rapide :

.. code-block:: bash

   pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy

---

Indices et Ressources
=====================

.. toctree::
   :hidden:
   :caption: Annexes

   glossaire
   faq

---

Licence et Attribution
======================

Ce projet s'inspire des travaux suivants :

- Jain & Wallace (2019) - « Attention is Not Explanation » (NAACL)
- Wiegreffe & Pinter (2019) - « Attention is Not Not Explanation » (EMNLP)

**Utilisation** : Libre d'utilisation à des fins éducatives et de recherche.

---

.. include:: footer.rst
