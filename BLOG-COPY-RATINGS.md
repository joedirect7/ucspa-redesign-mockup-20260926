# UCS Blog Copy Ratings

**Date:** Sat Sep 26, 2026 (ET)  
**Scope:** Live ucspa.com/blog (prefer), mockup `/blog/`, inventory `blogs-index.md` + `content-dump/`  
**Corpus:** ~353 sitemap posts; mockup showcases ~29. Rated only posts with real body text.  
**Joe guidance:** Preserve educational voice. Do **not** wholesale rewrite. Refresh+Redate allowed for evergreen. **Exclude** stale topics. Never invent new legal claims or fake stats.

**Score axes (1–10):** Educational depth · Accuracy/trust tone · Readability · SEO/link-worthiness · Freshness · Conversion (subtle CTA fit)  
**Composite** = mean of six axes.  
**Verdicts:** `Refresh+Redate` | `Keep as-is` | `Light polish only` | `Exclude (stale topic)`

**Canonical CTA target for internal links:** `/insurance-claim-help`

---

## Summary

| Verdict | Count (scored posts) |
|---------|----------------------|
| Keep as-is | 5 |
| Refresh+Redate | 28 |
| Light polish only | 4 |
| Exclude (stale topic) | 18 (accessed body) + more inventory-flagged (see revamp plan) |
| Incomplete fetch — skip score | 5 mockup-only stubs / wrong slug in mockup |

**Explicit recommendation:** Do **not** revise every blog. Visual redesign + selective in-body links to `/insurance-claim-help` is enough for most. Prioritize Refresh+Redate for the mockup blog index; hide or demote Excludes. See `BLOG-REVAMP-PLAN.md`.

### Top 10 keep-as-is / showcase pillars (best for backlinks + mockup)

These are the strongest educational assets for backlinks and mockup showcase (Keep as-is or Refresh+Redate with minimal touch):

1. **Difference in Coverage for Regular Storms vs. Hurricanes** — cites III, FL Statutes, DFS; AOP vs hurricane deductible
2. **Behind the Claims: Insiders Reveal Altered Reports After Hurricanes** — newsworthy, 60 Minutes-sourced
3. **Are Slab Leaks Covered By Homeowners Insurance?** — deep HO-1/HO-3 education (Dec 2024)
4. **Quick Guide to the Differences Between the Types of Adjusters** — clear staff/independent/public taxonomy
5. **Common Mistakes on Insurance Claims** — practical claim hygiene (Sep 2024)
6. **Signs of Water Damage in Your Walls** (`…-walls-0`) — long-form detection guide (Nov 2024)
7. **When Does Homeowners Insurance Cover Roof Replacements** (`…-0`) — coverage vs wear-and-tear teaching
8. **What Happens When You Don’t Call a Public Adjuster** (`…-0`) — language pitfalls that deny claims
9. **Frozen Pipe Insurance Claims: WHAT TO DO** — denial reasons + duties after loss (Jan 2025)
10. **Burden of Proof in Florida Homeowners Insurance Claims** — FL-specific legal education (strip expired Irma deadline on refresh)

### Mockup nav spot-check (5 HTML files)

Checked relative links in:

- `blog/burden-of-proof-in-florida/index.html`
- `blog/behind-the-claims-insiders-reveal-altered-reports-after-hurricanes/index.html`
- `blog/quick-guide-to-the-differences-between-the-types-of-adjusters-0/index.html`
- `blog/common-mistakes-on-insurance-claims/index.html`
- `blog/how-do-i-reopen-an-insurance-claim/index.html`

**Result:** Home (`../../index.html`), claim-help (`../../insurance-claim-help/`), blog index (`../../blog/` / `../`), related posts, and service/location nav — **all OK (0 broken)** on each file.

**Nav notes (non-blocking):**

- Mockup slug mismatches vs live: several live posts use a trailing `-0` (e.g. `signs-of-water-damage-in-your-walls-0`); mockup folders omit `-0`. Fix redirects or rename when implementing so cards don’t 404.
- Footer © still reads live as 2009–2022; mockup already uses 2009–2026 — fine for redesign.

---

## Rated posts (full body accessed)

### A. Keep as-is (recent pillars — redesign + claim-help link only)

