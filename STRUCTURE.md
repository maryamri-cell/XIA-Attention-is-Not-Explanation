# Structure du Projet

Guide complet de l'organisation des fichiers et dossiers.

---

## Vue d'Ensemble

```
read-the-doc/
├── 📓 Projet7_Attention_Not_Explanation.ipynb  ← Notebook source (le cœur)
├── 📖 README.md                                ← Vue générale (LIRE D'ABORD)
├── 📚 INSTALL.md                              ← Guide installation
├── 🤝 CONTRIBUTING.md                         ← Directives contribution
├── 📝 CHANGELOG.md                            ← Historique versions
├── ⚖️ LICENSE                                  ← MIT License
├── 📋 STRUCTURE.md                            ← Ce fichier
│
├── 📁 docs/                                   ← **Documentation Sphinx**
│   ├── Makefile                               ← Build script (Unix)
│   ├── requirements.txt                       ← Dépendances Sphinx
│   ├── build/                                 ← Output HTML/PDF (generated)
│   │   ├── html/                              ← Pages HTML (consulter dans navigateur)
│   │   ├── pdf/                               ← PDFs (si généré)
│   │   └── ...
│   │
│   └── source/                                ← **Fichiers source .rst**
│       ├── conf.py                            ← Configuration Sphinx
│       ├── index.rst                          ← Page d'accueil
│       ├── GETTING_STARTED.rst                ← Guide démarrage rapide
│       │
│       ├── 1_contexte_motivation.rst          ← Section 1
│       ├── 2_intuition_methode.rst            ← Section 2
│       ├── 3_formalisation_mathematique.rst   ← Section 3
│       ├── 4_implementation_pratique.rst      ← Section 4
│       ├── 5_experiences_visualisations.rst   ← Section 5
│       ├── 6_discussion_critique.rst          ← Section 6
│       ├── 7_conclusion_points_cles.rst       ← Section 7
│       ├── 8_references.rst                   ← Section 8
│       │
│       ├── glossaire.rst                      ← Glossaire (50+ termes)
│       ├── faq.rst                            ← FAQ (30+ questions)
│       ├── footer.rst                         ← Pied de page
│       │
│       ├── _static/                           ← Ressources statiques (images, CSS)
│       └── _templates/                        ← Templates HTML personnalisés
│
├── 📁 .github/                                ← Configuration GitHub
│   └── workflows/
│       └── build-docs.yml                     ← CI/CD pour compiler docs
│
├── .gitignore                                 ← Fichiers à ignorer par Git
└── .readthedocs.yml                           ← Configuration ReadTheDocs.org
```

---

## Fichiers Racine

### Fichiers Principaux

| Fichier | Purpose | À Lire |
|---------|---------|--------|
| `README.md` | Vue générale du projet | ✅ COMMENCER ICI |
| `INSTALL.md` | Installation détaillée | ✅ Si problèmes d'install |
| `CONTRIBUTING.md` | Directives contribution | ✅ Si vouloir contribuer |
| `CHANGELOG.md` | Historique des versions | ⭐ Pour suivi projet |
| `LICENSE` | MIT License | ℹ️ Informations légales |
| `STRUCTURE.md` | Ce fichier | ℹ️ Organisation fichiers |

### Fichiers de Configuration

| Fichier | Purpose | Éditer ? |
|---------|---------|----------|
| `.gitignore` | Fichiers à ignorer Git | Non (standards) |
| `.readthedocs.yml` | Config ReadTheDocs | Rarement |
| `.github/workflows/` | CI/CD automatique | Non (avancé) |

---

## Notebook Jupyter

### `Projet7_Attention_Not_Explanation.ipynb`

**Le cœur du projet !**

**Contenu** :

1. **Titres et présentation** : Contexte du projet
2. **Section 1** : Contexte & Motivation
3. **Section 2** : Intuition de la Méthode
4. **Section 3** : Formalisation Mathématique
5. **Section 4** : Implémentation Pratique
   - Installation
   - Chargement modèle
   - Extraction attention
   - Configuration LIME
6. **Section 5** : Expériences & Visualisations
   - Visualisations d'attention
   - Comparaison LIME
   - Analyse corrélation
   - Cas pathologiques (négations)
7. **Section 6** : Discussion Critique
8. **Section 7** : Conclusion
9. **Section 8** : Références

**Exécuter** :

```bash
jupyter notebook Projet7_Attention_Not_Explanation.ipynb
```

**Durée** : ~20-30 minutes pour tout exécuter

---

## Documentation Sphinx

### Structure `docs/`

