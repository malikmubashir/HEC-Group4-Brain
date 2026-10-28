#!/usr/bin/env python3
"""Génère index.html : la page d'accès aux productions Helium du 27 octobre 2026.

Usage : python3 make_index.py [dossier_des_productions] [sortie]
Par défaut : le dossier parent de ce script (Outils/..) et index.html à sa racine.

Les liens vers les documents sont absolus (GitHub) pour fonctionner depuis un clone
local comme depuis une page servie. Les images de la marque sont relatives.
"""
from __future__ import annotations

import html
import os
import sys
from datetime import date
from urllib.parse import quote

OWNER = "malikmubashir"
REPO = "HEC-Group4-Brain"
BRANCH = "main"
FOLDER = "PRODUCTIONS ASSISTANTS/2026 1027 Helium Board"

BLOB = f"https://github.com/{OWNER}/{REPO}/blob/{BRANCH}/"
RAW = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/"
TREE = f"https://github.com/{OWNER}/{REPO}/tree/{BRANCH}/"
ZIP = f"https://github.com/{OWNER}/{REPO}/archive/refs/heads/{BRANCH}.zip"
OFFICE = "https://view.officeapps.live.com/op/view.aspx?src="

# Palette Helium (helium_brand.py)
P = dict(ink="#201C19", chalk="#F7F3EC", glow="#F0916A", glow_deep="#D9734F",
         d3="#E9C46A", euc="#6B8F7A", stone="#8A8178", linen="#E4DDD2", mist="#EFE9E0")

