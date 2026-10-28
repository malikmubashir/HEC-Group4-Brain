#!/usr/bin/env python3
"""Helium, coût par mission V1 : classeur de réponse à la demande de cadrage Finance.

Onglets : LISEZ-MOI · Tarifs · Missions · Synthèse · Sensibilité · Protections · Plan de charge · Tableau commun.
Formules vivantes : toute entrée est dans Tarifs (prix unitaires) ou Missions (paramètres par mission).
"""
import os, sys, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.chart import BarChart, Reference
from openpyxl.comments import Comment

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helium_brand import PALETTE

ARIAL = "Arial"
BLUE = Font(name=ARIAL, size=10, color="0000FF")
BLACK = Font(name=ARIAL, size=10, color="000000")
GREEN = Font(name=ARIAL, size=10, color="008000")
BOLD = Font(name=ARIAL, size=10, bold=True)
HEAD = Font(name=ARIAL, size=10, bold=True, color=PALETTE["ink"])
TITLE = Font(name="Georgia", size=16, color=PALETTE["ink"])
SUB = Font(name=ARIAL, size=9, italic=True, color=PALETTE["stone"])
SMALL = Font(name=ARIAL, size=9, color=PALETTE["ink"])
YELLOW = PatternFill("solid", fgColor="FFFF00")
MIST = PatternFill("solid", fgColor=PALETTE["mist"])
LINEN = PatternFill("solid", fgColor=PALETTE["linen"])
GLOWF = PatternFill("solid", fgColor=PALETTE["glow"])
EUCF = PatternFill("solid", fgColor="DCE7DF")
BOT = Border(bottom=Side(style="thin", color=PALETTE["glow"]))
THINB = Border(bottom=Side(style="thin", color=PALETTE["linen"]))

EUR = '#,##0" €";(#,##0" €");"-"'
EUR2 = '#,##0.00" €";(#,##0.00" €");"-"'
EUR3 = '#,##0.000" €";(#,##0.000" €");"-"'
USD = '#,##0.00" $";(#,##0.00" $");"-"'
USD4 = '#,##0.0000" $";(#,##0.0000" $");"-"'
PCT = '0%;(0%);"-"'
PCT1 = '0.0%;(0.0%);"-"'
NUM = '#,##0;(#,##0);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
NUM2 = '#,##0.00;(#,##0.00);"-"'

OUT = os.environ.get("OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out", "technique", "Helium_Cout_par_mission_V1.xlsx"))
TODAY = os.environ.get("INDEX_DATE", "28/10/2026")

# ---------------------------------------------------------------------------
# TARIFS : (clé, poste, valeur, unité, nature, source, date, note)
# nature : "Tarif public" (sourcé) ou "Hypothèse"
# Les valeurs sont renseignées depuis research/llm-pricing.md, infra-services.md, benchmarks-rates.md
# ---------------------------------------------------------------------------
from missions_data import PRICES, MISSIONS, OFFERS, WORKLOAD, RATES, NONLABOUR, PROTECTIONS, COMMON_TABLE, MODEL_TIERS

PRICE_CELL = {}


def P(key):
    return PRICE_CELL[key]


