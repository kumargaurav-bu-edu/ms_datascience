# Policy Analysis — Week 8: Survey and Evaluation of Proposed Solutions

**Author:** Kumar Gaurav
**Topic:** Commercial sale of precise location data and AI-driven inference of sensitive traits (anchor case: *FTC v. Kochava*)
**Purpose of this draft:** Baseline research for the Policy Analysis paper (due end of Week 13). This section catalogs the solutions already proposed or enacted, evaluates each, and identifies elements to adopt, drop, or combine.

---

## Terminology used to find these proposals

Searching for these terms surfaced most of the sources below: *precise geolocation data*, *sensitive data*, *sensitive locations / sensitive points of interest*, *data broker registry*, *data minimization*, *geofencing*, *commercially available information (CAI)*, *data broker loophole*, *bulk sensitive personal data*, *algorithmic disgorgement*, and *universal opt-out / deletion mechanism*.

---

## A. Federal (United States)

### 1. FTC case-by-case enforcement under Section 5 (Kochava, X-Mode/Outlogic, Gravy Analytics/Venntel, Mobilewalla)

**What it is.** The FTC treats the sale of sensitive location data as an "unfair" practice. Its orders against X-Mode/Outlogic (FTC, 2024), Gravy Analytics/Venntel and Mobilewalla (finalized January 14, 2025), and the proposed Kochava order (FTC, 2026) ban sales tied to *sensitive locations* (clinics, places of worship, shelters, union offices, protests, military sites), require a "Sensitive Location Data Program," and in some cases require deletion of data and of products derived from it (Hunton Andrews Kurth, 2025).

| Strengths | Weaknesses |
|---|---|
| Already in force; no new statute needed | Binds only the named company; competitors with the same architecture continue (Yale Journal on Regulation, 2026) |
| Created a usable list of "sensitive locations" | Slow: *Kochava* took four years and an amended complaint |
| Introduced deletion of derived products, a form of algorithmic disgorgement (Mintz, 2024) | Depends on agency leadership and priorities; relies on the contested "substantial injury" test |

### 2. American Privacy Rights Act (APRA, 2024 discussion draft)

**What it is.** A bipartisan, bicameral comprehensive privacy bill with a strong *data minimization* standard, opt-in consent for transfers of sensitive data (including precise geolocation), a federal data broker registry, and a private right of action. The June 27, 2024 House Energy and Commerce markup was canceled amid disputes over preemption and the private right of action; the revised draft had also dropped its civil-rights and algorithm-assessment sections (IAPP, 2024).

| Strengths | Weaknesses |
|---|---|
| Data minimization attacks the problem at collection, not only sale | Never reached a floor vote; politically stalled |
| Sensitive-data opt-in plus a broker registry | Later drafts removed algorithmic impact assessments, the piece most relevant to AI inference |
| Private right of action gives victims a remedy | Preemption fights split states and Congress |

### 3. SECURE Data Act (H.R. 8413, introduced April 2026)

**What it is.** The current House Republican comprehensive bill. It treats geolocation as sensitive data (opt-in consent), creates an FTC-managed data broker registration, and is enforced by the FTC and state attorneys general with a 45-day cure period. It contains broad "relates to" preemption and no private right of action, data protection assessments, or universal opt-out requirement (IAPP, 2026; Reason Foundation, 2026).

| Strengths | Weaknesses |
|---|---|
| One national standard reduces the state patchwork | Ceiling preemption could erase stronger state laws (e.g., Oregon's sale ban, California's DROP) |
| Federal broker registry | Consent-based, not a ban; repeats notice-and-consent failure |
| Live vehicle in the current Congress | No private remedy; cure period weakens deterrence |

### 4. Fourth Amendment Is Not For Sale Act (H.R. 4639)

**What it is.** Requires law enforcement and intelligence agencies to obtain a court order before buying data from brokers that they would otherwise need a warrant to get. It passed the House 219–199 on April 17, 2024 but did not pass the Senate (U.S. House of Representatives, Office of the Clerk, 2024).

