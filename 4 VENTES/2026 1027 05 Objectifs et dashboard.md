# Objectifs commerciaux MVP et tableau de bord
**27 octobre 2026 — objectifs proposés, non adoptés**

## Base financière
Tarifs BMC hypothétiques : Personal 29 €, Premium 79 €, Family 129 € TTC/mois ; TVA supposée 20 %. Premium : 65,83 € HT/mois ; coût variable 18 € HT ; contribution 47,83 € HT avant CAC et frais fixes. Simulation de 1 000 Premium actifs constants = 790 000 € HT annualisés : **ce n'est pas un objectif officiel de CA**. Aucun objectif officiel chiffré n'a été trouvé dans les prévisions consultées.

## OKR à 90 jours
**O1 — Demande :** 30 entretiens (12 couples, 12 cadres, 6 dirigeants), ≥ 10 pilotes payants, ≥ 30 abonnés actifs payants à J90 sous réserve des garde-fous.
**O2 — Usage :** ≥ 70 % des pilotes actifs à J30 ; ≥ 80 % des tâches éligibles correctement réalisées ; temps gagné mesuré ; zéro incident critique.
**O3 — Économie :** marge variable ≥ 65 %, coût variable Premium ≤ 18 € HT/mois, remboursement du CAC par la contribution ≤ 6 mois.

## Scénario J90 (non prévision validée)
10 Personal + 12 Premium + 8 Family = 30 abonnés.
MRR TTC = 10 × 29 + 12 × 79 + 8 × 129 = **2 270 €**.
MRR HT (TVA 20 %) = **1 891,67 €** ; ARR HT instantané = **22 700 €**.
Suppose un mois complet payé par tous, hors churn, promotions et autres taxes. **Ne représente pas le CA encaissé sur 90 jours.**

## Dashboard hebdomadaire
| Indicateur | Formule | Source | Fréquence | Cible proposée |
|---|---|---|---|---|
| Leads qualifiés | Prospects répondant aux critères | CRM | Hebdo | À calibrer |
| Conversion lead→payant | Nouveaux payants / leads qualifiés de cohorte | CRM + paiements | Hebdo/cohorte | À établir |
| Activation J7 | Nouveaux clients avec ≥ 1 parcours utile / nouveaux clients | Produit | Hebdo | ≥ 70 % |
| Rétention J30 | Clients actifs J30 / cohorte activée | Produit + paiements | Mensuel | ≥ 70 % |
| MRR HT | Abonnements mensuels HT actifs | Facturation | Hebdo | 1 891,67 € à J90 (scénario) |
| Nouveaux clients nets | Nouveaux payants – résiliations | Facturation | Hebdo | 30 actifs J90 |
| ARPA HT | MRR HT / abonnés actifs | Facturation | Mensuel | Suivre le mix |
| CAC | Dépenses acquisition attribuées / nouveaux payants | Finance + CRM | Mensuel | Payback ≤ 6 mois |
| Payback CAC | CAC / contribution mensuelle moyenne/client | Finance | Mensuel | ≤ 6 mois |
| Marge variable | (CA HT – coûts variables HT) / CA HT | Finance | Mensuel | ≥ 65 % |
| Qualité | Tâches éligibles correctes / tâches lancées éligibles | Logs + revue | Hebdo | ≥ 80 % |
| Incidents critiques | Nombre d'incidents confirmés | Sécurité | Continu | 0 |
| Temps gagné | Minutes évitées / utilisateur actif | Journal + entretiens | Mensuel | Base à mesurer |

## Funnel et pilotage
Visiteurs → leads → qualifiés → démos → pilotes payants → abonnés actifs → renouvellements. Suivre les cohortes par persona et canal, sans inventer de taux de conversion. Lundi : 30 minutes CRM ; vendredi : qualité et retours ; mensuel : CAC, rétention, marge et décision go/no-go. Suspendre l'acquisition en cas d'incident critique, de marge durablement négative ou d'absence d'usage.

Source : Business Model Canvas V2, 27/10/2026, 0 INBOX. Tous les objectifs sont des propositions.

---