def setw(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[L(i)].width = w


def header(ws, row, labels, fill=MIST, wrap=True, height=None):
    for j, lab in enumerate(labels, start=1):
        c = ws.cell(row=row, column=j, value=lab)
        c.font = HEAD
        c.fill = fill
        c.border = BOT
        c.alignment = Alignment(wrap_text=wrap, vertical="bottom", horizontal="left")
    if height:
        ws.row_dimensions[row].height = height


def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = TITLE
    if sub:
        ws["A2"] = sub
        ws["A2"].font = SUB
    ws.sheet_view.showGridLines = False


# ---------------------------------------------------------------------------
def write_readme(ws):
    title(ws, "Helium, coût par mission et plan de charge MVP, V1")
    lines = [
        ("Objet", "Réponse chiffrée à la demande de cadrage Finance → Produit/Technique (2 FINANCE/PREVISIONS/2026 1027 Demande de cadrage Produit Technique) : coût unitaire par mission, coût variable par abonné, protections contre les dérives, plan de charge et budget MVP."),
        ("Statut", "Document de travail préparé par l'assistant IA Direction à la demande du CEO (Malik), le " + TODAY + ". Rien n'est mesuré : tous les volumes de jetons, taux de réussite et minutes sont des hypothèses d'ingénierie, étiquetées comme telles. Seuls les prix unitaires marqués « Tarif public » sont sourcés (URL et date dans l'onglet Tarifs)."),
        ("Légende", "Texte bleu = entrée modifiable (hypothèse). Fond jaune = levier clé. Texte noir = formule. Texte vert = lien vers un autre onglet. Fond vert pâle (Tarifs) = prix public sourcé."),
        ("Onglets", "Tarifs (prix unitaires, taux de change, coût du support) · Missions (paramètres et coût par exécution, par mission) · Synthèse (coût variable par abonné et par offre, comparaison avec l'hypothèse Finance H03 et avec le modèle 36 mois) · Sensibilité (variations linéaires des composantes) · Protections (plafonds par offre et coût au plafond) · Plan de charge (jours par profil, budget MVP, comparaison avec les 77 050 € du Business plan Lean V1) · Tableau commun (le format demandé par Finance)."),
        ("Mécanique", "Coût d'une exécution = facteur de reprises × [appels petit modèle × (entrée non cachée × prix + entrée cachée × prix caché + sortie × prix) + appels moyen × idem, dont une part escaladée vers le modèle frontière] + recherches + lieux + lectures de page + minutes de navigateur piloté + minutes de support humain espérées. Prix en dollars convertis en euros au taux de l'onglet Tarifs. Coût mensuel par abonné = somme des fréquences × coût par exécution, pondérée par offre."),
        ("Ce que mesure le pilote", "Pour les missions 1 et 5 d'abord, puis 3 et 4 : jetons réels par étape, nombre d'étapes, reprises, taux de réussite sans correction, minutes de support. Chaque mesure remplace une cellule bleue de l'onglet Missions. Le classeur est conçu pour que Finance n'ait qu'à substituer."),
        ("Contrôles", "Recalcul complet sous LibreOffice, zéro erreur ; cohérence du nombre d'exécutions par offre avec les 20 / 60 / 90 missions par mois du modèle financier 36 mois ; coût moyen par mission comparé à l'hypothèse de 0,18 € (central) et 0,30 € (prudent) de ce modèle."),
        ("Liens", "Modèle financier 36 mois (Finance/Helium_Modele_financier_36m_V1.xlsx) · Réponse au cadrage (Technique/2026 1028 Reponse au cadrage Produit Technique V1.docx) · Contribution marketing au cadrage MVP (5 PRODUIT) · Références prix (Technique/2026 1028 References prix et benchmarks.md)."),
    ]
    r = 3
    for k, v in lines:
        ws.cell(row=r, column=1, value=k).font = BOLD
        c = ws.cell(row=r, column=2, value=v)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    setw(ws, [22, 125])


# ---------------------------------------------------------------------------
def write_tarifs(ws):
    title(ws, "Tarifs unitaires", "Prix publics relevés en octobre 2026 (fond vert) et hypothèses (texte bleu). Les formules des autres onglets pointent ici.")
    header(ws, 4, ["Clé", "Poste", "Valeur", "Unité", "Nature", "Source", "Date", "Note"], height=30)
    r = 5
    for key, label, val, unit, nature, src, date, note in PRICES:
        ws.cell(row=r, column=1, value=key).font = SMALL
        ws.cell(row=r, column=2, value=label).font = BLACK
        c = ws.cell(row=r, column=3, value=val)
        c.font = BLUE
        if unit.startswith("$"):
            c.number_format = USD4 if val < 1 else USD
        elif unit.startswith("€"):
            c.number_format = EUR3 if val < 1 else EUR2
        elif unit == "%":
            c.number_format = PCT1
        else:
            c.number_format = NUM2
        if nature == "Tarif public":
            c.fill = EUCF
        ws.cell(row=r, column=4, value=unit).font = BLACK
        ws.cell(row=r, column=5, value=nature).font = BLACK
        s = ws.cell(row=r, column=6, value=src)
        s.font = SMALL
        s.alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=7, value=date).font = SMALL
        n = ws.cell(row=r, column=8, value=note)
        n.font = SMALL
        n.alignment = Alignment(wrap_text=True, vertical="top")
        for col in range(1, 9):
            ws.cell(row=r, column=col).border = THINB
            if col not in (6, 8):
                ws.cell(row=r, column=col).alignment = Alignment(vertical="top", wrap_text=(col == 2))
        PRICE_CELL[key] = f"Tarifs!$C${r}"
        r += 1
    # Tiers de modèles (texte)
    r += 1
    ws.cell(row=r, column=1, value="Paliers de modèles retenus").font = BOLD
    r += 1
    header(ws, r, ["Palier", "Rôle", "Modèle recommandé", "Alternative UE", "Prix entrée ($/M)", "Prix sortie ($/M)", "Résidence des données", "Note"], height=30)
    r += 1
    for tier in MODEL_TIERS:
        for j, v in enumerate(tier, start=1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = SMALL
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = THINB
        r += 1
    setw(ws, [16, 44, 12, 10, 13, 52, 11, 60])
    ws.freeze_panes = "A5"


# ---------------------------------------------------------------------------
MCOL = {}  # nom logique -> lettre de colonne dans Missions


def write_missions(ws):
    title(ws, "Missions : paramètres et coût par exécution", "Une ligne par mission. Colonnes bleues = hypothèses à remplacer par les mesures du pilote. Fréquences pour un abonné Premium.")
    cols = [
        ("num", "#", 5), ("name", "Mission", 30), ("prio", "Priorité", 9), ("level", "Validation (A/C/X)", 10),
        ("freq", "Exécutions par mois (Premium)", 11),
        ("n_s", "Appels petit modèle", 9), ("in_s", "Entrée par appel (jetons)", 11), ("c_s", "Part cachée", 8), ("out_s", "Sortie par appel (jetons)", 10),
        ("n_m", "Appels moyen", 9), ("in_m", "Entrée par appel (jetons)", 11), ("c_m", "Part cachée", 8), ("out_m", "Sortie par appel (jetons)", 10),
        ("f_f", "Part escaladée vers frontière", 10),
        ("srch", "Recherches web", 8), ("plc", "Appels Places", 8), ("pg", "Lectures de page", 8), ("brw", "Navigateur piloté (min)", 10),
        ("retry", "Facteur de reprises", 9), ("succ", "Taux de réussite estimé (non mesuré)", 11), ("dur", "Durée (min)", 8),
        ("h_share", "Part des échecs traités par un humain", 11), ("h_min", "Minutes par traitement", 9),
        ("emb", "Jetons d'embedding", 10),
        ("c_llm", "Coût modèles par exécution", 12), ("c_tools", "Coût outils par exécution", 12), ("c_supp", "Coût support par exécution", 12),
        ("c_exec", "Coût total HT par exécution", 12), ("c_month", "Coût mensuel par abonné Premium", 12), ("share", "Part du coût mensuel", 9),
        ("llm_m", "dont modèles / mois", 11), ("tools_m", "dont outils / mois", 11), ("supp_m", "dont support / mois", 11),
    ]
    for i, (k, lab, w) in enumerate(cols, start=1):
        MCOL[k] = L(i)
        ws.column_dimensions[L(i)].width = w
    header(ws, 4, [lab for _, lab, _ in cols], height=58)
    r0 = 5
    r = r0
    fx = P("fx")
    for m in MISSIONS:
        for k in ("num", "name", "prio", "level"):
            ws[f"{MCOL[k]}{r}"].value = m[k]
            ws[f"{MCOL[k]}{r}"].font = BLACK
        # inputs
        for k in ("freq", "n_s", "in_s", "c_s", "out_s", "n_m", "in_m", "c_m", "out_m", "f_f", "srch", "plc", "pg", "brw", "retry", "succ", "dur", "h_share", "h_min", "emb"):
            c = ws[f"{MCOL[k]}{r}"]
            c.value = m[k]
            c.font = BLUE
            c.number_format = PCT if k in ("c_s", "c_m", "f_f", "succ", "h_share") else (NUM2 if k in ("freq", "retry", "n_s", "n_m") else NUM)
        ws[f"{MCOL['name']}{r}"].alignment = Alignment(wrap_text=True, vertical="top")
        ws[f"{MCOL['name']}{r}"].font = BOLD if m["num"] not in ("M0", "M11") else BLACK
        # formulas
        def tok(n, inn, cc, out, pin, pcache, pout):
            return (f"{MCOL[n]}{r}*(({MCOL[inn]}{r}*(1-{MCOL[cc]}{r}))*{P(pin)}+{MCOL[inn]}{r}*{MCOL[cc]}{r}*{P(pcache)}+{MCOL[out]}{r}*{P(pout)})/1000000")
        small = tok("n_s", "in_s", "c_s", "out_s", "small_in", "small_cached", "small_out")
        mid = tok("n_m", "in_m", "c_m", "out_m", "mid_in", "mid_cached", "mid_out")
        front = tok("n_m", "in_m", "c_m", "out_m", "front_in", "front_cached", "front_out")
        emb = f"{MCOL['emb']}{r}*{P('embed')}/1000000"
        ws[f"{MCOL['c_llm']}{r}"] = f"={MCOL['retry']}{r}*({small}+(1-{MCOL['f_f']}{r})*{mid}+{MCOL['f_f']}{r}*{front}+{emb})*{fx}"
        ws[f"{MCOL['c_tools']}{r}"] = (f"={MCOL['retry']}{r}*({MCOL['srch']}{r}*{P('search_call')}+{MCOL['plc']}{r}*{P('places_call')}"
                                       f"+{MCOL['pg']}{r}*{P('page_read')}+{MCOL['brw']}{r}*{P('browser_min')})*{fx}")
        ws[f"{MCOL['c_supp']}{r}"] = f"=(1-{MCOL['succ']}{r})*{MCOL['h_share']}{r}*{MCOL['h_min']}{r}*{P('support_min')}"
        ws[f"{MCOL['c_exec']}{r}"] = f"={MCOL['c_llm']}{r}+{MCOL['c_tools']}{r}+{MCOL['c_supp']}{r}"
        ws[f"{MCOL['c_month']}{r}"] = f"={MCOL['freq']}{r}*{MCOL['c_exec']}{r}"
        ws[f"{MCOL['llm_m']}{r}"] = f"={MCOL['freq']}{r}*{MCOL['c_llm']}{r}"
        ws[f"{MCOL['tools_m']}{r}"] = f"={MCOL['freq']}{r}*{MCOL['c_tools']}{r}"
        ws[f"{MCOL['supp_m']}{r}"] = f"={MCOL['freq']}{r}*{MCOL['c_supp']}{r}"
        for k in ("c_llm", "c_tools", "c_supp", "c_exec"):
            ws[f"{MCOL[k]}{r}"].number_format = EUR3
            ws[f"{MCOL[k]}{r}"].font = BLACK
        for k in ("c_month", "llm_m", "tools_m", "supp_m"):
            ws[f"{MCOL[k]}{r}"].number_format = EUR2
            ws[f"{MCOL[k]}{r}"].font = BLACK
        ws[f"{MCOL['c_exec']}{r}"].fill = MIST
        ws[f"{MCOL['c_month']}{r}"].fill = MIST
        r += 1
    r_last = r - 1
    # Part du coût mensuel (hors onboarding M11 : fréquence 0 par mois)
    for rr in range(r0, r_last + 1):
        ws[f"{MCOL['share']}{rr}"] = f"=IF(${MCOL['c_month']}${r_last + 1}=0,0,{MCOL['c_month']}{rr}/${MCOL['c_month']}${r_last + 1})"
        ws[f"{MCOL['share']}{rr}"].number_format = PCT1
        ws[f"{MCOL['share']}{rr}"].font = BLACK
    # Totals row
    rt = r_last + 1
    ws[f"{MCOL['name']}{rt}"] = "Total mensuel, abonné Premium (M0 à M10)"
    ws[f"{MCOL['name']}{rt}"].font = BOLD
    ws[f"{MCOL['freq']}{rt}"] = f"=SUM({MCOL['freq']}{r0}:{MCOL['freq']}{r_last})"
    ws[f"{MCOL['freq']}{rt}"].number_format = NUM1
    for k in ("c_month", "llm_m", "tools_m", "supp_m"):
        ws[f"{MCOL[k]}{rt}"] = f"=SUM({MCOL[k]}{r0}:{MCOL[k]}{r_last})"
        ws[f"{MCOL[k]}{rt}"].number_format = EUR2
        ws[f"{MCOL[k]}{rt}"].font = BOLD
        ws[f"{MCOL[k]}{rt}"].fill = YELLOW
    ws[f"{MCOL['freq']}{rt}"].font = BOLD
    for col in range(1, len(cols) + 1):
        ws.cell(row=rt, column=col).border = BOT
    # Coût moyen par mission
    ra = rt + 1
    ws[f"{MCOL['name']}{ra}"] = "Coût moyen par exécution (toutes missions, hors M11)"
    ws[f"{MCOL['name']}{ra}"].font = BOLD
    ws[f"{MCOL['c_exec']}{ra}"] = f"={MCOL['c_month']}{rt}/{MCOL['freq']}{rt}"
    ws[f"{MCOL['c_exec']}{ra}"].number_format = EUR3
    ws[f"{MCOL['c_exec']}{ra}"].font = BOLD
    ws[f"{MCOL['c_exec']}{ra}"].fill = YELLOW
    ra2 = ra + 1
    ws[f"{MCOL['name']}{ra2}"] = "Coût moyen par exécution, hors socle M0 (missions visibles 1 à 10)"
    ws[f"{MCOL['name']}{ra2}"].font = BLACK
    ws[f"{MCOL['c_exec']}{ra2}"] = f"=({MCOL['c_month']}{rt}-{MCOL['c_month']}{r0})/({MCOL['freq']}{rt}-{MCOL['freq']}{r0})"
    ws[f"{MCOL['c_exec']}{ra2}"].number_format = EUR3
    ws.freeze_panes = f"{MCOL['freq']}5"
    # Notes par mission (scénario d'exécution) en commentaire
    for i, m in enumerate(MISSIONS):
        ws[f"{MCOL['name']}{r0 + i}"].comment = Comment(m["scenario"], "Assistant IA Direction")
    return r0, r_last, rt, ra, ra2


# ---------------------------------------------------------------------------
def write_synthese(ws, rows):
    r0, r_last, rt, ra, ra2 = rows
    title(ws, "Synthèse : coût variable par abonné et par offre", "Multiplicateurs de fréquence par offre (bleu) appliqués aux missions. Comparaison avec l'hypothèse Finance H03 (18 € HT) et avec le modèle 36 mois.")
    offers = OFFERS  # list of dict: name, price_ttc, mult per mission num
    n_off = len(offers)
    header(ws, 4, ["#", "Mission", "Coût par exécution"] + [f"{o['name']} : multiplicateur" for o in offers] + [f"{o['name']} : exécutions / mois" for o in offers] + [f"{o['name']} : coût / mois" for o in offers], height=44)
    r = 5
    first = r
    for i, m in enumerate(MISSIONS):
        mr = r0 + i
        ws.cell(row=r, column=1, value=m["num"]).font = BLACK
        ws.cell(row=r, column=2, value=m["name"]).font = BLACK
        c = ws.cell(row=r, column=3, value=f"=Missions!{MCOL['c_exec']}{mr}")
        c.font = GREEN
        c.number_format = EUR3
        for j, o in enumerate(offers):
            cm = ws.cell(row=r, column=4 + j, value=o["mult"].get(m["num"], 0))
            cm.font = BLUE
            cm.number_format = NUM2
            ce = ws.cell(row=r, column=4 + n_off + j, value=f"={L(4 + j)}{r}*Missions!{MCOL['freq']}{mr}")
            ce.font = BLACK
            ce.number_format = NUM1
            cc = ws.cell(row=r, column=4 + 2 * n_off + j, value=f"={L(4 + n_off + j)}{r}*$C{r}")
            cc.font = BLACK
            cc.number_format = EUR2
        r += 1
    last = r - 1
    # totals
    ws.cell(row=r, column=2, value="Exécutions et coût IA, outils et support par mois").font = BOLD
    for j in range(n_off):
        for base in (4 + n_off, 4 + 2 * n_off):
            c = ws.cell(row=r, column=base + j, value=f"=SUM({L(base + j)}{first}:{L(base + j)}{last})")
            c.font = BOLD
            c.number_format = NUM1 if base == 4 + n_off else EUR2
            c.border = BOT
    rtot = r
    r += 2
    # Bloc par offre
    header(ws, r, ["", "Par abonné et par mois"] + [o["name"] for o in offers], height=20)
    r += 1
    labels = []

    def line(label, formula_fn, fmt=EUR2, bold=False, fill=None, font=BLACK):
        nonlocal r
        ws.cell(row=r, column=2, value=label).font = BOLD if bold else BLACK
        for j, o in enumerate(offers):
            c = ws.cell(row=r, column=3 + j, value=formula_fn(j, o))
            c.font = BOLD if bold else font
            c.number_format = fmt
            if fill:
                c.fill = fill
        labels.append((label, r))
        r += 1
        return r - 1

    rp = line("Prix TTC", lambda j, o: o["price_ttc"], font=BLUE)
    rht = line("Prix HT (TVA 20 %)", lambda j, o: f"={L(3 + j)}{rp}/1.2")
    rex = line("Exécutions par mois (socle compris)", lambda j, o: f"={L(4 + n_off + j)}{rtot}", fmt=NUM1)
    rexv = line("Missions visibles par mois (hors socle M0)", lambda j, o: f"={L(4 + n_off + j)}{rtot}-{L(4 + n_off + j)}{first}", fmt=NUM1)
    rm36 = line("Missions par mois dans le modèle 36 mois", lambda j, o: o["m36"], fmt=NUM, font=BLUE)
    ria = line("Coût IA, outils et support (ce classeur)", lambda j, o: f"={L(4 + 2 * n_off + j)}{rtot}", bold=True, fill=YELLOW)
    rhost = line("Hébergement, stockage, connecteurs (par abonné)", lambda j, o: f"={P('hosting_user')}")
    rpay = line("Frais de paiement", lambda j, o: f"={L(3 + j)}{rp}*{P('stripe_pct')}+{P('stripe_fixed')}")
    rvar = line("Coût variable total HT", lambda j, o: f"={L(3 + j)}{ria}+{L(3 + j)}{rhost}+{L(3 + j)}{rpay}", bold=True, fill=YELLOW)
    rh03 = line("Hypothèse Finance H03 (coût variable)", lambda j, o: 18 if o["name"] == "Premium" else "", font=BLUE)
    rmod = line("Modèle 36 mois, central : missions × 0,18 € + 1,50 € + 3,00 €", lambda j, o: f"={L(3 + j)}{rm36}*0.18+1.5+3")
    rmodp = line("Modèle 36 mois, prudent : missions × 0,30 € + 2,00 € + 5,00 €", lambda j, o: f"={L(3 + j)}{rm36}*0.30+2+5")
    rcpm = line("Coût moyen par mission visible (ce classeur, socle réparti)", lambda j, o: f"=IF({L(3 + j)}{rexv}=0,0,{L(3 + j)}{ria}/{L(3 + j)}{rexv})", fmt=EUR3, bold=True)
    rcon = line("Contribution par abonné (prix HT − coût variable)", lambda j, o: f"={L(3 + j)}{rht}-{L(3 + j)}{rvar}", bold=True)
    rmg = line("Marge variable", lambda j, o: f"=IF({L(3 + j)}{rht}=0,0,{L(3 + j)}{rcon}/{L(3 + j)}{rht})", fmt=PCT1)
    r += 1
    ws.cell(row=r, column=2, value="Coût d'activation (M11, une fois par nouvel abonné)").font = BOLD
    c = ws.cell(row=r, column=3, value=f"=Missions!{MCOL['c_exec']}{r0 + len(MISSIONS) - 1}")
    c.font = GREEN
    c.number_format = EUR2
    ract = r
    r += 1
    ws.cell(row=r, column=2, value="Part des missions à navigateur piloté (M3, M4, M10) dans le coût Premium").font = BLACK
    idx = {m["num"]: i for i, m in enumerate(MISSIONS)}
    prem_col = L(4 + 2 * n_off + [o["name"] for o in offers].index("Premium"))
    c = ws.cell(row=r, column=3, value=f"=({prem_col}{first + idx['M3']}+{prem_col}{first + idx['M4']}+{prem_col}{first + idx['M10']})/{prem_col}{rtot}")
    c.number_format = PCT1
    c.font = BLACK
    r += 2
    ws.cell(row=r, column=2, value="Lecture").font = BOLD
    r += 1
    notes = [
        "Le coût variable de ce classeur est inférieur à l'hypothèse H03 de 18 € : la différence est une marge de prudence, pas une économie acquise. Le modèle 36 mois conserve 0,18 € par mission en central et 0,30 € en prudent tant que le pilote n'a pas mesuré.",
        "Les trois missions à navigateur piloté (prise de rendez-vous, restaurant, événement) concentrent l'essentiel du coût : ce sont elles qu'il faut mesurer en premier et plafonner (onglet Protections).",
        "Le coût d'activation (lecture initiale de la boîte, M11) se traite comme un coût d'acquisition : il s'ajoute au CAC, pas au coût mensuel.",
        "Les multiplicateurs par offre sont des hypothèses de conception : Personal reçoit un briefing hebdomadaire et les missions de lecture ; Family double les missions de coordination et de réservation.",
    ]
    for n in notes:
        c = ws.cell(row=r, column=2, value=n)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3 + 2 * n_off)
        ws.row_dimensions[r].height = 30
        r += 1
    setw(ws, [6, 52, 14] + [13] * (3 * n_off))
    # Chart: coût mensuel par mission, Premium
    ch = BarChart()
    ch.type = "bar"
    ch.style = 10
    ch.title = "Coût mensuel par mission, abonné Premium (€ HT)"
    ch.y_axis.title = None
    ch.x_axis.title = None
    data = Reference(ws, min_col=4 + 2 * n_off + [o["name"] for o in offers].index("Premium"), min_row=first, max_row=last)
    cats = Reference(ws, min_col=2, min_row=first, max_row=last)
    ch.add_data(data, titles_from_data=False)
    ch.set_categories(cats)
    ch.legend = None
    ch.height = 9
    ch.width = 18
    ch.series[0].graphicalProperties.solidFill = PALETTE["glow"]
    ws.add_chart(ch, f"{L(5 + 3 * n_off)}4")
    return dict(ria=ria, rvar=rvar, rcpm=rcpm, rtot=rtot, first=first, last=last, prem_col=prem_col, rp=rp, rhost=rhost, rpay=rpay, rcon=rcon, rht=rht, idx=idx)


