"""Build the Helium 36-month financial model (live formulas) with openpyxl.

Sheets: Lisez-moi, Hypothèses, Économie unitaire, Modèle Prudent / Central /
Ambitieux, Synthèse, Tornade (+ S01..S10 sensitivity copies of the Central
model), KPI, Financement.
"""
import os, sys, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.utils import get_column_letter as L
from openpyxl.chart import BarChart, Reference
from openpyxl.worksheet.properties import PageSetupProperties
from openpyxl.comments import Comment

sys.path.insert(0, os.path.dirname(__file__))
from helium_brand import PALETTE

OUT = "/home/claude/helium-work/out/finance/Helium_Modele_financier_36m_V1.xlsx"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

ARIAL = "Arial"
BLUE = Font(name=ARIAL, size=10, color="0000FF")
BLACK = Font(name=ARIAL, size=10, color="000000")
GREEN = Font(name=ARIAL, size=10, color="008000")
BOLD = Font(name=ARIAL, size=10, bold=True)
HEAD = Font(name=ARIAL, size=10, bold=True, color=PALETTE["ink"])
TITLE = Font(name="Georgia", size=16, color=PALETTE["ink"])
SUB = Font(name=ARIAL, size=9, italic=True, color=PALETTE["stone"])
YELLOW = PatternFill("solid", fgColor="FFFF00")
MIST = PatternFill("solid", fgColor=PALETTE["mist"])
GLOWF = PatternFill("solid", fgColor=PALETTE["glow"])
THIN = Side(style="thin", color=PALETTE["linen"])
BOT = Border(bottom=Side(style="thin", color=PALETTE["glow"]))

EUR = '#,##0" €";(#,##0" €");"-"'
EUR2 = '#,##0.00" €";(#,##0.00" €");"-"'
PCT = '0.0%;(0.0%);"-"'
NUM = '#,##0;(#,##0);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
MULT = '0.00"x";(0.00"x");"-"'
DATE = 'mmm-yy'

N = 36  # months
FIRST = 3  # first month column index (C)


def mcol(m):
    """Column letter of month m (1-based)."""
    return L(FIRST + m - 1)


# ---------------------------------------------------------------- assumptions
# key: (label, unit, prudent, central, ambitieux, format, comment)
ASSUMPTIONS = [
    ("__sec", "Calendrier", None, None, None, None, None, None),
    ("start_date", "Date de début du modèle (M1)", "date", datetime.date(2026, 11, 1), datetime.date(2026, 11, 1), datetime.date(2026, 11, 1), DATE, "Hypothèse de calendrier : M1 = novembre 2026. Modifiable."),
    ("pilot_month", "Mois de démarrage du pilote payant", "mois", 4, 3, 3, NUM, "Plan Ventes 90 jours : 10 pilotes payants entre J31 et J60 (4 VENTES/2026 1027 01 Synthese executive)."),
    ("pilot_subs", "Taille de la cohorte pilote payante", "abonnés", 10, 10, 10, NUM, "Même source. Les pilotes paient le prix public."),
    ("launch_month", "Mois de lancement commercial", "mois", 10, 7, 6, NUM, "Finance V3 : lancement M7 (central) / M10 (prudent). Source : 2 FINANCE/TRESORERIE/2026 1027 Synthese tresorerie V3."),
    ("__sec", "Prix et mix (TTC par mois)", None, None, None, None, None, None),
    ("price_personal", "Prix Personal TTC", "€/mois", 29, 29, 29, EUR, "BMC V2, hypothèse H01 non validée. À tester (Van Westendorp)."),
    ("price_premium", "Prix Premium TTC", "€/mois", 79, 79, 79, EUR, "BMC V2, hypothèse H01 non validée."),
    ("price_family", "Prix Family TTC", "€/mois", 129, 129, 129, EUR, "BMC V2, hypothèse H01 non validée."),
    ("vat", "TVA", "%", 0.20, 0.20, 0.20, PCT, "Taux normal France (hypothèse H02). Ventes B2C UE hors France : TVA du pays du client (OSS)."),
    ("mix_personal", "Part Personal dans les abonnés", "%", 0.30, 0.25, 0.20, PCT, "Hypothèse de mix. Aucune donnée observée."),
    ("mix_premium", "Part Premium", "%", 0.55, 0.60, 0.60, PCT, "Hypothèse de mix."),
    ("mix_family", "Part Family", "%", 0.15, 0.15, 0.20, PCT, "Hypothèse de mix. Doit sommer à 100 % avec les deux lignes précédentes."),
    ("__sec", "Acquisition", None, None, None, None, None, None),
    ("acq_y1", "Budget d'acquisition mensuel, du lancement à M12", "€ HT/mois", 2000, 3000, 4000, EUR, "Hypothèse. Finance V3 : 24 188 € d'acquisition en A1 (central)."),
    ("acq_y2", "Budget d'acquisition mensuel, M13 à M24", "€ HT/mois", 6000, 10000, 12000, EUR, "Hypothèse. Finance V3 : 121 688 € en A2."),
    ("acq_y3", "Budget d'acquisition mensuel, M25 à M36", "€ HT/mois", 12000, 25000, 25000, EUR, "Hypothèse. Finance V3 : 340 275 € en A3."),
    ("cac", "CAC (coût par abonné payant acquis)", "€", 240, 150, 110, EUR, "Hypothèse H04 (150 €) et prudent (240 €). Benchmarks : CPI iOS 4,70 $ (Adapty 2026) / conversion téléchargement → payant 2 % (RevenueCat 2026) ≈ 235 $ par abonné payant en acquisition payante ; 44 $ avec paywall et essai. Réseau et parrainage visés pour rester sous 150 €. Non mesuré."),
    ("referral", "Acquisition organique (parrainage), % de la base par mois", "%", 0.01, 0.02, 0.025, PCT, "Hypothèse. À mesurer pendant le pilote."),
    ("__sec", "Rétention et encaissement", None, None, None, None, None, None),
    ("churn", "Churn mensuel (résiliations / abonnés début de mois)", "%", 0.06, 0.03, 0.025, PCT, "Hypothèse H05 (3 %). Benchmarks : Recurly juillet 2026, ARPU 10 à 25 $ : 4,3 % par mois ; ProfitWell, ARPU 25 à 50 $ : 6,9 % par mois ; RevenueCat 2026, applications IA en plan mensuel : 6 % de rétention à 12 mois (churn précoce très élevé). Prudent fixé à 6 %. Non mesuré."),
    ("unpaid", "Impayés, % de la facturation", "%", 0.02, 0.01, 0.005, PCT, "Scénario prudent Finance : 2 %."),
    ("fee_pct", "Frais de paiement, % du montant encaissé", "%", 0.015, 0.015, 0.015, PCT, "Ordre de grandeur Stripe cartes EEE : 1,5 % + 0,25 €. À vérifier sur la grille en vigueur."),
    ("fee_fixed", "Frais de paiement fixes par transaction", "€", 0.25, 0.25, 0.25, EUR2, "Idem."),
    ("__sec", "Coûts variables (HT, par abonné et par mois)", None, None, None, None, None, None),
    ("missions_personal", "Missions exécutées par mois, Personal", "missions", 20, 20, 20, NUM, "Hypothèse d'usage. À mesurer (demande de cadrage Finance → Produit)."),
    ("missions_premium", "Missions exécutées par mois, Premium", "missions", 60, 60, 60, NUM, "Hypothèse : 2 missions par jour ouvré."),
    ("missions_family", "Missions exécutées par mois, Family", "missions", 90, 90, 90, NUM, "Hypothèse."),
    ("cost_mission", "Coût IA et outils par mission (tokens, API, reprises)", "€ HT", 0.30, 0.18, 0.12, EUR2, "Hypothèse conservée au-dessus de l'estimation ascendante : le classeur Technique/Helium_Cout_par_mission_V1.xlsx (28/10/2026, prix publics Mistral, Anthropic via Bedrock UE, Brave, Places, Browserbase) donne environ 0,07 € par mission visible pour un abonné Premium, socle nocturne réparti, et environ 1 € pour une prise de rendez-vous par navigateur piloté (support humain compris). 0,18 € (central) couvre 2,5 fois l'estimation ; 0,30 € (prudent) est le seuil au-delà duquel le plan prévoit limites d'usage et test de prix. Référence externe : tau2-bench 0,26 à 0,49 $ par trajectoire (classe Sonnet). À remplacer par les mesures des missions 1 et 5 (3 décembre) puis 3 et 4 (19 décembre)."),
    ("hosting", "Hébergement, stockage, connecteurs", "€ HT", 2.0, 1.5, 1.0, EUR2, "Hypothèse."),
    ("support", "Support humain (minutes × coût horaire)", "€ HT", 5.0, 3.0, 2.0, EUR2, "Hypothèse."),
    ("__sec", "Coûts fixes (HT, par mois)", None, None, None, None, None, None),
    ("founders_paid", "Nombre de fondateurs rémunérés à partir du mois ci-dessous", "personnes", 2, 2, 2, NUM, "Hypothèse Finance : fondateurs non rémunérés M1 à M12."),
    ("salary_start", "Premier mois de rémunération des fondateurs", "mois", 13, 13, 13, NUM, "Idem."),
    ("founder_cost", "Coût chargé mensuel par fondateur rémunéré", "€ HT", 5500, 5000, 5000, EUR, "Hypothèse modeste (≈ 3 000 € nets + charges, régime assimilé salarié)."),
    ("e1_start", "Embauche 1 (growth / customer success), premier mois", "mois", 16, 13, 10, NUM, "Plan Ventes : growth 0,5 ETP puis customer success."),
    ("e1_cost", "Coût chargé mensuel, embauche 1", "€ HT", 4500, 4500, 4500, EUR, "Hypothèse."),
    ("e2_start", "Embauche 2 (ingénieur), premier mois", "mois", 24, 19, 14, NUM, "Hypothèse."),
    ("e2_cost", "Coût chargé mensuel, embauche 2", "€ HT", 6500, 6500, 6500, EUR, "Hypothèse."),
    ("mvp_budget", "Budget MVP externe (développement, UX, sécurité, juridique)", "€ HT", 100000, 77050, 60000, EUR, "Business plan Lean V1 : 77 050 € HT (central), 100 000 € (prudent). Étalé de M1 au mois précédant le lancement."),
    ("tools", "Outils et SaaS", "€ HT/mois", 400, 400, 400, EUR, "Hypothèse."),
    ("legal", "Juridique et expertise comptable", "€ HT/mois", 1000, 800, 800, EUR, "Hypothèse."),
    ("insurance", "Assurance RC professionnelle (à partir du lancement)", "€/mois", 150, 150, 150, EUR, "Hypothèse. Pas de TVA."),
    ("mkt_fixed", "Marketing fixe (marque, contenu), à partir du lancement", "€ HT/mois", 500, 1000, 1500, EUR, "Hypothèse."),
    ("ga", "Frais généraux", "€ HT/mois", 300, 300, 300, EUR, "Hypothèse."),
    ("audit", "Audit de sécurité annuel (évaluation CASA Tier 2 pour les scopes Gmail restreints, renouvelée chaque année)", "€ HT/an", 8000, 5000, 3000, EUR, "Scopes Gmail « restreints » : vérification Google + CASA Tier 2 annuelle, laboratoires 540 à 3 000 $ et plus, 4 à 6 semaines (Nango, Switch Labs, 2026). Le montant inclut le temps de préparation interne."),
    ("setup", "Frais de constitution (M2)", "€ HT", 2500, 2500, 2500, EUR, "Hypothèse : immatriculation, conseil, dépôt de marque."),
    ("reserve", "Réserve de sécurité cible", "€", 60000, 40000, 30000, EUR, "Finance V3 : 60 000 € (prudent), 40 500 € (central)."),
    ("cash0", "Trésorerie initiale (apports déjà versés)", "€", 0, 0, 0, EUR, "Non établi par les sources."),
    ("__sec", "Financement (désactivé par défaut : 0 = trésorerie avant financement)", None, None, None, None, None, None),
    ("fin_on", "Inclure le financement dans la trésorerie (1 = oui, 0 = non)", "0/1", 0, 0, 0, NUM, "Mettre 1 pour simuler le plan de financement de l'onglet Financement."),
    ("fin1_month", "Tranche 1, mois", "mois", 2, 2, 2, NUM, "Voir onglet Financement."),
    ("fin1_amt", "Tranche 1, montant", "€", 15000, 15000, 15000, EUR, "Apports fondateurs, hypothèse."),
    ("fin2_month", "Tranche 2, mois", "mois", 10, 7, 6, NUM, "À la création / au lancement."),
    ("fin2_amt", "Tranche 2, montant", "€", 150000, 150000, 150000, EUR, "Prêts d'honneur, Bourse French Tech, business angels : éligibilité non vérifiée."),
    ("fin3_month", "Tranche 3, mois", "mois", 16, 13, 13, NUM, ""),
    ("fin3_amt", "Tranche 3, montant", "€", 450000, 300000, 250000, EUR, "Amorçage, sous réserve de traction."),
]

