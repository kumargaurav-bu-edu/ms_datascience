# Predicting Consumer Credit Default Across Two Markets
## Milestone 2 – Modeling Techniques, Evaluation, and Findings

### 1. Project Overview

Consumer credit default prediction is an important application of machine learning because lenders must evaluate borrower risk while balancing lending opportunities against potential financial losses. This project examines whether machine learning techniques can identify patterns associated with consumer credit default and whether those patterns can support different credit-risk decisions.

The analysis uses two datasets representing different lending environments:

- **Lending Club:** A sample of 60,000 closed installment loans drawn from a source population of approximately 1.25 million loans issued between 2007 and 2018. The objective is to predict whether a loan will default by the end of its term.
- **Taiwan Credit Card Clients:** Approximately 30,000 credit card accounts from 2005. The objective is to predict whether a customer will default on the following month's payment.

The datasets provide an opportunity to examine how model performance changes across different populations, feature sets, and prediction horizons. Lending Club represents a loan-origination risk assessment problem, while the Taiwan dataset represents a shorter-term early-warning problem.

This milestone extends the Logistic Regression (LR) and Random Forest (RF) baselines established in Milestone 1 by introducing K-Nearest Neighbors (KNN), Gradient Boosting (GB), K-Means, DBSCAN, and Hierarchical Agglomerative Clustering (HAC).

The project addresses four research questions:

1. Which borrower and account characteristics provide the strongest signals for predicting default?
2. Do the additional modeling techniques improve predictive performance over the Milestone 1 baselines?
3. How do predictive patterns and model performance differ between Lending Club and Taiwan?
4. How could the results support underwriting decisions and early-warning or collections strategies?

**In-depth topics:** This report focuses particularly on Week 8 (KNN) and Week 9 (Gradient Boosting). These techniques provided useful lessons about feature scaling, distance calculations, hyperparameter selection, overfitting, and the importance of comparing models against properly tuned baselines. Weeks 10 and 11 are discussed to explain the value and limitations of unsupervised clustering.

### 2. Data Understanding and Exploratory Data Analysis

The two datasets have different structures and prediction objectives. Lending Club contains six numerical and five categorical features in the analytical dataset, while the Taiwan dataset contains 20 numerical and three categorical features.

A stratified 80/20 train-test split was used for both datasets, with random seed 42. The same test observations were retained across the modeling experiments to make comparisons more consistent. This produced 12,000 Lending Club test observations and 6,000 Taiwan test observations.

Preprocessing included log transformations for selected monetary variables and feature standardization where distance-based modeling required comparable feature scales. Standardization was fitted within each cross-validation training fold to reduce the risk of information leakage.

The default prevalence was approximately 20.28% for Lending Club and 22.13% for Taiwan. This class imbalance made accuracy alone an inadequate evaluation measure. A model could achieve apparently reasonable accuracy by predicting the majority non-default class while failing to identify borrowers who default.

Exploratory Data Analysis (EDA) informed several modeling decisions:

- **Feature scale:** Lending Club monetary variables had substantially larger numerical ranges than several other features. For example, the raw loan amount range was approximately 39,000, compared with an interest-rate range of approximately 27. This difference made standardization important for distance-based algorithms and clustering.
- **Skewness and outliers:** Log transformation reduced the maximum absolute z-score for Lending Club income from approximately 75.6 to 7.84, reducing the influence of extreme values.
- **Repayment history:** In the Taiwan dataset, the PAY_* variables captured historical repayment behavior and provided useful signals for predicting subsequent default.
- **Credit-risk attributes:** Lending Club grade and interest rate represented important risk-related signals. Removing both reduced ROC-AUC by approximately 0.029 in the feature-ablation analysis.
- **Class distribution:** The proportion of defaults in both datasets reinforced the need to evaluate models using ROC-AUC, precision-recall performance, and probability-based metrics rather than accuracy alone.

[Insert Figure 1: Default distribution and key dataset characteristics for Lending Club and Taiwan.]

