My initial assessment is that the main opportunity is not adding more experiments; it is tightening the validity of a few experiments and making sure the conclusions do not claim more than the evidence supports. That is particularly important given your Milestone 1 feedback about making conclusions concrete and tying them directly to the central research problem.
1. What the two notebooks currently establish
Topic	Lending Club	Taiwan
Week 8: KNN ROC-AUC	0.7090	0.7610
Week 8: best KNN setting	k=802, Manhattan, distance-weighted	k=202, Euclidean, uniform
Week 9: Gradient Boost ROC-AUC	0.7136	0.7737
Week 9: Gradient Boost PR-AUC	0.3829	0.5568
Strongest conclusion	KNN adds little ranking performance over the existing models	Gradient Boost and Random Forest capture useful nonlinear repayment patterns

The results support a useful cross-market observation: model flexibility and local-neighbourhood methods do not deliver the same benefit in both datasets. Lending Club's grade and int_rate already encode substantial risk information, while Taiwan's repayment-history variables, particularly PAY_1, appear to provide stronger nonlinear predictive structure.

That is a promising foundation for the capstone. I would, however, address the issues below before treating these results as final evidence.
2. Week 8 — KNN review
Strong experimental coverage
Several items need correction

What is working well
1. Feature scaling is convincingly demonstrated. Without scaling, loan_amnt accounts for essentially 100% of Lending Club's raw numeric variance. Scaling improves validation ROC-AUC from 0.6161 to approximately 0.690. Taiwan also improves, from 0.7485 to 0.7754 with RobustScaler. This is an excellent example of EDA directly influencing model design.

2. The bias–variance discussion has evidence behind it. At k=1, training AUC is 1.000 on Lending Club and 0.9994 on Taiwan, while validation AUC is much lower. Increasing k improves validation performance before it eventually plateaus or declines.

3. You compare different distance metrics rather than assuming Euclidean is best. Manhattan performs slightly better in the validation sweep, but the differences are small. That is a useful finding in itself: the distance metric matters, but it is not the dominant source of performance improvement.

4. You compare KNN with the previous models on the same test split. This gives the capstone a consistent model-comparison story across Weeks 6, 8 and 9.

5. The threshold experiment is particularly useful. For Lending Club, the KNN F1 score rises from 0.005 at threshold 0.5 to 0.431 at the OOF-selected threshold of 0.21. This demonstrates why accuracy or default-threshold results alone are inadequate for imbalanced credit-risk classification.
Issues I would fix before relying on the results
Priority	Finding	Why it matters
High	The final k search selects the largest candidate in both datasets: 802 for Lending Club and 202 for Taiwan.	You cannot yet conclude these are optimal k values. The search boundary may be truncating the best range.
High	The final model uses StandardScaler, but the conclusion says RobustScaler is best for Taiwan.	The final tuning and the scaler conclusion are not aligned.
High	The final grid search selects Euclidean for Taiwan, but the conclusion table says Manhattan for both markets.	The reported configuration should match the actual fitted model.
High	The dollar-based expected-loss calculation is not reliable.	It appears to confuse precision with the false-positive proportion and makes unsupported revenue assumptions.
High	The target-encoding preview uses full-training labels to encode the same training rows.	This creates target leakage if the resulting encoded features are used to train the model.
Medium	The no-grade ablation, reliability diagnostic and target-encoding experiment have no saved outputs.	These should not be presented as completed findings until executed and verified.
Medium	The Taiwan manual neighbour-probability calculation differs from scikit-learn by as much as 0.0196 at k=51.	The discrepancy needs investigation before relying on the manual neighbour-sweep implementation.

A particularly important detail about k: your final GridSearchCV considers only three values around the earlier best k. It chooses 802 for Lending Club and 202 for Taiwan, both at the upper end of the candidate grid. Expand the range and check whether performance plateaus. Until then, call these the best values among the candidates tested, not the optimal values.

The scaler mismatch also needs resolving. Your earlier validation sweep found Taiwan RobustScaler at 0.7754 versus StandardScaler at 0.7717. But the final make_prep() default is StandardScaler, and the final GridSearchCV does not tune the scaler. Either tune the scaler within cross-validation or explicitly use the scaler you intend to report.
The expected-loss calculation should be removed or rebuilt
The Week 8 section translating KNN performance into dollars is the most concerning part of this notebook.

Your test precision is 0.326. That means only 32.6% of the loans flagged as defaults are actual defaults; approximately 67.4% are false positives. The narrative instead describes 32.6% as the proportion of flagged borrowers who would repay. Those are different quantities.

There are also assumptions about lifetime interest revenue, loan duration and loss given default that are not sufficient to calculate actual net credit economics.

I would not include the current estimated $1.8 million benefit in your capstone report. If you want an economic analysis, rebuild it from a confusion matrix with explicit false-positive and false-negative costs, loan-level exposure, loss given default, repayment timing and a defensible revenue model.
A further methodological issue: target encoding
The notebook defines target_encode_oof(), which is the right direction, but the later target_encode_apply() maps the training rows using category default rates calculated from the entire training target. That means each training row contributes to the encoding used for itself.

