.. _implementation-pratique:

==========================
4. Implémentation Pratique
==========================

.. contents::
   :local:
   :depth: 2

---

Configuration de l'Environnement
=================================

Installation des Dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installez les packages requis via pip :

.. code-block:: bash

    pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy -q

Ou avec conda :

.. code-block:: bash

    conda install pytorch transformers lime shap matplotlib seaborn pandas numpy scipy

Vérification
~~~~~~~~~~~~

Après installation, vérifiez que tout fonctionne :

.. code-block:: python

    import torch
    import transformers
    import shap
    import lime
    
    print(f"PyTorch: {torch.__version__}")
    print(f"Transformers: {transformers.__version__}")
    print(f"SHAP, LIME: OK")

---

Imports et Configuration
========================

Code Python minimal pour débuter :

.. code-block:: python

    # === Imports ===
    import warnings
    warnings.filterwarnings('ignore')

    # Deep Learning & NLP
    import torch
    import torch.nn.functional as F
    from transformers import (
        AutoTokenizer, 
        AutoModelForSequenceClassification,
        pipeline
    )

    # XAI Libraries
    import shap
    from lime.lime_text import LimeTextExplainer

    # Data & Visualization
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

    # Configuration du style
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("husl")
    plt.rcParams['figure.dpi'] = 100

    print("Environnement initialisé avec succès !")

---

Chargement du Modèle
====================

Nous utilisons **DistilBERT** fine-tuné sur le dataset **SST-2** pour la classification de sentiments.

Code
~~~~

.. code-block:: python

    # === Chargement du modèle ===
    MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

    print("Chargement du modèle DistilBERT...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_NAME, 
        output_attentions=True  # IMPORTANT: Activation des sorties d'attention
    )
    model.eval()

    # Pipeline pour prédictions
    sentiment_pipeline = pipeline(
        "sentiment-analysis", 
        model=model, 
        tokenizer=tokenizer,
        return_all_scores=True
    )

    print("✓ Modèle chargé avec succès")
    print(f"  Architecture     : DistilBERT")
    print(f"  Tâche            : Sentiment Analysis (SST-2)")
    print(f"  Couches          : 6")
    print(f"  Têtes d'attention: 12")

Détails Techniques
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Propriété
     - Valeur
   * - **Modèle de base**
     - DistilBERT (version réduite de BERT)
     * - **Tokenizer**
     - BertTokenizer (vocabulaire 30k tokens)
   * - **Fine-tuning**
     - SST-2 (Stanford Sentiment Treebank)
   * - **Classes**
     - 2 (NEGATIVE, POSITIVE)
   * - **Couches Transformer**
     - 6 couches
   * - **Têtes d'attention**
     - 12 par couche (72 au total)
   * - **Dimension modèle**
     - 768

.. note::
   
   Le paramètre ``output_attentions=True`` est crucial : il force le modèle à retourner les matrices d'attention.

---

Corpus de Test
==============

Préparation des Données
~~~~~~~~~~~~~~~~~~~~~~~

Définissez un ensemble de phrases couvrant différents cas :

.. code-block:: python

    test_sentences = [
        # Cas clairs avec sentiment explicit
        "This movie is absolutely fantastic and wonderful!",
        "The film was terrible and boring, I hated it.",
        
        # Cas avec négation simple
        "The movie was not bad at all, actually quite good.",
        
        # Cas avec négation et inversion d'expectation
        "I thought I would hate it but surprisingly I loved it.",
        "Despite the great acting, the movie failed to impress me.",
        
        # Cas avec double négation
        "The movie is not uninteresting.",
        "I cannot say this was a bad experience.",
    ]

Code pour Tester les Prédictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    print("=" * 70)
    print("  PRÉDICTIONS DU MODÈLE")
    print("=" * 70)
    print()

    results = []
    for i, sentence in enumerate(test_sentences, 1):
        pred = sentiment_pipeline(sentence)[0]
        label = "POSITIVE" if pred[1]['score'] > pred[0]['score'] else "NEGATIVE"
        score = max(pred[0]['score'], pred[1]['score'])
        
        results.append({
            'ID': i,
            'Phrase': sentence[:60] + ("..." if len(sentence) > 60 else ""),
            'Sentiment': label,
            'Confiance': f"{score:.1%}"
        })
        
        indicator = "[+]" if label == "POSITIVE" else "[-]"
        print(f"  {indicator} Phrase {i}: {label} ({score:.1%})")
        print(f"      \"{sentence}\"")
        print()

    # Affichage du tableau
    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))

---

Extraction des Poids d'Attention
=================================

