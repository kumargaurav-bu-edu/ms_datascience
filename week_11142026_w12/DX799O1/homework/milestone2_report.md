# Predicting Consumer Credit Default Across Two Markets

**Milestone 2 — DX799 O1 Data Science Capstone**
**Kumar Gaurav · Boston University · Fall 2026**

---

## 1. Project statement and research questions

This capstone examines whether machine learning can predict consumer credit default in two very different lending markets. The datasets are U.S. Lending Club (approximately 1.25 million closed installment loans from 2007 to 2018, 20.28 % default rate — a loan-origination risk problem) and Taiwan credit-card clients (approximately 30,000 accounts from 2005, 22.13 % default rate — an early-warning problem one month out). Default prediction matters because lenders must price risk fairly, set loss provisions accurately, and intervene early on borrowers likely to miss payments. Milestone 1 established Logistic Regression and Random Forest baselines; Milestone 2 adds K-Nearest Neighbors, Gradient Boosting, K-Means, DBSCAN, and Hierarchical Agglomerative Clustering, and asks whether these add predictive, interpretive, or operational value. Four research questions carry over from Milestone 1: which features drive default; whether the Milestone 2 methods improve on the baselines; how indicators differ across markets; and how the findings could support Lending Club underwriting and Taiwan early-warning or collections-triage work.

## 2. Dataset and exploratory data analysis

| Property | Lending Club | Taiwan |
|---|---|---|
| Rows used | 60,000 random sub-sample of 1.25M | 30,000 (full) |
| Features | 6 numeric + 5 categorical | 20 numeric + 3 categorical |
| Target | Default by end-of-term (36 or 60 months) | Default next month (October 2005) |
| Prediction point | Underwriting at origination | Early-warning one month out |
| Shared split | 80/20 stratified, random seed 42; identical test rows across Weeks 6, 8, and 9 (12,000 Lending Club, 6,000 Taiwan) |

Both datasets are class-imbalanced at 20–22 % default, so overall accuracy alone is not useful — a model that always predicts "no default" would look accurate while failing to identify any actual defaulter. The 60,000-row Lending Club sub-sample is a compute compromise; a sample-size comparison at 60k / 120k / 240k rows is confounded because each size draws its own train-test split.

Exploratory data analysis guided several modeling decisions. Log-transforming the money columns reduced the maximum absolute z-score of Lending Club annual income from 75.6 to 7.84, so extreme outliers no longer dominated gradient-boosted splits or distance calculations. The raw Lending Club loan amount range (39,000) versus interest-rate range (27) — a ratio of about 1,444 — explained why unscaled K-Means and K-Nearest Neighbors behaved poorly, making feature standardization a correctness requirement. The Taiwan PAY_* columns emerged as the strongest predictive block for next-month default, and a tie-detection check on those columns explained a 1/k discrepancy between a hand-rolled K-Nearest Neighbors probability and the scikit-learn implementation.

## 3. Breadth across Weeks 8–11

| Week · Technique | Selected configuration | Key quantitative result | Headline finding |
|---|---|---|---|
| 8 · K-Nearest Neighbors | LC: k = 1,602, Manhattan, distance-weighted. TW: k = 202, Euclidean, uniform | Test ROC-AUC: LC 0.7097, TW 0.7610 | Scaling is decisive (§5); threshold selection moves LC F1 from 0 to 0.431 |
| 9 · Gradient Boosting | Both markets: min_samples_leaf = 20, subsample = 0.8, depth 3, learning rate 0.1 | Test ROC-AUC: LC 0.7136, TW 0.7737 | Regularization grid gains only 0.0005 over default — same config optimal for both markets |
| 10 · K-Means | k = 4 on standardized features (silhouette favored k = 2) | TW cluster default-rate spread 15.4 %–58.8 %; LC spread 13.6 %–32.4 % | TW highest-risk cluster is defined by elevated PAY_* values; adding cluster id to GB adds no predictive lift |
| 11 · DBSCAN | eps at knee of k-distance; min_samples = 5 | LC 2 clusters; DBCV = −0.0949 vs silhouette 0.239 | The two LC clusters are the binary loan-term split, not a true density gap |
| 11 · Ward HAC | k = 4 linkage | TW default rates 12.6 / 19.2 / 21.8 / 58.1 %; H3 holds 10.5 % of applicants, 27 % of defaulters | Silhouette ranks LC linkages in reverse of usefulness (single 0.591 vs Ward 0.120; **Figure 4**) |

## 4. Deep-dive: Gradient Boosting versus the Milestone 1 Random Forest

