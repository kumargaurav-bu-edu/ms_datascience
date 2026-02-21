Skip to main content
Open
Course status Open
26sprgcdsdx699_o2
DX699 O2 AI for Leaders (Spring 26)
Course Content
Syllabus
Quiz: Course Policies
No due date
Formative
Complete this quiz to show that you have read and understood the course policies outlined in the syllabus. Please note you will not be able to access Week 2 of this course until you have acknowledged the course policies.

This topic covers everything you need to know to get started with this module!
1 of 6 started

The BU Virtual Campus
Access the virtual campus, your destination for dedicated support on the OMDS program.
LTI Link
Yellowdig
Live Sessions Information
Access useful information about faculty live sessions.
Group Office Hours Information
Access useful information about group office hours.

Explore how to preprocess and summarize data when working with a dataset.
4 of 4 started


Explore how to apply Week 1 ideas about preprocessing to your own datasets.
5 of 5 started


Explore univariate analysis by analyzing individual columns of data independent of their relationships with other columns.
1 of 5 completed


Apply the univariate ideas from Week 3 to your own datasets.
1 of 8 completed


Explore bivariate analysis, including scatter plots, pair plots, line graphs, waterfall plots, and area plots, as well as correlations.

Apply the bivariate ideas from Week 5 to your own datasets.
1 of 6 started

Course Faculty
Joshua Von Korff
Instructor

Show more
Details & Actions
Roster
View everyone in your course

Attendance
View your attendance

Books & Tools
View course & institution tools

Course Announcements
Milestone 3 Rubric Clarifications
As you continue working on Milestone Three, please review the rubric carefully and use the exact section headings listed in the submission outline. Below are additional clarifications to help you move from a broad project idea to a strong, focused analysis.



Description of Project: Moving from Broad Topic to Specific Question



Each of you selected a project from the pre-approved list. The project descriptions were intentionally broad. Your job is to narrow that topic into a more specific analytical focus.

You should not simply restate the project blurb. Instead, clearly define:

What specific question are you trying to answer?
What population, time period, or outcome are you focusing on?
Why does this question matter?


Examples:

If the project is about healthcare costs:

Broad: “Analyze healthcare spending trends.”

More specific: “Examine whether patient age and insurance type are associated with higher out-of-pocket costs in urban hospitals between 2018–2022.”



If the project is about housing data:

Broad: “Study housing price patterns.”

More specific: “Investigate whether proximity to public transportation is associated with higher median home prices in metropolitan areas, and whether that relationship differs by neighborhood income level.”



Your description should explain what your analysis entails and the potential impact of answering that question.



Preprocessing: What Did You Learn?



Preprocessing is not just cleaning. It is about understanding the structure and quality of your data.

Examples of preprocessing steps:

Identifying and handling missing values (dropping rows, imputing, flagging missingness)
Converting categorical variables into consistent formats (i.e. one-hot encoding)
Standardizing units (e.g., dollars, percentages, time formats)
Removing duplicates
Merging datasets and evaluating join quality
Detecting outliers
Filtering unrealistic values
There is no single “correct” preprocessing workflow. You must look at your dataset and decide what is needed.



Example:

If 40 percent of one variable is missing, you may:

Drop the variable and explain why
Impute values and justify the method
If one dataset cannot be reliably merged due to inconsistent keys, that is an insight. You would explain the issue and how it affects your analysis. In this section, explain what trends, patterns, or data quality issues you discovered during preprocessing.



Univariate Analysis: What Does Each Variable Look Like?



Univariate analysis focuses on one variable at a time.

Examples:

Histograms of income, age, or price
Bar charts of categorical variables (industry, region, gender)
Summary statistics (mean, median, standard deviation)
Identifying skewed or bimodal distributions
Detecting extreme values
Example:

If income is heavily right-skewed, that suggests a few extreme earners may influence modeling decisions. You would discuss whether a log transformation might later be appropriate. If a categorical variable is highly imbalanced (e.g., 90 percent in one category), that may impact model performance.



Bivariate Analysis: How Variables Relate

Bivariate analysis examines relationships between two variables.

Examples:

Scatterplots (price vs. square footage in a real estate project)
Correlation matrices
Boxplots of outcome by category
Crosstab tables
Grouped means


Example:

If you find a strong positive correlation between years of experience and salary, that suggests predictive potential. If two predictors are highly correlated with each other, that may indicate multicollinearity concerns for regression. Again, there is no right answer. The dataset determines what relationships are meaningful to explore.



Dataset Inclusion and Disqualification

Reminder: You must maintain at least one of the original datasets listed under your selected project.

When discussing inclusion or exclusion:

If you added new datasets and later found one unusable, explain why.
Do not explain why you did not use all original datasets. That is not the purpose of this section.


Example:

If you attempted to use an external dataset but discovered it lacked matching keys or had incompatible time periods, you would explain why it was excluded and how that affects your conclusions.



Supervised or Unsupervised Analyses Suggested

You are not building a full model. You are identifying 1–2 appropriate models suggested by your exploratory work.

Focus on a maximum of two models.

Examples:

If your project predicts a numeric outcome:

Linear regression (if relationships appear approximately linear)
Random forest regression (if nonlinear patterns are visible)
If your outcome is categorical:

Logistic regression
Decision tree classifier
If no labeled outcome exists:

K-means clustering to identify groups
Hierarchical clustering
You must explain why the model fits your data structure and research question.

Example:

“If housing prices show a linear relationship with square footage and location indicators, a multiple linear regression would be appropriate. However, because of potential nonlinear effects, a tree-based model may better capture interactions.”



Figures Formatting

You are required to include 6–8 figures in the body of the paper.

It is strongly recommended that:

You place all graphs on a single page near the end.
Arrange them two across and three down.
Caption them as Figure 1, Figure 2, etc.
In the text, reference them directly:

“As shown in Figure 2, income distribution is heavily right-skewed.”

This approach ensures fairness in page count. That figure page does count toward the 8–12 page limit.



AI Appendix

You must include an AI appendix if you used AI. If you did not, ignore this section.

If you did use AI:

List the prompts you used.
Include the output you relied on.
If the conversation was long, include only the final output you used.
Write a short paragraph explaining how AI assisted you.


This appendix does not count toward the page limit, but it must be attached at the end of your submission.



References Page

You must include:

Citations for all datasets used
Citations for any articles referenced
The references page does not count toward the page limit.



Final Reminder

Milestone Three is about insight, not volume. The rubric emphasizes clear reasoning, thoughtful interpretation, and justified decisions. There is no universal template for analysis. The quality of your explanation is what determines an exemplary submission.

If you are unsure whether a particular analysis step is appropriate for your dataset, ask yourself: what question am I trying to answer, and does this analysis help clarify it?



