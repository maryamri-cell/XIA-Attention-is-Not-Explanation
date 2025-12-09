.. _references:

==========
8. Références
==========

.. contents::
   :local:
   :depth: 2

---

Articles Fondateurs du Débat
=============================

**[1] Jain, S., & Wallace, B. C. (2019).**

"Attention is Not Explanation"

*Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)*

ArXiv: https://arxiv.org/abs/1902.10186  
DOI: 10.18653/v1/N19-1357

**Résumé** :

Les auteurs démontrent que :

- Les poids d'attention peuvent être permutés sans changer la prédiction
- Des distributions alternatives d'attention produisent les mêmes résultats
- L'attention a une corrélation faible avec les gradients
- L'attention n'explique pas les décisions du modèle de manière fiable

**Impact** : Article très influent (~2000+ citations) qui a remis en question l'usage des heatmaps d'attention comme explications.

---

**[2] Wiegreffe, S., & Pinter, Y. (2019).**

"Attention is Not Not Explanation"

*Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)*

ArXiv: https://arxiv.org/abs/1908.04626  
DOI: 10.18653/v1/D19-1002

**Résumé** :

Les auteurs répondent aux critiques de Jain & Wallace :

- Les tests de Jain & Wallace sont méthodologiquement discutables
- L'attention peut être une explication valide sous certaines conditions
- Distinction importante : explication vs explication fidèle
- L'attention reste informative quand interprétée correctement

**Impact** : Apporte une nuance importante au débat, montrant que la réponse n'est pas binaire.

---

Articles de Contexte
====================

**[3] Vaswani, A., et al. (2017).**

"Attention is All You Need"

*Advances in Neural Information Processing Systems (NeurIPS)*

ArXiv: https://arxiv.org/abs/1706.03762  
DOI: 10.5555/3294996.3295043

**Résumé** :

L'article fondateur des Transformers et du mécanisme d'attention moderne.

Introduit :

- Scaled Dot-Product Attention
- Multi-Head Attention
- Architecture entièrement basée sur l'attention

**Impact** : Révolutionnaire, a lancé l'ère des modèles Transformer (BERT, GPT, etc.)

---

**[4] Devlin, J., et al. (2019).**

"BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"

*Proceedings of NAACL-HLT 2019*

ArXiv: https://arxiv.org/abs/1810.04805

**Résumé** :

Introduit BERT (Bidirectional Encoder Representations from Transformers).

BERT est un Transformer pré-entraîné sur de grands corpus de texte.

Peut être fine-tuné pour diverses tâches NLP.

**Impact** : BERT a révolutionné le NLP et est la base de nombreux modèles (DistilBERT, RoBERTa, etc.)

---

**[5] Sanh, V., et al. (2020).**

"DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"

*Findings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*

ArXiv: https://arxiv.org/abs/1910.01108

**Résumé** :

DistilBERT est une version compressée de BERT avec 40% moins de paramètres.

Conserve 97% des performances avec vitesse 60% plus rapide.

C'est le modèle utilisé dans notre étude.

**Impact** : Permet le déploiement pratique de Transformers fine-tuning.

---

Explicabilité et Interprétabilité
==================================

**[6] Ribeiro, M. T., Singh, S., & Guestrin, C. (2016).**

"Why Should I Trust You?: Explaining the Predictions of Any Classifier"

*Proceedings of the 22nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)*

ArXiv: https://arxiv.org/abs/1602.04938

**Résumé** :

Introduit **LIME** (Local Interpretable Model-agnostic Explanations).

LIME perturbe l'entrée localement et entraîne un modèle linéaire pour estimer l'importance des features.

**Impact** : Méthode très influente pour l'XAI local, model-agnostic.

---

**[7] Lundberg, S. M., & Lee, S.-I. (2017).**

"A Unified Approach to Interpreting Model Predictions"

*Advances in Neural Information Processing Systems (NeurIPS)*

ArXiv: https://arxiv.org/abs/1705.07874