### 3. Modeling and Evaluation Approach

All supervised models were evaluated using stratified five-fold cross-validation on the training data, followed by evaluation on the held-out test set. Hyperparameters were selected using training data rather than the final test results.

The principal evaluation measures were:

- **ROC-AUC:** Measures the model's ability to rank defaulted accounts above non-defaulted accounts across classification thresholds.
- **PR-AUC / Average Precision:** Focuses on the precision-recall trade-off for the default class, which is particularly relevant when defaults are less common.
- **Brier score:** Measures the mean squared difference between predicted probabilities and actual outcomes. Lower values indicate better probability predictions.
- **F1 score:** Balances precision and recall at a selected classification threshold.

ROC-AUC and PR-AUC were emphasized when comparing predictive ranking performance. A classification threshold of 0.5 was not assumed to be operationally optimal, particularly for models whose predicted probabilities were concentrated below that threshold.

For the comparison between Gradient Boosting and Random Forest, paired bootstrap confidence intervals and DeLong tests were used to assess differences in ROC-AUC. Bootstrap analysis used 5,000 resamples. These analyses helped distinguish small numerical differences from differences supported by statistical evidence.

### 4. Week 8 Deep Dive: K-Nearest Neighbors

#### 4.1 Why KNN was explored

KNN predicts an observation's outcome based on the outcomes of nearby observations in feature space. Unlike Logistic Regression, it does not assume a predefined linear relationship between predictors and the outcome.

KNN was particularly interesting for this project because it allowed the analysis to examine whether borrower similarity could provide useful predictive information. However, its performance depends heavily on feature representation, distance calculations, and the number of neighbors selected.

#### 4.2 Feature scaling and distance metrics

Feature scaling was one of the most important findings from the KNN experiments. Without appropriate scaling, variables with large numerical ranges can dominate distance calculations even when they are not proportionally more informative.

The experiments evaluated different distance metrics and neighborhood configurations. Manhattan and Euclidean distances were considered, along with distance-weighted and uniform neighbor voting.

The Lending Club validation AUC improved from 0.6161 to 0.6901 after correcting the feature-scaling approach and evaluating a fixed KNN configuration using k=51 and Euclidean distance. Taiwan validation AUC improved from 0.7485 to 0.7717.

These improvements demonstrated that KNN performance was not determined solely by the algorithm. The representation and scale of the input features materially affected the similarity calculations.

The expanded tuning experiments selected different configurations for the two datasets:

- **Lending Club:** k=1,602, Manhattan distance, and distance-weighted voting.
- **Taiwan:** k=202, Euclidean distance, and uniform voting.

The selected configurations illustrate that the optimal neighborhood structure differed across the datasets. Lending Club required a much larger neighborhood, while Taiwan performed best with a smaller one.

[Insert Figure 2: KNN validation performance across selected distance metrics and neighborhood configurations.]

#### 4.3 Overfitting and generalization

KNN can overfit when the neighborhood is too small, particularly when k=1, because predictions can become highly sensitive to individual observations. Increasing k generally smooths predictions by incorporating more neighbors, although an excessively large neighborhood can reduce the model's ability to capture local patterns.

The selected configurations were evaluated using cross-validation and an independent test set.

| Dataset | KNN training AUC | CV AUC | Test AUC |
|---|---:|---:|---:|
| Lending Club | 1.0000 | 0.7023 | 0.7097 |
| Taiwan | 0.7800 | 0.7718 | 0.7610 |

The Lending Club training AUC of 1.0000 requires careful interpretation. With a large neighborhood and self-comparison in the training evaluation, an observation can be included among its own zero-distance neighbors. This can make the training score overly optimistic. Therefore, the training AUC should not be interpreted as evidence that the model generalizes perfectly.

The cross-validation and independent test results provide a more realistic assessment. Lending Club test AUC was 0.7097, while Taiwan test AUC was 0.7610. The smaller difference between cross-validation and test performance suggests that the selected configurations generalized reasonably well, although the Lending Club training score demonstrates why training performance alone is insufficient.