ROW = {}  # key -> row in Hypothèses


def write_assumptions(ws):
    ws.title = "Hypothèses"
    ws["A1"] = "Hypothèses par scénario"
    ws["A1"].font = TITLE
    ws["A2"] = "Cellules bleues = entrées modifiables. Colonne F = scénario actif (sélecteur en F3). Chaque ligne cite sa source ou dit qu'elle est une hypothèse."
    ws["A2"].font = SUB
    ws["E3"] = "Scénario actif (1 = Prudent, 2 = Central, 3 = Ambitieux)"
    ws["E3"].font = BOLD
    ws["E3"].alignment = Alignment(horizontal="right")
    ws["F3"] = 2
    ws["F3"].font = BLUE
    ws["F3"].fill = YELLOW
    heads = ["Hypothèse", "Unité", "Prudent", "Central", "Ambitieux", "Actif", "Source / commentaire"]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=5, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
    r = 6
    for key, label, unit, p, c, a, fmt, com in ASSUMPTIONS:
        if key == "__sec":
            cell = ws.cell(row=r, column=1, value=label)
            cell.font = Font(name=ARIAL, size=10, bold=True, color=PALETTE["glow_deep"])
            r += 1
            continue
        ROW[key] = r
        ws.cell(row=r, column=1, value=label).font = BLACK
        ws.cell(row=r, column=2, value=unit).font = SUB
        for j, v in zip((3, 4, 5), (p, c, a)):
            cell = ws.cell(row=r, column=j, value=v)
            cell.font = BLUE
            cell.number_format = fmt
        act = ws.cell(row=r, column=6, value=f"=INDEX(C{r}:E{r},1,$F$3)")
        act.font = BLACK
        act.number_format = fmt
        ws.cell(row=r, column=7, value=com).font = SUB
        r += 1
    # mix check
    ws.cell(row=r + 1, column=1, value="Contrôle : somme du mix (doit être 100 %)").font = BOLD
    for j in (3, 4, 5, 6):
        col = L(j)
        cell = ws.cell(row=r + 1, column=j, value=f"={col}{ROW['mix_personal']}+{col}{ROW['mix_premium']}+{col}{ROW['mix_family']}")
        cell.number_format = PCT
        cell.font = BLACK
    ws.column_dimensions["A"].width = 58
    ws.column_dimensions["B"].width = 12
    for col in "CDEF":
        ws.column_dimensions[col].width = 14
    ws.column_dimensions["G"].width = 90
    ws.freeze_panes = "C6"


def H(key, scol):
    """Reference to an assumption in the given scenario column letter."""
    return f"Hypothèses!${scol}${ROW[key]}"


# ------------------------------------------------------------- model sheet
MR = {}  # model row map (filled once, identical on every model sheet)


