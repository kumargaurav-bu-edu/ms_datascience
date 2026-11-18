# Policy Analysis — Week 10: Choosing and Applying an Ethical Framework

**Author:** Kumar Gaurav
**Topic:** Commercial sale of precise location data and AI-driven inference of sensitive traits (anchor case: *FTC v. Kochava*)
**Builds on:** Week 8 (proposed solutions) and Week 9 (policy levels and implementation)

---

## 1. The policy being defended (one-paragraph recap)

A three-tier policy: (1) a **federal floor statute** that bans the sale and transfer of precise geolocation data and of AI-derived inferences from it, requires data minimization, requires a warrant for government purchases, and authorizes **algorithmic disgorgement**; (2) **FTC rulemaking and enforcement** with a broker registry and national deletion portal, alongside state attorneys general; and (3) mandatory **organizational compliance programs** led by a named accountable executive.

---

## 2. The four frameworks, tested against the policy

| Framework | Core question | What it says about selling location data | Fit with my policy |
|---|---|---|---|
| **Consequence-based** (utilitarianism) | Which rule produces the greatest overall good? | Weighs ad revenue, free apps, and fraud detection against harms to tracked people | **Partial.** Supports regulation, but a pure cost-benefit test could permit sales if the aggregate benefit is large |
| **Duty-based** (Kantian deontology) | Does the act respect persons as ends in themselves? | Turning a person's movements into a product sold without real consent uses that person merely as a means | **Strong — primary framework.** Justifies a categorical *ban* rather than a consent box |
| **Contract-based** (social contract; Rawls) | What rules would free and equal people agree to? | Behind a "veil of ignorance," no one would accept a market that might expose them as a clinic visitor, shelter resident, or worshipper | **Strong — supporting framework.** Justifies the multi-level, democratically legitimate design |
| **Character-based** (virtue ethics) | What would a person of good character do? | A virtuous data scientist would not build a pipeline that infers pregnancy or religion for sale | **Partial.** Fits the organizational tier but cannot stop firms that choose not to be virtuous |

(Framework definitions follow Tavani, 2024, Chapter 2.)

---

## 3. Primary framework: duty-based ethics

**Why it aligns best.** My policy is built around **prohibitions and rights**, not trade-offs. Kant's formula of humanity requires treating people "never merely as a means" (Kant, 1785/1998). In *Kochava*, users were treated purely as means: their GPS pings were packaged and sold so that unknown buyers could locate them, and they had no meaningful say.

**Duty-based ethics explains three design choices that other frameworks do not:**

1. **A ban instead of consent.** A duty-based view takes consent seriously, which is exactly why it rejects *fake* consent. A user who taps "Allow" in a weather app cannot reasonably foresee resale to a broker, clustering by an inference model, and sale of an "abortion clinic visitor" segment. Solove (2013) shows that privacy self-management fails when people cannot understand downstream uses. When consent cannot be informed, the duty not to use a person merely as a means requires a prohibition.
2. **A duty that does not depend on proven harm.** The FTC lost its first *Kochava* complaint because it had not shown "substantial injury." Under duty-based reasoning, the wrong is the treatment itself, whether or not a particular person was later stalked. My statute therefore makes the sale unlawful in itself, with no need to prove harm case by case.
3. **Algorithmic disgorgement.** If a model was built by violating a duty, the wrongdoer should not keep the benefit. Requiring deletion of models and audience segments trained on unlawfully obtained data follows directly from this principle (Mintz, 2024).

**Universalizability test.** Kant's first formulation asks whether a rule could be willed as universal law. "Any company may sell anyone's movements to anyone" universalizes into a society where no visit to a clinic, mosque, or shelter is private — a rule no rational person could will for themselves.

---

## 4. Supporting framework: contract-based ethics

Duty-based ethics tells us *what* must be prohibited; contract-based ethics tells us *why the rules are legitimate and who should make them*.

