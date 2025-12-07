# Installation & Setup Guide

Guide complet pour installer et configurer la documentation et le notebook.

## Table des Matières

1. [Installation Rapide (2 min)](#installation-rapide)
2. [Installation Complète (5-10 min)](#installation-complète)
3. [Vérification](#vérification)
4. [Dépannage](#dépannage)

---

## Installation Rapide

Pour les impatients qui veulent juste lancer le notebook :

### Étape 1 : Installer Python

Vérifiez que Python 3.8+ est installé :

```bash
python --version
# Devrait afficher : Python 3.x.x (x >= 8)
```

Si absent, télécharger de https://www.python.org/

### Étape 2 : Installer les Dépendances

```bash
pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy
```

### Étape 3 : Lancer le Notebook

```bash
# Installer Jupyter
pip install jupyter

# Lancer
jupyter notebook

# Ouvrir Projet7_Attention_Not_Explanation.ipynb
```

**Durée totale : 5-10 minutes**

---

## Installation Complète

Pour avoir l'expérience complète avec la documentation HTML.

### Étape 1 : Cloner le Repository

```bash
# Via HTTPS
git clone https://[votre-repo-url].git
cd read-the-doc

# Ou via SSH
git clone git@github.com:[votre-repo].git
cd read-the-doc
```

### Étape 2 : Créer un Environnement Virtual (Recommandé)

```bash
# Sur macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Sur Windows
python -m venv venv
venv\Scripts\activate
```

### Étape 3 : Mettre à Jour pip

```bash
pip install --upgrade pip setuptools wheel
```

### Étape 4 : Installer les Dépendances Notebook

```bash
pip install torch transformers lime shap matplotlib seaborn pandas numpy scipy jupyter
```

### Étape 5 : Installer les Dépendances Documentation

```bash
cd docs
pip install -r requirements.txt
cd ..
```

### Étape 6 : Construire la Documentation

```bash
cd docs
make html

# Sur Windows (sans Makefile) :
cd source
sphinx-build -b html . ../build/html
cd ../..
```

### Étape 7 : Ouvrir la Documentation

```bash
# macOS/Linux
open docs/build/html/index.html

# Windows
start docs\build\html\index.html

# Linux (générique)
xdg-open docs/build/html/index.html
```

### Étape 8 : Lancer le Notebook (Optionnel)

```bash
jupyter notebook Projet7_Attention_Not_Explanation.ipynb
```

---

## Vérification

Confirmez que tout fonctionne :

### Vérifier Python

```bash
python --version
# ✓ Devrait afficher Python 3.8+
```

### Vérifier pip

```bash
pip --version
# ✓ Devrait afficher pip 20.0+
```

### Vérifier les Imports Principaux

```bash
python -c "
import torch
import transformers
import shap
import lime
import matplotlib
import pandas
print('✓ Tous les imports sont OK !')
"
```

### Vérifier Sphinx

```bash
cd docs
sphinx-build --version
# ✓ Devrait afficher sphinx-build X.X.X
```

### Vérifier la Documentation

Accédez à `docs/build/html/index.html` dans votre navigateur.

Vous devriez voir la page d'accueil de la documentation avec le logo et les sections.

---

## Dépannage

### Erreur : "Python not found"

**Cause** : Python n'est pas installé ou pas dans le PATH.

**Solution** :

1. Télécharger Python depuis https://www.python.org/
2. Lors de l'installation, cocher "Add Python to PATH"
3. Redémarrer le terminal/l'IDE
4. Réessayer

---

### Erreur : "pip: command not found"

**Cause** : pip n'est pas installé ou pas accessible.

**Solution** :

```bash
# Réinstaller pip
python -m pip install --upgrade pip

# Puis utiliser :
python -m pip install [package]
# Au lieu de :
pip install [package]
```

---

### Erreur : "No module named 'torch'"

**Cause** : PyTorch n'est pas installé.

**Solution** :

```bash
pip install torch
# Ou (pour une version spécifique) :
pip install torch==1.12.0
```

---

### Erreur : "No module named 'sphinx'"

**Cause** : Sphinx n'est pas installé.

**Solution** :

```bash
cd docs
pip install -r requirements.txt
```

---

### Erreur : "ModuleNotFoundError: No module named 'transformers'"

**Cause** : HuggingFace Transformers n'est pas installé.

**Solution** :

```bash
pip install transformers
# Ou avec version spécifique :
pip install transformers==4.25.0
```

---

### Documentation HTML ne s'ouvre pas

**Cause** : Le chemin est incorrect ou le build a échoué.

**Solution** :

```bash
# Reconstruire
cd docs
make clean
make html

# Vérifier le dossier build
ls -la build/html/
# ✓ Devrait contenir index.html
```

---

### Notebook Jupyter ne lance pas

**Cause** : Jupyter n'est pas installé ou le port est occupé.

**Solution** :

```bash
# Installer/réinstaller
pip install jupyter --upgrade

# Lancer sur un port spécifique
jupyter notebook --port 8888 Projet7_Attention_Not_Explanation.ipynb

# Ou utiliser JupyterLab (alternatif)
pip install jupyterlab
jupyter lab
```

---

### Modèle DistilBERT ne télécharge pas

**Cause** : Connexion internet manquante ou HuggingFace hub inaccessible.

**Solution** :

```bash
# Télécharger manuellement
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = AutoModel.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Les fichiers seront cachés dans ~/.cache/huggingface/
```

---

### La compilation Sphinx échoue

**Cause** : Syntax error dans les fichiers .rst ou dépendance manquante.

**Solution** :

```bash
# Vérifier les erreurs
cd docs
sphinx-build -b html -W . build/html

# -W traite les warnings comme erreurs pour identifier le problème

# Installer les dépendances manquantes
pip install sphinx-rtd-theme sphinx-autodoc-typehints
```

---

### Sur Windows : "make: command not found"

**Cause** : make n'est pas disponible sur Windows.

**Solution** :

```bash
# Utiliser sphinx-build directement
cd docs/source
sphinx-build -b html . ../build/html

# Ou installer GNU make :
# Via Chocolatey : choco install make
# Via MinGW : installer mingw et ajouter au PATH
```

---

### Erreurs d'import au lancement du notebook

**Cause** : L'environnement Python du notebook n'est pas le bon.

**Solution** :

```bash
# Vérifier l'environnement
jupyter kernelspec list

# Installer/utiliser le kernel courant
python -m ipykernel install --user --name venv

# Puis sélectionner le kernel "venv" dans Jupyter
```

---

## Installations Optionnelles

### GPU Support (pour accélérer les calculs)

```bash
# CUDA 11.8 (si vous avez une GPU NVIDIA)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Outils Additionnels

```bash
# Pour les visualisations avancées
pip install plotly bokeh

# Pour les notebooks interactifs
pip install ipywidgets

# Pour la gestion de notebook
pip install nbstripout  # Nettoyer les outputs avant commit
```

### IDE/Éditeur Recommandés

- **VSCode** : https://code.visualstudio.com/ (recommandé pour cette doc)
- **PyCharm** : https://www.jetbrains.com/pycharm/
- **Jupyter Lab** : `pip install jupyterlab` (amélioration de Jupyter Notebook)
- **Google Colab** : https://colab.research.google.com/ (cloud, gratuit)

---

## Vérification Finale

Une fois tout installé, exécutez ce script pour confirmer :

```bash
python -c "
import sys
import torch
import transformers
import shap
import lime
import matplotlib
import pandas
import numpy
import scipy
import jupyter

print('✓ Python version:', sys.version.split()[0])
print('✓ PyTorch version:', torch.__version__)
print('✓ Transformers version:', transformers.__version__)
print('✓ SHAP version:', shap.__version__)
print('✓ LIME version:', lime.__version__)
print('✓ Matplotlib version:', matplotlib.__version__)
print('✓ Pandas version:', pandas.__version__)
print('✓ NumPy version:', numpy.__version__)
print('✓ SciPy version:', scipy.__version__)
print('✓ Jupyter version:', jupyter.__version__)
print()
print('✅ Toutes les dépendances sont installées !')
"
```

**Résultat attendu** :

```
✓ Python version: 3.10.x
✓ PyTorch version: 2.0.x
✓ Transformers version: 4.2x.x
...
✅ Toutes les dépendances sont installées !
```

---

## Prochaines Étapes

Une fois l'installation réussie :

1. Ouvrir la documentation HTML : `docs/build/html/index.html`
2. Consulter le **Démarrage Rapide** : voir `GETTING_STARTED.rst`
3. Exécuter le notebook : `jupyter notebook Projet7_Attention_Not_Explanation.ipynb`
4. Lire les sections selon votre intérêt

---

## Support

Si vous avez des problèmes d'installation :

- **README.md** : Vue générale du projet
- **FAQ** : Questions courantes (dans la doc)
- **GitHub Issues** : Signaler un bug
- **Email** : Contacter les auteurs

---

**Dernière mise à jour** : Décembre 2025  
**Version** : 1.0  
**Testé sur** : Python 3.8-3.11, macOS/Linux/Windows