def write_model(ws, title, scol, shocks):
    """shocks: dict with keys price, churn, cac, ai, fixed (multipliers) and delay (months)."""
    ws["A1"] = title
    ws["A1"].font = TITLE
    ws["A2"] = "Flux en € HT sauf mention TTC. Formules vivantes ; ne saisir que dans l'onglet Hypothèses et la ligne de chocs ci-dessous."
    ws["A2"].font = SUB
    shock_labels = [("C", "price", "Prix ×"), ("D", "churn", "Churn ×"), ("E", "cac", "CAC ×"),
                    ("F", "ai", "Coût IA ×"), ("G", "fixed", "Coûts fixes ×"), ("H", "delay", "Retard lancement (mois)")]
    ws["A3"] = "Chocs de sensibilité (1 = aucun ; retard en mois)"
    ws["A3"].font = BOLD
    for col, k, lab in shock_labels:
        ws[f"{col}3"] = lab
        ws[f"{col}3"].font = SUB
        ws[f"{col}3"].alignment = Alignment(horizontal="center", wrap_text=True)
        ws[f"{col}4"] = shocks[k]
        ws[f"{col}4"].font = BLUE
        ws[f"{col}4"].fill = YELLOW
        ws[f"{col}4"].number_format = '0.00' if k != "delay" else '0'
    S = {k: f"${col}$4" for col, k, _ in shock_labels}

    # effective calendar (row 5)
    ws["A5"] = "Mois de lancement effectif"
    ws["A5"].font = BOLD
    ws["B5"] = f"={H('launch_month', scol)}+{S['delay']}"
    ws["B5"].font = GREEN
    ws["B5"].number_format = NUM
    LAUNCH = "$B$5"

    r = 7
    rows = []  # (key, label, unit, fmt, formula_builder, style)

    def add(key, label, unit, fmt, fb, style="n"):
        rows.append((key, label, unit, fmt, fb, style))

    def prev(key):
        return lambda m: (f"{mcol(m-1)}{MR[key]}" if m > 1 else "0")

    # Calendar
    add("month", "Mois", "n°", NUM, lambda m: m, "h")
    add("date", "Date", "", DATE, lambda m: f"=EDATE({H('start_date', scol)},{mcol(m)}{MR['month']}-1)", "h")
    add("launched", "Lancé ? (1 = oui)", "0/1", NUM, lambda m: f"=IF({mcol(m)}{MR['month']}>={LAUNCH},1,0)")
    add("pilot", "Pilote en cours ? (1 = oui)", "0/1", NUM, lambda m: f"=IF(AND({mcol(m)}{MR['month']}>={H('pilot_month', scol)},{mcol(m)}{MR['month']}<{LAUNCH}),1,0)")
    add("acq_budget", "Budget d'acquisition du mois", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['launched']}=1,IF({mcol(m)}{MR['month']}<=12,{H('acq_y1', scol)},IF({mcol(m)}{MR['month']}<=24,{H('acq_y2', scol)},{H('acq_y3', scol)})),0)")
    add("__sec", "Abonnés", "", None, None)
    add("open", "Abonnés en début de mois", "abonnés", NUM1, lambda m: f"={prev('close')(m)}")
    add("new_paid", "Nouveaux abonnés par acquisition payante", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['acq_budget']}/({H('cac', scol)}*{S['cac']})")
    add("new_pilot", "Nouveaux abonnés pilote", "abonnés", NUM1, lambda m: f"=IF({mcol(m)}{MR['month']}={H('pilot_month', scol)},{H('pilot_subs', scol)},0)")
    add("new_org", "Nouveaux abonnés organiques (parrainage)", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['launched']}*{mcol(m)}{MR['open']}*{H('referral', scol)}")
    add("churned", "Résiliations", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['open']}*{H('churn', scol)}*{S['churn']}")
    add("close", "Abonnés en fin de mois", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['open']}+{mcol(m)}{MR['new_paid']}+{mcol(m)}{MR['new_pilot']}+{mcol(m)}{MR['new_org']}-{mcol(m)}{MR['churned']}", "b")
    add("sub_p", "dont Personal", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['close']}*{H('mix_personal', scol)}")
    add("sub_pr", "dont Premium", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['close']}*{H('mix_premium', scol)}")
    add("sub_f", "dont Family", "abonnés", NUM1, lambda m: f"={mcol(m)}{MR['close']}*{H('mix_family', scol)}")
    add("__sec", "Revenus", "", None, None)
    add("mrr_p", "Facturation Personal TTC", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['sub_p']}*{H('price_personal', scol)}*{S['price']}")
    add("mrr_pr", "Facturation Premium TTC", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['sub_pr']}*{H('price_premium', scol)}*{S['price']}")
    add("mrr_f", "Facturation Family TTC", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['sub_f']}*{H('price_family', scol)}*{S['price']}")
    add("billing", "Facturation totale TTC (MRR TTC)", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['mrr_p']}+{mcol(m)}{MR['mrr_pr']}+{mcol(m)}{MR['mrr_f']}", "b")
    add("vat_out", "TVA collectée", "€", EUR, lambda m: f"={mcol(m)}{MR['billing']}*{H('vat', scol)}/(1+{H('vat', scol)})")
    add("rev_ht", "Chiffre d'affaires HT", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['billing']}-{mcol(m)}{MR['vat_out']}", "b")
    add("unpaid", "Impayés (TTC)", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['billing']}*{H('unpaid', scol)}")
    add("fees", "Frais de paiement", "€", EUR, lambda m: f"=({mcol(m)}{MR['billing']}-{mcol(m)}{MR['unpaid']})*{H('fee_pct', scol)}+{mcol(m)}{MR['close']}*{H('fee_fixed', scol)}")
    add("receipts", "Encaissements nets TTC", "€ TTC", EUR, lambda m: f"={mcol(m)}{MR['billing']}-{mcol(m)}{MR['unpaid']}-{mcol(m)}{MR['fees']}", "b")
    add("__sec", "Coûts variables", "", None, None)
    add("ai_cost", "Coût IA et outils (missions × coût par mission)", "€ HT", EUR, lambda m: f"=({mcol(m)}{MR['sub_p']}*{H('missions_personal', scol)}+{mcol(m)}{MR['sub_pr']}*{H('missions_premium', scol)}+{mcol(m)}{MR['sub_f']}*{H('missions_family', scol)})*{H('cost_mission', scol)}*{S['ai']}")
    add("host_cost", "Hébergement, stockage, connecteurs", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['close']}*{H('hosting', scol)}")
    add("supp_cost", "Support humain", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['close']}*{H('support', scol)}")
    add("var_cost", "Total coûts variables", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['ai_cost']}+{mcol(m)}{MR['host_cost']}+{mcol(m)}{MR['supp_cost']}", "b")
    add("contrib", "Marge sur coûts variables (CA HT − variables − frais − impayés HT)", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['rev_ht']}-{mcol(m)}{MR['var_cost']}-{mcol(m)}{MR['fees']}-{mcol(m)}{MR['unpaid']}/(1+{H('vat', scol)})", "b")
    add("__sec", "Acquisition et coûts fixes", "", None, None)
    add("acq_spend", "Dépenses d'acquisition", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['acq_budget']}")
    add("fx_founders", "Rémunération des fondateurs", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['month']}>={H('salary_start', scol)},{H('founders_paid', scol)}*{H('founder_cost', scol)},0)*{S['fixed']}")
    add("fx_e1", "Salarié 1 (growth / customer success)", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['month']}>={H('e1_start', scol)},{H('e1_cost', scol)},0)*{S['fixed']}")
    add("fx_e2", "Salarié 2 (ingénieur)", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['month']}>={H('e2_start', scol)},{H('e2_cost', scol)},0)*{S['fixed']}")
    add("fx_mvp", "Développement MVP externe (étalé jusqu'au lancement)", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['month']}<{LAUNCH},{H('mvp_budget', scol)}/MAX(1,{LAUNCH}-1),0)")
    add("fx_tools", "Outils et SaaS", "€ HT", EUR, lambda m: f"={H('tools', scol)}*{S['fixed']}")
    add("fx_legal", "Juridique et comptabilité", "€ HT", EUR, lambda m: f"={H('legal', scol)}*{S['fixed']}")
    add("fx_ins", "Assurance RC pro", "€", EUR, lambda m: f"={mcol(m)}{MR['launched']}*{H('insurance', scol)}*{S['fixed']}")
    add("fx_mkt", "Marketing fixe", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['launched']}*{H('mkt_fixed', scol)}*{S['fixed']}")
    add("fx_ga", "Frais généraux", "€ HT", EUR, lambda m: f"={H('ga', scol)}*{S['fixed']}")
    add("fx_audit", "Audit de sécurité (annuel, à partir du lancement)", "€ HT", EUR, lambda m: f"=IF(AND({mcol(m)}{MR['launched']}=1,MOD({mcol(m)}{MR['month']}-{LAUNCH},12)=0),{H('audit', scol)},0)*{S['fixed']}")
    add("fx_setup", "Frais de constitution", "€ HT", EUR, lambda m: f"=IF({mcol(m)}{MR['month']}=2,{H('setup', scol)},0)")
    add("fixed", "Total coûts fixes", "€ HT", EUR, lambda m: f"=SUM({mcol(m)}{MR['fx_founders']}:{mcol(m)}{MR['fx_setup']})", "b")
    add("ebitda", "EBITDA (marge variable − acquisition − fixes)", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['contrib']}-{mcol(m)}{MR['acq_spend']}-{mcol(m)}{MR['fixed']}", "b")
    add("ebitda_pos", "EBITDA positif ? (1 = oui)", "0/1", NUM, lambda m: f"=IF({mcol(m)}{MR['ebitda']}>0,1,0)")
    add("__sec", "Trésorerie", "", None, None)
    add("vat_pay", "TVA collectée reversée (mois suivant)", "€", EUR, lambda m: f"={prev('vat_out')(m)}")
    add("vat_rec", "TVA déductible récupérée (mois suivant, coûts externes)", "€", EUR, lambda m: (f"=({mcol(m-1)}{MR['var_cost']}+{mcol(m-1)}{MR['acq_spend']}+{mcol(m-1)}{MR['fx_mvp']}+{mcol(m-1)}{MR['fx_tools']}+{mcol(m-1)}{MR['fx_legal']}+{mcol(m-1)}{MR['fx_mkt']}+{mcol(m-1)}{MR['fx_ga']}+{mcol(m-1)}{MR['fx_audit']}+{mcol(m-1)}{MR['fx_setup']})*{H('vat', scol)}" if m > 1 else "=0"))
    add("fin_in", "Financement reçu", "€", EUR, lambda m: f"={H('fin_on', scol)}*(IF({mcol(m)}{MR['month']}={H('fin1_month', scol)},{H('fin1_amt', scol)},0)+IF({mcol(m)}{MR['month']}={H('fin2_month', scol)},{H('fin2_amt', scol)},0)+IF({mcol(m)}{MR['month']}={H('fin3_month', scol)},{H('fin3_amt', scol)},0))")
    add("cash_open", "Trésorerie d'ouverture", "€", EUR, lambda m: (f"={mcol(m-1)}{MR['cash_close']}" if m > 1 else f"={H('cash0', scol)}"))
    add("cash_flow", "Flux de trésorerie du mois", "€", EUR, lambda m: f"={mcol(m)}{MR['receipts']}-{mcol(m)}{MR['var_cost']}-{mcol(m)}{MR['acq_spend']}-{mcol(m)}{MR['fixed']}-{mcol(m)}{MR['vat_pay']}+{mcol(m)}{MR['vat_rec']}+{mcol(m)}{MR['fin_in']}")
    add("cash_close", "Trésorerie de clôture", "€", EUR, lambda m: f"={mcol(m)}{MR['cash_open']}+{mcol(m)}{MR['cash_flow']}", "b")
    add("fin_cum", "Financement cumulé", "€", EUR, lambda m: f"={prev('fin_cum')(m)}+{mcol(m)}{MR['fin_in']}")
    add("cash_pre", "Trésorerie cumulée hors financement", "€", EUR, lambda m: f"={mcol(m)}{MR['cash_close']}-{mcol(m)}{MR['fin_cum']}", "b")
    add("cash_min", "Point bas glissant hors financement", "€", EUR, lambda m: (f"=MIN({mcol(m-1)}{MR['cash_min']},{mcol(m)}{MR['cash_pre']})" if m > 1 else f"={mcol(m)}{MR['cash_pre']}"))
    add("cash_recov", "Trésorerie cumulée hors financement positive après lancement ? (1 = oui)", "0/1", NUM, lambda m: f"=IF(AND({mcol(m)}{MR['launched']}=1,{mcol(m)}{MR['cash_pre']}>0),1,0)")
    add("__sec", "Indicateurs", "", None, None)
    add("arr", "ARR HT instantané (CA HT × 12)", "€ HT", EUR, lambda m: f"={mcol(m)}{MR['rev_ht']}*12")
    add("arpa", "ARPA HT (CA HT / abonnés)", "€ HT", EUR2, lambda m: f"=IF({mcol(m)}{MR['close']}>0,{mcol(m)}{MR['rev_ht']}/{mcol(m)}{MR['close']},0)")
    add("varpa", "Coût variable par abonné", "€ HT", EUR2, lambda m: f"=IF({mcol(m)}{MR['close']}>0,{mcol(m)}{MR['var_cost']}/{mcol(m)}{MR['close']},0)")
    add("contripa", "Contribution par abonné", "€ HT", EUR2, lambda m: f"=IF({mcol(m)}{MR['close']}>0,{mcol(m)}{MR['contrib']}/{mcol(m)}{MR['close']},0)")
    add("var_margin", "Marge variable (% du CA HT)", "%", PCT, lambda m: f"=IF({mcol(m)}{MR['rev_ht']}>0,{mcol(m)}{MR['contrib']}/{mcol(m)}{MR['rev_ht']},0)")
    add("cac_eff", "CAC effectif", "€", EUR, lambda m: f"=IF({mcol(m)}{MR['new_paid']}>0,{mcol(m)}{MR['acq_spend']}/{mcol(m)}{MR['new_paid']},0)")
    add("payback", "Payback du CAC (mois)", "mois", NUM1, lambda m: f"=IF({mcol(m)}{MR['contripa']}>0,{H('cac', scol)}*{S['cac']}/{mcol(m)}{MR['contripa']},0)")
    add("ltv", "LTV contributive simplifiée (contribution / churn)", "€ HT", EUR, lambda m: f"=IF({H('churn', scol)}*{S['churn']}>0,{mcol(m)}{MR['contripa']}/({H('churn', scol)}*{S['churn']}),0)")
    add("ltv_cac", "LTV / CAC", "x", MULT, lambda m: f"=IF({H('cac', scol)}*{S['cac']}>0,{mcol(m)}{MR['ltv']}/({H('cac', scol)}*{S['cac']}),0)")

    # assign rows
    rr = r
    for key, label, unit, fmt, fb, style in rows:
        if key == "__sec":
            rr += 1
            continue
        MR[key] = rr
        rr += 1
    # header row for months
    ws.cell(row=r - 1, column=1, value="Ligne").font = HEAD
    ws.cell(row=r - 1, column=2, value="Unité").font = HEAD
    for m in range(1, N + 1):
        c = ws.cell(row=r - 1, column=FIRST + m - 1, value=f"M{m}")
        c.font = HEAD
        c.fill = MIST
        c.alignment = Alignment(horizontal="center")
    for k, lab in enumerate(("Année 1", "Année 2", "Année 3")):
        c = ws.cell(row=r - 1, column=FIRST + N + 1 + k, value=lab)
        c.font = HEAD
        c.fill = GLOWF
        c.alignment = Alignment(horizontal="center")
    # write rows
    rr = r
    FLOW_KEYS = {"acq_budget", "new_paid", "new_pilot", "new_org", "churned", "mrr_p", "mrr_pr", "mrr_f", "billing",
                 "vat_out", "rev_ht", "unpaid", "fees", "receipts", "ai_cost", "host_cost", "supp_cost", "var_cost",
                 "contrib", "acq_spend", "fx_founders", "fx_e1", "fx_e2", "fx_mvp", "fx_tools", "fx_legal", "fx_ins",
                 "fx_mkt", "fx_ga", "fx_audit", "fx_setup", "fixed", "ebitda", "vat_pay", "vat_rec", "fin_in", "cash_flow"}
    STOCK_KEYS = {"close", "sub_p", "sub_pr", "sub_f", "cash_close", "cash_pre", "cash_min", "fin_cum", "arr", "arpa", "varpa",
                  "contripa", "var_margin", "cac_eff", "payback", "ltv", "ltv_cac"}
    for key, label, unit, fmt, fb, style in rows:
        if key == "__sec":
            c = ws.cell(row=rr, column=1, value=label)
            c.font = Font(name=ARIAL, size=10, bold=True, color=PALETTE["glow_deep"])
            rr += 1
            continue
        ws.cell(row=rr, column=1, value=label).font = BOLD if style == "b" else BLACK
        ws.cell(row=rr, column=2, value=unit).font = SUB
        for m in range(1, N + 1):
            v = fb(m)
            c = ws.cell(row=rr, column=FIRST + m - 1, value=v)
            c.font = BOLD if style == "b" else BLACK
            if fmt:
                c.number_format = fmt
        # annual columns
        for k in range(3):
            col = FIRST + N + 1 + k
            m1, m12 = 12 * k + 1, 12 * k + 12
            if key in FLOW_KEYS:
                f = f"=SUM({mcol(m1)}{rr}:{mcol(m12)}{rr})"
            elif key in STOCK_KEYS:
                f = f"={mcol(m12)}{rr}"
            else:
                f = None
            if f:
                c = ws.cell(row=rr, column=col, value=f)
                c.font = BOLD if style == "b" else BLACK
                c.number_format = fmt
        rr += 1
    ws.column_dimensions["A"].width = 62
    ws.column_dimensions["B"].width = 10
    for m in range(1, N + 1):
        ws.column_dimensions[mcol(m)].width = 11
    for k in range(3):
        ws.column_dimensions[L(FIRST + N + 1 + k)].width = 13
    ws.freeze_panes = f"C{r}"
    return rr


