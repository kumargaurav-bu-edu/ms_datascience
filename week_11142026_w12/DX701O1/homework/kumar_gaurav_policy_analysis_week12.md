# Closing the Clinic-Door Loophole: A Federal Policy Against the Commercial Sale of Precise Location Data and AI-Derived Inferences

**Author:** Kumar Gaurav
**Course:** DX701O1 — Ethics, Policy, and Governance in Data Science and AI
**Date:** November 2026

---

## 1. Introduction

A *data broker* is a company that collects personal information — often without the knowledge of the people it is about — and sells it to buyers it does not vet. In August 2022, the Federal Trade Commission (FTC) sued one such broker, Kochava, Inc., for selling the precise GPS locations of millions of smartphone users (FTC, 2022). A free sample of Kochava's data, offered on a public cloud marketplace, covered more than 61 million devices and could trace people to reproductive health clinics, places of worship, domestic violence shelters, and addiction recovery centers (Electronic Frontier Foundation [EFF], 2026). After *Dobbs v. Jackson Women's Health Organization* (2022), such data can carry legal consequences; for a shelter resident, it can be a safety threat.

This paper argues that the United States should enact a **federal floor statute** that bans the commercial sale and transfer of precise geolocation data and of AI-derived inferences from it, administered by the FTC with concurrent state enforcement and backed by mandatory organizational compliance programs. The paper identifies the ethical problem and stakeholders, grounds the policy in duty-based and contract-based ethics, specifies the implementation level, and addresses both anticipated critiques and unintended negative consequences.

---

## 2. The ethical problem

Kochava collected location signals through software embedded in ordinary mobile apps and sold them as timestamped GPS coordinates tied to Mobile Advertising IDs — the unique codes assigned to each phone. The amended FTC complaint alleged that Kochava also linked devices to names, addresses, and phone numbers and sold inferred audience segments based on sensitive traits (FTC, 2026). In February 2024, the court denied Kochava's motion to dismiss, finding that the FTC plausibly alleged substantial injury; a proposed stipulated order followed in May 2026 (Yale Journal on Regulation, 2026).

Two features make this an ethical problem rather than a mere commercial dispute. First, the *market exists without the knowledge of the people it is about*. Users who grant a weather app location access cannot reasonably anticipate resale to brokers, clustering by inference models, and sale of an "abortion clinic visitor" segment. Second, *inference turns ordinary data into sensitive data*. A single GPS ping is mundane, but models trained on millions of pings can cluster them into pregnancy, religion, sexuality, or addiction — what Zuboff (2019) calls the "behavioral surplus" at the core of surveillance capitalism.

---

## 3. Stakeholders

Five groups have a stake in how this problem is resolved.

- **Tracked users and their families** bear the harm. A clinic visitor after *Dobbs*, a shelter resident, or a worshipper faces exposure to prosecution, stalking, or violence.
- **Brokers and their leadership** (Kochava and its subsidiary Collective Data Solutions, founded by Charles Manning) argue they follow industry norms and cause no concrete injury (FTC, 2026).
- **Technical professionals inside those firms** — the data scientists and engineers who build products like Kochava's Database Graph and audience segments — face a professional dilemma under the ACM Code, which requires computing professionals to "avoid harm" (1.2) and "respect privacy" (1.6) (Association for Computing Machinery, 2018).
- **Enablers** — app developers who embed broker SDKs for revenue, buyers who purchase the feeds, and cloud marketplaces that host sample datasets — profit from the system and bear reputational and legal risk.
- **Authorities** — the FTC, the federal courts, and Congress — set the rules. The FTC has acted one company at a time; Congress, lacking a federal privacy law, is the absent stakeholder whose inaction forced a four-year lawsuit.

---

## 4. Why current safeguards fail

Four features of the current system explain why case-by-case enforcement is not enough.

- **The anonymization myth.** De Montjoye et al. (2013) showed that four spatio-temporal points uniquely identify about 95% of people in a mobility dataset. A home address at night and a workplace by day effectively *are* an identity, whether or not names are attached.
- **Notice-and-consent failure.** Solove (2013) shows that privacy self-management collapses when people cannot foresee downstream uses. A tap on "Allow" in a weather app cannot be meaningful consent to resale and inference.
- **The *Carpenter* loophole.** In *Carpenter v. United States* (2018), the Supreme Court required a warrant for police to obtain historical cell-site records. Buying the same kind of information from a broker is a way around that rule.
- **A fragmented patchwork.** Oregon, Maryland, Washington, California, and Montana have each addressed one slice — a sale ban (Oregon Legislative Assembly, 2025), a minimization rule, a geofencing rule, a deletion portal, a warrant rule — but national firms operate across every state (IAPP, 2026).