**Résumé** :

Introduit **SHAP** (SHapley Additive exPlanations).

SHAP calcule les valeurs de Shapley de la théorie des jeux coopératifs pour expliquer les prédictions.

**Propriétés** :

- Théoriquement fondée (satisfait efficacité, symétrie, etc.)
- Model-agnostic
- Coûteuse en calcul mais très robuste

**Impact** : Devient le gold standard pour l'explicabilité en ML.

---

**[8] Montavon, G., Samek, W., & Müller, K. (2017).**

"Methods for Interpreting and Understanding Deep Neural Networks"

*Digital Signal Processing*

ArXiv: https://arxiv.org/abs/1706.07979

**Résumé** :

Survey complet des méthodes d'interprétabilité pour les réseaux profonds.

Couvre :

- Feature importance
- Perturbation-based methods
- Gradient-based methods
- Layer-wise relevance propagation

**Impact** : Reference complète pour les chercheurs en XAI.

---

Critiques Complémentaires de l'Attention
=========================================

**[9] Serrano, S., & Smith, N. A. (2019).**

"Is Attention Interpretable?"

*Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)*

ArXiv: https://arxiv.org/abs/1906.03731

**Résumé** :

Analyse critiquement si l'attention peut être interprétée comme une mesure d'importance.

Montre :

- Attention confond importance et similarité
- Biais vers les self-attention
- Instabilité à travers différents fine-tunings

**Impact** : Renforce les critiques de Jain & Wallace avec des analyses additionnelles.

---

**[10] Clark, K., Khandelwal, U., Levy, O., & Manning, C. D. (2019).**

"What Does BERT Look At? An Analysis of BERT's Attention"

*BlackboxNLP Workshop at ACL 2019*

ArXiv: https://arxiv.org/abs/1906.04341

**Résumé** :

Analyse empiriquement ce que les différentes couches et têtes de BERT font :

- Couches basses : syntaxe locale
- Couches intermédiaires : relations de phrase
- Couches hautes : patterns sémantiques

Mais montre aussi que beaucoup de têtes sont sans interprétation claire.

**Impact** : Fournit des insights sur la structure de BERT, mais aussi sur la variabilité de l'attention.

---

Causality et Explicabilité
===========================

**[11] Pearl, J. (2009).**

"Causality: Models, Reasoning, and Inference" (2nd Edition)

*Cambridge University Press*

ISBN: 978-0521895589

**Résumé** :

Traité fondamental sur la causalité en statistiques et en graphes causaux.

Introduit :

- Directed Acyclic Graphs (DAGs)
- D-separation et backdoor criterion
- Interventions et counterfactuals

**Impact** : Fondamental pour comprendre pourquoi l'attention n'est pas causale.

---

**[12] Goyal, Y., et al. (2019).**

"Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR"

*Harvard Journal of Law & Technology*

ArXiv: https://arxiv.org/abs/1711.00399

**Résumé** :

Discute des explications contrefactuelles pour la conformité GDPR.

Argument : Pour vraiment expliquer une décision, il faut montrer comment la modifier.

**Impact** : Important pour les applications réglementaires de l'XAI.

---

Ressources d'apprentissage
============================

**Pour débuter**

1. **Blog : The Illustrated Transformer** (Jay Alammar)
   
   https://jalammar.github.io/illustrated-transformer/
   
   Excellente introduction visuelle aux Transformers.

2. **Blog : The Illustrated BERT, ELMo, and co.** (Jay Alammar)
   
   https://jalammar.github.io/illustrated-bert/
   
   Explication visuelle de BERT.

3. **Hugging Face Course**
   
   https://huggingface.co/course
   
   Cours complet et gratuit sur les Transformers.

---

**Pour approfondir**

1. **Explainability in Deep Learning**
   
   https://github.com/slundberg/shap
   
   Repository SHAP avec examples.

2. **Interpretable Machine Learning**
   
   https://christophm.github.io/interpretable-ml-book/
   
   Livre complet sur l'interprétabilité en ML (version web libre).

