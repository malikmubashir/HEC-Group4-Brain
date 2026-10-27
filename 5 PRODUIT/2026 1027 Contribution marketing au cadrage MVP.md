# Contribution marketing au cadrage du MVP

**Date :** 27 octobre 2026
**Auteur :** Assistant IA Marketing, à la demande de la directrice marketing
**Nature :** proposition, soumise à approbation (voir [[RULES]])
**Répond à :** [[2026 1027 Demande de cadrage Produit Technique]], questions 1 (missions) et 3 (autonomie), sous l'angle de la valeur utilisateur
**Rangement :** `3 MARKETING/MARCHE/`

> **Périmètre.** Cette note donne le point de vue **utilisateur et marché**. L'architecture, les modèles IA, la mesure des coûts et le plan de développement (questions 2, 4 et 5) relèvent de `5 PRODUIT/` et `6 OPERATIONS/`. Le périmètre du MVP sera **décidé par le responsable Produit et l'équipe**, puis noté dans [[REGISTRE DES DECISIONS]].
>
> **Statut des missions.** La liste est **provisoire**. Elle sera confirmée ou modifiée après les entretiens (guide, questions 3 à 6 : [[2026 1027 Validation de la cible et guide d'entretien]]).

Cible de référence : cadre supérieur très actif (cible principale), avec quelques missions de coordination familiale pour tester la cible secondaire.

---

## 1. Les 10 missions prioritaires

Niveaux de validation : **A** = automatique, **C** = confirmation avant action, **X** = exclu du MVP (voir § 3).
L'intensité IA est une **inférence** marketing destinée à orienter la Finance. Les coûts réels restent à mesurer par Produit.

| # | Mission | Résultat attendu | Limites MVP | Validation | Intensité IA (inférence) |
|---|---|---|---|---|---|
| 1 | **Briefing quotidien** | Chaque matin, un message de 3 à 5 points : rendez-vous, échéances, actions à valider | Lecture seule (agenda, emails, Drive) | A | Moyenne, quotidienne |
| 2 | **Suivi des échéances personnelles** | Échéances repérées dans les emails et documents (assurance, contrôle technique, papiers d'identité, impôts), avec rappel à J-30 et J-7 | Rappel seulement, aucune démarche sur un portail officiel | A | Faible |
| 3 | **Prise de rendez-vous de service** (garage, coiffeur, artisan) | 2 ou 3 créneaux compatibles avec l'agenda, puis rendez-vous pris et ajouté au calendrier | Plateformes avec réservation en ligne uniquement ; pas d'appel téléphonique | C | Moyenne |
| 4 | **Réservation de restaurant** | 3 propositions selon les préférences, puis réservation confirmée | Pas de prépaiement ni d'empreinte bancaire | C | Moyenne |
| 5 | **Organisation d'un déplacement privé** (week-end, court séjour) | Un programme avec 2 ou 3 options de transport et d'hébergement, chiffrées | Le majordome prépare, l'utilisateur paie lui-même | C | Élevée |
| 6 | **Brouillons d'emails personnels** (école, syndic, prestataires) | Brouillon prêt à envoyer, dans le ton de l'utilisateur | Envoi uniquement après validation | C | Moyenne |
| 7 | **Coordination de l'agenda familial** | Conflits détectés (activités des enfants, garde, déplacements) et solution proposée | Calendriers partagés existants ; pas encore de profils multiples | C dès qu'un tiers est concerné | Moyenne |
| 8 | **Suivi des abonnements** | Inventaire tiré des emails, alerte avant renouvellement, lettre de résiliation préparée | Envoi après validation ; pas d'accès bancaire | C | Faible |
| 9 | **Relances et engagements en attente** (devis, réponses attendues) | Liste des attentes avec relance préparée au bon moment | Envoi après validation | C | Faible |
| 10 | **Préparation d'un événement personnel** (anniversaire, cadeau, dîner) | Rappel anticipé, idées et organisation, réservation si besoin | Aucun achat en ligne pour le MVP | C | Moyenne |

**Logique du choix (inférence) :** les missions 1, 2 et 9 sont peu coûteuses et créent une **habitude quotidienne**, ce qui soutient la rétention. Les missions 3, 4 et 5 sont celles qui **démontrent la promesse** : il agit pour vous. Les missions 7 et 10 servent à tester la cible famille.

## 2. Indispensables et reportées

**Indispensables pour le MVP (proposition)**
- Connecteurs Gmail, Google Agenda et Drive (repris de la feuille de route V1).
- Mémoire des préférences de l'utilisateur : lieux, horaires, contraintes, personnes du foyer.
- Écran de validation en un geste : valider, modifier ou refuser.
- **Journal des actions**, consultable à tout moment.
- Réglage des autorisations par type de mission.
- Briefing quotidien, notifications, interface conversationnelle écrite.

**Reportées après le pilote**
- Paiement et achat effectués par le majordome.
- Appels téléphoniques et assistant vocal.
- Profils multiples et offre Family complète.
- Démarches sur portails officiels (impôts, ANTS, CAF).
- Connecteurs Microsoft et Apple.
- Données de santé et accès bancaire.
- Prestations physiques par des partenaires.

## 3. Validations nécessaires avant action

| Niveau | Règle | Exemples |
|---|---|---|
| **A — Automatique** | Lecture, synthèse, rappel adressé **à l'utilisateur seul** | Briefing, détection d'échéance, inventaire des abonnements |
| **C — Confirmation** | Toute action visible par un **tiers** ou qui **engage** l'utilisateur | Envoyer un email, réserver, modifier un agenda partagé, annuler |
| **X — Exclu du MVP** | Paiement, signature, transmission de données sensibles, démarche officielle en son nom | Payer un billet, résilier par prélèvement, transmettre un document d'identité |

Cohérence : c'est conforme au projet de CGV-CGU, art. 10 : achats, paiements, engagements et données sensibles exigent une validation spécifique (`7 JURIDIQUE RH/CONTRATS/`, projet non signé). C'est aussi conforme à la promesse client, engagement n° 2 ([[2026 1027 Promesse client]]).

## 4. Parcours utilisateurs

**P1 — Premier jour (onboarding, environ 10 minutes)**
Inscription → connexion de Gmail, de l'Agenda et de Drive → 5 questions de préférences (foyer, lieux, horaires) → choix des autorisations par mission → premier briefing généré immédiatement (« effet waouh »).

**P2 — Demande de l'utilisateur**
« Réserve-moi un restaurant jeudi pour 4 » → le majordome propose 3 options → l'utilisateur valide → réservation effectuée → confirmation et ajout à l'agenda → ligne au journal.

**P3 — Proactivité**
Le majordome détecte une échéance, un conflit ou une relance → suggestion dans le briefing → l'utilisateur valide, modifie ou ignore → exécution → ligne au journal.

**P4 — Erreur ou refus**
L'utilisateur corrige une proposition → le majordome retient la préférence → l'incident est compté dans les indicateurs de fiabilité.

## 5. Critères de réussite du pilote (10 utilisateurs, propositions de seuils)

| Critère | Mesure | Seuil proposé |
|---|---|---|
| **Sécurité** (bloquant) | Actions exécutées sans autorisation | **0** |
| Fiabilité | Missions réussies sans correction ÷ missions lancées | ≥ 80 % |
| Pertinence | Suggestions proactives validées ÷ suggestions faites | ≥ 50 % |
| Usage | Utilisateurs avec au moins 3 missions par semaine | ≥ 7 sur 10 |
| Rétention | Utilisateurs **actifs** en semaine 4 (pas seulement inscrits) | ≥ 7 sur 10 |
| Valeur perçue | Temps gagné déclaré par semaine | ≥ 2 h (à comparer à l'hypothèse de 3 h de la V1) |
| Disposition à payer | Utilisateurs prêts à payer 79 € après le pilote | ≥ 5 sur 10 |
| Économie | Coût variable mesuré par utilisateur et par mois | ≤ 18 € HT (hypothèse Finance, non vérifiée) |

Seuils à valider par l'équipe **avant** le pilote.

## 6. Arbitrages recommandés (proposition)

1. **Adopter la liste des 10 missions comme base provisoire**, révisable après les entretiens.
2. **Exclure tout paiement du MVP.** Cela réduit le risque juridique, le risque de confiance et le coût de développement.
3. **Faire du critère de sécurité un critère éliminatoire** : une seule action non autorisée suffit à arrêter le pilote.
4. **Demander à Produit de mesurer en priorité le coût des missions 1 et 5**, la plus fréquente et la plus coûteuse, qui bornent l'économie unitaire.