**Comparative note on GDPR.** The European Union's General Data Protection Regulation treats data revealing health, religion, or sexual orientation as *special-category data* requiring explicit consent (European Council, n.d.; Laybats & Davies, 2018). Norway fined Grindr NOK 65 million for sharing GPS and advertising IDs with ad partners without valid consent (Datatilsynet, 2023), and a Catholic newsletter in 2021 used commercially obtained Grindr data to out a senior U.S. priest (Boorstein et al., 2021). Even Europe's stronger regime — built on consent and large fines — has not stopped the broker market from producing this kind of harm. That is a reason to prefer a *prohibition* over a better consent box.

---

## 5. Ethical framework

The policy rests primarily on **duty-based (Kantian) ethics** and secondarily on **contract-based (Rawlsian) ethics**, both drawn from Tavani (2024, Chapter 2).

Kant's formula of humanity requires treating people "never merely as a means" (Kant, 1785/1998). In *Kochava*, users were treated purely as means: their movements were packaged and sold to unknown buyers, with no meaningful say. A duty-based view takes consent seriously, which is exactly why it rejects *fake* consent. When consent cannot be informed, the duty not to use a person merely as a means requires a prohibition — not a better pop-up. This framework also justifies **algorithmic disgorgement**: if a model was built by violating a duty, the wrongdoer should not keep the benefit (Mintz, 2024).

Contract-based ethics supplies the structural case. Behind Rawls's (1971) veil of ignorance, not knowing whether they will be the broker or the domestic violence survivor, rational people would demand protection for the most vulnerable. This is why the policy is a **federal floor** that applies to everyone, not just the residents of protective states, and why it is made by Congress, the FTC, and state attorneys general — public institutions — rather than by voluntary industry codes.

Consequentialist reasoning supports parts of the case (less stalking, lower enforcement costs than four-year lawsuits), but a simple utility sum can approve markets that endanger a minority while spreading the benefit across many. Virtue ethics shapes the organizational tier (see §7) but cannot stop firms that choose not to be virtuous.

---

## 6. The proposed policy

I propose a three-tier *Location Privacy and Algorithmic Accountability Act* with the following provisions:

- **A categorical ban** on the sale, transfer, or disclosure of *precise geolocation data* (defined, as in Oregon, as data that locates a person or device within 1,750 feet) and of inferences derived from such data, with narrow exceptions only for services the consumer directly requests (navigation, ride-hailing, emergency services).
- **Data minimization** at collection: a firm may collect only what is strictly necessary for the service a user asked for, matching the Maryland Online Data Privacy Act standard (Office of the Attorney General of Maryland, n.d.).
- **A warrant requirement** for government purchases of broker data, closing the *Carpenter* loophole, with an exigent-circumstances exception (imminent threat to life, missing child) subject to prompt after-the-fact court review.
- **Algorithmic disgorgement** as a standard remedy: deletion of models, audience segments, and derived products built from unlawfully obtained data (Mintz, 2024).
- **A research and public-interest exception** for *aggregated* data protected with formal privacy guarantees such as differential privacy (Dwork & Roth, 2014). The model is Google's COVID-19 Community Mobility Reports (Aktay et al., 2020).
- **Federal floor preemption** that keeps states free to go further, preserving fast state action like Oregon's (The Oregonian, 2025).

The statute is designed to be prohibition-based rather than consent-based, which follows from §5 and from the comparative evidence in §4.

---

## 7. Implementation level

The policy operates at **three levels**:

**National law.** Congress enacts the statute. A federal law is required because the supply chain is national: apps, SDK vendors, cloud marketplaces, and buyers all operate across state lines.