#### 1. Are Slab Leaks Covered By Homeowners Insurance?
- **URL:** https://www.ucspa.com/blog/are-slab-leaks-covered-by-homeowners-insurance-0  
- **Slug:** `are-slab-leaks-covered-by-homeowners-insurance-0`  
- **Title:** Are Slab Leaks Covered By Homeowners Insurance?  
- **Date:** Dec 11, 2024 (JS)  
- **Scores:** Ed 9 · Trust 8 · Read 8 · SEO 9 · Fresh 9 · Conv 7 → **Composite 8.3**  
- **Verdict:** Keep as-is  
- **Proposed new date:** —  
- **Note:** Strong HO-1 vs HO-3 teaching. Tiny typos (“there a few”, “I f a leaking”) — optional only. Add in-body link to claim-help.

#### 2. Behind the Claims: Insiders Reveal Altered Reports After Hurricanes
- **URL:** https://www.ucspa.com/blog/behind-the-claims-insiders-reveal-altered-reports-after-hurricanes  
- **Slug:** `behind-the-claims-insiders-reveal-altered-reports-after-hurricanes`  
- **Title:** Behind the Claims: Insiders Reveal Altered Reports After Hurricanes  
- **Date:** Oct 2, 2024 (SE)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 10 · Fresh 8 · Conv 7 → **Composite 8.5**  
- **Verdict:** Keep as-is  
- **Note:** Best link magnet. Title says “Helen” in H2 (likely Helene) — typo-only fix if touching. Do not invent new investigation claims.

#### 3. Quick Guide to the Differences Between the Types of Adjusters
- **URL:** https://www.ucspa.com/blog/quick-guide-to-the-differences-between-the-types-of-adjusters-0  
- **Slug:** `quick-guide-to-the-differences-between-the-types-of-adjusters-0`  
- **Title:** Quick Guide to the Differences Between the Types of Adjusters  
- **Date:** Sep 24, 2024 (Katya S)  
- **Scores:** Ed 9 · Trust 9 · Read 9 · SEO 9 · Fresh 9 · Conv 7 → **Composite 8.7**  
- **Verdict:** Keep as-is  
- **Note:** Mockup has full body — showcase candidate.

#### 4. Common Mistakes on Insurance Claims
- **URL:** https://www.ucspa.com/blog/common-mistakes-on-insurance-claims-0  
- **Slug:** `common-mistakes-on-insurance-claims-0` (mockup folder omits `-0`)  
- **Title:** Common Mistakes on Insurance Claims  
- **Date:** Sep 3, 2024 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 9 · SEO 8 · Fresh 9 · Conv 8 → **Composite 8.3**  
- **Verdict:** Keep as-is  
- **Note:** Mockup body is teaser-only; paste full live CMS body on publish.

#### 5. Frozen Pipe Insurance Claims: WHAT TO DO
- **URL:** https://www.ucspa.com/blog/frozen-pipe-insurance-claims-0  
- **Slug:** `frozen-pipe-insurance-claims-0` (mockup: `frozen-pipe-insurance-claims-what-to-do`)  
- **Title:** Frozen Pipe Insurance Claims: WHAT TO DO  
- **Date:** Jan 2, 2025 (joe suskind)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 8 · Fresh 10 · Conv 8 → **Composite 8.7**  
- **Verdict:** Keep as-is  
- **Note:** Typo-only: “vacant of unoccupied” → “or”. Excellent denial-reason education.

---

### B. Refresh+Redate (evergreen — keep core teaching)

#### 6. Difference in Coverage for Regular Storms vs. Hurricanes
- **URL:** https://www.ucspa.com/blog/difference-in-coverage-for-regular-storms-vs-hurricanes-0  
- **Slug:** `difference-in-coverage-for-regular-storms-vs-hurricanes-0`  
- **Title:** Difference in Coverage for Regular Storms vs. Hurricanes  
- **Date:** Jul 2, 2024 (JS)  
- **Scores:** Ed 10 · Trust 10 · Read 9 · SEO 10 · Fresh 7 · Conv 7 → **Composite 8.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-06  
- **Note:** Citations accessed Apr 2021 — re-verify FL Statute / DFS links only; keep examples. Top pillar for mockup (not currently in mockup set — add).

