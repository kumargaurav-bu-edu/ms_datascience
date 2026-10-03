Since the other posts so far have focused on the kernel trick, I thoug I'd try to wrap my head around regularization in SVM and connect it to what we've done in earlier weeks!

The regularization parameter in this case is C, where:

Large C gets every point correctly divided even if the margin becomes thin. This is great for obsessive persons (very clear distinction) yet the points near the hyperplane can't be trusted as much as the ones further away from the margin. This doesn't only risk overfitting, but in a dataset where one misclassifcation can be extremely detrimental! Imagine a voltage spike in lab equipment or a tainted blood sample causing a misdiagnosis in a patient that's actually healthy, or vice versa.

Small C keeps the margin wide, and if there are a few shady data points, it's okay to ignore them. I don't want to be the data gestapo, I like this option more. Sure, it could underfit but would generalize unseen data more accurately.

I'm thinking of it this way, if the data is mostly separate and a few points are close to the divisor- ignore them. They are skewed or misrepresenting the outcome in some way.

On the other hand, if there are thousands of points crowded around a hyperplane with thin margins, what can you trust? You might as well throw it all out.

There are pros and cons to everything in life, including SVM and regularization. Let's go back to L1 and L2 loss, I see a connection.

If you want to select features, only use a small percentage of available features, or have more features than samples, L1 is the choice. Just like large C. The problem is that if the features you're using are correlated, the data becomes useless.

If you want to keep all features since everything contributes to the outcome, or the data is highly correlated, and you want discernable differences in a big pool of information, L2 is your friend. Small C.

I could have it wrong, you tell me what you think!

This video has a one question quiz, that's how I started walking down this path!

https://www.youtube.com/watch?v=joTa_FeMZ2s1

This article introduces Support Vector Machines (SVMs) as one of the most powerful and mathematically elegant, supervised learning algorithms for classification. It emphasizes that SVMs are fundamentally about finding the optimal separating hyperplane — the boundary that maximizes the margin between classes. The author explains that this margin‑maximization principle makes SVMs highly robust, especially in high‑dimensional spaces.

Key Concepts Covered:

Hyperplane & Margin

SVMs choose the hyperplane that maximizes the distance to the nearest data points (support vectors). This margin‑based approach reduces overfitting and improves generalization.

Support Vectors

Only a small subset of training points — those closest to the boundary — influence the model. This makes SVMs computationally efficient and resistant to noise.

Linear vs. Nonlinear Boundaries

The article highlights that many real‑world datasets are not linearly separable. A simple linear hyperplane won’t work — which motivates the need for the kernel trick.

The Kernel Trick (Preview)

Part I introduces the intuition behind kernels: instead of explicitly transforming data into higher dimensions, SVMs use kernel functions to compute similarity in those higher dimensions without ever performing the transformation directly. This allows SVMs to learn nonlinear decision boundaries while keeping computation manageable.

Why SVMs Matter:

The author positions SVMs as ideal for:

high‑dimensional data

small‑to‑medium datasets

problems requiring strong generalization

applications like text classification, image recognition, and bioinformatics

The article’s main takeaway is that SVMs are powerful because they combine geometric intuition (maximizing margins) with computational efficiency (support vectors + kernel trick). Part I sets the stage for deeper exploration of kernels by showing why linear boundaries are insufficient and how SVMs overcome that limitation elegantly.


https://medium.com/@dswithgk/support-vector-machines-svm-the-kernel-trick-a-comprehensive-guide-part-i-6a6b16d346ca1

My Week 5 SVM caught 98 of 121 loss-making order lines, compared with 82 for logistic regression—but it also raised 28 false alarms instead of 3. In retail terms, that could mean preventing more bad recommendations while also hiding products that would have been profitable.

This scikit-learn guide makes a useful distinction: predicting risk and deciding when to act on it are separate problems. A recent open-access study on cost-sensitive classification goes further, arguing that the costs of different mistakes are often uncertain when a model is built.

Maybe choosing a model should start with a business decision table, not a leaderboard. What would a false positive and false negative actually cost in your capstone?


scikit-learn
3.3. Tuning the decision threshold for class prediction
Classification is best divided into two parts: the statistical problem of learning a model to predict, ideally, class probabilities;, the decision problem to take concrete action based on those pro…

Digital object identifier - Apr 02, 2025

Cost-sensitive classification with cost uncertainty: do we need surrogate losses? - Machine Learning
In many binary classification applications, the costs of false positives and negatives are imbalanced. Furthermore, there is often uncertainty about the exact costs of these errors. A natural measure-of-interest to be minimised in such scenarios is the expected misclassification cost. We identify many situations where this measure has analytic gradients, and thus it can be used as a training loss and optimised directly using empirical risk minimisation. In particular, we derive such losses from the Beta, Gamma and Gaussian distributions to model different kinds of cost uncertainty. The Beta family includes commonly used losses such as cross-entropy, squared error and 0–1 loss as special cases. The question then arises as to when it is appropriate to directly optimize the measure-of-interest, versus using a standard surrogate like cross-entropy or focal loss during training. After revisiting the theory of surrogate losses, proper losses and cost-sensitive learning to obtain good candidate surrogates out of derived families, we conduct an empirical comparison of derived training losses that, to our knowledge, were never tried on deep neural networks before, with the aim to minimise cost-sensitive measures-of-interest. The findings show that using Beta losses in training leads to improved performance compared to traditional training objectives like cross-entropy, label smoothing, and focal loss. This improvement is seen not only in terms of misclassification cost metrics, but (perhaps surprisingly) also in conventional metrics such as accuracy, mean squared error, and the area under the ROC curve.

Hi everyone! This week I found a short 3 minute video that quickly goes over the kernel trick a little more. I found the video helped me understand the readings more, especially when it came to the polynomial kernel. It doesn't go into much depth on it, but it does give a good basis on what the polynomial kernel does to the data and how it can be split with the support vector machine. I hope this helps others!

https://www.youtube.com/watch?v=Q7vT0--5VII2

Hi James,

I found your result interesting because weighting the less common cases seemed reasonable, yet it did not improve ranking much. One might alternatively evaluate balanced accuracy, which computes the mean recall for both categories (scikit-learn developers, n.d.). Would analyzing the percentages of false positives and false negatives among different applicant categories assist you in evaluating fairness for your ethical project?

Reference

scikit-learn developers. (n.d.). balanced_accuracy_score. scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html

I found this short video explaining SVM in a very comprehensive yet easy to understand way (maybe it was the visualizations?). It talks about what it is, key words that were covered in our class content, and even different use cases like facial recognition and text detection. I didn't know that that's what SVM was used for!

Highly recommend if you don't have a lot of time, but need a refreshed: https://www.youtube.com/watch?v=_YPScrckx285

Hernán, M. A., & Robins, J. M. (2020). Causal inference: What if. Chapman & Hall/CRC. https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf

Shmueli, G. (2010). To explain or to predict? Statistical Science, 25(3), 289–310. https://doi.org/10.1214/10-STS330

    