.. _faq:

========================================
FAQ - Questions Fréquemment Posées
========================================

.. contents::
   :local:
   :depth: 2

---

Questions Générales
====================

**Q: Qu'est-ce que ce projet exactement ?**

R: C'est une étude empirique comparant les explications par attention avec les méthodes XAI établies (LIME, SHAP). L'objectif est de déterminer si les poids d'attention des Transformers constituent de vraies explications.

---

**Q: Faut-il vraiment le lire entièrement ?**

R: Non, voici une lecture optimisée :

- Pressé(e) ? Lire le **Résumé Exécutif** (section 1)
- Intéressé(e) par les résultats ? Sections 4-5
- Chercheur ? Tout (spécialement section 6-7)
- Praticien ? Sections 4 + 6-7

---

**Q: Quel modèle est utilisé ?**

R: DistilBERT fine-tuné sur SST-2 (Stanford Sentiment Treebank) pour la classification de sentiments. C'est un modèle d'environ 66M paramètres, idéal pour les démonstrations.

---

**Q: Peux-je utiliser ce code avec d'autres modèles ?**

R: Oui ! Le code est écrit pour être générique. Vous pouvez substituer :

- `distilbert-base-uncased-finetuned-sst-2-english` par `bert-base-uncased`, `roberta-base`, etc.
- La tâche SST-2 par d'autres (NER, QA, traduction, etc.)

Voir section 4 (Implementation) pour les détails.

---

**Q: Quel est le résultat principal ?**

R: Corrélation de Spearman moyenne = 0.31 entre attention et LIME.

Cela indique une **faible corrélation**, soutenant partiellement Jain & Wallace : l'attention seule n'est pas une explication fiable.

---

Questions Techniques
====================

**Q: Comment fonctionne l'attention exactement ?**

R: 

1. Chaque token a un vecteur Query (Q), chaque token a un vecteur Key (K) et Value (V)
2. Score d'attention = softmax(Q · K^T / √d_k)
3. Output = somme pondérée des Values selon les scores
4. Cela se répète sur 12 têtes et 6 couches (pour DistilBERT)

Voir section 2 pour l'intuition visuelle, section 3 pour les équations.

---

**Q: Pourquoi utiliser Spearman et pas Pearson pour la corrélation ?**

R: Spearman compare les **rangs**, pas les valeurs absolues. Cela est plus robuste aux outliers et à la non-linéarité. Puisqu'on veut savoir "est-ce que l'ordre d'importance est similaire ?", Spearman est plus approprié.

---

**Q: Pourquoi l'attention échoue-t-elle sur les négations ?**

R: L'attention se concentre sur les tokens avec forte similarité cosinus dans l'espace de représentation. "Good" a une forte représentation sémantique, tandis que "not" est structurel. L'architecture n'apprend pas intrinsèquement que la négation modifie la sémantique entière.

C'est une limitation architecturale, pas un bug.

---

**Q: Comment agréger l'attention de 12 têtes et 6 couches ?**

R: Approche standard : moyenne arithmétique. Alternatives :

- Max pooling (sélectionne la plus élevée)
- Weighted average (poids par couche)
- Attention rollout (propager à travers les couches)

La moyenne est la plus simple et transparente.

---

Questions sur la Méthodologie
==============================

**Q: Pourquoi LIME et pas SHAP ?**

R: Nous utilisons les deux, mais LIME est choisi pour le benchmark car :

1. Moins coûteux en calcul (démonstration viable)
2. Local (comparable à attention qui est par-token)
3. Non-déterministe (tester la robustesse)

SHAP serait idéal mais trop coûteux pour cette démonstration.

---

**Q: Comment avez-vous choisi les phrases de test ?**

R: Intentionnellement diverse :