#### 7. Signs of Water Damage in Your Walls
- **URL:** https://www.ucspa.com/blog/signs-of-water-damage-in-your-walls-0  
- **Slug:** `signs-of-water-damage-in-your-walls-0`  
- **Title:** Signs of Water Damage in Your Walls  
- **Date:** Nov 20, 2024 (JS)  
- **Scores:** Ed 9 · Trust 8 · Read 8 · SEO 9 · Fresh 8 · Conv 8 → **Composite 8.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-13  
- **Note:** Mockup slug missing `-0`. Light trim of repetition; keep checklist structure.

#### 8. When Does Homeowners Insurance Cover Roof Replacements
- **URL:** https://www.ucspa.com/blog/when-does-homeowners-insurance-cover-roof-replacements-0  
- **Slug:** `when-does-homeowners-insurance-cover-roof-replacements-0`  
- **Title:** When Does Homeowners Insurance Cover Roof Replacements  
- **Date:** Oct 22, 2024 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 7 · SEO 9 · Fresh 8 · Conv 8 → **Composite 8.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-20  
- **Note:** Slightly wordy; keep coverage vs wear-and-tear core. Fix mockup slug.

#### 9. What Happens When You Don’t Call a Public Adjuster?
- **URL:** https://www.ucspa.com/blog/what-happens-when-you-dont-call-a-public-adjuster-0  
- **Slug:** `what-happens-when-you-dont-call-a-public-adjuster-0`  
- **Title:** What Happens When You Don’t Call a Public Adjuster?  
- **Date:** Nov 7, 2024 (JS)  
- **Scores:** Ed 9 · Trust 8 · Read 8 · SEO 9 · Fresh 8 · Conv 8 → **Composite 8.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-27  
- **Note:** Strong “language that denies claims” section — preserve. Mockup slug missing `-0`.

#### 10. Top Five Tips on Filing a Mold Damage Claim
- **URL:** https://www.ucspa.com/blog/top-five-tips-on-filing-a-mold-damage-claim-0  
- **Slug:** `top-five-tips-on-filing-a-mold-damage-claim-0`  
- **Title:** Top Five Tips on Filing a Mold Damage Claim  
- **Date:** Dec 3, 2024 (Lisa)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 8 · Fresh 8 · Conv 8 → **Composite 8.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-03  
- **Note:** CDC/FEMA/UPHelp cites — keep; redate access dates on refresh only. Mockup slug missing `-0`.

#### 11. Top Five Tips on Hurricane Preparation
- **URL:** https://www.ucspa.com/blog/top-five-tips-on-hurricane-preparation-0  
- **Slug:** `top-five-tips-on-hurricane-preparation-0`  
- **Title:** Top Five Tips on Hurricane Preparation  
- **Date:** Jun 27, 2024 (JS)  
- **Scores:** Ed 8 · Trust 9 · Read 9 · SEO 8 · Fresh 5 · Conv 7 → **Composite 7.7**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-05-15 (pre-season)  
- **Note:** NOAA **2024** season outlook is dated — swap to current-season NOAA blurb only (no invented forecast). Keep 5 tips + waterproof policy copy.

#### 12. Why You Should Not Accept an Insurance Company’s First Offer
- **URL:** https://www.ucspa.com/blog/why-you-should-not-accept-an-insurance-companys-first-offer-0  
- **Slug:** `why-you-should-not-accept-an-insurance-companys-first-offer-0`  
- **Title:** Why You Should Not Accept an Insurance Company’s First Offer  
- **Date:** Aug 19, 2024 (JS)  
- **Scores:** Ed 7 · Trust 8 · Read 8 · SEO 8 · Fresh 8 · Conv 8 → **Composite 7.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-10  
- **Note:** Mockup is stub teaser — restore full live body.

#### 13. Insurance Claim Denied? These Are the Next Steps
- **URL:** https://www.ucspa.com/blog/insurance-claim-denied-these-are-the-next-steps-0  
- **Slug:** `insurance-claim-denied-these-are-the-next-steps-0`  
- **Title:** Insurance Claim Denied? These Are the Next Steps  
- **Date:** Aug 27, 2024 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 8 · Conv 8 → **Composite 8.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-17  
- **Note:** Solid denial taxonomy. Link claim-help + denied-claims hub.

