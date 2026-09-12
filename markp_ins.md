   Now I want to add detailed markup/explanations for **each cell** in this program.

   For every cell, please explain:

   1. **Why are we doing this?**

      * What is the purpose of this cell?
      * What problem does it solve?
      * Why is this step necessary in the overall data science workflow?

   2. **What are we doing?**

      * Explain what the code is actually doing in simple, beginner-friendly language.
      * Explain the important functions, libraries, variables, parameters, and outputs being used.

   3. **How are we doing it?**

      * Walk me through the logic step by step.
      * Explain the data flow and how the output of this cell is used by subsequent cells.
      * If there is any data science or machine learning concept involved, explain the concept before or alongside the code.

   4. **Why did we choose this approach?**

      * Explain why this particular method, algorithm, library, model, or technique was selected.
      * Explain the assumptions behind the approach.
      * Mention any important trade-offs.

   5. **What are the alternatives?**

      * Identify reasonable alternative approaches.
      * Briefly explain how each alternative would work.
      * Explain when an alternative might be better than our current approach.
      * If there is a simpler or more standard approach, mention it.

   6. **What should I learn from this cell?**

      * Highlight the key data science/programming concepts I should understand.
      * Define unfamiliar terminology.
      * If there is a concept that is particularly important for someone learning data science, call it out clearly.

   7. **Potential issues and improvements**

      * Point out anything that could go wrong.
      * Mention edge cases, scalability concerns, performance considerations, or potential sources of bias/error.
      * Suggest improvements where appropriate.

   
   8. **How do we interpret the result?**

      This is a critical part of the explanation. Do not stop at explaining what the code does. **After the notebook/code produces an actual result, explain what that result means and what conclusion we should draw from it.**

      For every cell that produces an output, statistical result, model result, metric, table, graph, or visualization:

      * Explain **what the output is telling us in plain English**.
      * Explain what each important number represents.
      * Explain whether the result is large, small, high, low, significant, insignificant, good, poor, or otherwise meaningful **when such an interpretation is appropriate**.
      * Explain the relevant threshold or reference point, if one exists.
      * Explain what statistical hypothesis is being tested, if applicable.
      * Clearly state the **null hypothesis (H₀)** and **alternative hypothesis (H₁)** in simple language.
      * Explain how the observed result affects our decision regarding the hypothesis.
      * State the appropriate conclusion in plain English.
      * Explain what we **can conclude** from the result.
      * Explain what we **cannot conclude** from the result.
      * Distinguish between:

      * statistical significance,
      * practical/business significance,
      * association/correlation,
      * and causation.
      * If the result involves a model, explain what the result says about the model and/or individual predictors.
      * If the result involves a metric, explain whether the value is considered good or bad **and why**, rather than simply labeling it good or bad.
      * If the result involves a visualization, explain the important patterns, relationships, outliers, trends, or differences that I should notice.
      * If the output is unexpected, explain possible reasons why.
      * If the output is ambiguous, explicitly say what additional analysis would be needed before drawing a stronger conclusion.
      * **Do not interpret numbers in isolation. Consider the context of the analysis, the variables involved, the units, assumptions, and the purpose of the model.**

   ### **For statistical tests specifically**

   When the notebook performs a statistical test, always explain:

   1. **What question are we trying to answer?**
   2. **What is H₀?**
   3. **What is H₁?**
   4. **What does the test statistic mean?**
   5. **What does the p-value mean?**
   6. **What significance level (α) are we using, such as 0.05, and why?**
   7. **Do we reject or fail to reject H₀?**
   8. **What does that decision mean in plain English?**
   9. **What does the result NOT prove?**
   10. **What additional information should we examine before making a practical or business conclusion?**

   ### **For regression/model coefficients specifically**

   When interpreting regression coefficients, explain:

   * The coefficient estimate and its direction.
   * What a positive or negative coefficient means.
   * The units of the coefficient.
   * The t-statistic and what it measures.
   * The p-value and whether the coefficient is statistically significant.
   * The confidence interval, if available.
   * Whether statistical significance means practical importance in this particular case.
   * Whether the coefficient represents an association or can reasonably be interpreted causally.
   * Whether multicollinearity or other model assumptions could affect the interpretation.
   * Compare predictors only when that comparison is statistically and practically appropriate.
   * **Do not conclude that the variable with the largest t-statistic necessarily has the largest effect.**
   * **Do not conclude causation merely because a coefficient is statistically significant.**

   ### **After interpreting the individual results, provide a conclusion**

   For cells containing statistical/model results, finish the explanation with:

   **### Result interpretation**

   Explain the result in beginner-friendly language.

   **### What does this tell us?**

   State the key finding.

   **### What can we conclude?**

   Give the appropriate statistical/data-science conclusion.

   **### What can we NOT conclude?**

   Clearly identify conclusions that would be unjustified.

   **### Example conclusion**

   If appropriate, provide a short example of how I could explain this result to another person in a meeting, report, or interview.