| Strengths | Weaknesses |
|---|---|
| Closes the *Carpenter* "data broker loophole" for government buyers | Does not touch commercial buyers (advertisers, stalkers, vigilantes) |
| Bipartisan coalition | Opposed by the executive branch on national-security grounds; stalled in the Senate |

### 5. DOJ Data Security Program (28 C.F.R. Part 202, implementing Executive Order 14117)

**What it is.** Effective April 8, 2025, it prohibits or restricts transfers of *bulk* U.S. sensitive personal data — including precise geolocation data on more than 1,000 U.S. devices — to six countries of concern (U.S. Department of Justice, 2025).

| Strengths | Weaknesses |
|---|---|
| Treats location data as a national-security asset; sets a precise numeric "bulk" threshold | Domestic sales to any U.S. buyer remain lawful |
| Due-diligence and audit duties create a compliance model | Protects national security, not individual privacy |

### 6. CFPB proposed rule on data brokers under the FCRA (withdrawn)

**What it is.** A December 2024 proposal to treat many data brokers as consumer reporting agencies under the Fair Credit Reporting Act. The CFPB withdrew it on May 15, 2025 (Consumer Financial Protection Bureau, 2025).

**Evaluation.** It used an existing statute, which was its strength, but its withdrawal shows that agency rulemaking without clear statutory authority can be reversed by the next administration — an argument for durable legislation.

---

## B. State level

### 7. Oregon HB 2008 (2025) — outright ban on selling precise geolocation

**What it is.** Amends the Oregon Consumer Privacy Act to prohibit *selling* data that locates a person or device within 1,750 feet, plus data of children under 16. Signed June 3, 2025; effective January 1, 2026 (Oregon Legislative Assembly, 2025).

| Strengths | Weaknesses |
|---|---|
| A ban, not a consent box — directly targets the Kochava business model | Protects only Oregon consumers |
| Clear technical threshold (1,750 ft) | "Sale" can be avoided through "sharing" or inferred audience segments; no model-level remedy |

### 8. Maryland Online Data Privacy Act (MODPA, effective October 1, 2025)

**What it is.** Prohibits the sale of all sensitive data, including precise geolocation, even with consent, and limits collection of sensitive data to what is "strictly necessary" (Office of the Attorney General of Maryland, n.d.).

| Strengths | Weaknesses |
|---|---|
| Strictest U.S. data minimization standard | AG-only enforcement; untested in court |
| Consent cannot override the sale ban | "Strictly necessary" may be argued narrowly or broadly |

### 9. Washington My Health My Data Act (2023)

**What it is.** Bans *geofencing* within 2,000 feet of in-person health care facilities to track visitors, collect health data, or target ads; treats location data that reveals health care seeking as health data; includes a private right of action (Washington State Legislature, 2023).

| Strengths | Weaknesses |
|---|---|
| Targets exactly the "clinic door" harm in *Kochava* | Health-only; does not cover places of worship or shelters |
| Private right of action | Broad definitions create compliance uncertainty |

### 10. California Delete Act (SB 362) and the DROP platform

**What it is.** Since January 1, 2026, Californians can send one deletion request to 600+ registered data brokers; brokers must process it every 45 days from August 1, 2026, including deleting inferences (California Privacy Protection Agency, 2026).

| Strengths | Weaknesses |
|---|---|
| Solves the "you can't opt out of a broker you've never heard of" problem | Still opt-out; the burden stays on consumers |
| Registry plus audits create visibility of the broker market | Brokers must match identifiers; MAID-only data may not match |

### 11. Montana SB 282 (2025) — state version of "Fourth Amendment Is Not For Sale"

**What it is.** The first state law barring state and local government from buying precise geolocation and other sensitive data without a warrant or investigative subpoena; improperly obtained data is inadmissible (Electronic Frontier Foundation, 2025).