def model_ref(sheet, key, col):
    return f"'{sheet}'!{col}{MR[key]}"


def write_synthese(ws, scen_sheets):
    ws["A1"] = "Synthèse des scénarios"
    ws["A1"].font = TITLE
    ws["A2"] = "Toutes les valeurs sont calculées à partir des onglets Modèle. Trésorerie hors financement sauf mention contraire."
    ws["A2"].font = SUB
    heads = ["Indicateur", "Unité"] + [s for s, _ in scen_sheets]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
    first, last = mcol(1), mcol(N)

    def rng(sheet, key):
        return f"'{sheet}'!{first}{MR[key]}:{last}{MR[key]}"

    lines = [
        ("Mois de lancement commercial", "mois", lambda s: f"='{s}'!$B$5", NUM),
        ("Point bas de trésorerie hors financement", "€", lambda s: f"=MIN({rng(s, 'cash_pre')})", EUR),
        ("Mois du point bas", "mois", lambda s: f"=MATCH(MIN({rng(s, 'cash_pre')}),{rng(s, 'cash_pre')},0)", NUM),
        ("Besoin de financement (−point bas + réserve)", "€", lambda s: f"=MAX(0,-MIN({rng(s, 'cash_pre')}))+{H('reserve', SCOL[s])}", EUR),
        ("Trésorerie cumulée hors financement fin A1", "€", lambda s: f"={model_ref(s, 'cash_pre', mcol(12))}", EUR),
        ("Trésorerie cumulée hors financement fin A2", "€", lambda s: f"={model_ref(s, 'cash_pre', mcol(24))}", EUR),
        ("Trésorerie cumulée hors financement fin A3", "€", lambda s: f"={model_ref(s, 'cash_pre', mcol(36))}", EUR),
        ("Premier mois d'EBITDA positif", "mois", lambda s: f"=IFERROR(MATCH(1,{rng(s, 'ebitda_pos')},0),\"non atteint\")", NUM),
        ("Premier mois de trésorerie cumulée positive (hors financement)", "mois", lambda s: f"=IFERROR(MATCH(1,{rng(s, 'cash_recov')},0),\"non atteint\")", NUM),
        ("Abonnés actifs fin A1", "abonnés", lambda s: f"={model_ref(s, 'close', mcol(12))}", NUM),
        ("Abonnés actifs fin A2", "abonnés", lambda s: f"={model_ref(s, 'close', mcol(24))}", NUM),
        ("Abonnés actifs fin A3", "abonnés", lambda s: f"={model_ref(s, 'close', mcol(36))}", NUM),
        ("Chiffre d'affaires HT A1", "€", lambda s: f"={model_ref(s, 'rev_ht', L(FIRST + N + 1))}", EUR),
        ("Chiffre d'affaires HT A2", "€", lambda s: f"={model_ref(s, 'rev_ht', L(FIRST + N + 2))}", EUR),
        ("Chiffre d'affaires HT A3", "€", lambda s: f"={model_ref(s, 'rev_ht', L(FIRST + N + 3))}", EUR),
        ("EBITDA A1", "€", lambda s: f"={model_ref(s, 'ebitda', L(FIRST + N + 1))}", EUR),
        ("EBITDA A2", "€", lambda s: f"={model_ref(s, 'ebitda', L(FIRST + N + 2))}", EUR),
        ("EBITDA A3", "€", lambda s: f"={model_ref(s, 'ebitda', L(FIRST + N + 3))}", EUR),
        ("ARR HT instantané à M36", "€", lambda s: f"={model_ref(s, 'arr', mcol(36))}", EUR),
        ("Coût variable par abonné à M36", "€", lambda s: f"={model_ref(s, 'varpa', mcol(36))}", EUR2),
        ("Marge variable à M36", "%", lambda s: f"={model_ref(s, 'var_margin', mcol(36))}", PCT),
        ("Payback du CAC à M36", "mois", lambda s: f"={model_ref(s, 'payback', mcol(36))}", NUM1),
        ("LTV / CAC à M36", "x", lambda s: f"={model_ref(s, 'ltv_cac', mcol(36))}", MULT),
        ("Dépenses d'acquisition cumulées (36 mois)", "€", lambda s: f"=SUM({rng(s, 'acq_spend')})", EUR),
        ("Coûts fixes cumulés (36 mois)", "€", lambda s: f"=SUM({rng(s, 'fixed')})", EUR),
    ]
    r = 5
    for label, unit, fb, fmt in lines:
        ws.cell(row=r, column=1, value=label).font = BLACK
        ws.cell(row=r, column=2, value=unit).font = SUB
        for j, (s, _) in enumerate(scen_sheets):
            c = ws.cell(row=r, column=3 + j, value=fb(s))
            c.font = GREEN
            c.number_format = fmt
        r += 1
    ws.cell(row=r + 1, column=1, value="Lecture : le besoin de financement est le montant à réunir avant le lancement pour ne jamais passer sous la réserve cible, si les hypothèses du scénario se réalisent. Aucun financement n'est acquis.").font = SUB
    ws.column_dimensions["A"].width = 60
    ws.column_dimensions["B"].width = 10
    for j in range(len(scen_sheets)):
        ws.column_dimensions[L(3 + j)].width = 16
    return r


