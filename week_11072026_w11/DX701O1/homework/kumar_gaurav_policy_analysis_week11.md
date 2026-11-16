# Policy Analysis — Week 11: Anticipating Critiques and Building the Rebuttal

**Author:** Kumar Gaurav
**Topic:** Commercial sale of precise location data and AI-driven inference of sensitive traits (anchor case: *FTC v. Kochava*)
**Builds on:** Week 8 (proposed solutions), Week 9 (policy levels and implementation), and Week 10 (ethical framework: duty-based primary, contract-based supporting)

---

## 1. The policy under critique (recap)

A three-tier policy: (1) a **federal floor statute** that bans the sale and transfer of precise geolocation data (within 1,750 feet) and of AI-derived inferences from it, requires data minimization, requires a warrant for government purchases, and authorizes **algorithmic disgorgement**; (2) **FTC rulemaking and enforcement** with a broker registry and national deletion portal, plus concurrent enforcement by state attorneys general; and (3) mandatory **organizational compliance programs** led by a named accountable executive.

A policy that bans a business model will be opposed by the people who run that business. The aim of this section is to state the strongest objections fairly, decide which ones actually threaten implementation, and show how the policy answers them — and where it should change.

---

## 2. Identifying the critiques

| # | Critique | Main source of the objection |
|---|---|---|
| C1 | **Economic harm:** the ban removes revenue from ad-supported apps, hurts small developers, and raises compliance costs | Data brokers, ad-tech firms, app developers |
| C2 | **First Amendment:** selling data is protected speech | Data brokers, industry trade groups |
| C3 | **Consent and autonomy:** a ban is paternalistic; users should be free to trade their data for services | Industry; libertarian commentators |
| C4 | **Overbreadth:** the ban blocks beneficial uses (public health, urban planning, research, fraud prevention) | Researchers, city planners, fraud and security vendors |
| C5 | **Law enforcement and national security:** a warrant requirement slows investigations | DOJ, intelligence agencies, police organizations |
| C6 | **Property and trade secrets:** datasets and models are the company's property; disgorgement destroys lawful investment | Data brokers, AI model developers |
| C7 | **Federalism and preemption:** a federal floor still leaves a patchwork of stronger state laws | National companies; supporters of ceiling preemption (SECURE Data Act) |
| C8 | **Enforceability and political feasibility:** the FTC lacks capacity, and Congress has not passed a privacy law in years | Policy analysts; skeptics across parties |
| C9 | **"De-identification is enough":** anonymized or hashed IDs already protect people | Data brokers (Kochava argued its data was not linked to names) |

---

## 3. Evaluating relevance: which critiques matter most for implementation?

I rank each critique by two questions: *Could it stop the policy from being enacted or upheld?* and *Does it point to a real design flaw?*

| Critique | Threat to enactment / survival | Reveals a real design flaw? | Priority |
|---|---|---|---|
| C2 First Amendment | **High** — a court can strike the statute after it passes | Partly — drafting must be careful | **1** |
| C1 Economic harm / business resistance | **High** — drives lobbying that has already stalled APRA | Partly — small firms need a transition | **2** |
| C5 Law enforcement | **High** — executive-branch opposition blocked the Fourth Amendment Is Not For Sale Act in the Senate | Partly — emergencies need an exception | **3** |
| C4 Overbreadth | Medium — weakens coalition support from researchers | **Yes** — a blanket ban would block legitimate aggregate uses | **4** |
| C6 Property / trade secrets | Medium — main argument against disgorgement in litigation | Partly — disgorgement needs a clear trigger | **5** |
| C3 Consent / autonomy | Medium — persuasive to the public | No — answered by the Week 10 framework | 6 |
| C9 De-identification | Low — empirical evidence contradicts it | No | 7 |
| C7 Preemption | Low–medium — a negotiating issue rather than a fatal flaw | No | 8 |
| C8 Enforceability / feasibility | Medium — a real risk, already addressed in Week 9 | No | 9 |

The rest of this section focuses on the five critiques with the highest priority, then answers the others briefly.

---

## 4. Rebuttals to the most significant critiques

### 4.1 C2 — "Selling data is protected speech"

**The critique at its strongest.** In *Sorrell v. IMS Health Inc.* (2011), the Supreme Court struck down a Vermont law that restricted the sale and use of doctors' prescribing records for marketing. The Court held that creating and spreading information is speech, and the law failed heightened scrutiny because it singled out particular speakers (pharmaceutical marketers) and a particular message. A data broker would argue that a location-data sale ban is the same kind of restriction.

