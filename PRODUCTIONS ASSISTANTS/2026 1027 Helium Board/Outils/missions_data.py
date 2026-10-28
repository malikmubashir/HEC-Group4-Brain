# -*- coding: utf-8 -*-
"""Données du classeur Helium_Cout_par_mission_V1 : tarifs, missions, offres, plan de charge.
Les prix sont renseignés depuis research/llm-pricing.md, infra-services.md, benchmarks-rates.md (octobre 2026).
"""

# (clé, poste, valeur, unité, nature, source, date, note)
PRICES = [
    ("fx", "Taux de change dollar → euro", 0.877, "€ par $", "Tarif public", "BCE, taux de référence 1 € = 1,1403 $ : https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html", "25/09/2026", "Dernier taux publié sur la page lue le 28/10/2026 ; à relire le jour du calcul."),
    ("small_in", "Petit modèle, entrée (Mistral Small 4, point d'accès UE api.eu.mistral.ai, +10 %)", 0.165, "$ / M jetons", "Tarif public", "https://docs.mistral.ai/models/pricing (0,15 $) et https://docs.mistral.ai/inference/regional-inference (×1,1)", "28/10/2026", "Alternative : Claude Haiku 5.5 sur Bedrock UE 0,11 $ ; Scaleway mistral-small-3.2 0,15 € (Paris, sans surcoût)."),
    ("small_cached", "Petit modèle, entrée cachée (10 % du prix d'entrée)", 0.0165, "$ / M jetons", "Tarif public", "https://docs.mistral.ai/models/pricing", "28/10/2026", ""),
    ("small_out", "Petit modèle, sortie", 0.66, "$ / M jetons", "Tarif public", "https://docs.mistral.ai/models/pricing (0,60 $ × 1,1)", "28/10/2026", ""),
    ("mid_in", "Modèle moyen, entrée (Claude Sonnet 5.5, Amazon Bedrock profil UE, +10 %)", 2.20, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/about-claude/pricing (2 $) et https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock (+10 % régional)", "28/10/2026", "Alternatives : gpt-6.1-sol sur eu.api.openai.com 2,20 $ ; Mistral Medium 3.5 UE 1,65 $ ; Mistral Large 4 UE 1,50 $."),
    ("mid_cached", "Modèle moyen, entrée cachée (lecture de cache, 5 % du prix d'entrée)", 0.11, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/build-with-claude/prompt-caching (0,10 $ × 1,1)", "28/10/2026", "Écriture de cache +25 % sur 5 min, non comptée ici (contexte stable réutilisé)."),
    ("mid_out", "Modèle moyen, sortie", 11.0, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/about-claude/pricing (10 $ × 1,1)", "28/10/2026", ""),
    ("front_in", "Modèle frontière, entrée (Claude Opus 5.5, Bedrock profil UE, +10 %)", 4.40, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/about-claude/pricing (4 $ × 1,1)", "28/10/2026", "Escalade des cas difficiles seulement. Fable 5.1 (10 / 50 $) exclu : retention 30 jours imposée, pas de point d'accès UE."),
    ("front_cached", "Modèle frontière, entrée cachée", 0.22, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/about-claude/pricing (0,20 $ × 1,1)", "28/10/2026", ""),
    ("front_out", "Modèle frontière, sortie", 22.0, "$ / M jetons", "Tarif public", "https://platform.claude.com/docs/en/about-claude/pricing (20 $ × 1,1)", "28/10/2026", ""),
    ("embed", "Embeddings (Mistral Embed, point d'accès UE)", 0.11, "$ / M jetons", "Tarif public", "https://docs.mistral.ai/models/pricing (0,10 $ × 1,1) ; Scaleway 0,10 €", "28/10/2026", ""),
    ("search_call", "Recherche web (Brave Search API)", 0.005, "$ / requête", "Tarif public", "https://api-dashboard.search.brave.com/documentation/pricing (5 $ pour 1 000 requêtes)", "28/10/2026", "Alternatives : Exa 7 $, Tavily 8 $ pour 1 000. Rétention zéro sur offre Entreprise."),
    ("places_call", "Google Places API (New) : moyenne d'une recherche textuelle Pro (32 $) et de deux fiches Pro (17 $) pour 1 000", 0.022, "$ / requête", "Tarif public", "https://developers.google.com/maps/billing-and-pricing/pricing", "28/10/2026", "5 000 événements gratuits par mois et par SKU : le pilote reste gratuit."),
    ("page_read", "Lecture d'une page web (Firecrawl, offre Hobby : 19 $ pour 5 000 pages)", 0.0038, "$ / page", "Tarif public", "https://www.firecrawl.dev/pricing.md", "28/10/2026", "Jina Reader environ 0,0005 $ par page (source secondaire)."),
    ("browser_min", "Navigateur piloté dans le nuage, infrastructure et proxy résidentiel", 0.012, "$ / minute", "Tarif public", "Browserbase 0,12 $ par heure-navigateur (https://docs.browserbase.com/account/billing/plans.md) soit 0,002 $/min ; proxy résidentiel 10 $/Go, environ 1 Mo par minute soit 0,01 $/min", "28/10/2026", "Hors jetons du modèle qui pilote (comptés dans les appels moyens). Browser Use Cloud 0,02 $/h, Anchor 0,05 $/h : l'infrastructure est négligeable, le proxy et les jetons font le coût."),
    ("support_min", "Support humain", 0.50, "€ / minute", "Hypothèse", "30 € HT de l'heure chargée (fondateur puis customer success)", "28/10/2026", "Cohérent avec l'embauche 1 du modèle 36 mois (4 500 € chargés)."),
    ("hosting_user", "Hébergement, stockage, connecteurs, par abonné et par mois", 1.5, "€ / abonné", "Hypothèse", "Modèle 36 mois, central ; détail dans la réponse au cadrage § 3.5", "28/10/2026", "Coût fixe de la plateforme réparti ; vaut à partir de ~300 abonnés."),
    ("stripe_pct", "Frais de paiement, part variable : carte EEE 1,5 % + Stripe Billing 0,7 % + Stripe Tax 0,5 %", 0.027, "%", "Tarif public", "https://stripe.com/fr/pricing", "28/10/2026", "Par prélèvement SEPA : 0,35 € fixe + 1,2 %, soit 1,30 € sur 79 €."),
    ("stripe_fixed", "Frais de paiement, part fixe (carte)", 0.25, "€ / transaction", "Tarif public", "https://stripe.com/fr/pricing", "28/10/2026", ""),
]

# Paliers (texte) : palier, rôle, modèle recommandé, alternative UE, prix entrée, prix sortie, résidence, note
MODEL_TIERS = [
    ("Petit", "Tri des courriels, extraction d'échéances et d'entités, lecture de pages, lecture initiale en lot", "Mistral Small 4 sur api.eu.mistral.ai (Mistral AI, Paris ; traitement dans l'UE et l'AELE)", "Claude Haiku 5.5 via Amazon Bedrock profil UE ; Scaleway mistral-small-3.2 (Paris, rétention zéro par défaut)", "0,165 (0,15 × 1,1)", "0,66", "UE / AELE ; rétention zéro sur demande (plan payant)", "Le socle lit les données les plus sensibles : un fournisseur européen y est préféré. Lot (−50 %) indisponible sur le point d'accès régional : l'activation M11 passe par le point d'accès global ou Scaleway."),
    ("Moyen", "Planification des missions, appels d'outils, pilotage du navigateur, rédaction dans le ton de l'utilisateur", "Claude Sonnet 5.5 via Amazon Bedrock, profil d'inférence UE (données traitées dans les régions UE, dont Paris eu-west-3)", "gpt-6.1-sol sur eu.api.openai.com (+10 %, résidence UE sur approbation) ; Mistral Medium 3.5 ou Large 4 sur api.eu.mistral.ai", "2,20 (2 × 1,1)", "11,0", "UE (profil Bedrock) ; AWS est sous-traitant ; rétention selon Bedrock", "Retenu pour les scores d'agents (tau2-bench, OSWorld) ; Mistral Large 4 testé en bascule au pilote, deux fois moins cher en sortie."),
    ("Frontière", "Escalade après deux échecs du modèle moyen ; cas ambigus ; 5 % des appels moyens en base, plafond 10 %", "Claude Opus 5.5 via Amazon Bedrock profil UE", "gpt-6-astra (10 / 50 $) ; Gemini 4 Argon (2 / 10 $, 4 / 20 $ dès le 1er décembre 2026, sans option de région sur l'API Gemini)", "4,40 (4 × 1,1)", "22,0", "UE (profil Bedrock)", "Fable 5.1 écarté : rétention 30 jours imposée et points d'accès régionaux limités aux États-Unis."),
]

# Missions : paramètres (hypothèses d'ingénierie, abonné Premium)
def M(num, name, prio, level, freq, n_s, in_s, c_s, out_s, n_m, in_m, c_m, out_m, f_f, srch, plc, pg, brw, retry, succ, dur, h_share, h_min, emb, scenario):
    return dict(num=num, name=name, prio=prio, level=level, freq=freq, n_s=n_s, in_s=in_s, c_s=c_s, out_s=out_s, n_m=n_m, in_m=in_m, c_m=c_m, out_m=out_m, f_f=f_f, srch=srch, plc=plc, pg=pg, brw=brw, retry=retry, succ=succ, dur=dur, h_share=h_share, h_min=h_min, emb=emb, scenario=scenario)

MISSIONS = [
    M("M0", "Socle : tri quotidien des courriels et de l'agenda (partagé par M1, M2, M8, M9)", "Socle", "A", 30,
      1, 20000, 0.20, 1500, 0, 0, 0, 0, 0.0, 0, 0, 0, 0, 1.05, 0.97, 1, 0.0, 0, 2000,
      "Chaque nuit : lecture des courriels des 24 dernières heures (environ 40 × 300 jetons), de l'agenda et des documents que l'utilisateur a confiés à Helium (périmètre drive.file) ; le petit modèle classe, résume et extrait les entités (échéances, engagements, abonnements, relances). Résumés et entités stockés en mémoire avec embeddings. Aucune action."),
    M("M1", "Briefing quotidien", "1", "A", 30,
      0, 0, 0, 0, 1, 8000, 0.50, 600, 0.0, 0, 0, 0, 0, 1.05, 0.95, 1, 0.10, 3, 0,
      "Chaque matin : le modèle moyen compose 3 à 5 points à partir des résumés du socle, de l'agenda du jour et des actions en attente de validation. Contexte système et préférences en cache."),
    M("M2", "Suivi des échéances personnelles", "1", "A", 8,
      1, 6000, 0.0, 400, 1, 5000, 0.40, 300, 0.0, 0, 0, 0, 0, 1.10, 0.90, 2, 0.10, 3, 0,
      "Quand le socle détecte une échéance (assurance, contrôle technique, papiers, impôts) : le petit modèle extrait date et objet, le modèle moyen confirme et planifie les rappels J-30 et J-7. Aucune démarche sur un portail."),
    M("M3", "Prise de rendez-vous de service (garage, coiffeur, artisan)", "2", "C", 1,
      2, 4000, 0.0, 300, 15, 12000, 0.40, 250, 0.05, 1, 3, 0, 8, 1.40, 0.65, 12, 0.40, 6, 0,
      "Compréhension de la demande, recherche de prestataires (Places), lecture des créneaux libres dans l'agenda, proposition de 2 ou 3 créneaux ; après validation, réservation sur la plateforme en ligne du prestataire par navigateur piloté (environ 15 étapes de 12 k jetons, arbre d'accessibilité plutôt que captures d'écran), puis ajout au calendrier et journal. Pas d'appel téléphonique."),
    M("M4", "Réservation de restaurant", "2", "C", 2,
      2, 4000, 0.0, 300, 12, 12000, 0.40, 250, 0.05, 0, 4, 0, 6, 1.30, 0.70, 10, 0.30, 5, 0,
      "Trois propositions selon les préférences (Places) ; après validation, réservation par l'API partenaire quand elle existe (TheFork, Mozrest), sinon par navigateur piloté sur le site du restaurant ou de sa plateforme (environ 12 étapes de 12 k jetons) ; confirmation, calendrier, journal. Ni prépaiement ni empreinte bancaire."),
    M("M5", "Organisation d'un déplacement privé", "2", "C", 0.5,
      4, 8000, 0.0, 500, 6, 15000, 0.30, 800, 0.10, 8, 0, 10, 0, 1.20, 0.75, 20, 0.20, 8, 0,
      "Recherche (8 requêtes), lecture de 10 pages (transport, hébergement), extraction par le petit modèle, synthèse par le modèle moyen en un programme à 2 ou 3 options chiffrées. L'utilisateur paie lui-même : aucune réservation dans le MVP."),
    M("M6", "Brouillons de courriels personnels", "1", "C", 6,
      0, 0, 0, 0, 1, 6000, 0.50, 500, 0.0, 0, 0, 0, 0, 1.15, 0.85, 1, 0.05, 2, 0,
      "Le modèle moyen rédige dans le ton de l'utilisateur à partir du fil et des préférences de style ; envoi par l'API Gmail après validation ; journal."),
    M("M7", "Coordination de l'agenda familial", "2", "C", 4,
      1, 5000, 0.0, 300, 1, 8000, 0.50, 400, 0.0, 0, 0, 0, 0, 1.10, 0.80, 2, 0.10, 3, 0,
      "Lecture des calendriers partagés (API), détection des conflits par le petit modèle, proposition de solution par le modèle moyen ; modification de l'agenda partagé après validation."),
    M("M8", "Suivi des abonnements", "3", "C", 1,
      1, 10000, 0.0, 500, 1.5, 6000, 0.40, 400, 0.0, 0, 0, 0, 0, 1.10, 0.85, 3, 0.10, 4, 0,
      "Mise à jour mensuelle de l'inventaire à partir du socle, alerte avant renouvellement, lettre de résiliation préparée (une fois sur deux) ; envoi après validation, pas d'accès bancaire. L'inventaire initial est dans M11."),
    M("M9", "Relances et engagements en attente", "1", "C", 4,
      0.5, 4000, 0.0, 200, 1, 4000, 0.50, 300, 0.0, 0, 0, 0, 0, 1.10, 0.85, 1, 0.05, 2, 0,
      "Liste des attentes (devis, réponses) tenue par le socle ; relance rédigée au bon moment par le modèle moyen ; envoi après validation."),
    M("M10", "Préparation d'un événement personnel", "3", "C", 0.5,
      1, 6000, 0.0, 400, 3, 10000, 0.30, 800, 0.05, 3, 1, 0, 3, 1.20, 0.70, 15, 0.20, 5, 0,
      "Rappel anticipé, idées et organisation (recherche, Places), réservation éventuelle par navigateur piloté (réutilise M4) ; aucun achat en ligne."),
    M("M11", "Activation : lecture initiale de la boîte et profil (une fois par nouvel abonné)", "Socle", "A", 0,
      1, 400000, 0.0, 20000, 1, 15000, 0.0, 800, 0.0, 0, 0, 0, 0, 1.0, 0.95, 30, 0.10, 5, 400000,
      "À l'inscription : lecture des 12 derniers mois de courriels (environ 2 000 × 200 jetons) par le petit modèle en lot, inventaire des abonnements, échéances, personnes du foyer, lieux ; profil de préférences établi par le modèle moyen et confirmé par l'utilisateur. Compté comme coût d'activation, pas comme coût mensuel."),
]

# Offres : prix TTC, missions/mois dans le modèle 36 mois, multiplicateurs de fréquence par mission
OFFERS = [
    dict(name="Personal", price_ttc=29, m36=20, mult={"M0": 1, "M1": 0.25, "M2": 1, "M6": 0.5, "M9": 0.5, "M8": 1}),
    dict(name="Premium", price_ttc=79, m36=60, mult={m: 1 for m in ("M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "M10")}),
    dict(name="Family", price_ttc=129, m36=90, mult={"M0": 1, "M1": 1, "M2": 1.5, "M3": 2, "M4": 2, "M5": 1.5, "M6": 1.5, "M7": 3, "M8": 1.5, "M9": 1.5, "M10": 2}),
]

# Protections : (nom, règle, [Personal, Premium, Family], note)
PROTECTIONS = [
    ("Plafond de missions par mois", "Au-delà, le majordome propose mais n'exécute plus les missions C jusqu'au mois suivant ; l'utilisateur est prévenu à 80 %.", [30, 90, 150], "Le modèle 36 mois suppose 20 / 60 / 90 missions : le plafond laisse 50 % de marge d'usage."),
    ("Plafond de navigateur piloté (minutes par mois)", "Les missions 3, 4 et 10 consomment le quota ; au plafond, le majordome prépare la réservation et laisse l'utilisateur cliquer.", [0, 60, 120], "Le navigateur piloté est le poste le plus cher et le moins fiable."),
    ("Budget de jetons par mission", "Chaque mission a un budget de jetons et d'étapes ; dépassement = arrêt propre, message à l'utilisateur, ligne au journal.", ["200 k", "400 k", "400 k"], "Empêche les boucles. Valeurs à caler sur les mesures des missions 3 et 4."),
    ("Escalade vers le modèle frontière", "Seulement après deux échecs du modèle moyen, et jamais pour le socle.", ["non", "≤ 10 %", "≤ 10 %"], "Part des appels moyens escaladés ; 5 % en base dans l'onglet Missions."),
    ("Alerte de coût par abonné", "Si le coût IA et outils du mois dépasse 25 % du prix HT, alerte interne ; à 40 %, revue manuelle et proposition de changement d'offre.", ["25 % / 40 %", "25 % / 40 %", "25 % / 40 %"], "Le classeur donne le coût au plafond ci-dessous."),
    ("Coupe-circuit global", "Si la dépense API journalière dépasse 3 fois la moyenne glissante sur 7 jours, les missions C sont suspendues et l'astreinte est prévenue.", ["oui", "oui", "oui"], "Protège contre un bug ou une injection qui ferait boucler des missions."),
    ("Clés et quotas fournisseurs", "Clés par environnement, quotas durs chez chaque fournisseur (plafond mensuel en dollars), rotation trimestrielle.", ["oui", "oui", "oui"], "Les fournisseurs permettent un plafond de dépense mensuel au niveau du compte."),
]

# Taux journaliers : (clé, profil, TJM retenu, fourchette source, nature, source, date)
RATES = [
    ("dev", "Développeur full-stack senior (externe)", 650, "Hays 2026 Paris, 8 ans et plus : 650 ; Paris confirmé 550 à 680, senior 670 et plus (La Fabrique du Net, juil. 2026)", "Tarif public", "https://www.blogdumoderateur.com/freelance-tech-taux-journaliers-moyens-metier-2026/ (étude Hays 2026) ; https://www.lafabriquedunet.fr/agences/tendances/tarifs-des-developpeurs-freelances-dans-les-grandes-villes-de-france", "28/10/2026"),
    ("ia", "Ingénieur IA / LLM (externe)", 800, "Malt Tech Trends 2025 : expert 670 à 750 (moyennes européennes 2024) ; Michael Page Île-de-France : 600 à 1 000", "Tarif public", "https://pages.malt.fr/hubfs/NEW%20-%20E-books%20visuals/Malt%20Tech%20Trends%202025/Malt%20Tech%20Trends%202025%20-%20FR.pdf ; https://www.michaelpage.fr/grilles-de-salaires/technology/", "28/10/2026"),
    ("ux", "Product designer UX/UI (externe)", 550, "450 à 700, médiane environ 510 (baromètre compilé 2026) ; moyenne 423 (Kicklox / RH Solutions 2025)", "Tarif public", "https://www.freelance-solution.fr/barometre-tjm-freelance-2026/ ; https://www.rh-solutions.com/app/uploads/2025/12/RHS-Etude-2025-les-TJM-freelances_compressed.pdf", "28/10/2026"),
    ("sec", "Pentest application et API, jour d'auditeur (prestataire)", 1150, "900 à 1 500 (PASSI 1 200 à 1 500, non PASSI 900 à 1 200) ; pentest boîte grise app + API 8 000 à 12 000 € plus contre-test 1 000 à 2 500 €", "Tarif public", "https://kolonell.com/fr/blog/prix-pentest-application-web-pme-france-2026 (1er oct. 2026, source fournisseur)", "28/10/2026"),
    ("rgpd", "Consultant RGPD / AIPD (externe)", 850, "800 à 900 (tarifs illustratifs ; aucun barème publié) ; AIPD estimée 4 à 8 jours", "Hypothèse", "https://www.legiscope.com/blog/dpo-externalise-cout.html ; https://donneespersonnelles.fr/dpo-externalise-tarifs", "28/10/2026"),
    ("f_cto", "Fondateur, architecture et sécurité (Malik)", 0, "non facturé", "Hypothèse", "Fondateurs non rémunérés M1 à M12 (hypothèse Finance)", "28/10/2026"),
    ("f_prod", "Fondateur, produit et recette (Steve)", 0, "non facturé", "Hypothèse", "Idem", "28/10/2026"),
    ("f_ops", "Fondateur, exploitation et support (Isaac)", 0, "non facturé", "Hypothèse", "Idem", "28/10/2026"),
]

# Chantiers : (chantier, profil, jours Lean, jours Confort, note)
WORKLOAD = [
    ("W0 Architecture, choix techniques, revue de sécurité", "f_cto", 15, 15, "Avant tout code : schéma de données, politique A/C/X, mandats, journal. Dépendance : D-01 (qui continue) et D-02 (nom, domaine)."),
    ("W1 Socle : comptes, OAuth Google, ingestion, mémoire, journal", "dev", 18, 15, "Connecteur Gmail/Agenda/Drive en périmètres restreints ; chiffrement des jetons OAuth ; file de missions durable (PostgreSQL)."),
    ("W2 Passerelle modèles, orchestrateur, moteur de politique", "ia", 16, 14, "Routage petit/moyen/frontière, cache de contexte, budgets par mission, traces de coût. Dépendance : W1."),
    ("W3 Missions de lecture et de rédaction (M0, M1, M2, M6, M9)", "dev", 14, 12, "Premières missions livrées au pilote ; mesurent le coût du socle et du briefing."),
    ("W4 Missions de coordination et d'inventaire (M7, M8, M11)", "dev", 10, 8, "Calendriers partagés, inventaire des abonnements, activation."),
    ("W5 Missions à navigateur piloté (M3, M4, M10)", "ia", 18, 16, "Le chantier le plus risqué : sites sans API, CAPTCHA, conditions d'utilisation. Mesurer M3 et M4 avant d'investir davantage."),
    ("W6 Mission de recherche (M5)", "ia", 6, 5, "Recherche, lecture de pages, synthèse chiffrée ; pas de réservation."),
    ("W7 Conception UX : onboarding, écran de validation, journal, briefing", "ux", 12, 15, "Maquettes puis tests avec les 10 pilotes."),
    ("W8 Application web (PWA) : front, notifications, facturation Stripe", "dev", 20, 18, "Dépendance : W7 ; PWA plutôt que magasins d'applications pour le MVP."),
    ("W9 Sécurité : pentest boîte grise (application et API) et contre-test", "sec", 9, 10, "Avant l'ouverture au-delà des 10 pilotes ; 8 000 à 12 000 € plus contre-test selon le marché 2026 ; devis à obtenir."),
    ("W10 RGPD : AIPD, registre, politiques, charte agents", "rgpd", 5, 6, "Avec Tiffany ; l'AIPD est obligatoire avant le pilote (lecture de courriels)."),
    ("W11 Vérification OAuth Google et évaluation CASA", "f_cto", 6, 6, "Dossier, vidéo de démonstration, domaine vérifié, politique de confidentialité publiée ; délai externe de 4 à 8 semaines, à lancer en janvier."),
    ("W12 Exploitation : hébergement, supervision, sauvegardes, astreinte", "f_ops", 10, 10, "Scaleway Paris ; procédures d'incident et de violation de données."),
    ("W13 Recette, pilote, support des 10 pilotes, mesures", "f_prod", 25, 25, "Protocole de mesure des missions 1, 5 puis 3, 4 ; rapport de pilote pour la porte J+90."),
    ("W14 Second développeur (variante Confort seulement)", "dev", 0, 40, "Parallélise W3 à W5 et W8 ; raccourcit le calendrier d'environ six semaines."),
]

# Autres coûts : (poste, base, Lean, Confort, source)
NONLABOUR = [
    ("API modèles et outils pendant la construction et le pilote (5 mois)", "5 mois × 400 €", 2000, 3000, "Hypothèse : 10 pilotes × coût mensuel + tests d'ingénierie ; voir Synthèse."),
    ("Hébergement et services pendant la construction (5 mois)", "5 mois × 250 €", 1250, 1500, "Scaleway Paris, base de données gérée, stockage, supervision ; détail dans la réponse au cadrage."),
    ("Évaluation de sécurité CASA niveau AL1 (laboratoire agréé, première année)", "forfait", 1500, 2500, "Marché 540 à 1 800 $ par an au niveau AL1 (TAC Security, Netsentries, Leviathan) ; renouvellement annuel ; vérification Google elle-même gratuite. Source : references prix et benchmarks, § infra 10.2."),
    ("Juridique : statuts, pacte, CGV, politiques", "forfait", 4000, 4000, "Business plan Lean V1 (Finance)."),
    ("Tests utilisateurs et acquisition pilote", "forfait", 5000, 5000, "Business plan Lean V1 (Finance)."),
    ("Logiciels, outils de développement, observabilité", "5 mois × 300 €", 1500, 2000, "Hypothèse."),
    ("Nom de domaine, marque (recherche d'antériorité, dépôt INPI)", "forfait", 1500, 1500, "Hypothèse ; dépôt INPI une classe environ 190 € + recherche."),
]

# Tableau commun : (num, scénario, modèle IA, appels/outils, risque, décision)
COMMON_TABLE = [
    ("M0", "Lecture nocturne des courriels, de l'agenda et de Drive ; classement, résumés, entités en mémoire.", "Petit", "1 appel petit modèle par nuit (≈ 20 k jetons) ; API Gmail, Agenda, Drive (gratuites) ; embeddings.", "Injection de prompt par un courriel : le socle ne doit jamais déclencher d'action. Volume de courriels très variable selon l'utilisateur.", "Construire en premier ; contenu des courriels traité comme données non fiables ; aucune capacité d'action."),
    ("M1", "Composition matinale de 3 à 5 points à partir du socle.", "Moyen", "1 appel moyen (≈ 8 k jetons, moitié en cache).", "Banalité : un briefing sans valeur perçue fait partir l'utilisateur.", "Mission d'habitude : livrer au pilote dès le jour 1 ; mesurer l'ouverture quotidienne."),
    ("M2", "Extraction et confirmation des échéances, rappels J-30 et J-7.", "Petit puis moyen", "1 appel petit + 1 appel moyen par échéance.", "Faux positifs (fausse échéance) et oublis ; aucune démarche officielle.", "Inclure ; rappel seulement ; taux de faux positifs à mesurer."),
    ("M3", "Recherche de prestataires, créneaux, réservation en ligne par navigateur piloté après validation.", "Moyen, escalade frontière 5 %", "≈ 15 appels moyens, 2 petits ; Places × 3 ; navigateur 8 min.", "Pas d'API chez la plupart des plateformes ; CAPTCHA et conditions d'utilisation ; échec en cours de parcours.", "Inclure sur un périmètre de plateformes testé ; au plafond de minutes, l'utilisateur termine lui-même."),
    ("M4", "Propositions puis réservation par navigateur piloté après validation.", "Moyen, escalade frontière 5 %", "≈ 12 appels moyens, 2 petits ; Places × 4 ; navigateur 6 min ; API partenaire si accord TheFork ou Mozrest.", "Idem M3 ; double réservation si reprise mal gérée.", "Inclure ; idempotence des réservations ; mesurer dès le pilote (mission qui démontre la promesse)."),
    ("M5", "Recherche, lecture de pages, programme à 2 ou 3 options chiffrées ; aucune réservation.", "Moyen, petit pour l'extraction", "8 recherches, 10 lectures de page, 6 appels moyens, 4 petits.", "Qualité de la synthèse ; prix périmés ; Code du tourisme si réservation.", "Inclure sans réservation ; la mission la plus coûteuse en jetons, à mesurer en premier avec M1."),
    ("M6", "Brouillon dans le ton de l'utilisateur, envoi après validation.", "Moyen", "1 appel moyen.", "Ton inadapté ; envoi sans validation (interdit par le moteur de politique).", "Inclure ; mesurer le taux de brouillons envoyés sans modification."),
    ("M7", "Détection des conflits d'agenda, proposition, modification après validation.", "Petit puis moyen", "1 petit + 1 moyen ; API Agenda.", "Tiers concernés (conjoint, enfants) : validation à chaque fois.", "Inclure pour tester la cible famille ; profils multiples reportés."),
    ("M8", "Inventaire mensuel des abonnements, alertes, lettre de résiliation préparée.", "Petit puis moyen", "1 petit + 1,5 moyen.", "Inventaire incomplet ; résiliation par prélèvement exclue.", "Inclure (faible coût, forte valeur perçue) ; pas d'accès bancaire."),
    ("M9", "Liste des attentes, relance rédigée au bon moment, envoi après validation.", "Moyen", "0,5 petit + 1 moyen.", "Relance inopportune ; doublon avec M6.", "Inclure ; fusionner l'interface avec M6."),
    ("M10", "Rappel, idées, organisation, réservation éventuelle (réutilise M4).", "Moyen", "3 moyens, 1 petit ; recherches × 3 ; Places ; navigateur 3 min.", "Faible fréquence, forte variabilité.", "Reporter après le pilote si M3 et M4 ne tiennent pas leurs mesures ; sinon inclure."),
    ("M11", "Lecture initiale de 12 mois de courriels en lot, profil de préférences confirmé par l'utilisateur.", "Petit en lot, moyen pour le profil", "≈ 400 k jetons petit modèle en lot (tarif lot −50 %), embeddings, 1 appel moyen.", "Coût d'activation ; données particulières incidentes (santé, opinions) à détecter et ne pas conserver.", "Inclure avec filtrage des données particulières ; compter dans le CAC."),
]