This report develops two topics in depth: **Gradient Boosting (Week 9)**, the central candidate for the question "does boosting improve on Random Forest," and **K-Nearest Neighbors (Week 8)**, which carries the clearest feature-scaling and threshold-tuning lessons. Clustering stays in the breadth section because both supervised-utility bridges (adding cluster labels as model features) produced no predictive lift.

### 4.1 Why Gradient Boosting was explored

Gradient Boosting builds an ensemble of shallow decision trees sequentially, each fit to the residual error of the existing ensemble. Unlike Logistic Regression it can capture nonlinear relationships without manual transformation, and unlike Random Forest it extracts signal serially rather than from parallel bagged trees. It was explored to answer whether this approach would improve on the Milestone 1 baselines.

### 4.2 Hyperparameter tuning

Three hyperparameter groups were tuned using grid search on 5-fold cross-validation: **learning rate** (how much each new tree contributes to the ensemble; smaller values generalize better but need more trees), **tree depth** (how complex a single tree can become; deeper trees capture more interactions but overfit faster), and a **regularization grid** covering `min_samples_leaf` (minimum rows per leaf, blocking splits that fit only a handful of borrowers), `subsample` (fraction of training rows each tree sees, adding useful randomness), and `min_impurity_decrease` (minimum split-quality improvement required). The regularization grid gained only 0.0005 cross-validation ROC-AUC over the default and settled on the same configuration for both markets (`min_samples_leaf = 20`, `subsample = 0.8`) — itself a finding, since the same regularization was optimal across two very different credit populations. Final test ROC-AUC: 0.7136 Lending Club, 0.7737 Taiwan (full train/CV/test numbers in §6).

### 4.3 Corrected comparison with the Milestone 1 Random Forest

The central comparison required fixing a setup error: Weeks 8 and 9 originally benchmarked Gradient Boosting against an untuned Random Forest that matched neither per-dataset winner from Milestone 1. The baseline was replaced with the tuned Milestone 1 winners (Lending Club: minimum samples per leaf 20, square-root feature selection, balanced class weights; Taiwan: minimum samples per leaf 50, 0.3 feature selection, unlimited depth, balanced-subsample), and the paired bootstrap (5,000 resamples) and DeLong test were re-run.

| Dataset | Model | Test ROC-AUC | Test PR-AUC | vs tuned RF, ROC Δ, 95 % CI | Verdict |
|---|---|---:|---:|---|---|
| Lending Club | Gradient Boosting | **0.7136** | 0.3829 | **+0.0037, [+0.0010, +0.0062]** | Marginal |
| Lending Club | Random Forest | 0.7099 | 0.3801 | — | Baseline |
| Lending Club | Logistic Regression | 0.7125 | 0.3784 | — | Tied |
| Taiwan | Gradient Boosting | **0.7737** | **0.5568** | **+0.0003, [−0.0037, +0.0043]** | Tied |
| Taiwan | Random Forest | 0.7733 | 0.5507 | — | Baseline |
| Taiwan | Logistic Regression | 0.7394 | 0.5029 | — | GB − LR +0.0343 |

**Figure 2** shows the ROC curves. Gradient Boosting shows no measurable improvement over the tuned Random Forest on Taiwan (PR-AUC interval [−0.0030, +0.0152] includes zero) and only a marginal ROC-AUC gain on Lending Club (PR-AUC interval [−0.0036, +0.0090] also includes zero). The earlier "clearly beats" interpretation does not survive the Milestone 1 tuning — every downstream conclusion in this report depends on that correction.

### 4.4 Probability quality: Brier loss

Where Gradient Boosting does show an advantage is in observed Brier score, which measures how well predicted probabilities match actual outcomes. A constant-prevalence predictor scores π(1 − π) — 0.1617 for Lending Club and 0.1723 for Taiwan. Gradient Boosting beats that baseline by 0.015 and 0.037; Logistic Regression by 0.015 and 0.028; the class-weighted Random Forest is worse than baseline on both (0.2132 and 0.1753). Random Forest Brier worse than a constant predictor despite healthy ROC-AUC indicates probability-scale distortion, most plausibly the balanced class weighting (Gradient Boosting and Logistic Regression are unweighted here). The reliability diagram (**Figure 3**) isolates the calibration component. The defensible claim is that Gradient Boosting has lower observed Brier on these samples, not that it is inherently better calibrated. This matters because loss provisioning and risk-based pricing rely on well-calibrated probabilities, not just correct ranking — a model whose probabilities are shifted away from actual default frequencies would mis-size reserves and mis-price loans. Isotonic calibration on the Random Forest is a proposed next step.

### 4.5 What was expected and unexpected

