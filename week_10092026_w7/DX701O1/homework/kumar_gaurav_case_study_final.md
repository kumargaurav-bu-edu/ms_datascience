# OMDS Module 5 — Case Study

**Author:** Kumar Gaurav

**Case study name:** Tracked to the Clinic Door: *FTC v. Kochava* and the Commercial Sale of Sensitive Location Data

**Topic area:** Data privacy and AI-driven surveillance — commercial data brokers, geolocation tracking, and algorithmic inference of sensitive personal information

---

## Summary of the Case

In August 2022, the Federal Trade Commission (FTC) sued Kochava, Inc., an Idaho-based data broker, for selling the precise locations of millions of smartphone users without their knowledge (Federal Trade Commission [FTC], 2022). Kochava collected location signals through software embedded in ordinary mobile apps and sold them as timestamped GPS coordinates tied to Mobile Advertising IDs (MAIDs), the unique codes assigned to each phone. A free sample of this data, offered to anyone on a public cloud marketplace, covered more than 61 million devices and could trace people to reproductive health clinics, places of worship, domestic violence shelters, and addiction recovery centers (Electronic Frontier Foundation [EFF], 2026). Because a phone that rests at the same address every night reveals its owner's home, this "anonymous" data could easily identify individuals.

The case centers on two main actors: Kochava, which built and sold the data, and the FTC, which argued that the sale was an unfair practice under Section 5 of the FTC Act. Other stakeholders include tracked users and their families, app developers who embedded Kochava's software, buyers who purchased the data, and lawmakers who have not passed a federal privacy law.

The legal battle was unusual. Kochava sued the FTC first, and in May 2023 the court dismissed the agency's original complaint for failing to show substantial injury. The amended complaint alleged that Kochava also linked devices to names, addresses, and phone numbers and sold inferred audience segments based on sensitive traits (FTC, 2026). In February 2024, the court denied Kochava's motion to dismiss, finding the FTC plausibly alleged substantial injury (Yale Journal on Regulation, 2026). In May 2026 the parties filed a proposed stipulated order barring Kochava and its subsidiary from selling sensitive location data; critics argue it leaves the broader industry untouched (Sigma Law Group, 2026).

---

## Stakeholders

- **Stakeholder 1 — Tracked users and their families.** Users behind the 61 million devices in Kochava's sample never knew a broker was selling their movements (EFF, 2026). *Impact:* for a clinic visitor after *Dobbs v. Jackson Women's Health Organization* (2022), a shelter resident, or worshipper, the data creates potential exposure to prosecution, stalking, or violence.

- **Stakeholder 2 — Defendant: Kochava, Inc. and its leadership.** Founder and CEO Charles Manning's company and its subsidiary, Collective Data Solutions, collected, linked, and sold the data, arguing that they followed industry norms and caused no concrete injury (FTC, 2026). *Impact:* the proposed order would end its sensitive-location business after four years of litigation.

- **Stakeholder 3 — Technical professionals: Kochava's data scientists and engineers.** They worked on the data products described in the FTC complaint — the Database Graph, App Graph, and audience segments. *Impact:* though not decision-makers, they faced a professional dilemma under the ACM Code of Ethics, which requires computing professionals to "avoid harm" (1.2) and "respect privacy" (1.6) (Association for Computing Machinery [ACM], 2018).

- **Stakeholder 4 — Enablers: app developers, data buyers, and Amazon Web Services (AWS).** Developers embedded Kochava's software for revenue, unvetted buyers purchased the feed, and AWS Marketplace hosted the free sample (FTC, 2022). *Impact:* each faces reputational and legal pressure to audit location data flows.

- **Stakeholder 5 — Authorities: the FTC, the federal court, and Congress.** The FTC, under then-Chair Lina Khan and Consumer Protection Director Samuel Levine, filed suit. Judge B. Lynn Winmill (District of Idaho) first dismissed it, then in February 2024 found the FTC plausibly alleged substantial injury (Yale Journal on Regulation, 2026). *Impact:* the ruling strengthened FTC authority to challenge privacy harms, while Congress, lacking a federal privacy law, remains the absent stakeholder whose inaction forced a four-year lawsuit.

---

## Connection to Broader Issues

