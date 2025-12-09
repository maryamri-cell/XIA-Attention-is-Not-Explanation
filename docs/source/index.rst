Remove standalone '---' separators: replaced occurrences with standard spacing and headings.

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

Présentation Générale
=====================

Ce projet exploite une question fondamentale en explicabilité de l'IA :

    **Les poids d'attention des Transformers constituent-ils de véritables explications ?**

Les modèles Transformer (BERT, GPT, etc.) utilisent des mécanismes d'attention pour pondérer l'importance relative des tokens. 
Nombreux sont les praticiens qui interprètent ces poids comme des **explications** de la décision du modèle.

Cependant, deux articles majeurs proposent des perspectives diamétralement opposées :

- **Jain & Wallace (2019)** : L'attention est fondamentalement insuffisante comme outil d'explication
- **Wiegreffe & Pinter (2019)** : L'attention peut fournir des explications valides sous certaines conditions

This project **reproduit expérimentalement ce débat** et développe une analyse critique de ces positions.

Aperçu Rapide
=============

**Problématique** 
   Les mécanismes d'attention ne reflètent pas nécessairement les éléments qui influencent la décision finale du modèle.

**Objectifs**
   - Analyser la fiabilité de l'attention comme méthode d'explicabilité
   - Comparer l'attention avec des méthodes d'attribution établies (LIME, SHAP)
   - Identifier des cas pathologiques où l'attention est trompeuse
   - Formuler des recommandations pour l'utilisation responsable des heatmaps d'attention

**Méthode**
   - Fine-tuning de DistilBERT (SST-2, classification de sentiments)
   - Extraction et analyse des poids d'attention
   - Comparaison avec LIME et SHAP
   - Analyse statistique (corrélation de Spearman)
   - Études de cas : négations et constructions linguistiques complexes

**Résultats clés**
   - Corrélation moyenne modérée-faible (~0.3) avec LIME
   - Sensibilité limitée de l'attention aux négations
   - Conclusion : l'attention constitue un outil exploratoire davantage qu'une explication causale

Accès Rapide
============

**1. Commencer**
   Comprenez le contexte scientifique et les motivations du projet. Voir :ref:`contexte-motivation`

**2. Concepts Théoriques**
   Équations et formalismes mathématiques du mécanisme d'attention. Voir :ref:`formalisation-mathematique`

**3. Code & Implémentation**
   Installation, configuration et code pour exécuter les expériences. Voir :ref:`implementation-pratique`

**4. Résultats**
   Visualisations, analyses et résultats empiriques. Voir :ref:`experiences-visualisations`

**5. Critique & Discussion**
   Forces, limites et recommandations pratiques. Voir :ref:`discussion-critique`

**6. Conclusion**
   Points clés et perspectives futures. Voir :ref:`conclusion-points-cles`

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

Indices et Ressources
=====================

.. toctree::
   :hidden:
   :caption: Annexes

   glossaire
   faq

Licence et Attribution
======================

Ce projet s'inspire des travaux suivants :

- Jain & Wallace (2019) - « Attention is Not Explanation » (NAACL)
- Wiegreffe & Pinter (2019) - « Attention is Not Not Explanation » (EMNLP)

**Utilisation** : Libre d'utilisation à des fins éducatives et de recherche.

.. include:: footer.rst
