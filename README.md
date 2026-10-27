# HEC Group 4 — second brain de l'équipe

> **Ce dépôt est privé, réservé à l'équipe.** Il doit le rester. Lire [RULES](RULES.md) avant d'ajouter quoi que ce soit.

Un second brain partagé : les documents de l'équipe, des notes reliées entre elles, des assistants IA par fonction, et un registre des décisions.

## Comment lire ce brain

| Dossier | Contenu | Assistant IA |
|---|---|---|
| [RULES](RULES.md) | Les règles que tout assistant (et tout membre de l'équipe) suit ici | — |
| [SOURCES](SOURCES.md) | La liste des pièces de `sources/`, leur nature, leur fiabilité, leurs contradictions | — |
| [`sources/`](sources/LISEZ-MOI.md) | Les pièces d'origine, jamais modifiées | — |
| [`0 INBOX/`](0%20INBOX/LISEZ-MOI.md) | Les nouveaux documents, pas encore traités | — |
| [`1 DIRECTION/`](1%20DIRECTION/AGENT.md) | Stratégie, gouvernance, synthèse entre fonctions, et le [registre des décisions](1%20DIRECTION/REGISTRE%20DES%20DECISIONS.md) | Assistant IA Direction |
| [`2 FINANCE/`](2%20FINANCE/AGENT.md) | Financement, trésorerie, prévisions, prix et marges | Assistant IA Finance |
| [`3 MARKETING/`](3%20MARKETING/AGENT.md) | Marché, utilisateurs, positionnement, concurrence, messages | Assistant IA Marketing |
| [`4 VENTES/`](4%20VENTES/AGENT.md) | Clients, prospects, pipeline, partenaires, contrats clients | Assistant IA Ventes |
| [`5 PRODUIT/`](5%20PRODUIT/AGENT.md) | Produits, versions, priorités, retours des utilisateurs | Assistant IA Produit |
| [`6 OPERATIONS/`](6%20OPERATIONS/AGENT.md) | Technique, fabrication, livraison, fournisseurs, délais | Assistant IA Opérations |
| [`7 JURIDIQUE RH/`](7%20JURIDIQUE%20RH/AGENT.md) | Statuts, contrats, équipe, recrutement ; tenue des sources | Assistant IA Juridique et RH, archiviste |
| [`PRODUCTIONS ASSISTANTS/`](PRODUCTIONS%20ASSISTANTS/LISEZ-MOI.md) | Ce que les assistants IA produisent à la demande | — |

Sept fonctions, sept dossiers : un par membre de l'équipe. Chaque dossier de fonction contient :
- `AGENT.md` : le rôle de l'assistant IA, ce qu'il lit, où il écrit, ses droits ;
- `README.md` : les faits datés de la fonction, chacun avec sa source.

Quatre couches, comme dans tout second brain : les **documents d'origine** (`sources/`), les **notes** en Markdown reliées par des liens entre doubles crochets, les **productions des assistants**, et le **registre des décisions**.

## Le cycle d'un document

1. On dépose le document dans `0 INBOX/`.
2. L'archiviste (`7 JURIDIQUE RH/`) le range dans `sources/` sous un identifiant (`S01`, `S02`…) et l'inscrit dans [SOURCES](SOURCES.md).
3. Les faits utiles passent dans le `README.md` de la fonction concernée, chacun avec sa source.
4. Une décision prise par un humain entre dans le [registre des décisions](1%20DIRECTION/REGISTRE%20DES%20DECISIONS.md).

## Comment interroger un assistant IA

> « Lis `RULES.md`, puis `2 FINANCE/AGENT.md`. Tu es l'assistant IA Finance de l'équipe. Nous sommes le **[date]**. Question : … »

La date compte : une question datée n'utilise que les faits connus à cette date.

## Travailler à plusieurs

- **Une personne = une fonction = un dossier.** Chacun n'écrit que dans le dossier de sa fonction, comme son assistant IA (voir son `AGENT.md`). Dans une équipe de six, une même personne prend deux dossiers ; ici `4 VENTES/` et `5 PRODUIT/`.

  | Fonction | Responsable |
  |---|---|
  | `1 DIRECTION` | Malik Mubashir Hassan, CEO |
  | `2 FINANCE` | Sébastien Ferrié, Director Finance |
  | `3 MARKETING` | Alice Tarnaud, Director Marketing |
  | `4 VENTES` | Steve Fayomi, Head of Product & Sales |
  | `5 PRODUIT` | Steve Fayomi, Head of Product & Sales |
  | `6 OPERATIONS` | Isaac Kalala Mukendi, Director Operations |
  | `7 JURIDIQUE RH` (archiviste) | Tiffany Rongvaux, Director Legal Affairs |

- Seul le responsable de `1 DIRECTION/` écrit dans le registre des décisions ; seul l'archiviste (`7 JURIDIQUE RH/`) range les pièces et attribue les identifiants `S01`, `S02`…
- Récupérer le travail des autres avant de commencer (`git pull`), publier le sien aussitôt après, en petits commits (`git commit`, `git push`).
- Un message de commit dit ce qui a changé et pourquoi.
- Les noms de fichiers créés commencent par la date : `AAAA MMJJ Nom` (ex. `2026 1026 Note de décision.md`).