**National regulator plus concurrent state enforcement.** The FTC stands up a *Location Data and Algorithmic Accountability Unit* inside the Bureau of Consumer Protection. It runs a broker registry financed by registration fees (the California Delete Act uses this model; California Privacy Protection Agency, 2026), a national deletion portal, a technologist team that audits SDK traffic, and a program of test purchases modeled on how journalists exposed SafeGraph (Cox, 2022). State attorneys general enforce concurrently, as in the FTC's X-Mode/Outlogic settlement (FTC, 2024).

**Organizational compliance programs.** Every registered broker must designate a senior accountable executive to run a Sensitive Location Data Program, as the FTC's Mobilewalla order already requires (Federal Trade Commission, 2025). Larger firms, above a bulk threshold matching the Department of Justice Data Security Program's 1,000-U.S.-device rule (U.S. Department of Justice, 2025), face board-level oversight, mandatory algorithmic impact assessments, and a protected whistleblower channel for engineers. This is where virtue ethics operationalizes into process.

---

## 8. Anticipating critiques

The strongest objections are legal, economic, and institutional.

- **First Amendment.** In *Sorrell v. IMS Health Inc.* (2011), the Supreme Court struck a Vermont law restricting the sale of prescribing data as content- and speaker-based. The response is to draft the ban as a uniform regulation of the commercial transfer of sensitive personal information — applied to *every* seller and buyer, not singling out a message or speaker — and to open the statute with legislative findings documenting stalking, clinic exposure, and national-security risk (Office of the Director of National Intelligence, 2022). A severability clause ensures that if one provision falls, the sale ban, registry, and warrant requirement survive. Honest limitation: no drafting can guarantee the outcome of First Amendment review.
- **Economic harm.** The ban targets *transfer*, not use: a navigation app can still use location to deliver service, and contextual advertising remains lawful. Apple's App Tracking Transparency and Google's move of Maps Timeline to on-device storage show that major platforms can adapt (Apple, 2021; Google, 2023). Phased effective dates (12 months for large brokers, 24 for small developers) and a small-business threshold protect smaller firms.
- **Law enforcement.** The *Fourth Amendment Is Not For Sale Act* passed the House 219–199 but stalled in the Senate on executive-branch opposition (U.S. House of Representatives, Office of the Clerk, 2024). The policy answers this with the exigent-circumstances exception already specified in §6, keeping foreign-intelligence activity under existing court-supervised procedures.
- **Overbreadth.** Research and public-health uses are protected through the aggregated, differentially private exception in §6.
- **Property and trade secrets.** Brokers argue that datasets and models are their property; disgorgement destroys lawful investment. Under Locke's (1690/1980) labor theory, property arises when labor is mixed with something *unowned*, leaving "enough, and as good" for others — a broker mixes labor with movements taken without consent, which does not create a clean property claim. Raw facts are not protected by copyright (*Feist Publications, Inc. v. Rural Telephone Service Co.*, 1991), and the FTC has already required deletion of models built from improperly obtained data in cases such as the X-Mode/Outlogic settlement. Disgorgement is triggered only by post-enactment violations, and firms that keep data-lineage records can show which models are clean.

A second group of objections — that de-identification is sufficient, that users should be free to trade their data, that a federal floor still leaves a state patchwork — is answered by §4 and by the federal-floor design choice.

---

## 9. Unintended negative consequences

Even if the policy works as intended, it may create four downstream effects that should be anticipated and mitigated.

- **Jurisdictional flight.** Brokers may incorporate overseas and sell data from outside U.S. jurisdiction. *Mitigation:* apply the statute to transfers *into* the United States and to U.S.-person data regardless of where the processor sits, mirroring the extraterritorial logic of GDPR and of the DOJ Data Security Program (U.S. Department of Justice, 2025).
- **Market consolidation.** Compliance cost favors large platforms that can absorb it, potentially entrenching Google, Apple, and Meta at the expense of smaller competitors. *Mitigation:* the small-business threshold, phased deadlines, and a public FTC compliance template reduce fixed costs for new entrants.
- **Chilling of legitimate research.** Even with the aggregated-data exception, researchers may avoid location studies out of caution. *Mitigation:* the FTC unit publishes an approved list of aggregation methods and a model data-use agreement, so researchers face a clear safe harbor rather than ambiguity.
- **Equity impact on ad-supported apps.** Reduced targeting revenue could push some apps to paid-only models, which falls hardest on low-income users. *Mitigation:* contextual advertising (ads based on page content or local weather, not personal history) remains lawful and is a smaller revenue loss than industry estimates suggest.