# ---------------------------------------------------------------------------
def write_sensibilite(ws, rows, syn):
    r0, r_last, rt, ra, ra2 = rows
    title(ws, "Sensibilité : coût variable Premium par mois", "Variations linéaires des composantes (modèles, outils, reprises, support, change). Chaque ligne recalcule le coût IA, outils et support de l'abonné Premium.")
    llm = f"Missions!{MCOL['llm_m']}{rt}"
    tools = f"Missions!{MCOL['tools_m']}{rt}"
    supp = f"Missions!{MCOL['supp_m']}{rt}"
    header(ws, 4, ["Cas", "Hypothèse", "Coût IA, outils, support (€ / mois)", "Écart vs base", "Coût variable total (€ / mois)", "Marge variable Premium"], height=40)
    cases = [
        ("Base", "Paramètres des onglets Tarifs et Missions", f"={llm}+{tools}+{supp}"),
        ("Prix des modèles × 2", "Hausse de prix ou routage dégradé (tout en moyen)", f"={llm}*2+{tools}+{supp}"),
        ("Prix des modèles × 0,5", "Baisse de prix annuelle observée, ou routage plus agressif vers le petit modèle", f"={llm}*0.5+{tools}+{supp}"),
        ("Sans cache de contexte", "Le cache ne fonctionne pas (facteur moyen 1,35 sur les modèles)", f"={llm}*1.35+{tools}+{supp}"),
        ("Outils × 2", "Navigateur piloté et recherches deux fois plus chers ou deux fois plus longs", f"={llm}+{tools}*2+{supp}"),
        ("Reprises +50 %", "Facteur de reprises 1,5 fois plus élevé sur modèles et outils", f"=({llm}+{tools})*1.5+{supp}"),
        ("Support × 3", "Taux d'échec ou minutes de support trois fois plus élevés", f"={llm}+{tools}+{supp}*3"),
        ("Dollar +10 %", "Change défavorable", f"=({llm}+{tools})*1.1+{supp}"),
        ("Tout en frontière", "Aucun routage : tous les appels moyens au prix frontière (approximation : modèles × ratio frontière/moyen)", f"={llm}*({P('front_in')}/{P('mid_in')})+{tools}+{supp}"),
        ("Réservations : volume × 3 et coût × 2", "Les missions à navigateur piloté (M3, M4, M10) trois fois plus fréquentes et deux fois plus chères", f"={llm}+{tools}+{supp}+5*(Synthèse!{syn['prem_col']}{syn['first'] + syn['idx']['M3']}+Synthèse!{syn['prem_col']}{syn['first'] + syn['idx']['M4']}+Synthèse!{syn['prem_col']}{syn['first'] + syn['idx']['M10']})"),
        ("Cumul défavorable", "Modèles × 2, outils × 2, reprises +50 %, support × 3", f"=({llm}*2+{tools}*2)*1.5+{supp}*3"),
    ]
    r = 5
    base_row = r
    prem = syn["prem_col"]
    rp = syn["rp"]
    prem_idx = [o["name"] for o in OFFERS].index("Premium")
    pc = L(3 + prem_idx)
    for name, hyp, f in cases:
        ws.cell(row=r, column=1, value=name).font = BOLD if name == "Base" else BLACK
        c = ws.cell(row=r, column=2, value=hyp)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c3 = ws.cell(row=r, column=3, value=f)
        c3.number_format = EUR2
        c3.font = BLACK
        c4 = ws.cell(row=r, column=4, value=f"=C{r}-C${base_row}")
        c4.number_format = EUR2
        c4.font = BLACK
        c5 = ws.cell(row=r, column=5, value=f"=C{r}+Synthèse!{pc}{syn['rhost']}+Synthèse!{pc}{syn['rpay']}")
        c5.number_format = EUR2
        c5.font = GREEN
        c6 = ws.cell(row=r, column=6, value=f"=(Synthèse!{pc}{syn['rht']}-E{r})/Synthèse!{pc}{syn['rht']}")
        c6.number_format = PCT1
        c6.font = BLACK
        ws.row_dimensions[r].height = 28
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Seuils").font = BOLD
    r += 1
    ws.cell(row=r, column=1, value="Hypothèse Finance H03").font = BLACK
    ws.cell(row=r, column=3, value=18).number_format = EUR2
    ws.cell(row=r, column=3).font = BLUE
    r += 1
    ws.cell(row=r, column=1, value="Seuil de la porte d'évidence (coût variable mesuré ≤ 18 € HT)").font = BLACK
    ws.cell(row=r, column=3, value=f"=IF(E{base_row}<=18,\"Tenu en base\",\"Dépassé en base\")").font = BOLD
    r += 1
    ws.cell(row=r, column=1, value="Coût par mission au-delà duquel le plan prévoit limites d'usage et test de prix (0,30 €)").font = BLACK
    ws.cell(row=r, column=3, value=f"=Missions!{MCOL['c_exec']}{ra}").number_format = EUR3
    ws.cell(row=r, column=3).font = GREEN
    setw(ws, [26, 60, 20, 14, 20, 16])
    # tornado chart
    ch = BarChart()
    ch.type = "bar"
    ch.title = "Écart de coût mensuel vs base (€, abonné Premium)"
    data = Reference(ws, min_col=4, min_row=base_row + 1, max_row=base_row + len(cases) - 1)
    cats = Reference(ws, min_col=1, min_row=base_row + 1, max_row=base_row + len(cases) - 1)
    ch.add_data(data, titles_from_data=False)
    ch.set_categories(cats)
    ch.legend = None
    ch.height = 8
    ch.width = 16
    ch.series[0].graphicalProperties.solidFill = PALETTE["glow_deep"]
    ch.x_axis.delete = False
    ch.y_axis.delete = False
    ws.add_chart(ch, "H4")