*Kochava* illustrates four broader problems in technology ethics. First, it exposes the myth of anonymization. De Montjoye et al. (2013) showed that just four spatio-temporal points are enough to uniquely identify 95% of individuals in a mobility dataset, so removing names from location data offers little real protection. Second, it shows how inference turns ordinary data into sensitive data. A single GPS ping is mundane, but inferential pipelines like the Database Graph and audience segments described in Kochava's complaint can cluster millions of pings to infer pregnancy, religion, sexuality, or addiction. This is the "behavioral surplus" that Zuboff (2019) places at the center of surveillance capitalism.

Third, the case reveals the failure of notice-and-consent. Users who grant a weather or game app location access cannot reasonably anticipate that the data will be resold, profiled, and offered to unknown buyers. Fourth, it highlights a constitutional gap. In *Carpenter v. United States* (2018), the Supreme Court required a warrant for police to obtain historical cell-site records, yet government agencies can still buy comparable data from commercial brokers without one.

Related cases show this is a systemic pattern rather than one bad actor. In 2021, a Catholic newsletter used commercially purchased Grindr location data to out a senior priest, who then resigned (Boorstein et al., 2021). In 2022, reporters bought a week of data from SafeGraph showing where visitors to Planned Parenthood locations had come from and gone afterward (Cox, 2022). In 2024, the FTC banned X-Mode Social/Outlogic from selling sensitive location data after finding that it had sold data to government contractors (FTC, 2024; Sherman, 2024). Earlier, a *New York Times* investigation had re-identified individuals from supposedly anonymous app data (Valentino-DeVries et al., 2018). Together, these cases suggest that AI capabilities have outpaced existing privacy law across the industry.

---

## Importance

This case deserves resolution because the harm is ongoing, scalable, and falls hardest on people with the most to lose. Kochava's free sample alone covered more than 61 million devices (EFF, 2026), and Kochava is only one of many brokers operating under similar business models. After *Dobbs*, location data showing a visit to a clinic can carry legal consequences, and data revealing a shelter's address can put a survivor's life at risk. These are not abstract privacy concerns; they are threats to physical safety and civil liberties.

The case also shows that enforcement after the fact is slow and incomplete. The FTC spent four years on one company and secured a proposed order that binds only Kochava, leaving competitors with the same data-flow architecture free to continue (Yale Journal on Regulation, 2026). Alternatives — state laws like CCPA/CPRA, industry self-regulation, and consumer tools — have proven insufficient: they create inconsistent protection, lack enforcement teeth, and push the burden onto users who cannot foresee downstream resale. Clear federal rules — defining precise geolocation as sensitive data and requiring algorithmic disgorgement of models trained on unlawfully obtained data (Mintz, 2024) — would protect consumers before harm occurs rather than years afterward.

---

## References

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

Boorstein, M., Iati, M., & Shin, A. (2021, July 21). Top U.S. Catholic Church official resigns after cellphone data used to track him on Grindr and to gay bars. *The Washington Post*. https://www.washingtonpost.com/religion/2021/07/20/bishop-misconduct-resign-burrill/

*Carpenter v. United States*, 585 U.S. 296 (2018).

Cox, J. (2022, May 3). Data broker is selling location data of people who visit abortion clinics. *Vice*. https://www.vice.com/en/article/location-data-abortion-clinics-safegraph-planned-parenthood/

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports, 3*, Article 1376. https://doi.org/10.1038/srep01376

*Dobbs v. Jackson Women's Health Organization*, 597 U.S. 215 (2022).

Electronic Frontier Foundation. (2026, August 4). *Location data brokers*. https://www.eff.org/issues/location-data-brokers

Federal Trade Commission. (2022, August 29). *FTC sues Kochava for selling data that tracks people at reproductive health clinics, places of worship, and other sensitive locations*. https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other

Federal Trade Commission. (2024, January 9). *FTC order prohibits data broker X-Mode Social and Outlogic from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data

Federal Trade Commission. (2026, May 4). *FTC to ban Kochava and subsidiary from selling sensitive location data to settle charges they sold location data linked to millions of mobile devices*. https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Sherman, J. (2024, March 12). *Location data broker X-Mode and the FTC's unprecedented settlement*. Lawfare. https://www.lawfaremedia.org/article/location-data-broker-x-mode-and-the-ftc-s-unprecedented-settlement

