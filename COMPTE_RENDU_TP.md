# Compte rendu — TP CI/CD Databricks, GitHub Actions et MLflow

**Étudiant :** Karl  
**Date :** 5 novembre 2026  
**Dépôt :** https://github.com/karl9722/databricks-ci-cd-example

## 1. Objectif
Mettre en place une chaîne CI/CD pour un projet de machine learning : versionnement Git, tests Pytest, entraînement Random Forest sur Iris, suivi et enregistrement du modèle MLflow, déclenchement d'un job Databricks depuis GitHub Actions.

## 2. Organisation du dépôt
- `notebooks/train_model.py` : entraînement et journalisation MLflow.
- `tests/test_train_model.py` : tests unitaires.
- `.github/workflows/ci_cd_pipeline.yml` : pipeline GitHub Actions.
- `requirements.txt` : dépendances.
- `README.md` : présentation.

## 3. Réalisation et résultats
- **Pytest :** 2 tests réussis en local.
- **MLflow :** modèle `workspace.default.irisrfmodel` enregistré dans Unity Catalog ; cinq versions visibles lors du contrôle.
- **GitHub Actions :** étapes `test` et `deploy` réussies ; workflow de correction MLflow au commit `9506acd` également réussi.
- **Databricks :** Git folder lié à GitHub, branche `main` ; job `iris-model-training` (ID `1062094326477269`) configuré pour exécuter `notebooks/train_model.py` depuis Git avec Serverless.

## 4. Incidents et corrections
1. `GIT_UNKNOWN_REF` : la référence de branche était vide ; correction en `main`.
2. `Could not find experiment with ID None` : ajout d'une expérience MLflow explicite dans le script puis push sur GitHub.

## 5. Validation finale — 5 novembre 2026
L'historique Databricks montre deux exécutions récentes du job `iris-model-training` avec le statut **Succeeded** :
- **12 h 19 :** Succeeded, durée 37 s.
- **12 h 24 :** Succeeded, durée 36 s.

Ces deux exécutions sont indiquées **Manually** dans Databricks. Elles valident l'exécution du job avec la nouvelle configuration Git, mais ne prouvent pas à elles seules que le déclenchement GitHub Actions s'est terminé avec succès dans Databricks.

## 6. Captures d'écran
Le compte rendu PDF remis avec le TP contient huit captures illustrant le Git folder, le code, MLflow, GitHub Actions, la configuration du job, les erreurs corrigées et les deux dernières exécutions réussies.

## Conclusion
Le TP a permis de mettre en place et de tester une chaîne CI/CD GitHub Actions–Databricks–MLflow. Les tests GitHub Actions sont verts et les deux dernières exécutions manuelles du job Databricks ont réussi.