# ---------------------------------------------------------------------------
# Contenu : un bloc par dossier, un item par fichier (chemin relatif au dossier)
# ---------------------------------------------------------------------------
SECTIONS = [
    dict(
        folder="Board", title="Board", who="Les six fondateurs",
        lead="La décision demandée au Board, en 24 diapositives.",
        items=[
            dict(path="Board/2026 1027 Helium Board deck V1.pptx",
                 name="Helium Board deck V1",
                 desc="Décision demandée, marché, modèle, économie unitaire, scénarios, options, "
                      "plan à 90 jours, risques, juridique, décisions à inscrire. 24 diapositives.",
                 time="20 min"),
        ]),
    dict(
        folder="Direction", title="Direction", who="Malik, puis le Board",
        lead="Le dossier complet derrière le deck.",
        items=[
            dict(path="Direction/2026 1027 Helium modele d affaires et etude de cas V1.docx",
                 name="Modèle d'affaires et étude de cas V1",
                 desc="Résumé exécutif ; situation, complication, question, réponse ; canvas V3 ; "
                      "position de prix ; économie unitaire ; scénarios ; options ; méthodes de succès ; "
                      "plan à 90 jours ; risques ; KPI ; gouvernance ; mémo de décision ; audit des hypothèses.",
                 time="45 min"),
        ]),
    dict(
        folder="Marketing", title="Marketing", who="Alice, Steve",
        lead="Le marché, les concurrents, les espaces blancs.",
        items=[
            dict(path="Marketing/2026 1027 Helium analyse de marche et concurrence V1.docx",
                 name="Analyse de marché et concurrence V1",
                 desc="Demande, dimensionnement, segments, chaîne de valeur, profils concurrents, "
                      "espaces blancs, war-game, durabilité de l'avantage, inconnues. 122 références.",
                 time="40 min"),
            dict(path="Marketing/2026 1027 References marche et concurrence.md",
                 name="Références marché et concurrence",
                 desc="Dossier de recherche : chaque chiffre avec son URL, sa date et sa fiabilité."),
        ]),
    dict(
        folder="Finance", title="Finance", who="Sébastien",
        lead="Le modèle à 36 mois, formules vivantes.",
        items=[
            dict(path="Finance/Helium_Modele_financier_36m_V1.xlsx",
                 name="Modèle financier 36 mois V1",
                 desc="Hypothèses par scénario, économie unitaire, trois modèles mensuels, synthèse, "
                      "tornade (11 sensibilités), KPI, plan de financement. Recalculé sans erreur. "
                      "Les cellules de choc C4 à H4 pilotent chaque scénario.",
                 time="Classeur"),
        ]),
    dict(
        folder="Technique", title="Technique", who="Sébastien, Malik, Steve, Isaac",
        lead="La réponse à la demande de cadrage Finance : architecture, coût par mission, plan et budget MVP.",
        items=[
            dict(path="Technique/2026 1028 Reponse au cadrage Produit Technique V1.docx",
                 name="Réponse au cadrage Produit et Technique V1",
                 desc="Arbitrages recommandés, périmètre MVP, architecture Lean avec alternatives, politique de validation, "
                      "coût par mission, plan de développement, risques, tableau commun, hypothèses H09 à H18.",
                 time="40 min"),
            dict(path="Technique/Helium_Cout_par_mission_V1.xlsx",
                 name="Coût par mission et plan de charge V1",
                 desc="Tarifs sourcés, paramètres par mission, synthèse par offre contre H03, sensibilité, protections, "
                      "plan de charge et budget MVP Lean et Confort, tableau commun. Formules vivantes.",
                 time="Classeur"),
            dict(path="Technique/2026 1028 References prix et benchmarks.md",
                 name="Références prix, benchmarks et taux",
                 desc="Les trois dossiers de recherche du 27 et 28 octobre : prix des API de modèles et résidence UE, "
                      "infrastructure et services, benchmarks d'agents et taux journaliers. URL et date pour chaque chiffre."),
            dict(path="Technique/architecture.png",
                 name="Schéma d'architecture",
                 desc="Le schéma du § 3 de la réponse, en PNG."),
        ]),
    dict(
        folder="Juridique", title="Juridique", who="Tiffany",
        lead="La revue des cinq projets, puis les versions corrigées. Rien ne remplace les projets 1.x sans sa décision.",
        items=[
            dict(path="Juridique/2026 1027 Revue juridique des cinq projets.docx",
                 name="Revue juridique des cinq projets",
                 desc="Constats par document, gravité, corrections, bases légales vérifiées, "
                      "documents manquants, plan d'action.",
                 time="30 min"),
            dict(path="Juridique/2026 1027 Statuts SAS Helium - Projet V2.md",
                 name="Statuts SAS Helium, projet V2",
                 desc="SAS à six associés au lieu de la SASU. Journal des modifications en fin de document."),
            dict(path="Juridique/2026 1027 CGV CGU Helium - Projet V2.md",
                 name="CGV et CGU Helium, projet V2",
                 desc="Rétractation en ligne, résiliation en trois clics, décret 2023-417, LCEN art. 1-1."),
            dict(path="Juridique/2026 1027 Politique de confidentialite Helium - Projet V2.md",
                 name="Politique de confidentialité, projet V2",
                 desc="Bases légales par traitement, sous-traitants, transferts, droits, durées."),
            dict(path="Juridique/2026 1027 Politique interne de protection des donnees Helium - Projet V2.md",
                 name="Politique interne de protection des données, projet V2",
                 desc="Registre, habilitations, violations, sous-traitance, formation."),
            dict(path="Juridique/2026 1027 Charte execution des agents IA Helium - Projet V2.md",
                 name="Charte d'exécution des agents IA, projet V2",
                 desc="Validation humaine de l'action finale, journalisation, limites par mission, règlement IA."),
            dict(path="Juridique/2026 1027 References juridiques verifiees.md",
                 name="Références juridiques vérifiées",
                 desc="Textes consultés, citations, points non confirmés. À relire sur Légifrance avant toute signature."),
        ]),
    dict(
        folder="Marque", title="Marque", who="Alice",
        lead="Une identité propre : le point levé, une palette sans bleu ni violet.",
        items=[
            dict(path="Marque/2026 1027 Helium charte de marque V1.docx",
                 name="Charte de marque V1",
                 desc="Nom, plateforme, voix, logo, palette, typographie, applications.",
                 time="25 min"),
            dict(path="Marque/assets", name="Fichiers du logo (dossier)", is_dir=True,
                 desc="Wordmark en PNG et SVG, icône d'application, versions sur fond chalk et sur fond ink."),
        ]),
    dict(
        folder="Outils", title="Outils", who="Qui veut régénérer",
        lead="Les scripts qui produisent le modèle, le logo et cette page.",
        items=[
            dict(path="Outils/build_model.py", name="build_model.py",
                 desc="Reconstruit le classeur Finance à partir de la liste ASSUMPTIONS (Python 3, openpyxl)."),
            dict(path="Outils/make_logo.py", name="make_logo.py",
                 desc="Régénère les fichiers du logo (Pillow)."),
            dict(path="Outils/helium_brand.py", name="helium_brand.py",
                 desc="Palette et polices, importées par les autres scripts."),
            dict(path="Outils/build_missions.py", name="build_missions.py et missions_data.py",
                 desc="Reconstruisent le classeur Technique à partir des tarifs et des paramètres par mission."),
            dict(path="Outils/make_index.py", name="make_index.py",
                 desc="Régénère cette page."),
            dict(path="Outils/LISEZ-MOI.md", name="LISEZ-MOI des outils",
                 desc="Mode d'emploi des scripts."),
        ]),
]

