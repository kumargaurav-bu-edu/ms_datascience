---

# ✅ **Additional Instructions for Generating a High-Quality Quiz**

### **1. Ensure Full Coverage of Learning Objectives**

The quiz must include questions that directly test all listed learning objectives:

For Example :

* Ranking vs. classification
* Profit curves
* ROC curves
* Lift curves
* Capstone proposal development
* Understanding of AUC, thresholds, confusion matrix relationships

Include **at least 2–3 questions per objective**.

---

### **2. Focus on Theoretical & Conceptual Understanding**

The quiz must:

* Avoid coding-heavy questions (unless demonstrating formula application).
* Emphasize conceptual clarity, definitions, and interpretations.
* Include scenario-based reasoning (e.g., “A model has a high AUC but low profit—why?”).
* Include error analysis questions (e.g., misinterpreting ROC curves).

---

### **3. Require Formula Knowledge & Application**

Since learners must practice formulas, include:

* Calculations based on confusion matrix entries (TP, FP, FN, TN)
* Deriving TPR, FPR, precision, recall
* Interpreting slope of ROC
* Interpreting lift scores

These can be **multiple-choice** or **short numerical answers**.

---

### **4. Include Multiple Question Types**

Ensure the quiz is diverse and engaging:

* Multiple choice
* True/false
* Short answer
* Fill-in-the-formula
* Interpretation of a graph (descriptive—no image required)
* Scenario questions comparing two models

---

### **5. Include Increasing Difficulty Levels**

Specify three tiers:

* **Level 1 (Basic):** Definitions, conceptual clarity
* **Level 2 (Intermediate):** Formula application, curve interpretation
* **Level 3 (Advanced):** Comparing models using profit/ROC/lift curves

---

### **6. Include Real-World Context**

Ensure questions relate to problems similar to:

* Fraud detection
* Credit scoring
* Customer churn
* Marketing response models

This strengthens understanding of how curves are used in practical decision-making.

---

### **7. Include Explanation for Each Correct Answer**

Require detailed explanations so learners understand:

* Why an answer is correct
* Why alternatives are incorrect
* How the concept connects back to the learning objectives

---

### **8. Ensure Quiz Length & Structure**

Require:

* Minimum **20 questions**
* Maximum **40**
* Balanced distribution across topics

---

### **9. Promote Critical Thinking**

Add instructions to include:

* Tradeoff questions (sensitivity vs. specificity)
* Curve comparison questions (ROC vs. lift vs. profit)
* Threshold effect questions



### **10. Enforce Concrete, Non-Abstract Answers**

All questions and answer keys **must avoid abstract placeholders** such as:

> “chart type”, “context”, “focus”, “declutter”, “story structure”, “action”, “visual encoding”

Instead, **require specific, concrete choices**, for example:

**Allowed:**

* Bar chart, line chart, slopegraph, stacked bar chart, area chart, dot plot
* Sort bars descending
* Add a callout annotation showing +40% CAC
* Highlight CAC in red, LTV in gray
* Remove gridlines and background shading
* Add subtitle explaining business impact
* Add a reference line for prior year CAC
* Use icons or arrows to show direction of change

**Disallowed:**

* Generic terms like “use a good chart type”
* Meta-framework labels without execution detail
* Any answer that could apply to *any* visualization

---

### **11. Force Actionable Design Steps in Storytelling Questions**

For any question related to:

* Storytelling with Data
* Dashboard design
* Executive communication
* Visual best practices

The **correct answer must include at least 3 concrete actions**, for example:

1. Chart choice (e.g., slopegraph instead of bar chart)
2. Visual emphasis (e.g., bold color for CAC increase, muted LTV)
3. Annotation (e.g., +40% callout, profitability warning label)
4. Layout change (e.g., left-to-right chronological order)
5. Decluttering step (e.g., remove legend, gridlines, borders)

Answers missing concrete design steps should be marked **incorrect**.

---

### **12. Use Question Formats Strategically to Maximize Learning Depth**

Do **not** default all questions to multiple choice.
Select the format based on the **learning objective and difficulty level**.

---

### **A. Format Rules by Difficulty Tier**