#### 4.4 Metrics and threshold selection

At the default classification threshold of 0.5, the Lending Club KNN model predicted no positive cases, producing an F1 score of zero. This did not mean the model had no predictive value. Its predicted probabilities were concentrated around the underlying default prevalence and generally did not exceed 0.5.

To investigate the operational implications, an alternative threshold was selected using out-of-fold predictions from the training data. A threshold of 0.21 was then applied to the independent test set, producing an F1 score of 0.431.

This demonstrates why threshold selection should be separated from model ranking. ROC-AUC evaluates ranking performance across thresholds, while F1 measures performance at one selected threshold. A lower threshold can identify more potential defaulters, but it may also increase false positives. The appropriate operating point therefore depends on the relative costs of missed defaults and unnecessary interventions.

[Insert Figure 3: KNN ROC or precision-recall comparison, including the effect of threshold selection.]

#### 4.5 What was expected and unexpected

It was expected that KNN would be sensitive to scaling because it relies on distance calculations. The magnitude of the improvement after correcting the scaling approach reinforced this expectation.

A less expected result was the competitive Lending Club performance. Its test AUC of 0.7097 was nearly identical to the tuned Random Forest result of 0.7099. The Taiwan result was less competitive: KNN test AUC of 0.7610 was below Gradient Boosting at 0.7737 and Random Forest at 0.7733.

Overall, KNN was a useful alternative for Lending Club, but it did not consistently outperform the tree-based models across both markets.

### 5. Week 9 Deep Dive: Gradient Boosting

#### 5.1 Why Gradient Boosting was explored

Gradient Boosting builds an ensemble of decision trees sequentially. Each new tree attempts to improve the errors made by the existing ensemble. This approach can capture nonlinear relationships and interactions without requiring the same feature transformations as distance-based models.

Gradient Boosting was introduced to determine whether a sequential boosting approach could improve upon the Milestone 1 Logistic Regression and Random Forest baselines.

#### 5.2 Hyperparameter tuning and overfitting controls

The experiments evaluated learning-rate and tree-depth configurations, followed by a regularization grid. Parameters included minimum samples per leaf, subsampling, and minimum impurity decrease.

These parameters influence model complexity:

- **Learning rate:** Controls how much each new tree contributes to the ensemble. Smaller values generally produce more gradual learning.
- **Tree depth:** Controls how complex the individual trees can become. Deeper trees can capture more complex interactions but may overfit.
- **Minimum samples per leaf:** Requires a minimum number of observations in terminal nodes, reducing overly specific splits.
- **Subsampling:** Uses a portion of the training observations when fitting each boosting iteration, which can introduce useful variation and reduce overfitting.
- **Minimum impurity decrease:** Requires a minimum improvement before a split is accepted, discouraging weak or unnecessary splits.

The regularization experiments selected a minimum leaf size of 20 and a subsample fraction of 0.8. The additional grid search produced only approximately 0.0005 improvement in cross-validation AUC for each dataset.

This small improvement suggested that the initial Gradient Boosting configuration was already close to the best-performing region of the tested parameter space. It also indicated that additional tuning did not necessarily translate into meaningful predictive gains.

The training, cross-validation, and test results were:

| Dataset | Training AUC | CV AUC | Test AUC |
|---|---:|---:|---:|
| Lending Club | 0.7218 | 0.7048 | 0.7136 |
| Taiwan | 0.8133 | 0.7845 | 0.7737 |

The training-to-CV gaps were approximately 0.017 for Lending Club and 0.029 for Taiwan. These gaps indicate some degree of fitting to the training data, but the test results remained reasonably close to cross-validation performance.

One methodological qualification is important: the Gradient Boosting cross-validation result was taken from the regularization-grid search, whereas the reported Random Forest and Logistic Regression cross-validation results came from fresh five-fold evaluations. The protocols were not perfectly identical, so the cross-validation gaps should be interpreted cautiously. A same-protocol comparison would provide a stronger assessment.

