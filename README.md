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

Plus : **Glossaire** et **FAQ**

## ⚡ Résumé Exécutif

### Résultat Principal
Corrélation de Spearman moyenne entre **Attention** et **LIME** = **0.31**

Cela indique une **corrélation faible**, insuffisante pour garantir que l'attention seule constitue une explication fiable.

### Conclusions
- ✓ L'attention offre des insights utiles pour l'exploration
- ✗ L'attention n'est pas une explication causale  
- ⚠ L'attention échoue systématiquement sur les négations
- ✓ Valider avec LIME/SHAP avant utilisation en production

## 🚀 Comment Accéder à la Documentation

### Option 1 : Construire localement avec Sphinx

```bash
# 1. Installer les dépendances
cd docs
pip install -r requirements.txt

# 2. Construire HTML
make html

# 3. Ouvrir dans le navigateur
open build/html/index.html  # macOS/Linux
start build\html\index.html # Windows
```

### Option 2 : Lire les fichiers .rst directement

```bash
# Les fichiers source sont dans docs/source/
cat docs/source/1_contexte_motivation.rst
cat docs/source/2_intuition_methode.rst
# etc.
```

### Option 3 : Déployer sur ReadTheDocs.org

1. Forker le repo
2. Créer compte sur https://readthedocs.org
3. Importer le projet
4. ReadTheDocs construit automatiquement

## 📊 Structure des Fichiers

```
read-the-doc/
├── Projet7_Attention_Not_Explanation.ipynb  ← Notebook source
├── README.md                                 ← Ce fichier
└── docs/
    ├── requirements.txt                      ← Dépendances Sphinx
    └── source/
        ├── conf.py                           ← Configuration Sphinx
        ├── index.rst                         ← Page d'accueil
        ├── 1_contexte_motivation.rst
        ├── 2_intuition_methode.rst
        ├── 3_formalisation_mathematique.rst
        ├── 4_implementation_pratique.rst
        ├── 5_experiences_visualisations.rst
        ├── 6_discussion_critique.rst
        ├── 7_conclusion_points_cles.rst
        ├── 8_references.rst
        ├── glossaire.rst
        ├── faq.rst
        ├── footer.rst
        ├── _static/                         ← Ressources statiques
        └── _templates/                      ← Templates HTML
```

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

## 🤝 Contribution

Les contributions sont bienvenues !

- **Corrections** : Typos, formulations, code
- **Extensions** : Nouveaux cas d'étude, langues, modèles
- **Discussions** : Issues et discussions GitHub

## 📄 Licence

Libre d'usage pour fins **éducatives et de recherche**.

Citation recommandée :
```bibtex
@misc{XAIAttentionProject2025,
  title={Mini-Projet XAI: Attention is Not Explanation},
  author={[Vos noms]},
  year={2025},
  institution={[Votre institution]},
  url={https://[votre-repo]}
}
```

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

## 📞 Support

- **Issues** : GitHub Issues (ce repo)
- **Discussions** : GitHub Discussions
- **Email** : [contact des auteurs]

## 🎉 Remerciements

Merci à :
- Jain & Wallace pour avoir soulevé la question
- Wiegreffe & Pinter pour avoir nuancé le débat
- La communauté NLP/XAI pour les discussions continues

---

**Dernière mise à jour** : Décembre 2025  
**Version** : 1.0  
**Statut** : Complet et reproductible
