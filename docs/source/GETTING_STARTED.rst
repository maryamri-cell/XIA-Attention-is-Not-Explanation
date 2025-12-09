.. _getting-started:

===============
Démarrage Rapide
===============

Bienvenue. Cette page présente des instructions pour démarrer rapidement.

---

Option 1 : Lire la documentation en ligne (recommandé)
==========================================================

Si vous avez accès à une version construite de cette documentation, naviguez simplement :

1. Commencez par l'**index** (vous êtes peut-être déjà ici)
2. Allez à **Section 1 : Contexte & Motivation**
3. Progressez linéairement ou sautez aux sections qui vous intéressent

Durée estimée : 1-3 heures (selon profondeur).

---

Option 2 : Construire Localement (5 minutes)
=============================================

Si vous disposez des sources (dépôt cloné) :

**Pré-requis** : Python 3.8+, pip

**Étapes** :

.. code-block:: bash

    # 1. Naviguer au dossier docs
    cd read-the-doc/docs
    
    # 2. Installer les dépendances
    pip install -r requirements.txt
    
    # 3. Construire le HTML
    make html
    
    # 4. Ouvrir dans le navigateur
    # Sur macOS/Linux :
    open build/html/index.html
    
    # Sur Windows :
    start build\html\index.html

**Résultat** : Documentation HTML locale accessible hors ligne.

---

Option 3 : Lire les Fichiers .rst Directement
==============================================

Les fichiers sources sont en format reStructuredText (.rst) :

.. code-block:: bash

    # Naviguer au dossier source
    cd read-the-doc/docs/source
    
    # Lire avec n'importe quel éditeur de texte
    cat 1_contexte_motivation.rst
    cat 2_intuition_methode.rst
    # ... etc

**Inconvénient** : Pas de formatage HTML/PDF, juste du texte brut.

---

Option 4 : Exécuter le Notebook Jupyter
========================================

Pour les expériences pratiques :

**Pré-requis** : 
- Jupyter (`pip install jupyter`)
- PyTorch, Transformers, LIME, SHAP (voir section Implémentation)

**Étapes** :

.. code-block:: bash

    # 1. Naviguer au dossier
    cd read-the-doc
    
    # 2. Lancer Jupyter
    jupyter notebook
    
    # 3. Ouvrir Projet7_Attention_Not_Explanation.ipynb
    # 4. Exécuter les cellules séquentiellement

**Durée** : ~20-30 minutes pour tout.

---

Parcours Recommandé par Profil
===============================

Je Suis... Étudiante en IA
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Temps disponible** : 4 heures  
**Chemin** :

1. Lire Section 1 (Contexte) - 30 min
2. Lire Section 2 (Intuition) - 45 min
3. Lire Section 3 (Maths) - 1h 15 min
4. Parcourir Section 5 (Résultats) - 30 min
5. Lire Section 6 (Critique) - 1h
6. **Total** : ~4h