None of these consequences outweighs the harm the policy prevents, but naming them is part of honest policy design.

---

## 10. Conclusion

*Kochava* is not an isolated bad actor. Grindr data outed a priest (Boorstein et al., 2021); SafeGraph sold data on visitors to Planned Parenthood clinics (Cox, 2022); a *New York Times* investigation re-identified individuals from supposedly anonymous app data (Valentino-DeVries et al., 2018). The pattern is that AI inference has outpaced existing privacy law, and that the harm falls hardest on people with the least power to protect themselves.

A federal floor statute that bans the commercial sale of precise location data and its AI-derived inferences, administered by the FTC with concurrent state enforcement and mandatory organizational compliance, answers the ethical problem identified in §2, honors the duty-based and contract-based frameworks in §5, closes the four safeguard failures in §4, and survives the critiques in §8. Its unintended consequences are real and can be mitigated. The alternative — another four-year lawsuit against the next Kochava — leaves vulnerable people exposed while the industry's architecture continues untouched.

---

## References

Aktay, A., Bavadekar, S., Cossoul, G., Davis, J., Desfontaines, D., Fabrikant, A., Gabrilovich, E., Gadepalli, K., Gipson, B., Guevara, M., Kamath, C., Kansal, M., Lange, A., Mandayam, C., Oplinger, A., Pluntke, C., Roessler, T., Schlosberg, A., Shekel, T., … Wilson, R. J. (2020). *Google COVID-19 community mobility reports: Anonymization process description (version 1.1)*. arXiv. https://arxiv.org/abs/2004.04145

Apple. (2021, April 26). *App Tracking Transparency* [Developer documentation]. https://developer.apple.com/documentation/apptrackingtransparency

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

Boorstein, M., Iati, M., & Shin, A. (2021, July 21). Top U.S. Catholic Church official resigns after cellphone data used to track him on Grindr and to gay bars. *The Washington Post*. https://www.washingtonpost.com/religion/2021/07/20/bishop-misconduct-resign-burrill/

California Privacy Protection Agency. (2026). *DROP for data brokers*. https://privacy.ca.gov/drop-for-data-brokers/

*Carpenter v. United States*, 585 U.S. 296 (2018).

Cox, J. (2022, May 3). Data broker is selling location data of people who visit abortion clinics. *Vice*. https://www.vice.com/en/article/location-data-abortion-clinics-safegraph-planned-parenthood/

Datatilsynet. (2023, October 2). *Record fine in the Grindr case confirmed*. https://www.datatilsynet.no/en/news/news-2023/record-fine-grindr-confirmed/

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports, 3*, Article 1376. https://doi.org/10.1038/srep01376

*Dobbs v. Jackson Women's Health Organization*, 597 U.S. 215 (2022).

Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. https://doi.org/10.1561/0400000042

Electronic Frontier Foundation. (2026, August 4). *Location data brokers*. https://www.eff.org/issues/location-data-brokers

European Council. (n.d.). *What is GDPR, the EU's new data protection law?* https://www.consilium.europa.eu/en/policies/data-protection-regulation/

Federal Trade Commission. (2022, August 29). *FTC sues Kochava for selling data that tracks people at reproductive health clinics, places of worship, and other sensitive locations*. https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other

Federal Trade Commission. (2024, January 9). *FTC order prohibits data broker X-Mode Social and Outlogic from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data

Federal Trade Commission. (2025). *Decision and order: In the matter of Mobilewalla, Inc.* https://search.ftc.gov/system/files/ftc_gov/pdf/Mobilewalla-D%26O.pdf

Federal Trade Commission. (2026, May 4). *FTC to ban Kochava and subsidiary from selling sensitive location data to settle charges they sold location data linked to millions of mobile devices*. https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data

*Feist Publications, Inc. v. Rural Telephone Service Co.*, 499 U.S. 340 (1991).

Google. (2023, December 12). *Updates to Location History and new controls coming soon to Maps*. The Keyword. https://blog.google/products/maps/updates-to-location-history-and-new-controls-coming-soon-to-maps/

IAPP. (2026, April). *SECURE Data Act: Analysis of the new federal privacy bill*. https://iapp.org/news/a/secure-data-act-analysis-of-the-new-federal-privacy-bill

