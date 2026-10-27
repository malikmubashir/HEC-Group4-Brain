# Outils de régénération

- `build_model.py` : reconstruit le classeur `Finance/Helium_Modele_financier_36m_V1.xlsx` (Python 3, openpyxl). Modifier les hypothèses dans la liste `ASSUMPTIONS`, exécuter, puis ouvrir dans Excel (recalcul automatique) ou recalculer avec LibreOffice.
- `make_logo.py` : régénère les fichiers du logo dans `Marque/assets/` (Pillow ; police Caladea Bold, à remplacer par Fraunces si installée).
- `helium_brand.py` : palette et polices de la marque, importées par les deux scripts.
- `make_index.py` : régénère `index.html`, la page d'accès aux productions (Python 3, bibliothèque standard). Exécuter depuis `Outils/` ; la date figurant en pied de page se force avec la variable `INDEX_DATE=JJ/MM/AAAA`.

Les chemins de sortie en tête de chaque script sont ceux de l'environnement d'origine ; les adapter avant exécution.
