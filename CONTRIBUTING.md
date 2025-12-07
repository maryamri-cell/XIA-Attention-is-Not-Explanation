# Directives de Contribution

Merci d'être intéressé(e) par la contribution à ce projet ! 🎉

Ce document fournit des directives et des instructions pour contribuer.

---

## Valeurs du Projet

Nous valorisons :

- **Rigueur scientifique** : Preuves empiriques et citations appropriées
- **Clarté** : Documentation lisible et accessible
- **Reproductibilité** : Code exécutable et résultats vérifiables
- **Inclusivité** : Bienvenue à toute personne intéressée par l'XAI
- **Ouverture** : Critique constructive et amélioration continue

---

## Types de Contributions

### 1. Corrections (Facile) ✅

**Typos, formulations, clarifications** dans la documentation.

**Exemple** : "L'atention" → "L'attention"

**Comment** :
1. Identifier le problème
2. Créer une issue ou un PR
3. Proposer la correction

**Priorité** : Haute (corriger rapidement)

---

### 2. Amélioration de Documentation (Moyen) 📚

**Nouvelles sections, exemples additionnels, clarifications**.

**Exemple** : Ajouter un diagramme pour la Section 2

**Comment** :
1. Proposer dans une issue
2. Discuter avec les mainteneurs
3. Implémenter avec exemples

**Priorité** : Moyenne (amélioration continue)

---

### 3. Implémentation de Fonctionnalités (Difficile) 🚀

**Nouvelles expériences, nouveaux modèles, extensions**.

**Exemple** : Ajouter le support pour RoBERTa

**Comment** :
1. Créer une issue de feature
2. Obtenir l'approbation des mainteneurs
3. Implémenter avec tests

**Priorité** : Basse (long terme)

---

## Processus de Contribution

### Étape 1 : Forker le Repository

```bash
# Sur GitHub, cliquez "Fork"
```

### Étape 2 : Cloner Localement

```bash
git clone https://github.com/[votre-username]/read-the-doc.git
cd read-the-doc
```

### Étape 3 : Créer une Branche

```bash
# Pour les corrections
git checkout -b fix/description

# Pour les features
git checkout -b feature/description

# Pour la documentation
git checkout -b docs/description
```

### Étape 4 : Faire les Changements

```bash
# Éditer les fichiers
# Tester localement
```

### Étape 5 : Commit

```bash
git add .
git commit -m "Type: Description claire"
```

**Formats de message recommandés** :

```
fix: Corriger typo dans section 1
feat: Ajouter support pour RoBERTa
docs: Améliorer glossaire
refactor: Restructurer conf.py
test: Ajouter test pour attention
```

### Étape 6 : Push

```bash
git push origin [votre-branche]
```

### Étape 7 : Créer une Pull Request

1. Aller sur GitHub
2. Cliquer "Compare & pull request"
3. Remplir le template
4. Soumettre

---

## Standards de Qualité

### Documentation (.rst)

- Vérifier la syntaxe : `sphinx-build -b html -W docs/source docs/build/html`
- Respecter la structure des sections
- Utiliser des citations appropriées ([1], [2], etc.)
- Ajouter des références à la section 8

**Checklist** :

```
- [ ] Pas de typos
- [ ] Syntaxe .rst valide
- [ ] Formules LaTeX correctes
- [ ] Liens internes fonctionnels
- [ ] Citations complètes
```

### Code Python

- Style : PEP 8
- Type hints recommandés
- Docstrings en Google/NumPy format
- Tests pour les nouvelles fonctions

**Checklist** :

```
- [ ] Code testé
- [ ] Pas d'erreurs pylint/flake8
- [ ] Docstrings complètes
- [ ] Exemple d'utilisation
```

### Jupyter Notebooks

- Exécutable sans erreurs
- Commentaires clairs
- Outputs nettoyés avant commit
- Version reproductible

**Tools** :

```bash
# Nettoyer les outputs
nbstripout notebook.ipynb

# Vérifier la syntaxe
jupyter nbconvert --to script notebook.ipynb
```

---

## Template de Pull Request

```markdown
## Description
Brève description des changements.

## Motivation
Pourquoi cette contribution est-elle importante ?

## Type de changement
- [ ] Correction de bug
- [ ] Nouvelle feature
- [ ] Amélioration documentation
- [ ] Refactoring
- [ ] Autre

## Checklist
- [ ] J'ai lu le CONTRIBUTING.md
- [ ] Mon code respecte les standards
- [ ] J'ai ajouté des tests/exemples
- [ ] J'ai mis à jour la documentation
- [ ] Pas de breaking changes (ou documenté)

## Screenshots (si applicable)
Insérer des images de changements visuels.

## Références
Lier les issues corrigées ou liées : fixes #123
```

