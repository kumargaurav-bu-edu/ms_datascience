# OMDS Module 5 — Case Study

**Author:** Kumar Gaurav

**Case study name:** Tracked to the Clinic Door: *FTC v. Kochava* and the Commercial Sale of Sensitive Location Data

**Topic area:** Data privacy and AI-driven surveillance — commercial data brokers, geolocation tracking, and algorithmic inference of sensitive personal information

---

## Summary of the Case

In August 2022, the Federal Trade Commission (FTC) sued Kochava, Inc., an Idaho-based data broker, alleging that its sale of precise geolocation data was an unfair practice under Section 5 of the FTC Act (Federal Trade Commission [FTC], 2026). Kochava gathered location signals through software embedded in ordinary mobile apps and sold them as timestamped latitude–longitude coordinates tied to Mobile Advertising IDs (MAIDs). The FTC showed that a free data sample, available to anyone on a public cloud marketplace, covered more than 61 million unique devices and could trace people to reproductive health clinics, places of worship, domestic violence shelters, and addiction recovery centers (Electronic Frontier Foundation [EFF], 2026). Because a device that rests at the same address every night reveals its owner's home, the data were "anonymous" in name only.

The case took an unusual path. Kochava sued the FTC first, and in May 2023 the court dismissed the agency's original complaint for failing to show substantial consumer injury, while allowing an amendment. The amended complaint went further, alleging that Kochava linked MAIDs to names, addresses, emails, and phone numbers and used the data to build inferred audience segments based on sensitive characteristics (FTC, 2026). In February 2024, the court denied Kochava's motion to dismiss, accepting that the invasion of privacy itself can be a substantial injury, which was a significant shift in how digital "harm" is defined (Yale Journal on Regulation, 2026).

After nearly four years of litigation, the parties settled in May 2026. The order bans Kochava and its subsidiary from selling sensitive location data and requires safeguards around the data it retains (FTC, 2026; Sigma Law Group, 2026). Commentators note, however, that the settlement leaves broader industry practices largely untouched (Yale Journal on Regulation, 2026).

---

## Stakeholders

- **Stakeholder 1 — Victims: tracked smartphone users and their families.** The victims are the ordinary app users behind the 61 million devices in Kochava's free sample, who never knew a broker held their movements (EFF, 2026). None were named, which is part of the harm: a clinic visitor after *Dobbs v. Jackson Women's Health Organization* (2022), a shelter resident, or a worshipper at a mosque could be traced home, exposing them and their families to prosecution, stalking, or violence.

- **Stakeholder 2 — Perpetrator: Kochava, Inc. and its leadership.** Kochava, led by founder and CEO Charles Manning, and its subsidiary Collective Data Solutions collected, linked, and sold the data (FTC, 2026). The company maintained that it followed industry norms and caused no concrete injury. The settlement ended its sensitive-location business.

- **Stakeholder 3 — Company employees: Kochava's data scientists and engineers.** These staff built the device-linking graphs and inferred audience segments. Though not decision-makers, they are bound by the ACM Code of Ethics to "avoid harm" (1.2) and "respect privacy" (1.6), raising the question of whether they should have objected (Association for Computing Machinery [ACM], 2018).

- **Stakeholder 4 — Enablers: app developers, data buyers, and Amazon Web Services (AWS).** Developers embedded Kochava's software for revenue, often unaware where the data went. Unvetted buyers could purchase the feed, and AWS Marketplace hosted the free sample (Internet Policy Review, 2022).

- **Stakeholder 5 — Authorities: the FTC, the federal court, and Congress.** The FTC, under Chair Lina Khan and Consumer Protection Director Samuel Levine, filed suit. Judge B. Lynn Winmill (District of Idaho) first dismissed it, then ruled in 2024 that privacy invasion can be substantial injury (Yale Journal on Regulation, 2026). Congress, lacking a federal privacy law, is the absent stakeholder whose inaction forced a four-year lawsuit.

---

## Connection to Broader Issues