Sigma Law Group. (2026, June 28). *The FTC's Kochava settlement and the new rules for location data*. https://sigmalawgroup.com/blog/2026-06-28-ftc-kochava-location-data/

Valentino-DeVries, J., Singer, N., Keller, M. H., & Krolik, A. (2018, December 10). Your apps know where you were last night, and they're not keeping it secret. *The New York Times*. https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html

Yale Journal on Regulation. (2026, July 14). *FTC's Kochava settlement advances data privacy enforcement–but leaves critical gaps in protecting consumers*. https://www.yalejreg.com/nc/ftcs-kochava-settlement-advances-data-privacy-enforcement-but-leaves-critical-gaps-in-protecting-consumers/

Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.

---

## AI Appendix

### (a) Full exchanges with AI tools

Full conversation logs are available at the links below. As my instructor recommended in the proposal feedback, I am providing links instead of pasted transcripts.

- **ChatGPT (review and fact-check of the final draft, October 25, 2026):** https://chatgpt.com/c/6adda887-757c-83ea-b28c-1ff9bf49291b

The key prompts I gave ChatGPT, in order, with a summary of each response:

| # | My prompt (summary) | What ChatGPT produced |
|---|---|---|
| 1 | Shared my proposal, instructor feedback, the rubric, and the template, and asked which case to focus on. | Compared *Kochava* and *Outlogic* and recommended *Kochava* for its deeper source base and four-year legal arc. |
| 2 | Asked for a Markdown draft of the four required sections within the rubric word ranges. | Drafted the summary, stakeholders, broader issues, and importance sections with APA in-text citations and a references list. |
| 3 | Shared the Week 5 task and asked to tighten the stakeholder section. | Reorganized stakeholders by role (victim, perpetrator, employees, enablers, authorities) and linked the employee stakeholder to the ACM Code of Ethics. |
| 4 | Shared the Week 6 task and asked to improve the summary using the Cambridge Analytica example. | Rewrote the summary to name the two central actors, define MAIDs for a non-expert reader, and present the legal timeline in order. |
| 5 | Asked for a final review of the near-final draft for factual and framing issues before submission. | Flagged legal-precision issues (proposed stipulated order vs. final ban, the motion-to-dismiss standard), suggested neutral labels for stakeholders, and recommended a Kochava-specific hook for the AI-inference discussion. |

### (b) Tools used

- **ChatGPT** (OpenAI large language model): used to review the near-final draft and flag factual and framing issues before submission.

### (c) How and why AI was used

1. **Case selection.** The AI compared the two examples from my proposal against the Week 4 requirement to choose the case with "more sources and enough complexity." *Kochava* won because of its four-year litigation history: a pre-emptive lawsuit, a dismissal, an amended complaint, and a settlement.
2. **Structure and word budgeting.** The AI mapped each template section to its rubric word range and checked the counts after every revision, which addressed the Writing Quality criterion.
3. **Research leads.** The AI suggested related cases (Grindr, SafeGraph, X-Mode/Outlogic, the *New York Times* investigation) and scholarly grounding (de Montjoye et al., 2013; Zuboff, 2019; *Carpenter*). I then checked each one against its original source.

### (d) Reflection on impact

Using AI saved me significant time organizing a complicated four-year legal history and finding related cases I would not have known to look for. It also made the word limits much easier to manage. However, the AI could not be trusted on its own for specific facts. Names, dates, and the 61 million device figure all had to be checked against FTC press releases and the court record. In one case, the AI attached a claim to a source that did not actually support it, which taught me that a citation that looks plausible is not the same as one that has been verified. Working through the stakeholder section changed how I view the case. I first saw it as a dispute between a company and a regulator, but the most serious harm falls on vulnerable individuals who are not even named in the record. I also noticed the irony of using an AI system to critique AI-driven inference, which made me more careful about what personal information I share with AI tools. Overall, AI worked best as a research assistant and editor, while the analysis, judgment, and responsibility for accuracy remained mine.

**Verification statement:** I checked every factual claim, date, name, and statistic against the cited sources and confirmed that every URL resolves before submitting.