# ---------------------------------------------------------------------------
def write_protections(ws, rows, syn):
    r0, r_last, rt, ra, ra2 = rows
    title(ws, "Protections contre les coûts excessifs", "Plafonds par offre (bleu) et coût au plafond. Un abonné qui atteint un plafond est informé ; le dépassement est une décision de Produit, pas un automatisme.")
    header(ws, 4, ["Protection", "Règle", "Personal", "Premium", "Family", "Note"], height=30)
    r = 5
    for name, rule, vals, note in PROTECTIONS:
        ws.cell(row=r, column=1, value=name).font = BOLD
        c = ws.cell(row=r, column=2, value=rule)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
        for j, v in enumerate(vals):
            cc = ws.cell(row=r, column=3 + j, value=v)
            cc.font = BLUE if isinstance(v, (int, float)) else BLACK
            if isinstance(v, (int, float)):
                cc.number_format = NUM if v >= 1 else PCT
        n = ws.cell(row=r, column=6, value=note)
        n.font = SMALL
        n.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 32
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Coût au plafond (ordre de grandeur)").font = BOLD
    r += 1
    header(ws, r, ["Poste", "Formule", "Personal", "Premium", "Family", "Note"], height=20)
    r += 1
    # rows: missions cap × coût moyen par exécution + browser cap × browser price + frontier
    cap_missions_row = 5  # first protection row = missions cap
    cap_brw_row = 6
    idx = {m["num"]: i for i, m in enumerate(MISSIONS)}
    rm = lambda n: r0 + idx[n]
    cx = MCOL['c_exec']; cm = MCOL['c_month']; fq = MCOL['freq']
    book_avg = f"AVERAGE(Missions!{cx}{rm('M3')},Missions!{cx}{rm('M4')})"
    read_avg = (f"((Missions!{cm}{rt}-Missions!{cm}{rm('M3')}-Missions!{cm}{rm('M4')}-Missions!{cm}{rm('M10')})"
                f"/(Missions!{fq}{rt}-Missions!{fq}{rm('M3')}-Missions!{fq}{rm('M4')}-Missions!{fq}{rm('M10')}))")
    ws.cell(row=r, column=1, value="Réservations possibles au plafond de navigateur (minutes ÷ 7 par réservation)").font = BLACK
    ws.cell(row=r, column=2, value="plafond de minutes ÷ 7").font = SMALL
    for j in range(3):
        c = ws.cell(row=r, column=3 + j, value=f"={L(3 + j)}{cap_brw_row}/7")
        c.number_format = NUM1
        c.font = BLACK
    r_book = r
    r += 1
    ws.cell(row=r, column=1, value="Coût des réservations au plafond (× coût moyen d'une réservation M3, M4)").font = BLACK
    ws.cell(row=r, column=2, value="réservations × moyenne(M3, M4)").font = SMALL
    for j in range(3):
        c = ws.cell(row=r, column=3 + j, value=f"={L(3 + j)}{r_book}*{book_avg}")
        c.number_format = EUR2
        c.font = BLACK
    r += 1
    ws.cell(row=r, column=1, value="Autres missions au plafond (× coût moyen des missions sans navigateur, socle compris)").font = BLACK
    ws.cell(row=r, column=2, value="(plafond missions − réservations) × moyenne hors M3, M4, M10").font = SMALL
    for j in range(3):
        c = ws.cell(row=r, column=3 + j, value=f"=MAX(0,{L(3 + j)}{cap_missions_row}-{L(3 + j)}{r_book})*{read_avg}")
        c.number_format = EUR2
        c.font = BLACK
    r += 1
    ws.cell(row=r, column=1, value="Coût maximal IA, outils et support par abonné et par mois").font = BOLD
    for j in range(3):
        c = ws.cell(row=r, column=3 + j, value=f"={L(3 + j)}{r - 2}+{L(3 + j)}{r - 1}")
        c.number_format = EUR2
        c.font = BOLD
        c.fill = YELLOW
    r += 1
    ws.cell(row=r, column=1, value="En part du prix HT").font = BLACK
    for j, o in enumerate(OFFERS):
        c = ws.cell(row=r, column=3 + j, value=f"={L(3 + j)}{r - 1}/({o['price_ttc']}/1.2)")
        c.number_format = PCT
        c.font = BLACK
    setw(ws, [40, 52, 12, 12, 12, 60])