*Kochava* illustrates four broader problems in technology ethics. First, it exposes the myth of anonymization. De Montjoye et al. (2013) showed that just four spatio-temporal points are enough to uniquely identify 95% of individuals in a mobility dataset, so removing names from location data offers little real protection. Second, it shows how inference turns ordinary data into sensitive data. A single GPS ping is mundane, but machine learning models that cluster millions of pings can infer pregnancy, religion, sexuality, or addiction. This is the "behavioral surplus" that Zuboff (2019) places at the center of surveillance capitalism.

Third, the case reveals the failure of notice-and-consent. Users who grant a weather or game app location access cannot reasonably anticipate that the data will be resold, profiled, and offered to unknown buyers. Fourth, it highlights a constitutional gap. In *Carpenter v. United States* (2018), the Supreme Court required a warrant for police to obtain historical cell-site records, yet government agencies can still buy comparable data from commercial brokers without one.

Related cases show this is a systemic pattern rather than one bad actor. In 2021, a Catholic newsletter used commercially purchased Grindr location data to out a senior priest, who then resigned (Boorstein et al., 2021). In 2022, reporters bought a week of data from SafeGraph showing where visitors to Planned Parenthood locations had come from and gone afterward (Cox, 2022). In 2024, the FTC banned X-Mode Social/Outlogic from selling sensitive location data after finding that it had sold data to government contractors (FTC, 2024; Sherman, 2024). Earlier, a *New York Times* investigation had re-identified individuals from supposedly anonymous app data (Valentino-DeVries et al., 2018). Together, these cases show that AI capabilities have outpaced privacy law across the whole industry.

---

## Importance

This case deserves resolution because the harm it reveals is ongoing, scalable, and falls hardest on people with the most to lose. Kochava's free sample alone covered more than 61 million devices (EFF, 2026), and Kochava is only one of many brokers operating under similar business models. After *Dobbs*, location data showing a visit to a clinic can carry legal consequences, and data revealing a shelter's address can put a survivor's life at risk. These are not abstract privacy concerns; they are threats to physical safety and civil liberties.

The case also shows that enforcement after the fact is slow and incomplete. The FTC spent nearly four years on a single company and secured a settlement that commentators still consider to have gaps (Yale Journal on Regulation, 2026). Alternatives — state laws like CCPA/CPRA, industry self-regulation, and consumer privacy tools — have proven insufficient, because they create inconsistent protection, lack enforcement teeth against profit incentives, and push the burden onto users who cannot foresee downstream resale. Clear federal rules, such as defining precise geolocation as sensitive data and requiring algorithmic disgorgement of models trained on unlawfully obtained data (Mintz, 2024), would protect consumers before harm occurs rather than years afterward.

---

## References

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

Boorstein, M., Iati, M., & Shin, A. (2021, July 21). Top U.S. Catholic Church official resigns after cellphone data used to track him on Grindr and to gay bars. *The Washington Post*. https://www.washingtonpost.com/religion/2021/07/20/bishop-misconduct-resign-burrill/

*Carpenter v. United States*, 585 U.S. 296 (2018).

Cox, J. (2022, May 3). Data broker is selling location data of people who visit abortion clinics. *Vice*. https://www.vice.com/en/article/location-data-abortion-clinics-safegraph-planned-parenthood/

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports, 3*, Article 1376. https://doi.org/10.1038/srep01376

*Dobbs v. Jackson Women's Health Organization*, 597 U.S. 215 (2022).

Electronic Frontier Foundation. (2026, August 4). *Location data brokers*. https://www.eff.org/issues/location-data-brokers

Federal Trade Commission. (2024, January 9). *FTC order prohibits data broker X-Mode Social and Outlogic from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data

Federal Trade Commission. (2026, May 4). *FTC to ban Kochava and subsidiary from selling sensitive location data to settle charges they sold location data linked to millions of mobile devices*. https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data

Holland & Knight. (2023, July 25). *The FTC is regulating AI: A comprehensive analysis*. https://www.hklaw.com/en/insights/publications/2023/07/the-ftc-is-regulating-ai-a-comprehensive-analysis

