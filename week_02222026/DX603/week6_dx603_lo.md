Learning Objectives
By the end of this week, you will be able to:

Describe the structure of decision trees (nodes, branches, depth, size, leaves)
Explain how decision trees split data
Explain how decision trees limit their size by limiting depth, leaf size, or pruning
Analyze the impact of tree complexity on model performance, such as overfitting and underfitting
Apply the appropriate functions in scikit-learn

Think About It
Why might a decision tree be easier to interpret compared to other machine learning models like neural networks or polynomial regression? How does this impact its use in real-world applications?
Imagine you are using a decision tree to predict house prices. What might be some advantages of splitting the data at certain features (e.g., 'number of rooms' or 'distance to city center') over others (e.g., ‘driveway length’ or ‘house color’)?
How does a decision tree’s ability to split the data recursively allow it to capture complex patterns? Can you think of a scenario where this might be especially useful?
What are some potential limitations of decision trees? For example, how might they handle noisy data or outliers?
What factors would you consider when deciding how deep a decision tree should be? How might the depth of the tree affect its performance?

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments. 

Reading | Géron, A. (2022). Hands-on machine learning with Scikit-Learn, Keras and TensorFlow : concepts, tools, and techniques to build intelligent systems (Third edition.). O’Reilly.

Read Chapter 6, Decision Trees. This chapter mostly discusses classification trees but specifically mentions regression trees on pages 204-208. Read through the classification material but understand that we will cover these in detail in Week 8. 

Video | Normalized Nerd. (2021, Feb. 4). Decision Tree Regression Clearly Explained!. [Video]. Youtube. https://www.youtube.com/watch?v=UhY5vPfQIrA (9:17) 

This video clearly and enthusiastically explains the topic and provides beautiful graphics relating a scatterplot of the data to a decision tree.

Think About It
How does the choice of impurity metric (e.g., MSE for regression, Gini impurity for classification) affect where the decision tree splits the data? 
Why might setting a maximum tree depth help prevent overfitting? What trade-offs should you consider when choosing this parameter?
If a decision tree consistently makes poor predictions on new, unseen data, what changes might you consider in its construction process to improve generalization?
How do decision trees handle complex interactions between features differently from models like linear regression or polynomial regression? Why might this be an advantage in certain datasets?

Think About It
Higher-dimensional decision trees create partitions in multi-dimensional space, not just along a single axis. What challenges might arise when visualizing and interpreting these splits, and how can this affect your understanding of the model's predictions?

Think About It
Why might a large, unpruned decision tree lead to overfitting, and how does pruning help address this issue? Can you think of a scenario where overfitting could be especially problematic?
The parameter ﻿alpha﻿ controls the balance between complexity and simplicity in a decision tree. How does adjusting ﻿alpha﻿ affect the model’s ability to capture patterns in the data? What trade-offs should you consider when choosing ﻿alpha﻿?
How does the process of pruning a decision tree compare to regularization techniques (like Lasso regression) that add a penalty for complexity? What similarities and differences can you identify?
Why is it beneficial to start by growing a large tree before pruning it back, rather than trying to create a smaller tree from the beginning? What advantages does this approach offer?

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may need to apply them in the graded assignments. 

Reading | GeeksforGeeks. (2024, April 10). Pruning decision trees. https://www.geeksforgeeks.org/pruning-decision-trees/  

This offers a straightforward presentation of the main ideas with code. 