def write_tornade(ws, base_sheet, cases):
    ws["A1"] = "Sensibilité du scénario Central (tornade)"
    ws["A1"].font = TITLE
    ws["A2"] = "Chaque cas est un onglet S01 à S10 : copie vivante du modèle Central avec un seul choc. Les écarts se recalculent."
    ws["A2"].font = SUB
    heads = ["Cas", "Choc", "Point bas hors financement", "Écart vs Central", "Besoin de financement", "Trésorerie fin A3 hors financement", "1er mois EBITDA > 0", "Abonnés fin A3"]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    first, last = mcol(1), mcol(N)

    def rng(sheet, key):
        return f"'{sheet}'!{first}{MR[key]}:{last}{MR[key]}"

    r = 5
    ws.cell(row=r, column=1, value="Central (base)").font = BOLD
    ws.cell(row=r, column=2, value="aucun").font = SUB
    ws.cell(row=r, column=3, value=f"=MIN({rng(base_sheet, 'cash_pre')})").number_format = EUR
    ws.cell(row=r, column=4, value=0).number_format = EUR
    ws.cell(row=r, column=5, value=f"=MAX(0,-MIN({rng(base_sheet, 'cash_pre')}))+{H('reserve', 'D')}").number_format = EUR
    ws.cell(row=r, column=6, value=f"={model_ref(base_sheet, 'cash_pre', mcol(36))}").number_format = EUR
    ws.cell(row=r, column=7, value=f"=IFERROR(MATCH(1,{rng(base_sheet, 'ebitda_pos')},0),\"non atteint\")").number_format = NUM
    ws.cell(row=r, column=8, value=f"={model_ref(base_sheet, 'close', mcol(36))}").number_format = NUM
    base_row = r
    r += 1
    for sheet, label, desc in cases:
        ws.cell(row=r, column=1, value=label).font = BLACK
        ws.cell(row=r, column=2, value=desc).font = SUB
        ws.cell(row=r, column=3, value=f"=MIN({rng(sheet, 'cash_pre')})").number_format = EUR
        ws.cell(row=r, column=4, value=f"=C{r}-$C${base_row}").number_format = EUR
        ws.cell(row=r, column=5, value=f"=MAX(0,-MIN({rng(sheet, 'cash_pre')}))+{H('reserve', 'D')}").number_format = EUR
        ws.cell(row=r, column=6, value=f"={model_ref(sheet, 'cash_pre', mcol(36))}").number_format = EUR
        ws.cell(row=r, column=7, value=f"=IFERROR(MATCH(1,{rng(sheet, 'ebitda_pos')},0),\"non atteint\")").number_format = NUM
        ws.cell(row=r, column=8, value=f"={model_ref(sheet, 'close', mcol(36))}").number_format = NUM
        for j in range(3, 9):
            ws.cell(row=r, column=j).font = GREEN
        r += 1
    # chart: écart du point bas
    ch = BarChart()
    ch.type = "bar"
    ch.style = 10
    ch.title = "Écart du point bas de trésorerie vs Central (€)"
    ch.y_axis.title = "€"
    data = Reference(ws, min_col=4, min_row=base_row + 1, max_row=r - 1)
    cats = Reference(ws, min_col=1, min_row=base_row + 1, max_row=r - 1)
    ch.add_data(data, titles_from_data=False)
    ch.set_categories(cats)
    ch.legend = None
    ch.height = 9
    ch.width = 18
    ws.add_chart(ch, f"A{r + 2}")
    # second chart: cash at end of year 3
    ws.cell(row=4, column=10, value="Écart de trésorerie fin A3 vs Central").font = HEAD
    for i in range(base_row + 1, r):
        c = ws.cell(row=i, column=10, value=f"=F{i}-$F${base_row}")
        c.number_format = EUR
        c.font = BLACK
    ch2 = BarChart()
    ch2.type = "bar"
    ch2.style = 10
    ch2.title = "Écart de trésorerie fin A3 vs Central (€)"
    data2 = Reference(ws, min_col=10, min_row=base_row + 1, max_row=r - 1)
    ch2.add_data(data2, titles_from_data=False)
    ch2.set_categories(cats)
    ch2.legend = None
    ch2.height = 9
    ch2.width = 18
    ws.add_chart(ch2, f"F{r + 2}")
    ws.column_dimensions["J"].width = 20
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 36
    for col in "CDEFGH":
        ws.column_dimensions[col].width = 18


