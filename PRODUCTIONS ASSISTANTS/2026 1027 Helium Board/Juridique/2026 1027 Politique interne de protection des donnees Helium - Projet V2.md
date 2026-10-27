# Politique interne de protection des données — Helium

**Version :** projet 2.0  
**Date :** 27 octobre 2026  
**Statut :** production d’assistant à la demande de l’utilisateur ; projet pédagogique à valider avant mise en application. Ce dépôt ne vaut pas adoption par la direction. Les coordonnées en .example sont fictives. Les durées et règles opérationnelles sont des propositions, non des caractéristiques vérifiées du produit.

> **Note V2 (27 octobre 2026).** Version corrigée par l'assistant IA Direction après revue juridique (voir `2026 1027 Revue juridique des cinq projets.docx`). Le nom « Helium » remplace « Super Majordome IA » sous réserve de la recherche d'antériorité (décision D-02). Les coordonnées restent fictives. Ce texte n'entre dans `7 JURIDIQUE RH/` que par décision de Tiffany et reste un projet non signé.

## Journal des modifications V2 — hors texte

| Section | Modification | Base |
|---|---|---|
| 3 | Registre des traitements obligatoire | RGPD art. 30 |
| 5 | Formation à la maîtrise de l’IA, avec trace | Règlement (UE) 2024/1689 art. 4 |
| 6 | Clauses minimales exigées des fournisseurs d’IA | RGPD art. 28 §3 |
| 9 | Délai de 72 heures, registre des violations | RGPD art. 33, 34 |
| 11 (nouveau) | Sécurité des accès aux comptes connectés des clients | RGPD art. 32 ; conditions des API Google |

**Diffusion interne — applicable après validation de la direction**

## 1. Objet et périmètre

Cette politique s’applique au fondateur, aux collaborateurs, aux intervenants externes autorisés et aux systèmes traitant des données pour le service.

Elle couvre les données clients, prospects, membres des foyers, tiers concernés et personnels.

## 2. Responsabilités

| Fonction | Responsabilité |
|---|---|
| Direction | Décider des finalités, fournir les moyens et assumer la responsabilité |
| Responsable technique/sécurité | Mettre en œuvre et vérifier les protections |
| Responsable juridique | Encadrer les contrats et les procédures |
| DPO | Conseiller, contrôler, alerter et servir de point de contact |
| Toute personne habilitée | Respecter les règles et signaler les incidents |

Une même personne peut exercer plusieurs fonctions si ses moyens et l’absence de conflit d’intérêts le permettent. Le DPO ne valide pas à la place de la direction les risques qu’elle décide de prendre.

## 3. Validation préalable des traitements

Avant toute nouvelle fonctionnalité ou modification importante, le porteur du projet documente :

- finalité, données, personnes et base juridique ;
- nécessité et solutions moins intrusives ;
- fournisseurs, transferts et conservation ;
- modalités d’information et d’exercice des droits ;
- risques et mesures de sécurité.

Le DPO est consulté en temps utile. Un registre des traitements est tenu dès le premier traitement non occasionnel. Une AIPD est réalisée avant tout traitement réel des données de clients, y compris le pilote. Les recommandations et arbitrages sont conservés.

## 4. Accès et confidentialité

Les accès sont individuels, limités aux missions et revus périodiquement. Les comptes privilégiés sont protégés par une authentification renforcée.

Tout départ ou changement de fonction entraîne une révision immédiate des droits.

L’accès de support à des contenus clients doit être nécessaire, autorisé, limité dans le temps et tracé. La consultation par curiosité est interdite.

## 5. Utilisation des outils d’IA

Il est interdit :

- de transférer des données clients dans un outil personnel ou non approuvé ;
- d’utiliser ces données pour une démonstration publique ;
- d’entraîner un modèle sur les contenus privés sans analyse et autorisation formalisées ;
- de copier des secrets ou jetons d’accès dans une conversation ou un dépôt de code.

Les tests utilisent des données synthétiques par défaut. Toute dérogation est documentée et assortie de mesures adaptées.

Toute personne qui conçoit, paramètre ou opère les agents suit une formation à la maîtrise de l’IA (fonctionnement, limites, risques, obligations) avant son premier accès ; la formation est tracée.

