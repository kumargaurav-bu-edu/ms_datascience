Welcome to Week 9!
This week, you will explore gradient boost, including learning rate, number of estimators, tree depth, and regularization.


Learning Objectives
At the end of this week, you should be able to: 

Explain how gradient boost works. 
Construct a gradient-boosting regression model by iteratively fitting weak learners to residuals. 
Compare the impact of different learning rates on model performance and complexity. 
Evaluate how tree depth and number of estimators impact the risks of underfitting or overfitting. 
Apply regularization techniques in gradient boosting, including limiting tree complexity, setting sample thresholds, and subsampling. 

Learning Rate, # of Estimators
If the learning rate is set to a small value, the gradient boost gradually moves toward a solution, taking a while to get there. The training takes longer — and the resulting model is more complex — but it may be more accurate because it contains a greater amount of complexity. 

Small learning rates result in a large number of trees (i.e., a large number of weak learners), while high learning rates result in faster training and a smaller number of weak learners. 

Tree Depth
We can also choose the tree depth of each weak learner. Very deep trees might tend to overfit, while shallow trees are more likely to underfit, as they have a harder time picking up on complex relationships between features. A tree is “deep” if it has many layers, allowing it to fit data in a complex way. For instance, if there are 1,000 samples, then, in principle, they could be fit perfectly by a tree with ﻿10﻿layers (up to ﻿2 to the power of 10 equals 1 comma 024﻿ leaves.) The problem is that if we fit the training data perfectly, we are likely overfitting — meaning that we fit this particular dataset exactly but cannot fit other data from the same population. On the other hand, underfitting means we do not even fit the training data. 

Regularization
Gradient boost can be regularized by (1) penalizing complexity (the number of leaves), (2) setting a minimum number of samples per leaf, or (3) using a subsample when training a given weak learner (e.g., if there are 1,000 samples, use a smaller number than 1,000 to train each weak learner). 

Think About It
How is gradient boost similar to random forest? 
How is gradient boost different from random forest? 
Does a small learning rate generally lead to higher or lower accuracy? Why? 