Internet Policy Review. (2022, August 4). *The untamed and discreet role of data brokers in surveillance capitalism: A transnational and interdisciplinary overview*. https://policyreview.info/articles/analysis/untamed-and-discreet-role-data-brokers-surveillance-capitalism-transnational-and

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Sherman, J. (2024, March 12). *Location data broker X-Mode and the FTC's unprecedented settlement*. Lawfare. https://www.lawfaremedia.org/article/location-data-broker-x-mode-and-the-ftc-s-unprecedented-settlement

Sigma Law Group. (2026, June 28). *The FTC's Kochava settlement and the new rules for location data*. https://sigmalawgroup.com/blog/2026-06-28-ftc-kochava-location-data/

Valentino-DeVries, J., Singer, N., Keller, M. H., & Krolik, A. (2018, December 10). Your apps know where you were last night, and they're not keeping it secret. *The New York Times*. https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html

Yale Journal on Regulation. (2026, July 14). *FTC's Kochava settlement advances data privacy enforcement–but leaves critical gaps in protecting consumers*. https://www.yalejreg.com/nc/ftcs-kochava-settlement-advances-data-privacy-enforcement-but-leaves-critical-gaps-in-protecting-consumers/

Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.

---

## AI Appendix

**Tools used:** Gemini Enterprise (proposal stage, September 19, 2026) and Cursor AI Agent, powered by a Claude large language model (case study stage, October 24, 2026; stakeholder revision, October 24, 2026).

**Conversation links:**
- Gemini (proposal): [insert shareable Gemini conversation link]
- Cursor (case study): [insert shareable Cursor conversation link or screenshot]

**How and why AI was used:**
1. **Case selection.** I asked the AI to compare the two events in my proposal. We chose *FTC v. Kochava* because it has more sources (court filings, FTC releases, legal analyses) and more complexity, including a pre-emptive lawsuit, an initial dismissal, an amended complaint, and a 2026 settlement.
2. **Structure and word budgeting.** I gave the AI the Week 4 task, the rubric, and the template. It drafted each section within the required word ranges (summary 250–300, stakeholders 250–300, broader issues 250–300, importance 150–200, and 900–1,100 words in total).
3. **Responding to instructor feedback.** My proposal feedback noted missing explicit citations and an AI appendix lacking reflection and conversation links. The AI added APA in-text citations to every factual claim, and this appendix now uses links instead of transcripts.
4. **Related cases and research.** The AI suggested related cases (Grindr/The Pillar, SafeGraph/Planned Parenthood, X-Mode/Outlogic, the *NYT* "Privacy Project") and academic grounding (de Montjoye et al., 2013; Zuboff, 2019; *Carpenter v. United States*).
5. **Week 5 stakeholder revision.** I gave the AI the Week 5 task, which asks that stakeholders be organized by role (victim, perpetrator, company representatives, connected parties, authorities, government) and named where possible. The AI restructured the stakeholder section around these roles, added named individuals (Charles Manning, Lina Khan, Samuel Levine, and Judge B. Lynn Winmill), and connected the employee stakeholder to the ACM Code of Ethics from this week's readings, while keeping the section within 250–300 words.

**Verification:** I checked each factual claim, date, and statistic (for example, the 61 million device sample, the May 2023 dismissal, the February 2024 denial of the motion to dismiss, and the 2026 settlement terms) against the cited primary sources. I also confirmed that every URL resolves and edited the prose into my own voice.

**Reflection:** [Personalize this paragraph in your own words. Suggested points: AI made it faster to structure a complex four-year legal history and to find related cases, but it could not be trusted on its own for exact dates, numbers, or legal holdings, so I had to verify them myself. Writing the stakeholder section made me realize that the harm is unevenly distributed, falling hardest on people who are already vulnerable. There is also an irony in using an AI system to critique AI-driven inference, which pushed me to think about what data I share with AI tools myself. Overall, AI worked best as a research assistant and editor, while the analysis and final judgment had to come from me.]