#### 14. Top 5 Benefits for Hiring a Public Insurance Adjuster
- **URL:** https://www.ucspa.com/blog/top-5-benefits-for-hiring-a-public-insurance-adjuster-0  
- **Slug:** `top-5-benefits-for-hiring-a-public-insurance-adjuster-0`  
- **Title:** Top 5 Benefits for Hiring a Public Insurance Adjuster  
- **Date:** Jul 17, 2024 (JS)  
- **Scores:** Ed 6 · Trust 7 · Read 8 · SEO 7 · Fresh 8 · Conv 8 → **Composite 7.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-24  
- **Note:** More marketing than deep education; keep structure, light tighten. Mockup body stubby.

#### 15. Burden of Proof in Florida Homeowners Insurance Claims
- **URL:** https://www.ucspa.com/blog/burden-of-proof-in-florida  
- **Slug:** `burden-of-proof-in-florida`  
- **Title:** Burden of Proof in Florida Homeowners Insurance Claims  
- **Date:** Feb 25, 2020 (JS)  
- **Scores:** Ed 9 · Trust 8 · Read 8 · SEO 9 · Fresh 4 · Conv 6 → **Composite 7.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-08  
- **Note:** **Remove expired Irma appeal deadline (“September 10”)** — stale within otherwise evergreen teaching. Keep burden-shift / slab-case education. Do not invent new case law.

#### 16. Bad Faith Insurance Claims
- **URL:** https://www.ucspa.com/blog/bad-faith-insurance-claims  
- **Slug:** `bad-faith-insurance-claims`  
- **Title:** Bad Faith Insurance Claims  
- **Date:** Feb 10, 2020 (joe suskind)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 9 · Fresh 4 · Conv 6 → **Composite 7.5**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-15  
- **Note:** Strong checklist of bad-faith patterns. Typo: “does not constitute as”. Pair with Civil Remedy Notices.

#### 17. Civil Remedy Notices
- **URL:** https://www.ucspa.com/blog/civil-remedy-notices  
- **Slug:** `civil-remedy-notices`  
- **Title:** Civil Remedy Notices  
- **Date:** Feb 25, 2020 (joe suskind)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 9 · Fresh 3 · Conv 5 → **Composite 7.2**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-16  
- **Note:** Keep Fla. Stat. 624.155 required elements. “Recent Changes” (2019 HB 301) — label as historical / verify if still accurate; do not invent updates. Typo: “you potential remedy is to a bad faith”.

#### 18. Churn and Burn Insurance Adjusting
- **URL:** https://www.ucspa.com/blog/churn-and-burn-insurance-adjusting  
- **Slug:** `churn-and-burn-insurance-adjusting`  
- **Title:** Churn and Burn Insurance Adjusting  
- **Date:** Mar 2, 2020 (joe suskind)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 9 · Fresh 4 · Conv 5 → **Composite 7.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-22  
- **Note:** Excellent industry-insider education; keep Merlin Law Group citation. High backlink potential.

#### 19. What You Need to Know About Sworn Statement in Proof of Loss
- **URL:** https://www.ucspa.com/blog/what-you-need-to-know-about-sworn-statement-in-proof-of-loss  
- **Slug:** `what-you-need-to-know-about-sworn-statement-in-proof-of-loss`  
- **Title:** What You Need to Know About Sworn Statement in Proof of Loss  
- **Date:** Mar 4, 2020 (JS)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 9 · Fresh 4 · Conv 7 → **Composite 7.7**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-10-29  
- **Note:** Typo: “errors or accuracies” → “inaccuracies”. Evergreen process piece.

#### 20. Preparing for Examination Under Oath
- **URL:** https://www.ucspa.com/blog/preparing-for-examination-under-oat  
- **Slug:** `preparing-for-examination-under-oat` (typo slug “oat”)  
- **Title:** Preparing for Examination Under Oath  
- **Date:** Feb 23, 2020 (joe suskind)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 8 · Fresh 4 · Conv 7 → **Composite 7.5**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-05  
- **Note:** Keep EUO teaching. Optional: add redirect from `…-oat` → corrected slug if CMS allows (no new claims).

#### 21. Appraisals in Hurricane Damage Insurance Claim Disputes
- **URL:** https://www.ucspa.com/blog/appraisals-in-hurricane-damage-insurance-claim-disputes  
- **Slug:** `appraisals-in-hurricane-damage-insurance-claim-disputes`  
- **Title:** Appraisals in Hurricane Damage Insurance Claim Disputes  
- **Date:** Jan 30, 2020 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 6 → **Composite 7.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-12  
- **Note:** Keep benefits/risks of appraisal. Soften Irma-era spike as historical context; do not invent new Citizens stats.

