# Homework Reflection 1

## Week 1

### 1. Is the farthest match distance too far to be meaningful? How can you decide?

The farthest match distance of **0.2102** appears too large to be a meaningful match because most distances are below 0.02. It suggests limited common support: some treated units, especially those with high Z values, lack comparable controls. Several treated units also match to control unit 18, indicating a possible gap among high-Z controls.

Applying a 0.2 caliper drops only the 2 worst matches (46 of 48 kept) and moves the estimated treatment effect from **0.5434 to 0.5363**; tighter calipers shift it further (0.515 at 0.15, 0.503 at 0.05), confirming the poor-match tail influences the estimate. I would compare the distance with the overall distribution, inspect overlap in Z, and test whether the estimate changes under a reasonable caliper. These checks suggest that the 0.2102 match should be excluded or handled cautiously.

### 2. Invent a different matching approach.

I would use **caliper + nearest-neighbor matching** with a maximum distance of 0.1. For each treated unit, I would select the single closest control, but only if the distance is at most 0.1; otherwise, I would exclude that treated unit. This avoids accepting arbitrarily distant matches and would prevent the 0.2102 match.

Unlike radius matching, this method selects only one control per treated unit, rather than all controls within the radius. Unlike unrestricted nearest-neighbor matching, it enforces a quality threshold. The trade-off is that some treated units may be dropped, potentially creating selection bias if excluded units differ systematically from those retained.

## Week 2

### 1. Invent an example situation that would use fixed effects.

A company wants to know whether voluntary job training increases productivity across 20 factories. Comparing trained and untrained workers directly may be misleading because well-managed factories may encourage training and also have higher productivity. Factory culture is unobserved and could confound the comparison.

Factory fixed effects give each factory its own intercept, so the training effect is estimated from comparisons within factories rather than differences between factories. In my simulation, training participation correlated with factory culture at **0.62**; pooled OLS estimated an effect of **4.85**, compared with the true effect of **2.0**, while both factory-dummy fixed effects and the within-transformation estimated **2.01**.

Fixed effects are useful for grouped or panel data when unobserved group characteristics may correlate with treatment. They cannot estimate effects of variables that never change within a group, and they do not remove confounding from factors that vary within groups over time. The key assumption is that, after accounting for group effects, treatment satisfies the required exogeneity condition; otherwise, another design may be needed.

### 2. Bootstrap simulation: variance of the mean of a Pareto distribution

I used a Pareto distribution with shape \(\alpha=3\) and scale \(x_m=1\), giving a theoretical mean of 1.5 and variance of 0.75. For sample sizes \(n \in \{20,50,200,1000,5000\}\), I generated a sample, resampled it with replacement 2,000 times, calculated each bootstrap sample mean, and estimated the variance across those means. I compared the results with the theoretical sampling variance, \(\sigma^2/n=0.75/n\).

The bootstrap variance decreased from **0.0210 at \(n=20\)** to **0.00014 at \(n=5{,}000\)**, consistent with the theoretical variance decreasing as sample size grows. A larger sample gives a more precise estimate of the population mean; for example, quadrupling sample size reduces the theoretical variance to one-quarter.

The small-sample estimates did not exactly match theory (at \(n=50\), the bootstrap variance was 0.0292 versus 0.0150 theoretically). This is expected because the Pareto distribution has a heavy right tail: small samples can miss very large values or include an unusually large one. Since the bootstrap relies on the observed sample, its estimate can be noisy for small samples.

## Week 3

### 1. How would you test for a change in the second derivative in the event study?

In the interrupted time-series model, `event_50` tests a level change and `T_post = max(0, time − 50)` tests a slope change. To test a second-derivative change (curvature), I added both a pre-event quadratic control and a post-event quadratic term:

```text
Y ~ time + D + T_post + time² + T_post²
```