- Sentiments clairs (baseline)
- Négations simples (test commun)
- Structures complexes (inversion d'attente, double négation)
- Cas ambigus

7 phrases c'est petit mais suffisant pour une étude pilote.

---

**Q: Pourquoi seulement anglais ? Pas de français ?**

R: 

- DistilBERT est meilleur en anglais (SST-2 optimisé)
- Mais le code fonctionne en français aussi
- Pour l'étendre au français : utiliser `distilbert-base-multilingual-uncased`

---

**Q: Les résultats sont-ils statistiquement significatifs ?**

R: Partiellement.

- Corrélation moyenne 0.31 : pas fort, mais pas 0
- Grandes variations : certaines corrélations significatives (p < 0.05), d'autres non
- Taille d'échantillon : petite (n=7), donc limites de confiance élevées

Un étude plus grande (centaines de phrases) serait plus robuste.

---

Questions Pratiques
====================

**Q: Peux-je reproduire ce projet facilement ?**

R: Oui ! Le notebook Jupyter contient tout le code.

Étapes :

1. Télécharger le notebook
2. Installer : `pip install torch transformers lime shap matplotlib`
3. Lancer chaque cellule
4. Adapter au besoin

Durée totale : ~20-30 minutes.

---

**Q: Comment adapter ce code à ma tâche ?**

R: 

1. Remplacer le modèle (section 4.1)
2. Adapter les phrases de test (section 4.2)
3. Exécuter les analyses (sections 5)
4. Interpréter les résultats

Le code est conçu pour être générique.

---

**Q: Y a-t-il une API simple ?**

R: Pour utiliser l'attention :

.. code-block:: python

    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-...")
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased-...", 
        output_attentions=True
    )
    
    inputs = tokenizer("Your text here", return_tensors="pt")
    outputs = model(**inputs)
    attentions = outputs.attentions  # Tuple of 6 tensors

Voir section 4.3 pour le code complet.

---

**Q: Comment visualiser l'attention ?**

R: Plusieurs approches :

1. **Simple** : Graphe en barres des poids moyennés
2. **Heatmap** : Matrice 2D (tokens × tokens)
3. **Network** : Graphe montrant les connexions d'attention
4. **Rolling** : Propager à travers les couches

Voir section 5 pour les visualisations du projet.

---

Questions Scientifiques
========================

**Q: Attention vs Explication : Quelle est vraiment la différence ?**

R: 

- **Attention** : "Le modèle regarde ce token" (observation)
- **Explication** : "Ce token cause la décision" (causalité)

Exemple : vous regardez quelqu'un rougir. Regarder les joues ≠ expliquer pourquoi il rougit. Il y a peut-être une cause cachée (embarrassment, coup de soleil, maladie).

---

**Q: Jain & Wallace vs Wiegreffe & Pinter : qui a raison ?**

R: Les deux, partiellement !

- **Jain & Wallace** : Correct que l'attention n'est pas une explication causale pure
- **Wiegreffe & Pinter** : Correct que l'attention peut aider en contexte approprié

Notre conclusion : utiliser l'attention avec LIME/SHAP pour validation.

---

**Q: Peut-on fixer l'attention pour la rendre plus explicable ?**

R: Oui, plusieurs approches :

1. **Task-aware attention** : entraîner l'attention à être pertinente pour la tâche
2. **Constrained attention** : ajouter des régularisations (sparsity, etc.)
3. **Attention+ Gradient** : combiner avec des informations de gradient

C'est une direction de recherche ouverte.

---

**Q: L'attention fonctionne-t-elle mieux en vision que NLP ?**

R: Bon question ! Préliminairement :

- Vision : Attention semble plus localisée spatialement
- NLP : Attention moins évidente (sémantique + syntaxe)

Mais peu d'études croisées. À investiguer !

---

Questions Éthiques & Réglementaires
====================================

**Q: Puis-je utiliser l'attention seule dans une application GDPR ?**

R: Non, c'est risqué.

GDPR requiert une explication "significative" des décisions. L'attention seule peut être trompeuse.

Utiliser : Attention + LIME + SHAP (validation croisée).

---

**Q: Comment expliquer l'attention à un utilisateur non-technique ?**

R: Analogie simple :

    "Ces couleurs montrent où notre système regarde. Mais ça ne veut pas dire que c'est la raison de sa décision. C'est comme demander à quelqu'un pourquoi il conclut quelque chose et il répond 'Je regardais l'écran'. Ça ne le dit pas vraiment."

Puis montrer aussi LIME/SHAP pour la vraie raison.