[Insert Figure 4: Gradient Boosting tuning results showing the effect of selected hyperparameters on validation performance.]

#### 5.3 Corrected comparison with the Milestone 1 Random Forest

An important development in this milestone was the correction of the Random Forest baseline used in the initial comparison.

Earlier comparisons used an untuned Random Forest configuration rather than the actual tuned Milestone 1 winners. This made the original Gradient Boosting advantage appear larger than it was. The comparison was therefore repeated using the correct Milestone 1 Random Forest configurations:

- Lending Club: minimum samples per leaf of 20, square-root feature selection, and balanced class weights.
- Taiwan: minimum samples per leaf of 50, 0.3 feature selection, unlimited tree depth, and balanced-subsample class weights.

The corrected test results were:

| Dataset | Model | ROC-AUC | PR-AUC |
|---|---|---:|---:|
| Lending Club | Logistic Regression | 0.7125 | 0.3784 |
| Lending Club | Random Forest | 0.7099 | 0.3801 |
| Lending Club | Gradient Boosting | 0.7136 | 0.3829 |
| Taiwan | Logistic Regression | 0.7394 | 0.5029 |
| Taiwan | Random Forest | 0.7733 | 0.5507 |
| Taiwan | Gradient Boosting | 0.7737 | 0.5568 |

For Lending Club, Gradient Boosting improved ROC-AUC over Random Forest by 0.0037. The paired comparison produced a 95% confidence interval of [0.0010, 0.0062], indicating a statistically supported but small improvement.

For Taiwan, the ROC-AUC difference was only 0.0003, with a 95% confidence interval of [-0.0037, 0.0043]. This interval includes zero, so the results do not establish a meaningful ROC-AUC improvement over Random Forest.

The PR-AUC confidence intervals for both datasets also included zero. Therefore, the analysis does not establish a statistically reliable PR-AUC improvement for Gradient Boosting over Random Forest.

[Insert Figure 5: Corrected test-set comparison of Gradient Boosting, tuned Random Forest, and Logistic Regression.]

#### 5.4 Probability quality and an unexpected finding

The Brier scores provided another perspective on model performance:

| Dataset | Logistic Regression | Random Forest | Gradient Boosting |
|---|---:|---:|---:|
| Lending Club | 0.1465 | 0.2132 | 0.1463 |
| Taiwan | 0.1445 | 0.1753 | 0.1355 |

Gradient Boosting and Logistic Regression produced lower Brier scores than Random Forest in both datasets. Random Forest's relatively high Brier scores, despite competitive ROC-AUC, suggest that its probability estimates may not be well aligned with observed default frequencies.

One possible explanation is the use of class weighting in Random Forest, which may affect the scale of predicted probabilities. However, this analysis does not establish class weighting as the cause. Further calibration experiments, such as isotonic calibration, would be needed to test that explanation.

The comparison also demonstrates that ranking performance and probability quality are different aspects of model evaluation. A model may rank borrowers effectively while producing probabilities that are less suitable for estimating actual default likelihood.

#### 5.5 What was expected and unexpected

It was expected that Gradient Boosting could capture nonlinear patterns and potentially improve upon the existing models. The unexpected finding was how little its advantage remained after correcting the Random Forest baseline.

The corrected results changed the original interpretation: Gradient Boosting provided a marginal ROC-AUC improvement for Lending Club, but no measurable ROC-AUC improvement for Taiwan. This was an important methodological lesson. A model comparison is only meaningful when the baseline is correctly specified and evaluated consistently.

### 6. Weeks 10 and 11: Unsupervised Clustering

K-Means, DBSCAN, and Hierarchical Agglomerative Clustering were explored to determine whether unsupervised techniques could reveal borrower segments with different default characteristics.

#### 6.1 K-Means and silhouette score

K-Means partitions observations into clusters by minimizing within-cluster squared distances. The silhouette score measures how well observations fit within their assigned clusters relative to neighboring clusters.