DECISIONS = [
    ("D-01", "Nature du projet, fondateurs, propriété intellectuelle",
     "Projet pédagogique ou entreprise ; qui continue ; à qui appartient ce qui est produit. "
     "Les statuts actuels font du CEO l'associé unique d'une SASU pendant que six personnes construisent."),
    ("D-02", "Le nom Helium",
     "Recherche d'antériorité INPI et EUIPO avant tout usage public. Helium Network, Helium 10 et Helium Health existent."),
    ("D-03", "Cible et seuils du pilote",
     "Cadres urbains, abonnement à 79 € ; seuils de prix accepté et de coût par mission qui déclenchent le go."),
    ("D-04", "Porte d'évidence",
     "90 jours, 15 k€ au plus, du 3 novembre 2026 au 1er février 2027. Pas un lancement."),
    ("D-05", "Go ou stop au jour 90",
     "Sur les mesures du pilote, pas sur les hypothèses du modèle."),
]

ICON = {".pptx": "PPTX", ".docx": "DOCX", ".xlsx": "XLSX", ".md": "MD", ".py": "PY", ".png": "PNG", ".svg": "SVG"}
OFFICE_EXT = {".pptx", ".docx", ".xlsx"}


def enc(rel: str) -> str:
    return quote(f"{FOLDER}/{rel}", safe="/")


def e(s: str) -> str:
    return html.escape(s, quote=True)


def links(item: dict) -> str:
    rel = item["path"]
    ext = os.path.splitext(rel)[1].lower()
    if item.get("is_dir"):
        return f'<a class="btn primary" href="{TREE}{enc(rel)}">Ouvrir le dossier</a>'
    out = [f'<a class="btn primary" href="{BLOB}{enc(rel)}">{"Lire" if ext in (".md",) else "Voir sur GitHub"}</a>']
    if ext in OFFICE_EXT:
        out.append(f'<a class="btn" href="{OFFICE}{quote(RAW + enc(rel), safe="")}">Aperçu en ligne</a>')
    out.append(f'<a class="btn" href="{RAW}{enc(rel)}" download>Télécharger</a>')
    return "\n".join(out)


def item_html(item: dict, size: str) -> str:
    ext = os.path.splitext(item["path"])[1].lower()
    tag = "DOSSIER" if item.get("is_dir") else ICON.get(ext, ext.strip(".").upper())
    meta = " · ".join(x for x in (item.get("time"), size) if x)
    return f"""
      <li class="item">
        <div class="tag">{tag}</div>
        <div class="body">
          <h3>{e(item["name"])}</h3>
          <p>{e(item["desc"])}</p>
          {f'<p class="meta">{e(meta)}</p>' if meta else ''}
        </div>
        <div class="actions">
          {links(item)}
        </div>
      </li>"""


def human(n: int) -> str:
    return f"{n / 1024:.0f} Ko" if n < 1024 * 1024 else f"{n / 1024 / 1024:.1f} Mo"