For a valid experiment:
- Generate out-of-fold encodings for training rows.
- Fit the category-to-target mapping on the full training data only when transforming the held-out test data.
- Keep encoding inside the cross-validation process when comparing hyperparameters.
The current target-encoding section has no saved output, so I would treat it as unfinished rather than as evidence.

3. Week 9 — Gradient Boosting review
Good modeling progression
Conclusion and validation corrections needed

What is working well
Week 9 has a logical progression:
- Staged train-versus-validation curves to examine overfitting.
- Learning-rate sweep.
- Tree-depth sweep.
- Regularization using min_samples_leaf, subsample and min_impurity_decrease.
- Final comparison against Random Forest and Logistic Regression.
- Feature importance, calibration, threshold selection and cost sensitivity.
This is a strong structure for demonstrating both breadth and depth.

The most useful findings are:
Finding	Lending Club	Taiwan
Gradient Boost ROC-AUC	0.7136	0.7737
Random Forest ROC-AUC	0.7085	0.7694
Logistic Regression ROC-AUC	0.7125	0.7394
Gradient Boost PR-AUC	0.3829	0.5568
Random Forest PR-AUC	0.3755	0.5500
Logistic Regression PR-AUC	0.3784	0.5029

The central result is that Gradient Boosting has a meaningful advantage over Logistic Regression on Taiwan, but the advantage over Random Forest is much smaller. Lending Club shows much less separation between the three models.
Issues I would fix
1. The Taiwan Gradient Boost versus Random Forest conclusion is too strong.

Your paired bootstrap reports:
- ROC-AUC difference: approximately +0.0044, with a 95% interval from approximately 0 to +0.0086.
- PR-AUC difference: approximately +0.0070, with a 95% interval from -0.0013 to +0.0150.
Both intervals include zero, or come extremely close to it. Therefore, the results do not establish a clear 95%-confidence advantage over Random Forest on Taiwan.

You can say Gradient Boosting has the highest observed point estimates. You should not say that it consistently or conclusively outperforms Random Forest.

The contrast with Logistic Regression is stronger: the Taiwan ROC-AUC improvement is approximately 0.0345, with a bootstrap interval of +0.0249 to +0.0433.

Also, 200 bootstrap resamples are relatively few for estimating 95% intervals. Increase this to at least 2,000, preferably 5,000, for the final analysis.

2. The Lending Club tree-depth decision needs a clearer explanation.

Your validation depth sweep identifies depth 5 as the best Lending Club depth, whereas the final model uses depth 3 for both datasets.

You subsequently audit depth 5 on the test set:
Lending Club configuration	Test ROC-AUC	Test PR-AUC
Depth 3	0.7136	0.3829
Depth 5	0.7118	0.3797

The depth-3 result is better on the held-out test set. However, the test set should not be used to choose between configurations after inspecting its performance.

I would explain that depth 3 was retained as a simpler, common configuration, while acknowledging that the validation sweep favored depth 5 for Lending Club. Ideally, resolve this through a more robust validation procedure rather than repeatedly consulting the test set.

3. The HGB speed comparison is not apples-to-apples.

This is an important technical correction.

The reported Gradient Boosting fit time of approximately 167.8 seconds is the time for the entire GridSearchCV process, not the time to fit one final Gradient Boosting model. The HGB time of 1.7 seconds is a single model fit.

Consequently, the claimed 98× speedup is not a valid comparison.

To correct it:
- Fit the final regularized Gradient Boosting model once.
- Fit the HGB model once on the same training split.
- Measure both fit times under comparable conditions.
- Report their ROC-AUC and PR-AUC.
- Explain that the two estimators have different available regularization controls.
HGB may still be substantially faster, but the current speedup figure does not establish that.

4. The calibration conclusion contradicts the experiment results.

You have already run a reliability-diagram/Brier-score experiment:
Dataset	Gradient Boost	Random Forest	Logistic Regression
Lending Club Brier	0.1463	0.1471	0.1465
Taiwan Brier	0.1355	0.1363	0.1445

Lower Brier scores are better. Gradient Boost has the lowest score in both datasets in the reported results.

But the final conclusion says that probabilities have not been checked for calibration and suggests that calibration should be done if Gradient Boost is the worst-calibrated model.

That statement is outdated and contradicts the executed experiment. Update the conclusion to acknowledge the calibration analysis. Also, remember that Brier score combines calibration and discrimination; it is not a pure calibration measure. Interpret it alongside the reliability diagrams.

5. The PR-AUC-to-number-of-defaulters calculation is not justified.

The notebook estimates additional defaulters identified by multiplying the PR-AUC difference by the sample size and class proportions.

A PR-AUC difference does not translate directly into a fixed number of additional defaults identified at the same precision. That calculation should be removed or replaced with a comparison at a specific operating threshold, using actual confusion matrices.

6. The cost ratios are scenarios, not established business costs.