Although the silhouette score favored k=2, k=4 was selected as a more descriptive compromise for examining borrower segments. The four-cluster solution revealed differences in default rates:

- Lending Club cluster default rates ranged from approximately 13.6% to 32.4%.
- Taiwan cluster default rates ranged from approximately 15.4% to 58.8%.

These differences suggested that unsupervised clustering could identify groups with different observed risk levels. However, the cluster assignments did not improve Gradient Boosting performance when added as additional features.

[Insert Figure 6: Default rates across K-Means or hierarchical clusters for both datasets.]

#### 6.2 DBSCAN and hierarchical agglomerative clustering

DBSCAN identifies dense regions of observations and labels observations outside those regions as noise. In Lending Club, the selected density configuration produced two clusters, but further examination showed that the split largely reflected loan-term differences. Taiwan produced one connected mass, indicating that DBSCAN did not identify similarly distinct density-based segments.

Ward hierarchical clustering produced more interpretable segments in Taiwan. The four clusters had default rates of approximately 12.6%, 19.2%, 21.8%, and 58.1%. The highest-risk cluster represented approximately 10.5% of applicants but 27% of defaulters, corresponding to approximately 2.6 times the overall default rate.

This was a potentially useful segmentation for prioritizing early-warning or collections attention. However, adding the Ward cluster and DBSCAN noise indicator to Gradient Boosting did not produce measurable predictive improvement.

An important finding was that a high silhouette score did not necessarily indicate greater business usefulness. For Lending Club, a single-cluster solution had a silhouette score of 0.591, while the Ward solution had a score of 0.120. The lower-scoring solution could still provide more useful risk segmentation.

The clustering results therefore supported descriptive analysis and risk segmentation, rather than improved supervised prediction.

### 7. Comparative Findings and Conclusions

The experiments provide several answers to the project's research questions.

**Research Question 1: Which features provide the strongest default signals?**

The analysis identified different predictive patterns across the two markets. In Taiwan, repayment-history variables were important signals for next-month default. In Lending Club, credit grade and interest rate were among the strongest individual predictive signals. Removing both reduced ROC-AUC by approximately 0.029, indicating that these attributes contributed meaningful predictive information. However, their importance should be considered in the context of responsible lending, since credit-related attributes may reflect historical or structural disadvantages.

**Research Question 2: Did the additional techniques outperform the Milestone 1 baselines?**

The results show that adding algorithms did not consistently improve prediction.

- Lending Club Gradient Boosting achieved a test ROC-AUC of 0.7136, compared with 0.7099 for tuned Random Forest. The improvement was statistically supported but small.
- Taiwan Gradient Boosting achieved 0.7737, compared with 0.7733 for Random Forest. The difference was not statistically distinguishable from zero.
- KNN was competitive with Random Forest in Lending Club, with test AUC of 0.7097, but performed below both tree-based models in Taiwan.
- Clustering revealed descriptive risk segments but did not provide measurable predictive lift when incorporated into Gradient Boosting.

These results reinforce the importance of evaluating new models against properly tuned baselines rather than assuming that a more complex algorithm will perform better.

**Research Question 3: How do patterns differ across the two markets?**

The Taiwan dataset showed stronger overall discrimination for the leading models, with Gradient Boosting ROC-AUC of 0.7737 compared with 0.7136 for Lending Club. The feature sets and prediction horizons differ substantially, so this difference should not be interpreted as evidence that one market is inherently easier to predict. Taiwan provides repayment-history information for a one-month-ahead prediction, whereas Lending Club predicts default over the life of a loan using origination-related information.

**Research Question 4: How could the findings support credit-risk decisions?**

For Lending Club, the models could support underwriting risk ranking at loan origination. Credit grade and interest rate provide useful signals, but probability calibration and threshold selection would be important before using predictions to guide lending decisions.