---

**Q: Quand est-ce "OK" d'utiliser l'attention seule ?**

R: 

- ✓ Débugage interne (vous connaissez les limitations)
- ✓ Recherche exploratoire (préalable à une analyse rigoureuse)
- ✓ Visualisations pédagogiques (avec contexte)
- ✗ Décisions critiques (médecine, justice, finance)
- ✗ Communication grand public (sans avertissement)
- ✗ Conformité réglementaire (seulement)

---

Questions de Recherche
=======================

**Q: Que devrait-on étudier ensuite ?**

R: Directions ouvertes :

1. Pourquoi l'attention échoue-t-elle sur les négations ? (architecture ? données ?)
2. Peut-on prédire quand l'attention sera fiable ? (méta-modèle)
3. Comment faire de l'attention causale ? (constrained learning)
4. Quelle est la meilleure agrégation (heads, layers) ? (empirical comparison)
5. Comment ça se généralise à d'autres domaines ? (vision, RL, etc.)

---

**Q: Y a-t-il des bugs ou limitations dans ce code ?**

R: Limitations connues :

- Petite taille d'échantillon (n=7 phrases)
- Seulement anglais (adapté au multilingual avec effort)
- Seulement SST-2 (une tâche spécifique)
- Attention moyenne sur têtes/couches (perte d'information)

Pour une étude robuste : augmenter l'échantillon, tester multilingue, multiple tâches.

---

**Q: Peut-on étendre ce à la génération (GPT) ?**

R: Oui, avec adaptations :

1. GPT produit aussi des attentions
2. Mais évaluer une explication est plus complexe (génération libre)
3. Benchmark pour la génération : BLEU, ROUGE (pas idéal)
4. Besoin de nouvelles métriques XAI

Intéressant mais out-of-scope pour ce projet.

---

Questions de Carrière
=======================

**Q: Apprendre ça, c'est utile professionnellement ?**

R: Oui ! L'XAI devient critique :

- **Règulation** : GDPR, IA Act rendent XAI obligatoire
- **Trust** : Les utilisateurs demandent des explications
- **Safety** : Comprendre les modèles identifie les biais
- **Skill** : Rares les data scientists sachant XAI bien

C'est une compétence de haut niveau très demandée.

---

**Q: Par où commencer pour devenir expert en XAI ?**

R: Chemin suggéré :

1. **Fondamentaux** : ML classique (régression, arbres, SVM)
2. **Deep Learning** : RNN, CNN, Transformer
3. **Représentation** : Embeddings, visualisation
4. **XAI** : LIME, SHAP, gradients
5. **Applications** : Cas d'usage réels, GDPR, réglementation
6. **Recherche** : Publier, contribuer open-source

Durée : ~2-3 ans de pratique sérieuse.

---

Questions Meta
==============

**Q: Qui a créé ce projet ?**

R: Projet pédagogique d'étudiants en IA (détails dans la page de couverture).

---

**Q: Puis-je utiliser ce contenu ?**

R: Oui ! Libre d'usage pour fins éducatives et recherche. Cite-nous si possible.

---

**Q: Comment contribuer ou signaler un bug ?**

R: 

- Issues : via [GitHub repo du projet]
- Pull requests : contributions bienvenues
- Discussion : contactez les auteurs

---

**Q: Existe-t-il une version plus simple ?**

R: Oui ! Version "15 minutes" :

- Lire cette FAQ
- Regarder les graphiques en section 5
- Lire le Verdict en section 7
- Conclusion : attention utile mais non-suffit, utiliser LIME/SHAP

---

**Q: Où puis-je poser d'autres questions ?**

R: 

- **GitHub Issues** : [URL]
- **Forum académique** : [URL]
- **Email** : [contact]

---

Remerciements
==============

Merci d'avoir lu ! Nous espérons que ce projet vous a aidé à :

✓ Comprendre le débat scientifique sur l'attention et l'XAI  
✓ Apprendre à évaluer les explications empiriquement  
✓ Utiliser LIME, SHAP de manière responsable  
✓ Développer un esprit critique en ML/IA  

Bonne lecture !

---