**Rebuttal.**
- *Sorrell* struck the Vermont law because it was **content- and speaker-based**: the same data could still be sold to many other buyers for other purposes. The Court suggested that a more coherent privacy policy, allowing disclosure only in a few narrow and well-justified circumstances, would be a different case (*Sorrell v. IMS Health Inc.*, 2011). My policy is designed to be that kind of policy: the ban applies to **every seller and every buyer**, regardless of the message or purpose, with only narrow exceptions tied to the consumer's own request (navigation, ride-hailing, emergency services).
- The government interest is substantial and documented: stalking, exposure of clinic and shelter visitors, outing of LGBTQ+ people, and national-security risk. The DOJ Data Security Program already treats bulk precise geolocation as a national-security asset (U.S. Department of Justice, 2025), and the Office of the Director of National Intelligence (2022) acknowledged that commercially available data can reveal sensitive personal details that the government would otherwise need legal process to obtain.
- The statute should open with **legislative findings** documenting these harms, so a reviewing court sees the interest and the fit on the record.

**How the policy anticipates it (design change).** Draft the ban as a regulation of the *commercial transfer of sensitive personal information*, applied uniformly, rather than as a restriction on any particular use or message. Include a **severability clause** so that, if a court strikes one provision (for example, the inference ban), the sale ban, registry, and warrant requirement survive.

**Honest limitation.** No drafting can guarantee the outcome of First Amendment review. This is the largest legal risk in the policy, and the paper should say so.

### 4.2 C1 — "The ban will hurt the app economy and small businesses"

**The critique at its strongest.** Free apps are funded partly by selling or sharing data. Small developers depend on third-party SDKs that pay for location access. A ban could push them out, reduce competition, and leave only large platforms that can afford in-house advertising.