def write_unit_economics(ws):
    ws["A1"] = "Économie unitaire (scénario actif)"
    ws["A1"].font = TITLE
    ws["A2"] = "Par abonné et par mois, HT. Référence : colonne Actif de l'onglet Hypothèses."
    ws["A2"].font = SUB
    heads = ["Ligne", "Personal", "Premium", "Family", "Mix pondéré"]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
    F = "F"
    tiers = [("price_personal", "missions_personal", "mix_personal"), ("price_premium", "missions_premium", "mix_premium"), ("price_family", "missions_family", "mix_family")]
    r = 5
    lines = [
        ("Prix TTC", EUR, lambda p, mi, mx: f"={H(p, F)}"),
        ("Prix HT", EUR2, lambda p, mi, mx: f"={H(p, F)}/(1+{H('vat', F)})"),
        ("Missions par mois", NUM, lambda p, mi, mx: f"={H(mi, F)}"),
        ("Coût IA et outils", EUR2, lambda p, mi, mx: f"={H(mi, F)}*{H('cost_mission', F)}"),
        ("Hébergement", EUR2, lambda p, mi, mx: f"={H('hosting', F)}"),
        ("Support", EUR2, lambda p, mi, mx: f"={H('support', F)}"),
        ("Frais de paiement", EUR2, lambda p, mi, mx: f"={H(p, F)}*(1-{H('unpaid', F)})*{H('fee_pct', F)}+{H('fee_fixed', F)}"),
        ("Impayés (HT)", EUR2, lambda p, mi, mx: f"={H(p, F)}*{H('unpaid', F)}/(1+{H('vat', F)})"),
    ]
    rowmap = {}
    for label, fmt, fb in lines:
        ws.cell(row=r, column=1, value=label).font = BLACK
        for j, (p, mi, mx) in enumerate(tiers):
            c = ws.cell(row=r, column=2 + j, value=fb(p, mi, mx))
            c.font = GREEN
            c.number_format = fmt
        c = ws.cell(row=r, column=5, value=f"=B{r}*{H('mix_personal', F)}+C{r}*{H('mix_premium', F)}+D{r}*{H('mix_family', F)}")
        c.number_format = fmt
        c.font = BLACK
        rowmap[label] = r
        r += 1
    ws.cell(row=r, column=1, value="Contribution par abonné et par mois").font = BOLD
    for j in range(2, 6):
        col = L(j)
        c = ws.cell(row=r, column=j, value=f"={col}{rowmap['Prix HT']}-{col}{rowmap['Coût IA et outils']}-{col}{rowmap['Hébergement']}-{col}{rowmap['Support']}-{col}{rowmap['Frais de paiement']}-{col}{rowmap['Impayés (HT)']}")
        c.number_format = EUR2
        c.font = BOLD
    rc = r
    r += 1
    ws.cell(row=r, column=1, value="Marge variable (% du prix HT)").font = BLACK
    for j in range(2, 6):
        col = L(j)
        c = ws.cell(row=r, column=j, value=f"=IF({col}{rowmap['Prix HT']}>0,{col}{rc}/{col}{rowmap['Prix HT']},0)")
        c.number_format = PCT
    r += 1
    ws.cell(row=r, column=1, value="Payback du CAC (mois)").font = BLACK
    for j in range(2, 6):
        col = L(j)
        c = ws.cell(row=r, column=j, value=f"=IF({col}{rc}>0,{H('cac', F)}/{col}{rc},0)")
        c.number_format = NUM1
    r += 1
    ws.cell(row=r, column=1, value="LTV contributive simplifiée (contribution / churn)").font = BLACK
    for j in range(2, 6):
        col = L(j)
        c = ws.cell(row=r, column=j, value=f"=IF({H('churn', F)}>0,{col}{rc}/{H('churn', F)},0)")
        c.number_format = EUR
    rl = r
    r += 1
    ws.cell(row=r, column=1, value="LTV / CAC").font = BOLD
    for j in range(2, 6):
        col = L(j)
        c = ws.cell(row=r, column=j, value=f"=IF({H('cac', F)}>0,{col}{rl}/{H('cac', F)},0)")
        c.number_format = MULT
        c.font = BOLD
    r += 3
    # grid LTV/CAC Premium: churn x CAC
    ws.cell(row=r, column=1, value="Grille LTV / CAC, abonné Premium : churn mensuel (lignes) × CAC (colonnes)").font = BOLD
    r += 1
    cacs = [100, 150, 200, 250, 300, 400]
    churns = [0.02, 0.03, 0.04, 0.05, 0.07, 0.10]
    ws.cell(row=r, column=1, value="Churn \\ CAC").font = HEAD
    for j, cv in enumerate(cacs):
        c = ws.cell(row=r, column=2 + j, value=cv)
        c.font = BLUE
        c.number_format = EUR
        c.fill = MIST
    hdr = r
    r += 1
    for ch in churns:
        c = ws.cell(row=r, column=1, value=ch)
        c.font = BLUE
        c.number_format = PCT
        for j in range(len(cacs)):
            col = L(2 + j)
            cell = ws.cell(row=r, column=2 + j, value=f"=IF(AND($A{r}>0,{col}${hdr}>0),($C${rc}/$A{r})/{col}${hdr},0)")
            cell.number_format = MULT
        r += 1
    r += 2
    ws.cell(row=r, column=1, value="Grille contribution Premium (€ HT/mois) : coût par mission (lignes) × missions par mois (colonnes)").font = BOLD
    r += 1
    missions = [30, 45, 60, 90, 120]
    costs = [0.08, 0.12, 0.18, 0.25, 0.35, 0.50]
    ws.cell(row=r, column=1, value="Coût/mission \\ Missions").font = HEAD
    for j, mv in enumerate(missions):
        c = ws.cell(row=r, column=2 + j, value=mv)
        c.font = BLUE
        c.number_format = NUM
        c.fill = MIST
    hdr2 = r
    r += 1
    for cv in costs:
        c = ws.cell(row=r, column=1, value=cv)
        c.font = BLUE
        c.number_format = EUR2
        for j in range(len(missions)):
            col = L(2 + j)
            cell = ws.cell(row=r, column=2 + j, value=f"=$C${rowmap['Prix HT']}-$A{r}*{col}${hdr2}-$C${rowmap['Hébergement']}-$C${rowmap['Support']}-$C${rowmap['Frais de paiement']}-$C${rowmap['Impayés (HT)']}")
            cell.number_format = EUR2
        r += 1
    ws.column_dimensions["A"].width = 48
    for col in "BCDEFG":
        ws.column_dimensions[col].width = 14


