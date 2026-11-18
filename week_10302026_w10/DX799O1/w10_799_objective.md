Learning Objectives
At the end of this week, you should be able to: 

Explain the k-means clustering algorithm 
Apply the elbow method to determine the optimal number of clusters 
Describe the calculations for the elbow method and the Silhouette score for cluster evaluation 
Explain the importance of distance metrics and feature scaling in k-means 

Hello all,

While reading through the week's material, as usual I started looking for resources that can give some good examples and use cases.

As usual towardsdatascience.com has some nice examples and use cases for different types of clustering and upsides/downsides of each.

https://towardsdatascience.com/6-types-of-clustering-methods-an-overview-7522dba026ca/2

For some Python examples, statology.org also gives an easy to follow example of how to apply the "elbow method" to a sample data set as a good starting point.

https://www.statology.org/performing-cluster-analysis-in-python-a-step-by-step-tutorial/


This freecodecamp.org example covers more methods (DBSCAN, t-SNE, hierarchical clustering, etc.) along with sample code that seemed like it could be useful as well. Just be aware its a long read and there's some ads on the page:

https://www.freecodecamp.org/news/clustering-in-python-a-machine-learning-handbook


I'm still trying to wrap my head around which methods may be useful for my data considering the number of features since I feel like getting a meaningful model that is interpretable and can give a strong conclusion has been an issue for me, but hopefully the resources are helpful.

I'm interested to hear what methods have seemed most useful for everyone else too, and any hurdles that you've all run into.

Think About It
When would we use the k-means algorithm? 
When would the Silhouette score be used as opposed to the elbow method? 
Why do we use k-means only with the Euclidean metric? 



While researching clustering algorithms this week, a recurring theme was how challenging it can be to evaluate the model's performance. Because unsupervised learning algorithms deal with data without labels, it is not always clear what the expected results should look like, so evaluating the performance usually requires manual inspection. I looked for more resources about this and found a Google guide that I thought described the process clearly and concisely. As a visual learner, I liked how it uses clear visualization examples and a step-by-step flowchart to evaluate clusters.

https://developers.google.com/machine-learning/clustering/kmeans/evaluate-results3

I wanted to share this Stanford article which I found better resource,

I thought this was a very helpful overview of clustering. The comparison of different methods, especially K-means and hierarchical clustering, made it easier for me to understand how unsupervised learning can discover meaningful patterns without predefined labels


https://web.stanford.edu/class/stats305c/lectures/Clustering.html