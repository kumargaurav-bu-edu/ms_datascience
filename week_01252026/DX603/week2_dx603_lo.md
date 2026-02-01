Key Terms
Linear Regression: A model that fits a straight line through data to predict a dependent variable based on one or more independent variables
Multiple Regression: An extension of linear regression that fits a hyperplane (the generalization of a line) to model the relationship between a dependent variable and multiple independent variables
Polynomial Regression: A regression technique that fits a non-linear relationship by modeling the data with a polynomial equation
Gradient Descent: An algorithm that iteratively adjusts model parameters to minimize prediction error
Mean Square Error (MSE): A metric that measures the average squared difference between actual and predicted values
Root Mean Square Error: The square root of the MSE, which uses the original units of ﻿Y﻿ 
Mean Absolute Error: The average of the absolute value of the errors, which also preserves the original units
Coefficient of Determination or ﻿R squared﻿: A measure of how much of the variance of ﻿Y﻿ is captured by the regression model 
Assumptions of Linear Regression: Includes linearity, independence of errors, normality with mean ﻿0﻿, and homoscedasticity (constant variance of errors across all levels of the independent variables)
Hyperparameter: A parameter whose value is set before the learning process begins and controls the behavior of the model during training. Unlike model parameters (such as weights in a regression model), hyperparameters are not learned from the data. Instead, they need to be manually specified or tuned during training. 

Learning Objectives
By the end of this week, you will be able to:

Describe the types of problems to which regression applies
Compare the assumptions and limitations of linear regression
Apply the basic algorithm and determine solutions using formulae
Explain the MSE, RMSE, MAE, and ﻿R squared﻿ metrics and how they characterize optimal solutions
Compare the methods for solving a problem using an explicit formula and using gradient descent
Explain how multiple regression can be used for higher-dimensional data
Explain how the linear model can be adapted for polynomial models and the issues with this approach


- Think About It
Can you think of any possible datasets where the linearity assumption would be completely inappropriate?
Can you think of situations in a housing price dataset where the independence assumption might be violated?
Can you think of any situations in a housing price dataset where homoscedasticity would be violated?
Why do you think we said, “but the techniques still usually work quite well”?

- Think About It
MSE is not precisely the same as L2 loss. What is the difference? If our goal is to minimize the errors, does it matter which one we use?
Would the average of the (unsquared) values make sense here? 

- Think About It
What would happen if the learning rate in gradient descent is set too high or too low?
In linear regression, the search space for parameters is a smooth paraboloid with a single point of minimum error. In more complex models, such as deep learning, the search space resembles rugged terrain with multiple peaks and valleys. 
What challenges does this introduce for finding the optimal solution?

- Think About It
Would the matrix and linear algebra formula work for the 2D case we started this lesson with? What would the matrices look like?
What are the risks associated with adding higher-order terms in polynomial regression?
How does increasing the number of predictors affect the interpretability of the model?
How efficient is the linear algebra formula for generating the model? (Hint: find out how expensive it is, in terms of ﻿n﻿, to calculate the matrix inverse and multiplication.)

- Think About It
Why do you think some models require more decisions about complexity (e.g., polynomial degree or learning rate) compared to simpler models like linear regression?
Why might adjusting hyperparameters (like the learning rate) during training lead to better generalization? What challenges do you think could arise in selecting the “optimal” hyperparameters?

- Review the Week's Learning Objectives
Describe the types of problems to which regression applies
Compare the assumptions and limitations of linear regression
Apply the basic algorithm and determine solutions using formulae
Explain the MSE, RMSE, and ﻿R squared﻿ metrics and how they characterize optimal solutions
Compare the methods for solving a problem using an explicit formula and using gradient descent
Explain how multiple regression can be used for higher-dimensional data
Explain how the linear model can be adapted for polynomial models and the issues with this approach