For Taiwan, repayment-history patterns and the high-risk hierarchical cluster could support early-warning prioritization. The highest-risk cluster's 58.1% default rate and approximately 2.6-times lift suggest that segmentation may help prioritize customer outreach. Such use would require validation on more recent data and assessment of false-positive costs.

Overall, Milestone 2 demonstrates that introducing additional algorithms does not necessarily translate into better predictive performance. Gradient Boosting provides limited improvement over the tuned Random Forest, KNN offers a competitive alternative in Lending Club, and clustering contributes descriptive segmentation rather than measurable predictive lift. The results reinforce the importance of appropriate baselines, feature representation, probability calibration, and operational threshold selection when evaluating machine learning models for consumer credit risk.

### 8. Limitations and Future Work

Several limitations should be considered when interpreting the results.

First, Lending Club uses a 60,000-observation sample rather than the full source population. The additional sample-size experiment comparing 60,000, 120,000, and 240,000 observations used separate train-test draws, making sample size and data composition difficult to distinguish.

Second, both datasets use random stratified splits rather than time-based validation. Consequently, the reported results do not establish how well the models would generalize to future economic conditions or changing borrower populations.

Third, some post-hoc analyses, including calibration and feature-ablation investigations, used the test set. Although they did not guide the original hyperparameter choices, this means the test set should no longer be regarded as a completely untouched final evaluation set.

Fourth, cross-market comparisons are affected by different target definitions, feature availability, and prediction horizons.

Future work should include time-based validation, nested cross-validation, additional probability-calibration experiments, and a more detailed evaluation of operational thresholds. Further analysis of the Taiwan repayment-history features and the stability of high-risk clusters would also help determine whether these findings remain useful outside the original samples.

### 9. External Learning Resources and References

The following external sources informed the selection, implementation, and evaluation of the modeling techniques. The associated notebook experiments and YellowDig discussions provide additional evidence of how the concepts were applied to the project.

**References**

- Breiman, L. (2001). Random forests. *Machine Learning, 45*, 5–32.
- Cover, T., & Hart, P. (1967). Nearest neighbor pattern classification. *IEEE Transactions on Information Theory, 13*(1), 21–27.
- DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated receiver operating characteristic curves. *Biometrics, 44*(3), 837–845.
- Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of the Second International Conference on Knowledge Discovery and Data Mining*.
- Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. *The Annals of Statistics, 29*(5), 1189–1232.
- MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability*.
- Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65.
- Ward, J. H. (1963). Hierarchical grouping to optimize an objective function. *Journal of the American Statistical Association, 58*(301), 236–244.
- Yeh, I.-C., & Lien, C.-H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. *Expert Systems with Applications, 36*(2), 2473–2480.

*Before submission, add the exact Lending Club dataset source, the scikit-learn version used, and the external educational URLs and YellowDig discussion links associated with your work. Include in-text citations at the relevant model descriptions and methodology discussions.*

### 10. AI Usage Disclosure

AI tools were used as supplementary assistance during the development and review of this project. Their use included code review, grammatical corrections, restructuring code for clarity, identifying potential gaps against the assignment rubric, and reviewing modeling methodology.

AI assistance also helped identify an inconsistency in the initial comparison between Gradient Boosting and Random Forest, leading to a corrected comparison using the tuned Milestone 1 Random Forest configurations.

All modeling decisions, experimental results, interpretations, and final conclusions were reviewed against the project notebooks and analysis outputs. The author remains responsible for the submitted work and its conclusions.

### Appendix: Supporting Project Materials

The supporting notebooks document the experiments conducted throughout the milestone:

- Week 6: Logistic Regression and Random Forest baselines.
- Week 8: KNN distance metrics, feature scaling, and hyperparameter tuning.
- Week 9: Gradient Boosting experiments and corrected baseline comparisons.
- Week 10: K-Means clustering and silhouette analysis.
- Week 11: DBSCAN and hierarchical agglomerative clustering.

The corresponding GitHub repository and YellowDig discussion links should be included in the final submission.