```
docs/
├── Makefile              # Compilation (Unix : make html)
├── requirements.txt      # Dépendances (pip install -r)
├── build/                # OUTPUT (généré, à ignorer)
└── source/               # INPUT (fichiers source)
```

### Structure `docs/source/`

#### Fichiers de Navigation

| Fichier | Role |
|---------|------|
| `index.rst` | **Page d'accueil** - point d'entrée |
| `conf.py` | Configuration Sphinx (thème, extensions, etc.) |
| `footer.rst` | Pied de page (copyrights, dates) |

#### Fichiers de Contenu Principal (8 sections)

| Fichier | Section | Sujet |
|---------|---------|-------|
| `1_contexte_motivation.rst` | 1 | Débat académique Jain vs Wiegreffe |
| `2_intuition_methode.rst` | 2 | Explication simple du problème |
| `3_formalisation_mathematique.rst` | 3 | Équations et métriques |
| `4_implementation_pratique.rst` | 4 | Code et installation |
| `5_experiences_visualisations.rst` | 5 | Résultats empiriques |
| `6_discussion_critique.rst` | 6 | Avantages et limitations |
| `7_conclusion_points_cles.rst` | 7 | Synthèse et recommendations |
| `8_references.rst` | 8 | Bibliographie (12+ articles) |

#### Fichiers Complémentaires

| Fichier | Contenu |
|---------|---------|
| `GETTING_STARTED.rst` | Guide démarrage rapide |
| `glossaire.rst` | Glossaire (50+ termes) |
| `faq.rst` | FAQ (30+ questions) |

#### Dossiers Spéciaux

| Dossier | Usage |
|---------|-------|
| `_static/` | Images, CSS, JavaScript |
| `_templates/` | Templates HTML personnalisés |

### Comment Compiler la Documentation

```bash
cd docs

# Option 1 : Unix (macOS, Linux)
make html          # Compile en HTML
make clean         # Nettoie les builds précédents
make pdf           # Compile en PDF (requiert LaTeX)

# Option 2 : Windows (sans make)
sphinx-build -b html source build/html

# Ouvrir le résultat
open build/html/index.html  # macOS
start build\html\index.html # Windows
xdg-open build/html/index.html # Linux
```

---

## Configuration Sphinx

### `conf.py` - Configuration Sphinx

**Éléments clés** :

```python
project = 'XAI Mini-Projet...'
extensions = ['sphinx_rtd_theme', 'sphinx.ext.mathjax', ...]
html_theme = 'sphinx_rtd_theme'
master_doc = 'index'
```

**À modifier si** :

- Changer le nom du projet
- Ajouter des extensions Sphinx
- Changer le thème (couleurs, fonts)

---

## Dépendances et Installation

### `requirements.txt` (Sphinx)

Fichier de dépendances pour la compilation de la documentation :

```
sphinx>=4.5.0
sphinx-rtd-theme>=1.0.0
...
```

**Installation** :

```bash
pip install -r docs/requirements.txt
```

### Installation Notebook

Les dépendances du notebook (PyTorch, Transformers, etc.) sont **séparées** :

```bash
pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy
```

---

## GitHub & CI/CD

### `.github/workflows/build-docs.yml`

**Automatise la compilation** de la documentation à chaque push :

1. Checkout du code
2. Installation de Python 3.10
3. Installation des dépendances
4. Compilation Sphinx
5. Upload de l'artifact

**Résultat** : Les docs sont compilées automatiquement à chaque changement.

### `.readthedocs.yml`

Configuration pour **ReadTheDocs.org** (hébergement gratuit de docs) :

```yaml
version: 2
python:
  version: 3.10
  install:
    - requirements: docs/requirements.txt
```

**Avantage** : Deploy automatique sur readthedocs.org

---

## Navigation et Liens

### Structure Logique

```
Index (page d'accueil)
├── Getting Started (démarrage rapide)
├── Section 1-8 (contenu principal)
└── Glossaire + FAQ (référence)
```

### Liens Internes

Les fichiers .rst utilisent les références Sphinx :

```rst
.. _nom-reference:

Titre Section
=============

Voir aussi :ref:`autre-reference`
```

---

## Règles de Nommage

### Fichiers .rst

```
{numero}_{titre_slug}.rst

Exemples:
✓ 1_contexte_motivation.rst
✓ 2_intuition_methode.rst
✓ glossaire.rst
✓ faq.rst
```

### Sections Python (Notebook)

```
# === Section Name ===
print("=" * 60)
```

### Branches Git

```
{type}/{description}

Exemples:
✓ fix/typo-section1
✓ feat/bert-support
✓ docs/glossaire
```

---

## Standards de Qualité

### Documentation