#### 22. Top Reasons to Hire a Public Adjuster
- **URL:** https://www.ucspa.com/blog/top-reasons-to-hire-a-public-adjuster  
- **Slug:** `top-reasons-to-hire-a-public-adjuster`  
- **Title:** Top Reasons to Hire a Public Adjuster  
- **Date:** Apr 1, 2020 (joe suskind)  
- **Scores:** Ed 7 · Trust 7 · Read 8 · SEO 8 · Fresh 4 · Conv 8 → **Composite 7.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-11-19  
- **Note:** Keep OPPAGA PDF citation for “747%” — do **not** invent alternate stats. Align “700%/747%” consistency sitewide only if already sourced.

#### 23. How to Dispute a Home Insurance Claim Settlement or Denial
- **URL:** https://www.ucspa.com/blog/how-to-dispute-a-home-insurance-claim-settlement-or-denial  
- **Slug:** `how-to-dispute-a-home-insurance-claim-settlement-or-denial`  
- **Title:** How to Dispute a Home Insurance Claim Settlement or Denial  
- **Date:** Feb 7, 2020 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 7 → **Composite 7.2**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-01  
- **Note:** Practical dispute path; link claim-help.

#### 24. How Do I Reopen an Insurance Claim?
- **URL:** https://www.ucspa.com/blog/how-do-i-reopen-an-insurance-claim  
- **Slug:** `how-do-i-reopen-an-insurance-claim`  
- **Title:** How Do I Reopen an Insurance Claim?  
- **Date:** May 15, 2019 (joe suskind)  
- **Scores:** Ed 7 · Trust 7 · Read 8 · SEO 8 · Fresh 3 · Conv 8 → **Composite 6.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-03  
- **Note:** Verify “three years” / “five years” language against current FL practice with Joe/counsel before publish — do not invent deadlines. Soft CTA already good.

#### 25. Condo Insurance Claims
- **URL:** https://www.ucspa.com/blog/condo-insurance-claims  
- **Slug:** `condo-insurance-claims`  
- **Title:** Condo Insurance Claims  
- **Date:** Feb 25, 2020 (joe suskind)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 6 → **Composite 7.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-08  
- **Note:** Strong unit vs master-policy education. Mockup teaser-only — restore full body.

#### 26. Does Homeowner’s Insurance Cover Land Erosion?
- **URL:** https://www.ucspa.com/blog/does-homeowners-insurance-cover-land-erosion  
- **Slug:** `does-homeowners-insurance-cover-land-erosion`  
- **Title:** Does Homeowner’s Insurance Cover Land Erosion?  
- **Date:** Mar 22, 2020 (joe suskind)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 5 → **Composite 6.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-10  
- **Note:** Keep earth-movement / NFIP / DIC teaching. Typo: “lighting” → “lightning”.

#### 27. Casualty Loss Deduction
- **URL:** https://www.ucspa.com/blog/casualty-loss-deduction  
- **Slug:** `casualty-loss-deduction`  
- **Title:** Casualty Loss Deduction  
- **Date:** Mar 8, 2020 (joe suskind)  
- **Scores:** Ed 8 · Trust 8 · Read 7 · SEO 7 · Fresh 2 · Conv 4 → **Composite 6.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-15  
- **Note:** TCJA rules through 2025 — **must** update for post-2025 tax status with accurate public IRS framing only (no invented tax advice). Typo: “much more brad”.

#### 28. Canine Liability Exclusion
- **URL:** https://www.ucspa.com/blog/canine-liability-exclusion  
- **Slug:** `canine-liability-exclusion`  
- **Title:** Canine Liability Exclusion  
- **Date:** Mar 18, 2020 (joe suskind)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 7 · Fresh 3 · Conv 4 → **Composite 6.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-17  
- **Note:** Keep breed-list / III claim-cost teaching; refresh 2018 III figure only if Joe confirms current public III number — else leave as dated cite.

