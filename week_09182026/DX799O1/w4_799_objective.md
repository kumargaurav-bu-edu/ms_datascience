Week 5 Overview
This week we will cover directed acyclic graphs (DAGs). DAGs visually represent causal relationships using nodes and arrows, helping us distinguish correlation from causation. Through examples, including one involving deer, flowers, and pesticides, we see how confounders and colliders affect our interpretation of data. DAGs also introduce tools like front door paths and placebo tests, which support more accurate causal analysis. 




Learning Objectives 
At the end of this week, you will be able to: 

Draw directed acyclic graphs/causal diagrams to describe a particular situation. 
Identify front door and back door paths in causal diagrams. 
Identify confounders in causal diagrams. 
Identify colliders in causal diagrams. 
Draw causal diagrams that use time to permit feedback loops. 

Logistic regression is a useful method when the outcome we want to predict is binary. Similar to linear regression, it starts by creating a linear combination of the input features and their coefficients. Because of this, logistic regression may struggle to capture complex nonlinear relationships unless we introduce transformations, interaction terms, or additional engineered features. The main difference is that logistic regression passes this linear combination through a sigmoid function, which converts the result into a value between 0 and 1. This allows the final output to be interpreted as a probability rather than a continuous value.

If you're a visual learner like me, check out this YouTube video from Visually Explained. It does a great job of showing how logistic regression works using simple examples and clear animations:

https://www.youtube.com/watch?v=3bvM3NyMiE04


Did you know? Logistic regression in scikit-learn uses L2 regularization by default?

This week’s SVM topic made me think about how businesses could predict whether someone will buy a product. For example, browsing time, pages viewed, and previous purchases could help a model identify patterns in customer behavior.

However, spending more time on a website does not always mean someone will buy something. Some people compare products for a long time, while others know exactly what they want. A soft-margin SVM allows some classification errors, which makes sense when buyers and non-buyers have overlapping behaviors.

This video is a useful resource for understanding SVM because it focuses on explaining the algorithm and links to worked examples. Connecting these concepts to shopping behavior makes the topic easier to understand.


https://www.youtube.com/watch?v=CWhFt6dJZ5g

Hello all,

While looking at this week's materials, I was thinking about the different ways to do feature scaling and best way to implement it with my data sets.

There are several ways to handle scaling, but I thought this site was helpful since it gave a few different types of scaling, along with implementation examples, and cases where you may consider using the different methods.

https://towardsdatascience.com/all-about-feature-scaling-bcc0ad75cb35/9

I thought this might be helpful since I like to see examples in addition to the underlying theory.


Towards Data Science - Apr 05, 2020

All about Feature Scaling
Scale data for better performance of Mach

This one is so good, I had to literally copy-paste and link directly to their profile.

The example is a good case of hindsight being 20-20, but sometimes there are so many groupings within the data the true story can go unnoticed.


You do not know, what you do not know in which you don't know.


You know?


We see subset clusters like this a lot in healthcare research, so be sure be thorough in your analyses and apply your subject matter expertise.


The original LinkedIn profile:

https://www.linkedin.com/in/giannis-tolios/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BOxqv6BBgQLGzqwV4j9DZEg%3D%3D4



    