def write_kpi(ws):
    ws["A1"] = "Architecture de KPI"
    ws["A1"].font = TITLE
    ws["A2"] = "Sept indicateurs au niveau Board, huit au niveau équipe. Seuils fixés avant de voir les données ; chaque métrique est appariée à une contre-métrique."
    ws["A2"].font = SUB
    heads = ["Niveau", "Indicateur", "Formule", "Décision qu'il change", "Propriétaire", "Avance / retard", "Vert", "Ambre (action)", "Rouge (action)", "Contre-métrique", "Cadence"]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    rows = [
        ("Board", "Abonnés actifs payants vs trajectoire", "Actifs fin de mois / cible du scénario", "Poursuivre, ralentir ou arrêter l'acquisition", "Malik", "Retard", "≥ 100 % de la cible", "80 à 100 % : revue des canaux", "< 80 % deux mois de suite : gel des dépenses d'acquisition", "Churn logo mensuel", "Mensuelle"),
        ("Board", "Rétention J30 des cohortes payantes", "Actifs à J30 / cohorte initiale", "Lancer ou non la montée en charge", "Steve", "Retard", "≥ 70 %", "60 à 70 % : entretiens de résiliation", "< 60 % : pas de montée en charge, retour produit", "Activation J7", "Mensuelle"),
        ("Board", "Fiabilité des missions", "Missions réussies sans correction / missions lancées", "Élargir ou restreindre le périmètre des missions", "Isaac", "Avance", "≥ 80 %", "70 à 80 % : gel des nouvelles missions", "< 70 % : retrait de la mission la moins fiable", "Taux de missions corrigées par l'utilisateur", "Hebdomadaire"),
        ("Board", "Incidents critiques (action sans autorisation, fuite de données, confusion de profils)", "Nombre confirmé", "Arrêt du pilote", "Tiffany", "Avance", "0", "1 mineur : analyse sous 48 h", "1 critique : arrêt du parcours, revue avant reprise", "Volume d'actions exécutées (éviter la fiabilité par inactivité)", "Continue"),
        ("Board", "Coût variable par abonné", "Coûts variables HT / abonnés actifs", "Prix, routage des modèles, limites d'usage", "Sébastien", "Retard", "≤ 18 € HT", "18 à 24 € : revue du routage IA", "> 24 € : limites d'usage ou hausse de prix", "Missions par abonné (ne pas réduire l'usage pour réduire le coût)", "Mensuelle"),
        ("Board", "Payback du CAC", "CAC effectif / contribution mensuelle par abonné", "Budget d'acquisition du mois suivant", "Sébastien", "Retard", "≤ 6 mois", "6 à 9 mois : réallocation entre canaux", "> 9 mois : arrêt du canal concerné", "Qualité des leads (rétention J30 par canal)", "Mensuelle"),
        ("Board", "Marge variable", "(CA HT − coûts variables − frais − impayés) / CA HT", "Soutenabilité du prix", "Sébastien", "Retard", "≥ 65 %", "55 à 65 %", "< 55 % : revue prix et périmètre", "ARPA (ne pas gonfler la marge par un mix artificiel)", "Mensuelle"),
        ("Équipe", "Activation J7", "Nouveaux clients avec ≥ 1 mission utile / nouveaux clients", "Onboarding", "Steve", "Avance", "≥ 70 %", "50 à 70 %", "< 50 %", "Temps jusqu'à la première mission", "Hebdomadaire"),
        ("Équipe", "Conversion essai → payant", "Payants / essais de la cohorte", "Parcours de souscription", "Steve", "Retard", "≥ 20 %", "10 à 20 %", "< 10 %", "Qualité des essais (activation)", "Hebdomadaire"),
        ("Équipe", "Churn logo mensuel", "Résiliations / actifs début de mois", "Rétention", "Steve", "Retard", "≤ 3 %", "3 à 5 %", "> 5 %", "Motifs de résiliation (produit vs prix)", "Mensuelle"),
        ("Équipe", "Coût par mission et taux d'échec", "Coût API / missions ; échecs / missions", "Choix des modèles", "Isaac", "Avance", "≤ 0,18 € ; ≤ 10 %", "0,18 à 0,30 € ; 10 à 20 %", "> 0,30 € ; > 20 %", "Fiabilité (ne pas dégrader la qualité pour le coût)", "Hebdomadaire"),
        ("Équipe", "Temps gagné déclaré par semaine", "Enquête mensuelle, heures", "Argumentaire et prix", "Alice", "Retard", "≥ 2 h", "1 à 2 h", "< 1 h", "Usage réel (missions / semaine)", "Mensuelle"),
        ("Équipe", "Suggestions proactives acceptées", "Validées / proposées", "Réglage de la proactivité", "Steve", "Avance", "≥ 50 %", "30 à 50 %", "< 30 % : réduire les suggestions", "Suggestions ignorées (bruit)", "Hebdomadaire"),
        ("Équipe", "CAC par canal et persona", "Dépenses attribuées / nouveaux payants attribués", "Allocation du budget", "Alice", "Retard", "≤ 150 €", "150 à 240 €", "> 240 € : arrêt du canal", "Rétention J30 par canal", "Mensuelle"),
        ("Équipe", "Délai de réponse support", "Médiane, heures ouvrées", "Dimensionnement du support", "Steve", "Avance", "≤ 4 h", "4 à 24 h", "> 24 h", "Taux de résolution au premier contact", "Hebdomadaire"),
    ]
    for i, row in enumerate(rows, 5):
        for j, v in enumerate(row, 1):
            c = ws.cell(row=i, column=j, value=v)
            c.font = BLACK if j != 1 else BOLD
            c.alignment = Alignment(wrap_text=True, vertical="top")
    widths = [9, 34, 30, 30, 11, 10, 14, 24, 30, 30, 12]
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[L(j)].width = w
    ws.freeze_panes = "C5"