3. **NLP with Transformers** (Tunstall et al., 2023)
   
   Book: O'Reilly Media
   
   Couvre les Transformers modernes et l'XAI.

---

**Pour chercheurs**

1. **ACL Anthology**
   
   https://aclanthology.org/
   
   Repository de tous les articles NAACL/ACL/EMNLP.

2. **ArXiv NLP**
   
   https://arxiv.org/list/cs.CL/recent
   
   Preprints les plus récents en NLP.

3. **SemEval Tasks**
   
   https://semeval.github.io/
   
   Shared tasks et benchmarks en NLP.

---

Données et modèles
===================

**Datasets**

- **SST-2** (Stanford Sentiment Treebank)
  
  https://huggingface.co/datasets/sst2
  
  Dataset d'analyse de sentiments utilisé dans notre étude.

- **GLUE**
  
  https://gluebenchmark.com/
  
  Suite de 9 benchmarks NLP variés.

---

**Modèles pré-entraînés**

- **DistilBERT**
  
  https://huggingface.co/distilbert-base-uncased
  
  Modèle utilisé dans cette étude.

- **BERT**
  
  https://huggingface.co/bert-base-uncased
  
  Modèle original.

- **RoBERTa**
  
  https://huggingface.co/roberta-base
  
  Version optimisée de BERT.

- **ELECTRA**
  
  https://huggingface.co/google/electra-base-discriminator
  
  Alternative efficace avec pré-entraînement adversarial.

---

Libraries et outils
===================

**XAI Libraries**

- **LIME** : https://github.com/marcotcr/lime
- **SHAP** : https://github.com/slundberg/shap
- **Captum** : https://github.com/pytorch/captum (PyTorch)
- **Alibi** : https://github.com/SeldonIO/alibi

**NLP & Deep Learning**

- **Transformers (HuggingFace)** : https://huggingface.co/transformers/
- **PyTorch** : https://pytorch.org/
- **TensorFlow** : https://www.tensorflow.org/

**Visualization**

- **Matplotlib** : https://matplotlib.org/
- **Seaborn** : https://seaborn.pydata.org/
- **Plotly** : https://plotly.com/python/
- **Altair** : https://altair-viz.github.io/

---

Conférences et workshops pertinents
===================================

**Conférences majeures**

- **ACL** : Association for Computational Linguistics (Annual)
- **EMNLP** : Conference on Empirical Methods in NLP (Annual)
- **NAACL** : North American Chapter ACL (Biennial)
- **NeurIPS** : Neural Information Processing Systems (Annual)

**Workshops spécialisés**

- **BlackboxNLP** : Interpreting and Understanding Black-box NLP Models
  
  https://blackboxnlp.github.io/

- **XAI/LIME Workshop**
  
  Regularly at KDD, AAAI, etc.

---

Glossaire Technique Complet
============================

Voir la section **Glossaire** pour un glossaire détaillé de tous les termes.

---

Questions Fréquemment Posées
=============================

Voir la section **FAQ** pour les questions courantes.

---

Curation Finale
===============

**Lecture d'une semaine** (si vous avez le temps) :

.. code-block:: text

    Jour 1: Illustrated Transformer (blog)
    Jour 2: BERT paper + Jain & Wallace paper
    Jour 3: LIME et SHAP papers
    Jour 4: Ce notebook + expériences
    Jour 5: Wiegreffe & Pinter + Serrano & Smith
    Jour 6: Résumé personnalisé + discussion
    Jour 7: Implémentation personnelle

---

Citation Recommandée
====================

Si vous utilisez ce projet dans votre recherche :

.. code-block:: bibtex

    @misc{XAIAttentionProject2025,
      title={Mini-Projet XAI: Attention is Not Explanation},
      author={[Vos noms]},
      year={2025},
      institution={[Votre institution]},
      url={https://[votre-repo]}
    }

---
