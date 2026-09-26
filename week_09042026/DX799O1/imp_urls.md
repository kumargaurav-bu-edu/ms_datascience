Ridge= retain (keeps all variables)

Lasso= loss ( feature can shrink to 0 leading to loss from the model)


Broad introduction to regularization- this was shared in machine learning fundamentals.

https://www.youtube.com/watch?v=8t5vaZroVjw


These are from StatQuest with Josh Starmer, I would highly recommend his entire playlist (he has funny intro song for each topic).. These are the topics for this week's class from his playlist


Ridge regression

https://www.youtube.com/watch?v=Q81RR3yKn30

Lasso regressio

https://youtu.be/NGf0voTMlcs?si=Sv52gmhaHJfGqsUG

Elastic net regression

https://youtu.be/1dKRdX9bfIo?si=MemKuVelpgbm9WTV


Then for a quick text summary this is all 3 compared from geeksforgeeks

https://www.geeksforgeeks.org/machine-learning/lasso-vs-ridge-vs-elastic-net-ml/

3 Key Points I Learned About Regularization
Regularization helps prevent overfitting. Both Ridge and Lasso add a penalty for large coefficients, encouraging a simpler model that is more likely to generalize well to new data.


Lasso (L1) can eliminate features. Lasso penalizes the absolute value of coefficients and can push some coefficients all the way to zero. This makes Lasso useful for feature selection. Remember: Lasso = L1 = Less features.


Ridge (L2) shrinks features but usually keeps them. Ridge penalizes squared coefficients. It reduces their magnitude but typically does not make them exactly zero. It is particularly useful when predictors are highly correlated (multicollinearity) because it tends to distribute influence among them.

\

https://www.youtube.com/watch?v=Q81RR3yKn30

https://www.youtube.com/watch?v=NGf0voTMlcs
    