---

## Template de Issue

```markdown
## Description
Décrire le problème ou la suggestion.

## Contexte
- Version Python utilisée
- OS (macOS/Windows/Linux)
- Version du projet

## Étapes pour Reproduire (si bug)
1. Faire X
2. Puis faire Y
3. Erreur : Z

## Comportement Attendu
Décrire ce qui devrait se passer.

## Comportement Actuel
Décrire ce qui se passe réellement.

## Screenshots (si applicable)
```

---

## Directives pour les Types de Contributions

### Corrections Orthographe/Typos

**Priorité** : Immédiate  
**Processus** : PR directe bienvenue

```
fix: Corriger 'atention' → 'attention' dans section X
```

---

### Améliorations Documentation

**Priorité** : Haute  
**Processus** : Discuter en issue d'abord

**Exemples acceptés** :
- Ajouter des diagrammes/images
- Clarifier une explication
- Ajouter des exemples
- Étendre le glossaire
- Améliorer la structure

---

### Nouvelles Expériences/Résultats

**Priorité** : Moyenne  
**Processus** : Issue + discussion + PR

**Critères d'acceptation** :
- Méthodologiquement rigoureuse
- Reproductible (code fourni)
- Résultats significatifs
- Bien documentée

**Format attendu** :
- Nouvelle section ou subsection
- Code Jupyter
- Visualisations
- Analyse des résultats

---

### Support de Nouveaux Modèles

**Priorité** : Basse (long terme)  
**Processus** : Planification long terme

**Exemples** :
- BERT au lieu de DistilBERT
- RoBERTa, ELECTRA, etc.
- Modèles multilingues

**Critères** :
- Adapter le code
- Ajouter des expériences
- Mettre à jour la documentation

---

### Support de Nouvelles Tâches

**Priorité** : Basse  
**Processus** : Planification long terme

**Exemples** :
- Named Entity Recognition (NER)
- Question Answering (QA)
- Text Summarization

**Critères** :
- Adapter la méthodologie
- Nouveaux datasets
- Nouvelles analyses

---

## Questions Fréquentes pour Contributeurs

### Q: Dois-je demander permission avant de contribuer ?

R: Pour les petites corrections (typos) : non, envoyez directement un PR.
Pour les changements majeurs : créez d'abord une issue pour discuter.

---

### Q: Quelle branche dois-je utiliser ?

R: Créez une nouvelle branche avec un nom descriptif :

```
fix/typo-section1      ← pour corrections
feat/bert-support      ← pour features
docs/glossaire         ← pour doc
refactor/conf-py       ← pour refactoring
```

---

### Q: Comment tester localement ?

R: 

```bash
# Documentation
cd docs && make html && open build/html/index.html

# Notebook
jupyter notebook Projet7_Attention_Not_Explanation.ipynb

# Linting
flake8 docs/source/conf.py
pylint *.py
```

---

### Q: Combien de temps avant réponse ?

R: Nous visons :

- Typos : <24h
- Issues : <1 semaine
- PR : <2 semaines

Soyez patient(e) 🙏 (projet académique)

---

### Q: Et si mon PR est rejeté ?

R: C'est normal ! Les rejets arrivent pour :

- Qualité insuffisante
- Out-of-scope
- Conflicts avec direction du projet

Nous expliquerons pourquoi et comment améliorer.

---

## Code of Conduct

Nous nous engageons à maintenir un environnement accueillant.

**Comportement attendu** :

- Respecter les différentes perspectives
- Critique constructive
- Zéro tolérance pour le harcèlement
- Inclusivité pour tous

**Exemple de commentaire** :

```
✅ BON : "J'ai remarqué que cette fonction pourrait être optimisée avec..."
❌ MAUVAIS : "Ton code est nul, tu ne sais rien programmer"
```

---

## Ressources Utiles

### Outils

- **Git** : https://git-scm.com/
- **GitHub** : https://github.com/
- **Sphinx** : https://www.sphinx-doc.org/
- **VSCode** : https://code.visualstudio.com/

### Documentation

- [reStructuredText](https://docutils.sourceforge.io/rst.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- [GitHub Guides](https://guides.github.com/)
- [Commit Message Best Practices](https://chris.beams.io/posts/git-commit/)

---

## Escalade

Si vous avez besoin d'aide :

1. **Petite question** → Commentaire sur PR/Issue
2. **Question moyenne** → Discussion GitHub
3. **Problème majeur** → Email aux mainteneurs

---

## Remerciements

Merci d'envisager de contribuer ! 🙏

Même les petites contributions (typos, suggestions) font une différence.

Bienvenue dans la communauté ! 🎉

---

**Dernière mise à jour** : Décembre 2025  
**Mainteneur** : [Nom Étudiant]