## 6. Fournisseurs et transferts

Aucun fournisseur recevant des données réelles n’est activé sans revue de ses garanties, du contrat, des usages secondaires et des transferts.

Les contrats de sous-traitance doivent notamment encadrer les instructions, la sécurité, les incidents, l’assistance aux droits, les sous-traitants ultérieurs et la restitution ou suppression. Pour les fournisseurs de modèles d’IA, les clauses minimales sont : interdiction d’entraîner sur les données transmises, suppression des données sous trente jours au plus, localisation du traitement, liste des sous-traitants ultérieurs, droit d’audit ou rapport d’audit tiers. [CNIL — article 28](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4)

## 7. Conservation et suppression

Un tableau de conservation approuvé est maintenu. Les délais de la politique publique et les paramètres techniques doivent correspondre.

La suppression couvre les bases actives, index, caches et traitements chez les fournisseurs. Les sauvegardes suivent une rotation documentée ; une restauration ne doit pas réintroduire durablement des données supprimées.

Les archives justifiées par une obligation légale ou un contentieux sont isolées avec accès restreint.

## 8. Exercice des droits

Toute demande est enregistrée et transmise au référent compétent sans délai.

La procédure prévoit l’identification proportionnée, la recherche dans les systèmes et chez les fournisseurs, la protection des droits des tiers et une réponse dans les délais légaux.

Aucune demande n’est écartée au seul motif qu’elle a été envoyée au mauvais service interne.

## 9. Incidents

Tout collaborateur signale immédiatement une perte, divulgation, accès indu ou action suspecte à securite@helium.example — contact à rendre opérationnel.

Le responsable désigné :

1. contient l’incident et préserve les preuves ;
2. évalue les personnes et données affectées ;
3. sollicite le DPO ;
4. documente la décision de notifier ou non ;
5. organise les notifications nécessaires ;
6. suit les mesures correctives.

Toutes les violations sont documentées dans un registre des violations (nature, personnes et données concernées, conséquences probables, mesures). La notification à la CNIL intervient dans les 72 heures suivant la prise de connaissance lorsqu’un risque existe pour les personnes ; les personnes sont informées sans délai en cas de risque élevé. [CNIL — gestion des violations](https://www.cnil.fr/fr/violations-de-donnees-personnelles-les-regles-suivre?trk=article-ssr-frontend-pulse_little-text-block)

## 10. Contrôle et formation

Une sensibilisation précède tout accès aux données. Une revue est organisée au moins annuellement et après tout incident majeur ou changement significatif.

La direction suit notamment les accès non justifiés, demandes hors délai, anomalies de suppression et fournisseurs non évalués. La politique entre en vigueur après validation et communication aux personnes concernées.

## 11. Sécurité des accès aux comptes connectés des clients

Les jetons d’accès aux messageries, agendas et espaces de documents des clients sont chiffrés au repos, limités aux périmètres autorisés, renouvelés selon les règles du fournisseur et révoqués à la résiliation ou à la demande. Aucun jeton n’est accessible en clair à une personne. Tout accès de support à un contenu de client est journalisé et motivé. Les environnements de développement, de test et de production sont séparés ; aucune donnée réelle de client n’est utilisée hors production. Les exigences de vérification des éditeurs d’API (notamment l’évaluation de sécurité annuelle exigée pour les accès restreints aux messageries) sont suivies par le responsable technique.

## Traçabilité et documents liés — hors texte de politique

Export de la rédaction demandée dans la conversation du 27 octobre 2026. Proposition d’assistant, non avis juridique ni décision officielle. Avant application : identifier les fournisseurs, valider les bases juridiques, durées et capacités effectives, nommer les responsables et rendre les contacts opérationnels. La politique de confidentialité ne doit être publiée qu’après ces vérifications.

- [[2026 1027 CGV CGU Helium - Projet]]
- [[2026 1027 Politique de confidentialite - Projet]]
- [[2026 1027 Charte execution des agents IA - Projet]]

[Service Public — information RGPD](https://entreprendre.service-public.gouv.fr/vosdroits/F24270) : l’information doit correspondre aux traitements réellement réalisés.