def build(root: str) -> str:
    missing = []
    sections = []
    for s in SECTIONS:
        rows = []
        for it in s["items"]:
            p = os.path.join(root, it["path"])
            size = ""
            if os.path.isdir(p):
                pass
            elif os.path.isfile(p):
                size = human(os.path.getsize(p))
            else:
                missing.append(it["path"])
            rows.append(item_html(it, size))
        sections.append(f"""
    <section class="block" id="{e(s["folder"].lower())}">
      <header class="block-head">
        <div>
          <p class="kicker">{e(s["folder"])}/</p>
          <h2>{e(s["title"])}</h2>
          <p class="lead">{e(s["lead"])}</p>
        </div>
        <p class="who"><span>Pour</span> {e(s["who"])}</p>
      </header>
      <ul class="items">{"".join(rows)}
      </ul>
    </section>""")
    if missing:
        print("ATTENTION fichiers absents :", *missing, sep="\n  ", file=sys.stderr)

    decisions = "".join(
        f"""
        <li><span class="dnum">{e(n)}</span><div><strong>{e(t)}</strong><p>{e(d)}</p></div></li>"""
        for n, t, d in DECISIONS)

    today = os.environ.get("INDEX_DATE") or date.today().strftime("%d/%m/%Y")
    history = f'https://github.com/{OWNER}/{REPO}/commits/{BRANCH}/{quote(FOLDER)}'

    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Helium, dossier Board</title>
<meta name="description" content="Productions Helium du 27 octobre 2026 : deck, analyses, modèle financier, revue juridique, charte de marque. Liens de lecture et de téléchargement.">
<link rel="icon" href="Marque/assets/app_icon_256.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {{
  --ink: {P["ink"]}; --chalk: {P["chalk"]}; --glow: {P["glow"]}; --glow-deep: {P["glow_deep"]};
  --d3: {P["d3"]}; --euc: {P["euc"]}; --stone: {P["stone"]}; --linen: {P["linen"]}; --mist: {P["mist"]};
  --bg: var(--chalk); --fg: var(--ink); --muted: var(--stone); --card: #FFFDF9; --line: var(--linen);
  --btn-bg: var(--ink); --btn-fg: var(--chalk); --accent: var(--glow-deep);
  --serif: "Fraunces", Georgia, "Times New Roman", serif;
  --sans: "Inter", system-ui, -apple-system, "Segoe UI", Arial, sans-serif;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: var(--ink); --fg: var(--chalk); --muted: #B8AFA4; --card: #2A2521; --line: #3A342F;
    --btn-bg: var(--chalk); --btn-fg: var(--ink); --accent: var(--glow);
  }}
}}
:root[data-theme="dark"] {{
  --bg: var(--ink); --fg: var(--chalk); --muted: #B8AFA4; --card: #2A2521; --line: #3A342F;
  --btn-bg: var(--chalk); --btn-fg: var(--ink); --accent: var(--glow);
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg); font-family: var(--sans);
  font-size: 16px; line-height: 1.55; -webkit-font-smoothing: antialiased;
}}
a {{ color: inherit; }}
.wrap {{ max-width: 1040px; margin: 0 auto; padding: 0 16px; }}

/* En-tête */
.top {{ padding: 40px 0 28px; border-bottom: 1px solid var(--line); }}
.top .row {{ display: flex; flex-wrap: wrap; gap: 24px; align-items: flex-end; justify-content: space-between; }}
.wordmark img {{ height: 64px; width: auto; display: block; }}
.top .date {{ font-family: var(--serif); font-size: 15px; color: var(--muted); margin: 0; }}
h1 {{
  font-family: var(--serif); font-weight: 600; font-size: clamp(32px, 5vw, 52px); line-height: 1.05;
  letter-spacing: -0.015em; margin: 28px 0 14px; max-width: 18ch;
}}
h1 .dot {{ color: var(--accent); }}
.intro {{ font-size: 18px; max-width: 62ch; margin: 0 0 22px; }}
.status {{
  display: inline-flex; align-items: center; gap: 10px; padding: 8px 14px; border-radius: 999px;
  background: var(--card); border: 1px solid var(--line); font-size: 14px; color: var(--muted);
}}
.status::before {{ content: ""; flex: none; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }}

