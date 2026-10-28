# Références : prix des API de modèles, infrastructure et services, benchmarks d'agents, taux du marché

Dossiers de recherche assemblés les 27 et 28 octobre 2026 par l'assistant IA Direction pour la réponse au cadrage Produit et Technique (demande Finance du 27 octobre). Trois parties, en anglais (langue des sources), chaque chiffre avec son URL, sa date de lecture et une étiquette [official] (page de l'éditeur, texte officiel) ou [secondary] (agrégateur, presse, cabinet) ; « non vérifié » quand la page n'a pas pu être lue. Les « Points non confirmés » de chaque partie sont à relire avant tout devis ou engagement.

Les prix sont ceux affichés le jour de la lecture ; plusieurs éditeurs annoncent des hausses datées (Google : Gemini 4 Argon ×2 au 1er décembre 2026, Gemini 3.8 Flash ×2 au 1er janvier 2027). Taux de change utilisé : 1 € = 1,1403 $ (BCE, taux de référence lu le 28 octobre 2026).

Sommaire : Partie 1, prix des API de modèles et résidence des données · Partie 2, infrastructure, services, vérification Google et plateformes de réservation · Partie 3, benchmarks d'agents et taux du marché français.

---

# Partie 1. Prix des API de modèles et résidence des données

## Helium: LLM API pricing and data-residency brief (October 2026)

Prepared 27-28 October 2026 for a French consumer "AI butler" (reads Gmail/Calendar, plans and executes tasks under human validation). Every number below was read on the provider's own page on the date shown unless tagged [secondary]. Tags: [official] = provider's own pricing or documentation page, or a primary legal text; [secondary] = third party, used only where the official page was unreachable or silent. "non vérifié" = could not be confirmed on any page read. Prices are USD per million tokens (MTok) unless stated; Scaleway is EUR excl. tax. Prices are list prices before any EU surcharge.

---

## 0. Executive summary

- Four price classes exist in October 2026, roughly 1 : 15 : 40 : 100 on input: budget (Haiku 5.5, GPT-6 Luna, Mistral Small 4, Gemini 3.1/3.5 Flash-Lite at $0.10-0.30 in / $0.50-2.50 out), mid (Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon, Mistral Large 4 at $1.36-2.00 in / $4.18-10.00 out), high (Opus 5.5, GPT-5.6 Sol at $4 in / $20 out) and frontier (Fable 5.1, GPT-6 Astra at $10 in / $50 out). Output is consistently 5x input at the US providers.
- All five providers give 50 % off for asynchronous batch and 90 to 97.5 % off on cached input reads. Cache write premiums: Anthropic +25 % (5 min) or +100 % (1 h); OpenAI +25 % (30 min) or +150 % (12 h); Google and Mistral show no write premium (Google bills cache storage per MTok-hour instead); Scaleway lists cached input at 20 % of input on some models.
- EU processing is available from every provider but costs 10 % more at the three US providers (Claude via Bedrock EU inference profile or Vertex `eu` multi-region; OpenAI `eu.api.openai.com`; Vertex regional/multi-region for Claude) and also +10 % at Mistral (`api.eu.mistral.ai`). Scaleway is Paris-hosted at list price with zero retention by default. Anthropic's first-party API has no `eu` inference_geo (only `us` and `global`); EU residency for Claude goes through AWS or Google Cloud.
- Zero data retention is contractual and on request at Anthropic, OpenAI and Mistral; default-on at Scaleway; the Gemini API paid tier keeps prompts "for a limited period" for abuse monitoring with no public ZDR switch and no region option (Vertex AI offers regional endpoints and its own data-governance terms, not read here).
- Announced price increases: Gemini 4 Argon doubles on 1 Dec 2026 ($4 / $20); Gemini 3.8 Flash doubles on 1 Jan 2027 ($1.50 / $7.50); GPT-5.6 Sol's promotional $4 / $20 holds "at least through November 21, 2026".

---

## 1. Anthropic Claude API

Source: https://platform.claude.com/docs/en/about-claude/pricing (redirect from docs.claude.com/en/docs/about-claude/pricing), read 27 Oct 2026 [official]. Cross-checked on https://claude.com/pricing (redirect from anthropic.com/pricing), read 27 Oct 2026 [official]. Caching detail: https://platform.claude.com/docs/en/build-with-claude/prompt-caching, read 27 Oct 2026 [official].

### 1.1 Current lineup and prices (standard tier, USD / MTok)

| Model (API ID) | Input | Output | Cache write 5 min | Cache write 1 h | Cache read | Batch input / output (-50 %) |
|---|---|---|---|---|---|---|
| Claude Fable 5.1 (`claude-fable-5-1`), top tier | 10.00 | 50.00 | 12.50 | 20.00 | 0.25 (0.025x) | 5.00 / 25.00 |
| Claude Opus 5.5 (`claude-opus-5-5`) | 4.00 | 20.00 | 5.00 | 8.00 | 0.20 (0.05x) | 2.00 / 10.00 |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | 2.00 | 10.00 | 2.50 | 4.00 | 0.10 (0.05x) | 1.00 / 5.00 |
| Claude Haiku 5.5 (`claude-haiku-5-5`), prompt ≤ 100K tokens | 0.10 | 0.50 | 0.125 | 0.20 | 0.01 (0.1x) | 0.05 / 0.25 |
| Claude Haiku 5.5, prompt > 100K tokens | 0.50 | 2.50 | 0.625 | 1.00 | 0.05 | 0.25 / 1.25 |
| Legacy: Sonnet 5 | 2.00 | 10.00 | 2.50 | 4.00 | 0.20 | 1.00 / 5.00 |
| Legacy: Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | 5.00 | 25.00 | 6.25 | 10.00 | 0.50 | 2.50 / 12.50 |
| Legacy: Sonnet 4.6 / 4.5 (deprecated) | 3.00 | 15.00 | 3.75 | 6.00 | 0.30 | 1.50 / 7.50 |
| Legacy: Haiku 4.5 | 1.00 | 5.00 | 1.25 | 2.00 | 0.10 | 0.50 / 2.50 |

Notes read on the pages [official]:
- The lineup assumed in the brief (Haiku 5.5, Sonnet 5.5, Opus 5.5) is confirmed; the current top model is Claude Fable 5.1 (Claude Mythos 5.1, limited availability, same price). Model IDs taken from the Bedrock and Vertex ID tables (`anthropic.claude-opus-5-5`, `claude-opus-5-5`), https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock, read 28 Oct 2026 [official].
- Batch API: "50% discount on input and output".
- Long context: for Claude 4.6 and later (except Haiku 5.5) the full 1M-token window is billed at standard rates; Haiku 5.5 is tiered at 100K prompt tokens (all input tokens, cache reads included, count toward the tier).
- Fast mode: Opus 5.5 at 2x ($8 / $40).
- Cache multipliers: 5-minute write 1.25x input; 1-hour write 2x input; read 0.1x input, except Fable 5.1 / Mythos 5.1 (0.025x) and Opus 5.5 / Sonnet 5.5 (0.05x). Minimum cacheable prompt 512 tokens for the 5.5 family. Default TTL 5 minutes, refreshed free on each hit; no manual purge. Cache reads do not count toward ITPM rate limits.
- `inference_geo: "us"` (US-only inference) costs 1.1x on every token category.

### 1.2 Availability in EU regions through AWS and Google Cloud

| Channel | EU availability | Price vs first-party | Source (read 27-28 Oct 2026) |
|---|---|---|---|
| Claude API first-party (`api.anthropic.com`) | `inference_geo` accepts only `"us"` and `"global"`: "Only `"us"` and `"global"` are available." No `"eu"`. Workspace geo (data at rest) is `"us"` only. Response `usage.inference_geo` reports where inference ran. | Global = standard; US-only = 1.1x | https://platform.claude.com/docs/en/build-with-claude/data-residency [official] |
| Claude in Amazon Bedrock (`bedrock-mantle.{region}.api.aws/anthropic/v1/messages`) | `eu-west-3` Europe (Paris): endpoint types "Global, EU" (EU cross-region inference profile). `eu-west-1` Ireland and `eu-north-1` Stockholm: "Global, EU, In-region only". Also Frankfurt, Zurich, Milan, Spain, London (Global, EU). Fable 5.1 regional endpoints "currently available in `us-east-1` only". Haiku 5.5, Sonnet 5.5, Opus 5.5 access criteria set per model by AWS. | "Global: ... No pricing premium. Regional: ... Regional endpoints carry a 10 percent pricing premium over global endpoints." Default quota 2M input TPM, up to 5M input / 500K output TPM without Anthropic approval. Message Batches API not supported. Data handling governed by Amazon Bedrock. | https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock [official] |
| AWS region-compatibility table (Haiku 5.5 row) | eu-west-3, eu-west-1, eu-central-1, eu-north-1: in-region "Not supported"; Geo (cross-region) and Global "Supported". Sonnet 5.5 / Opus 5.5 rows truncated in the page read. | AWS Bedrock price list not read: non vérifié | https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html [official] |
| Claude Models on Google Cloud, Google managed (Vertex AI / Agent Platform) | `global`; multi-region `eu` (`aiplatform.eu.rep.googleapis.com`, "any region in the European Union"); regional (`europe-west1` etc.). "Regional endpoints serve Claude Sonnet 4.6 and earlier models only. For newer models, use a global or multi-region endpoint." 1M context on Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5. | "Multi-region and regional endpoints cost 10 percent more than global endpoints." Message Batches API not supported. Google Cloud governs retention (Vertex data-governance page, not read). | https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed [official] |
| Google Cloud data-residency page | Partner models (Claude, Mistral): EU multi-region, Belgium `europe-west1`, Netherlands `europe-west4`. `europe-west9` (France) listed for Google models only. "Requests submitted to a global endpoint may be processed in any Google Cloud location around the world, and therefore don't provide any data residency guarantees." | | https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency [official] |
| Claude on Google Cloud, Anthropic managed (`claude.googleapis.com`) | Location `global` only; Anthropic-operated, billed via Google Cloud Marketplace; same retention policy and ZDR-on-request as first-party | Same as first-party | https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview [official] |

Conclusion for Helium: Paris (`eu-west-3`) is reachable for Claude 5.5 only through the Bedrock EU cross-region profile (data stays within the EU geography, not pinned to Paris) at +10 % over global; Vertex `europe-west9` does not host Claude, the `eu` multi-region does, at +10 %. Batch pricing (-50 %) is first-party only (Batches API absent on Bedrock and Google-managed Vertex).

### 1.3 Data retention and ZDR on the Claude API

Sources: https://platform.claude.com/docs/en/manage-claude/api-and-data-retention, read 27-28 Oct 2026 [official]; https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data (page dated 1 July 2026), read 28 Oct 2026 [official].

- Default: "we automatically delete inputs and outputs on our backend within 30 days of receipt or generation" (API customers); "Retained data is never used for model training without your express permission."
- ZDR: "Under a ZDR arrangement, Anthropic does not store customer prompts or responses at rest after the API response is returned. To request ZDR for your organization, contact the Anthropic sales team." Enabled per organization. Covers Messages and Token Counting APIs; prompt caching ("Your prompts and Claude's outputs are not stored. KV cache representations and cryptographic hashes are held in memory"); data residency (`inference_geo`); web search and web fetch; PDF inline. Not covered: Message Batches API, Files API, code execution, Managed Agents, Console, CORS from browsers. Covered Models (Fable 5.1, Mythos 5.1, Fable 5, Mythos 5) "require 30-day data retention and are not available under ZDR unless expressly authorized by Anthropic."
- Flagged content or legal holds: "Anthropic may retain inputs and outputs for up to 2 years" regardless of arrangement.
- Claude Platform on AWS and Google Cloud (Anthropic managed): same policy, ZDR on request via account representative. On Amazon Bedrock and Google-managed Vertex the cloud provider is the data processor.

### 1.4 Rate limits and spend caps

Source: https://platform.claude.com/docs/en/api/rate-limits, read 28 Oct 2026 [official].

| Tier | Monthly spend cap | Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (each its own bucket) | Fable 5.x (combined) | Batch queue |
|---|---|---|---|---|
| Evaluation (new orgs) | below Start | "limits below the standard limits ... increase automatically" | | |
| Start | $500 | 1,000 RPM; 2,000,000 ITPM; 400,000 OTPM | 1,000 RPM; 500,000 ITPM; 100,000 OTPM | 1,000 RPM; 200,000 queued |
| Build | $1,000 | 5,000 RPM; 5,000,000 ITPM; 1,000,000 OTPM | 2,000; 1,500,000; 300,000 | 2,000; 300,000 |
| Scale | $200,000 | 10,000 RPM; 10,000,000 ITPM; 2,000,000 OTPM | 4,000; 4,000,000; 800,000 | 4,000; 500,000 |
| Custom | none | via sales | | |

"For most Claude models, only uncached input tokens count toward your ITPM rate limits." Tier advances automatically with usage history; "Request tier increase" on the Console Rate limits page; rate limits shared across `inference_geo` values.

---

## 2. OpenAI API

Source: https://developers.openai.com/api/docs/pricing (redirect from platform.openai.com/docs/pricing; openai.com/api/pricing now shows only ChatGPT Business seats), read 27 Oct 2026 [official]. Caveat: the scraped page shows tier tables in tab order "Standard, Flex/Batch, Fast, Ultrafast" without labels; the Flex/Batch mapping is inferred from tab order and matches the Batch guide's "50% cost discount compared to synchronous APIs" (https://developers.openai.com/api/docs/guides/batch, read 28 Oct 2026 [official]).

### 2.1 Current lineup and prices (USD / MTok)

| Model | Input | Cached input | Output | Cache write 30 min | Cache write 12 h | Flex / Batch input / output (-50 %) | Fast (2x) input / output |
|---|---|---|---|---|---|---|---|
| gpt-6-astra (flagship) | 10.00 | 1.00 (0.1x) | 50.00 | 12.50 | 25.00 | 5.00 / 25.00 | 20.00 / 100.00 |
| gpt-6.1-sol | 2.00 | 0.10 (0.05x) | 10.00 | 2.50 | 5.00 | 1.00 / 5.00 | 4.00 / 20.00 |
| gpt-6.1-terra | 1.00 | 0.05 | 5.00 | 1.25 | 2.50 | 0.50 / 2.50 | 2.00 / 10.00 |
| gpt-6-luna (small) | 0.10 | 0.01 (0.1x) | 0.50 | 0.125 | 0.25 | 0.05 / 0.25 | 0.20 / 1.00 |
| gpt-5.6-sol ("promotional pricing is available at least through November 21, 2026") | 4.00 | 0.40 | 20.00 | 5.00 | 10.00 | non vérifié | non vérifié |
| chat-latest | 5.00 | 0.50 | 30.00 | | | | |
| gpt-5.3-codex | 1.75 | 0.175 | 14.00 | | | | 3.50 / 28.00 |

Also on the page [official]: Ultrafast tier at 6x (Astra $60 / $300); "Priority processing was renamed Fast mode on July 30, 2026"; no separate "mini" / "nano" models (Luna is the lowest tier); fine-tuning "no longer open to new users"; web search tool $10 per 1k calls; file search $2.50 per 1k calls and $0.10/GB/day.