#### 29. Completing a Total Loss Inventory
- **URL:** https://www.ucspa.com/blog/completing-a-total-loss-inventory  
- **Slug:** `completing-a-total-loss-inventory`  
- **Title:** Completing a Total Loss Inventory  
- **Date:** Mar 24, 2020 (joe suskind)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 7 → **Composite 7.2**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-22  
- **Note:** Practical how-to; keep room-by-room method.

#### 30. Property Loss Claims: What Is Replacement Cost vs Actual Cash Value?
- **URL:** https://www.ucspa.com/blog/for-property-loss-claims-what-is-replacement-cost-vs-actual-cash-value  
- **Slug:** `for-property-loss-claims-what-is-replacement-cost-vs-actual-cash-value`  
- **Title:** Property Loss Claims: What Is Replacement Cost vs Actual Cash Value?  
- **Date:** Feb 3, 2021 (JS)  
- **Scores:** Ed 9 · Trust 9 · Read 8 · SEO 9 · Fresh 5 · Conv 7 → **Composite 7.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-12-29  
- **Note:** Excellent RCV/ACV/recoverable depreciation teaching — pillar for mockup add.

#### 31. 5 Things Your Insurance Company May Not Want You to Know
- **URL:** https://www.ucspa.com/blog/5-things-your-insurance-company  
- **Slug:** `5-things-your-insurance-company` (mockup longer slug)  
- **Title:** 5 Things Your Insurance Company May Not Want You to Know  
- **Date:** Feb 23, 2020 (JS)  
- **Scores:** Ed 7 · Trust 7 · Read 8 · SEO 8 · Fresh 4 · Conv 7 → **Composite 6.8**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-05  
- **Note:** Keep listicle structure; soft claims only.

#### 32. How To Manage A Denied Homeowners Insurance Claim
- **URL:** https://www.ucspa.com/blog/how-to-manage-a-denied-homeowners-insurance-claim  
- **Slug:** `how-to-manage-a-denied-homeowners-insurance-claim`  
- **Title:** How To Manage A Denied Homeowners Insurance Claim  
- **Date:** Oct 21, 2021 (JS)  
- **Scores:** Ed 8 · Trust 8 · Read 8 · SEO 8 · Fresh 5 · Conv 8 → **Composite 7.5**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-07  
- **Note:** Keep III fraud cites as dated; link claim-help.

#### 33. What You Need to Know About Hail Damage Claims
- **URL:** https://www.ucspa.com/blog/what-you-need-to-know-about-hail-damage-claims  
- **Slug:** `what-you-need-to-know-about-hail-damage-claims`  
- **Title:** What You Need to Know About Hail Damage Claims  
- **Date:** Jan 30, 2020 (joe suskind)  
- **Scores:** Ed 7 · Trust 8 · Read 8 · SEO 8 · Fresh 4 · Conv 7 → **Composite 7.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-12  
- **Note:** Keep scammer caution section. Mockup stub — restore full body.

#### 34. How can I Find a Public Adjuster Near Me?
- **URL:** https://www.ucspa.com/blog/how-can-i-find-a-public-adjuster-near-me  
- **Slug:** `how-can-i-find-a-public-adjuster-near-me`  
- **Title:** How can I Find a Public Adjuster Near Me?  
- **Date:** Sep 28, 2019 (joe suskind)  
- **Scores:** Ed 5 · Trust 6 · Read 7 · SEO 7 · Fresh 3 · Conv 8 → **Composite 6.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-14  
- **Note:** More sales than education; keep process beats (inspection → docs → negotiate). Lighten repetition.

#### 35. Why Reopen a Denied Insurance Claim?
- **URL:** https://www.ucspa.com/blog/why-reopen-a-denied-insurance-claim  
- **Slug:** `why-reopen-a-denied-insurance-claim`  
- **Title:** Why Reopen a Denied Insurance Claim?  
- **Date:** Sep 21, 2018 (joe suskind)  
- **Scores:** Ed 5 · Trust 6 · Read 7 · SEO 7 · Fresh 3 · Conv 8 → **Composite 6.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-19  
- **Note:** Overlaps reopen how-to; keep shorter companion or cross-link rather than expand claims.

