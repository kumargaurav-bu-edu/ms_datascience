Week 8 Overview
Matching is a powerful alternative to regression for estimating treatment effects when linear assumptions may not hold or when the relationship between variables is complex. This content introduces the concept of matching as a way to “close back doors” by pairing treated and untreated units with similar covariates, enabling more accurate estimation of causal effects. You’ll explore different matching techniques, including distance-based matching, propensity score matching, inverse probability weighting, and kernel-based weighting. The content also covers how to match using one or multiple variables, how to assess balance and common support, and how to handle practical challenges like bias-variance tradeoffs and the curse of dimensionality. By the end, you’ll understand how matching can be used on its own or combined with regression to support valid causal inference. 




Learning Objectives 
At the end of this week, you will be able to: 

Explain matching and its application to average treatment effect (ATE), ATT (average treatment effect on the treated), and ATUT (average treatment effect on the untreated) 
Perform inverse probability weighting and propensity score matching  
Explain matching variants such as the Mahalanobis distance and the Epanechnikov kernel 

Topic Overview 
This section explains how to calculate propensity scores and use them effectively in matching and weighting strategies for causal inference. You'll learn how logistic regression or binning can estimate treatment probabilities and explore practical decisions like how many matches to select, whether to match with or without replacement, and how to assign weights based on distance using kernels like Epanechnikov. The section also introduces inverse probability weighting (IPW), considerations for caliper selection, matching in high-dimensional spaces, and advanced techniques like Mahalanobis distance, coarsened exact matching, and entropy balancing. Finally, you'll see how to validate your propensity score models through stratification tests and how machine learning can enhance score estimation. 

Learning Objectives 
Perform inverse probability weighting and propensity score matching  
Explain matching variants such as the Mahalanobis distance and the Epanechnikov kernel. 

Key Terms and Definitions


Matching: A method for estimating causal effects by pairing treated and untreated units with similar values of confounding variables to simulate a randomized experiment. 
Average Treatment Effect on the Treated (ATT): The average causal effect of a treatment on those who actually received the treatment. 
Weighted Matching: A method where untreated observations are weighted to match the distribution of confounders in the treated group rather than selecting exact matches. 
Distance Matching: A technique that matches treated and untreated observations based on the smallest distance (e.g., Euclidean) between their covariate values. 
Propensity Score Matching: Matching based on the probability of receiving treatment given covariates; units with similar scores are matched to control for confounding. 
Propensity Score: The probability of receiving the treatment, estimated using observed covariates (e.g., via logistic regression). 
Epanechnikov Kernel: A weighting function used in kernel-based matching that assigns weights based on the distance between units, favoring closer matches. 
Inverse Probability Weighting (IPW): A method where each observation is weighted by the inverse of the probability of receiving the treatment (or control) it actually received, to estimate ATE. 
Caliper / Bandwidth: A threshold distance used to restrict acceptable matches; matches outside this range are discarded to improve quality. 
Coarsened Exact Matching: A matching approach where covariates are binned into categories, and matches are made within the same bins across groups. 
Bias-Variance Tradeoff: A fundamental concept where tighter matching (low bias) may increase variability, while looser matching (low variance) may introduce bias. 
Mahalanobis Distance: A distance metric that accounts for correlations among covariates when matching, improving match quality in multivariate settings. 
Curse of Dimensionality: A challenge in high-dimensional matching where most points are approximately equidistant, making meaningful matching difficult. 
Entropy Balancing:A reweighting method that ensures exact balance of specified covariate moments (e.g., means) between treated and control groups. 
Common Support: The condition that there is sufficient overlap in covariate distributions between treated and untreated groups to allow meaningful matching. 
Balance: The degree to which covariate distributions are similar between treated and control groups after matching. 
Balance Table: A table comparing means (and often standard deviations) of covariates across groups to assess the success of matching. 
Bootstrap Simulation: A resampling technique used to estimate standard errors of treatment effects in matching procedures. 
Regression Adjustment: Using regression after matching to control for residual covariate differences and improve precision. 
Double Robust Estimation: A method that combines matching and regression; valid if either model is correctly specified. 
Augmented Inverse Probability Weighted Estimator (AIPWE): A specific double robust estimator that combines outcome modeling and propensity weighting. 
Treatment Effects (ATE, ATT, ATUT): 
ATE: average treatment effect across the entire population 
ATT: Effect on the treated group 
ATUT: Effect on the untreated group 
Stratification Test: A check to ensure that within strata (bins) of the propensity score, covariates are uncorrelated with treatment assignment. 
Selecting Matches: The process of choosing one or more untreated units for each treated unit (or vice versa), often using nearest neighbor, radius, or caliper methods. 
Matching With/Without Replacement: Whether an untreated unit can be matched to multiple treated units (with replacement) or only one (without replacement). 