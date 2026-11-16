Welcome to Week 11!
This week, you will examine the following: density-based spatial clustering of applications with noise (DBSCAN), hierarchical agglomerative clustering (HAC), linkage methods in HAC, and the use of dendrograms to choose clusters. 


Learning Objectives
At the end of this week, you should be able to: 

Explain how DBSCAN applies to cluster datasets and how it identifies core, border, and noise points based on given 
ϵ
 and MinPts values. 
Define a cluster in DBSCAN based on the concept of core point connectivity. 
Compare and contrast linkage methods (single, complete, average, Ward’s) in hierarchical agglomerative clustering and explain how each influences cluster merging. 
Interpret dendrograms to determine a suitable number of clusters in HAC. 

Think About It
How do the choices of 
ϵ
 and MinPts in DBSCAN affect the number and shape of clusters — and what might go wrong if these values are poorly chosen? 
Why might different linkage methods in HAC (like single vs. complete linkage) lead to very different clustering results, even when starting from the same data? 
When would you choose DBSCAN over HAC — or vice versa — based on the structure or goals of your analysis? 




Resources on DBSCAN and Hierarchical Clustering
Week 11 Resource Showcase


Mark Irsfeld
Today at 10:21 PM EST
Mark as read
More Options
This week, I found a couple of nice articles. First is a blog from medium.com: https://medium.com/data-science/how-to-use-dbscan-effectively-ed212c02e621

In the blog, author Vijini Mallawaarachchi gives a pretty straightforward read on how to tune DBSCAN, including some nice code and visual examples. It also introduced me to a python library called "kneed" that is focused on helping find the "elbow" in your k-means curves. I may give it a shot myself.

Another good article for hierarchical clustering is this article from stackabuse.com by author Cássia Sampaio.

https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

This one is a bit longer, but I like it since it gives some good practical examples starting with EDA and initial plotting, to encoding, dimensionality reduction/PCA and then the different clustering methods and how you might draw conclusions.

The code and visualizations are nice and clear, and the article does a really good job of giving a nice review of some of the methods that were discussed in yesterday's live session.

I know I'm going to have a experiment with my data and how to best set up these diagrams to draw a meaningful conclusion, so I am interested to hear how others are approaching it in their projects.