- **Veil of ignorance.** Rawls (1971) asks what principles people would choose without knowing their place in society. Not knowing whether they will be the data broker or the domestic violence survivor whose shelter is exposed, rational people would choose strong location protections. This is why my policy sets a **federal floor** that applies to everyone, not only residents of protective states.
- **Protecting the least advantaged.** Rawls' difference principle favors rules that benefit the worst-off. The harms of location sales fall hardest on vulnerable groups: people seeking reproductive care after *Dobbs*, LGBTQ+ people (as in the Grindr data used to out a priest), immigrants, and survivors.
- **Democratic legitimacy.** A social contract is made through public institutions. The policy's reliance on Congress, the FTC, and state attorneys general — rather than voluntary codes like the NAI standards — reflects the idea that rules about surveillance must come from the people affected, not from the industry that profits.

**Link to Week 10 course themes.** The social credit readings show how data-driven systems can monitor and score behavior (Cho, 2024; Kobie, 2019). The commercial location market is a private analog: it profiles people to predict and influence their behavior, which is the core of surveillance capitalism (Barney & Wigmore, n.d.; Zuboff, 2019). A social-contract framing asks whether citizens ever agreed to this kind of monitoring; in the U.S. they have not, because no federal law has been passed.

---

## 5. Why not consequence-based ethics as the primary lens?

Utilitarian reasoning still supports parts of the policy, and the paper should acknowledge it:

- **Rule-utilitarian support.** A general rule against selling sensitive location data probably produces better outcomes overall: less stalking and discrimination, more trust in apps, and lower enforcement costs than four-year lawsuits.

But it is not strong enough to be the foundation:

- **Aggregation hides concentrated harm.** Ad-targeting gains are spread across millions of users and firms, while harms are severe and concentrated on a few people. A simple utility sum can approve a market that endangers a minority.
- **Hard to measure.** Harms such as chilling effects (people avoiding a clinic or protest because they could be tracked) are real but hard to quantify. This is the same weakness that sank the FTC's first complaint.
- **Re-identification risk is systemic.** Because four spatio-temporal points identify 95% of people (de Montjoye et al., 2013), every dataset creates risk to everyone in it, which a case-by-case cost-benefit test underestimates.

## 6. Where character-based ethics fits

Virtue ethics shapes the **organizational tier**. Requiring a named accountable executive, cross-functional review, and a whistleblower channel aims to build an organizational culture of honesty and care. The ACM Code's principles to "avoid harm" (1.2) and "respect privacy" (1.6) describe the character expected of computing professionals (Association for Computing Machinery, 2018). Virtue alone is insufficient: Kochava's leadership argued it followed industry norms, which shows that character standards need the backing of enforceable duties.

---

## 7. Summary statement for the paper

> This policy is grounded primarily in **duty-based ethics**: selling a person's precise movements and the sensitive traits inferred from them treats that person merely as a means, and because meaningful consent is impossible in this market, the duty can be honored only by prohibition. **Contract-based ethics** supports the policy's multi-level, democratically enacted structure, since people choosing rules behind a veil of ignorance would demand protection for the most vulnerable. Consequence-based reasoning reinforces the case at the level of general rules, and character-based ethics guides how organizations put the policy into practice.

---

## References

Association for Computing Machinery. (2018). *ACM code of ethics and professional conduct*. https://www.acm.org/code-of-ethics

Barney, N., & Wigmore, I. (n.d.). *What is surveillance capitalism?* TechTarget. https://www.techtarget.com/searchcio/definition/surveillance-capitalism

Cho, E. (2024, December 11). The social credit system: Not just another Chinese idiosyncrasy. *Journal of Public and International Affairs*.

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports, 3*, Article 1376. https://doi.org/10.1038/srep01376

Kant, I. (1998). *Groundwork of the metaphysics of morals* (M. Gregor, Trans.). Cambridge University Press. (Original work published 1785)

Kobie, N. (2019, June 7). The complicated truth about China's social credit system. *Wired*.

Mintz. (2024, January 24). *Algorithmic disgorgement: An increasingly important part of the FTC's remedial arsenal*. https://www.mintz.com/insights-center/viewpoints/54731/2024-01-23-algorithmic-disgorgement-increasingly-important-part

Rawls, J. (1971). *A theory of justice*. Harvard University Press.

Solove, D. J. (2013). Privacy self-management and the consent dilemma. *Harvard Law Review, 126*(7), 1880–1903.

Tavani, H. T. (2024). *Ethics and technology: Controversies, questions, and strategies for ethical computing* (5th ed.). Wiley.

Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the new frontier of power*. PublicAffairs.