# ---------------------------------------------------------------------------
def write_charge(ws):
    title(ws, "Plan de charge et budget MVP", "Jours par profil et par chantier, deux variantes : Lean (un développeur senior externe, fondateurs à la manœuvre) et Confort (deux développeurs). Taux journaliers sourcés (vert) ou hypothèses (bleu).")
    # Rates table
    ws["A4"] = "Taux journaliers HT"
    ws["A4"].font = BOLD
    header(ws, 5, ["Profil", "TJM retenu (€ HT)", "Fourchette source", "Nature", "Source", "Date"], height=30)
    r = 6
    RATE_CELL = {}
    for key, prof, val, rng, nature, src, date in RATES:
        ws.cell(row=r, column=1, value=prof).font = BLACK
        c = ws.cell(row=r, column=2, value=val)
        c.font = BLUE
        c.number_format = EUR
        if nature == "Tarif public":
            c.fill = EUCF
        ws.cell(row=r, column=3, value=rng).font = SMALL
        ws.cell(row=r, column=4, value=nature).font = SMALL
        s = ws.cell(row=r, column=5, value=src)
        s.font = SMALL
        s.alignment = Alignment(wrap_text=True)
        ws.cell(row=r, column=6, value=date).font = SMALL
        RATE_CELL[key] = f"$B${r}"
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Chantiers").font = BOLD
    r += 1
    header(ws, r, ["Chantier", "Profil", "Jours Lean", "Jours Confort", "Coût Lean (€ HT)", "Coût Confort (€ HT)", "Dépendances et notes"], height=30)
    r += 1
    first = r
    for chantier, prof_key, d_lean, d_conf, note in WORKLOAD:
        ws.cell(row=r, column=1, value=chantier).font = BLACK
        prof_label = next(p for k, p, *_ in RATES if k == prof_key)
        ws.cell(row=r, column=2, value=prof_label).font = BLACK
        c3 = ws.cell(row=r, column=3, value=d_lean); c3.font = BLUE; c3.number_format = NUM1
        c4 = ws.cell(row=r, column=4, value=d_conf); c4.font = BLUE; c4.number_format = NUM1
        c5 = ws.cell(row=r, column=5, value=f"=C{r}*{RATE_CELL[prof_key]}"); c5.font = BLACK; c5.number_format = EUR
        c6 = ws.cell(row=r, column=6, value=f"=D{r}*{RATE_CELL[prof_key]}"); c6.font = BLACK; c6.number_format = EUR
        n = ws.cell(row=r, column=7, value=note); n.font = SMALL; n.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 26
        r += 1
    last = r - 1
    ws.cell(row=r, column=1, value="Total jours et coût de main-d'œuvre externe").font = BOLD
    for col in (3, 4, 5, 6):
        c = ws.cell(row=r, column=col, value=f"=SUM({L(col)}{first}:{L(col)}{last})")
        c.font = BOLD
        c.number_format = NUM1 if col in (3, 4) else EUR
        c.border = BOT
    rlab = r
    r += 1
    ws.cell(row=r, column=1, value="dont jours des fondateurs (non facturés)").font = BLACK
    for col in (3, 4):
        c = ws.cell(row=r, column=col, value=f"=SUMIF($B${first}:$B${last},\"Fondateur*\",{L(col)}{first}:{L(col)}{last})")
        c.font = BLACK
        c.number_format = NUM1
    r += 2
    ws.cell(row=r, column=1, value="Autres coûts du MVP (hors main-d'œuvre externe)").font = BOLD
    r += 1
    header(ws, r, ["Poste", "Base", "Lean (€ HT)", "Confort (€ HT)", "", "", "Source ou hypothèse"], height=20)
    r += 1
    first2 = r
    for poste, base, lean, conf, src in NONLABOUR:
        ws.cell(row=r, column=1, value=poste).font = BLACK
        ws.cell(row=r, column=2, value=base).font = SMALL
        c3 = ws.cell(row=r, column=3, value=lean); c3.font = BLUE if isinstance(lean, (int, float)) else BLACK; c3.number_format = EUR
        c4 = ws.cell(row=r, column=4, value=conf); c4.font = BLUE if isinstance(conf, (int, float)) else BLACK; c4.number_format = EUR
        n = ws.cell(row=r, column=7, value=src); n.font = SMALL; n.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 26
        r += 1
    last2 = r - 1
    ws.cell(row=r, column=1, value="Sous-total autres coûts").font = BOLD
    for col in (3, 4):
        c = ws.cell(row=r, column=col, value=f"=SUM({L(col)}{first2}:{L(col)}{last2})")
        c.font = BOLD
        c.number_format = EUR
        c.border = BOT
    rsub = r
    r += 2
    ws.cell(row=r, column=1, value="Budget MVP").font = BOLD
    r += 1
    ws.cell(row=r, column=1, value="Main-d'œuvre externe").font = BLACK
    ws.cell(row=r, column=3, value=f"=E{rlab}").number_format = EUR
    ws.cell(row=r, column=4, value=f"=F{rlab}").number_format = EUR
    r += 1
    ws.cell(row=r, column=1, value="Autres coûts").font = BLACK
    ws.cell(row=r, column=3, value=f"=C{rsub}").number_format = EUR
    ws.cell(row=r, column=4, value=f"=D{rsub}").number_format = EUR
    r += 1
    ws.cell(row=r, column=1, value="Imprévus (15 %, comme le Business plan Lean V1)").font = BLACK
    ws.cell(row=r, column=3, value=f"=(C{r - 2}+C{r - 1})*0.15").number_format = EUR
    ws.cell(row=r, column=4, value=f"=(D{r - 2}+D{r - 1})*0.15").number_format = EUR
    r += 1
    ws.cell(row=r, column=1, value="Total budget MVP HT").font = BOLD
    for col in (3, 4):
        c = ws.cell(row=r, column=col, value=f"=SUM({L(col)}{r - 3}:{L(col)}{r - 1})")
        c.font = BOLD
        c.number_format = EUR
        c.fill = YELLOW
    rtotal = r
    r += 1
    ws.cell(row=r, column=1, value="Business plan Lean V1 (Finance)").font = BLACK
    ws.cell(row=r, column=3, value=77050).number_format = EUR
    ws.cell(row=r, column=3).font = BLUE
    ws.cell(row=r, column=4, value=77050).number_format = EUR
    ws.cell(row=r, column=4).font = BLUE
    r += 1
    ws.cell(row=r, column=1, value="Écart").font = BLACK
    for col in (3, 4):
        c = ws.cell(row=r, column=col, value=f"={L(col)}{rtotal}-{L(col)}{r - 1}")
        c.number_format = EUR
        c.font = BLACK
    r += 1
    ws.cell(row=r, column=1, value="Modèle 36 mois : prudent 100 000 €, central 77 050 €, ambitieux 60 000 €").font = SMALL
    setw(ws, [52, 30, 13, 13, 15, 15, 70])
    return rtotal


