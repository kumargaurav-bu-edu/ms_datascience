
Homework reflection 4

1. The Coding Quiz gives two options for instrumental variables.  For the second item (dividing the range of W into multiple ranges), explain how you did it, show your code, and discuss any issues you encountered.

1. Instrumental Variables: Dividing the Range of W into Multiple Ranges
Question: The Coding Quiz gives two options for instrumental variables. For the second item (dividing the range of W into multiple ranges), explain how you did it, show your code, and discuss any issues you encountered.
How I Stratified W and the Issues
Within each narrow W-range, W is nearly constant, so the Z → Y contrast within that range is less likely to be driven by W. The within-bin Wald ratio,
(Mean Y | Z = 1 − Mean Y | Z = 0) / (Mean X | Z = 1 − Mean X | Z = 0),
provides the local causal estimate. I then calculated the size-weighted average across bins to obtain the overall effect.
The code uses pd.qcut(W, k) to create quantile bins, followed by groupby to calculate the differences in each bin. Finally, np.average(ratios, weights=sizes) calculates the weighted average of the ratios.
The crude (unstratified) Wald estimate was 1.5619. The stratified estimates were approximately 1.505–1.516 across k = 5, 10, and 20, matching the 2SLS estimate with W (1.5123). The small difference suggests that the mild imbalance in W between the two Z groups (E[W | Z = 1] ≈ 0.01 versus −0.03) affects the crude estimate.
Issues encountered
Bin construction matters more than the number of bins. Quantile bins created using qcut were stable, with weighted estimates of 1.5156, 1.5089, and 1.5055. There were no empty bins, and the minimum absolute difference in X between the Z groups was approximately 0.9.
Equal-width bins created using cut caused problems. Some bins contained observations from only one Z group or were empty, producing NaN values. The denominators also became very small, with minimum absolute differences in X of approximately 0.14–0.24. The unweighted mean ranged from 0.82 to 1.62, showing how a sparse tail bin could disproportionately influence the average. This demonstrated the importance of weighting by bin size and preferring quantile bins.
Checking the denominator is important. The difference in X between Z = 1 and Z = 0 must be sufficiently far from zero in every bin. A very small denominator indicates a potentially weak instrument within that stratum. I printed the minimum absolute difference in X as a diagnostic.
Avoiding unintended dataframe changes. The quiz code creates a Wbin column directly in the shared dataframe, permanently modifying it. My function instead creates bins in a temporary object to avoid this side effect.
Balancing the number of bins. More bins can reduce residual confounding by W, but they can also make the local denominators noisier. Testing 5, 10, and 20 bins provides a practical stability check. Since all three estimates were similar, the result does not appear to be an artifact of the chosen number of bins.


2. Plotting the College Outcome (Y) Against Test Score (X) Around 80
Question: Plot the college outcome (Y) versus the test score (X) in a small range of test scores around 80. Compare the plot with the probability of Y predicted by logistic regression. The ground-truth Y value is 0 or 1, so do not simply plot 0 or 1, as that would make the plot unreadable. Find a way to make it look better.
How I improved the readability
Plotting all 68,000 raw observations with outcomes of 0 or 1 creates two solid horizontal bands because many points overlap. I used three techniques to make the plot easier to interpret:
Vertical jitter: I added a small amount of random vertical noise (standard deviation = 0.03) and used an alpha transparency of 0.04. This reduces overplotting and makes the density of observations visible at each score and outcome.
Binned admission rates: I calculated admission rates in one-point test-score bins and plotted them as yellow dots. These dots show the conditional mean outcome at each score without the noise of individual observations.
Logistic regression curve: I overlaid the predicted probability, P(Y = 1 | X, D), from logistic regression with a cutoff indicator. This provides a model-based comparison and allows the predicted probability to jump at the cutoff of 80, consistent with the regression discontinuity setup.
What the plot shows
Dataset A: The binned admission rates are relatively flat, at approximately 0.30 on the left and 0.60 on the right. The logistic regression coefficient for X is approximately 0.002. The predicted curve therefore consists of two nearly flat segments connected by a jump at the cutoff. The coefficient for D is 1.23.
Dataset B: The admission rates increase on both sides of the cutoff, and the coefficient for X is approximately 0.050. The logistic regression curve shows a visibly increasing S-shape, along with a smaller jump at the cutoff. The coefficient for D is 1.37.
In both datasets, the logistic regression predictions closely follow the yellow binned-rate dots. The reported model accuracies were 0.65 for Dataset A and 0.79 for Dataset B. These plots support the earlier regression discontinuity finding: Dataset A does not appear to require a slope in X, whereas Dataset B does.
Limitations
Jitter creates artificial vertical spread. If readers mistake this spread for actual variation in the outcome, they may incorrectly interpret the binary outcome as continuous. The binned admission-rate dots provide a more direct representation of the observed conditional means.
The logistic regression model also assumes that the log-odds are linear in X within each side of the cutoff and, with the cutoff indicator, allows a sharp jump exactly at 80. If the relationship has additional curvature or the cutoff is not sharp, a richer model specification may be needed.