**Level 1 (Basic – Definitions & Formulas)**
Use **fill-in-the-blank or short answer only** (no options):

* Metric definitions (AUC, precision, recall, lift, ROC)
* Formula recall and application
* Confusion matrix relationships
* Simple numeric calculations

Purpose:
➡ Encourages **active recall** and prevents answer-pattern guessing.

---

**Level 2 (Intermediate – Interpretation & Application)**
Use a **mixed format**:

* Fill-in-the-blank for:

  * Curve interpretation
  * Metric tradeoffs
  * Threshold effects
* Multiple choice (4 options) for:

  * Comparing two models
  * Identifying flawed reasoning
  * Selecting the best analytical approach

Purpose:
➡ Builds **reasoning depth** while introducing scenario discrimination.

---

**Level 3 (Advanced – Strategy & Decision-Making)**
Use **scenario-based multiple choice + open-ended prompts**:

* Multiple choice (4 options) when:

  * Evaluating competing strategies
  * Selecting the best business decision
  * Comparing ROC vs lift vs profit curves
* Open-ended (no options) when:

  * Designing a solution from scratch
  * Recommending thresholds or actions
  * Explaining tradeoffs in business terms

Purpose:
➡ Tests **synthesis, judgment, and real-world decision-making**.

---

### **B. When Multiple Choice Is Used**

If MCQ format is chosen:

* Always generate **4 realistic answer options (A–D)**
* Only **one option** may be fully correct
* Distractors must be *plausible but flawed*, such as:

  * Wrong chart choice
  * Incorrect threshold logic
  * Misinterpreted ROC slope
  * Poor business framing
  * Over-optimized for accuracy instead of profit

Purpose:
➡ Preserves **scenario-based discrimination** and forces concept mastery.

---

### **C. When Fill-in-the-Blank / Short Answer Is Used**

If open-ended format is chosen:

* Do **not** provide answer options
* The correct answer must:

  * Use **concrete terms** (no abstract labels)
  * Reference **specific metrics or variables**
  * Include at least **one actionable insight** when relevant
* Vague or framework-only answers must be graded **incorrect**

Purpose:
➡ Encourages **active recall & synthesis** and blocks pattern-matching.

---

### **D. Anti–Pattern Recognition Rule**

Across the full quiz:

* Do **not** reuse answer structures or phrasing patterns
* Avoid predictable placement of correct answers
* Vary:

  * Question length
  * Numerical vs conceptual prompts
  * Answer styles (numeric, verbal, strategic)

Purpose:
➡ Prevents learners from gaming the test instead of learning.


---

### **13. Replace Generic “Concept Lists” with Executable Answers**

If a correct answer would normally be a list of concepts (e.g., *focus, context, story, action*),
**translate it into execution**, such as:

* “Use a slopegraph comparing CAC vs LTV for 2024 vs 2025”
* “Color CAC red and add a +40% arrow annotation”
* “Add a subtitle: ‘Rising acquisition cost is eroding margin’”
* “End slide with a call-to-action: ‘Optimize acquisition channels or raise pricing’”

Answers that remain conceptual should be **rejected**.

---

### **14. Require Explicit Business Actions When Prompt Asks to “Drive Action”**

Whenever a question includes:

> “…drive action”, “what should leadership do?”, “recommend next steps”

The answer must include **at least one explicit business decision**, such as:

* Reduce paid media spend
* Reprice premium plans
* Improve onboarding to raise LTV
* Shift budget to organic channels
* Run retention campaigns
* A/B test new acquisition funnels

---

### **15. Validate Against a “Could This Be Any Chart?” Test**

Before finalizing any correct answer:

Apply this rule:

> If the answer could apply to *any* business chart, it is **invalid**.

The answer must reference:

* The **specific metric(s)** in the question
* The **specific business risk** (e.g., profitability decline)
* The **specific visual technique** used to highlight that risk

---
### 16. Quiz Standard
Ensure that all quiz questions and scenarios are designed at the academic rigor and difficulty level expected in a typical U.S. Master’s (MS) program.



## setup an interactive python program quiz which is reusable. for example you took questions and answer as json and running the program on it. adding more questions or changing questions set will be smoothless.(will use generic_quiz.py to practice the quiz)