**Evaluation.** Shows that the government-purchase loophole can be closed at state level, but, like the federal bill, it does nothing about private buyers.

### 12. Massachusetts Consumer Data Privacy Act (home state; pending)

**What it is.** The Senate passed S.2619 (40–0) in September 2025, banning the sale of all sensitive data. The House passed H.5479 (146–0) on June 4, 2026, with a blanket ban on selling precise geolocation data that protects residents *and visitors*, plus a private right of action against "large data holders." As of November 2026 a conference committee is reconciling the versions (Massachusetts House of Representatives, 2026; ODIPA, 2026).

| Strengths | Weaknesses |
|---|---|
| Covers visitors, protecting people who travel to Massachusetts for reproductive or gender-affirming care | Not yet law; could lapse if the session ends in January 2027 |
| Combines a geolocation sale ban with private enforcement for the largest holders | The House version allows other sensitive data to be sold with opt-in consent |

---

## C. Industry and international

### 13. NAI Voluntary Enhanced Standards for Precise Location Information (2022)

**What it is.** A self-regulatory code under which participating firms (Cuebiq, Foursquare, Precisely PlaceIQ) agree not to use or sell data tied to "Sensitive Points of Interest" and not to sell data to law enforcement without legal process; subject to annual NAI review (Network Advertising Initiative, 2022).

| Strengths | Weaknesses |
|---|---|
| Detailed, practical list of sensitive locations later mirrored by FTC orders | Voluntary — Kochava and X-Mode were not bound by it |
| Industry expertise; fast to adopt | No penalties beyond NAI expulsion or FTC deception claims |

### 14. EU GDPR special-category data (Norway's Grindr fine)

**What it is.** The GDPR treats data revealing sexual orientation, health, or religion as special-category data requiring explicit consent. Norway's regulator fined Grindr NOK 65 million (about €5.8 million) for sharing GPS location and advertising IDs with ad partners without valid consent; the Privacy Appeals Board upheld the fine in September 2023 (Datatilsynet, 2023).

| Strengths | Weaknesses |
|---|---|
| Recognizes that *inferred* membership in a group is sensitive | Consent-based; enforcement is slow and cross-border |
| Large, dissuasive fines | U.S. constitutional and political context differs |

---

## D. Synthesis: what to add, remove, and combine

**Recurring gaps across the proposals**

1. **Consent is the default safeguard** (SECURE Data Act, GDPR, House Massachusetts version), even though notice-and-consent is the failure shown in *Kochava*.
2. **Most measures target the sale of raw data, not the inferences.** Few address the AI models and audience segments that turn pings into "pregnant," "Muslim," or "in recovery." Only FTC orders reach derived products.
3. **Scope is fragmented** — one company (FTC), one state (Oregon, Maryland), one sector (Washington health), one buyer type (government-purchase bills), or one set of countries (DOJ rule).

**Elements to adopt**

- Oregon/Massachusetts House: a **categorical ban on selling precise geolocation**, rather than consent.
- Maryland: **strict data minimization** at collection.
- FTC orders and NAI: a **standard sensitive-location list** and a mandatory Sensitive Location Data Program.
- FTC: **algorithmic disgorgement** — deletion of models and segments built from unlawfully obtained data.
- California: a **federal broker registry plus a one-stop deletion mechanism**.
- Fourth Amendment Is Not For Sale / Montana: a **warrant requirement** for government purchases.
- DOJ rule: **clear numeric thresholds** and audit duties.
- Washington: a **private right of action**.

**Elements to remove or avoid**

- **Ceiling preemption** (SECURE Data Act) — use a federal floor that lets states go further.
- **Long cure periods** that let violators avoid penalties.
- **Reliance on voluntary codes** as the primary safeguard.