Fonction Principale
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def get_attention_weights(text, model, tokenizer, layer_aggregation='mean'):
        """
        Extrait les poids d'attention pour une phrase donnée.
        
        Parameters:
            text (str): Phrase à analyser
            model: Modèle Transformer fine-tuné
            tokenizer: Tokenizer associé
            layer_aggregation (str): 'mean', 'max', ou 'first'
        
        Returns:
            tokens (list): Liste des tokens
            attention_weights (np.array): Poids d'attention moyennés
            all_attentions (tuple): Attention brute par couche et tête
        """
        # Tokenization
        inputs = tokenizer(
            text, 
            return_tensors="pt", 
            truncation=True, 
            max_length=512
        )
        tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
        
        # Forward pass avec extraction d'attention
        with torch.no_grad():
            outputs = model(**inputs)
        
        # Extraction des attentions : tuple of tensors
        # Shape de chaque élément: (batch_size, num_heads, seq_len, seq_len)
        attentions = outputs.attentions
        
        # Étape 1: Extraire l'attention du token [CLS] vers tous les autres
        # [CLS] est le premier token (indice 0)
        cls_attention_per_layer = []
        for layer_attention in attentions:
            # layer_attention shape: (1, 12, seq_len, seq_len)
            # Extraire pour position [CLS] = position 0
            cls_layer = layer_attention[0, :, 0, :]  # (12, seq_len)
            cls_attention_per_layer.append(cls_layer)
        
        # Étape 2: Agréger selon layer_aggregation
        if layer_aggregation == 'mean':
            # Moyenne sur les couches et les têtes
            cls_attention_stacked = torch.stack(cls_attention_per_layer)  # (6, 12, seq_len)
            avg_attention = cls_attention_stacked.mean(dim=(0, 1)).cpu().numpy()
        elif layer_aggregation == 'max':
            cls_attention_stacked = torch.stack(cls_attention_per_layer)
            avg_attention = cls_attention_stacked.max(dim=0)[0].mean(dim=0).cpu().numpy()
        else:
            # Utiliser seulement la première couche
            avg_attention = cls_attention_per_layer[0].mean(dim=0).cpu().numpy()
        
        return tokens, avg_attention, attentions


Exemple d'Utilisation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Test sur une phrase
    test_text = "This movie is fantastic!"
    tokens, attention, _ = get_attention_weights(test_text, model, tokenizer)

    print(f"Phrase: {test_text}")
    print(f"Tokens: {tokens}")
    print(f"Poids d'attention: {attention}")
    print()
    print("Détail :")
    for tok, att in zip(tokens, attention):
        print(f"  {tok:15} → {att:.4f}")

**Résultat attendu** :

.. code-block:: text

    Phrase: This movie is fantastic!
    Tokens: ['[CLS]', 'this', 'movie', 'is', 'fantastic', '!', '[SEP]']
    Poids d'attention: [0.1234, 0.0987, 0.1456, 0.1234, 0.4512, 0.0987, 0.0590]
    
    Détail :
      [CLS]           → 0.1234
      this            → 0.0987
      movie           → 0.1456
      is              → 0.1234
      fantastic       → 0.4512   ← Attention élevée
      !               → 0.0987
      [SEP]           → 0.0590

---

Configuration de LIME
=====================

.. code-block:: python

    # Fonction de prédiction pour LIME
    def predict_proba(texts):
        """
        Wrapper de prédiction compatible avec LIME.
        
        Parameters:
            texts (list): Liste de phrases
        
        Returns:
            np.array: Probabilités [P(NEG), P(POS)] pour chaque phrase
        """
        results = []
        for text in texts:
            pred = sentiment_pipeline(text)[0]
            probs = [pred[0]['score'], pred[1]['score']]
            results.append(probs)
        return np.array(results)

    # Création du explainer
    lime_explainer = LimeTextExplainer(
        class_names=['NEGATIVE', 'POSITIVE'],
        split_expression=r'\W+',  # Split sur les non-word characters
        random_state=42
    )

    print("✓ LIME Explainer configuré")

---

Exécution des Analyses
======================

Voir les sections **5. Expériences & Visualisations** pour le code d'analyse complet.

Points clés :

1. Extraire attention et LIME pour chaque phrase
2. Calculer la corrélation de Spearman
3. Visualiser et comparer les résultats
4. Analyser les cas pathologiques (négations, etc.)

---

Prochaines Étapes
==================

Le code complet est dans le notebook `Projet7_Attention_Not_Explanation.ipynb`.

.. button-ref:: 5_experiences_visualisations
   :color: primary
   :outline:

   Vers les Expériences →

---