Expected: boosting's sequential error-correction could extract more signal than parallel bagging. Not expected: once Random Forest was tuned to its Week 6 winners, the Gradient Boosting advantage largely disappeared, and Gradient Boosting's observed Brier was markedly better than the class-weighted Random Forest's — with Random Forest actually worse than a constant-prevalence predictor. Both surprises only emerged after the baseline correction.

## 5. Deep-dive: K-Nearest Neighbors — scaling, threshold tuning, and a competitive ceiling

### 5.1 Why K-Nearest Neighbors was explored

K-Nearest Neighbors predicts an outcome from the labels of nearby observations rather than fitting a global decision rule, which makes it a natural way to ask whether "similar borrowers behave similarly." It also makes feature scaling and distance choice first-order modeling decisions — the main lesson this deep-dive develops.

### 5.2 Feature scaling and distance metrics

Feature scaling was the most consequential finding. With a fixed k = 51 and Euclidean distance, applying StandardScaler lifted ROC-AUC from 0.6161 to 0.6901 on Lending Club and from 0.7485 to 0.7717 on Taiwan (**Figure 1**). Without it, large-magnitude columns like loan amount dominate the distance calculation regardless of their actual predictive value. The expanded tuning search then selected k = 1,602 with Manhattan distance and distance-weighted voting on Lending Club, and k = 202 with Euclidean distance and uniform voting on Taiwan — different winners suggesting the two feature spaces have genuinely different local structure.

### 5.3 Overfitting and generalization

The Lending Club training score of 1.0000 (§6) is not a real overfitting signal: at k = 1,602 with distance weighting, each training observation is its own zero-distance neighbor, so the training prediction is always its own label. The Taiwan row (k = 202, uniform voting, train minus cross-validation gap 0.008) is a more interpretable estimate because the self-vote contributes only 1 part in 202.

### 5.4 Metrics and threshold selection

Tuned K-Nearest Neighbors reached 0.7097 ROC-AUC on Lending Club — essentially a dead-heat with the Milestone 1 Random Forest (0.7099, DeLong p = 0.840) and tied with Logistic Regression (0.7125). On Taiwan it reached 0.7610, significantly below both tree ensembles (differences of −0.0127 versus Gradient Boosting and −0.0123 versus Random Forest; both confidence intervals exclude zero). At the default 0.5 threshold, the Lending Club model never predicted a positive class because its predicted probabilities concentrated around the 0.20 base rate. This did not mean the model lacked predictive value. Selecting a lower threshold of 0.21 from out-of-fold training predictions (the test set was not used for selection) moved the test F1 score from 0 to 0.431. **The operational message is that operating-point selection changes real-world outcomes more than hyperparameter tuning does on this data.**

### 5.5 What was expected and unexpected

Expected: scaling sensitivity (confirmed). Not expected: how competitive K-Nearest Neighbors remained on Lending Club — tying the tuned Milestone 1 Random Forest (DeLong p = 0.840) despite using no tree-interaction information. Taiwan's repayment-history features plausibly reward tree-ensemble interactions that K-Nearest Neighbors' isotropic distance cannot exploit; a partial-dependence analysis is a Milestone-3 follow-up.

## 6. Overfitting and metrics across all models

The train-minus-cross-validation gap is a cleaner overfitting diagnostic than a single train-minus-test gap. Consolidated across all four supervised models and both datasets (train / cross-validation / test ROC-AUC):

| Model | Lending Club train | LC CV | LC OOB | LC test | Taiwan train | TW CV | TW test |
|---|---:|---:|---:|---:|---:|---:|---:|
| K-Nearest Neighbors | 1.0000 | 0.7023 | — | 0.7097 | 0.7800 | 0.7718 | 0.7610 |
| Gradient Boosting | 0.7218 | 0.7048 | — | 0.7136 | 0.8133 | 0.7845 | 0.7737 |
| Random Forest | 0.7602 | 0.7047 | 0.7029 | 0.7099 | 0.8489 | 0.7864 | 0.7733 |
| Logistic Regression | 0.7047 | 0.7034 | — | 0.7125 | 0.7511 | 0.7498 | 0.7394 |

Train minus cross-validation gaps: Gradient Boosting 0.017 Lending Club and 0.029 Taiwan, Random Forest 0.056 and 0.063, Logistic Regression ≈ 0 on both. Gradient Boosting's smaller gap is consistent with its leaf-size and subsampling regularization. The Random Forest out-of-bag score tracks the 5-fold cross-validation mean on both datasets (0.7029 vs 0.7047 Lending Club; 0.7864 vs 0.7864 Taiwan), independently confirming the Random Forest test score is not inflated. The Lending Club K-Nearest Neighbors training score of 1.0000 is a self-matching artefact at k = 1,602 with distance weighting, not an overfitting signal (§5.3).