## Actualisation V2 — scénario Finance et tableau de bord coordonné
### Trajectoire à comparer (non approuvée)
| Échéance | Abonnés actifs fin de période | Statut |
|---|---:|---|
| J90 | 30 | Objectif test Ventes, proposition |
| Fin A1 | 150 | Scénario Finance |
| Fin A2 | 800 | Scénario Finance |
| Fin A3 | 2 500 | Scénario Finance |

**Attention :** les 30 abonnés J90 ne démontrent pas la faisabilité de 150 fin A1. Pour une année A1 de douze mois et J90 à fin M3, atteindre 150 fin M12 exigerait au minimum **120 abonnés nets supplémentaires en neuf mois**, soit **13,3 nets/mois en moyenne**, avant toute modélisation mensuelle du churn. Finance doit valider la courbe d'acquisition et les dépenses correspondantes.

### Hypothèses unitaires Finance
| KPI | Hypothèse / calcul | Nature |
|---|---:|---|
| Premium TTC/mois | 79 € | Prix proposé |
| Premium HT/mois | 65,83 € | TVA supposée 20 % |
| Coût variable HT/client/mois | 18 € | Hypothèse non mesurée |
| Contribution Premium HT/mois | 47,83 € | Calcul |
| CAC | 150 € | Hypothèse non mesurée |
| Churn mensuel | 3 % | Hypothèse non mesurée |
| Payback CAC simplifié | 150 / 47,83 = 3,14 mois | Calcul, hors coûts fixes |
| LTV contributive simplifiée | 47,83 / 0,03 = 1 594,44 € | Calcul théorique |
| LTV/CAC simplifié | 10,63x | Calcul théorique |

Ces indicateurs **ne doivent pas être affichés comme résultats constatés**. La LTV simplifiée suppose notamment une contribution et un churn constants.

### Chiffre d'affaires : distinguer simulation et objectif
Finance présente **CA HT A1 29 625 €, A2 375 250 €, A3 1 303 500 €**, avec mention expresse « à recalculer et auditer ». Ces montants ne sont pas des objectifs votés. Le BMC simule séparément **790 000 € HT annualisés pour 1 000 Premium actifs constants** ; ne pas confondre ARR instantané, CA reconnu et encaissements.

### Dashboard V2 — ajouts
| KPI | Calcul / suivi | Responsable | Cadence |
|---|---|---|---|
| Écart à trajectoire | Actifs fin de mois – cible mensuelle à établir | Ventes + Finance | Mensuel |
| CAC par canal et persona | Dépenses attribuables / nouveaux payants attribués | Growth + Finance | Mensuel |
| Conversion visiteurs→essai→payant | Cohortes distinctes, taux réels | Marketing + Ventes | Hebdo |
| Churn logo mensuel | Résiliations / actifs début de mois | Ventes + Finance | Mensuel |
| Rétention J30/J60/J90 | Actifs payants de cohorte / payants initiaux | Produit + Ventes | Mensuel |
| Contribution unitaire | ARPA HT – coûts variables HT/client | Finance + Opérations | Mensuel |
| Payback CAC | CAC / contribution mensuelle moyenne positive | Finance | Mensuel |
| MRR/ARR HT | MRR abonnements actifs ; ARR = 12 × MRR | Finance | Mensuel |
| Coût par mission et échec | Coûts API/support ; taux de reprise | Produit + Opérations | Hebdo |
| Incidents critiques | Incidents confirmés | Sécurité | Continu |

### Décisions nécessaires
1. Finance : auditer les chiffres de CA, budget MVP **77 050 € HT**, charges fixes et acquisition, et fixer une courbe mensuelle.
2. Produit/Opérations : documenter 10 missions, taux de réussite, coût unitaire et restrictions avant la mise en vente.
3. Marketing/Ventes : mesurer CAC, conversions et disposition à payer 29/79/129 €.
4. Direction : adopter ou rejeter les cibles, budgets et prix ; aucune décision inscrite au registre à ce stade.

Sources : `2 FINANCE/PREVISIONS/2026 1027 Business plan Lean V1.md`, hypothèses/budget/résultats ; `2 FINANCE/PREVISIONS/2026 1027 Acquisition et economie unitaire V1.md`, hypothèses/tests ; `2 FINANCE/PREVISIONS/2026 1027 Registre des hypotheses Finance.md`, H01–H08 ; `2 FINANCE/PREVISIONS/2026 1027 Demande de cadrage Produit Technique.md`. **Propositions non validées.**
