For my capstone project, I am integrating public health datasets that encapsulate information at the county scale. Prior to examining the correlation between social vulnerability and healthcare accessibility, I must verify that the records align accurately and that the metrics are comparable. Variations in county identities, absent data, or the temporal scope of each dataset may influence the counties represented and the interpretation of the findings.
CDC investigators advocate for the assessment of health data based on attributes like completeness, validity, accuracy, consistency, and representativeness prior to its utilization in addressing research inquiries (El Burai Felix et al., 2024). This renders data preparation a crucial component of the analysis, rather than only a technical procedure before modeling. What verifications do you employ when amalgamating datasets from various origins?

How would you record unpaired entries or absent information to enable readers to assess their impact on the outcomes?

Reference

El Burai Felix, S., Yusuf, H., Ritchey, M., Romano, S., Namulanda, G., Wilkins, N., & Boehmer, T. K. (2024). A standard framework for evaluating large health care data and related resources. MMWR Supplements, 73(3), 1–13. https://www.cdc.gov/mmwr/volumes/73/su/su7303a1.htm1


Why Randomness makes the forest smarter
Jegan Arthanari
Last Thursday at 4:19 AM EDT
Mark as read
More Options
Reading any modeling techniques in the context or real world application is always interesting, especially when you are able to connect the logic to the purpose. I stumbled upon this article, it is simple but effective in explaining why RF suits better in Healthcare

https://ioaglobal.org/blog/random-forests-explained-simply-prediction-real-world-use/

k-NN
Week 8 Resource Showcase


Yan Xu
Yesterday at 10:00 PM EDT
Mark as read
More Options
This 8-year old video gives you some explanation of the basic train-test split and CV. The interesting thing is that it also gives you the intuition when p gets very large for Minkowski distance.


https://www.youtube.com/watch?v=oymtGlGdT-k1
Machine learning-based detection of complex cyberattacks
Week 5 Resource Showcase


Sangeetha Kasi
10/10/2026 PM EDT
Mark as read
More Options

Hölbl and Rotovnik reviewed 68 studies on using machine learning to detect complex cyberattacks such as advanced persistent threats (APTs), reconnaissance and steganography, which evade traditional rule based detection. They found that ensemble models usually outperform single models, by about 5.2% on average, and that XGBoost, Random Forest and LightGBM are the most effective. Supervised learning dominates, while unsupervised and semi supervised methods are underused. Common datasets such as UNSW-NB15 and NSL-KDD are outdated, so newer ones like DAPT2020 and SCVIC-APT-2021 are preferred. The authors call for better real world datasets, fixes for class imbalance, more unsupervised approaches and stronger defenses against adversarial attacks.

Techniques:

Ensemble and supervised: XGBoost, Random Forest, LightGBM, MLP, Decision Tree, SVM, Naive Bayes, KNN, AdaBoost, Logistic Regression, LSTM, ANN, CNN
Unsupervised: Isolation Forest, One Class SVM, Local Outlier Factor, Autoencoders, incremental learning
Semi supervised: Deep Triplet Auto-Encoder
Custom ensembles: voting ensembles and the three stage MLAPT model
https://link.springer.com/article/10.1007/s10586-026-06367-4

Random Forest
Week 6 Resource Showcase


Gavaskar Thavarajah
Last Tuesday at 9:32 PM EDT
Mark as read
More Options
I found an interesting article about Random Forest


https://towardsdatascience.com/random-forest-explained-a-visual-guide-with-code-examples-9f736a6e1b3c/2

After reading the article, I understand random forests as a way to combine many decision trees to make a more reliable prediction. Each tree is trained on a slightly different sample of the data and considers a random subset of features when making decisions. For classification, the forest uses the trees’ votes; for regression, it averages their predictions.

The main advantage is that combining trees can reduce the instability of relying on a single decision tree, which may fit the training data too closely. Random forests can also handle many features and provide estimates of feature importance. However, they can be harder to interpret than one tree and may require more computing resources.

One point I found interesting is how the randomness in the training process helps the trees make different errors, so combining them can improve the overall result. I’m curious how we should choose between a random forest and a simpler model when interpretability matters as much as predictive accuracy. What kinds of problems do you think are a good fit for random forests?



    