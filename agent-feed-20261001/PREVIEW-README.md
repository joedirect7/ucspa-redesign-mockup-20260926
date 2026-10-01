# UCS fuller agent / LLM feed — PREVIEW for Joe

**Drafted:** Thursday Oct 1, 2026 (ET)  
**Folder:** `/workspace/ucs-seo/agent-feed-20261001/`  
**Status:** PREVIEW / DRAFT ONLY

## Hard lock — nothing live changed

- **Live** https://www.ucspa.com/llms.txt is **NOT** updated.
- **No HubSpot publish** of this feed (no File Manager overwrite, no CMS page swap).
- Box-only work; no `machineId` / JOE_HP2.
- Soft-power only; no denial/CUT URLs in the feed; Cherry Hill = NJ; Miami NAP = 11900 Biscayne Blvd #400, North Miami FL 33181.
- Brand phone **855-321-5677**; CallRail **855-917-2449** documented as `/insurance-claim-help` only.

## What to review

| File | Role |
|------|------|
| `llms-full.txt` | Expanded agent map (org, NAP, services, canonical URLs, live cities, damage landers, soft CTA, do-not-invent) |
| `SETTLEMENTS.md` | Straight-fact settlement catalog from live `/recent-settlements` |
| `FAQ.md` | Live FAQ Q&A catalog (social handles + FL lic# scrubbed from this agent copy; claim-help = 24/7) |
| `llms-full.html` | Clickable local / GH Pages preview of the map |
| `PREVIEW-README.md` | This file |

## How Joe reviews

1. Open the clickable preview (GH Pages URL below, or open `llms-full.html` locally).
2. Spot-check facts vs live `/for-agents`, `/contact-us`, `/faq`, `/recent-settlements`.
3. Confirm live cities list still matches production (seven cities only).
4. Confirm no denial/CUT URLs and no invented fee % / licenses / cities.
5. **Approve explicitly** before any HubSpot publish or overwrite of live `llms.txt`.

## Proposed HubSpot paths (only after Joe green-lights)

| Asset | Proposed live path | Notes |
|-------|--------------------|-------|
| Fuller agent map | Option A: replace content of `https://www.ucspa.com/llms.txt` with `llms-full.txt` (or a trimmed merge) | Current live file is the thin map (revised 2026-09-29) |
| Fuller agent map | Option B: new HubSpot File Manager path e.g. `/llms-full.txt` + link from `/for-agents` | Keeps thin `llms.txt` as cheap map |
| Settlements catalog | Optional: attach or mirror as `/agent-settlements.md` **or** keep human page only at `/recent-settlements` | Prefer human page as source of truth |
| FAQ catalog | Optional: `/agent-faq.md` **or** keep human page only at `/faq` | Live FAQ already has FAQPage schema |
| Agent cheat sheet | Keep canonical ingest: https://www.ucspa.com/for-agents | Update that page if fuller facts need to merge there |

**Do not publish** until Joe names which option (A/B) and which companions go live.

## Sources used

1. https://www.ucspa.com/llms.txt  
2. https://www.ucspa.com/for-agents  
3. https://www.ucspa.com/recent-settlements  
4. https://www.ucspa.com/faq (live; draft FAQ file only used as fallback reference)  
5. `/workspace/ucs-seo/seo-agency-scoreboard/PROTOCOL.md` + `BEST-PRACTICES-PA-FIRM.md`  
6. Live sitemap + HEAD/GET spot-checks for damage landers and geo URLs  

## Gaps / unknowns

- Laundry-room and Hurricane Michael / Irma settlement rows do not name a city/locale beyond the event or damage type on the live page — catalog leaves place as unspecified where live does.
- `hail-damage-insurance-claims-0` exists in sitemap (200) but looks like a duplicate junk slug — **excluded** from the agent map pending Joe.
- Short damage aliases (`/water-damage`, `/flood-damage`, etc.) redirect to longer `*-insurance-claims` canonicals — map lists finals.
- Social handles intentionally omitted from `FAQ.md` agent scrub (live FAQ Q19 mentions Facebook / X / Instagram generically).
- FL LIC# W806268 kept in `llms-full.txt` (live footer / for-agents) but scrubbed from `FAQ.md` per agent-feed scrub note.
- Review snippets remain on `/for-agents`; this pack does not duplicate long quote blocks into `llms-full.txt` beyond pointing to reviews.

## Preview URL

See deploy note at bottom of this file after GH Pages push (or use box path `file:///workspace/ucs-seo/agent-feed-20261001/llms-full.html`).

## Clickable preview

- **GH Pages (after deploy):** https://joedirect7.github.io/ucspa-redesign-mockup-20260926/agent-feed-20261001/
- **Box file:** `/workspace/ucs-seo/agent-feed-20261001/llms-full.html`
- **Raw text:** `/workspace/ucs-seo/agent-feed-20261001/llms-full.txt`