def write_financement(ws):
    ws["A1"] = "Plan de financement par jalons (hypothèses, aucune aide ni levée acquise)"
    ws["A1"].font = TITLE
    ws["A2"] = "Reprend la stratégie Finance V1 (2 FINANCE/FINANCEMENT). Les montants alimentent les tranches de l'onglet Hypothèses quand « Inclure le financement » = 1."
    ws["A2"].font = SUB
    heads = ["Phase", "Fenêtre", "Objectif", "Source envisagée", "Montant (hypothèse)", "Conditions et vérifications", "Statut"]
    for j, h in enumerate(heads, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.font = HEAD
        c.fill = MIST
        c.border = BOT
        c.alignment = Alignment(wrap_text=True, vertical="center")
    rows = [
        ("Phase 0, validation", "M1 à M3", "Entretiens, prototype des missions 1 et 5, test de prix", "Apports des fondateurs", 15000, "Pas de société nécessaire. Dépenses non éligibles aux aides si engagées avant création : vérifier avant tout paiement.", "Hypothèse"),
        ("Phase 1, création et MVP", "Au lancement (M7 central)", "Société, MVP, pilote, 30 premiers abonnés", "Prêts d'honneur (Initiative, Réseau Entreprendre), Bourse French Tech (Bpifrance), business angels, incubateur HEC", 150000, "Éligibilité, calendrier d'instruction et montants à vérifier auprès de chaque dispositif ; les prêts d'honneur sont personnels aux fondateurs.", "Hypothèse"),
        ("Phase 2, croissance", "M13 (central)", "Acquisition, embauches 1 et 2, Family", "Amorçage (business angels, fonds d'amorçage), prêt bancaire adossé", 300000, "Conditionné à : rétention J30 ≥ 70 %, payback ≤ 6 mois, coût variable ≤ 18 €, zéro incident critique.", "Hypothèse"),
    ]
    for i, row in enumerate(rows, 5):
        for j, v in enumerate(row, 1):
            c = ws.cell(row=i, column=j, value=v)
            c.font = BLACK
            c.alignment = Alignment(wrap_text=True, vertical="top")
            if j == 5:
                c.number_format = EUR
                c.font = BLUE
    ws.cell(row=9, column=4, value="Total des tranches").font = BOLD
    c = ws.cell(row=9, column=5, value="=SUM(E5:E7)")
    c.number_format = EUR
    c.font = BOLD
    ws.cell(row=11, column=1, value="Comparaison avec le besoin calculé (onglet Synthèse, scénario Central) :").font = BOLD
    ws.cell(row=12, column=1, value="Besoin de financement Central")
    c = ws.cell(row=12, column=5, value="=Synthèse!D8")
    c.number_format = EUR
    c.font = GREEN
    ws.cell(row=13, column=1, value="Couverture du besoin par les tranches (x)")
    c = ws.cell(row=13, column=5, value="=IF(E12>0,E9/E12,0)")
    c.number_format = MULT
    widths = [24, 18, 36, 40, 16, 60, 11]
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[L(j)].width = w


def write_readme(ws, cases):
    ws["A1"] = "Helium, modèle financier 36 mois, V1"
    ws["A1"].font = TITLE
    lines = [
        ("Objet", "Prévision mensuelle de trésorerie sur 36 mois pour le projet Helium (ex Super Majordome IA), HEC GEMM Group 4. Trois scénarios, économie unitaire, sensibilités, KPI et plan de financement."),
        ("Statut", "Document de travail. Toutes les hypothèses sont non validées par des mesures (voir colonne Source de l'onglet Hypothèses). Aucun chiffre n'est une dépense engagée ni un financement obtenu."),
        ("Préparé par", "Assistant IA Direction, à la demande du CEO (Malik), le 27 octobre 2026, pour Sébastien (Finance)."),
        ("Légende", "Texte bleu = entrée modifiable. Fond jaune = levier clé. Texte noir = formule. Texte vert = lien vers un autre onglet. Ne rien saisir dans les onglets Modèle et S01 à S10 en dehors de la ligne de chocs."),
        ("Onglets", "Hypothèses (toutes les entrées, trois scénarios, sélecteur F3) · Économie unitaire (par offre, grilles de sensibilité) · Modèle Prudent / Central / Ambitieux (36 mois) · Synthèse (comparaison) · Tornade (sensibilités du Central) · S01 à S11 (copies du Central avec un choc) · KPI · Financement."),
        ("Mécanique", "Abonnés : ouverture + acquisition payante (budget / CAC) + pilote + organique − churn. Revenus TTC → TVA → CA HT. Coûts variables = missions × coût par mission + hébergement + support. Trésorerie : encaissements TTC, coûts HT, TVA nette réglée le mois suivant, financement optionnel."),
        ("Simplifications", "Mix par offre appliqué au total des abonnés. TVA récupérable sur tous les coûts externes (fournisseurs étrangers en autoliquidation). Pas d'impôt sur les sociétés (pertes), pas de CIR/CII, pas de délai de paiement fournisseurs. Développement MVP passé en charges."),
        ("Sensibilités", "Onglet Tornade : " + " ; ".join(f"{lab} ({desc})" for _, lab, desc in cases) + "."),
        ("Contrôles effectués", "Recalcul complet sous LibreOffice, zéro erreur de formule ; mix = 100 % ; cohérence avec les ordres de grandeur Finance V3 (point bas central −173 k€, prudent −580 k€) ; hypothèses de coût IA, churn et CAC confrontées aux benchmarks publics d'octobre 2026 (sources dans la colonne G de l'onglet Hypothèses et dans l'analyse de marché)."),
        ("À faire par Finance", "Remplacer les hypothèses de coût par mission et de missions par mois par les mesures de Produit/Opérations ; remplacer CAC, conversion et churn par les cohortes du pilote ; saisir les devis MVP réels ; valider le régime de TVA et les dates d'encaissement."),
        ("Sources internes", "0 INBOX/BMC V2 ; 2 FINANCE/PREVISIONS (Business plan Lean V1, Registre des hypothèses, Acquisition et économie unitaire) ; 2 FINANCE/TRESORERIE (Synthèse V3) ; 2 FINANCE/FINANCEMENT (Stratégie V1) ; 4 VENTES (Synthèse exécutive, Objectifs et dashboard) ; 5 PRODUIT (Contribution marketing au cadrage MVP)."),
    ]
    r = 3
    for k, v in lines:
        ws.cell(row=r, column=1, value=k).font = BOLD
        c = ws.cell(row=r, column=2, value=v)
        c.font = BLACK
        c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 120


SCOL = {}


def main():
    wb = Workbook()
    ws_read = wb.active
    ws_read.title = "Lisez-moi"
    ws_h = wb.create_sheet("Hypothèses")
    write_assumptions(ws_h)
    ws_u = wb.create_sheet("Économie unitaire")
    base_shock = dict(price=1, churn=1, cac=1, ai=1, fixed=1, delay=0)
    scen = [("Modèle Prudent", "C"), ("Modèle Central", "D"), ("Modèle Ambitieux", "E")]
    for name, col in scen:
        SCOL[name] = col
        ws = wb.create_sheet(name)
        write_model(ws, f"{name} (36 mois)", col, base_shock)
    ws_s = wb.create_sheet("Synthèse")
    ws_t = wb.create_sheet("Tornade")
    ws_k = wb.create_sheet("KPI")
    ws_f = wb.create_sheet("Financement")
    cases = [
        ("S01", "Churn 5 %", "churn × 1,67 (3 % → 5 %)", dict(base_shock, churn=1.6667)),
        ("S02", "Churn 2 %", "churn × 0,67 (3 % → 2 %)", dict(base_shock, churn=0.6667)),
        ("S03", "CAC 240 €", "CAC × 1,6", dict(base_shock, cac=1.6)),
        ("S04", "CAC 105 €", "CAC × 0,7", dict(base_shock, cac=0.7)),
        ("S05", "Coût IA +67 %", "coût par mission × 1,67 (0,18 → 0,30 €)", dict(base_shock, ai=1.6667)),
        ("S06", "Coût IA −33 %", "coût par mission × 0,67 (0,18 → 0,12 €)", dict(base_shock, ai=0.6667)),
        ("S07", "Prix −20 %", "prix × 0,8 (Premium 79 → 63 €)", dict(base_shock, price=0.8)),
        ("S08", "Prix +20 %", "prix × 1,2 (Premium 79 → 95 €)", dict(base_shock, price=1.2)),
        ("S09", "Lancement +3 mois", "retard de lancement de 3 mois", dict(base_shock, delay=3)),
        ("S10", "Coûts fixes +30 %", "coûts fixes × 1,3", dict(base_shock, fixed=1.3)),
        ("S11", "Churn 8 % (type app store)", "churn × 2,67 (3 % → 8 %)", dict(base_shock, churn=2.6667)),
    ]
    for sheet, lab, desc, shocks in cases:
        ws = wb.create_sheet(sheet)
        write_model(ws, f"Sensibilité {sheet} : {lab} (copie du Central)", "D", shocks)
        ws.sheet_properties.tabColor = PALETTE["linen"]
    write_unit_economics(ws_u)
    write_synthese(ws_s, scen)
    write_tornade(ws_t, "Modèle Central", [(s, lab, desc) for s, lab, desc, _ in cases])
    write_kpi(ws_k)
    write_financement(ws_f)
    write_readme(ws_read, [(s, lab, desc) for s, lab, desc, _ in cases])
    for name, col in scen:
        wb[name].sheet_properties.tabColor = PALETTE["glow"]
    ws_h.sheet_properties.tabColor = PALETTE["d3"]
    ws_s.sheet_properties.tabColor = PALETTE["eucalyptus"]
    wb.save(OUT)
    print("written", OUT)


if __name__ == "__main__":
    main()