# ---------------------------------------------------------------------------
def write_common(ws, rows):
    r0, r_last, rt, ra, ra2 = rows
    title(ws, "Tableau commun demandé par Finance", "Mission | priorité | scénario d'exécution | modèle IA | appels et outils | coût estimé HT | taux de réussite | risque | décision recommandée. Les coûts sont liés à l'onglet Missions.")
    header(ws, 4, ["Mission", "Priorité", "Scénario d'exécution", "Modèle IA", "Appels et outils", "Coût estimé HT par exécution", "Coût mensuel Premium", "Taux de réussite (estimé, non mesuré)", "Risque principal", "Décision recommandée"], height=44)
    r = 5
    idx = {m["num"]: i for i, m in enumerate(MISSIONS)}
    for row in COMMON_TABLE:
        num = row[0]
        mr = r0 + idx[num]
        m = MISSIONS[idx[num]]
        vals = [f"{num} {m['name']}", m["prio"], row[1], row[2], row[3], f"=Missions!{MCOL['c_exec']}{mr}", f"=Missions!{MCOL['c_month']}{mr}", f"=Missions!{MCOL['succ']}{mr}", row[4], row[5]]
        for j, v in enumerate(vals, start=1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = GREEN if (isinstance(v, str) and v.startswith("=")) else (BOLD if j == 1 else SMALL)
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = THINB
            if j == 6:
                c.number_format = EUR3
            elif j == 7:
                c.number_format = EUR2
            elif j == 8:
                c.number_format = PCT
        ws.row_dimensions[r].height = 92
        r += 1
    setw(ws, [26, 9, 46, 18, 34, 12, 12, 12, 34, 40])
    ws.freeze_panes = "B5"
    ws.page_setup.orientation = "landscape"


# ---------------------------------------------------------------------------
def main():
    wb = Workbook()
    ws_readme = wb.active
    ws_readme.title = "LISEZ-MOI"
    ws_tarifs = wb.create_sheet("Tarifs")
    ws_missions = wb.create_sheet("Missions")
    ws_syn = wb.create_sheet("Synthèse")
    ws_sens = wb.create_sheet("Sensibilité")
    ws_prot = wb.create_sheet("Protections")
    ws_charge = wb.create_sheet("Plan de charge")
    ws_common = wb.create_sheet("Tableau commun")
    write_readme(ws_readme)
    write_tarifs(ws_tarifs)
    rows = write_missions(ws_missions)
    syn = write_synthese(ws_syn, rows)
    write_sensibilite(ws_sens, rows, syn)
    write_protections(ws_prot, rows, syn)
    write_charge(ws_charge)
    write_common(ws_common, rows)
    for ws in wb.worksheets:
        ws.sheet_properties.tabColor = PALETTE["glow"] if ws.title in ("Synthèse", "Tableau commun") else PALETTE["linen"]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    wb.save(OUT)
    print("écrit :", OUT)


if __name__ == "__main__":
    main()