The FN:FP ratios of 3, 5 and 10 are useful sensitivity experiments. But they are assumptions, not measured credit-loss economics.

Present them as hypothetical cost scenarios and explain how a lender would need to estimate the actual costs before adopting a threshold.

7. The final test set is being used for too many diagnostic and comparison exercises.

Across the two notebooks, the held-out test data are used for model comparisons, bootstrap analysis, permutation importance, feature ablation, calibration, threshold evaluation and additional model audits.

Some post-fit diagnostics are reasonable, but once the results influence model choices or conclusions, the test set is no longer a completely untouched final evaluation set.

For the final capstone, I would recommend a disciplined structure:
- Training data: model fitting.
- Cross-validation within training data: hyperparameter and threshold selection.
- Validation data, if needed: model selection and diagnostic decisions.
- Final test data: one final evaluation after the modeling decisions are locked.
Your previously identified limitation of using a random split rather than an out-of-time split is also still important. A time-based validation would better test whether the findings generalize to future loans.
4. How I would use these findings in your Milestone 2 report
I would not give equal space to every experiment. The assignment rewards both breadth and depth, so I would organize the report around two deeper stories.

Deep-dive topic 1: Gradient Boosting (Week 9)

This is the stronger candidate for your primary deep dive because you have:
- Staged learning curves and evidence of overfitting.
- Learning-rate and tree-depth experiments.
- Regularization and cross-validation.
- Comparisons with previous models.
- Feature importance and probability calibration.
- Threshold and cost-sensitivity analysis.
Your central conclusion should be that Gradient Boosting improves on Logistic Regression substantially in Taiwan, but its incremental benefit over Random Forest is modest. On Lending Club, model differences are small, suggesting that the existing pricing and grade variables already capture much of the available predictive signal.

Deep-dive topic 2: KNN (Week 8)

Use KNN to explain why distance-based methods require careful feature scaling and why their effectiveness depends on the structure of the data.

The strongest evidence is:
- Scaling produces a large improvement in both datasets.
- Large k values perform better than very small k values.
- Manhattan and Euclidean distances produce relatively similar results.
- KNN is competitive on Taiwan but does not outperform Gradient Boosting.
- Threshold selection changes the practical classification results considerably.
For breadth, briefly cover all Week 8 and Week 9 experiments, but do not let the technical details obscure the business implications.
5. My recommended correction order
I would fix these before moving to Week 10 and Week 11.
Review action tracker
0/11 completed



[ ] Week 8: Expand the k search because both final selections are at the upper boundary.
[ ] Week 8: Align the selected scaler and distance metric with the final model and conclusion.
[ ] Week 8: Investigate the Taiwan manual-neighbour calculation discrepancy.
[ ] Week 8: Remove or rebuild the dollar-based expected-loss calculation.
[ ] Week 8: Correct the target-encoding implementation to use out-of-fold training encodings.
[ ] Week 8: Execute and save the missing ablation, calibration and target-encoding results.
[ ] Week 9: Increase bootstrap repetitions and qualify the Taiwan GB-versus-RF conclusion.
[ ] Week 9: Clarify why depth 3 was retained for Lending Club despite the depth-5 validation result.
[ ] Week 9: Correct the HGB-versus-GB fit-time comparison.
[ ] Week 9: Update the calibration conclusion and remove the unsupported PR-AUC-to-default-count calculation.
[ ] Both: Use nested validation or a separate validation set for tuning, and preserve a final untouched test set.

6. Overall assessment against the Milestone 2 rubric
Rubric area	My assessment
Problem statement	Good foundation; make sure both weekly topics explicitly connect to the same research question.
Conclusions — depth	Strong experimental material, but conclusions need more careful interpretation and stronger business linkage.
Conclusions — breadth	Good coverage of the techniques and experiments.
Overfitting	Good evidence, particularly the KNN k-sweep and Gradient Boosting staged curves.
Metrics and tuning	Strong coverage, but some tuning and comparison methodology needs correction.
Expected/unexpected	Good observations; distinguish measured findings from hypotheses.
EDA	Strong connection between scaling, feature distributions and KNN behavior.
AI appendix and citations	Not established by these notebooks alone; ensure the final submission includes the required disclosure and references.
Communication	Well-organized technical notebooks, but some sections are overly detailed and some conclusions are inconsistent with the outputs.

My overall verdict: These are promising submissions, and there is enough evidence here to build a strong Milestone 2 report. I would not yet call them final-ready because of the validation issues, inconsistent conclusions and a few unsupported economic interpretations.

One important point: your Milestone 1 instructor feedback was specifically about making conclusions concrete and connecting them to the central problem. You now have more quantitative evidence than before. The next step is to make sure every major conclusion answers three questions:
1. What did the experiment demonstrate, with actual numbers?
2. Why does that result matter for predicting consumer credit default?
3. What does it tell us about the difference between the US and Taiwan markets?
My suggestion: Correct Week 8 and Week 9 first, then share Week 10. Once we have all four topics, we can build one consistent evidence-to-conclusion matrix for the final report rather than writing four disconnected weekly summaries.