#### 36. Contractors Cannot Legally Negotiate Insurance Claims
- **URL:** https://www.ucspa.com/blog/contractors-legally-negotiate-insurance-claims  
- **Slug:** `contractors-legally-negotiate-insurance-claims`  
- **Title:** Contractors Cannot Legally Negotiate Insurance Claims  
- **Date:** Sep 4, 2012 (JS)  
- **Scores:** Ed 7 · Trust 8 · Read 6 · SEO 8 · Fresh 2 · Conv 5 → **Composite 6.0**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2027-01-21  
- **Note:** Short but valuable FL 626.854 teaching — expand only with Joe-approved statute language already on live; do not invent penalties. Keep core warning.

#### 37. An Ounce of Prevention: Minimizing Hurricane Damage
- **URL:** https://www.ucspa.com/blog/an-ounce-of-prevention-minimizing-hurricane-damage  
- **Slug:** `an-ounce-of-prevention-minimizing-hurricane-damage`  
- **Title:** An Ounce of Prevention: Minimizing Hurricane Damage  
- **Date:** Jun 2, 2021 (JS)  
- **Scores:** Ed 6 · Trust 6 · Read 7 · SEO 6 · Fresh 3 · Conv 4 → **Composite 5.3**  
- **Verdict:** Refresh+Redate  
- **Proposed new date:** 2026-05-22  
- **Note:** Association-focused tips OK. **Fix broken CTA URL `usfl.com` → ucspa.com** (typo only). Short — keep checklist.

---

### C. Light polish only

#### 38. How to Handle Homeowner’s Insurance Denial
- **URL:** https://www.ucspa.com/blog/how-to-handle-homeowners-insurance-denial  
- **Slug:** `how-to-handle-homeowners-insurance-denial`  
- **Title:** How to Handle Homeowner’s Insurance Denial  
- **Date:** Apr 21, 2015 (JS)  
- **Scores:** Ed 5 · Trust 6 · Read 6 · SEO 6 · Fresh 2 · Conv 4 → **Composite 4.8**  
- **Verdict:** Light polish only *(or demote behind newer denial posts)*  
- **Proposed new date:** —  
- **Note:** Thin; newer denial posts supersede for showcase. Typo: “measures of inadequate”. Prefer Refresh path only if Joe wants 2015 URL kept live.

#### 39. How To Fast Track Your Insurance Claims
- **URL:** https://www.ucspa.com/blog/how-to-fast-track-your-insurance-claims  
- **Slug:** `how-to-fast-track-your-insurance-claims`  
- **Title:** How To Fast Track Your Insurance Claims  
- **Date:** Aug 6, 2013 (JS)  
- **Scores:** Ed 4 · Trust 5 · Read 5 · SEO 5 · Fresh 2 · Conv 5 → **Composite 4.3**  
- **Verdict:** Light polish only *(candidate to demote from mockup index)*  
- **Note:** Dated Fort Lauderdale flooding voice; thin. Prefer newer denial/process pillars for showcase.

#### 40. Why You Should Employ a Private Insurance Adjuster in Miami
- **URL:** https://www.ucspa.com/blog/why-you-should-employ-a-private-insurance-adjuster-in-miami  
- **Slug:** `why-you-should-employ-a-private-insurance-adjuster-in-miami`  
- **Title:** Why You Should Employ a Private Insurance Adjuster in Miami  
- **Date:** (live/meta partial)  
- **Scores:** Ed — · Trust — · Read — · SEO — · Fresh — · Conv — → **incomplete for full score from live body in this pass**  
- **Verdict:** Light polish only *(mockup teaser; prefer full CMS paste)*  
- **Note:** Mockup ~208 words teaser — treat as incomplete until full body restored from CMS. Skip hard score.

#### 41. A Florida Public Adjuster Can Help After Storm Damage
- **URL / mockup:** `a-florida-public-adjuster-can-help-after-storm-damage`  
- **Scores:** —  
- **Verdict:** incomplete fetch — skip score  
- **Note:** Live 404 on that slug; mockup teaser only. Locate CMS original or map to nearest live storm-damage PA post before scoring.

---

### D. Exclude (stale topic) — accessed bodies