**Proposed combination (baseline for my policy):** a federal floor statute that (1) bans the sale and transfer of precise geolocation data and of inferences derived from it, (2) requires data minimization, (3) maintains an FTC data broker registry with a California-style deletion portal, (4) authorizes algorithmic disgorgement as a standard remedy, (5) requires a warrant for government purchases, and (6) is enforced by the FTC, state attorneys general, and a limited private right of action.

---

## References

California Privacy Protection Agency. (2026). *DROP for data brokers*. https://privacy.ca.gov/drop-for-data-brokers/

Consumer Financial Protection Bureau. (2025, May 15). Protecting Americans from harmful data broker practices (Regulation V); Withdrawal of proposed rule. *Federal Register*. https://www.federalregister.gov/documents/2025/05/15/2025-08644/protecting-americans-from-harmful-data-broker-practices-regulation-v-withdrawal-of-proposed-rule

Datatilsynet. (2023, October 2). *Record fine in the Grindr case confirmed*. https://www.datatilsynet.no/en/news/news-2023/record-fine-grindr-confirmed/

Electronic Frontier Foundation. (2025, May). *Montana becomes first state to close the law enforcement data broker loophole*. https://www.eff.org/deeplinks/2025/05/montana-becomes-first-state-close-law-enforcement-data-broker-loophole

Federal Trade Commission. (2024, January 9). *FTC order prohibits data broker X-Mode Social and Outlogic from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data

Federal Trade Commission. (2026, May 4). *FTC to ban Kochava and subsidiary from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data

Hunton Andrews Kurth. (2025, January). *FTC finalizes orders against data brokers over sensitive location data*. https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-finalizes-orders-against-data-brokers-over-sensitive-location-data

IAPP. (2024, June 27). *American Privacy Rights Act markup canceled, next US House steps uncertain*. https://iapp.org/news/a/american-privacy-rights-act-markup-canceled-next-us-house-steps-uncertain

IAPP. (2026, April). *SECURE Data Act: Analysis of the new federal privacy bill*. https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill

Massachusetts House of Representatives. (2026, June 4). *House passes Massachusetts Consumer Data Privacy Act* [Press release]. https://malegislature.gov/PressRoom/Detail?pressReleaseId=1396

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Network Advertising Initiative. (2022, June 22). *Leading companies commit to privacy-first NAI Enhanced Standards for precise location information*. https://thenai.org/press/leading-companies-commit-to-privacy-first-nai-enhanced-standards-for-precise-location-information/

Office of the Attorney General of Maryland. (n.d.). *Data privacy in Maryland*. https://oag.maryland.gov/resources-info/Pages/data-privacy.aspx

ODIPA. (2026, October). *Privacy digest, October 2026 edition*. https://www.odipa.org/research-releases/privacy-digest-2026-10/

Oregon Legislative Assembly. (2025). *House Bill 2008 (Enrolled)*. https://olis.oregonlegislature.gov/liz/2025R1/Downloads/MeasureDocument/hb2008/Enrolled

Reason Foundation. (2026). *The SECURE Data Act could reduce compliance costs and improve consistency*. https://reason.org/backgrounder/the-secure-data-act-could-reduce-compliance-costs-and-improve-consistency/

U.S. Department of Justice, National Security Division. (2025). *Data Security Program: Frequently asked questions*. https://www.justice.gov/nsd/media/1415006/dl

U.S. House of Representatives, Office of the Clerk. (2024, April 17). *Roll call 136, H.R. 4639, Fourth Amendment Is Not For Sale Act*. https://clerk.house.gov/Votes/2024136

Washington State Legislature. (2023). *Chapter 19.373 RCW: Washington My Health My Data Act*. https://app.leg.wa.gov/rcw/default.aspx?cite=19.373&full=true

Yale Journal on Regulation. (2026, July 14). *FTC's Kochava settlement advances data privacy enforcement–but leaves critical gaps in protecting consumers*. https://www.yalejreg.com/nc/ftcs-kochava-settlement-advances-data-privacy-enforcement-but-leaves-critical-gaps-in-protecting-consumers/
