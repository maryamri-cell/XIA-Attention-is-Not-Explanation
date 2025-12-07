# Changelog

Tous les changements notables de ce projet sont documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet suit [Semantic Versioning](https://semver.org/lang/fr/).

---

## [1.0] - 2025-12-01

### Ajouté (Added)

- **Documentation Read the Docs complète**
  - 8 sections principales couvrant l'étude complète
  - Glossaire avec 50+ termes
  - FAQ avec 30+ questions

- **Structure Sphinx**
  - Configuration complète (conf.py)
  - Theme "Read the Docs" installé
  - Support HTML, PDF, ePub

- **Fichiers de Support**
  - README.md : Vue générale du projet
  - INSTALL.md : Guide installation détaillé
  - .readthedocs.yml : Configuration pour ReadTheDocs.org
  - .github/workflows/build-docs.yml : CI/CD avec GitHub Actions

- **Sections Documentées**
  1. Contexte & Motivation (débat Jain vs Wiegreffe)
  2. Intuition de la Méthode (explication conceptuelle)
  3. Formalisation Mathématique (équations et métriques)
  4. Implémentation Pratique (code et setup)
  5. Expériences & Visualisations (résultats empiriques)
  6. Discussion Critique (forces et limitations)
  7. Conclusion & Points Clés (synthèse)
  8. Références (12+ articles majeurs)

- **Ressources Complémentaires**
  - Glossaire technique complet
  - FAQ avec questions pratiques
  - Guide de démarrage rapide
  - Ressources externes et liens

- **Qualité**
  - Tous les liens internes fonctionnels
  - Formules mathématiques en LaTeX
  - Tableaux et visualisations intégrés
  - Code Python exemple exécutable

### Modifié (Changed)

- N/A (première version stable)

### Supprimé (Removed)

- N/A

### Corrigé (Fixed)

- N/A

### Dépendances

- sphinx >= 4.5.0
- sphinx-rtd-theme >= 1.0.0
- PyTorch >= 1.9
- Transformers >= 4.0
- LIME >= 0.2
- SHAP >= 0.40

---

## Plans Futurs

### v1.1 (Prévu Q1 2026)
- [ ] Ajouter des images/diagrammes (SVG)
- [ ] Exécutable Binder pour notebook
- [ ] Support multilingue (FR, ES, DE)
- [ ] Videos tutorielles

### v1.2 (Prévu Q2 2026)
- [ ] Extension à d'autres modèles (BERT, RoBERTa, GPT)
- [ ] Extension à d'autres tâches (NER, QA)
- [ ] Comparaison avec autres méthodes XAI (gradients, integrated gradients)
- [ ] Benchmark sur datets plus grands

### v2.0 (Prévu Q4 2026)
- [ ] Interactive dashboard (Streamlit)
- [ ] Paper scientifique soumis à conférence
- [ ] Open-source package PyPI
- [ ] Support académique complet

---

## Notes de Version

### 1.0 - Release Initiale

Cette version représente une documentation complète et stable du mini-projet XAI.

**Statut** : Production-ready ✅

**Points Forts** :
- Documentation exhaustive
- Code reproductible
- Installation facile
- Guide utilisateur complet

**Limitations Connues** :
- Petite taille d'échantillon (n=7 phrases)
- Seulement en anglais (SST-2)
- Seulement DistilBERT
- Seulement sentiment analysis

**Prochaines Étapes** :
- Tester sur d'autres modèles
- Étendre à d'autres langues
- Augmenter la taille de l'étude

---

## Comment Contribuer

Les contributions sont bienvenues !

### Types de Contributions Acceptées

- **Corrections** : Typos, formulations, clarifications
- **Extensions** : Nouvelles sections, expériences
- **Code** : Améliorations d'implémentation
- **Traductions** : Autres langues
- **Issues** : Rapporter des bugs

### Processus

1. Fork le repository
2. Créer une branche (`git checkout -b feature/...`)
3. Commit les changes (`git commit -m 'Ajout de...'`)
4. Push vers la branche (`git push origin feature/...`)
5. Créer une Pull Request

### Standards de Qualité

- Code testé
- Documentation mise à jour
- Messages de commit clairs
- Respect du style existant

---

## Versioning

Ce projet suit [Semantic Versioning](https://semver.org/) :

**Format** : MAJOR.MINOR.PATCH

- **MAJOR** : Changement incompatible (nouvelle structure, nouvelle API)
- **MINOR** : Nouvelle fonctionnalité compatible
- **PATCH** : Correction de bug

**Exemple** :
- v1.0.0 : Release initiale
- v1.0.1 : Correction d'une typo
- v1.1.0 : Ajout d'une nouvelle section
- v2.0.0 : Restructuration complète

---

## Archive des Versions

### v1.0 (2025-12-01)
- Release initiale
- Documentation complète
- 8 sections + Glossaire + FAQ
- Code reproductible

---

## Auteurs & Remerciements

**Auteurs** :
- [Nom Étudiant 1]
- [Nom Étudiant 2]

**Contribution** :
- Direction : [Professeur/Advisor]
- Révision : [Peer reviewers]

**Remerciements à** :
- Jain & Wallace (2019) pour avoir soulevé la question
- Wiegreffe & Pinter (2019) pour le débat nuancé
- HuggingFace pour les outils
- La communauté NLP/XAI

---

## Licence

Ce projet est sous licence **MIT**.

Voir `LICENSE` pour plus de détails.

---

## Support & Contact

- **Issues** : GitHub Issues
- **Discussions** : GitHub Discussions
- **Email** : [contact-email]
- **Website** : [projet-url]

---

**Dernière mise à jour** : 2025-12-01  
**Mainteneur** : [Nom Étudiant]  
**Status** : ✅ Actif et maintenu