**Rebuttal.**
- **The ban targets transfer, not use.** A weather or navigation app can still collect location to deliver the service the user asked for. What it cannot do is sell the trail to a broker. Contextual advertising (ads based on the page or the local weather, not a person's history) remains lawful.
- **Major platforms already operate without this practice.** Apple's App Tracking Transparency (2021) requires apps to ask permission before tracking users across other companies' apps (Apple, 2021), and Google moved Maps Timeline data to storage on the user's device (Google, 2023). The ad-supported app market continued to operate after both changes. This shows that the location-sale model is a business choice, not a technical necessity.
- **The costs of the current system fall on the wrong people.** Stalking victims, clinic visitors, and shelter residents bear the harm, while firms keep the revenue. Under the duty-based framework from Week 10, revenue gained by treating people merely as a means is not a legitimate interest that the law must protect.
- **Uncertainty is already costly.** Firms today face FTC orders (Kochava, X-Mode, Gravy, Mobilewalla), Oregon's and Maryland's sale bans, Washington's private right of action, and California's deletion platform. A clear national floor replaces litigation risk with a compliance checklist.

**How the policy anticipates it (design changes).**
- **Phased effective dates:** large brokers within 12 months; app developers and small firms within 24 months.
- **Small-business threshold** for the heavier duties (named executive, annual audit), using a data-volume trigger similar to the DOJ "bulk" threshold, while the sale ban itself applies to everyone.
- **Safe harbor:** firms that register, follow the FTC sensitive-location list, and certify compliance face reduced penalties for a first good-faith violation (but no 45-day "cure period" that lets violators escape penalties, which I rejected in Week 8).

### 4.3 C5 — "A warrant requirement will slow law enforcement"

**The critique at its strongest.** Police and intelligence agencies buy commercial data to locate suspects, missing persons, and foreign threats quickly. A warrant requirement adds delay, and executive-branch opposition is the main reason the Fourth Amendment Is Not For Sale Act stalled in the Senate after passing the House 219–199 (U.S. House of Representatives, Office of the Clerk, 2024).

**Rebuttal.**
- In *Carpenter v. United States* (2018), the Supreme Court held that the government generally needs a warrant to obtain historical cell-site location records from a phone company. Buying the same kind of information from a broker is a way around that rule. The policy does not create a new limit; it closes a loophole in an existing one.
- Under the contract-based framework, people behind a veil of ignorance would not agree to a system where the government can buy what it cannot lawfully demand.
- Montana's SB 282 already applies a warrant-or-subpoena rule to state and local agencies (Electronic Frontier Foundation, 2025), which shows that the rule can operate in practice.

**How the policy anticipates it (design change).** Add an **exigent-circumstances exception** (imminent threat to life, missing child) with after-the-fact court review within a short deadline, and keep foreign-intelligence purchases under existing court-supervised procedures rather than open market purchasing.

### 4.4 C4 — "The ban blocks beneficial uses"

**The critique at its strongest.** During COVID-19, aggregated mobility data helped public health officials see whether distancing measures were working. City planners, transit agencies, and disaster responders use foot-traffic data. A blanket ban would cut off these uses.

**Rebuttal and design change.** This critique points to a **real gap** in my Week 9 design, and the policy should change:
- Add a **research and public-interest exception** for data that is **aggregated** and protected with **formal privacy guarantees** such as differential privacy (Dwork & Roth, 2014), provided to vetted researchers or public agencies under a data-use agreement that bans re-identification and resale.
- The model is Google's COVID-19 Community Mobility Reports, which published aggregated, differentially private trends rather than individual device trails (Aktay et al., 2020). This proves that the public-health benefit does not require selling individual-level location histories.
- The FTC unit would certify which aggregation methods qualify, so the exception keeps pace with new techniques.

This change makes the policy narrower and therefore also strengthens the First Amendment defense in Section 4.1 (better fit between the ban and the harm).

### 4.5 C6 — "Our datasets and models are our property; disgorgement destroys them"

**The critique at its strongest.** Brokers invest in collecting, cleaning, and modeling data. Their audience segments and trained models are trade secrets. Requiring their deletion destroys valuable property and discourages AI investment.

**Rebuttal — using the property theories from this week's reading (Tavani, 2024, Chapter 8).**
- **Labor theory (Locke).** Locke (1690/1980) argued that a person gains property by mixing their labor with something *unowned*, and only when "enough, and as good" is left for others. A broker does not mix labor with unowned material: it processes the movements of people who never agreed to the transfer. Labor applied to something taken without consent does not create a clean property claim.
- **Personality theory (Hegel).** Personality theory ties property to the expression of a person's will and identity. A person's daily movements — to a clinic, mosque, or shelter — are far closer to an expression of *their* personality than to the broker's. If this theory supports anyone's claim, it supports the data subject's.
- **Utilitarian theory.** Intellectual property rights are justified when they encourage socially valuable creation. Protecting a model whose main output is "likely visited an abortion clinic" does not serve that purpose.
- **Legal doctrine.** Raw facts, such as the fact that a device was at a location, are not protected by copyright (*Feist Publications, Inc. v. Rural Telephone Service Co.*, 1991). Trade-secret law protects a company against *misappropriation by competitors*; it does not shield the company from regulation of how it obtained the underlying data.
- **Precedent.** The FTC has already required deletion of models and algorithms built from improperly obtained data in cases such as Everalbum (2021) and WW/Kurbo (2022), and deletion of derived products in the location-data orders (Mintz, 2024).

**How the policy anticipates it (design change).** Disgorgement is triggered only by **data obtained in violation of the statute after its effective date**, or by a court or FTC finding of a violation. Firms that keep **data lineage records** (recommended in Week 9) can show which models are clean and retrain only the affected ones. This makes disgorgement predictable rather than open-ended.

---

## 5. Brief responses to the remaining critiques

- **C3 Consent and autonomy.** Consent is respected where it can be meaningful: a user can still share location with the service they chose. But a tap on "Allow" in a weather app cannot be informed consent to resale, inference, and sale of an "abortion clinic visitor" segment (Solove, 2013). As argued in Week 10, when meaningful consent is impossible, respecting persons requires a prohibition, not a better pop-up.
- **C9 "De-identification is enough."** Four spatio-temporal points uniquely identify about 95% of people in a mobility dataset (de Montjoye et al., 2013). A home location at night and a work location by day effectively *are* an identity. Hashed advertising IDs do not change this.
- **C7 Preemption.** National firms want one rule; consumer advocates want strong state laws. A **federal floor** gives firms a single minimum standard nationwide while keeping states free to go further, which preserves the speed shown by Oregon (about three months from introduction to signature). Ceiling preemption would erase the strongest protections in force today.
- **C8 Enforceability and feasibility.** Week 9 addressed capacity through registration-fee funding, a technologist team, test purchases, and annual certifications. On feasibility, the phased strategy does not depend on Congress acting first: companies and states move first, and their actions build pressure for a national floor.

---

## 6. Overcoming company objections: the business case

The task asks specifically how to persuade companies. The arguments differ by stakeholder:

| Company type | Likely objection | Argument to overcome it |
|---|---|---|
| **Data brokers** (Kochava, Gravy) | "This ends our business model." | The FTC orders already ban sensitive-location sales for the largest brokers one at a time; a uniform statute stops competitors from undercutting compliant firms. Aggregated, privacy-protected analytics under the research exception remain a lawful product. |
| **App developers** | "We lose SDK revenue." | Location can still be used to run the app; contextual ads remain. Phased deadlines and the small-business threshold reduce the cost of transition. Users who trust an app are more willing to grant the location permission it actually needs. |
| **Ad-tech firms** | "Targeting accuracy will drop." | Apple's tracking changes show that the industry can adapt. Location-based segments are now a legal liability under Oregon, Maryland, Washington, and FTC orders; a national rule turns uncertain risk into a known requirement. |
| **Cloud marketplaces** | "We are just the platform." | Kochava offered its sample dataset through a cloud marketplace. A certification requirement for sellers is a small cost that protects the marketplace's reputation and reduces its own enforcement risk. |
| **Large platforms** | "We already comply." | They benefit most from a uniform floor, because their competitors can no longer gain an edge by selling what responsible firms withhold. |

**Three cross-cutting arguments:**
1. **Predictability over litigation.** *Kochava* took about four years from complaint to proposed order. A statute replaces case-by-case "substantial injury" arguments with clear rules and safe harbors.
2. **A level playing field.** Voluntary codes such as the NAI Enhanced Standards failed because non-members like Kochava and X-Mode were not bound. A mandatory rule protects firms that already behave responsibly.
3. **Professional responsibility.** The ACM Code asks computing professionals to "avoid harm" and "respect privacy" (Association for Computing Machinery, 2018). The required compliance program gives data scientists and engineers a formal process and a whistleblower channel to act on those duties.

---

## 7. How the critiques strengthened the policy

| Change made this week | Critique it answers |
|---|---|
| Uniform, speaker-neutral drafting + legislative findings + severability clause | C2 First Amendment |
| Phased effective dates, small-business threshold, good-faith safe harbor (no cure period) | C1 Economic harm |
| Exigent-circumstances exception with prompt court review | C5 Law enforcement |
| Research/public-interest exception for aggregated, differentially private data | C4 Overbreadth |
| Disgorgement limited to post-enactment violations; lineage records to separate clean models | C6 Property / trade secrets |

## 8. Summary statement for the paper

> The strongest objections to this policy are legal (the First Amendment), economic (business resistance), and institutional (law enforcement access). The policy answers them by applying the ban uniformly to all sellers and buyers, documenting the government's interest in legislative findings, phasing in duties for smaller firms, and allowing emergency access with court review. Two critiques — overbreadth and the property claims against disgorgement — revealed real design gaps, which are addressed by a research exception for aggregated, differentially private data and a clearly defined disgorgement trigger. Under property theories, a broker's claim to datasets built from people's movements without consent is weak: labor applied to something taken without consent does not create a clean property right. Addressing these critiques makes the policy narrower, more defensible in court, and more persuasive to the companies it regulates.

---

## References

<!-- TODO: replace "et al." with the full author list from the arXiv page before submission (APA 7 lists up to 20 authors) -->
Aktay, A., et al. (2020). *Google COVID-19 community mobility reports: Anonymization process description (version 1.1)*. arXiv. https://arxiv.org/abs/2004.04145

Apple. (2021, April 26). *App Tracking Transparency* [Developer documentation]. https://developer.apple.com/documentation/apptrackingtransparency

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

*Carpenter v. United States*, 585 U.S. 296 (2018).

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports, 3*, Article 1376. https://doi.org/10.1038/srep01376

Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. https://doi.org/10.1561/0400000042

Electronic Frontier Foundation. (2025, May). *Montana becomes first state to close the law enforcement data broker loophole*. https://www.eff.org/deeplinks/2025/05/montana-becomes-first-state-close-law-enforcement-data-broker-loophole

*Feist Publications, Inc. v. Rural Telephone Service Co.*, 499 U.S. 340 (1991).

Google. (2023, December 12). *Updates to Location History and new controls coming soon to Maps*. The Keyword. https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/

Locke, J. (1980). *Second treatise of government* (C. B. Macpherson, Ed.). Hackett. (Original work published 1690)

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Office of the Director of National Intelligence. (2022). *Report to the Director of National Intelligence: Senior Advisory Group panel on commercially available information* (Declassified June 2023). https://www.dni.gov/files/ODNI/documents/assessments/ODNI-Declassified-Report-on-CAI-January2022.pdf

Solove, D. J. (2013). Privacy self-management and the consent dilemma. *Harvard Law Review, 126*(7), 1880–1903.

*Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011).

Tavani, H. T. (2024). *Ethics and technology: Controversies, questions, and strategies for ethical computing* (5th ed.). Wiley.

U.S. Department of Justice, National Security Division. (2025). *Data Security Program: Frequently asked questions*. https://www.justice.gov/nsd/media/1415006/dl

U.S. House of Representatives, Office of the Clerk. (2024, April 17). *Roll call 136, H.R. 4639, Fourth Amendment Is Not For Sale Act*. https://clerk.house.gov/Votes/2024136
