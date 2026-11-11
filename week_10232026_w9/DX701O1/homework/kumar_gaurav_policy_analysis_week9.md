# Policy Analysis — Week 9: Policy Level, Structure, and Implementation

**Author:** Kumar Gaurav
**Topic:** Commercial sale of precise location data and AI-driven inference of sensitive traits (anchor case: *FTC v. Kochava*)
**Builds on:** Week 8 survey of proposed solutions (`week_10162026_w8/DX701O1/homework/kumar_gaurav_policy_analysis_week8.md`)

---

## 1. At what level were the existing policies proposed?

| Level | Policies (from Week 8) | Status |
|---|---|---|
| **National — legislative** | APRA (2024); SECURE Data Act, H.R. 8413 (2026); Fourth Amendment Is Not For Sale Act, H.R. 4639 | None enacted |
| **National — regulatory/executive** | FTC Section 5 orders (Kochava, X-Mode/Outlogic, Gravy/Venntel, Mobilewalla); DOJ Data Security Program (E.O. 14117); CFPB data broker rule | FTC orders and DOJ rule in force; CFPB rule withdrawn May 2025 |
| **State** | Oregon HB 2008; Maryland MODPA; Washington My Health My Data Act; California Delete Act/DROP; Montana SB 282; Massachusetts Consumer Data Privacy Act | All in force except Massachusetts (in conference committee) |
| **Business/organizational** | NAI Voluntary Enhanced Standards (2022); company Sensitive Location Data Programs required by FTC orders | Voluntary or order-imposed on single firms |
| **International** | EU GDPR special-category data (Norway's Grindr fine) | In force |

**Pattern.** The strongest *substantive* protections (outright sale bans) exist at the **state** level. The broadest *reach* exists at the **national regulatory** level but only one company at a time. The **national legislative** level, where a comprehensive fix would sit, has produced no law since at least 2022. Business-level rules exist but are voluntary.

---

## 2. What type of policy would be most effective?

**A federal statute that sets a floor, not a ceiling.** Location data crosses state lines by design: an app in Ohio, an SDK vendor in Idaho, a cloud marketplace in Washington, and a buyer anywhere. A state law protects only its own residents (Massachusetts' House bill extends to visitors, which is a partial fix). Only Congress can regulate the whole supply chain — collection, sale, inference, and purchase — at once.

The statute should be **prohibition-based rather than consent-based**: ban the sale and transfer of precise geolocation data (defined, like Oregon, as within 1,750 feet) and of inferences derived from it, with narrow exceptions for services the consumer directly requests (navigation, ride-hailing, emergency services).

---

## 3. Are multiple levels needed? Yes — three tiers

| Tier | Instrument | Role |
|---|---|---|
| **1. National law** | *Location Privacy and Algorithmic Accountability Act* (working title) | Sale/transfer ban; data minimization; warrant requirement for government purchases; algorithmic disgorgement as a standard remedy; federal floor preemption |
| **2. National regulator** | FTC (new Location Data and Algorithmic Accountability unit within the Bureau of Consumer Protection) | Rulemaking for the sensitive-location list and technical thresholds; broker registry and national deletion portal; audits and enforcement |
| **2b. State enforcement** | State attorneys general (e.g., Massachusetts AG) | Concurrent enforcement; freedom to legislate stronger protections above the federal floor |
| **3. Organizational** | Required compliance programs at brokers, SDK vendors, app developers, and cloud marketplaces | Day-to-day implementation: data inventories, sensitive-location suppression, impact assessments, named accountable officer |

**Why a regulator alongside the law?** The *Kochava* litigation shows that a general "unfairness" statute forces the FTC to prove substantial injury company by company. An explicit statutory ban turns each case into a compliance question ("did you sell location data?") rather than a four-year argument about harm. The regulator is still needed to keep technical definitions current as AI inference techniques change.

**Why keep states in?** Oregon moved from bill introduction (February 27, 2025) to signature (June 3, 2025) in about three months (The Oregonian, 2025). States act as fast laboratories; ceiling preemption, as in the SECURE Data Act, would remove that safety valve (IAPP, 2026).

---

## 4. Would I advise companies to adopt a particular policy?

Yes — companies should not wait for Congress. I would recommend that any company that collects or handles location data adopt these steps now:

1. **Adopt the NAI Enhanced Standards' sensitive points-of-interest list as a minimum** and suppress any data linked to those locations (Network Advertising Initiative, 2022).
2. **Vet and contractually restrict SDK partners.** App developers should audit every third-party SDK that requests location permission and prohibit downstream resale.
3. **Cloud marketplaces** (the channel through which Kochava's free sample was offered) should require sellers of location data to certify compliance with the FTC sensitive-location orders.
4. **Run an algorithmic impact assessment** before training any model on location data and document the inferences the model can produce.
5. **Plan for disgorgement:** keep data lineage records so that models trained on tainted data can be identified and retrained or deleted.

The business case is that the FTC orders already impose these duties on Gravy, Mobilewalla, and Kochava, and Oregon, Maryland, and (likely) Massachusetts make the sale itself unlawful. Voluntary adoption lowers future compliance cost and legal risk.

---

## 5. Implementation: what is needed to make it effective?

### Government: deploying resources and monitoring

- **Dedicated staff and technologists.** Enforcement of location-data cases requires engineers who can audit SDK traffic and model outputs, not only lawyers. The statute should fund a technologist team inside the FTC unit.
- **Self-funding through registration fees.** California's DROP is financed by data broker registration fees and now processes deletion requests for more than 600 registered brokers (California Privacy Protection Agency, 2026). A federal registry can use the same model.
- **Active monitoring, not complaint-driven enforcement:**
  - *Test purchases* — the regulator buys sample datasets, as journalists did with SafeGraph data (Cox, 2022), to check whether sensitive-location data is still being sold.
  - *SDK traffic audits* on popular apps.
  - *Annual compliance certifications* signed by a senior officer, similar to the DOJ Data Security Program's audit and reporting duties (U.S. Department of Justice, 2025).
- **Public metrics.** Publish yearly figures: registered brokers, deletion requests processed, audits run, and penalties imposed, so Congress can judge whether the policy works.

### Business: organizational structure and leadership

- **Named accountable executive.** The FTC's Mobilewalla order requires a senior officer, such as a Chief Privacy Officer or Chief Compliance Officer, to run the Sensitive Location Data Program (Federal Trade Commission, 2025). My policy would make this mandatory for every registered broker.
- **Board-level oversight** for firms above a data-volume threshold (for example, more than 1,000 U.S. devices, matching the DOJ "bulk" threshold).
- **Cross-functional privacy review.** Data science, engineering, legal, and product must sign off before a new location-derived audience segment is launched — putting the "avoid harm" and "respect privacy" duties of the ACM Code into a formal process (Association for Computing Machinery, 2018).
- **Whistleblower channel.** Engineers who work on products like Kochava's Database Graph need a protected way to raise concerns.

---

## 6. Time and effort required

| Tier | Realistic timeline | Evidence |
|---|---|---|
| Company policy | Weeks to months | Internal policies need only executive approval and an engineering release cycle |
| State law | Months to two years | Oregon HB 2008: about 3 months; Massachusetts: Senate passed September 2025, House June 2026, still in conference (ODIPA, 2026) |
| FTC enforcement | Years per company | *Kochava*: filed August 2022, proposed order May 2026 |
| Federal law | Multi-year and uncertain | APRA markup canceled June 2024 (IAPP, 2024); SECURE Data Act introduced April 2026 and still in committee |
| Federal rulemaking after enactment | 1–2 years | SECURE Data Act provisions would take effect one to two years after enactment (IAPP, 2026) |

**How leadership structure affects speed.** Federal law needs both chambers, committee chairs, and party leadership to agree; APRA collapsed when House leadership opposed the committee chair (IAPP, 2024). A company with a single CEO and board can act fastest. States sit in between.

**Phased strategy.** Because the tiers move at different speeds, the policy should be phased:

1. **Immediately:** companies adopt the voluntary program; Massachusetts enacts the House geolocation sale ban.
2. **Within two years:** more states follow the Oregon/Maryland model, creating pressure for national uniformity.
3. **Medium term:** Congress passes the federal floor statute, and the FTC issues implementing rules and stands up the registry and portal.

---

## References

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

California Privacy Protection Agency. (2026). *DROP for data brokers*. https://privacy.ca.gov/drop-for-data-brokers/

Cox, J. (2022, May 3). Data broker is selling location data of people who visit abortion clinics. *Vice*. https://www.vice.com/en/article/location-data-abortion-clinics-safegraph-planned-parenthood/

Federal Trade Commission. (2025). *Decision and order: In the matter of Mobilewalla, Inc.* https://search.ftc.gov/system/files/ftc_gov/pdf/Mobilewalla-D%26O.pdf

IAPP. (2024, June 27). *American Privacy Rights Act markup canceled, next US House steps uncertain*. https://iapp.org/news/a/american-privacy-rights-act-markup-canceled-next-us-house-steps-uncertain

IAPP. (2026, April). *SECURE Data Act: Analysis of the new federal privacy bill*. https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill

Network Advertising Initiative. (2022, June 22). *Leading companies commit to privacy-first NAI Enhanced Standards for precise location information*. https://thenai.org/press/leading-companies-commit-to-privacy-first-nai-enhanced-standards-for-precise-location-information/

ODIPA. (2026, October). *Privacy digest, October 2026 edition*. https://www.odipa.org/research-releases/privacy-digest-2026-10/

The Oregonian. (2025). *HB 2008: Oregon Legislature bill tracker*. https://gov.oregonlive.com/bill/2025/HB2008/

U.S. Department of Justice, National Security Division. (2025). *Data Security Program: Frequently asked questions*. https://www.justice.gov/nsd/media/1415006/dl
