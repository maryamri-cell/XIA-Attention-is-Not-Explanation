# XAI Mini-Projet : Attention is Not Explanation - Read the Docs

Documentation complète basée sur le notebook Jupyter `Projet7_Attention_Not_Explanation.ipynb`.

## 📚 À Propos

Ce projet est une étude empirique combinant recherche académique et implémentation pratique pour répondre à une question fondamentale en explicabilité de l'IA :

**Les poids d'attention des Transformers constituent-ils de véritables explications des décisions du modèle ?**

## 🎯 Contenu

La documentation est organisée en 8 sections principales :

1. **Contexte & Motivation** - Débat scientifique entre Jain & Wallace (2019) et Wiegreffe & Pinter (2019)
2. **Intuition de la Méthode** - Explication conceptuelle du mécanisme d'attention
3. **Formalisation Mathématique** - Équations et métriques rigoureuses
4. **Implémentation Pratique** - Guide d'installation et code reproductible
5. **Expériences & Visualisations** - Résultats empiriques et analyses
6. **Discussion Critique** - Forces, limitations et recommandations
7. **Conclusion & Points Clés** - Synthèse et implications pratiques
8. **Références** - Bibliographie complète (12+ articles majeurs)

## 🔧 Pré-requis Techniques

### Pour Jupyter (Notebook)
```bash
pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy
```

### Pour Sphinx (Documentation)
```bash
pip install sphinx sphinx-rtd-theme
```

## 📖 Lectures Recommandées

### Débutant (30 minutes)
1. Cette README
2. Section "Intuition de la Méthode" (Index → 2)
3. FAQ

### Intermédiaire (2-3 heures)
1. Sections 1-5 complètes
2. Glossaire pour clarifications
3. Références pour les articles clés

### Avancé (1 jour+)
1. Toute la documentation
2. Relire le notebook Jupyter
3. Reproduire les expériences
4. Lire les 12 articles de référence

## 🎓 Apprenants Cibles

✓ **Étudiants** en IA/ML : Comprendre XAI  
✓ **Data Scientists** : Implémenter LIME/SHAP responsablement  
✓ **Chercheurs** : Investiguer explicabilité de l'IA  
✓ **Product Managers** : Décider quand utiliser l'attention  
✓ **Policy Makers** : Réglementer l'IA explicable  

## 🔍 Points Clés

### Forces de l'Attention
- ⚡ Très rapide (gratuit à inférence)
- 🎨 Facile à visualiser et interpréter
- 🔬 Granularité détaillée (couches, têtes, tokens)
- 🧠 Révèle les patterns internes du modèle

### Limitations de l'Attention
- ❌ Non causale (observation ≠ causalité)
- 🎭 Ambiguïté multi-têtes
- 📍 Bias positionnel
- 🚫 Échoue sur les négations
- 🎪 Manipulable (permutation sans effet)

## 💡 Recommandations Pratiques

### Pipeline XAI Responsable
```
1. Extraction    → Attention + LIME + SHAP
2. Validation    → Corrélation Spearman > 0.5 ?
3. Classement    → Simple vs Complexe
4. Affichage     → Attention (simple) ou LIME/SHAP (complexe)
5. Audit         → Tests adversariaux
```

### Quand Utiliser Quoi
| Contexte | Attention | LIME | SHAP |
|----------|:---------:|:----:|:----:|
| Débugage rapide | ✓ | - | - |
| Exploration | ✓ | ✓ | - |
| Validation | - | ✓ | ✓ |
| Production sensible | - | ✓ | ✓ |
| Conformité GDPR | ⚠ | ✓ | ✓ |


## 🔗 Ressources Externes

### Articles Clés
- Jain & Wallace (2019) - "Attention is Not Explanation"
- Wiegreffe & Pinter (2019) - "Attention is Not Not Explanation"
- Vaswani et al. (2017) - "Attention is All You Need"

### Outils
- HuggingFace Transformers : https://huggingface.co/transformers/
- SHAP : https://shap.readthedocs.io/
- LIME : https://github.com/marcotcr/lime

### Cours
- Stanford CS224N : https://cs224n.stanford.edu/
- HuggingFace Course : https://huggingface.co/course


## 🎉 Remerciements

Merci à :
- Jain & Wallace pour avoir soulevé la question
- Wiegreffe & Pinter pour avoir nuancé le débat
- La communauté NLP/XAI pour les discussions continues

---

**Dernière mise à jour** : Décembre 2025  
**Version** : 1.0  
**Statut** : Complet et reproductible