Embeddings (absent from the pricing page; model pages read 28 Oct 2026 [official]): text-embedding-3-small $0.02 / MTok (https://developers.openai.com/api/docs/models/text-embedding-3-small); text-embedding-3-large $0.13 / MTok (https://developers.openai.com/api/docs/models/text-embedding-3-large). Batch price not distinguished on those pages.

### 2.2 EU data residency

Source: https://developers.openai.com/api/docs/guides/your-data, read 27 Oct 2026 [official].

- Region "Europe (EEA + Switzerland)", endpoint `eu.api.openai.com`: storage at rest and regional processing (inference) both in region. "Requires MAM or ZDR" (Modified Abuse Monitoring or Zero Data Retention) and a "Modified Retention amendment"; data residency is a sales-approved project option. Set per project at creation, or per request with the prefixed domain and a Global-project key.
- Price: "Data residency endpoints are charged a 10% uplift" for eligible models released on or after 5 March 2026 (pricing page wording: "Regional processing (data residency) endpoints are charged a 10% uplift"). GPT-6 family is therefore at 1.1x on EU endpoints.
- Batch guide: "GPT-6 Sol and Luna support EU data residency with Standard, Flex, and Batch processing."
- Chat Completions, Responses and Batches are listed with EU storage and processing.

### 2.3 Retention and ZDR

Source: same page [official].

- "data sent to the OpenAI API is not used to train or improve OpenAI models" (opt-in exception).
- Abuse-monitoring logs "retained for up to 30 days" by default. Responses API state at least 30 days or while `store=true`; Conversations, Files, Vector Stores, Batches "Until deleted".
- ZDR: "subject to prior approval by OpenAI and acceptance of additional requirements"; request via sales. Eligible: Chat Completions, Responses, Decisions, Embeddings, Audio, Moderations, Realtime. Not eligible: Batches, Files, Conversations, Assistants, Vector Stores, Fine-tuning, Evals. Under ZDR `store` is always treated as `false`.

### 2.4 Azure OpenAI (Microsoft Foundry) in France Central / Sweden Central

Source: https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure-region-availability#data-zone-standard, read 28 Oct 2026 via Microsoft Learn [official].

- Data Zone Standard (EU data zone), Europe table: `gpt-6-astra` (2026-09-03), `gpt-6-luna` and `gpt-6-sol` (2026-09-22), `gpt-6.1-sol` (2026-09-29), `gpt-6.1-terra` (2026-10-26), `gpt-5.6-luna/sol/terra`, `text-embedding-3-small/large` marked available in **francecentral** and **swedencentral** (and most other EU regions). Data Zone deployments keep inference inside the EU data zone; Global Standard routes inference worldwide.
- Pricing parity with the OpenAI API: non vérifié (the Azure pricing page could not be fetched in this session; Azure bills per deployment type, Global vs Data Zone vs Regional Standard).
- Retention: abuse monitoring stores prompts/completions "up to 30 days" by default; Modified Abuse Monitoring is available to customers meeting Limited Access criteria via application form (https://learn.microsoft.com/azure/foundry/openai/concepts/abuse-monitoring#modified-abuse-monitoring, read 28 Oct 2026 [official]). Microsoft Q&A answers (read 28 Oct 2026, [secondary], Microsoft-moderated forum) state that human review for EU Data Zone deployments takes place within the EEA and that ZDR requires an EA or MCA agreement rather than pay-as-you-go.

### 2.5 Rate limits and tiers

Source: https://developers.openai.com/api/docs/guides/rate-limits, read 28 Oct 2026 [official].

| Tier | Qualification | Monthly usage limit | Astra / Sol / Terra: RPM, TPM | Luna: RPM, TPM |
|---|---|---|---|---|
| Free | "User must be in an allowed geography" | $100 / month | not listed | not listed |
| Build | $5 in total credit purchases | $500 / month | 5,000; 1,000,000 | 5,000; 2,000,000 |
| Launch | $100 | $5,000 / month | 10,000; 4,000,000 | 10,000; 10,000,000 |
| Grow | $500 | $200,000 / month | 15,000; 40,000,000 | 30,000; 180,000,000 |

"Your organization's usage tier upgrades automatically as its total credit purchases reach each threshold"; manual "Upgrade tier" in Settings > Organization > Limits.

---

## 3. Google Gemini API (AI Studio) and Vertex AI

Source: https://ai.google.dev/gemini-api/docs/pricing, read 27 Oct 2026 [official] (135K-character page read in two passes; the embeddings block was not in the retrieved text).

### 3.1 Current lineup and prices (paid tier, USD / MTok)

| Model (ID) | Input | Output (incl. thinking) | Context caching (cached input) | Cache storage per MTok-hour | Batch input / output (-50 %) | Announced change |
|---|---|---|---|---|---|---|
| Gemini 4 Argon (`gemini-4-argon`), flagship | 2.00 | 10.00 | 0.10 (implicit caching only) | not listed | 1.00 / 5.00 | "$4.00 from Dec 1, 2026" / $20.00; caching 0.20; batch 2.00 / 10.00 |
| Gemini 3.1 Pro Preview (`gemini-3.1-pro-preview`) | 2.00 (≤200K) / 4.00 (>200K) | 12.00 / 18.00 | 0.20 / 0.40 | 4.50 | 1.00 / 6.00 (≤200K) | none |
| Gemini 3.8 Flash (`gemini-3.8-flash`) | 0.75 | 3.75 | 0.075 | 0.50 | 0.375 / 1.875 | 1.50 / 7.50, caching 0.15, storage 1.00 "from Jan 1, 2027" |
| Gemini 3.6 Flash (previous generation) | 0.75 | 3.75 | 0.075 | 0.50 | 0.375 / 1.875 | same as 3.8 Flash from 1 Jan 2027 |
| Gemini 3.5 Flash-Lite (`gemini-3.5-flash-lite`) | 0.30 | 2.50 | 0.03 | 1.00 | 0.15 / 1.25 | none |
| Gemini 3.1 Flash-Lite (`gemini-3.1-flash-lite`) | 0.25 text / 0.50 audio | 1.50 | 0.025 | 1.00 | 0.125 / 0.75 | none |

Also read [official]: Priority tier at 1.8x standard (Argon $3.60 / $18.00); Flex tier tables exist per model (figures not captured); Gemini 2.5 Flash-Lite $0.10 / $0.40 still listed; free tier "Free of charge" on Standard for Flash and Flash-Lite models, "Not available" for Argon and 3.1 Pro; "Batch API (50% cost reduction)".

Embeddings: `gemini-embedding-2` (latest, multimodal, 3072 dims default, flexible 128-3072) and `gemini-embedding-001` (text-only) per https://ai.google.dev/gemini-api/docs/embeddings, read 28 Oct 2026 [official], which says batch runs "at 50% of the default Embedding price" but gives no number. Price not found in the retrieved pricing text: $0.20 / MTok input per https://opencode.ai/data/google/gemini-embedding-2.md, read 28 Oct 2026 [secondary]; the Vertex AI pricing page served (https://cloud.google.com/vertex-ai/generative-ai/pricing, read 28 Oct 2026) listed "Gemini Embedding" at $0.00015 per 1K tokens = $0.15 / MTok (batch $0.12) but that snapshot still shows 2.5-generation models, so it is treated as possibly stale. Marked non vérifié.

### 3.2 Data retention and residency

- Gemini API terms (https://ai.google.dev/gemini-api/terms, read 28 Oct 2026 [official]): Paid Services: "Google doesn't use your prompts" or responses to improve products; Google "logs prompts and responses for a limited period of time" solely for Prohibited Use detection and legal needs (no day count); "This data may be stored transiently or cached in any country in which Google or its agents maintain facilities"; no region option. Unpaid Services: content used to improve products, "human reviewers may read, annotate, and process your API input and output"; EEA, Swiss and UK users receive the paid-service data terms even on free usage. Grounding with Google Search / Maps: prompts and outputs stored "for thirty (30) days".
- Pricing-page data-use column: free tier "Yes" (used to improve products), paid tier "No" [official].
- Vertex AI / Agent Platform (https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency, read 28 Oct 2026 [official]): "Data stored at rest in the customer selected location remains at rest in that location"; ML processing stays in the geography for jurisdictional multi-region (`eu`) and within the multi-regional or country jurisdiction for locational endpoints. Google models available in EU multi-region, France (`europe-west9`), Germany (`europe-west3`), Netherlands (`europe-west4`), UK (`europe-west2`). Global endpoint gives no residency guarantee.
- Vertex AI prices for Gemini 4 / 3.8 on EU regional endpoints versus global: non vérifié (the Vertex pricing page served did not list the 3.x/4 models or a regional premium).

### 3.3 Rate limits and tiers

Source: https://ai.google.dev/gemini-api/docs/rate-limits, read 28 Oct 2026 [official].

| Tier | Qualification | Billing tier cap | Spend limit per rolling 10 min |
|---|---|---|---|
| Free | "Active project" or free trial | n/a | n/a |
| Tier 1 | "Set up and link an active billing account" | $250 | $10 |
| Tier 2 | $100 paid + 3 days since first successful payment | $2,000 | $50 |
| Tier 3 | $1,000 paid + 30 days | $20,000 - $100,000+ | $200 |

Per-model RPM/TPM/RPD are shown in AI Studio, not on the page ("Rate limits depend on a variety of factors"; "Specified rate limits are not guaranteed"). Batch enqueued-token quotas (Tier 1 / 2 / 3): 3.8 Flash 3M / 400M / 1B; 3.5 Flash-Lite 10M / 500M / 1B; 4 Argon and 3.1 Pro 5M / 500M / 1B. Priority inference defaults to 0.3x the standard rate limit. Upgrades automatic (Free to Tier 1 "typically take effect instantly"); "Request paid tier rate limit increase" form with "no guarantees".

---

## 4. Mistral AI (La Plateforme)

Sources: https://docs.mistral.ai/models/pricing (target of the redirect from mistral.ai/fr/pricing/api/), read 27 Oct 2026 [official], USD; https://mistral.ai/pricing, read 27 Oct 2026 [official]; https://docs.mistral.ai/getting-started/models/models_overview/, read 27 Oct 2026 [official].

### 4.1 Current models and prices (USD / MTok unless stated)

| Model (version, licence) | Input | Cached input | Output |
|---|---|---|---|
| Mistral Large 4 (v26.10, open) | 1.36 | 0.14 | 4.18 |
| Mistral Large 3 (v25.12, Apache 2.0) | 0.50 | 0.05 | 1.50 |
| Mistral Medium 3.5 (v26.04, modified MIT) | 1.50 | 0.15 | 7.50 |
| Mistral Small 4 (v26.03, Apache 2.0) | 0.15 | 0.015 | 0.60 |
| Ministral 3 14B / 8B / 3B (edge, Apache 2.0) | 0.20 / 0.15 / 0.10 | 0.02 / 0.015 / 0.01 | 0.20 / 0.15 / 0.10 |
| Codestral (v25.08) | 0.30 | 0.03 | 0.90 |
| Z.ai GLM 5.3 Flash / GLM 5.3 (hosted open models) | 0.15 / 1.40 | 0.03 / 0.14 | 0.50 / 4.40 |
| OCR 4.1 / OCR 3 | $4 / $2 per 1,000 pages | 0.40 / 0.20 per 1,000 pages | n/a |
| Mistral Embed (v23.12) / Codestral Embed | 0.10 / 0.15 | 0.01 / 0.015 | n/a |
| Mistral Moderation 2 | free | free | free |
| Voxtral Mini Transcribe 3 / Small Transcribe 3 | $0.0035 / $0.004 per minute | | |

- Discrepancy, both [official]: mistral.ai/pricing quotes "Mistral Large" at $0.5 in / $1.5 out (matches Large 3 on the docs page); the docs list Large 4 at $1.36 / $4.18.
- Magistral and Devstral are no longer current (all in the deprecated table; Devstral 2 and Magistral Medium 1.2 retired 31 Jul 2026, Medium 3 / 3.1 retired 31 Aug 2026, Small 3.2 retired 31 Jul 2026).
- Batch: "Batch processing ... reduces the price by 50%" (mistral.ai/pricing) [official]; the docs page has a Batch tab whose figures were not captured. Prompt caching: "cached input tokens reduce input cost by up to 90%" [official]; the cached-input column equals 10 % of input on every model.
- Model training: "Opt-out" on Pro, Team and Enterprise plans (mistral.ai/pricing).

### 4.2 Hosting, regional inference, ZDR, Mistral Compute

- Regional inference (https://docs.mistral.ai/inference/regional-inference, read 28 Oct 2026 [official]): Global `api.mistral.ai`: "Mistral does not commit to a specific inference location", no upcharge. EU `api.eu.mistral.ai`: processing "across multiple data centers in EU and EFTA countries". US `api.us.mistral.ai`. Regional endpoints "cost 1.1× standard list pricing, a 10% upcharge on input tokens, output tokens, cached reads, and cache writes". "Function calling is the only supported regional tool"; "Agents, Batch, and the Files API are not available on regional endpoints"; available models vary by region (check `models.list` on the regional URL). Account configuration, keys, billing and usage analytics "may still be handled outside the selected geography". GA announced 11 Aug 2026 (https://mistral.ai/news/regional-inference-open-models-new-compute/, read 28 Oct 2026 [official]).
- ZDR (https://docs.mistral.ai/admin/monitor-comply/zero-data-retention, read 28 Oct 2026 [official]): requested through support with a legitimate reason, reviewed case by case; "ZDR is available on paid plans for supported stateless API calls" (chat completions, FIM, embeddings, moderation, classification, OCR, audio). Excluded: Agents, Batch processing files, Conversations, Libraries, `/v1/files`, Vibe Work, Chat, Labs models. Default retention period without ZDR: not stated on that page (non vérifié).
- "Hébergement européen": Mistral is a French company; the EU endpoint runs on "GPU infrastructure managed by Mistral, within the selected geography"; the global endpoint carries no location commitment. Mistral Compute (https://mistral.ai/products/compute, read 28 Oct 2026 [official]): dedicated GPU clusters (NVIDIA GB200 / GB300 / B300), "Sovereign capacity at frontier scale across the EU, by 2027", 200 MW target by 2027, Sweden site with EcoDataCenter "in motion", first external customers March 2026, AES-256 at rest with BYOK, enterprise SLAs, Kubernetes and Slurm; pricing not disclosed; sold via "European Compute Units" with multi-year commitments and a plan for up to 1 GW by 2030 (news page, 11 Aug 2026). The Enterprise plan on mistral.ai/pricing offers private, self-hosted or on-premises deployments where "your data stays in your environment". Priority Tier (committed service levels, custom rate limits, uptime SLA) in public preview since Aug 2026.
- Free API tier (https://help.mistral.ai/en/articles/225174-what-are-the-limits-of-the-free-tier, read 28 Oct 2026 [official]): 1 request / second, 500,000 tokens / minute, 1 billion tokens / month. Paid limits: per-model tokens per minute and requests per second shown in Admin Panel > API > Limits; monthly spend caps per Organization and Workspace; raise via support with target RPS, TPM, monthly tokens and use case (https://docs.mistral.ai/admin/billing-usage/usage-limits, read 28 Oct 2026 [official]).

---

## 5. Scaleway Generative APIs (Paris)

Source: https://www.scaleway.com/en/pricing/model-as-a-service/, read 27 Oct 2026 [official]. EUR per MTok, excl. tax, region Paris.

| Model | Input | Cached input | Output |
|---|---|---|---|
| gpt-oss-120b | 0.15 | | 0.60 |
| mistral-small-3.2-24b-instruct-2506 | 0.15 | | 0.35 |
| mistral-medium-3.5-128b | 1.50 | | 7.50 |
| llama-3.3-70b-instruct | 0.90 | | 0.90 |
| qwen3.6-35b-a3b | 0.25 | | 1.50 |
| qwen3.5-397b-a17b | 0.60 | | 3.60 |
| qwen3-235b-a22b-instruct-2507 | 0.75 | | 2.25 |
| qwen3.8-27b | 0.60 | 0.12 | 3.30 |
| deepseek-v4.1-flash | 0.60 | 0.12 | 1.80 |
| deepseek-v4-flash-0731 | 0.40 | 0.08 | 0.80 |
| glm-5.3 / glm-5.2 | 1.80 | | 5.50 |
| gemma-4-26b-a4b-it | 0.25 | | 0.50 |
| qwen3-embedding-8b; bge-multilingual-gemma2 (embeddings) | 0.10 | | n/a |
| lightonocr-3-0.8b (OCR) | 2.20 (column mapping ambiguous on the page) | | |
| whisper-large-v3 | €0.003 per audio minute | | |

- Free tier: "1 million tokens and 60 minutes of audio transcription"; billing from token 1,000,001. Batches API: -50 %. "All hosted in Europe"; region selector Paris.
- Dedicated deployments (per GPU-hour, Paris): L4-24G €0.93 (≈ €679 / month), L40S-48G €1.72, H100-80G €3.40 (≈ €2,482 / month), H100-SXM-8 €30.06 (≈ €21,944 / month); no rate limits beyond provisioned capacity.
- Data privacy (https://www.scaleway.com/en/docs/generative-apis/reference-content/data-privacy/, read 28 Oct 2026 [official]): "By default we apply a Zero Data Retention Policy"; personal data "may be stored in the following region: Paris, France"; "Your data is not used for training, retraining, or improving the base models"; not subject to "extraterritorial laws such as the American Cloud Act"; GDPR compliant; request content kept only when traffic harms the service (500-error investigations "up to two weeks"); aggregated anonymised usage 6 months; TLS in transit; caching "does not store prompt content itself". HDS / ISO 27001 / SecNumCloud are not mentioned on that page.
- Rate limits (https://www.scaleway.com/en/docs/organizations-and-projects/additional-content/organization-quotas/, Generative APIs section, read 28 Oct 2026 [official]): per Organization, two levels (payment method validated / payment method and identity validated). Tokens per minute (input + output): 200k / 1,000k for gpt-oss-120b, mistral-medium-3.5, qwen3-235b, qwen3-embedding-8b, glm-5.2; 200k / 2,000k for mistral-small-3.2, qwen3.6-35b, qwen3.5-397b, gemma-4; 200k / 400k for llama-3.3-70b, bge. Requests per minute 300 / 600 for every model; 100 concurrent requests. Batches: no rate limit, 20 / 100 concurrent batches, 50,000 requests per file, 200 MB. Rate-limits page (reviewed 24 Apr 2026, read 28 Oct 2026 [official]): raise by identity verification, Batches API, Dedicated Deployment, or a sales volume commitment.

---

## 6. Embeddings and small-task models for memory and retrieval (one per provider)

| Provider | Embedding model | Price / MTok input | Small-task model | Input / output | Source, date, tag |
|---|---|---|---|---|---|
| Anthropic | none (no first-party embeddings API) | n/a | Claude Haiku 5.5 | $0.10 / $0.50 (≤100K prompt); cache read $0.01 | platform.claude.com pricing, 27 Oct 2026 [official] |
| OpenAI | text-embedding-3-small (3-large $0.13) | $0.02 | gpt-6-luna | $0.10 / $0.50; cached $0.01 | model pages 28 Oct and pricing page 27 Oct 2026 [official] |
| Google | gemini-embedding-2 | $0.20 [secondary] or $0.15 [stale Vertex snapshot]: non vérifié | Gemini 3.1 Flash-Lite (3.5 Flash-Lite $0.30 / $2.50) | $0.25 / $1.50; cached $0.025 | ai.google.dev pricing, 27 Oct 2026 [official] |
| Mistral | Mistral Embed | $0.10 | Mistral Small 4 (Ministral 3 3B $0.10 / $0.10) | $0.15 / $0.60; cached $0.015 | docs.mistral.ai/models/pricing, 27 Oct 2026 [official] |
| Scaleway | qwen3-embedding-8b or bge-multilingual-gemma2 | €0.10 | mistral-small-3.2-24b (gpt-oss-120b €0.15 / €0.60) | €0.15 / €0.35 | scaleway.com pricing, 27 Oct 2026 [official] |

Reading: embedding a user's mailbox once (say 50,000 emails × 400 tokens = 20M tokens) costs $0.40 with text-embedding-3-small, $2 with Mistral Embed or Scaleway (EU-hosted), about $3-4 with Gemini Embedding 2. Retrieval cost is negligible against generation.

---

## 7. Rate limits and tiers for a pilot (10 users, then 100 to 3,000)

Sizing assumption (ours, not sourced): a butler user triggers about 50 model calls a day with a 20K-token context, i.e. roughly 1M input tokens per user per day; peaks of 10 calls a minute per active user. At 10 users that is ≈ 100 RPM and ≈ 2M input tokens a minute uncached (far less with caching); at 3,000 users with 10 % concurrently active, ≈ 3,000 RPM and ≈ 60M TPM uncached.

| Provider | Entry (10 users) | 100 users | 3,000 users | Source, date, tag |
|---|---|---|---|---|
| Anthropic | Evaluation tier (reduced) then Start: $500/month cap; 1,000 RPM; 2M ITPM; 400K OTPM per 5.5 model; cache reads free of ITPM | Build: $1,000 cap; 5,000 RPM; 5M ITPM; 1M OTPM. The $1,000 cap, not the rate limit, is the blocker: request Scale early | Scale: $200,000 cap; 10,000 RPM; 10M ITPM; 2M OTPM; Custom via sales. Bedrock: 2M input TPM default, 5M without Anthropic approval | https://platform.claude.com/docs/en/api/rate-limits, 28 Oct 2026 [official] |
| OpenAI | Build ($5 bought): $500/month; 5,000 RPM; 1M TPM (Sol) / 2M (Luna) | Launch ($100 bought): $5,000/month; 10,000 RPM; 4M / 10M TPM | Grow ($500 bought): $200,000/month; 15,000-30,000 RPM; 40M / 180M TPM | https://developers.openai.com/api/docs/guides/rate-limits, 28 Oct 2026 [official] |
| Google Gemini API | Tier 1 on linking billing: $250 cap; $10 per 10 min | Tier 2 ($100 paid + 3 days): $2,000 cap; $50 per 10 min | Tier 3 ($1,000 + 30 days): $20,000-$100,000+; $200 per 10 min; per-model RPM/TPM only in AI Studio; Vertex AI quotas separate | https://ai.google.dev/gemini-api/docs/rate-limits, 28 Oct 2026 [official] |
| Mistral | Free: 1 RPS, 500K TPM, 1B tokens/month; paid per-model TPM/RPS in Admin Panel | Support ticket with target RPS/TPM | Priority Tier (preview): committed capacity, custom limits, SLA | help.mistral.ai article 225174; docs usage-limits; news 11 Aug 2026, 28 Oct 2026 [official] |
| Scaleway | Payment method validated: 300 RPM; 200K TPM per model; 100 concurrent | Identity validated: 600 RPM; 1M-2M TPM per model (spread load across models, or Batches with no rate limit) | Dedicated Deployment (H100 €3.40/h) or volume commitment via sales | organization-quotas page, 28 Oct 2026 [official] |

Reading: for 10 pilot users every provider's first paid tier suffices when the system and memory context is cached. At 100 users the binding constraints are monthly spend caps (Anthropic Build $1,000, OpenAI Launch $5,000, Gemini Tier 2 $2,000) rather than RPM, so tier increases must be requested before launch. At 3,000 users only Anthropic Scale/Custom, OpenAI Grow, Gemini Tier 3 or Vertex, Mistral Priority Tier and Scaleway dedicated deployments fit, and the $200,000/month caps at Anthropic Scale and OpenAI Grow become the next ceiling.

---

## 8. Prompt caching economics

Worked example: a 20,000-token system + memory context reused across 10 calls within the cache TTL; each call adds 1,000 fresh input tokens and produces 500 output tokens. "No cache" = 10 × (21,000 input + 500 output). "Cached" = 1 cache write (or first-call input at list price where no write premium exists) of 20,000 + 9 cache reads of 20,000 + 10 × 1,000 fresh input + 10 × 500 output. USD, standard tier, our arithmetic on the official prices above.

| Provider, model | Input | Cache write | Cache read | Output | No cache (10 calls) | With cache | Saving |
|---|---|---|---|---|---|---|---|
| Anthropic Sonnet 5.5 (5-min TTL) | 2.00 | 2.50 (1.25x) | 0.10 (0.05x) | 10.00 | $0.470 | $0.138 | 71 % |
| Anthropic Haiku 5.5 (5-min TTL) | 0.10 | 0.125 | 0.01 (0.1x) | 0.50 | $0.0235 | $0.0078 | 67 % |
| Anthropic Opus 5.5 (1-h TTL) | 4.00 | 8.00 (2x) | 0.20 (0.05x) | 20.00 | $0.940 | $0.336 (5-min TTL: $0.276) | 64 % (71 %) |
| OpenAI gpt-6.1-sol (30-min write) | 2.00 | 2.50 (1.25x) | 0.10 (0.05x) | 10.00 | $0.470 | $0.138 | 71 % |
| OpenAI gpt-6-luna (30-min write) | 0.10 | 0.125 | 0.01 (0.1x) | 0.50 | $0.0235 | $0.0078 | 67 % |
| Google Gemini 3.8 Flash (explicit cache) | 0.75 | none; storage $0.50 / MTok-hour (≈ $0.00001 for 20K tokens for 1 h) | 0.075 (0.1x) | 3.75 | $0.176 | $0.055 | 69 % |
| Google Gemini 4 Argon (implicit caching only) | 2.00 | none | 0.10 (0.05x) | 10.00 | $0.470 | $0.128 if all 9 re-reads hit | 73 % |
| Mistral Medium 3.5 | 1.50 | none shown | 0.15 (0.1x) | 7.50 | $0.353 | $0.110 | 69 % |
| Mistral Small 4 | 0.15 | none shown | 0.015 (0.1x) | 0.60 | $0.0345 | $0.0102 | 70 % |
| Scaleway deepseek-v4.1-flash (EUR) | 0.60 | none shown | 0.12 (0.2x) | 1.80 | €0.135 | €0.049 | 64 % |

Arithmetic, Sonnet 5.5: no cache = 10 × 21,000 × 2.00 / 1e6 + 10 × 500 × 10.00 / 1e6 = 0.420 + 0.050 = 0.470. Cached = 20,000 × 2.50 / 1e6 (0.050) + 9 × 20,000 × 0.10 / 1e6 (0.018) + 10 × 1,000 × 2.00 / 1e6 (0.020) + output 0.050 = 0.138. Same structure for the other rows.

Rules read on the pages: Anthropic write 1.25x (5 min) or 2x (1 h), read 0.1x except 0.05x on Opus/Sonnet 5.5 and 0.025x on Fable 5.1, minimum 512 tokens, TTL refreshed free on each hit, reads excluded from ITPM [official]. OpenAI write 1.25x (30 min) or 2.5x (12 h), read 0.1x on Astra and Luna, 0.05x on Sol and Terra [official]. Google: cached input 0.1x (Flash family) or 0.05x (Argon, implicit only), plus storage per MTok-hour [official]. Mistral: cached input 10 % of input, no write price shown [official]. Scaleway: cached input 20 % of input where listed [official]. Practical consequence for Helium: the butler's per-user memory block should sit in a cached prefix refreshed by activity; with Anthropic or OpenAI mid-tier models a 10-call session costs about $0.14 instead of $0.47, and a 5.5-Haiku or Luna routing of triage steps brings it under one cent.

---

## 9. Regulatory context (brief, sourced)

### 9.1 EU AI Act, Article 50 transparency, from 2 August 2026

- Primary text: Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 ("Digital Omnibus on AI"); entry into force 27 July 2026 (https://eur-lex.europa.eu/eli/reg/2026/1744/oj, metadata read 28 Oct 2026 [official]; article text not retrieved).
- What changed and what did not (Goodwin, 3 Aug 2026, https://goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force, read 28 Oct 2026 [secondary]; Baker Botts, 10 Sep 2026, https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live, read 28 Oct 2026 [secondary]; concordant): Article 50 obligations "became enforceable" on 2 August 2026 and "took effect on schedule"; high-risk obligations postponed to 2 December 2027 (Annex III) and 2 August 2028 (Annex I); providers of generative systems already on the market before 2 August 2026 have "until 2 December 2026" to implement machine-readable marking; Commission "Guidelines on transparency obligations for providers and deployers of AI systems" adopted 20 July 2026; voluntary "Code of Practice on Transparency of AI-Generated Content" published by the AI Office on 31 July 2026; fines up to €15 million or 3 % of worldwide turnover (Art. 99(4)).
- Obligations relevant to Helium (as summarised by both firms): (1) providers of systems "that interact directly with people must ensure users are told they are dealing with AI, unless that is obvious from context" (Art. 50(1)); (2) providers of systems generating synthetic text must mark outputs "in a machine-readable, detectable format" (Art. 50(2)); (3) deployers must disclose deepfakes and AI-generated text "published on matters of public interest ... unless the content has undergone human editorial review with a person assuming responsibility for its publication" (Art. 50(4)).
- Application to a consumer agent drafting a user's emails (our reading, flagged as inference): Helium is the provider of its system (it assembles and markets it under its brand) and a deployer of the underlying model; the GPAI-model obligations (Chapter V) fall on Anthropic, OpenAI, Google or Mistral, not on Helium. Art. 50(1) applies: the app must tell the user they interact with an AI (trivially satisfied by the product). Art. 50(2) applies to Helium as provider of a system generating synthetic text: the drafted emails are synthetic text and should carry machine-readable marking (a technical header or metadata), subject to the Guidelines' treatment of assistive editing where the human validates each message. Art. 50(4) targets publication to the public on matters of public interest and carries a human-review exception; a private email validated by the user before sending is not "published" and is reviewed by a person assuming responsibility, so no visible disclosure to the recipient is required by Art. 50(4). Neither source read addresses private correspondence explicitly: non vérifié at the level of the Guidelines text.

### 9.2 EU-US Data Privacy Framework (DPF) status

- General Court, case T-553/23 Latombe v Commission, 3 September 2025: annulment action dismissed, the DPF adequacy decision stands (https://streamlex.eu/resources/dpf-developments-tracker/, read 28 Oct 2026 [secondary]).
- Appeal to the Court of Justice filed 31 October 2025 (OJ C/2025/6610), case C-703/25 (WilmerHale, 1 Dec 2025, https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20251201-european-court-of-justice-to-review-challenge-to-eu-us-data-privacy-framework, read 28 Oct 2026 [secondary]; Next, 30 Jun 2026, https://next.ink/244691/microsoft-vole-au-secours-du-data-privacy-framework-entre-lue-et-les-etats-unis/, read 28 Oct 2026 [secondary]). Microsoft was granted leave to intervene in support of the Commission (Microsoft blog 28 June 2026, per Next). No hearing date, Advocate General opinion or judgment date found as of 28 Oct 2026; "Le pourvoi est toujours en discussion" (Next). The adequacy decision remains in force pending the appeal; the Norwegian DPA (26 Feb 2026) and Danish DPA advise companies to "prepare an exit strategy" since a revocation may come without transition (streamlex tracker [secondary]).
- Consequence for Helium: transfers of user mailbox content to US providers (Anthropic, OpenAI, Google) can rely on the DPF where the provider is certified, but the GDPR-safe design is to avoid relying on it: process in the EU (Bedrock EU profile, Vertex `eu`, OpenAI `eu.api.openai.com`, Mistral EU endpoint, Scaleway Paris) with Standard Contractual Clauses as the fallback transfer tool and a documented switch-over plan. Note that EU processing does not stop the US provider from being the processor: metadata, billing and support may still be handled in the US (explicit at Mistral and OpenAI).

### 9.3 CNIL positions, 2025-2026

- Programme de travail 2026 (CNIL, 7 Apr 2026, https://cnil.fr/fr/accompagnement-des-professionnels-le-programme-de-travail-de-la-cnil-pour-2026, read 28 Oct 2026 [official]): the CNIL "se prépare à être désignée autorité de surveillance de marché" under the AI Act; it will clarify GDPR application to non-anonymous AI models and the respective responsibilities of model designers and deployers; a public consultation is planned on a recommendation on "la sécurisation des échanges de données personnelles" (including email); no item on AI agents as such.
- Note CNIL / Conseil de l'IA et du numérique (CIANum), "IA agentique et protection des données personnelles : équation à inconnues multiples pour les utilisateurs", juillet 2026, published 20 July 2026 (https://www.cnil.fr/sites/default/files/2026-07/ia-cianum-cnil.pdf, read 28 Oct 2026 [official]; commentary Norton Rose Fulbright 18 Aug 2026 [secondary]). Directly relevant to a mailbox-reading butler. Key statements: agentic AI "peut amener les utilisateurs à perdre le contrôle de leurs données personnelles"; where a user grants access to their environment the agent may read everything available "mais certaines de ces informations peuvent ne pas être strictement nécessaires à l'exécution de la tâche demandée" (minimisation and purpose limitation); example cited of an agent that deleted many professional emails and could not easily be stopped; GDPR "reste pleinement applicable". Recommendations: let the user choose which data the system accesses ("Permettre à l'utilisateur de choisir les données auquel le système a accès"); per-agent isolated memory ("chaque agent devrait disposer d'une mémoire dédiée et isolée"), memory expiry and sandboxing; real-time monitoring and filtering of agent actions; human-in-the-loop for critical actions with risk classification and user-chosen approval thresholds; a user-held kill switch ("un bouton d'arrêt d'urgence (kill switch button) à la main de l'utilisateur"); traceability so a user can see, per task, "les données personnelles mobilisées, les agents intervenus"; human review under Art. 22 GDPR must be "réelle, effective" not "purement formelle ou automatique"; independent security and privacy evaluation with published results. The note is non-binding; EDPB and Commission guidance on GDPR/AI Act interplay expected end 2026.
- No CNIL deliberation specific to third-party apps reading consumer mailboxes was found in this session (non vérifié); the general CNIL AI recommendations (2024-2025 fiches, https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-specifiques) remain the applicable baseline.

---

## 10. Price per 1 M tokens, October 2026 (USD unless stated; input / output; list price, global endpoint)

| Tier | Anthropic | OpenAI | Google (Gemini API) | Mistral | Scaleway (EUR, Paris) |
|---|---|---|---|---|---|
| Cheapest capable | Haiku 5.5: 0.10 / 0.50 | gpt-6-luna: 0.10 / 0.50 | Gemini 3.1 Flash-Lite: 0.25 / 1.50 (3.5 Flash-Lite 0.30 / 2.50) | Mistral Small 4: 0.15 / 0.60 | mistral-small-3.2-24b: 0.15 / 0.35 (gpt-oss-120b 0.15 / 0.60) |
| Mid | Sonnet 5.5: 2.00 / 10.00 | gpt-6.1-sol: 2.00 / 10.00 (gpt-6.1-terra 1.00 / 5.00) | Gemini 3.8 Flash: 0.75 / 3.75 (1.50 / 7.50 from 1 Jan 2027) | Mistral Large 4: 1.36 / 4.18 (Medium 3.5 1.50 / 7.50) | deepseek-v4.1-flash: 0.60 / 1.80 (qwen3.5-397b 0.60 / 3.60) |
| Frontier | Fable 5.1: 10.00 / 50.00 (Opus 5.5 4.00 / 20.00) | gpt-6-astra: 10.00 / 50.00 (gpt-5.6-sol 4.00 / 20.00 promo) | Gemini 4 Argon: 2.00 / 10.00 (4.00 / 20.00 from 1 Dec 2026) | none frontier-class; Large 4 is the top | glm-5.3: 1.80 / 5.50 (mistral-medium-3.5 1.50 / 7.50) |
| EU-processing surcharge | +10 % via Bedrock regional/EU or Vertex `eu`; first-party API has no EU option | +10 % on `eu.api.openai.com` (models released after 5 Mar 2026) | Gemini API: no region option; Vertex EU premium non vérifié | +10 % on `api.eu.mistral.ai` | 0 (Paris by default) |
| Batch | -50 % (first-party only) | -50 % (EU residency supported for Sol and Luna) | -50 % | -50 % (not on regional endpoints) | -50 % (no rate limit) |
| Cache read | 0.025x-0.1x; write +25 % / +100 % | 0.05x-0.1x; write +25 % / +150 % | 0.05x-0.1x + storage per MTok-hour | 0.1x | 0.2x where offered |
| ZDR | on request (sales), not for Fable/Mythos, not for Batch/Files | on request (sales), not for Batches/Files | no public ZDR on Gemini API; paid data not used for training | on request (support), paid plans, stateless endpoints | default |

All figures: provider pages read 27-28 Oct 2026 [official]; URLs in sections 1-5.

---

## Points non confirmés

1. Gemini Embedding 2 price per MTok (not in the retrieved pricing text; $0.20 [secondary] vs $0.15 on a Vertex pricing snapshot that still lists 2.5-generation models).
2. Vertex AI prices for Gemini 4 Argon / 3.8 Flash and whether EU regional or multi-region endpoints carry a premium for Gemini models (the Vertex pricing page served was stale).
3. Azure OpenAI price parity with the OpenAI API in France Central / Sweden Central (Azure pricing page not fetchable in this session); Azure ZDR eligibility (EA/MCA only) comes from a Microsoft Q&A answer, not a policy page.
4. Amazon Bedrock list prices for Claude 5.5 models (AWS pricing page not read); Anthropic docs state +10 % for regional versus global endpoints and no premium for global.
5. Sonnet 5.5 and Opus 5.5 rows of the AWS region-compatibility table (truncated; the Haiku 5.5 row shows Paris reachable via cross-region profile only).
6. Mistral default retention period for API inputs/outputs without ZDR (not on the ZDR page); Mistral Batch-tab prices (only the 50 % statement on mistral.ai/pricing).
7. OpenAI embeddings batch price (model pages show a single figure under a "Batch API price" label); OpenAI tier-table mapping (Flex/Batch, Fast, Ultrafast) inferred from tab order; GPT-5.6 Sol batch price and price after 21 Nov 2026.
8. Text of Regulation (EU) 2026/1744 amendments (only the EUR-Lex title and entry-into-force metadata were read; dates come from two concordant law-firm notes) and the Commission transparency Guidelines' treatment of AI-assisted private correspondence.
9. CJEU case C-703/25 procedural calendar (hearing, Advocate General opinion); no official court page was read.
10. Any CNIL deliberation specific to consumer apps reading mailboxes (none found).


---

# Partie 2. Infrastructure, services, vérification Google, plateformes de réservation

## Helium: infrastructure and third-party services brief (prices, constraints, lead times)

Prepared 28 October 2026. All URLs read 28 October 2026 unless stated. Tags: [official] = vendor's own page or public API; [secondary] = press, blog, aggregator. "non vérifié" = could not be confirmed on the vendor's page. Prices are excl. VAT unless stated. Monthly figures derived from hourly rates use 730 h/month and are marked "calc".

Scope: a French consumer web app ("AI butler") that reads Gmail, Google Calendar and Google Drive, sends emails after user validation, books restaurants and service appointments on the user's behalf, and bills a monthly subscription.

---

## 1. Hosting in Europe

### 1.1 Scaleway (Paris, PAR-1), French provider [official]

Sources: https://www.scaleway.com/en/pricing/virtual-instances/ ; https://www.scaleway.com/en/pricing/managed-databases/ ; https://www.scaleway.com/en/pricing/storage/ ; https://www.scaleway.com/en/pricing/network/ ; https://www.scaleway.com/en/pricing/security-and-account/ ; https://www.scaleway.com/en/docs/cockpit/reference-content/cockpit-pricing/ ; https://www.scaleway.com/en/pricing/serverless/ (all read 28/10/2026).

| Component | SKU | Spec | Unit price | EUR/month (calc) |
|---|---|---|---|---|
| App container / small VM | DEV1-S | 2 vCPU, 2 GB | €0.00898/h | 6.55 |
| App VM | PLAY2-NANO | 2 vCPU, 4 GB | €0.02754/h | 20.10 |
| App VM | PLAY2-MICRO | 4 vCPU, 8 GB | €0.05508/h | 40.20 |
| App VM (prod grade) | PRO2-XXS | 2 vCPU, 8 GB | €0.0561/h | 40.95 |
| Managed PostgreSQL | DB-DEV-M | 3 vCPU, 4 GB | €0.0382/h | 27.89 |
| Managed PostgreSQL | DB-DEV-L | 4 vCPU, 8 GB | €0.0756/h | 55.19 |
| Managed PostgreSQL | DB-PRO2-XXS | 2 vCPU, 8 GB | €0.11/h (main node); HA standby node €0.0583/h | 80.30 (single) / 122.86 (HA) |
| PostgreSQL storage | Block 5K | per GB | €0.0993/GB/month | 50 GB = 4.97 |
| PostgreSQL backups | snapshots | per GB | €0.03/GB/month | 100 GB = 3.00 |
| Managed Redis | RED1-MICRO | 2 vCPU, 2 GB | €0.048/h | 35.04 |
| Object Storage | Standard Multi-AZ | per GB | €0.000022/GB/h (≈ €0.01606/GB/month) | 100 GB = 1.61 |
| Object Storage | Standard One Zone | per GB | €0.000011/GB/h (≈ €0.008/GB/month) | 100 GB = 0.80 |
| Egress (Object Storage) | | 75 GB free/month then €0.01/GB | | 200 GB = 1.25 |
| Load Balancer | LB-GP-S | 200 Mbit/s | €0.016/h | 11.68 |
| Public IPv4 | Additional IP | per IP | €0.004/h | 2.92 |
| Secret Manager | | per secret version | €0.04/version/month + €0.03 per 10,000 requests | 20 versions = 0.80 |
| Key Manager | | per key version | €0.06/key version/month + €0.03 per 10,000 ops | 2 keys = 0.12 |
| Logs (Cockpit) | custom logs | per GB ingested | €0.35/GB (7 days retention included; Scaleway-product metrics/logs free) | 10 GB = 3.50 |
| Metrics (Cockpit) | custom metrics | per million samples | €0.15 (0 to 10 bn tier) | small |
| Serverless Containers (alternative to VMs) | | per resource-second | €0.00001/vCPU-s and €0.000002/GB-s, after 200,000 vCPU-s and 400,000 GB-s free per month | 1 vCPU + 1 GB always-on ≈ 24.3 + 4.5 = 28.8 |

Notes: Scaleway publishes hourly prices only for most SKUs; monthly figures are calc. Multi-AZ for Managed Database is "available on Read Replica only, priced once per node type" (pricing page). Object Storage egress free allowance: 75 GB/month. Private Networks free. Public Gateway VPC-GW-S €0.0199/h (≈ €14.53/month) if a NAT gateway is needed instead of per-instance IPs.

Pilot (10 users), Scaleway: 2 × DEV1-S (13.10) + 1 × DEV1-S worker (6.55) + DB-DEV-M (27.89) + 20 GB DB storage (1.99) + 20 GB backups (0.60) + RED1-MICRO (35.04) + 100 GB object storage multi-AZ (1.61) + egress (0.50) + LB-GP-S (11.68) + 3 IPs (8.76) + Secret Manager (0.80) + Cockpit logs 5 GB (1.75) = **about €110/month** (calc). Dropping managed Redis for a Redis container on a DEV1-S brings it to about €82/month.

100 to 1,000 users, Scaleway: 2 × PLAY2-MICRO (80.40) + 1 × PLAY2-NANO worker (20.10) + DB-PRO2-XXS HA (122.86) + 50 GB DB storage (4.97) + 100 GB backups (3.00) + RED1-MICRO (35.04) + 100 GB object storage (1.61) + egress 300 GB (2.25) + LB-GP-S (11.68) + 3 IPs (8.76) + Secret/Key Manager (1.50) + Cockpit logs 20 GB (7.00) + metrics (2.00) = **about €301/month** (calc).

### 1.2 OVHcloud Public Cloud (Gravelines GRA / Strasbourg SBG / Paris region), French provider [official]

Source: https://www.ovhcloud.com/fr/public-cloud/prices/ (EUR HT, read 28/10/2026). Note: the /en/ site shows USD; the /fr/ site shows EUR. Prices are displayed per hour; monthly prices are either calc or, for b3/c3, the 12-month Savings Plan price shown by OVHcloud.

| Component | SKU | Spec | Unit price | EUR/month |
|---|---|---|---|---|
| App VM (shared, Discovery) | d2-4 | 4 GB RAM, 250 GB disk, 250 Mbit/s | €0.0206/h | 11.44 (calc) |
| App VM (shared, Discovery) | d2-8 | 8 GB RAM, 450 GB disk, 500 Mbit/s | €0.0372/h | 20.60 (calc) |
| App VM (General Purpose) | b3-8 | 2 vCore, 8 GB, 500 Mbit/s | €0.0512/h no-commit | 37.38 (calc) / 31.77 (12-month Savings Plan, shown) |
| App VM (General Purpose) | b3-16 | 4 vCore, 16 GB | €0.1023/h | 74.68 (calc) / 63.48 (12-month) |
| Compute optimised | c3-4 | 2 vCore, 4 GB | €0.0457/h | 33.36 (calc) / 28.36 (12-month) |
| Managed PostgreSQL Essential (1 node) | DB1-4 | 2 vCore, 4 GB | €0.0746/h | 54.46 (shown approx) |
| Managed PostgreSQL Essential (1 node) | DB1-7 | 2 vCore, 7 GB | €0.1477/h | 107.82 |
| Managed PostgreSQL Business (2 nodes, HA) | DB1-4 | 2 vCore, 4 GB | €0.0949/h per node (€0.1898/h total) | 138.55 |
| Managed PostgreSQL Business (2 nodes, HA) | DB1-7 | 2 vCore, 7 GB | €0.1899/h per node | 277.25 |
| Managed DB additional storage | | per GB per node | €0.0004/GB/h (Essential), €0.0006/GB/h (Business) | 50 GB Essential = 14.60 |
| Managed Valkey (Redis-compatible) | DB1-4 Essential | | USD 0.0764/h on /en/ page; EUR price non vérifié (page section not rendered) | ≈ 55.8 USD |
| Object Storage Standard multi-zone | | per GiB | ≈ €0.0140/GiB/month (first 50 TiB) | 100 GB = 1.40 |
| Object Storage Standard one-zone | | per GiB | ≈ €0.0071/GiB/month | 100 GB = 0.71 |
| Object Storage egress | | | "Trafic sortant externe : gratuit" | 0 |
| Block Storage Classic | | per GB | €0.000059/GB/h (≈ €0.043/GB/month) | 50 GB = 2.15 |
| Block Storage High Speed | | per GB | €0.000119/GB/h (≈ €0.087/GB/month) | |
| Load Balancer | S | | €0.0083/h | 6.06 |
| Load Balancer | M | | €0.0208/h | 15.18 |
| Instance egress | | included in instance price in European regions (the /en/ page states 1 TB/month per project is included in three regions; per-GB overage price not shown) | | 0 |
| Logs Data Platform, KMS, Secret Manager | | described on the page, no prices rendered | non vérifié | |

Pilot (10 users), OVHcloud: 2 × d2-4 (22.88) + 1 × d2-4 worker (11.44) + PostgreSQL Essential DB1-4 (54.46, backups included per product page) + Redis self-hosted on the worker (0) + 100 GB object storage (1.40) + LB S (6.06) + logs (non vérifié, assume 0 with self-hosted) = **about €96/month** (calc). With Managed Valkey DB1-4 (≈ €52 at a 1 USD ≈ 0.93 EUR assumption, non vérifié) about €148.

100 to 1,000 users, OVHcloud: 2 × b3-8 (74.76 no-commit) + 1 × d2-8 worker (20.60) + PostgreSQL Business DB1-7 HA (277.25) + 50 GB extra DB storage (21.90) + Managed Valkey DB1-4 (≈ 52, non vérifié) + 100 GB object storage (1.40) + Block storage 100 GB (4.30) + LB M (15.18) = **about €467/month** (calc). With PostgreSQL Business DB1-4 instead of DB1-7: about €329.

### 1.3 Hetzner Cloud (Falkenstein FSN1 / Nuremberg NBG1), German provider [official unless tagged]

Sources: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/ (official price list effective 15 June 2026, read 28/10/2026); https://www.hetzner.com/cloud/load-balancer/ ; https://www.hetzner.com/storage/object-storage/ ; https://docs.hetzner.com/cloud/servers/primary-ips/overview ; https://docs.hetzner.com/cloud/billing/faq/ ; https://www.hetzner.com/cloud/ (read 28/10/2026).

Important: Hetzner raised cloud prices on 1 April 2026 and again on 15 June 2026 (CPX and CCX lines up to +175 %). On 28/10/2026 hetzner.com/cloud shows the Cost-Optimized (CX/CAX) line as "Currently not available" (capacity). Secondary sources (bitdoze.com, 20/10/2026) report CX/CAX unorderable since at least 2 September 2026. Budget on CPX (Regular Performance) or CCX (dedicated).

| Component | SKU | Spec | EUR/month (official) | EUR/hour |
|---|---|---|---|---|
| Shared VM, cost-optimised | CX23 | 2 vCPU, 4 GB, 40 GB NVMe | 5.49 (not orderable 28/10/2026) | 0.0088 |
| Shared VM, cost-optimised | CX33 | 4 vCPU, 8 GB, 80 GB | 8.49 (not orderable) | 0.0136 |
| Shared VM, ARM | CAX11 | 2 vCPU, 4 GB, 40 GB | 5.99 (not orderable) | 0.0096 |
| Shared VM, ARM | CAX21 | 4 vCPU, 8 GB, 80 GB | 10.49 (not orderable) | 0.0168 |
| Shared VM, regular performance | CPX22 | 2 vCPU, 4 GB, 80 GB | 19.49 | 0.0312 |
| Shared VM, regular performance | CPX32 | 4 vCPU, 8 GB, 160 GB | 35.49 | 0.0569 |
| Dedicated vCPU | CCX13 | 2 vCPU, 8 GB, 80 GB | 42.99 | 0.0689 |
| Dedicated vCPU | CCX23 | 4 vCPU, 16 GB, 160 GB | 85.99 | 0.1378 |
| Primary IPv4 | | per IP | 0.50 | 0.0008 |
| Load Balancer | LB11 | 5 services, 25 targets, IPv4 included | 7.49 | 0.0120 |
| Load Balancer | LB21 | 15 services, 75 targets | 21.49 | 0.0344 |
| Object Storage | | base fee incl. 1 TB storage and 1 TB egress | 6.49 (€0.0104/h cap) | extra storage €0.0087/TB-hour; extra egress listed as "€1.00 per TB" |
| Backups | | 7 slots | 20 % of server price | |
| Volumes (block storage) | | per GB | non vérifié on 28/10/2026 (interactive page); secondary sources quote about €0.05/GB/month | |
| Traffic overage | | per TB beyond included 20 TB (EU shared plans, secondary) | non vérifié on vendor page; secondary: €1.00 to 1.20/TB | |
| Managed PostgreSQL / Redis | | Hetzner has no managed database or managed Redis: self-host on a VM (e.g. CCX13 + backups) | | |
| KMS / secrets | | none offered: use Vault/Infisical/SOPS self-hosted or a third party | | |
| Logs | | none offered: self-host (Loki/Grafana) or third party | | |

Pilot (10 users), Hetzner (CX line unavailable, CPX used): 2 × CPX22 app (38.98) + 1 × CPX22 worker with Redis container (19.49) + PostgreSQL self-hosted on CPX32 (35.49) + backups 20 % of the four servers (18.79) + 4 IPv4 (2.00) + LB11 (7.49) + Object Storage (6.49) = **about €129/month** (official list prices). If CX23/CX33 become orderable again: 2 × CX23 (10.98) + CX23 (5.49) + CX33 (8.49) + backups (4.99) + 4 IPv4 (2.00) + LB11 (7.49) + Object Storage (6.49) = **about €46/month**.

100 to 1,000 users, Hetzner: 2 × CPX32 (70.98) + 1 × CPX22 worker (19.49) + PostgreSQL primary CCX13 (42.99) + PostgreSQL streaming replica CCX13 (42.99) + backups 20 % (35.29) + Redis on worker (0) + 5 IPv4 (2.50) + LB11 (7.49) + Object Storage (6.49) + 100 GB volume (≈ 5, non vérifié) = **about €233/month**. Operational cost of self-managing PostgreSQL HA, secrets and logs is not priced here.

### 1.4 Clever Cloud (PaaS, French; zones par = Paris, rbx/grahds = OVHcloud Roubaix/Gravelines, scw = Scaleway) [official, machine-readable]

Sources: Clever Cloud public pricing API https://api.clever-cloud.com/v4/billing/price-system?zone_id=par (currency EUR) and https://api.clever-cloud.com/v2/products/addonproviders (read 28/10/2026). The web pricing page https://www.clever.cloud/pricing/ is an interactive estimator and could not be read as text; the API is the source of the figures below. Billing is per second; hourly prices below × 730 h = calc monthly. Load balancing (Sōzu reverse proxies), TLS, deployments, metrics and log console are included in runtime prices (Clever Cloud pricing page statement "All the resources deployed in this way are billed by the second"; no separate LB line item exists in the price system).

| Component | Flavor / plan | Spec | Unit price (EUR) | EUR/month |
|---|---|---|---|---|
| App runtime (Node, Docker, Python...) | pico | 1 vCPU, 256 MiB | 0.00625/h | 4.56 (calc) |
| App runtime | nano | 1 vCPU, 512 MiB | 0.00833/h | 6.08 |
| App runtime | XS | 1 vCPU, 1 GiB | 0.02222/h | 16.22 |
| App runtime | S | 2 vCPU, 2 GiB | 0.04444/h | 32.44 |
| App runtime | M | 4 vCPU, 4 GiB | 0.10556/h | 77.06 |
| App runtime | L | 6 vCPU, 8 GiB | 0.21111/h | 154.11 |
| PostgreSQL add-on | DEV | shared, 256 MB, 5 connections, no backups | 0 | 0 |
| PostgreSQL add-on | XXS Small Space | 1 vCPU, 512 MB, 1 GB, 45 conn | monthly | 5.25 |
| PostgreSQL add-on | XS Small Space | 1 vCPU, 1 GB, 5 GB, 75 conn | monthly | 19.50 |
| PostgreSQL add-on | S Medium Space | 2 vCPU, 2 GB, 15 GB, 125 conn | monthly | 44.00 |
| PostgreSQL add-on | M Medium Space | 4 vCPU, 4 GB, 40 GB, 250 conn | monthly | 98.00 |
| PostgreSQL add-on | L Small Space | 6 vCPU, 8 GB, 40 GB, 500 conn | monthly | 178.00 |
| PostgreSQL add-on | L Medium Space | 6 vCPU, 8 GB, 80 GB | monthly | 198.00 |
| PostgreSQL backups | | daily, 7 days retention, included ("free backup every day", docs page https://www.clever.cloud/developers/doc/deploy/databases/postgresql/) | 0 | 0 |
| Redis add-on | S | 128 MB, 100 conn | monthly | 5.00 |
| Redis add-on | M | 256 MB, 250 conn | monthly | 12.50 |
| Redis add-on | L | 512 MB, 500 conn | monthly | 19.00 |
| Cellar (S3 object storage) | | per GB stored, first 100 MB free | 0.00002844/GB/h (≈ €0.0208/GB/month) up to 1 TB | 100 GB = 2.08 |
| Cellar egress | | per GB out | €0.09/GB up to 10 TB, then €0.07 | 200 GB = 18.00 |
| FS Bucket | | per GB | 0.00229/GB/h (≈ €1.67/GB/month), first 100 MB free | |
| Secrets / KMS | | environment variables encrypted at rest; no separate KMS product | 0 | |
| Logs / metrics | | included (console, Grafana metrics); retention limits not priced | 0 | |

Caveat: whether add-on plan "price" fields are monthly amounts is inferred from the API field semantics and from the public price points known for these plans; the web pricing page could not be read to confirm (marked non vérifié in section 13).

Pilot (10 users), Clever Cloud: 2 × XS app (32.44) + 1 × nano worker (6.08) + PostgreSQL XS Small Space (19.50) + Redis S (5.00) + Cellar 100 GB (2.08) + egress 50 GB (4.50) = **about €70/month** (calc).

100 to 1,000 users, Clever Cloud: 2 × S app (64.88) + 1 × XS worker (16.22) + PostgreSQL L Medium Space 8 GB RAM (198.00) + Redis M (12.50) + Cellar 100 GB (2.08) + egress 300 GB (27.00) = **about €321/month** (calc). With PostgreSQL M Medium Space (4 GB RAM) instead: about €221.

### 1.5 Hosting comparison (EUR/month, calc)

| Provider | Pilot (10 users) | 100 to 1,000 users | Managed PostgreSQL HA? | Managed Redis? | KMS/secrets? | Managed logs? | Legal entity |
|---|---|---|---|---|---|---|---|
| Scaleway (Paris) | ≈ 110 | ≈ 301 | Yes (standby node) | Yes | Yes (Secret + Key Manager) | Yes (Cockpit) | French (Iliad group) |
| OVHcloud (GRA/SBG) | ≈ 96 | ≈ 329 to 467 | Yes (Business plan, 2 nodes) | Valkey (EUR price non vérifié) | KMS and Secret Manager exist, prices non vérifié | Logs Data Platform, price non vérifié | French |
| Hetzner (FSN/NBG) | ≈ 129 (CPX) / ≈ 46 if CX orderable | ≈ 233 (self-managed DB) | No (self-host) | No (self-host) | No | No | German |
| Clever Cloud (par) | ≈ 70 | ≈ 221 to 321 | Add-on, backups daily; HA on request (non vérifié) | Yes | Env vars only | Included | French |

---

## 2. Supabase, Neon, Vercel (the "US PaaS" alternative)

### 2.1 Supabase [official]

Source: https://supabase.com/pricing ; https://supabase.com/docs/guides/platform/regions ; https://supabase.com/legal/dpa (read 28/10/2026). Prices in USD.

| Item | Free | Pro | Team |
|---|---|---|---|
| Price | $0 (2 active projects max) | from $25/month (first project; additional projects from $10/month) | from $599/month |
| Database size included | 500 MB | 8 GB per project | 8 GB |
| MAUs (Auth) included | 50,000 | 100,000 | 100,000 |
| File storage | 1 GB | 100 GB | 100 GB |
| Egress | 5 GB | 250 GB | 250 GB |
| Compute credits | none | $10/month | $10/month |
| Log retention | 1 day | 7 days | 28 days |
| Backups | none | 7 days | 14 days |

Overages (Pro and above): database disk $0.125/GB (General Purpose); MAU $0.00325 per MAU above 100,000; egress $0.09/GB; storage $0.0213/GB. Compute add-ons (monthly): Micro $10 (shared, 1 GB), Small $15 (2 GB), Medium $60 (4 GB), Large $110 (2 dedicated vCPU, 8 GB), XL $210 (4 vCPU, 16 GB); first instance covered by the $10 credit. PITR add-on from $100/month per 7 days retention. Custom domain $10/month. Branching $0.01344 per branch-hour. Log drains $60 per drain/month.

EU regions: Ireland eu-west-1, London eu-west-2, **Paris eu-west-3**, Frankfurt eu-central-1, Zurich eu-central-2, Stockholm eu-north-1 (specific regions). Note from the regions page: the "Europe" general region can include London and Zurich (outside the EU); pick a specific region for residency.

DPA: Supabase DPA "Version 1 — August 1, 2026" at https://supabase.com/legal/dpa, incorporates the EU SCCs (Decision 2021/914) plus UK and Swiss addenda; states that where the customer directs processing in a specific region, Supabase keeps the data stored and primarily processed there (with stated exceptions). The DPA applies by acceptance of the Terms ("acceptance of the Agreement shall have the same effect as signing the SCCs"); no separate signature step described. Supabase contracting entity: Supabase Pte. Ltd. (Singapore). Subprocessor list: https://supabase.com/legal/customer-resources/subprocessor-list.

Supabase estimate for Helium: pilot = Pro $25 (Micro compute covered by credits) ≈ **$25/month**; 500 users = Pro $25 + Large compute 8 GB ($110, less $10 credit) + PITR ($100) ≈ **$225/month**, plus egress above 250 GB.

### 2.2 Neon (serverless Postgres) [official]

Source: https://neon.com/pricing ; https://neon.com/docs/introduction/regions (read 28/10/2026). USD.

| Plan | Monthly minimum | Compute | Storage | Restore window | Branches |
|---|---|---|---|---|---|
| Free | $0 | 100 CU-hours per project included | 1 GB per project, 20 GB account total | 6 hours (1 GB limit) | 10 |
| Launch | none, usage-based | $0.106 per CU-hour | $0.35 per GB-month | up to 7 days; instant restore $0.20 per GB-month | 10 included then $1.50 per branch-month |
| Scale | none, usage-based | $0.222 per CU-hour | $0.35 per GB-month | up to 30 days | 25 included |

1 CU = 1 vCPU + 4 GB RAM. A 2 CU (8 GB) always-on compute on Launch = 2 × 730 × $0.106 ≈ **$155/month** plus storage. A 0.25 CU always-on pilot ≈ $19/month. EU regions: Frankfurt aws-eu-central-1 (all services), London aws-eu-west-2 (Postgres); **Paris not available** (request via support). Azure regions are being deprecated (no new projects).

### 2.3 Vercel [official]

Source: https://vercel.com/pricing ; https://vercel.com/docs/regions (last updated 11/08/2026) (read 28/10/2026). USD.

| Plan | Price | Included | Overage (Pro) |
|---|---|---|---|
| Hobby | $0; "for personal, non-commercial use" (FAQ) | 100 GB fast data transfer, 1 M CDN requests, 4 active CPU hours, 360 GB-h provisioned memory, 1 M function invocations, 5k image transformations per month | none (hard limits) |
| Pro | $20/month per seat ("Developer seat $20/month") with $20 of included usage credit | usage billed against the credit | Fast Origin Transfer 10 GB included then from $0.06/GB; function invocations from $0.60 per 1 M; Fluid Active CPU from $0.128/hour; provisioned memory from $0.0106/GB-h; image transformations $0.05 per 1k; firewall rate-limit requests $0.50 per 1 M |
| Enterprise | custom | | |

Regions: Paris **cdg1** (eu-west-3), Frankfurt fra1, London lhr1, Dublin dub1, Stockholm arn1 among 19 compute regions. Functions default to iad1 (Washington D.C.) unless the region is set per project; Vercel recommends running functions in the database's region. Hobby cannot be used for a commercial product, so Helium starts on Pro ($20/month + usage; with 2 developers $40).

---

## 3. Authentication

Sources: https://clerk.com/pricing ; https://auth0.com/pricing (read 28/10/2026); https://www.budgetforge.dev/tools/auth0-pricing-2026 [secondary, July 2026 rates].

| Provider | Free tier | Paid entry | Cost at 1,000 MAU | Cost at 10,000 MAU | Notes |
|---|---|---|---|---|---|
| Clerk [official] | Hobby: $0, 50,000 monthly retained users (MRU) per app, 3 dashboard seats, SMS codes not included | Pro $25/month ($20 annual), 50,000 MRU included, MFA included | $25 | $25 | MRU overage $0.02 (50,001 to 100,000), $0.018 (100,001 to 1 M). SMS: US/CA $0.01, international "market rate". Business $300/month (SOC2 report, 10 seats). Clerk counts retained users (return after 24 h), not MAU. B2B/Admin add-ons $100/month each. |
| Auth0 [official page shows 500 MAU only] | Free: $0 up to 25,000 MAU, passwordless included, no Pro MFA | Essentials $35/month at 500 MAU; Professional $240/month at 500 MAU | Free plan $0 (within 25,000 MAU) or Essentials ≈ $70 [secondary] | Free plan $0 or Essentials ≈ $700, Professional ≈ $1,600 [secondary, non vérifié on vendor page] | Auth0 pricing page uses a MAU slider; only the 500-MAU price rendered. Auth0 (Okta) hosts EU tenants in the EU region on request. |
| Supabase Auth [official] | 50,000 MAU on Free; 100,000 MAU on Pro ($25) | included in Pro | $0 to $25 | $0 to $25 | Overage $0.00325/MAU above 100,000. Comes with the database if Supabase is chosen. |
| Self-hosted (Keycloak, Authentik, Ory Kratos OSS, Better Auth / Lucia libraries) | $0 licence | $0 licence | infra only: one small VM, e.g. Scaleway DEV1-S €6.55 or Hetzner CPX22 €19.49 | same, plus ops time | Google OAuth is the only identity provider Helium needs at launch (users must connect Google anyway), so a library-level approach (NextAuth/Auth.js, Better Auth) in the app is viable at zero licence cost. |

Recommendation input: at 1,000 and 10,000 MAU, Clerk Pro ($25) or Auth0 Free ($0, 25,000 MAU) are both flat; self-hosting saves nothing material at this scale but keeps data in France.

## 4. Billing

Sources: https://stripe.com/fr/pricing ; https://stripe.com/fr/pricing/local-payment-methods ; https://docs.stripe.com/payments/sepa-debit ; https://www.lemonsqueezy.com/pricing ; https://www.paddle.com/pricing (all read 28/10/2026).

### 4.1 Stripe France [official]

| Item | Fee (EUR, HT) |
|---|---|
| European (EEA) consumer cards, standard | 1.5 % + €0.25 |
| European premium cards (business/commercial) | 2.8 % + €0.25 |
| UK cards | 2.5 % + €0.25 |
| International cards | 3.15 % + €0.25 |
| Currency conversion | + 2 % |
| SEPA Direct Debit (prélèvement SEPA) | €0.35 per successful debit; €3.50 per failed debit; €15.00 per disputed debit; no percentage, no cap stated |
| SEPA constraints (docs) | €10,000 per transaction limit; new accounts €10,000/week limit at first; funds available T+6 business days; "no questions asked" dispute window 8 weeks, unauthorised-debit disputes up to 13 months; disputes are final (no appeal); additional identity verification required to enable SEPA |
| Stripe Billing (subscriptions), pay-as-you-go | 0.7 % of volume processed through Billing |
| Stripe Billing, monthly plan | from €500/month, 1-year commitment |
| Stripe Tax, Basic no-code | 0.5 % per transaction |
| Stripe Tax, Basic API | €0.45 per transaction (10 Calculations calls included, then €0.04 per call) |
| Stripe Tax, Complete | from €80/month, 1-year commitment |
| Radar (fraud) | included in standard pricing; Radar for Fraud Teams from €0.05 per screened transaction |
| Card dispute fee | €20.00 per dispute (refunded if won when contested manually) |
| Payouts | standard payouts free; instant payouts 1 % (min €0.50) |
| Bancontact / iDEAL-Wero / PayPal | 1.4 % + €0.25 / €0.29 / 0.2 % + €0.10 plus PayPal's own fee |

Worked example, Helium Personal €29 TTC/month by EEA card: 1.5 % × 29 + 0.25 = €0.685 + Billing 0.7 % = €0.20 + Tax 0.5 % = €0.145 → **about €1.03 per subscription per month (3.6 % of TTC price)**. By SEPA: €0.35 + €0.20 + €0.145 = **€0.70 (2.4 %)**. For Premium €79: card €1.98 (2.5 %), SEPA €1.30 (1.6 %).

### 4.2 Merchant-of-record alternatives [official]

| Provider | Fee | Includes | Notes |
|---|---|---|---|
| Lemon Squeezy (now part of Stripe; "Sold through Link, LLC f/k/a Lemon Squeezy LLC") | 5 % + $0.50 per transaction | tax collection and remittance, subscriptions, checkout, email marketing (free up to 500 subscribers) | "Transactions outside the US may encounter small additional fees" (amount not stated); payouts twice a month by wire or PayPal; volume pricing on request. Page announces "Lemon Squeezy + Stripe Managed Payments" (2026). |
| Paddle Billing | 5 % + $0.50 per Checkout transaction | global tax compliance and filing, fraud, chargebacks, buyer support, subscription billing | no monthly fee; products under $10 need bespoke pricing; payout and chargeback fees not stated. |

On a €29 subscription, MoR cost ≈ €1.45 + €0.46 ≈ €1.91 (6.6 %) versus ≈ €1.03 with Stripe + Billing + Tax; the MoR removes VAT registration/remittance work (French VAT is still due by Helium's own entity when selling in France; the MoR advantage is mainly for cross-border sales).

## 5. Transactional email, SMS, push

Sources: https://www.brevo.com/pricing.md (USD catalogue) [official]; https://getkanal.com/fr/blog/brevo-prix.md (EUR grid and SMS credits, 24/10/2026) [secondary]; https://resend.com/pricing ; https://www.resend.com/docs/dashboard/domains/regions.md ; https://www.twilio.com/en-us/sms/pricing/fr (all read 28/10/2026).

| Service | Plan | Price | Notes |
|---|---|---|---|
| Brevo (French) email [official USD, EUR secondary] | Free | $0, 300 emails/day | transactional SMTP and API included on all plans |
| Brevo | Starter 5,000 emails/month | $9 (≈ €7 [secondary]) | 10,000: $17 (≈ €14); 20,000: $32 (≈ €28); 50,000: $56 (≈ €47) |
| Brevo | Standard 5,000 / 20,000 | $18 / $69 (≈ €15 / €55) | Professional from $499 (150,000 emails) |
| Brevo | Dedicated IP | ≈ €228/year [secondary]; Enterprise feature on the pricing page | |
| Brevo SMS France | credits | 4.5 credits per SMS, 500 credits = €5.00 → **≈ €0.045 per SMS** [secondary, from Brevo à la carte page]; vendor SMS page could not be fetched | |
| Resend email [official] | Free | $0, 3,000 emails/month, 100/day, 3 domains, 30-day retention | |
| Resend | Pro | $20/month, 50,000 emails, 10 domains | overage $0.90 per 1,000 |
| Resend | Scale | $90/month, 100,000 emails | dedicated IP $30/month (Scale, > 3,000/day) |
| Resend regions | | sending regions us-east-1, **eu-west-1 (Ireland)**, sa-east-1, ap-northeast-1 | region controls sending only; "account data, including logs and email metadata, is stored in the United States regardless of the sending region" (docs). Relevant for GDPR mapping. |
| Twilio SMS France [official, USD] | outbound long code or alphanumeric sender | **$0.0798 per segment** | inbound $0.0075; number rental from $1.15/month; alphanumeric sender free; failed message fee $0.001 |
| Web Push (VAPID) | | free (browser vendors' push services) | |
| iOS PWA push | | free; supported since iOS 16.4 for Home Screen web apps (see section 11) | |

Helium volumes: at 500 users, about 10 notification emails per user per month = 5,000 emails → Brevo Free (300/day cap is a constraint at bursts) or Starter ≈ €7, Resend Pro $20. SMS used only for exceptional alerts: 500 users × 1 SMS ≈ €22 (Brevo) or $40 (Twilio).

## 6. Customer support tooling (2 to 3 seats)

Sources: https://crisp.chat/en/pricing/ ; https://www.intercom.com/pricing ; https://www.plain.com/pricing ; https://www.chatwoot.com/pricing (read 28/10/2026).

| Tool | Plan | Price | 3 seats cost | Notes |
|---|---|---|---|---|
| Crisp (French) [official, USD shown] | Free | $0, 2 agents | n/a (2 seats) | per workspace pricing |
| Crisp | Mini | $45/month, 4 agents | **$45** | |
| Crisp | Essentials | $95/month, 10 agents | $95 | Plus $295/month, 20 agents, extra agent $10 |
| Intercom [official] | Essential | $19/seat/month (new customers, struck-through $29) | **$57** | Advanced $85/seat, Expert $132/seat; Fin AI Agent from $0.99 per outcome; Proactive Support Plus $99/month |
| Plain [official] | Foundation | $45/user/month billed annually (struck $55), up to 5 seats, 1,000 AI credits | **$135** | Horizon $99/user/month (min 3 seats); no free plan, 7-day trial |
| Chatwoot Cloud [official] | Hacker | $0, 2 agents | n/a | Startups $19/agent, Business $39/agent, Enterprise $99/agent |
| Chatwoot self-hosted | community edition | $0 licence | infra only (≈ €7 to 20/month VM) | self-hosted paid tiers on a separate page (non vérifié) |

## 7. Observability for LLM apps

Sources: https://langfuse.com/pricing ; https://langfuse.com/pricing-self-host ; https://langfuse.com/self-hosting/license-key ; https://www.helicone.ai/pricing ; https://docs.sentry.io/pricing ; https://betterstack.com/pricing.md (read 28/10/2026). sentry.io/pricing and docs.sentry.io/organization/data-storage-location could not be fetched (permission blocked); Team/Business subscription prices and EU-region plan eligibility are therefore from secondary sources or marked non vérifié.

| Tool | Plan | Price | Included | EU region | Self-host |
|---|---|---|---|---|---|
| Langfuse Cloud [official] | Hobby | $0 | 50k units/month, 30 days data access | US, **EU**, JP | |
| Langfuse Cloud | Core | $29/month | 100k units, 90 days | EU available | |
| Langfuse Cloud | Pro | $199/month | 100k units, 3 years, data retention management | EU, HIPAA | Teams add-on $300/month |
| Langfuse Cloud | overage | $8 per 100k units | | | |
| Langfuse self-host [official] | OSS | $0, MIT, "all core features without any limits" | | your infra (e.g. Scaleway) | Enterprise licence: custom price; EE features: RBAC, retention policies, audit logs, SCIM |
| Helicone [official] | Hobby | $0 | 10,000 requests, 1 GB, 1 seat | not mentioned | open source, on-prem on Enterprise |
| Helicone | Pro | $79/month | 10,000 requests then usage-based (rate not shown) | | Team $799/month |
| Sentry [official docs] | Developer | $0 | limited (quota not on docs page) | | |
| Sentry | Team / Business | subscription price non vérifié on vendor page this session (secondary sources: Team $26/month, Business $80/month, billed monthly) | 50k errors, 5M spans, 50 replays, 1 GB attachments | EU (Frankfurt) data region exists per Sentry docs; plan eligibility non vérifié | self-host (open source) possible |
| Sentry PAYG | | errors $0.0003625 each (Team, 50k to 100k tier), spans $0.000002, replays $0.00375; Seer $40 per active contributor/month | | | |
| Better Stack Telemetry [official] | Free | 3 GB/month logs, 3 days retention | | **Europe pricing region: ingest $0.10/GB, retention $0.05/GB/month** (US $0.15 and $0.08) | Uptime: 10 monitors included, 50 more $25/month |

Helium pilot: Langfuse Hobby (EU) $0 + Sentry Developer $0 + Better Stack Free $0 = $0. At 500 users (≈ 300k traces/month): Langfuse Core $29 + 2 × $8 overage = $45; Sentry Team ≈ $26 (secondary); Better Stack 20 GB ≈ $3; total ≈ **$75/month**. Self-hosted Langfuse on a Scaleway PLAY2-MICRO (€40) plus Postgres and ClickHouse is the data-in-France alternative.

## 8. Browser automation for sites without API, and booking-platform API access

### 8.1 Hosted browser infrastructure [official docs unless tagged]

Sources: https://docs.browserbase.com/account/billing/plans.md ; https://browser-use.com/pricing.md ; https://docs.steel.dev/overview/pricing ; https://docs.anchorbrowser.io/pricing.md ; https://www.browserbase.com/changelog/stagehand-v4 (read 28/10/2026). The vendors' marketing pricing pages (browserbase.com/pricing, browser-use.com/pricing, steel.dev/pricing, anchorbrowser.io/pricing) could not be fetched (permission blocked); the figures come from their documentation pages.

| Vendor | Free tier | Entry plan | Mid plan | Per browser-hour | Proxy | Session limits |
|---|---|---|---|---|---|---|
| Browserbase | $0: 1 browser-hour, 3 concurrent, 15-min sessions, 7-day retention | Developer $20/month: 100 h, 25 concurrent, 1 GB proxy | Startup $99/month: 500 h, 100 concurrent, 5 GB proxy | overage $0.12/h (Developer), $0.10/h (Startup) | $12/GB (Developer), $10/GB (Startup) | 6 h max session; Scale: contact sales |
| Browser Use Cloud | $1 one-time credit; 10 concurrent | pay as you go, no subscription; top-ups from $5 | concurrency 50 after $100 paid, 250 after $1,000 | **$0.02/browser-hour** (per minute, 1-min minimum) | residential $5/GB; BYO/direct egress $0.20/GB | agent tokens billed per model: default "GPT-5.6 Luna" $0.24 in / $1.44 out per 1M tokens; BU 2.0 model $0.60 in / $3.50 out per 1M; API V2 legacy $0.01 per task + from $0.006 per step |
| Steel | Hobby $0: $10 credits ≈ 100 h, 2 concurrent, 15-min sessions | Starter $29/month ≈ 290 h, 5 concurrent, 30-min sessions | Developer $99/month ≈ 1,238 h, 10 concurrent, 1-h sessions | $0.10/h (Hobby, Starter), $0.08/h (Developer), $0.05/h (Pro $499) | $10/GB Starter, $8/GB Developer, $5/GB Pro | PAYG overage up to 3× plan credits |
| Anchor Browser | $0: $5 credits/month, 5 concurrent, 5 sessions/min | Starter $50/month, 25 concurrent | Growth $2,000/month, 200 concurrent | **$0.05/h** + $0.01 per browser created | Anchor proxy $8/GB; BYO egress $0.20/GB | AI steps $0.01 to $0.10 per step; task runs $0.10 each |
| Stagehand (Browserbase SDK) | open-source SDK (listed under "Open Source" on browserbase.com; licence not stated on the changelog page; MIT per the GitHub repo, non vérifié this session) | $0 licence; runs on Browserbase or a local/remote Chromium | | pays only the browser infra + LLM tokens | | v4 released 10/08/2026 |

Helium sizing: one booking attempt ≈ 3 to 6 minutes of browser time ≈ $0.002 to $0.01 of browser infra (Browser Use/Anchor) plus LLM tokens (typically $0.02 to $0.15 per task). At 500 users × 4 bookings/month = 2,000 tasks ≈ 150 browser-hours → Browserbase Startup $99 or Steel Starter $29 or Browser Use ≈ $3 of browser time + tokens. Residential proxies ($5 to $12/GB) matter because French booking sites block datacenter IPs.

### 8.2 Do the French booking platforms offer APIs to book on behalf of consumers?

| Platform | API status found | Source (read 28/10/2026) | Consequence for Helium |
|---|---|---|---|
| TheFork (LaFourchette) | **B2B/partner API exists** (api.thefork.io/manager/v1, OAuth2 client-credentials via Auth0, endpoints POST /restaurants/{id}/reservations, GET and PATCH /reservations/{id}; docs at docs.thefork.io/B2B-API; terms "LaFourchette-Partners-API-Licence" PDF). Access is by partner licence; no self-serve sign-up found. docs.thefork.io could not be fetched this session. | https://apis.apievangelist.com/store/thefork-reservations-api/ [secondary index of the official docs]; https://unified.to/integrations/thefork.md [secondary] | Partner agreement with TheFork required to create reservations by API; otherwise browser automation of thefork.fr under the consumer's own account (ToS risk, see legal brief). |
| Zenchef | **Restaurant-side API** ("Create new reservations and modify existing reservations", availability, webhooks). Access requires the restaurant to hold a Grow subscription or a special agreement; documentation on request to api-tech-help@zenchef.com; official partnership via zenchef.com/integrations. Rate cap 100 calls/min. Not a consumer-channel API. | https://help.zenchef.com/hc/en-gb/articles/27690768125597-Zenchef-API [official] | Access flows through each restaurant, not through Helium; a booking-channel partnership (or Mozrest below) is the realistic route. |
| Mozrest (aggregator of restaurant booking systems) | Single API to "50+/60+" booking systems (SevenRooms, Zenchef, Eat App, TableOnline, Dineplan, Resfor, CoverManager, Tableo, Quandoo...), "200,000+ restaurants", real-time reservation into the restaurant's software; open to "booking channels" with an established product, via contact form. TheFork not listed. Pricing not published. | https://mozrest.com/fr-fr/solutions-pour-les-canaux-de-reservation [official] | Most credible API path for restaurant bookings outside TheFork; commercial terms non vérifié. |
| Planity | **No public API, no developer portal** (Supergood API report card, October 2026: grade F; integration only via a white-label module switched on by support or the Chift connector for accounting software). | https://supergood.ai/api-report-card/planity [secondary] | Browser automation only, or a bespoke partnership. |
| Treatwell | Partner APIs exist for **salon software** only (Supplier T&Cs define "APIs" for Salon Software; salons may "not use any other third party software to enable Customers to make Bookings"). Third-party integrators such as anny work by e-mail forwarding and ICS calendar feeds, "no direct API connection". No consumer-channel API. | https://www.treatwell.es/en/info/supplier-terms-and-conditions/ [official]; https://docs.anny.co/en/treatwell.md [secondary] | Browser automation only; Treatwell itself exposes salons via Reserve with Google. |
| Doctolib | **Partner API exists but is password-gated** (partner-api.doctolib.com, aimed at health software and institutions; content not readable). Consumer T&Cs (version April 2026) ban web scraping and "moyens automatisés de collecte de données", require credentials to stay secret, allow booking only for oneself or an authorised "Proche", and restrict use to private, non-commercial purposes (art. 8.1). | https://partner-api.doctolib.com/documentation/guide/introduction [official, gated]; https://media.doctolib.com/image/upload/v1776929137/legal/B2C_T_Cs.pdf [official] | Automated booking by a commercial agent on a user's Doctolib account is contractually fragile; exclude medical appointments from the MVP or obtain a partnership. |
| Reserve with Google (Actions Center) | Open to partners with "a direct contractual relationship with all the merchants included in their integration feed" (end-to-end reservations overview); application via Partner interest form then invitation; no fee stated; services with subscriptions/recurring billing not supported; "Guest Checkout" preferred. Designed for booking-software providers that hold the merchant inventory, not for consumer-side agents. | https://developers.google.com/actions-center/verticals/reservations/e2e/overview ; .../policies/platform-policies [official] | Not an access path for Helium to book into third-party inventory; Google does not expose a public "book via RwG" API to consumer apps. |

## 9. Search and web-reading APIs for the agent; Google Places

Sources: https://docs.tavily.com/documentation/api-credits.md ; https://exa.ai/docs/changelog/pricing-update.md ; https://api-dashboard.search.brave.com/documentation/pricing ; https://www.firecrawl.dev/pricing.md ; https://developers.google.com/maps/billing-and-pricing/pricing (read 28/10/2026) [all official]; Jina: https://markaicode.com/pricing/jina-ai-pricing/ [secondary, 01/09/2026] because jina.ai/api-dashboard/pricing disallows fetching.

| API | Free | Price per 1,000 requests (USD) | Notes |
|---|---|---|---|
| Tavily search | 1,000 credits/month | PAYG $8.00 per 1,000 credits ($0.008/credit); plans Project $30 = 4,000 credits ($7.50/1k), Bootstrap $100 = 15,000, Startup $220 = 38,000, Growth $500 = 100,000 ($5/1k) | basic search 1 credit, advanced 2; extract 1 credit per 5 pages; map 1 credit per 10 pages |
| Exa search | not stated on changelog | **$7 per 1,000 searches with contents** (10 results, text + highlights); Lite $4/1k (since 19/10/2026); Deep $12/1k; Deep reasoning $15/1k; extra results $1 per 1,000; contents endpoint $1 per 1,000 pages per content type; summaries $1/1k | pricing update effective 03/03/2026 |
| Brave Search API | $5 credit/month per product (≈ 1,000 requests); free tier removed May 2026 | **Search $5.00 per 1,000** (50 QPS); Answers $4.00 per 1,000 + $5 per 1M input and output tokens (2 QPS); Spellcheck/Autosuggest $5 per 10,000 | prepaid; Enterprise custom with zero data retention |
| Firecrawl | 1,000 credits/month, 2 concurrent | Hobby $19/month = 5,000 credits (≈ $3.80/1k pages); Standard $99 = 100,000 credits ($0.99/1k); Growth $399 = 500,000; extra credits $5 per 1,000 (Hobby) to $5 per 2,500 (Growth) | scrape/crawl 1 credit per page (+4 for JSON); search 2 credits per 10 results |
| Jina Reader (r.jina.ai) | 10 M tokens one-time welcome grant per key [secondary] | $0.05 per 1 M tokens on most models [secondary]; a typical web page ≈ 3,000 to 10,000 tokens → ≈ $0.15 to $0.50 per 1,000 pages | official pricing page not fetchable; rate limits for Reader non vérifié |
| Google Places API (New), Text Search Pro | 5,000 free events/month per SKU | **$32.00** (0 to 100k tier) | Enterprise $35, Enterprise + Atmosphere (reviews, ratings) $40; "IDs Only" Essentials unlimited free |
| Google Places API (New), Place Details | Essentials 10,000 free; Pro 5,000; Enterprise 1,000 | Essentials $5.00; Pro $17.00; Enterprise $20.00; Enterprise + Atmosphere $25.00 | Nearby Search Pro $32; Autocomplete $2.83 per 1,000 requests (10,000 free); Geocoding $5 (10,000 free). The former $200 monthly credit is not mentioned on the current page (replaced by per-SKU free caps in March 2025; page notes further "adjustments to discounts and credits" upcoming). |

Helium sizing at 500 users (≈ 20 agent searches/user/month = 10,000 searches, 3,000 page reads, 2,000 Places text searches + 2,000 details): Brave $50 or Tavily $80 (PAYG) or Exa $70; Firecrawl Hobby $19 or Jina ≈ $1.50; Places: Text Search Pro 2,000 - 5,000 free = $0, Place Details Pro 2,000 - 5,000 free = $0 → **≈ $70 to $100/month**. The pilot stays within free tiers (≈ $0 to $20).

## 10. Google Workspace APIs: quotas, OAuth verification, CASA

### 10.1 Quotas [official]

Sources: https://developers.google.com/workspace/gmail/api/reference/quota ; https://developers.google.com/calendar/quota (read 28/10/2026).

| API | Per project | Per user | Daily | Unit costs |
|---|---|---|---|---|
| Gmail API | 1,200,000 quota units per minute | **6,000 quota units per minute per user** (page now expresses the limit per minute; the former "250 units per user per second" wording is gone) | 80,000,000 units per project per day is a billing threshold: "Usage below it incurs no charges"; cannot be raised | messages.list 5; messages.get 20 (60 with format full/raw/html); messages.send 100; drafts.send 100; history.list 2 |
| Calendar API | 10,000 requests per minute | **600 requests per minute per user** | 1,000,000 requests per project per day billing threshold | "All standard use of the Google Calendar API is available at no additional cost"; the page announces that exceeding quota limits "is planned to incur charges later in 2026"; quota increases via Cloud console, approval not guaranteed, Google advises not to raise the per-user default |
| Drive API | not fetched this session (non vérifié); historically 12,000 queries per minute per project and 12,000 per user | | | |

Helium sizing: polling one user's inbox every 5 minutes with history.list (2 units) + fetching 20 new messages/day (20 × 20 = 400 units) ≈ 1,000 units/user/day; 1,000 users ≈ 1 M units/day, far under the 80 M daily threshold. Prefer Gmail push notifications (users.watch via Cloud Pub/Sub, renew every 7 days) over polling.

### 10.2 OAuth app verification (sensitive and restricted scopes) [official unless tagged]

Sources: https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification ; https://developers.google.com/identity/protocols/oauth2/production-readiness/overview ; https://support.google.com/cloud/answer/15549945 ; https://support.google.com/cloud/answer/13465431 ; https://appdefensealliance.dev/casa/tier-2/tier2-overview (read 28/10/2026). Secondary: https://nango.dev/docs/api-integrations/google-shared/google-security-review.md ; https://deepstrike.io/blog/google-casa-security-assessment-2025 (updated 02/09/2026) ; https://leviathansecurity.com/programs/google-casa-cloud-application-security-assessment ; https://www.switchlabs.dev/post/casa-tier-2-tier-3-security-review-providers-pricing-and-the-cheapest-option ; https://www.nylas.com/blog/google-oauth-app-verification/ (2021, updated 2025).

Scope classification for Helium: gmail.readonly, gmail.send, gmail.modify (and gmail.compose) are **restricted**; calendar and calendar.events are **sensitive**; drive.readonly is **restricted** (Drive full-access scopes are restricted; drive.file, which only covers files the user picks, is non-sensitive). Using drive.file + Google Picker instead of drive.readonly removes one restricted scope.

| Step | Requirement (Google) | Duration | Cost |
|---|---|---|---|
| Testing status | up to 100 test users on the allowlist; test-user authorisations and refresh tokens expire after 7 days (except basic identity scopes) | immediate | 0 |
| Brand verification | app name/logo, domain verified in Google Search Console, public home page, privacy policy hosted on the same domain and linked on the consent screen; "Compliant verification results are valid for 7 days" | "typically takes 2-3 business days" if branding changed; automated review "a few minutes" | 0 |
| Sensitive scope verification (calendar) | scope justification, demo video (YouTube unlisted, English, showing consent screen, client ID in address bar, each scope's feature) | Google: several business days to weeks; community threads report 5 to 12 weeks when stalled (discuss.google.dev, 2026) [secondary] | 0 |
| Restricted scope verification (gmail.*, drive.readonly) | all of the above plus "how you will use the restricted scopes in your app and why more limited scopes aren't sufficient"; application type must be in Google's permitted list (an "AI assistant / productivity" use is permitted; the Gmail User Data Policy forbids using the data for ads, selling it, or human reading except with consent) | "can potentially take several weeks to complete" (Google); Nango reports Trust & Safety approval "often ... in under a week" and 4 to 6 weeks end-to-end | 0 (Google) |
| Security assessment (CASA) | required when the app stores or transmits restricted-scope data on servers or accesses it through a third-party server (Helium does: server-side agent). Run under the App Defense Alliance CASA framework by "an independent, third-party assessor that is approved by Google"; two assurance levels, AL1 (developer-tested, lab-reviewed; the market calls it "Tier 2") and AL2 (lab-tested, "Tier 3"); Google decides the level; Trust & Safety contacts the developer "when it is time to initiate the security assessment"; the old free self-scan is marked **deprecated** on appdefensealliance.dev | AL1: 1 to 3 weeks once scans and SAQ are ready (TAC Security via deepstrike); Nango: 5 to 20 days; Leviathan start within 2 to 30 days depending on package | **Paid by the developer.** AL1/Tier 2 market prices: TAC Security $540 (2 revalidations) to $720 (unlimited) or up to $1,800 (premium) [secondary, Aug 2025]; Netsentries ≈ $700 to $1,500; Leviathan $800 to $1,200 (switchlabs) or $3,000 / $4,500 / $6,000 packages (Leviathan's own page, "AL1", no rush / standard / priority) [official]; Prescient $1,000 to $3,000+; Bishop Fox $1,500+. AL2/Tier 3: $4,500 (TAC) to $8,000+ (Bishop Fox). The older "$15,000 to $75,000" range quoted by Nylas dates from the 2019-2021 regime. |
| Annual renewal | "at least every 12 months after your assessor's Letter of Assessment (LOA) approval date"; Google e-mails about 90 days before expiry; level never goes down | renewal "much easier" absent major changes | same order as initial (TAC bundles include revalidations) |
| Authorized labs | ADA list page redirects to appdefensealliance.org/certification/authorized-labs (not fetchable this session). Named across sources: TAC Security, Leviathan Security, Bishop Fox, DEKRA, NCC Group, NetSentries, Prescient Security, KPMG, Orange Cyberdefense (French), GDS/Aon | | |
| Legal entity | Google's pages do not state that a company is required; verification is attached to a Cloud project owned by any Google account, a verified domain and a privacy policy. Community reports show individual developers passing; a registered business makes the privacy policy, data-deletion commitments and lab contract simpler. Marked **non vérifié as a formal rule**. | | |

Planning input for Helium: budget **$600 to $1,800 per year for CASA Tier 2** plus 4 to 10 weeks of calendar time from submission to restricted-scope approval, and keep the pilot (≤ 100 users) in Testing status with 7-day token expiry, or publish early with an "unverified app" warning (hard cap 100 users for sensitive/restricted scopes until verified).

## 11. Domain, deliverability, Apple, PWA push (notes, nothing to price)

- Domain: a .fr or .com costs about €10 to €15/year (not researched vendor by vendor). Google brand verification needs the domain verified in Search Console and the privacy policy on that same domain.
- Deliverability: publish SPF, DKIM (Brevo and Resend both provide DKIM keys per sending domain) and a DMARC record (start at p=none, move to p=quarantine). Gmail and Yahoo bulk-sender rules require DMARC and one-click unsubscribe for marketing mail; transactional mail sent on the user's behalf goes through the user's own Gmail (gmail.send), so Helium's own domain only carries notifications.
- Sign in with Apple: Apple requires it only for native apps on the App Store that offer third-party social login (App Store Review Guideline 4.8); a web app is not concerned. Not needed for Helium as a web/PWA product.
- PWA push on iOS in 2026: Web Push works for Home Screen web apps since iOS/iPadOS 16.4 (March 2023); the user must add the app to the Home Screen (no install prompt); Declarative Web Push (no service worker) added in iOS/iPadOS 18.4 (March 2025) and Safari 18.5 on macOS [secondary: progressier.com, magicbell.com 20/03/2026]. EU: Apple announced in February 2024 that Home Screen web apps would be removed in the EU under iOS 17.4, then reversed on 1 March 2024 ("continue to offer the existing Home Screen web apps capability in the EU", built on WebKit) [secondary: 9to5mac.com, 01/03/2024]; MagicBell's 2026 matrix still marks EU push as unavailable, which contradicts Apple's reversal: test on a French iPhone before relying on it (non vérifié). Remaining iOS PWA limits: no Background Sync, 7-day cache eviction, 50 MB storage cap.
- Android: PWA push and install prompts work in Chrome; no store listing needed.

## 12. Summary: monthly fixed service costs (excl. VAT, excl. LLM tokens and Stripe per-transaction fees)

Hosting lines are the section 1 and 2 estimates (calc). USD items are left in USD; no exchange rate is assumed. "Lean stack" = French/EU-hosted, self-hosted where sensible; "Alternative stack" = US PaaS/SaaS.

| Line | Lean stack, pilot (10 users) | Lean stack, 500 users | Alternative stack, pilot | Alternative stack, 500 users |
|---|---|---|---|---|
| Hosting, DB, cache, storage, LB, logs | Scaleway ≈ €110 (Clever Cloud ≈ €70) | Scaleway ≈ €300 (Clever Cloud ≈ €220 to €320) | Vercel Pro $20 + Supabase Pro $25 (Micro compute within credits) = $45 | Vercel Pro $20 + ≈ $20 usage + Supabase Pro $25 + Large compute $100 + PITR $100 = $265 |
| Authentication | Auth.js / Better Auth in app, Google OAuth only: €0 | €0 | Clerk Pro $25 | Clerk Pro $25 |
| Billing platform | Stripe: no fixed fee (≈ €1.03 per €29 card subscription, €0.70 by SEPA) | Stripe: no fixed fee (variable ≈ €515/month at 500 × €29) | Stripe, same | Stripe, same (or Paddle/Lemon Squeezy MoR 5 % + $0.50) |
| Email, SMS | Brevo Free €0; SMS ≈ €0.045 each | Brevo Starter ≈ €7 ($9) + ≈ 500 SMS ≈ €22 | Resend Pro $20 | Resend Pro $20 + Twilio SMS 500 × $0.08 = $40 |
| Support | Crisp Free (2 agents) €0 | Crisp Mini $45 | Intercom Essential 2 seats $38 | Intercom Essential 3 seats $57 |
| Observability | Langfuse Hobby EU + Sentry Developer + Better Stack Free = $0 | Langfuse Core $29 + $16 overage + Sentry Team ≈ $26 [secondary] + Better Stack ≈ $3 = $74 (or Langfuse self-hosted on Scaleway ≈ €40) | Langfuse Core $29 + Sentry Team $26 = $55 | $74 |
| Browser automation infra | Browser Use PAYG ≈ $5 (browser time + a little proxy) | Browser Use ≈ 150 h × $0.02 = $3 + 5 GB residential proxy $25 = $28 | Browserbase Developer $20 | Browserbase Startup $99 (500 h, 5 GB proxy) |
| Search, web reading, Places | Brave $5 credit, Places free caps, Jina free grant = $0 | Brave 10k searches $50 + Firecrawl Hobby $19 + Places within free caps $0 = $69 | Tavily Project $30 | Tavily Bootstrap $100 + Firecrawl Hobby $19 = $119 |
| Google OAuth verification (CASA Tier 2, amortised) | not yet needed under 100 test users: $0 (but 7-day token expiry) | $540 to $1,800/year ≈ $45 to $150/month | $0 | $45 to $150 |
| Domain, DNS | ≈ €1 | ≈ €1 | ≈ €1 | ≈ €1 |
| **Total fixed** | **≈ €111 + $5** | **≈ €330 + $310 to $415** | **≈ €1 + $233** | **≈ €1 + $700 to $805** |

Reading: at 500 paying users on the working hypothesis of €29 to €129 per month (≈ €20,000+ MRR), fixed infrastructure and tooling stay under 4 % of revenue in both stacks; the decisive cost lines are LLM tokens (out of scope here), Stripe's ≈ 3.6 % per card subscription, and CASA renewal. The lean stack keeps user mail and calendar data in France (Scaleway Paris or Clever Cloud Paris) and avoids US transfers for the sensitive data set; the alternative stack is faster to build but puts the database in AWS Paris via Supabase (Singapore entity, SCCs) and Vercel functions must be pinned to cdg1.

## Points non confirmés

1. Hetzner Volumes price per GB and traffic overage per TB: the vendor page is interactive and could not be read; secondary sources quote ≈ €0.05/GB/month and €1.00 to 1.20/TB. Hetzner CX/CAX "Currently not available" status read on hetzner.com/cloud on 28/10/2026; may change.
2. OVHcloud EUR prices for Managed Valkey, Logs Data Platform, KMS and Secret Manager: described but not rendered on the /fr/ price page; Valkey USD price ($0.0764/h DB1-4) seen on the /en/ page. OVHcloud instance egress overage per GB not shown.
3. Clever Cloud: all prices come from the public pricing API (zone par, currency EUR); the web estimator could not be read to confirm that add-on "price" fields are monthly; PostgreSQL HA option and price not found.
4. Scaleway: Serverless Containers per-request charge not listed; Managed Database HA semantics ("Multi-AZ on Read Replica only") to be confirmed with Scaleway for a single-region standby.
5. Supabase: whether the DPA requires a separate signature on Pro (page says acceptance of the Terms has the effect of signing the SCCs); Supabase Pte. Ltd. (Singapore) as contracting entity for EU customers to be checked against the French DPO's requirements.
6. Auth0 prices above 500 MAU (slider not rendered): $70 at 1,000 MAU and $700 at 10,000 MAU for Essentials are from budgetforge.dev (July 2026).
7. Brevo EUR grid and SMS France price (≈ €0.045/SMS): from getkanal.com (24/10/2026) because brevo.com/fr pricing pages failed; the USD grid is official.
8. Resend: which plans may select the eu-west-1 sending region not stated; account data stored in the US regardless of region (official docs).
9. Sentry Team ($26/month) and Business ($80/month) subscription prices and EU-region plan eligibility: sentry.io/pricing and the data-storage-location doc were blocked this session; PAYG unit prices are official (docs.sentry.io/pricing).
10. Browserbase, Browser Use, Steel, Anchor: marketing pricing pages blocked; figures come from each vendor's docs pages (official). Stagehand licence (MIT) not confirmed on the page read.
11. TheFork B2B API eligibility and licence terms: docs.thefork.io blocked; endpoint list and OAuth2 details come from a third-party index of the official docs. Mozrest pricing and onboarding conditions not published.
12. Doctolib Partner API: documentation is password-gated; audience and terms unknown.
13. Jina Reader pricing and rate limits: official page disallows fetching; $0.05 per 1 M tokens and 10 M free tokens from markaicode.com (01/09/2026).
14. Google Drive API quotas not fetched this session. Gmail per-user quota now reads 6,000 units/minute (28/10/2026); confirm against the project's Cloud console quotas, as Google is changing Workspace API billing in 2026.
15. CASA: cost paid by the developer is certain; the exact lab prices are secondary (deepstrike 09/2026, switchlabs "as of 2024") except Leviathan's own AL1 packages ($3,000 to $6,000). The ADA authorized-labs page could not be fetched. Whether an individual (no company) can obtain restricted-scope approval is not stated by Google.
16. iOS PWA push in the EU: Apple's 2024 reversal is secondary (9to5mac); one 2026 vendor matrix still marks EU push unavailable. Test on device.
17. Exchange rate: USD figures are not converted; totals mix EUR and USD deliberately.






(Authentication, billing, email/SMS, support, LLM observability, browser automation and booking APIs, search APIs, Google Workspace APIs and OAuth verification, deliverability and PWA notes, summary table.)


---

# Partie 3. Benchmarks d'agents et taux du marché français

## Helium: agent success rates, costs and French MVP rates (research brief)

Prepared 28 October 2026. All URLs read 27 or 28 October 2026 (date given per row). Tags: [official] = primary source (paper, leaderboard data file, vendor announcement or system card, government or statutory text, official FAQ); [secondary] = aggregator, press, consultancy or vendor blog reporting someone else's figures; "non vérifié" = could not be confirmed on a primary source. Each figure carries source, date read and tag. ESTIMATE rows show the calculation. Nothing below is taken from memory without a URL; where only memory was available the row says "non vérifié".

Scope: a consumer "AI butler" (an LLM agent that reads a user's mailbox and calendar, prepares and executes everyday tasks such as booking a restaurant, taking a garage appointment, drafting emails, tracking deadlines, under human validation). Part A: what success rates and costs to expect from LLM agents, late 2026. Part B: French market rates to build the MVP, 2025-2026.

Blocked or unreachable pages during this research (not cited): bpifrance.fr catalogue pages (CloudFront 403 from the research container), artificialanalysis.ai/models/capabilities/agentic, hai.stanford.edu AI Index 2026, urssaf.fr rates page (empty reply), malt.fr tarif pages (JavaScript only). Substitutes are noted in each section.

---

## PART A. Agent success rates and costs (late 2026)

### A1. tau2-bench: tool-calling agent with a simulated user (closest proxy for API-based booking and account actions)

Source: Sierra public submissions bucket that feeds taubench.com, `https://sierra-tau-bench-public.s3.us-west-2.amazonaws.com/submissions/manifest.json` and each `<submission>/submission.json`, read 27 Oct 2026 [official]. Metric: pass^1 = share of tasks solved in one trial; pass^k = probability that all k independent trials succeed (a reliability measure). The `cost` field is defined in `https://github.com/sierra-research/tau2-bench/blob/main/docs/leaderboard-submission.md` (read 27 Oct 2026 [official]) as "average cost per trajectory in USD".

| Model (reasoning effort, user simulator) | Submitted | Retail pass^1 | Airline pass^1 | Telecom pass^1 | Overall | Retail pass^4 | Airline pass^4 | Telecom pass^4 | USD per trajectory retail / airline / telecom |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.5-397B-A17B (thinking, gpt-5.2 sim) | 2026-03-02 | 84.4 | 81.5 | 97.8 | 87.9 (#1 on taubench.com) | not reported | | | not reported |
| Gemini 3.0 Pro (Google self-report) | 2025-11-18 | 85.3 | 73.0 | 98.0 | 85.4 | not reported | | | not reported |
| Claude Opus 4.5 (high, gpt-5.2 sim) | 2026-02-26 | 79.6 | 84.0 | 92.3 | 85.3 | 51.8 | 70.0 | 78.1 | 0.387 / 0.399 / 0.720 |
| GPT-5.2 (high, gpt-5.2 sim) | 2026-02-26 | 81.6 | 83.0 | 89.7 | 84.8 | not reported | | | 0.072 / 0.114 / 0.093 |
| Claude Sonnet 4.5 (Anthropic self-report) | 2025-09-29 | 86.2 | 70.0 | 98.0 | 84.7 | not reported | | | not reported |
| Gemini 3 Flash (high, gpt-5.2 sim) | 2026-03-02 | 76.8 | 82.5 | 91.2 | 83.5 | not reported | | | not reported |
| GPT-5 (gpt-4.1 sim) | 2025-10-02 | 81.6 | 62.5 | 95.8 | 80.0 | not reported | | | 0.106 / 0.134 / 0.165 |
| Claude Sonnet 4.5 (Sierra run, gpt-5.2 sim) | 2026-02-26 | 72.4 | 72.0 | 84.9 | 76.4 | not reported | | | 0.255 / 0.296 / 0.488 |
| GPT-5.2 (no reasoning) | 2026-02-26 | 75.0 | 52.5 | 57.2 | 61.6 | not reported | | | 0.048 / 0.054 / 0.049 |
| GPT-4.1 (2025 baseline) | 2025-06-09 | 74.0 | 56.0 | 34.0 | 54.7 | not reported | | | not reported |

Vendor-reported newer figures: GPT-5.5 scores 98.0 % on tau2-bench Telecom (GPT-5.4: 92.8 %) with GPT-4.1 as user model and original prompts; retail and airline not published. `https://openai.com/index/introducing-gpt-5-5/` (23 Apr 2026), read 28 Oct 2026 [official].

Reading for Helium: the best 2026 models solve 80 to 98 % of scripted customer-service tasks in one trial, but four-trial reliability (pass^4) drops to 52 to 78 % even for a frontier model (Opus 4.5). Cost per task is 0.05 to 0.72 USD depending on model and reasoning effort; telecom (longest, most tool calls) is the most expensive domain; switching reasoning off divides cost by 2 to 8 but costs 25 to 35 points of pass^1 on airline and telecom.

Note: the August 2026 submission batch (Claude Opus 5, GPT-5.6-sol, Grok 4.5, Qwen 3.8 Max, Kimi K3, GLM-5.2, Muse Spark 1.1, Inkling) was run only on the new tau3-Banking knowledge-retrieval domain (best: Qwen 3.8 Max 55.2 %, Claude Opus 5 48.7 %, Grok 4.5 47.9 %, GPT-5.6-sol 46.9 %, GPT-5.5 44.6 %; taubench.com, read 27 Oct 2026 [official]), so the retail/airline/telecom table stops at models released up to March 2026. Secondary aggregators (`https://leaderboard.steel.dev/leaderboards/tau-bench/`, read 27 Oct 2026 [secondary]) list vendor-reported tau2 scores of 88.2 % (Step-3.5-Flash, Jan 2026) and 87.4 % (GLM-4.7, Dec 2025); non vérifié on the Sierra bucket.

### A2. Computer-use and web agents

| Benchmark (what it measures) | Best verified result (date) | Agent / model | Human baseline | Reference points | Source, date read, tag |
|---|---|---|---|---|---|
| OSWorld-Verified (361 real desktop tasks on Ubuntu: Chrome, LibreOffice, Thunderbird email, GIMP, VLC, multi-app) | 90.19 % (2026-07-25), agentic framework, 100 steps, code actions | Intelligence-Indeed Agent | 72.36 % (paper) | OpenAI computer-use-preview (the Operator model) 26 % at 15 steps, 31.4 % at 100 steps (2025-07-28); OpenAI o3 23 % | `https://os-world.github.io/static/data/osworld_verified_results.xlsx` (data file behind os-world.github.io), 27 Oct 2026 [official] |
| OSWorld-Verified, best general-purpose model, screenshot only | 85.96 % (2026-08-01) | claude-fable-5 [1m]; Chrome subset 35.9/46 = 78 %; Thunderbird (email client) 12/15 = 80 % | 72.36 % | claude-opus-5 [1m] 83.39 %; Muse Spark 1.1 (Meta) 80.67 %; MiniMax M3 75.19 %; Qwen 3.7 Plus 73.3 %; claude-sonnet-4-6 72.11 % | same file [official] |
| OSWorld-Verified, best French specialised model | 82.56 % (2026-04-20) | Holo3-35B-A3B (H Company) | 72.36 % | | same file [official] |
| OSWorld 2.0 (harder August 2026 task release) | 77.9 % partial / 41.7 % strict | Claude Fable 5.1 (Fable 5: 72.9 / 36.1; Opus 5: 75.4 / 39.6); Fable 5.1 scored zero wherever safeguards intervened | not stated | not comparable with earlier OSWorld 2.0 numbers (different task files) | `https://www.anthropic.com/claude-fable-and-mythos-5-1` (Sept 2026), 28 Oct 2026 [official] |
| OSWorld-Verified, vendor-reported | 78.7 % | GPT-5.5 (GPT-5.4 75.0; Claude Opus 4.7 78.0) | 72.36 % | | `https://openai.com/index/introducing-gpt-5-5/` (23 Apr 2026), 28 Oct 2026 [official] |
| WebArena (812 tasks on self-hosted sites: shopping, CMS, forum, GitLab, map) | 86.1 % (09/2026, self-reported) | Narada AI Code | 78.24 % (paper) | DeepSeek v3.2 + WebTactix 74.3 % (02/2026); OpAgent 71.6 % (01/2026); IBM CUGA 61.7 % (02/2025); OpenAI Operator 58.1 % (01/2025, system card); gpt-4-0613 14.9 % (2023) | WebArena leaderboard sheet linked from `https://webarena.dev` (Google Sheet 1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ), 28 Oct 2026 [official] |
| Online-Mind2Web (300 tasks on 136 live websites, human-judged) | 97.7 % (2026-08-04) | Hark Handoff (Easy 100 / Medium 95.0 / Hard 100) | not given | Yutori Navigator n1.5 97.3 % (2026-06-28); Enhans ACT-2 on GPT-5.4 92.7 % (2026-08-04); Yutori n1-preview 78.7 % (2025-11-18); Google Gemini 2.5 Computer Use 69.0 % (Easy 77.1 / Medium 71.3 / Hard 55.4, 2025-09-29); OpenAI Operator 61.3 % (83.1 / 58.0 / 43.2, 2025-03-22); Claude Computer Use 3.7 56.3 % (2025-04); Browser Use + gpt-4o 30.0 % | OSU NLP leaderboard CSV `human_Mind2Web-Online - Leaderboard_data.csv` in HF space osunlp/Online_Mind2Web_Leaderboard, 28 Oct 2026 [official] |
| Online-Mind2Web, auto-judged (o4-mini WebJudge) | 95.3 % verified (Hark); 92.3 % ACT-2; 86.7 % Microsoft Webwright on GPT-5.4 (2026-05-04, verified) | | | GPT-5.4 92.8 % and ChatGPT Atlas 70.9 % are self-reported and marked "not verified" by OSU (2026-03-05); Operator 58.3 %; Gemini 2.5 CU 57.3 % | same space, `auto_o4-mini_...csv` [official] |
| WebVoyager (643 tasks on live sites) | 87.0 % | OpenAI CUA (Jan 2025) | not reported | | `https://openai.com/index/computer-using-agent/` (23 Jan 2025), 28 Oct 2026 [official] |
| Mind2Web 2 (120 private long-horizon agentic search tasks, Agent-as-a-Judge) | 30.5 % success (2026-05-17) | QUEST-35B (partial completion 0.548) | 54 % success, 0.79 partial, 83 % pass@3 (18.4 min per task) | OpenAI Deep Research 28 % (partial 0.54, 8.4 min); Tencent Youtu 27 %; Grok DeeperSearch 27 %; TongAgents 25 %; Gemini Deep Research 18 %; Perplexity Deep Research 15 %; OpenAI Operator 10 %; Claude Research 10 %; ChatGPT Search 6 % | `https://osu-nlp-group.github.io/Mind2Web-2/leaderboard_data.json`, 28 Oct 2026 [official] |
| GAIA (466 general assistant questions with tools; public test leaderboard) | 94.0 % average (2026-10-12), Level 3 91.8 % | Shadow Harness V8.01 (multi-model harness) | 92 % (paper; non vérifié here, the paper itself was not re-read) | Ops-Agentic-Search-2.0 93.7 % (2026-09-22); CustomGPT.ai v44 93.4 % (2026-06-03); Co-Sight Pro (ZTE) 93.0 % (2026-05-16); 4,044 submissions, many anonymous | HF dataset `gaia-benchmark/results_public`, `2023/test-00000-of-00001.parquet`, 28 Oct 2026 [official]; benchmark is saturated and gamed, low signal |
| BrowseComp (1,266 hard web-research questions) | 90.1 % | GPT-5.5 Pro (GPT-5.5 84.4; Gemini 3.1 Pro 85.9; Claude Opus 4.7 79.3; GPT-5.4 82.7) | n/a | ChatGPT agent 68.9 % (Jul 2025) | `https://openai.com/index/introducing-gpt-5-5/` (23 Apr 2026) [official]; `https://openai.com/index/introducing-chatgpt-agent/` (17 Jul 2025, page carries OpenAI's own "outdated" banner) [official], both read 28 Oct 2026 |
| Zapier AutomationBench (real workflow-automation tasks, pass rate) | 31.4 % | Claude Fable 5.1 (Opus 5 26.9; GPT-5.6 Sol 19.6; Fable 5 17.1) | n/a | Opus 5 announcement: pass rate about 1.5x next-best model at same cost per task | Anthropic Fable 5.1 page [official]; `https://www.anthropic.com/news/claude-opus-5` (24 Jul 2026), 28 Oct 2026 [official] |
| TheAgentCompany (simulated software company: web, code, chat with coworkers) | 30 % of tasks autonomously | best agent at paper time (v2, 10 Sep 2025) | n/a | | `https://arxiv.org/abs/2412.14161`, 28 Oct 2026 [official]; live leaderboard is JavaScript-only, not read |
| AgentBench | not refreshed; no 2026 primary-source update found | | | | non vérifié |

Google Project Mariner / Gemini agent: the Gemini 2.5 Computer Use announcement (`https://blog.google/technology/google-deepmind/gemini-computer-use-model/`, 7 Oct 2025, read 28 Oct 2026 [official]) states the model leads Online-Mind2Web, WebVoyager and AndroidWorld and gives "70 %+ accuracy at about 225 seconds latency" on the Browserbase harness, but the numeric table is an image; the verified Online-Mind2Web figure (69.0 %, human-judged) comes from the OSU leaderboard above. Google says the model may ask the user to confirm actions such as completing a purchase and that a per-step safety service reviews each proposed action.

### A3. Vendor-published real-world task trials (booking and form-filling style)

OpenAI, Operator launch page `https://openai.com/index/computer-using-agent/` (23 Jan 2025), read 28 Oct 2026 [official]; 10 attempts per task on live sites:

| Live-site task | Successes / 10 |
|---|---|
| Britannica: search and filter information | 10 |
| Todoist: build grocery list | 10 |
| Spotify: build 1990s playlist | 10 |
| Poppi: check a soda deal | 9 |
| tagvenue.com: find concert hall, with detailed hints | 8 |
| html5editor: text formatting | 4 |
| tagvenue.com: same task without hints | 3 |
| Redfin: townhouse search | 3 |

OpenAI's own wording: "Reliability varies for different websites and UIs" and CUA "is not precise at text editing". The ChatGPT agent page (17 Jul 2025) lists booking and appointments as use cases but publishes no pass rate for them; it requires explicit confirmation for purchases and refuses bank transfers. No vendor (OpenAI, Anthropic, Google, Perplexity, Amazon, Apple) was found to publish a production completion rate for restaurant or appointment booking: non vérifié (see Points non confirmés).

### A4. Cost per task and token consumption

| Item | Figure | Source, date read, tag |
|---|---|---|
| tau2-bench cost per trajectory, frontier model with reasoning (Claude Opus 4.5, high) | 0.39 USD retail, 0.40 airline, 0.72 telecom | Sierra bucket, 27 Oct 2026 [official] |
| tau2-bench cost per trajectory, cheaper frontier with reasoning (GPT-5.2 high) | 0.07 / 0.11 / 0.09 USD | same [official] |
| tau2-bench cost per trajectory, mid model (Claude Sonnet 4.5, Sierra run) | 0.26 / 0.30 / 0.49 USD | same [official] |
| tau2-bench cost per trajectory, no reasoning (GPT-5.2 none) | 0.05 USD per task, but pass^1 falls to 52 to 57 % on airline and telecom | same [official] |
| HAL (Holistic Agent Leaderboard, Princeton), total cost of a full benchmark run: TAU-bench Airline | HAL Generalist Agent on Claude 3.7 Sonnet 56.0 %, 42.11 USD; Tool Calling on o4-mini high 56.0 %, 11.36 USD; Opus 4.1 54.0 %, 180.49 USD | `https://hal.cs.princeton.edu/`, 28 Oct 2026 [official]; latest dated entries Sep 2025, "new model additions paused" |
| HAL, Online Mind2Web (300 tasks) | SeeAct on GPT-5 medium 42.3 %, 171.07 USD; Browser-Use on Claude Sonnet 4 40.0 %, 1,577.26 USD | same [official] |
| HAL, GAIA | HAL Generalist on Sonnet 4.5 74.5 %, 178.20 USD; Opus 4.1 high 68.5 %, 562.24 USD | same [official] |
| HAL, AssistantBench | Browser-Use on o3 medium 38.8 %, 15.15 USD; GPT-5 medium 35.2 %, 41.69 USD | same [official] |
| ESTIMATE, HAL cost per task | TAU-bench airline: 42.11 / 50 tasks = 0.84 USD (Claude 3.7), 11.36 / 50 = 0.23 USD (o4-mini); Online Mind2Web: 171.07 / 300 = 0.57 USD (SeeAct GPT-5), 1,577 / 300 = 5.26 USD (Browser-Use Sonnet 4); GAIA: 178.20 / 165 validation tasks = 1.08 USD. Task counts are the public set sizes; HAL subset sizes non vérifié | derived from HAL totals |
| HAL paper headline findings | 21,730 rollouts, about 40,000 USD, 9 models x 9 benchmarks; in 21 of 36 model-scaffold-benchmark combinations, higher reasoning effort gave equal or lower accuracy; token use correlates positively with accuracy on 6 of 9 benchmarks; 8 cases of agents finding gold answers on HuggingFace or arXiv instead of solving the task; "Agents can be 100x more expensive while only being 1 % better" | `https://arxiv.org/abs/2510.11977` (13 Oct 2025, ICLR 2026) and hal.cs.princeton.edu, 28 Oct 2026 [official] |
| Artificial Analysis, cost per Intelligence-Index task (full eval suite, not only agentic) | Claude Sonnet 5: 2.29 USD per task (about 2x Sonnet 4.6, about 15 % above Opus 4.8); Sonnet 5 uses about 40 % more output tokens per task than Sonnet 4.6 and about 3x the agentic turns on GDPval-AA and AA-Briefcase; max vs low effort = about 6x the turns | `https://artificialanalysis.ai/articles/claude-sonnet-5-agentic-cost` (30 Jun 2026), 28 Oct 2026 [secondary, independent benchmarker] |
| API list prices, USD per million tokens, Oct 2026 | Claude Opus 5: 5 in / 25 out (24 Jul 2026); Claude Fable 5.1: 10 / 50, cache read 0.25, "about 25 % savings for typical workloads, up to about 45 % for highly agentic work" vs Fable 5; GPT-5.5: 5 / 30 (Batch and Flex half price); GPT-5.5 Pro: 30 / 180; GPT-5.4: 2.50 / 15; Claude Sonnet 5: 3 / 15 | Anthropic and OpenAI announcement pages above [official]; Sonnet 5 price via Artificial Analysis [secondary] |
| Absolute input/output tokens and step counts per agentic task | Not published as such by any primary source found. Indirect: OSWorld-Verified results above are at 100 steps max; Mind2Web 2 tasks take 2.6 to 13.7 minutes per task for commercial agents vs 18.4 min for humans; HAL logs 2.5 billion tokens for 21,730 rollouts = about 115,000 tokens per rollout on average (ESTIMATE from HAL abstract figures) | HAL paper [official]; Mind2Web 2 leaderboard [official] |

Working assumption for the pilot's variable cost: 0.10 to 0.75 USD per API-style task with a reasoning model, 0.5 to 5 USD per browser-driven task (HAL Online-Mind2Web range), before prompt caching. The Opus 5 and Fable 5.1 pages both stress cost-per-task curves at different effort levels, so effort should be a per-task-type setting, not a global one.

### A5. Failure modes, retries and prompt injection

Reliability and retries

| Finding | Figure | Source, date read, tag |
|---|---|---|
| Repeat-trial reliability collapses faster than single-trial accuracy | Claude Opus 4.5 on tau2: pass^1 79.6 / 84.0 / 92.3 vs pass^4 51.8 / 70.0 / 78.1 (retail / airline / telecom) | Sierra bucket, 27 Oct 2026 [official] |
| Retrying helps on research-type tasks | Mind2Web 2: pass@3 0.40 vs single-run success 0.28 (OpenAI Deep Research); human pass@3 0.83 vs 0.54 | Mind2Web 2 leaderboard, 28 Oct 2026 [official] |
| Automated attacks also gain from retries | GPT-5 single-attempt attack success 4.5 to 4.7 %, success@4 about 30 % | Hofer, Debenedetti, Tramèr, `https://arxiv.org/abs/2606.10525` (9 Jun 2026), 28 Oct 2026 [official] |
| Difficulty gradient on live websites | Online-Mind2Web (human-judged): Gemini 2.5 CU Easy 77.1 / Medium 71.3 / Hard 55.4; Operator 83.1 / 58.0 / 43.2 | OSU leaderboard CSV, 28 Oct 2026 [official] |
| Cross-benchmark synthesis of failure clusters (27 papers, 19 benchmarks, 2023-2026) | Six clusters: tool invocation and parameter errors; planning and constraint-satisfaction failures; long-horizon degradation from context accumulation; multi-agent coordination failures; safety and security failures under adversarial or underspecified conditions; measurement validity. "Failures compound nonlinearly with task length", "strong performance on individual sub-tasks does not reliably translate into end-to-end success", "additional scaffolding does not consistently improve reliability" | `https://arxiv.org/abs/2607.05775` (7 Jul 2026), 28 Oct 2026 [official] |
| More reasoning is not always better | 21 of 36 HAL combinations: equal or lower accuracy at higher reasoning effort | HAL paper [official] |
| Site-dependence of browser agents | Operator trials 3/10 to 10/10 by site; same tagvenue task 8/10 with hints vs 3/10 without | OpenAI CUA page [official] |

Prompt injection (indirect, via content the agent reads: emails, calendar invites, web pages)

| Study or product | Setting | Attack success rate (ASR) and utility | Source, date read, tag |
|---|---|---|---|
| AgentDojo (ETH Zurich) | 97 tasks (email client, e-banking, travel booking, Slack), 629 security test cases | Results page (last row 2025-02-24): claude-3-7-sonnet utility 88.66 %, utility under attack 77.27 %, targeted ASR 7.31 % (important_instructions attack); claude-3-5-sonnet-20241022 79.38 / 72.50 / 1.11 %; gpt-4o-2024-05-13 69.07 / 50.08 / 47.69 %; gemini-2.0-flash 43.30 / 39.75 / 20.83 %. Defenses on gpt-4o: tool_filter ASR 6.84 % (utility 72.16 %), prompt-injection detector 7.95 % (utility drops to 41.24 %), repeat_user_prompt 27.82 %, spotlighting 41.65 % | `https://arxiv.org/abs/2406.13352` and `https://agentdojo.spylab.ai/results/`, 28 Oct 2026 [official]; the site states it is "not a leaderboard" because not all models were attacked with all attacks |
| Automated attacks on AgentDojo (TAP and GCG), 80 task pairs | Workspace suite = email, calendar, cloud drive | GPT-5: 4.5 to 4.7 % ASR per attempt (universal TAP), about 30 % success@4; Claude Sonnet 4.5 and GPT-5-mini: GCG transfer below 2 %; Qwen3-4B (small open model): 44.6 to 45.2 %; Slack suite most vulnerable (about 67 % on Qwen3-4B); Workspace suite: direct-instruction attacks near zero ASR; Figure 2 shows a calendar-lookup injection that makes a small model send an unauthorised email | arXiv 2606.10525 (9 Jun 2026) [official] |
| Claude for Chrome (Anthropic browser agent) | 123 test cases, 29 attack scenarios | ASR 23.6 % without mitigations, 11.2 % with mitigations in autonomous mode; browser-specific challenge set (4 attack types) 35.7 % to 0 %. Example: a malicious email saying emails must be deleted "for security reasons" made the agent delete the user's emails before mitigations. Controls: site-level permissions, confirmation before publishing, purchasing or sharing personal data | `https://claude.com/resources/articles/claude-for-chrome` (25 Aug 2025), 28 Oct 2026 [official] |
| OpenAI, "Understanding prompt injections" | ChatGPT Atlas agent mode | No figures published; prompt injection "remains a frontier, challenging research problem"; thousands of red-teaming hours; recommended user controls: logged-out mode, Watch Mode on sensitive sites (agent pauses when the tab is not active), confirmation before purchases, narrow instructions rather than "review my emails and take whatever action is needed" | `https://openai.com/index/prompt-injections/` (7 Nov 2025), 28 Oct 2026 [official] |
| OpenAI, Atlas hardening (RL-trained automated attacker) | | OpenAI: prompt injection "is unlikely to ever be fully 'solved'"; OpenAI declined to quantify the reduction in successful injections; UK NCSC (Dec 2025): attacks "may never be totally mitigated", reduce impact rather than try to stop them | TechCrunch, 22 Dec 2025, reporting `https://openai.com/index/hardening-atlas-against-prompt-injection/`, 28 Oct 2026 [secondary] |
| Google Gemini 2.5 Computer Use | | Prompt injection and scams named as risks; per-step out-of-model safety service; confirmation for consequential actions | Google blog (7 Oct 2025) [official] |

Incident rates in production: no vendor or regulator publishes an incident rate for consumer email or calendar agents; non vérifié. The only quantified figures are the pre-deployment test rates above (4 to 48 % ASR depending on model and attack, 0 to 11 % with mitigations).

Design consequence for Helium: treat every email, invite and web page as untrusted input; keep a tool allow-list per task type (AgentDojo's tool_filter is the cheapest effective defense in the data: ASR 47.7 % to 6.8 % on gpt-4o with no utility loss); require explicit human validation before any send, book, pay or delete action; and log every action for audit.

### A6. Production metrics from consumer assistants

| Product | Published completion metric | Source and tag |
|---|---|---|
| OpenAI Operator (Jan 2025) | Only the 10-attempt site trials in A3 (3/10 to 10/10) | OpenAI CUA page [official] |
| OpenAI ChatGPT agent / Atlas agent mode | None published; ChatGPT Atlas 70.9 % on Online-Mind2Web is self-reported and unverified | OSU leaderboard [official], OpenAI pages [official] |
| Google Gemini 2.5 Computer Use / Project Mariner | 69.0 % human-judged on Online-Mind2Web; no production rate | OSU leaderboard [official] |
| Anthropic Claude for Chrome | Only safety figures (A5); no completion rate | Anthropic page [official] |
| Perplexity Comet, Amazon "Buy for Me", Google call-to-book, Apple | No completion rate found | non vérifié |

---

## PART B. French market rates for building the MVP (2025-2026)

### B1. Freelance day rates (TJM, € HT per day)

Primary-source difficulty: Malt's live tarif pages are JavaScript-only and its 2026 barometer was not found as a document; the Malt Tech Trends 2025 PDF (2024 data) is the only Malt primary document read, and it gives European averages with the caveat "les données au niveau local sont susceptibles de varier". Île-de-France figures therefore come from Hays (via BDM), Michael Page and Kicklox/RH Solutions.

| Profile | Malt Tech Trends 2025, European averages, 2024 data (junior / intermédiaire / expert 8-15 y / expert plus 15+ y; overall average) | Hays France 2026, Paris, by years of experience 0-3 / 3-5 / 5-8 / 8+ | Other 2025-2026 references | Suggested assumption for Helium, Île-de-France senior (ESTIMATE) |
|---|---|---|---|---|
| Développeur full-stack senior (Python / TypeScript) | Backend developer: 250 / 380 / 500 / 600; average 400 | Full-stack developer: 450 / 515 / 580 / 650 | La Fabrique du Net (8 Jul 2026, citing Malt barometer without per-figure attribution): full-stack about 560, Python about 600, Paris confirmé 550 to 680 (average 620), senior/expert 670 and above [secondary]; freelance-solution.fr (16 Jun 2026): full-stack median about 485, P25-P75 350 to 650 [secondary] | 600 to 700 |
| Ingénieur IA / LLM / ML | AI/ML specialist: 350 / 525 / 670 / 750; average 540 (vs 400 for non-AI tech profiles) | not in BDM extract | Michael Page étude de rémunérations 2027, Île-de-France, ingénieur IA freelance: 600 low to 1,000 high (grid partly locked, unit labelled ambiguously on page) [secondary]; freelance-solution.fr citing Hays/Malt via Jobbers: IA/ML 750 to 1,500 [secondary] | 700 to 950 |
| Product designer UX/UI | not covered | not in BDM extract | Kicklox / RH Solutions Étude Freelance 2025 (Dec 2025): Design UX/UI average 423 [secondary, vendor study]; freelance-solution.fr: UX/UI about 510 (450 to 700), product/identity designer about 520 (450 to 900) [secondary] | 500 to 650 |
| DevSecOps / cloud engineer | Cloud engineer: 410 / 600 / 750 / 800; average 750 | Cloud architect: 580 / 620 / 700 / 780; SecOps: 530 / 600 / 635 / 750; Data engineer 480 / 590 / 660 / 700 | freelance-solution.fr: DevOps/cloud about 600 (500 to 950); cloud architect about 780 beyond 8 years [secondary] | 700 to 800 |
| Pentester / expert cybersécurité | Cybersecurity expert: 400 / 620 / 750 / 830; average 700 (top certifications listed: RGPD, ISO 27001, PenTest) | SecOps row above | Kolonell (French pentest vendor, 1 Oct 2026): auditor day rate 900 to 1,500 € HT (PASSI-qualified 1,200 to 1,500; non-PASSI 900 to 1,200) [secondary, vendor]; freelance-solution.fr citing Hays: 700 to 1,200 [secondary] | 900 to 1,200 (vendor day), 750 to 850 (freelance) |
| Consultant RGPD / DPO | not covered (RGPD is the top-demanded cybersecurity skill) | Project manager row as proxy: 600 / 680 / 730 / 800 | Legiscope (2 Jul 2026): no CNIL or regulatory tariff exists; illustrative 800 €/day [secondary]; donneespersonnelles.fr (updated 3 Oct 2026): illustrative 2,700 € for 3 days = 900 €/day [secondary]; freelance-solution.fr: consultant stratégie median 629 (400 to 1,000) as neighbour [secondary] | 700 to 900 |

Regional and other adjustments (all read 28 Oct 2026): Hays 2026 via BDM, regions vs Paris: cloud about -7 %, cybersecurity -6 %, data and BI -9 %, software development -10 %, project management -5 % [secondary]; Kicklox/RH Solutions 2025: Île-de-France vs province gap only about 5 %, freelances living abroad -25 %, seniors bill 2.4x juniors, junior to avancé +72 % [secondary]; Michael Page 2027 grid: regions -5 % to -20 % vs Île-de-France [secondary]; Malt Tech Trends 2025: data expert day rates +38 % year on year, 40 % of Malt tech freelances are Expert or Expert plus [official, Malt].

Sources: Malt Tech Trends 2025 FR PDF `https://pages.malt.fr/hubfs/NEW%20-%20E-books%20visuals/Malt%20Tech%20Trends%202025/Malt%20Tech%20Trends%202025%20-%20FR.pdf` (pages 36-39 read as images) [official, Malt]; Hays France étude de rémunération 2026 as reported by Blog du Modérateur `https://www.blogdumoderateur.com/freelance-tech-taux-journaliers-moyens-metier-2026/` (29 Jan 2026, panel of more than 2,500 professionals) [secondary]; Michael Page `https://www.michaelpage.fr/grilles-de-salaires/technology/postes-en-freelance-et-management-de-transition-les-recherch%C3%A9s-tmj-ing%C3%A9nieur-ia` [secondary]; Kicklox / RH Solutions `https://www.rh-solutions.com/app/uploads/2025/12/RHS-Etude-2025-les-TJM-freelances_compressed.pdf` [secondary]; La Fabrique du Net `https://www.lafabriquedunet.fr/agences/tendances/tarifs-des-developpeurs-freelances-dans-les-grandes-villes-de-france` [secondary]; freelance-solution.fr `https://www.freelance-solution.fr/barometre-tjm-freelance-2026/` (compiles Malt 2026, Hays 2026, RH Solutions 2026, TJMètre 15,372 observations) [secondary]. Freelance.com and Comet barometers: not found as 2025-2026 documents, non vérifié. Robert Half: not found for TJM, non vérifié.

### B2. Pentest, AIPD, ISO 27001 / SOC 2 "lite"

| Item | Figure | Source, date read, tag |
|---|---|---|
| Web-app pentest, small SaaS, grey box, France | 4,000 to 15,000 € HT for 3 to 10 auditor-days. By scope: simple app with 1 role, 3-4 days, 4,000 to 6,000; business app with 2-3 roles, 5-7 days, 6,000 to 10,000; app plus exposed REST API, 6-8 days, 8,000 to 12,000; app plus API plus cloud infrastructure, 8-10 days, 11,000 to 15,000; retest after fixes 1-2 days, 1,000 to 2,500. Worked example: 7 days grey box at 1,150 €/day = 8,050 € HT, fixes 2,415, retest 1,150, total 11,615 € HT. Lead time 1 to 4 weeks (non-PASSI), 3 to 8 weeks (PASSI). Grey box with supplied test accounts recommended | Kolonell `https://kolonell.com/fr/blog/prix-pentest-application-web-pme-france-2026` (1 Oct 2026), 28 Oct 2026 [secondary, vendor] |
| Pentest, international vendor view | about 5,000 € for a very small scope; 15,000 to 30,000 € typical for a manual pentest of a standard business application (one to two weeks of testing); 50,000 €+ enterprise | 7ASecurity `https://7asecurity.com/blog/2026/04/the-2026-guide-to-penetration-testing-pricing-and-scoping/` (3 Apr 2026), 28 Oct 2026 [secondary, vendor] |
| Assumption for Helium MVP pentest (ESTIMATE) | 8,000 to 12,000 € HT for app plus API, grey box, plus 1,000 to 2,500 € retest; budget 12,000 € | derived from the two rows above |
| AIPD (DPIA) by a consultant | No published French market price found. Both specialist sites read refuse to give one ("aucun tarif réglementaire ni barème CNIL"). Illustrative day rates in those pages: 800 to 900 € HT. ESTIMATE: an AIPD for a mailbox-and-calendar agent (high-risk processing: systematic monitoring of private communications, large-scale personal data) at 4 to 8 consultant-days = 3,200 to 7,200 € HT; non vérifié as a market price | Legiscope `https://www.legiscope.com/blog/dpo-externalise-cout.html` (2 Jul 2026) [secondary]; donneespersonnelles.fr `https://donneespersonnelles.fr/dpo-externalise-tarifs` (27 May 2024, modified 3 Oct 2026) [secondary]; dpo-consulting.com AIPD page: no price or duration [secondary] |
| DPO externalisé, illustrative packages | donneespersonnelles.fr illustrative offers: setup 1,200 + 650 €/month (7,800/yr) + 3 extra days 2,700 = 12,300 € HT; or 900 €/month = 10,800 €/yr. Legiscope illustrative: 2 days/month at 800 € = 19,200 €/yr; forfait 1,500 €/month = 18,000 €/yr often excluding AIPD and incident handling | same pages [secondary]; both explicitly say these are not observed 2026 tariffs |
| ISO 27001-lite or SOC 2 lite | No credible cheap route with published French pricing found; skipped as instructed | non vérifié |

### B3. Public programmes for a French pre-seed startup

| Programme | Amount and conditions | Source, date read, tag |
|---|---|---|
| Bpifrance Bourse French Tech (BFT) | Subvention up to 70 % of eligible expenses, capped at 30,000 €. Company registered in France less than 1 year, fewer than 50 employees, turnover or balance sheet under 10 M€, any sector, innovation project with a maturation and technico-economic validation phase; Bpifrance targets founders supported by an accelerator or incubator. Eligible: internal staff costs and flat overheads; external support, IP, feasibility, legal and market studies, design, training. Expenses engaged before filing not retained; paid in two tranches (signature, then final report); fonds propres assessed at instruction without a published threshold | les-aides.fr sheet (CCI network, undated) `https://les-aides.fr/aide/M3OP3w/bpifrance.bourse-french-tech.pdf` [secondary]; Hayot Expertise `https://hayot-expertise.fr/blog/bourse-french-tech-bpifrance-conditions` (25 Sep 2026) citing bpifrance.fr/catalogue-offres/bourse-french-tech [secondary]; bpifrance.fr itself returned 403 from the research container, so the 30,000 € / 70 % parameters are confirmed by two secondary sources only |
| BFT Émergence (deeptech) and FPI Incubation (Paris) | Émergence: up to 90,000 €, 50 % rising to 70 % by company category, deeptech per Bpifrance referential. Fonds Parisien pour l'Innovation, volet Incubation: up to 30,000 €, requires an FPI-labelled incubator and a Paris establishment | Hayot (25 Sep 2026) [secondary] |
| Bpifrance Prêt d'amorçage "Préparer la levée" (Invest EU) | 50,000 to 100,000 € per intervention, up to 300,000 € with a Region guarantee, capped by equity and quasi-equity; 8 years including 3 years of capital deferral; no guarantee on company assets or founders' personal assets; 5 % of the loan retained at disbursement; fixed rate per published scale plus 0.40 % arrangement fee. Eligible: innovative SME under 5 years, seed stage, having received an innovation aid under the RDI regime (such as BFT); fundraising being prepared. "Accompagner la levée" variant: 100,000 to 1,000,000 € (2,000,000 by derogation) for SMEs under 8 years that closed a raise of at least 200,000 € with professional investors, capped at half the raise | Bpifrance Création encyclopedia `https://bpifrance-creation.fr/encyclopedie/financements/lemprunt/pret-damorcage-bpifrance` (Nov 2025), 28 Oct 2026 [official, Bpifrance] |
| JEI status (jeune entreprise innovante) | Conditions: PME (under 250 staff, turnover under 50 M€ or balance sheet under 43 M€), created less than 8 years ago, R&D expenses at least 20 % of charges (15 % threshold still applies to IR companies until FY2024), capital at least 50 % held by individuals, other JEIs, research bodies or investment companies, genuinely new activity. Social: for JEIs created before 31 Dec 2028, exemption of employer "cotisations d'assurances sociales et d'allocations familiales" for R&D staff and officers, on monthly pay up to 8,401.58 € (4.5 SMIC) and up to 240,300 € per établissement per year (5 PASS), until the last day of the 7th year after creation; not cumulable with another employer-contribution exemption for the same employee (so no réduction générale on top). Tax: JEIs created from 1 Jan 2024 no longer get the corporate income tax exemption (100 % then 50 % was for JEIs created before 31 Dec 2023); optional CFE and property-tax exemptions (7 years) on local deliberation. Threshold raised from 15 % to 20 % by LFSS 2025 (loi 2025-199 du 28 fév 2025), effective 1 Mar 2025 | `https://entreprendre.service-public.gouv.fr/vosdroits/F31188` (Vérifié le 01 juin 2026), 28 Oct 2026 [official]; URSSAF sheet via les-aides.fr `https://les-aides.fr/aide/VVj9/urssaf.jei-et-jeu-jeune-entreprise-innovante-et-jeune-entreprise-universitaire-exoneration-de-cotisations-patronales.pdf` [secondary, reproducing URSSAF]; Hayot `https://hayot-expertise.fr/blog/jei-2026-reforme-loi-finances-startups` [secondary] |
| CIR (crédit d'impôt recherche) | 30 % of eligible R&D expenses up to 100 M€ (5 % above); operating costs counted at 40 % of staff costs and 75 % of depreciation; immediate refund for companies under 2 years, JEIs and PMEs | `https://entreprendre.service-public.gouv.fr/vosdroits/F23533` (Vérifié le 21 février 2025), 28 Oct 2026 [official] |
| CII (crédit d'impôt innovation) | 20 % of eligible expenses (métropole; 60 % DOM; higher rates for small companies in Corsica), PME only, prototype or pilot installation of a new product not yet on the market, expenses capped at 400,000 € per year, applies to expenses until 31 Dec 2027; same immediate-refund rule as CIR | `https://entreprendre.service-public.gouv.fr/vosdroits/F35494` (Vérifié le 20 février 2026), 28 Oct 2026 [official]; Hayot confirms 20 % since 1 Jan 2025 and extension to 31 Dec 2027 [secondary] |
| Station F Founders Program | Founders Program 2.0 is "currently on pause" (programme designed for early-stage companies, up to 18 months, starting with a 3-month intensive phase). Fighters Program is free (under-represented founders). F/ai launched Jan 2026 (20 startups per batch, 2 batches per year, by recommendation only). Campus stay up to 2 years across programmes. Founders Program fee: not shown on the FAQ, non vérifié | Station F FAQ `https://faq.stationf.co/hc/en-us/articles/14706543850130-STATION-F-In-House-Programs`, 28 Oct 2026 [official] |
| Incubateur HEC Paris at Station F | Station F format: 300 € per desk per month, rising by 40 € per desk per month each quarter; online format: 300 € per startup per month. 4-month programme, extendable by 3-month periods up to 8 in total. Jury selects 18 to 24 projects per round; three calls per year (apply early October for January, early February for May, early June for September); eligibility form answered within 48 hours. Includes a desk among 200+, introductions to 1,000+ experts, network of about 200 entrepreneurs, 60,000 alumni, 4,000 students per year, Station F perks. Equity: not mentioned on the page. Track record: 900+ companies since 2007, 7 IPOs, over 1 bn€ raised; spring 2026 batch 13 teams | `https://www.hec.edu/en/hec-institute/innovation-entrepreneurship/our-centers/incubation-et-acceleration-center/hec-paris-incubateur`, 28 Oct 2026 [official, HEC] |

ESTIMATE, Incubateur HEC cost for 3 founders over 12 months at Station F, with the 40 € step applied from the second quarter (Q1 300, Q2 340, Q3 380, Q4 420 € per desk per month): per desk (300 + 340 + 380 + 420) x 3 months = 4,320 €; 3 desks = 12,960 € HT per year (10,800 € if the price stayed at 300 €); online format alternative 3,600 € per year per startup. Whether the page's prices are HT or TTC is not stated.

### B4. Gross monthly cost of a first engineer at 55,000 € brut annual (2026)

Parameters (read 28 Oct 2026): SMIC 12.31 €/h, 1,867.02 €/month, 22,404.20 €/year from 1 June 2026 (`https://www.service-public.gouv.fr/particuliers/vosdroits/F2300`, Vérifié le 01 juin 2026 [official]); PASS 2026 4,005 €/month = 48,060 €/year (Cleiss [official]); 55,000 € = 4,583 €/month = 2.45 SMIC.

Employer contribution rates at 1 Jan 2026 (Cleiss `https://www.cleiss.fr/docs/cotisations/france.html` [official], completed by Legisocial for formation, apprentissage and dialogue social [secondary] and Hayot for the AT/MP national average [secondary]): maladie 13 %; CSA 0.30 %; vieillesse plafonnée 8.55 % to the PASS; vieillesse déplafonnée 2.11 %; allocations familiales 5.25 %; AT/MP variable (national average 2.08 %, office activities usually around 1 %); chômage 4.00 % and AGS 0.25 % to 4 PASS; FNAL 0.10 % (under 50 staff); Agirc-Arrco T1 4.72 % / T2 12.95 %; CEG T1 1.29 % / T2 1.62 %; CET 0.21 %; APEC 0.036 % employer; formation 0.55 % (under 11 staff); taxe d'apprentissage 0.68 %; dialogue social 0.016 %; prévoyance cadre 1.5 % of T1 (conventional minimum). Réduction générale 2026 (RGDU): new formula from 1 Jan 2026, degressive from 1 to 3 SMIC, nil above; Tmax 0.3973 under 50 staff (Tmin 0.02, Tdelta 0.3773, exponent 1.75), décret 2025-1446 (Agirc-Arrco FAQ `https://www.agirc-arrco.fr/storage/FAQ-AA-Reduction-generale-des-cotisations-2026.pdf` [official]). The former reduced maladie (7 %) and allocations familiales (3.45 %) bands are treated as merged into this formula from 1 Jan 2026 (Hayot, 11 May 2026 [secondary], consistent with the new décret formula); the Cleiss page still lists them, see Points non confirmés.

| Scenario (ESTIMATE, formulas above) | Employer contributions per year | Rate on gross | Total annual cost | Monthly cost |
|---|---|---|---|---|
| Without JEI, before RGDU (AT/MP 2.08 %) | 24,443 € | 44.4 % | 79,443 € | 6,620 € |
| Without JEI, after RGDU (coefficient 0.0281 at 2.45 SMIC = 1,543 €) | 22,900 € | 41.6 % | 77,900 € | 6,490 € |
| Same with AT/MP at 1.0 % (office risk) | 22,306 € | 40.6 % | 77,306 € | 6,440 € |
| With JEI exemption on an eligible R&D engineer (maladie 13 % + vieillesse 8.55 % to PASS + 2.11 % + AF 5.25 % = 15,307 €, under the 8,401.58 €/month and 240,300 €/établissement caps; RGDU not cumulable) | 9,136 € | 16.6 % | 64,136 € | 5,345 € |

Net effect of JEI on this salary: about 13,760 € per year saved versus the RGDU case (15,307 € exemption minus the 1,543 € RGDU foregone), i.e. the monthly loaded cost falls from about 6,490 € to about 5,345 €. If "assurances sociales" were read as excluding vieillesse (the narrower reading in one secondary source), the exemption would be 10,038 € and the monthly cost about 5,780 €; the URSSAF wording "cotisations patronales d'assurances sociales et d'allocations familiales" covers vieillesse in standard URSSAF usage, which is the reading retained here.

Rule of thumb for the budget: 1.42 x gross without JEI, 1.17 x gross with JEI, excluding mutuelle (employer share of a mandatory health plan, typically 20 to 40 €/month), titres-restaurant, equipment and the médecine du travail fee.

---

## What to assume for a pilot

| Task type for Helium | Assumed first-pass success (range) | Reliability on repeat / notes | Variable cost per task (USD) | Source basis |
|---|---|---|---|---|
| Read-only synthesis (inbox and calendar summary, deadline extraction, "what needs my attention") | 85 to 95 % of outputs usable without correction | Errors are omissions and hallucinated dates, not harmful actions; human reads the output anyway. No benchmark isolates this; proxies: GAIA 94 % (saturated), tau2 retail read-heavy tasks 80 to 86 %, Mind2Web 2 partial completion 0.55 to 0.60 for long synthesis | 0.02 to 0.10 | GAIA, tau2, Mind2Web 2 [official] |
| Draft-for-validation (reply emails, booking request emails, reminders the user approves before sending) | 80 to 90 % of drafts accepted with at most light edits | AgentDojo utility 88.7 % on workspace tasks (email, calendar) for a frontier model without attack; prompt-injection ASR 1 to 7 % on frontier models without defenses, 0 to 11 % with, so the validation gate is the control | 0.03 to 0.15 | AgentDojo results page, Claude for Chrome tests [official] |
| API-based booking and account actions (partner APIs, structured tool calls: restaurant platform, garage booking widget with API, calendar write) | 80 to 90 % pass^1 with a frontier reasoning model; 55 to 75 % on a first attempt with a non-reasoning or small model | pass^4 50 to 78 % (Opus 4.5): expect 1 in 4 to 1 in 2 tasks to fail at least once over four repetitions, so design retries and a confirmation step; telecom-like multi-step flows cost 2x | 0.07 to 0.75 (reasoning model); 0.05 without reasoning | tau2-bench Sierra bucket [official] |
| Browser-based booking (no API: generic restaurant or garage websites, forms, logins) | 60 to 80 % per task on ordinary sites with a 2026 agent; 40 to 60 % on "hard" sites (multi-step filters, dynamic UIs, anti-bot) | Online-Mind2Web human-judged: 69 % (Gemini 2.5 CU, Sept 2025) to 92 to 98 % (specialised 2026 agents on GPT-5.4 or proprietary models); Operator live trials 3/10 to 10/10 by site; OSWorld-Verified Chrome subset 78 % for the best general model; retries help (pass@3 +12 points on Mind2Web 2) | 0.5 to 5 (HAL Online-Mind2Web: 0.57 with SeeAct on GPT-5, 5.26 with Browser-Use on Sonnet 4) plus browser infrastructure | OSU Online-Mind2Web, OSWorld-Verified, OpenAI CUA, HAL [official] |
| Any action with external effect (send, book, pay, delete) | Only after explicit user validation | Vendors (OpenAI, Anthropic, Google) all gate purchases and sensitive actions behind confirmation; OpenAI: prompt injection "unlikely to ever be fully solved" | n/a | OpenAI, Anthropic, Google pages [official] |

Budget assumptions for the French MVP (ESTIMATE, from Part B): senior full-stack 600 to 700 € HT/day, AI/LLM engineer 700 to 950, product designer 500 to 650, DevSecOps/cloud 700 to 800, pentest 12,000 € HT all-in, AIPD 3,200 to 7,200 € HT (non vérifié), first engineer at 55 k€ brut 6,490 €/month loaded (5,345 € with JEI), Incubateur HEC at Station F about 13,000 € per year for 3 desks, BFT up to 30,000 € subvention (70 % of expenses) and Prêt d'amorçage 50,000 to 100,000 € once BFT is obtained.

## Points non confirmés

1. tau2-bench retail and airline scores for models released after March 2026 (Claude Opus 5, Fable 5.1, GPT-5.5, GPT-5.6-sol): not published on the Sierra leaderboard (only tau3-Banking) nor on the vendor pages read, except GPT-5.5 telecom 98.0 %.
2. GAIA human baseline (92 %) quoted from the benchmark's own paper as remembered; the paper was not re-read, and the public leaderboard is saturated with anonymous multi-model harnesses, so GAIA is not used in the pilot assumptions.
3. AgentBench: no 2025-2026 primary-source refresh found.
4. OpenAI Operator system card prompt-injection figures and ChatGPT agent system card: pages could not be read (JavaScript-only or blocked); no figure quoted from them.
5. Production completion rates for consumer assistants (OpenAI, Perplexity Comet, Amazon Buy for Me, Google call-to-book, Apple): none published; the only quantified live-site evidence is the Operator 10-attempt trials and the Online-Mind2Web leaderboard.
6. Absolute token and step counts per agentic task: no primary source publishes them; the 115,000 tokens per rollout figure is a crude average from the HAL abstract (2.5 bn tokens / 21,730 rollouts) across heterogeneous benchmarks.
7. HAL per-task costs assume the public task-set sizes (50 for TAU-bench airline, 300 for Online Mind2Web, 165 for GAIA validation); HAL's exact subsets were not verified.
8. Malt "baromètre des TJM" 2026 as a document: not found; Malt figures are 2024 European averages from Malt Tech Trends 2025, and Île-de-France medians rely on Hays (via press), Michael Page and Kicklox. Freelance.com, Comet and Robert Half TJM guides: not found for 2025-2026.
9. Michael Page "ingénieur IA" freelance figure (600 to 1,000 €) is labelled ambiguously on the page (annual salary heading on a TJM grid) and the detailed grid is locked.
10. Pentest prices come from two vendors' blogs (one French SEO-heavy, one international); no neutral French survey of pentest prices was found. ANSSI PASSI qualification is not required for Helium's MVP.
11. AIPD market price: no published French figure; the 3,200 to 7,200 € estimate is derived from illustrative day rates and an assumed 4 to 8 days.
12. ISO 27001-lite / SOC 2-lite: no credible low-cost route with published pricing found; skipped.
13. Bourse French Tech parameters (30,000 €, 70 %) confirmed only on two secondary sources because bpifrance.fr blocked the research container; to re-check on `https://www.bpifrance.fr/catalogue-offres/bourse-french-tech` before filing. Regional co-funding of BFT: not mentioned by either source.
14. Station F Founders Program fee: not published on the FAQ and the programme is "on pause"; no figure retained.
15. HEC Incubator equity terms and whether non-HEC founders are eligible: not stated on the page read.
16. 2026 employer rates: the Cleiss table (1 Jan 2026) still lists the reduced maladie 7 % (up to 2.396 SMIC) and allocations familiales 3.45 % (up to 3.3 SMIC) bands, while Hayot (May 2026) states they were removed and merged into the new RGDU, and the Agirc-Arrco FAQ gives the new RGDU formula (décret 2025-1446) without mentioning the bands. The brief follows the merged-RGDU reading; if the bands still applied, the 55 k€ engineer (2.45 SMIC) would get allocations familiales at 3.45 % instead of 5.25 %, lowering the non-JEI cost by about 990 € per year.
17. AT/MP rate is établissement-specific (Carsat notification); 2.08 % is a national average across all sectors and 1.0 % is an assumption for office work.
18. JEI exemption scope: "assurances sociales" read as including vieillesse (standard URSSAF usage); one secondary source lists only sickness, maternity, disability, death and family. The narrower reading changes the monthly loaded cost from about 5,345 € to about 5,780 €.
19. Artificial Analysis "Agentic Index" and its cost-to-run figures: page blocked; only the Sonnet 5 article was read, and its 2.29 USD per task covers the whole Intelligence Index, not only agentic tasks.
20. Stanford AI Index 2026 (agent adoption and incident statistics): page blocked, not used.
