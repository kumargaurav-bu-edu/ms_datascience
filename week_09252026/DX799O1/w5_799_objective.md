Welcome to Week 5!
This week, you will examine the following: support vector machines (SVMs), the kernel trick, and regularization for support vector machines.


Learning Objectives
At the end of this week, you should be able to: 

Describe how a support vector machine creates a decision boundary and how the margin relates to classification performance. 
Identify the role of support vectors and explain how they determine the position of the decision boundary. 
Use different kernel functions (linear, polynomial, Gaussian) to apply the kernel trick and transform data for better classification. 
Adjust the regularization parameter 
C
 in SVMs to balance margin size and classification accuracy on the training data. 

 Google's Machine Learning Crash Course
Week 5 Resource Showcase


Tiffany Chan
Yesterday at 4:09 PM EDT
Mark as read
More Options
https://developers.google.com/machine-learning/crash-course/numerical-data/normalization9

This is from Google's Machine Learning Crash Course and gives a pretty clear explanation of why feature scaling matters. It explains how features with very different ranges can cause a model to give disproportionate attention to certain variables and discusses z-score normalization, min-max scaling, and other approaches too!

Add reaction
Flag Post
Bookmark Post

Something strange came up when I tried SVMs this week, and it took me a while to figure out.


The lesson mentions that a basic SVM doesn't give you probabilities. It just tells you which side of the line a point falls on. scikit-learn will give you probabilities anyway if you ask for them. Behind the scenes it trains a second, small model that turns the SVM's scores into probabilities. This is called Platt scaling.


Only 6% of my insurance claims are fraud, so I turned on balanced class weights. Then I compared the two outputs on the same claims:


The SVM's yes/no prediction said 2,151 claims were fraud.

The probabilities didn't give a single claim a 50% chance or higher.


Same model, same claims, completely different answers.


It turns out both are working as designed. The class weights push the line over so more claims land on the fraud side. But the probabilities are trained on the real data, where fraud is rare, so almost nothing gets close to 50%. The scikit-learn docs actually warn that this can happen: 1.4.1.2. Scores and probabilities


So which one do you trust? For picking a cutoff, the raw score is fine, because all I need is to rank claims from most to least suspicious. But imagine telling an investigator "this claim is flagged as fraud" and then showing them a probability under 50%. They'd stop trusting the model pretty fast.


If you had to show one number to a non-technical person, would you give them the score or the probability?


scikit-learn
1.4. Support Vector Machines
Support vector machines (SVMs) are a set of super

Last week I tested feature scaling on my logistic regression, and it barely mattered. The model trained faster, but the score hardly moved. So I started Week 5 thinking scaling was mostly housekeeping.


Then I ran an SVM on the same fraud data: about 12,000 car insurance claims, 6% of them fraud. No tuning, just scikit-learn's default settings. I scored it with PR-AUC, where random guessing gets 0.06.


Without scaling: 0.075

With standardization: 0.172

With min-max scaling: 0.179


That last one beats the logistic regression I spent all of Week 4 tuning (0.161).


Why such a big gap? The RBF kernel decides how similar two claims are by measuring the distance between them. Most of my columns are yes/no, so they barely add to that distance. The deductible is in dollars. Two claims with deductibles $100 apart look further apart than two claims that differ on every yes/no column combined. So the unscaled SVM was really just comparing deductibles and ages, and ignoring everything else.


The source that explained it for me: "A Practical Guide to Support Vector Classification" by Hsu, Chang and Lin at National Taiwan University. It's a free PDF: A Practical Guide to Support Vector Classification


Why I think it's a good source: the authors wrote LIBSVM, the library scikit-learn's SVM is built on. It's short and written for beginners. It gives a simple recipe: scale your data, start with the RBF kernel, then tune C and gamma with cross-validation. It even tells you which values to try. In their own example, scaling alone takes accuracy from 67% to 96%.


My numbers are still untuned. That's this weekend's job.


Did scaling change your SVM results, or just how fast it ran?

The support vector machine algorithm wasn't very intuitive for me when I started my Data Science journey. Mostly because it uses something called the kernel trick, which calculates the relationship between observations as if they were in higher dimensions to separate them correctly.


So we calculate the transformation effect while avoiding the extra computational power of performing the transformation. I'd really like to know how someone could come up with this idea :D


Below is the video that helped me the most in fully understanding this concept:

https://www.youtube.com/watch?v=efR1C6CvhmE2


https://mldemystified.com/posts/basics-of-ml/support-vector-machines/svm-kernel-machines/4


This article highlights a feature of support vector machines, which is it enables us to use kernels. Support vector machines employ the kernel trick to project data into higher-dimensional spaces, enabling the separation of classes that are not linearly separable in the original feature space. This feature allows support vector machines to construct complex, non-linear decision boundaries without explicitly computing the high-dimensional transformations.


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

    

 