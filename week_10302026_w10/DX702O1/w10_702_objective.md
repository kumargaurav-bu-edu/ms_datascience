Week 10 Overview
This week’s content introduces fixed effects models as a method for controlling unobserved confounders in grouped data. It explains the logic of isolating within-group variation by assigning a fixed intercept to each group, allowing the estimation of consistent treatment effects when group-level characteristics are unknown or unmeasured. The distinction between between-group and within-group variation is emphasized, along with practical estimation techniques such as demeaning and dummy variable encoding. The material also covers two-way fixed effects, where multiple grouping structures are present, and explores the interpretation of model coefficients and R² values. Extensions and alternatives are presented, including random effects models, which rely on distributional assumptions, and clustered standard errors, which address correlation in error terms. The week concludes with hierarchical random effects models that incorporate partially predictable group-specific variation based on observed characteristics. 


Learning Objectives 
At the end of this week, you will be able to: 

Apply fixed effects and two-way fixed effects models. 
Understand random effects. 
Review heteroskedasticity and nonlinear regression. 

Topic Overview 
Fixed effects models provide a powerful strategy for controlling for unobserved, group-level influences in observational data. When data is organized into meaningful groups — such as individuals over time, hospitals, classrooms, or cities — there may be hidden characteristics that differ across groups and confound the relationship between a treatment and an outcome. Fixed effects address this by assigning a separate baseline level, or intercept, to each group, effectively removing the influence of any group-specific confounders that remain constant within that group. By focusing on variation within each group rather than differences between groups, fixed effects models allow for a cleaner estimate of how changes in a predictor variable are associated with changes in the outcome, assuming the effect is consistent across groups. This section introduces the logic behind fixed effects, explains the distinction between within-group and between-group variation, and illustrates the concept with intuitive examples. 

Learning Objectives 
Apply fixed effects and two-way fixed effects models. 
Understand random effects. 
Review heteroskedasticity and nonlinear regression.

Required Resources
The following resources are required for your learning this week. Make sure you review everything linked below, as you may be tested on the concepts in an upcoming Knowledge Check or Quiz. 

Reading | Huntington-Klein, N. (2022, January 5). The effect: An introduction to research design and causality. Chapman & Hall.

Read the following chapters: 

Chapter 16 and any part of chapter 13 that matches the assigned topics (e.g., heteroskedasticity and nonlinear regression). 
In all cases, do the entire reading. If for any reason you do not have time to do the entire reading, read a given chapter from the beginning and get as far as you can. 

