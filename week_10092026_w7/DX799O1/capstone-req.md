DX799 O1 Data Science Capstone (Fall 26)
New announcement from Sarah Rashed
Milestone One: Guidelines & Expectations
Hi everyone,

This post breaks down what Milestone One requires, how the rubric is weighted, and what separates an "Exemplary" submission from one that is merely "Proficient" or "Needs Improvement." Read this in full before you start writing. The assignment rewards both breadth and depth, and the most common way points are lost is treating it as a checklist rather than an analysis. Pay attention to the points dedicated to each section, that will tell you how long or detailed that section should be.


Datasets and Project Setup
The minimum requirement is two datasets. Ideally these are the datasets you found useful in AI for Leaders Part Two and carried into your capstone proposal. If you have since switched ideas or datasets, that is fine and does not require permission, but you must complete the necessary EDA on whatever you are using now. Do not submit modeling on data you have not explored first.


Part 1: Problem Statement / Description (5 points)
A clear description of your chosen project. Much of this can carry over from last semester's capstone proposal. Cover the industry, the impact of the project, and what it could be used for. Keep this to no more than half a page. State the project clearly enough that a grader who has never seen your proposal understands what problem you are solving and why it matters.

Part 2: Modeling Techniques — Breadth and Depth (60 points combined)
This is the core of the assignment and where most of your grade lives. There are six techniques, each tied to a week of the course:

Polynomial and interaction terms (Week 1)
Lasso, ridge, elastic net regression (Week 2)
Forward and backward selection, principal component regression (PCR), partial least squares regression
(PLSR) (Week 3)
Logistic regression and feature scaling (Week 4)
Support vector machines, the kernel trick, and regularization for support vector machines (Week 5)
Decision trees and random forests (Week 6)

You will apply all six techniques to your datasets. The rubric then splits your work into two scored dimensions:

Breadth (30 points) means you discuss all six techniques across your datasets. For each one, briefly cover the numeric results, the evaluation metrics you used and what they returned, and how the model performed. Breadth is about coverage. It should be clear you ran every technique and understood what each told you, including each model's shortcomings.

Depth (30 points) means you select one or two models (almost certainly the ones that performed best) and go much deeper. Depth is about insight, not coverage. You must explicitly state in your document which technique(s) you are treating in depth so the grader knows where to look.

To make the distinction concrete:

A breadth-level treatment of ridge regression might read: "Ridge regression was applied with five-fold cross-validation. The optimal alpha was 1.2, producing a test RMSE of 4.3 compared to 5.1 for unregularized linear regression. This suggests mild multicollinearity among the predictors that ridge successfully dampened."

A depth-level treatment of that same model would extend further: "I tuned alpha across a logarithmic grid from 0.001 to 100 using five-fold cross-validation, plotting validation RMSE against alpha to identify where the bias-variance tradeoff minimized error. The curve flattened sharply after alpha = 1, indicating that beyond this point additional shrinkage traded too much bias for marginal variance reduction. The fact that the optimal alpha was small but nonzero tells me the predictors carry mostly independent signal with limited redundancy, which aligns with the moderate correlations I observed during EDA. Compared to lasso on the same data, ridge retained all features rather than zeroing any out, which matters for this project because [domain reason]." The depth version connects the mechanics to the data and to the problem; the breadth version reports the result.

These two categories are 60 of 100 points. This is where your effort should concentrate.


Part 3: Overfitting (10 points)
Dedicate a paragraph to overfitting. For each model, explain the techniques you used to prevent it (cross-validation, regularization, train/test splits, pruning for trees, and so on), why each technique was expected to help, and what the results showed. The "why" matters as much as the "what." Stating that you used cross-validation earns less than explaining that you used it because your dataset was small enough that a single holdout split would have given an unstable error estimate.


Part 4: Metrics and Hyperparameter Tuning (5 points)
A separate paragraph focused on the metrics you chose and the tuning you performed. Describe which metrics you used and why they suit your problem. For instance, why you reported F1 rather than accuracy on an imbalanced classification target. For hyperparameter tuning, describe the method (grid search, randomized search), the parameters you searched, and what the chosen values mean in the context of your problem.

Hyperparameter tuning is not required for every model. Concentrate it on the one or two models you treat in depth. An example of how to split this: you might tune the regularization strength C and kernel choice for your SVM, and the maximum depth and number of estimators for your random forest, while leaving simpler baseline models at their defaults and noting that you did so deliberately.


Part 5: Exploratory Data Analysis (5 points)
A paragraph on how your EDA informed your modeling decisions. Keep this brief but specific. Did a skewed distribution lead you to scale features? Did a correlation heatmap push you toward regularization or dimensionality reduction? Did class imbalance shape your choice of metric? The point is to show that your modeling choices were driven by what you saw in the data, not made by default.

Part 6: Expected vs. Unexpected Results (5 points)

This is its own scored section, and it is where your own interpretation needs to come through. Discuss what aligned with your expectations and what surprised you. Graders are looking for genuine analytical voice here, not a restatement of numbers. If a weaker model outperformed a more complex one, say so and offer a reasoned explanation.


Remaining Rubric Items
AI Appendix and Citations (5 points): Include an AI appendix that clearly states whether you used AI in your submission. If you did, describe the prompt you entered and the purpose you used it for. Citations may follow APA, Chicago, or any consistent style that lets the grader locate your sources. Minor style deviations will not cost points.

Communication (5 points): Write clearly and concisely for your audience. Organize the document so a grader can follow your reasoning without hunting for it.

Formatting Requirements
8 to 10 pages, double-spaced, 12-point Times New Roman, one-inch margins.
Include 3 to 8 figures. Figures go in the body of your submission, not in an appendix, and they count toward the 8 to 10 page limit. Tables count toward your figure total. Captions do not count toward figure dimensions and should be at least 12-point Times New Roman.
Maximum of six images per page. Figures may be larger than the reference size but never smaller, legibility is the priority.
You must also turn in your Jupyter Notebooks. You can submit either a combined PDF or a link to a Google Drive folder containing your notebooks. A PDF is easier for us to grade. If you use the link option, please set it to public, view-only access. The notebook appendix has no page limit and does not count toward the 8 to 10 pages.