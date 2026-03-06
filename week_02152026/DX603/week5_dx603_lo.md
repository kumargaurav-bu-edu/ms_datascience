Learning Objectives
By the end of this week, you should be able to:

Explain the motivation for forward and backward selection methods and how each works
Define regularization and its role in regression in preventing overfitting
Differentiate between L1 (Lasso) and L2 (Ridge) regularization
Apply each of the methods in scikit-learn
Determine when to use each method in practice and how to tune the regularization parameters

Think About It
Think about why reducing the number of features can be beneficial. How might using too many features affect model performance, especially in terms of overfitting and interpretability?
Forward selection adds features one by one, while backward selection starts with all features and removes them. In what situations might one method be preferable to the other?
Does reducing the number of features make a model simpler? How might this impact interpretability and model performance?

Think About It
Ridge regression shrinks all coefficients toward zero but keeps them in the model, while lasso regression can set some coefficients exactly to zero. How might this difference affect the interpretability of a model?
How does regularization impact the bias-variance trade-off? Why might adding a regularization term increase bias but reduce variance?
Are there cases where adding a regularization term might actually worsen model performance? What kind of data characteristics might make regularization less effective?

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments. 

Reading | Géron, A. (2022). Hands-on machine learning with Scikit-Learn, Keras and TensorFlow : concepts, tools, and techniques to build intelligent systems (Third edition.). O’Reilly.

Read Chapter 4, Training Models, pp. 155-161. This is a practical explanation of regularization methods for regression, including elastic nets and early stopping, techniques worth knowing about but which we do not cover in this lesson. 

Video | Computational Thinking. (2022, Nov. 16). Regularization. [Video]. Youtube. https://www.youtube.com/watch?v=8t5vaZroVjw (5:57)

This video offers a short and pithy presentation of the most important ideas with attractive graphics.

python3 generic_quiz.py week_02152026/DX603/quiz_questions.json