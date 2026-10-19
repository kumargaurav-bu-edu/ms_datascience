

Hello everyone,

While continuing to work through notebooks, I am looking for good examples of how you may set up models and evaluation.

I found this article had a nice example of how to setup Random forest and grid search with parameter tuning, to help optimize hyperparameters. It gives several examples and how you may set up your model for GridSearch, RandomSearch, Optuna, etc. along with the hyperparameters used for each, along with a few others like XGBoost, etc.

https://drivedatascience.com/hyperparameter-tuning-gridsearch-randomsearch-optuna-cross-validation/1

I like this one since it gives example code for each case, and then some examples of how you might incorporate in a workflow that aren't too complicated, and common errors to avoid. The only thing it's missing it how to visualize the plots, so including another link that has focuses on GridSearch but some plot examples too:

https://blog.trainindata.com/random-forest-with-grid-search/1

Let me know if it's helpful. I've seen some great resources posted by everyone so hopefully this adds to the knowledge base.
As I move from weekly notebooks into Milestone One, Week 6 creates an interesting tradeoff: a decision tree can give a retailer a rule they can follow, while a random forest may predict better but hides its reasoning across hundreds of trees.

A 2025 open-access study in Machine Learning asks whether we can have both. The researchers used SHAP and co-clustering to represent random forests with small groups of shallow decision trees, producing explanations that remained reasonably faithful but were easier to understand.

For my capstone, that matters: if a model flags a recommendation as likely to lose money, “the forest says so” is not much of a business case. How much predictive performance would you trade for an explanation someone can actually use—or should we expect both?

This article explains why decision trees and random forests remain two of the most practical and widely used machine‑learning models. It begins by describing decision trees as intuitive, question‑driven structures that guide users through a sequence of feature‑based decisions until reaching an outcome. In machine learning, algorithms such as ID3, C4.5, CART, CHAID, and MARS automatically generate these trees by selecting the most informative questions and arranging them hierarchically. Their biggest advantages are interpretability, built‑in feature selection, minimal data preprocessing, and fast prediction times — making them ideal for large datasets and resource‑constrained environments.

The article then expands to random forests, which are ensembles of many decision trees trained on different bootstrap samples and random subsets of features. By aggregating the predictions of multiple trees (typically through majority voting), random forests achieve higher accuracy, stronger generalization, and reduced overfitting compared to single decision trees. This makes them a go‑to model for both classification and regression tasks when transparency is less important than performance.

Finally, the article recommends learning key concepts like pruning and bootstrapping to fully understand how these models work, and encourages readers to practice building them in Python to strengthen their machine‑learning workflow.


https://365datascience.com/tutorials/machine-learning-tutorials/decision-trees-and-random-forests-in-machine-learning/2
https://medium.com/sfu-cspmp/surviving-in-a-random-forest-with-imbalanced-datasets-b98b963d52eb





    