---

   ### Important context

   I am relatively new to data science and I am using AI to help me build this program. **My goal is not just to get working code—I want to understand what I am building.**

   Therefore:

   * Do not assume I already understand data science terminology.
   * Explain concepts in simple language first, then introduce the technical terminology.
   * Do not just say "this is standard" or "this is best practice." Explain **why**.
   * When you use a technical term, briefly explain what it means.
   * Distinguish clearly between **what is required**, **what is recommended**, and **what is simply one possible choice**.
   * If there are multiple valid approaches, explain the reasoning behind choosing one.
   * Do not unnecessarily rewrite working code just for the sake of changing it.
   * Preserve the existing functionality unless there is a good technical reason to change it.

   ### Format

   ### Format for the Jupyter Notebook

   This is a Jupyter notebook, so I want the explanations to become part of the notebook itself.

   For every code cell:

   * Add a **Markdown cell immediately before the code cell**.
   * The Markdown cell should explain the purpose and reasoning behind the following code.
   * Do not put all explanations at the end of the notebook.
   * Keep the explanation close to the code it describes so I can study the notebook from top to bottom.

   Use this structure for each Markdown cell:

   ### Cell X — [Short Description]

   **Why are we doing this?**
   Explain why this step is necessary and what problem it solves.

   **What are we doing?**
   Explain what the following code does in simple, beginner-friendly language.

   **How does it work?**
   Walk through the logic step by step. Explain important functions, parameters, variables, libraries, and data flow.

   **Why did we choose this approach?**
   Explain the reasoning behind the method or implementation we selected.

   **Alternatives:**
   Explain other reasonable approaches and when they might be preferable.

   **Key data science concepts:**
   Explain the important concepts and terminology I should learn from this cell.

   **Potential issues / improvements:**
   Explain anything that could go wrong, including assumptions, edge cases, performance, scalability, bias, or other concerns.

   **Connection to the next step:**
   Explain:

   1. What this cell produces.
   2. How the next cell uses that output.
   3. **Why the result we just obtained matters for the next step.**
   4. **What decision, interpretation, or hypothesis does this result lead us toward?**
   5. If this is a model evaluation or statistical test, explain whether the result means we should continue, investigate further, modify the model, or draw a conclusion.

   This last part is important because it teaches you the **reasoning chain**:

   **Code → Output → Interpretation → Conclusion → Next decision**

   ### Important

   Do not modify the code just to add explanations. Preserve the existing functionality unless a technical improvement is genuinely necessary.

   The goal is for the final notebook to serve as both:

   1. A **working data science program**, and
   2. A **learning/study guide** that I can read later and understand without depending entirely on AI.

   Please make the explanations detailed enough that I could eventually understand and explain the entire program myself, rather than simply relying on AI to generate the code.

   ### **Key learning**

   **A statistically significant coefficient tells us that there is evidence that the coefficient is not zero. It does not tell us how large or practically important the effect is.**

   That distinction is exactly the kind of thing I'd want your AI-generated notebook to teach you.

   If you add the section above to your prompt, your notebook should become much more of a **“code → result → interpretation → conclusion → decision” study guide**, rather than just annotated code.