I tested whether the coefficient on `T_post²` equals zero using an OLS t-test. The curvature-change p-values were **0.979, 0.154, and 0.776** for the three series, all above 0.05; therefore, I failed to reject the null hypothesis for each series. The corresponding level-change p-values were 0.020, 0.095, and 0.000, and slope-change p-values were 0.000, 0.012, and 0.000.

These results suggest level or slope changes may explain the event effects, with no statistically significant evidence of an additional curvature change. However, quadratic terms can be highly correlated, inflating standard errors, and a small number of post-event observations can make curvature hard to estimate. A joint F-test of `D`, `T_post`, and `T_post²` could also test whether the event affected the outcome through any of these pathways.

### 2. Difference-in-Differences (DiD): tutoring effect

Two schools take the same exam before and after a semester. School A receives tutoring and already scores about 10 points higher than School B; both schools’ scores also rise because the later exam is easier. A post-semester comparison (87.95 versus 73.07) or School A’s before-and-after change alone would mix the tutoring effect with these baseline and time differences.

School B’s average rises from **70.15 to 73.07** (+2.91), while School A rises from **80.03 to 87.95** (+7.93). The DiD estimate is School A’s gain minus School B’s gain: **7.93 − 2.91 = 5.013 points**, matching the regression interaction coefficient `treat:post` (p ≈ \(4 \times 10^{-83}\)). This recovers the true effect of 5 points and provides strong evidence that tutoring increases exam scores.

The key assumption is **parallel trends**: without tutoring, School A would have changed by the same amount as School B. It holds by construction here but needs justification in real data, such as by checking multiple pre-treatment periods. Spillovers between schools or changes in student composition could also bias the estimate.

## Week 4

### 1. Instrumental variables: dividing W into multiple ranges

I divided W into quantile bins using `pd.qcut(W, k)`. Within each bin, I calculated the Wald ratio—the difference in mean Y between Z groups divided by the difference in mean X—and then averaged the bin estimates weighted by bin size. This compares observations with more similar W values and reduces the influence of W imbalance on the crude estimate.

The unstratified Wald estimate was **1.5619**; the stratified estimates were **1.5156, 1.5089, and 1.5055** for 5, 10, and 20 bins, close to the 2SLS estimate with W (**1.5123**). Quantile bins had no empty bins and minimum absolute X differences of about 0.9. Equal-width bins created sparse or single-group bins, NaNs, and small denominators (about 0.14–0.24), causing unstable estimates; unweighted averages ranged from 0.82 to 1.62.

These checks showed that bin construction and weighting matter. In every bin, the difference in X between Z groups must be far enough from zero to avoid a potentially weak instrument. I used a temporary binned object to avoid modifying the shared dataframe, and compared 5, 10, and 20 bins to check stability: the similar estimates suggest the result is not driven by one bin choice.

### 2. Plotting college outcome (Y) against test score (X) around 80

Plotting all 68,000 binary outcomes directly creates overlapping horizontal bands, so I added small vertical jitter (standard deviation 0.03) and transparency (0.04) to show point density. I also plotted admission rates in one-point score bins and overlaid logistic-regression predictions for \(P(Y=1 \mid X,D)\), including a possible jump at the cutoff of 80.

For Dataset A, binned admission rates were relatively flat at about 0.30 on the left and 0.60 on the right; the X coefficient was about 0.002 and the cutoff indicator coefficient was 1.23. For Dataset B, admission rates increased on both sides, with an X coefficient around 0.050 and cutoff coefficient 1.37. The logistic curves followed the binned rates; model accuracies were **0.65** for A and **0.79** for B. The plots suggest Dataset A may not need an X slope, while Dataset B does.

Jitter improves readability but creates artificial vertical spread, so it should not be interpreted as actual continuous variation in Y; the binned rates show observed conditional means more directly. Logistic regression also assumes log-odds are linear in X on each side of the cutoff. If there is additional curvature or the cutoff relationship differs from this specification, a richer model may be necessary.
