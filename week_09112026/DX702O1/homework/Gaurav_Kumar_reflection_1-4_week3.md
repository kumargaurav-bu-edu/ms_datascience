Homework reflection 3

1. In the event study in Coding Quiz 3, how would we go about testing for a change in the second derivative as well?


# Homework Reflection 4

## 1. Testing for a Second-Derivative Change

### Answer to Question 1 — Testing a Second-Derivative Change

**How I did it**

Quiz 3's interrupted time series analysis (ITSA) tests the zeroth derivative (a level change through the `event_50` dummy) and the first derivative (a slope change through `T_post = max(0, time − 50)`).

A second-derivative change represents a change in curvature or acceleration. To test this, I added the squared post-event term, `T_post²`, along with a pre-event `time²` control. The model becomes:

`Y ~ time + D + T_post + time² + T_post²`

I then tested the null hypothesis that the coefficient on `T_post²` equals zero against the alternative that it is not zero, using the usual OLS t-test.

Including `time²` is important because, without it, any smooth background curvature could be attributed to `T_post²`. This would confound pre-existing curvature with a potential event effect.

**Results on the quiz data**

The p-values for the curvature-change tests were:

* Value 1: **0.979**
* Value 2: **0.154**
* Value 3: **0.776**

All three p-values are greater than the significance level of 0.05, so I failed to reject the null hypothesis for each series. Therefore, there is no statistically significant evidence of a second-derivative change in any of the three series.

For comparison, the base level-change p-values were 0.020, 0.095, and 0.000, while the slope-change p-values were 0.000, 0.012, and 0.000, respectively. Value 2's curvature p-value of 0.154 is the closest to statistical significance, but it still does not meet the 0.05 threshold.

Overall, the results suggest that the event effects may be captured by changes in level or slope, without statistically significant evidence of an additional change in curvature.

**Limitations**

Estimating curvature requires enough observations after the event. When there are only a few post-event observations, fitting a quadratic term can produce noisy estimates.

In addition, `time`, `T_post`, `time²`, and `T_post²` can be highly correlated, which may inflate standard errors. Therefore, an insignificant result could mean either that there is no meaningful curvature change or that there is insufficient data to detect one.

A joint F-test of `D`, `T_post`, and `T_post²` would be a useful complement to the individual t-test because it tests whether the event has any effect on the outcome through a level change, a slope change, or a curvature change.