**Metrics summary.** ROC-AUC measures how well a model ranks defaulters above non-defaulters across all thresholds. PR-AUC (`average_precision_score`) focuses on precision and recall for the minority default class — more informative under 20–22 % class imbalance. Brier score measures how well predicted probabilities match actual outcomes (lower is better-calibrated, not just better-ranked). F1/precision/recall are reported only at thresholds chosen from out-of-fold training predictions; the Milestone 1 Random Forest is class-weighted and the others unweighted, so threshold metrics are not like-for-like. Significance: paired bootstrap at 5,000 resamples with 95 % confidence intervals at the 2.5/97.5 percentiles, with DeLong's test as a second check on ROC-AUC pairs.

**Clustering stability and the supervised-utility bridge.** The clustering analog of overfitting is resampling stability: Ward at k = 4 produced bootstrap Adjusted Rand Indices of 0.46 on Lending Club and 0.57 on Taiwan (partially stable), while K-Means produced 0.93. Neither clustering bridge (adding cluster identifiers as Gradient Boosting features) produced measurable predictive lift, so the clustering findings are descriptive rather than predictive — the most operationally interesting result is the Ward H3 Taiwan segment described in §3. The most transferable methodological lesson is that silhouette alone cannot be trusted to select a hierarchical linkage method without also checking cluster-size balance (**Figure 4**).

## 7. Limitations and future research

All significance tests use the corrected per-dataset Milestone 1 Random Forest. The Lending Club 60,000-row sub-sample is not the full population; the sample-size comparison is confounded because each size drew its own split. Both datasets use random 80/20 splits rather than time-based validation, so results do not establish how the models would generalize to changing economic conditions. Post-hoc diagnostics on the test set (calibration, permutation importance, ablations) did not feed into model selection but mean it is not a fully independent final evaluation. Clustering stability is single-sample. The cross-market contrast is a hypothesis — the two datasets differ in target horizon, feature family, and sample size. Priority next steps: a time-based Lending Club split, nested cross-validation, isotonic calibration on the Random Forest, a leakage-protected out-of-fold cluster assignment, and a precision-at-fixed-recall comparison.

## 8. Final conclusions — answers to the four research questions

**Which features drive default?** On Lending Club, the largest single signal is the lender-assigned interest rate and credit grade (endogenous to Lending Club's own scorecard); borrower-only features retain about 86 % of the AUC-above-chance lift. On Taiwan, the six-month PAY_* block dominates.

**Do Milestone 2 techniques beat the baselines?** Against the tuned Milestone 1 Random Forest, Gradient Boosting shows no measurable Taiwan improvement (ROC-AUC +0.0003, CI straddles zero) and only a marginal Lending Club gain (+0.0037, [+0.0010, +0.0062]; PR-AUC inconclusive). Gradient Boosting clearly beats Logistic Regression on Taiwan (+0.0343). K-Nearest Neighbors ties Random Forest on Lending Club but loses on Taiwan. Clustering adds no measurable supervised prediction.

**How do indicators differ across markets?** Taiwan produces higher observed ROC-AUC and sharper cluster separation, but the two markets differ in target horizon, feature family, and sample size — the AUC gap is not evidence one market is intrinsically more predictable.

**Operational implications and responsible use.** Lending Club underwriting: ranking alone does not justify replacing Milestone 1 Random Forest with Gradient Boosting; Gradient Boosting's lower observed Brier needs calibration analysis first. Taiwan early-warning: Gradient Boosting is a stronger alternative to Logistic Regression, and the Ward H3 segment (10.5 % of applicants, 27 % of defaulters, 2.6-times lift) is a potential collections-prioritization input to investigate. These models identify predictive patterns but should not drive standalone lending or collections decisions — fairness, proxy discrimination, explainability, calibration, and regulatory requirements all require assessment before deployment.

## 9. References

- Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5–32.
- Campello, R. J. G. B., Moulavi, D., & Sander, J. (2013). Density-based clustering based on hierarchical density estimates. *PAKDD*, LNAI 7819, 160–172.
- Cover, T. M., & Hart, P. E. (1967). Nearest neighbor pattern classification. *IEEE Transactions on Information Theory*, 13(1), 21–27.
- DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988). Comparing the areas under two or more correlated ROC curves: a nonparametric approach. *Biometrics*, 44(3), 837–845.
- Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of KDD-96*, 226–231.
- Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. *Annals of Statistics*, 29(5), 1189–1232.
- MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the 5th Berkeley Symposium on Mathematical Statistics and Probability*, 281–297.
- Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53–65.
- Sun, X., & Xu, W. (2014). Fast implementation of DeLong's algorithm for comparing the areas under correlated receiver operating characteristic curves. *IEEE Signal Processing Letters*, 21(11), 1389–1393.
- Ward, J. H. (1963). Hierarchical grouping to optimize an objective function. *Journal of the American Statistical Association*, 58(301), 236–244.
- Yeh, I.-C., & Lien, C.-H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. *Expert Systems with Applications*, 36(2), 2473–2480.

