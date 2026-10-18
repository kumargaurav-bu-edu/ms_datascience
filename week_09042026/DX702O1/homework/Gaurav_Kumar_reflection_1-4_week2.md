Homework reflection 2
Week 2

1. Invent an example situation that would use fixed effects.

**Situation.** A company runs a voluntary job-training program in 20 factories and asks: does training raise worker productivity? A naive comparison of trained vs. untrained workers is confounded by *factory culture*: well-run factories both encourage training and are more productive for everyone. Culture is unobserved, so it cannot be controlled for directly — this is exactly when **fixed effects** (one intercept per factory) are used: each factory gets its own baseline, and the training effect is estimated from *within-factory* comparisons only.

**What the simulation shows.** Training uptake correlates with factory culture at 0.62, so confounding is strong. Pooled OLS (one shared intercept) estimates the effect as **4.85** against a truth of **2.0** — badly upward biased, because it credits training for the culture gap between factories. The fixed-effects estimator (factory dummies) gives **2.01**, and the equivalent within-transform (demeaning Y and X per factory) also gives **2.01** — both recover the truth by discarding all between-factory variation.

**When this applies.** Grouped or panel data (workers in factories, students in schools, patients in hospitals, firms over years) where an unobserved group trait may correlate with the treatment. The identifying assumption is strict exogeneity *within* groups: after removing the group mean, the treatment must be as-good-as-random.

**Limitations.** Fixed effects cannot estimate the effect of anything constant within a group (e.g. a factory-level policy), they do nothing about *within-group* confounding, and they cost one degree of freedom per group. If the unobserved confounder varies within groups over the relevant dimension, a different design (IV, RDD) is needed.


2. Write a Python program that performs a bootstrap simulation to find the variance in the mean of the Pareto distribution when different samples are taken.  Explain what you had to do for this.  As you make the full sample size bigger (for the same distribution), what happens to the variance of the mean of the samples?  Does it stay about the same, get smaller, or get bigger?

**What I had to do.** (1) Pick a Pareto with finite variance — shape α=3, scale xm=1 (mean 1.5, variance 0.75; α must exceed 2 or the variance does not exist and the exercise breaks). (2) For each sample size n in {20, 50, 200, 1000, 5000}, draw one sample and resample it with replacement B=2000 times, recording each resample's mean. (3) Take the variance across the 2000 bootstrap means as the estimate of Var(sample mean). (4) Compare against the textbook sampling variance σ²/n = 0.75/n and plot both on log-log axes.

**Result: it gets smaller.** Bootstrap Var(mean) falls from 0.0210 (n=20) to 0.00014 (n=5000), tracking the 0.75/n line (0.0375 → 0.00015). That is the expected 1/n decay: the standard error of the mean is σ/√n, so its square — the variance — is σ²/n. A bigger sample pins down the mean; quadrupling n quarters the variance.

**Caveats worth stating.** At n=20 and n=50 the bootstrap values (0.0210, 0.0292) wobble around theory (0.0375, 0.0150) rather than sitting on it — Pareto's heavy right tail means small samples sometimes miss (or catch) a huge draw, so both the sample variance and its bootstrap inherit that instability. The bootstrap estimates the *sampling* variance from one sample; with heavy tails and small n it is noisier than the textbook formula, and it converges to it as n grows, exactly as the table shows.