- ✓ Syntaxe .rst valide
- ✓ Pas de liens cassés
- ✓ Formules LaTeX correctes
- ✓ Numérotation cohérente

**Vérifier** :

```bash
cd docs
sphinx-build -b html -W source build/html
# -W traite les warnings comme erreurs
```

### Code Python

- ✓ PEP 8 compliant
- ✓ Type hints
- ✓ Docstrings
- ✓ Tests

**Vérifier** :

```bash
flake8 Projet7_Attention_Not_Explanation.ipynb
pylint *.py
```

---

## Génération de Fichiers

### À ne PAS commiter

```
docs/build/          ← HTML/PDF généré (trop gros)
__pycache__/         ← Cache Python
.ipynb_checkpoints/  ← Cache Jupyter
*.egg-info/          ← Info paquetage
```

Voir `.gitignore` pour la liste complète.

---

## Arborescence Complète (Étendue)

```
read-the-doc/
├── 📓 Jupyter Notebook
│   └── Projet7_Attention_Not_Explanation.ipynb
│
├── 📖 Root Documentation
│   ├── README.md                    (Vue générale)
│   ├── INSTALL.md                   (Installation)
│   ├── CONTRIBUTING.md              (Contribution)
│   ├── CHANGELOG.md                 (Historique)
│   ├── LICENSE                      (MIT)
│   ├── STRUCTURE.md                 (Ce fichier)
│   ├── .gitignore
│   ├── .readthedocs.yml
│   └── .github/
│       └── workflows/
│           └── build-docs.yml
│
└── 📁 docs/
    ├── Makefile                     (Build script)
    ├── requirements.txt             (Dépendances Sphinx)
    │
    ├── build/                       (OUTPUT - généré)
    │   ├── html/                    (Pages web)
    │   │   ├── index.html
    │   │   ├── _sources/
    │   │   ├── _static/
    │   │   └── ...
    │   ├── pdf/                     (PDFs si généré)
    │   └── ...
    │
    └── source/                      (INPUT - source)
        ├── conf.py                  (Configuration Sphinx)
        ├── index.rst                (Page d'accueil)
        ├── GETTING_STARTED.rst
        │
        ├── 1_contexte_motivation.rst
        ├── 2_intuition_methode.rst
        ├── 3_formalisation_mathematique.rst
        ├── 4_implementation_pratique.rst
        ├── 5_experiences_visualisations.rst
        ├── 6_discussion_critique.rst
        ├── 7_conclusion_points_cles.rst
        ├── 8_references.rst
        │
        ├── glossaire.rst
        ├── faq.rst
        ├── footer.rst
        │
        ├── _static/                 (Ressources statiques)
        │   ├── logo.png
        │   ├── style.css
        │   └── ...
        │
        └── _templates/              (Templates personnalisés)
            └── layout.html
```

---

## Cas d'Usage Courants

### Je veux lire la documentation

```bash
# Option 1 : Web
open https://read-the-doc.readthedocs.io

# Option 2 : Localement (après make html)
open docs/build/html/index.html

# Option 3 : Texte brut
cat docs/source/1_contexte_motivation.rst
```

---

### Je veux contribuer

```bash
git clone https://github.com/[repo].git
cd read-the-doc

# Créer une branche
git checkout -b fix/typo-section1

# Éditer les fichiers
# Tester localement
cd docs && make html

# Commit et push
git add .
git commit -m "fix: Corriger typo section 1"
git push origin fix/typo-section1

# Créer un PR sur GitHub
```

---

### Je veux ajouter une nouvelle section

```bash
# 1. Créer le fichier
touch docs/source/9_section_nouvelle.rst

# 2. Ajouter au index.rst
nano docs/source/index.rst
# ↓ Ajouter: 9_section_nouvelle

# 3. Remplir le contenu
nano docs/source/9_section_nouvelle.rst

# 4. Compiler
cd docs && make html

# 5. Vérifier
open build/html/index.html
```

---

## Maintenance

### Tâches Régulières

- **Mensuel** : Vérifier les liens
- **Trimestriel** : Mettre à jour les dépendances
- **Annuel** : Réviser le contenu principal

### Mises à Jour

```bash
# Mettre à jour Sphinx
pip install --upgrade sphinx sphinx-rtd-theme

# Mettre à jour dépendances du notebook
pip install --upgrade torch transformers lime shap
```

---

## Références

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [reStructuredText Primer](https://docutils.sourceforge.io/rst.html)
- [ReadTheDocs Guide](https://docs.readthedocs.io/)
- [Git Best Practices](https://github.com/git-tips/tips)

---

**Dernière mise à jour** : Décembre 2025  
**Mainteneur** : [Nom Étudiant]