/* Par où commencer */
.start {{ padding: 32px 0 8px; }}
.start h2 {{ font-family: var(--serif); font-weight: 600; font-size: 22px; margin: 0 0 14px; }}
.steps {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; list-style: none; padding: 0; margin: 0; }}
.steps li {{
  background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 18px 18px 16px;
  display: flex; flex-direction: column; gap: 6px;
}}
.steps .n {{ font-family: var(--serif); font-size: 30px; line-height: 1; color: var(--accent); font-weight: 600; }}
.steps strong {{ font-size: 16px; }}
.steps p {{ margin: 0; color: var(--muted); font-size: 14px; }}
.steps a {{ margin-top: auto; font-weight: 600; text-decoration: none; color: var(--fg); border-bottom: 2px solid var(--accent); width: fit-content; }}

/* Sommaire */
.toc {{ display: flex; flex-wrap: wrap; gap: 8px; padding: 22px 0 6px; }}
.toc a {{
  text-decoration: none; font-size: 14px; font-weight: 500; padding: 6px 12px; border-radius: 999px;
  border: 1px solid var(--line); color: var(--fg); background: transparent;
}}
.toc a:hover {{ border-color: var(--accent); }}

/* Blocs */
.block {{ padding: 30px 0 10px; border-top: 1px solid var(--line); margin-top: 20px; }}
.block-head {{ display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px 32px; align-items: flex-start; margin-bottom: 14px; }}
.kicker {{ font-family: var(--serif); color: var(--accent); margin: 0 0 2px; font-size: 14px; letter-spacing: 0.02em; }}
.block h2 {{ font-family: var(--serif); font-weight: 600; font-size: 30px; margin: 0 0 6px; letter-spacing: -0.01em; }}
.lead {{ margin: 0; color: var(--muted); max-width: 60ch; }}
.who {{ margin: 6px 0 0; font-size: 14px; white-space: nowrap; }}
.who span {{ color: var(--muted); margin-right: 6px; }}
.items {{ list-style: none; padding: 0; margin: 0; display: grid; gap: 10px; }}
.item {{
  display: grid; grid-template-columns: 64px 1fr auto; gap: 16px; align-items: start;
  background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 16px 18px;
}}
.tag {{
  font-family: var(--serif); font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-align: center;
  padding: 7px 0; border-radius: 8px; background: var(--mist); color: var(--ink);
}}
:root[data-theme="dark"] .tag {{ background: #3A342F; color: var(--chalk); }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) .tag {{ background: #3A342F; color: var(--chalk); }} }}
.item h3 {{ margin: 0 0 4px; font-family: var(--serif); font-weight: 600; font-size: 19px; line-height: 1.25; }}
.item p {{ margin: 0; font-size: 14.5px; }}
.item .meta {{ margin-top: 6px; color: var(--muted); font-size: 13px; }}
.actions {{ display: flex; flex-direction: column; gap: 6px; min-width: 160px; }}
.btn {{
  display: inline-block; text-align: center; text-decoration: none; font-size: 13.5px; font-weight: 600;
  padding: 8px 12px; border-radius: 9px; border: 1px solid var(--line); color: var(--fg); background: transparent;
}}
.btn:hover {{ border-color: var(--accent); }}
.btn.primary {{ background: var(--btn-bg); color: var(--btn-fg); border-color: var(--btn-bg); }}
.btn.primary:hover {{ background: var(--accent); border-color: var(--accent); color: var(--ink); }}

/* Décisions */
.decisions {{ padding: 30px 0 10px; border-top: 1px solid var(--line); margin-top: 20px; }}
.decisions h2 {{ font-family: var(--serif); font-weight: 600; font-size: 30px; margin: 0 0 6px; }}
.decisions ol {{ list-style: none; padding: 0; margin: 16px 0 0; display: grid; gap: 10px; }}
.decisions li {{ display: grid; grid-template-columns: 64px 1fr; gap: 16px; background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 14px 18px; }}
.dnum {{ font-family: var(--serif); font-weight: 700; color: var(--accent); font-size: 18px; }}
.decisions strong {{ font-family: var(--serif); font-size: 17px; font-weight: 600; }}
.decisions p {{ margin: 4px 0 0; font-size: 14.5px; color: var(--muted); }}

/* Pied */
.foot {{ margin-top: 36px; padding: 26px 0 48px; border-top: 1px solid var(--line); font-size: 14px; color: var(--muted); }}
.foot p {{ margin: 0 0 10px; max-width: 78ch; }}
.foot a {{ color: var(--fg); }}

@media (max-width: 760px) {{
  .steps {{ grid-template-columns: 1fr; }}
  .item {{ grid-template-columns: 56px 1fr; }}
  .actions {{ grid-column: 1 / -1; flex-direction: row; flex-wrap: wrap; }}
  .actions .btn {{ flex: 1 1 auto; }}
  .who {{ white-space: normal; }}
}}
</style>
</head>
<body>
<div class="wrap">

  <header class="top">
    <div class="row">
      <picture class="wordmark">
        <source srcset="Marque/assets/wordmark_chalk.png" media="(prefers-color-scheme: dark)">
        <img src="Marque/assets/wordmark_ink.png" alt="Helium">
      </picture>
      <p class="date">Productions des 27 et 28 octobre 2026</p>
    </div>
    <h1>Le dossier Board, à un clic de chaque pièce<span class="dot">.</span></h1>
    <p class="intro">Tout ce qui a été produit pour la décision du Board : le deck, les deux analyses, le modèle financier, la revue juridique, la charte de marque, et la réponse technique au cadrage Finance. Chaque pièce se lit sur GitHub ou se télécharge.</p>
    <p class="status">Propositions. Rien n'est acté tant que ce n'est pas au registre des décisions.</p>
  </header>

  <section class="start">
    <h2>Par où commencer</h2>
    <ol class="steps">
      <li><span class="n">1</span><strong>Le deck</strong><p>La décision demandée et pourquoi, en 24 diapositives. Vingt minutes.</p><a href="{BLOB}{enc('Board/2026 1027 Helium Board deck V1.pptx')}">Ouvrir le deck</a></li>
      <li><span class="n">2</span><strong>Le modèle d'affaires</strong><p>Le raisonnement complet, les options écartées et l'audit des hypothèses. Quarante-cinq minutes.</p><a href="{BLOB}{enc('Direction/2026 1027 Helium modele d affaires et etude de cas V1.docx')}">Ouvrir le dossier</a></li>
      <li><span class="n">3</span><strong>Votre dossier de fonction</strong><p>Marketing, Finance, Juridique, Marque : ce qui vous concerne directement, ci-dessous.</p><a href="#marketing">Aller aux dossiers</a></li>
    </ol>
  </section>

  <nav class="toc" aria-label="Sommaire">
    <a href="#board">Board</a><a href="#direction">Direction</a><a href="#marketing">Marketing</a><a href="#finance">Finance</a><a href="#technique">Technique</a><a href="#juridique">Juridique</a><a href="#marque">Marque</a><a href="#outils">Outils</a><a href="#decisions">Décisions attendues</a>
  </nav>
{"".join(sections)}

  <section class="decisions" id="decisions">
    <h2>Cinq décisions attendues, dans cet ordre</h2>
    <p class="lead">À inscrire au <a href="{BLOB}{quote('1 DIRECTION/REGISTRE DES DECISIONS.md')}">registre des décisions</a> avec la date, la pièce et qui a décidé.</p>
    <ol>{decisions}
    </ol>
  </section>

  <footer class="foot">
    <p>Ces productions restent dans <code>PRODUCTIONS ASSISTANTS/</code> conformément à <a href="{BLOB}RULES.md">RULES.md</a>. Elles n'entrent dans un dossier de fonction que par décision du responsable de la fonction.</p>
    <p>Les boutons « Aperçu en ligne » et « Télécharger » passent par l'adresse publique du dépôt : ils cesseront de fonctionner le jour où le dépôt redeviendra privé. Les liens « Voir sur GitHub » continueront pour les membres connectés.</p>
    <p><a href="{ZIP}">Télécharger le dépôt entier (zip)</a> · <a href="{TREE}{quote(FOLDER)}">Le dossier sur GitHub</a> · <a href="{BLOB}{quote(FOLDER + '/LISEZ-MOI.md')}">LISEZ-MOI</a> · <a href="{history}">Historique des modifications</a></p>
    <p>Page générée le {today} par <code>Outils/make_index.py</code>.</p>
  </footer>

</div>
</body>
</html>
"""


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(here, ".."))
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(build(root))
    print("écrit :", out)