**External educational resources (shared on YellowDig):**

- scikit-learn developers. *User Guide*. [https://scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html)
- scikit-learn developers. *Clustering — DBSCAN*. [https://scikit-learn.org/stable/modules/clustering.html#dbscan](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
- VanderPlas, J. *Python Data Science Handbook — Random Forests*. [https://jakevdp.github.io/PythonDataScienceHandbook/05.08-random-forests.html](https://jakevdp.github.io/PythonDataScienceHandbook/05.08-random-forests.html)
- Lending Club public loan-book documentation.

## 10. AI Usage Appendix

Generative AI tools were used as an assistive resource for: (1) code review for readability and consistency; (2) grammar and language correction; (3) rubric-alignment gap analysis; (4) code restructuring without changing the analytical approach; and (5) a methodological review that identified the Random Forest baseline used in Weeks 8 and 9 did not match the tuned per-dataset configuration selected in Milestone 1 — correcting it and re-running the paired-bootstrap and DeLong tests changed the comparison from "Gradient Boosting clearly beats Random Forest" to "no measurable improvement on Taiwan, marginal on Lending Club" (§4.3). All final decisions, analysis, and validation were performed and reviewed by the author; AI suggestions were evaluated against source notebook outputs before incorporation.

---

**Appendix A — Figures (referenced from body text by figure number):**

| Figure and caption | Image |
|---|---|
| **Figure 1.** K-Nearest Neighbors train versus validation ROC-AUC across k. At k = 1 the model memorises training data; at k far above 100 it regularises toward the base rate. Supports §5.2. | FIGURE_1_IMAGE |
| **Figure 2.** ROC curves for Gradient Boosting, tuned Milestone 1 Random Forest, and Logistic Regression on both datasets. The Gradient Boosting advantage over Random Forest collapses once Random Forest is tuned to its Milestone 1 winners. Supports §4.3. | FIGURE_2_IMAGE |
| **Figure 3.** Reliability diagram and per-model Brier scores. Gradient Boosting and Logistic Regression sit near the diagonal; the class-weighted Random Forest's calibration curve is visibly shifted, matching the constant-prevalence baseline comparison in §4.4. | FIGURE_3_IMAGE |
| **Figure 4.** Dendrograms for ward, complete, average, and single linkages on Lending Club. Single and average linkage score highest on silhouette but are operationally useless, producing one giant cluster plus singletons. Supports §6 and §3. | FIGURE_4_IMAGE |

**Appendix B — Source notebooks (submitted alongside this document):** Week 6 `kumar_gaurav_week6_dx799O1_v2.ipynb`; Week 8 `kumar_gaurav_week8_dx799O1_v2.ipynb`; Week 9 `kumar_gaurav_week9_dx799O1_v3.ipynb`; Week 10 `kumar_gaurav_week10_dx799O1.ipynb`; Week 11 `kumar_gaurav_week11_dx799O1.ipynb`.

**Appendix C — YellowDig discussion evidence:** [Post 1](https://yellowdig.app/n/bu-omds/community/6a74e33e-32f1-4802-b26a-ff70bfa21bc0?postId=6adcf930-154b-4eaf-82c4-2ca0c33c8df9) · [Post 2](https://yellowdig.app/n/bu-omds/community/6a74e33e-32f1-4802-b26a-ff70bfa21bc0?postId=6b02574a-d55b-4249-b512-8c8ac0c4b06f) · [Post 3](https://yellowdig.app/n/bu-omds/community/6a74e33e-32f1-4802-b26a-ff70bfa21bc0?postId=6b00b3d3-bc14-458e-879c-cb823ef87e3e) · [Post 4](https://yellowdig.app/n/bu-omds/community/6a74e33e-32f1-4802-b26a-ff70bfa21bc0?postId=6af7b185-2cab-4f79-a5ee-75e798f38025) · [Post 5](https://yellowdig.app/n/bu-omds/community/6a74e33e-32f1-4802-b26a-ff70bfa21bc0?postId=6add7cad-1215-429a-b3c0-c9f733dca789)