| URL slug | Title | Date | Why stale |
|----------|-------|------|-----------|
| `are-you-prepared-for-hurricane-erika` | Are You Prepared For Hurricane Erika? | Aug 28, 2015 | Named dead storm event; “en route Monday” ephemeral |
| `homeowners-insurance-claim-reviewal-amidst-covid-19` | Homeowners Insurance Claim Reviewal Amidst COVID-19 | Apr 23, 2020 | Pandemic-era process; superseded conditions |
| `citizens-board-approves-2-sets-rate-hikes` | Citizens Board Approves 2 Sets of Rate Hikes | Aug 29, 2012 | One-off 2012 rate/news + Tropical Storm Isaac |
| `call-florida-public-adjuster-hurricane-irma-damage` | Should I Call… Hurricane Irma Damage? | Sep 7, 2017 | Named-storm event post (inventory) |
| `hurricane-irma-claims-assistance-from-a-west-palm-beach-public-adjuster` | Hurricane Irma Claims Assistance… | — | Named-storm event |
| `florida-public-adjuster-can-help-settle-hurricane-irma-insurance-claim` | …Settle Hurricane Irma… | — | Named-storm event |
| `how-do-i-find-a-public-adjuster-in-panama-city-for-hurricane-michael-claims` | …Hurricane Michael Claims | — | Named-storm event |
| `how-to-get-your-hurricane-ida-property-damage-paid-for` | Hurricane Ida Property Damage | — | Named-storm event |
| `hurricane-season-2013` | Hurricane Season 2013 | — | Dead season year |
| `the-fight-for-business-disruption-covid-19-claims-continues` | Business Disruption COVID-19 Claims | — | COVID BI claims era |
| `insurance-commissioners-asked-to-extend-deadlines-amidst-covid-19-pandemic` | Commissioners Extend Deadlines Amidst COVID | — | COVID deadline news |
| `citizens-corporate-scandal-exposed` | Citizens Corporate Scandal Exposed | Nov 27, 2012 | Old scandal news cycle |
| `citizens-calls-inspection-floridians-higher-premiums` | Citizens Calls It An Inspection… | Oct 3, 2012 | 2012 news |
| `citizens-insurance-has-once-again-left-its-homeowners-under-water` | Citizens… Under Water | Aug 6, 2014 | Dated carrier-news |
| `citizens-board-directors-violating-florida-law` | Citizens Board… Violating Florida Law | Oct 3, 2012 | Dated political news |
| `flood-insurance-increases-are-being-delayed-by-florida-congressmen` | Flood Insurance Increases Delayed… | — | Dated legislative news |
| `florida-approved-removal-150000-policies` | Florida Approved Removal 150000 Policies | — | Dated market-news |
| `floridas-hurricane-tax-comes-to-an-end` | Florida’s Hurricane Tax Comes To An End | — | Superseded fiscal event |
| `florida-regulators-move-policies-to-private-companies` | Regulators Move Policies… | — | Dated depopulation news |
| `florida-under-costliest-u-s-insurance-despite-10-year-storm-lull-2` | …10 Year Storm Lull | — | Dated market narrative |
| `news-4` | News 4 | — | Non-educational stub/news dump |

*(Full Exclude list + mockup hide/demote instructions: `BLOG-REVAMP-PLAN.md`.)*

---

### E. Incomplete fetch — skip score

| Source | Slug / path | Reason |
|--------|-------------|--------|
| Mockup only | `signs-of-water-damage-in-your-walls` (no `-0`) | Wrong slug vs live; mockup teaser |
| Mockup only | `top-five-tips-on-filing-a-mold-damage-claim` | Wrong slug; live is `…-0` |
| Mockup only | `when-does-homeowners-insurance-cover-roof-replacements` | Wrong slug; live is `…-0` |
| Mockup only | `what-happens-when-you-dont-call-a-public-adjuster` | Wrong slug; live is `…-0` |
| Mockup only | `a-florida-public-adjuster-can-help-after-storm-damage` | Live 404; teaser only |
| Content-dump stubs (~307) | most `blog__*.md` under 80 body words | CF-blocked / stub — skip score until CMS full paste |

**Inventory note:** ~353 posts in sitemap. This file scores **~37 with real bodies** from live fetch + substantial mockup paste. Remainder = incomplete fetch — skip score (do not treat stubs as rewrite targets).

---

## Scoring method notes

- Educational voice preserved: high scores for teaching (deductibles, burden of proof, EUO, CRN, RCV/ACV, denial language), not for hard-sell density.
- Freshness penalizes expired deadlines, single-storm news, COVID process, and season-specific NOAA years — not the underlying evergreen lesson.
- Conversion rewards subtle CTAs (consult / free inspection) without inventing settlement promises.
- Typos flagged only; **no new claims**.