**Ressources** :
- Focus : Comprendre le débat scientifique
- Ignorer : Code détaillé (pour l'instant)
- Consulter : Glossaire au besoin

---

Je Suis... Data Scientist
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Temps disponible** : 3 heures  
**Chemin** :

1. Survol Section 1 - 15 min
2. Sauter Section 2-3 (assumé connu) - 0 min
3. Lire Section 4 (Code) - 45 min
4. Exécuter le Notebook - 1h 15 min
5. Lire Section 6 (Recommandations) - 30 min
6. **Total** : ~3h

**Ressources** :
- Focus : Code et résultats pratiques
- Important : Savoir quand utiliser attention/LIME/SHAP
- Consulter : FAQ pour questions techniques

---

Je Suis... Chercheur en NLP
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Temps disponible** : 8 heures  
**Chemin** :

1. Lire tout (sections 1-8) - 5h
2. Relire les articles clés (Jain, Wiegreffe, Serrano) - 2h
3. Exécuter le notebook et expérimenter - 1h
4. **Total** : ~8h

**Ressources** :
- Focus : Rigueur scientifique, états de l'art
- Important : Lire les références
- Consulter : Glossaire académique

---

Je Suis... Product Manager / Décisionnaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Temps disponible** : 1 heure  
**Chemin** :

1. Lire cette page - 10 min
2. Lire Section 1 (Contexte) - 20 min
3. Lire Section 6 (Recommandations) + Section 7 (Conclusion) - 20 min
4. Consulter FAQ si questions - 10 min
5. **Total** : ~1h

**Ressources** :
- Focus : Implications pratiques et recommandations
- Ignorer : Maths détaillées, code
- Key takeaway : "Utiliser LIME/SHAP pour les décisions critiques"

---

Checklist de Démarrage
======================

Avant de vous lancer :

.. list-table::
   :header-rows: 1

   * - Élément
     - À Vérifier
   * - Python 3.8+
     - ``python --version``
   * - Pip à jour
     - ``pip --version``
   * - Git (optionnel)
     - ``git --version``
   * - Editeur de texte/IDE
     - VSCode, PyCharm, Jupyter, etc.
   * - Au moins 2 Go RAM
     - Pour exécuter le notebook
   * - Connexion Internet
     - Pour télécharger les modèles

---

Premiers Pas : Exécuter le Code (5 min)
=======================================

Si vous voulez essayer immédiatement :

.. code-block:: python

    # 1. Installation
    pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy
    
    # 2. Code minimal (voir notebook pour version complète)
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    
    tokenizer = AutoTokenizer.from_pretrained(
        "distilbert-base-uncased-finetuned-sst-2-english"
    )
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased-finetuned-sst-2-english",
        output_attentions=True
    )
    
    text = "This movie is fantastic!"
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    
    print("Attention shape:", outputs.attentions[0].shape)
    print("Prediction:", model(**inputs).logits)

**Résultat** :

.. code-block:: text

    Attention shape: torch.Size([1, 12, 9, 9])
    Prediction: tensor([[-4.2367, 4.5634]])

Exemple : extraction des poids d'attention affichée ci-dessus.

---

Première Question : Par Où Commencer ?
======================================

**Si vous souhaitez voir rapidement les résultats**

→ Accédez à **Section 5 : Expériences & Visualisations**

Vous verrez les résultats maintenant. Revenez ensuite aux sections 1-4 pour le contexte détaillé.

---

**Si vous aimez construire les fondations** 🏗

→ Commencez par **Section 1 : Contexte & Motivation**

Progressez linéairement. C'est plus logique et plus complet.

---

**Si vous avez des questions spécifiques**

→ Consultez la **FAQ**

La FAQ couvre les questions les plus fréquentes.

---

Prochaines Étapes
=================

Une fois que vous avez parcouru cette page :

1. **Choisissez votre parcours** selon votre profil ci-dessus
2. **Rendez-vous à l'Index** pour naviguer
3. **Consultez le Glossaire** si vous êtes bloquée/bloqué sur un terme
4. **Exécutez le Notebook** pour expérimenter
5. **Partagez vos questions** via Issues ou Discussions

---

Ressources Rapides
==================

.. list-table::
   :header-rows: 1

   * - Ressource
     - Accès
   * - **Index principal**
     - Lien dans le menu
   * - **Glossaire**
     - Lien dans le menu
   * - **FAQ**
     - Lien dans le menu
   * - **Notebook Jupyter**
     - Fichier `Projet7_Attention_Not_Explanation.ipynb`
   * - **Source .rst**
     - Dossier `docs/source/`

---

Aide et Support
===============

Coincée/Coincé ? Besoin d'aide ?

- **Question conceptuelle** → FAQ ou Glossaire
- **Bug de code** → Notebook `4_implementation_pratique.rst`
- **Question scientifique** → Section `6_discussion_critique.rst`
- **Problème technique** → README.md ou Issues GitHub

---

Démarrage
=========

Vous pouvez désormais parcourir la documentation selon votre rythme.

N'hésitez pas à poser des questions via les issues ou discussions du dépôt.

Bonne lecture.

---

*Dernière mise à jour : Décembre 2025*
