Learning Objectives
By the end of this week, you will be able to:

Define the various types of classification 
Differentiate between classification and regression
Explain the Logistic Regression classification method 
Describe why gradient descent must be used for logistic regression
Explain how tree methods change from regression to the classification setting
Interpret evaluation metrics such as accuracy, precision, recall, and the F1 score
Explain why “improvement over the baseline” is necessary in evaluation metrics 
Describe what underfitting, overfitting, and regularization mean in the classification setting

Key Terms
Classification: A supervised learning technique that predicts discrete class labels (Y) from input features (X)
Types of classification problems:
Binary: Classification with two possible outcomes (e.g., spam vs. not spam)
Multi-Class: Classification with more than two possible outcomes, where each data point is assigned one class (e.g., classifying handwritten digits 0-9)
Multi-Label: Classification where each data point can belong to multiple classes simultaneously (e.g., tagging photos with "dog" and "beach")
Categorical Data: Data representing discrete categories with no inherent order (e.g., blood types A, B, AB, O)
Ordinal Data: Categorical data with a meaningful order (e.g., grades A, B, C)
Confusion Matrix: A table summarizing the performance of a classification model by showing true positives, false negatives, false positives, and true negatives
Metrics used in classification:
Accuracy: The percentage of correct predictions out of total predictions
Precision: The proportion of positive predictions that are actually correct
Recall (Sensitivity): The proportion of actual positives that are correctly identified
F1-Score: The harmonic mean of precision and recall, balancing their trade-off

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments.

Reading | (2024, August 8). Classification in Machine Learning: An Introduction. Datacamp.com. https://www.datacamp.com/blog/classification-machine-learning 

This excellent blog post covers all the most important issues with practical examples and code. It's long, but time well spent! Skim first, then return to it after finishing this week’s lessons. 

Reading | (2019, May 22). Difference Between Classification and Regression in Machine Learning. MachineLearningMastery.com. https://machinelearningmastery.com/classification-versus-regression-in-machine-learning/ 

Another solid blog post by Jason Brownlee that presents the two methods side by side and discusses how to convert one to the other. 

Think About It
Suppose you’re developing a model to assist in medical diagnosis. Would you use binary classification (e.g., "disease" vs. "no disease"), multi-class classification (identifying a specific disease out of many), or multi-label classification (identifying multiple possible conditions for a patient)? What factors would influence your choice?
Each type of classification requires different metrics for evaluation. Why might accuracy (the percentage of the predictions that are correct) alone be insufficient in multi-label classification, where each instance can have multiple labels?



