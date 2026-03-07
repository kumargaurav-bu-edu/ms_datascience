Learning Objectives
By the end of this week, you will be able to:

Explain how ensemble methods improve accuracy and reduce overfitting compared to individual models
Differentiate between Bagging, Boosting, and Random Forests 
Illustrate how decision boundaries evolve in ensemble methods as models are added
Explain why ensemble methods are less interpretable than simpler models 
Evaluate the efficiency of the various methods

Think About It
Why might Bagging be particularly effective for high-variance models like decision trees? What does it mean to "average out the noise"? Does this depend on your assumption about the probability distribution of the noise?
Bagging reduces variance but does not change bias. What are some scenarios where this might be a limitation, and how could you address it?
How does the Central Limit Theorem explain the effectiveness of Bagging in reducing the impact of random errors?
If you observe that your Bagging model's performance improves as you increase the number of trees ﻿B﻿, what might be happening? Are there practical limits to how far you should increase ﻿B﻿?
Suppose each decision tree in your Bagging model consistently underestimates the value of expensive houses. Will adding more trees improve this bias? Why or why not?

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments.

Video| codebasics. (2021, Oct. 22). Machine Learning Tutorial Python - 21: Ensemble Learning - Bagging. [Video]. Youtube. https://www.youtube.com/watch?v=RtrBtAKwcxQ (23:37)


Think About It
Why does adding randomness to the feature selection process help Random Forests reduce overfitting compared to standard Bagging?
How might Random Forests handle a dataset where certain features are highly correlated? Would this affect the feature sampling process?
Can you think of a scenario where Random Forests might not perform well? What characteristics of the data could lead to this, and how might you address it?
How do Random Forests compare to a single decision tree in terms of interpretability? Why might this be a drawback in some applications?
Why do important features still tend to "shine through" in Random Forests, even though individual trees may use different subsets of features?

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments. 

Video | StatQuest with Josh Starmer. (2018, Feb. 5). StatQuest: Random Forests 1: Building, Using, and Evaluating. [Video]. Youtube. https://www.youtube.com/watch?v=J4Wdy0Wc_xQ (9:54)

Josh Starmer can’t sing, but he presents statistics in a friendly and clear way; this is one of his best videos on the basics of random forests. 
Think About It
How might reducing ﻿lambda﻿ affect the learning process in Boosting? Would it make the model more accurate or more prone to overfitting?
Why might Boosting be more effective than using a single decision tree, even if the tree is very complex?
What are some situations where you think Boosting would outperform Random Forests? Conversely, when might Random Forests be preferable?