Kant, I. (1998). *Groundwork of the metaphysics of morals* (M. Gregor, Trans.). Cambridge University Press. (Original work published 1785)

Laybats, C., & Davies, J. (2018). GDPR: Implementing the regulations. *Business Information Review, 35*(2), 81–83. https://doi.org/10.1177/0266382118777808

Locke, J. (1980). *Second treatise of government* (C. B. Macpherson, Ed.). Hackett Publishing. (Original work published 1690)

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Office of the Attorney General of Maryland. (n.d.). *Data privacy in Maryland*. https://oag.maryland.gov/resources-info/Pages/data-privacy.aspx

Office of the Director of National Intelligence. (2022). *Report to the Director of National Intelligence: Senior Advisory Group panel on commercially available information* (Declassified June 2023). https://www.dni.gov/files/ODNI/documents/assessments/ODNI-Declassified-Report-on-CAI-January2022.pdf

Oregon Legislative Assembly. (2025). *House Bill 2008 (Enrolled)*. https://olis.oregonlegislature.gov/liz/2025R1/Downloads/MeasureDocument/hb2008/Enrolled

Rawls, J. (1971). *A theory of justice*. Harvard University Press.

Solove, D. J. (2013). Privacy self-management and the consent dilemma. *Harvard Law Review, 126*(7), 1880–1903.

*Sorrell v. IMS Health Inc.*, 564 U.S. 552 (2011).

Tavani, H. T. (2024). *Ethics and technology: Controversies, questions, and strategies for ethical computing* (5th ed.). Wiley.

The Oregonian. (2025). *HB 2008: Oregon Legislature bill tracker*. https://gov.oregonlive.com/bill/2025/HB2008/

U.S. Department of Justice, National Security Division. (2025). *Data Security Program: Frequently asked questions*. https://www.justice.gov/nsd/media/1415006/dl

U.S. House of Representatives, Office of the Clerk. (2024, April 17). *Roll call 136, H.R. 4639, Fourth Amendment Is Not For Sale Act*. https://clerk.house.gov/Votes/2024136

Valentino-DeVries, J., Singer, N., Keller, M. H., & Krolik, A. (2018, December 10). Your apps know where you were last night, and they're not keeping it secret. *The New York Times*. https://www.nytimes.com/interactive/2018/12/10/business/location-data-privacy-apps.html

Yale Journal on Regulation. (2026, July 14). *FTC's Kochava settlement advances data privacy enforcement–but leaves critical gaps in protecting consumers*. https://www.yalejreg.com/nc/ftcs-kochava-settlement-advances-data-privacy-enforcement-but-leaves-critical-gaps-in-protecting-consumers/

Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.

### Consulted but not cited

European Union. (2016). *Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation)*. GDPR Info. https://gdpr-info.eu/

Hunton Andrews Kurth. (2025, January). *FTC finalizes orders against data brokers over sensitive location data*. https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-finalizes-orders-against-data-brokers-over-sensitive-location-data

IAPP. (2024, June 27). *American Privacy Rights Act markup canceled, next US House steps uncertain*. https://iapp.org/news/a/american-privacy-rights-act-markup-canceled-next-us-house-steps-uncertain

Massachusetts House of Representatives. (2026, June 4). *House passes Massachusetts Consumer Data Privacy Act* [Press release]. https://malegislature.gov/PressRoom/Detail?pressReleaseId=1396

Network Advertising Initiative. (2022, June 22). *Leading companies commit to privacy-first NAI Enhanced Standards for precise location information*. https://thenai.org/press/leading-companies-commit-to-privacy-first-nai-enhanced-standards-for-precise-location-information/

Sherman, J. (2024, March 12). *Location data broker X-Mode and the FTC's unprecedented settlement*. Lawfare. https://www.lawfaremedia.org/article/location-data-broker-x-mode-and-the-ftc-s-unprecedented-settlement

Sigma Law Group. (2026, June 28). *The FTC's Kochava settlement and the new rules for location data*. https://sigmalawgroup.com/blog/2026-06-28-ftc-kochava-location-data/

Washington State Legislature. (2023). *Chapter 19.373 RCW: Washington My Health My Data Act*. https://app.leg.wa.gov/rcw/default.aspx?cite=19.373&full=true
