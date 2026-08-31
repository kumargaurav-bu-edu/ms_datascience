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

* Minimum **25 questions**
* Maximum **35 questions**
* Balanced distribution across topics and learning objectives

**Recommended Breakdown (for 25-35 questions):**
- Level 1 (Basic): 30-35% → 7-12 questions
- Level 2 (Intermediate): 40-50% → 10-17 questions
- Level 3 (Advanced): 15-25% → 4-9 questions

**Example for 26 questions (DX603 Week 3):**
- Level 1: 8 questions
- Level 2: 12 questions
- Level 3: 6 questions

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
### **16. Quiz Standard**

Ensure that all quiz questions and scenarios are designed at the academic rigor and difficulty level expected in a typical U.S. Master's (MS) program.

---

## **CRITICAL: JSON Schema Structure & Format**

### **Quiz File JSON Schema Specification**

**All quiz_questions.json files MUST follow this exact structure:**

```json
{
  "quiz_metadata": {
    "title": "string (format: 'COURSE_CODE SEMESTER: WEEK# TOPIC' e.g., 'DX603 Spring 2026: Week 3 - Underfitting, Overfitting & Bias-Variance Tradeoff')",
    "description": "string (1-2 sentences summarizing quiz scope and connection to learning objectives)",
    "version": "string (should be '1.0')",
    "total_questions": "integer (must be 25-35 inclusive)"
  },
  "questions": [
    {
      "number": "integer (1-indexed, sequential 1 to total_questions)",
      "level": "integer (MUST be 1, 2, or 3 only)",
      "question_type": "string (MUST be one of: 'fill_in', 'multiple_choice', 'true_false', 'short_answer', 'scenario', 'calculation', 'interpretation', 'analysis')",
      "section": "string (derived from learning objective topic; max 50 characters)",
      "question_text": "string (clear, specific, no abstract placeholders like 'chart type' or 'declutter')",
      "options": "array of 4 strings OR null (4 options ONLY for multiple_choice; null for all other types)",
      "correct_answer": "string (concrete, specific, never abstract terms or vague framework labels)",
      "explanation": "string (min 2-3 sentences: why correct + why alternatives wrong + link to LO)",
      "learning_objective": "string (exact match to one learning objective from course material)",
      "keywords": "array of 4-6 strings (for open-ended questions only; empty array for MCQ and true_false)"
    }
  ]
}
```

---

### **Subject-Specific Notes**

This quiz generation framework applies to all three subjects:

1. **DX699 O2: AI for Leaders**
   - Focus: Conceptual understanding, business implications, strategic decision-making
   - Real-world context: AI governance, organizational readiness, ROI, ethical implications
   - Avoid: Deep technical implementation details, coding

2. **DX603 O1: Machine Learning Fundamentals**
   - Focus: Algorithms, formulas, model evaluation, statistical concepts
   - Real-world context: Fraud detection, credit scoring, churn prediction, medical diagnosis
   - Include: Confusion matrix calculations, ROC interpretation, threshold selection

3. **DX604 O1: Data Management at Scale**
   - Focus: Schema design, governance, compliance, data quality, architecture
   - Real-world context: HIPAA, GDPR, financial regulations, data migration, ETL
   - Include: Schema types, governance frameworks, stewardship roles, tools

---

### **Section Naming Strategy**

**Rule: Create ONE section per Learning Objective**

The quiz section name should directly map to the learning objective. Use the topic area from the LO.

**Naming convention:**
- Extract the primary topic from the learning objective
- Use 2-4 words, capitalized
- Make it self-contained (don't reference framework names)

**Examples:**

For DX603:
- LO: "Analyze the notions of underfitting and overfitting" → Section: "Underfitting and Overfitting"
- LO: "Define the crucial concept of generalization" → Section: "Generalization"
- LO: "Explain the bias-variance tradeoff" → Section: "Bias-Variance Tradeoff"

For DX604:
- LO: "Define data schemas" → Section: "Data Schemas"
- LO: "Compare various types of data governance" → Section: "Data Governance Types"
- LO: "Explore best practices for implementing data governance" → Section: "Implementing Data Governance"

For DX699:
- LO: "Understand AI readiness assessments" → Section: "AI Readiness & Assessment"
- LO: "Evaluate ethical implications of AI" → Section: "AI Ethics & Governance"

---

### **Learning Objective Coverage & Distribution**

**Step 1: Create Coverage Table**

Before generating questions, create this verification table:

| Learning Objective | Section Name | Target Questions | Planned Question Types | Planned Levels |
|---|---|---|---|---|
| (LO 1 text) | Section A | 8-9 | fill_in(2), MCQ(2), scenario(1), ... | L1: 2, L2: 4, L3: 1 |
| (LO 2 text) | Section B | 8-9 | fill_in(1), MCQ(3), analysis(2), ... | L1: 2, L2: 4, L3: 2 |
| (LO 3 text) | Section C | 8-9 | MCQ(2), true_false(2), interpretation(1), ... | L1: 3, L2: 4, L3: 2 |
| *TOTAL* | *All* | ***25-35*** | *(all types represented)* | *L1: 7-12, L2: 10-17, L3: 4-9* |

**Step 2: Allocate Questions Per Objective**

For N learning objectives:
- Minimum questions per objective: 25 ÷ N (rounded up)
- Target questions per objective: 30 ÷ N (rounded up)
- Maximum per objective: 35 ÷ N (rounded down)

**Example: 3 learning objectives, 26 questions:**
- Minimum per LO: 9 questions
- Target: 8-9 questions each
- Distribution: 8 + 9 + 9 = 26 ✓

**Step 3: Verify Coverage**

- [ ] All learning objectives represented with 2-3+ questions minimum
- [ ] Each section has at least 1 Level 1, 1 Level 2, and 1 Level 3 question (when possible)
- [ ] Each section includes ≥1 real-world scenario

---

### **Question Type Decision Tree**

Use this tree to select appropriate question type based on difficulty level and learning objective:

```
START: What is the difficulty level and what are we testing?

LEVEL 1 (Definitions, Formulas, Foundational Concepts)
├─ Is the question asking for a DEFINITION or FORMULA RECALL?
│  └─→ Use: fill_in (with 4-5 keywords)
│     Example: "___ is the error from overly simple assumptions"
│
├─ Is the question a YES/NO statement about a concept?
│  └─→ Use: true_false (answer: True or False only)
│     Example: "True/False: Overfitting means low training error but high test error"
│
└─ Is the question asking to complete a sentence with specific term?
   └─→ Use: fill_in OR short_answer
      Example: "The ___ error cannot be reduced because it comes from randomness"

LEVEL 2 (Application, Interpretation, Calculation, Comparison)
├─ Is the question asking learner to CHOOSE between alternatives?
│  └─→ Use: multiple_choice (4 realistic options, 1 clearly best)
│     Example: "Which is high-bias, likely to underfit? (A) deep tree (B) simple linear (C) neural net"
│
├─ Does the question ask to INTERPRET metrics from a scenario (2-3 sentences)?
│  └─→ Use: short_answer OR interpretation (with 4-6 keywords for evaluation)
│     Example: "A model has training R²=0.98, test R²=0.55. What's happening? Why?"
│
├─ Does the question ask for formula APPLICATION or CALCULATION?
│  └─→ Use: calculation (with keywords for partial credit)
│     Example: "Given TP=90, FP=20, FN=10, TN=80, calculate TPR"
│
└─ Does the question compare TWO approaches, models, or frameworks?
   └─→ Use: multiple_choice (each option presents competing strategy)
      Example: "To reduce overfitting without more data, choose best action: (A) ... (B) ..."

LEVEL 3 (Strategy, Synthesis, Real-World Decision-Making, Design)
├─ Is the question a REAL-WORLD SCENARIO requiring action plan?
│  └─→ Use: scenario (open-ended, 4-6 keywords for evaluation)
│     Example: "You're building fraud detection. Training AUC=0.95, test AUC=0.72. 
│                What's wrong and what do you recommend? (Give 2 specific actions)"
│
├─ Does the question ask learner to DESIGN or BUILD a solution?
│  └─→ Use: analysis (open-ended, 4-6 keywords required)
│     Example: "Design a data governance framework for a healthcare company handling PHI"
│
├─ Does the question ask learner to SELECT best STRATEGY from alternatives?
│  └─→ Use: multiple_choice (4 options all plausible, but 1 is clearly best given context)
│     Example: "Your model overfits. You can't get more data. Best choice: (A) Ridge (B) ...?"
│
└─ Does the question ask for DETAILED REASONING or BREAKDOWN?
   └─→ Use: short_answer OR analysis (keywords-based evaluation)
      Example: "Explain why collecting more data reduces variance without increasing bias"
```

---

### **Keywords Selection Rules**

Keywords are used to evaluate open-ended questions (fill_in, short_answer, scenario, analysis, interpretation).

**Rule 1: Quantity**
- Level 1 fill-in: 4-5 keywords
- Level 2+ open-ended: 4-6 keywords
- Multiple choice & true/false: empty array `[]`

**Rule 2: Content**
✅ GOOD Keywords (concrete, evaluatable):
- Specific terms: "overfitting", "regularization", "Ridge", "Lasso", "L2 penalty"
- Metric names: "AUC", "TPR", "FPR", "precision", "recall", "F1"
- Actions: "reduce complexity", "add features", "cross-validation", "tune hyperparameter"
- Concepts: "bias", "variance", "training error", "generalization"

❌ BAD Keywords (abstract, not evaluatable):
- Framework labels: "focus", "context", "story", "action", "declutter"
- Vague terms: "improve", "better", "optimize", "good"
- Generic concepts: "model", "data", "train", "evaluate"

**Rule 3: Match to Answer**
- Keywords should represent the KEY CONCEPTS in the ideal answer
- Do NOT make the complete correct_answer into keywords
- DO include related terms and synonyms learner might use

**Example (GOOD):**
```json
{
  "question_text": "___ occurs when a model learns training data too closely, including noise",
  "correct_answer": "Overfitting",
  "keywords": ["overfitting", "noise", "memorize", "training", "poor generalization"],
  "explanation": "..."
}
```
Evaluator will accept:
- "Overfitting" (exact)
- "Learning training data too closely" (paraphrase)
- "Model memorizing noise" (uses keywords)
- "Poor generalization from noise" (uses 2+ keywords)

**Example (BAD):**
```json
{
  "question_text": "___ occurs when a model learns training data too closely",
  "correct_answer": "Overfitting",
  "keywords": ["Overfitting"],  // Too narrow—only exact match counts
  "explanation": "..."
}
```
Evaluator will REJECT:
- "Model overfitting to noise" (keyword exists but evaluator may miss paraphrases)

---

### **Explanation Quality Standard**

**Every question MUST have an explanation with this 3-part structure:**

**Part 1: Why the Answer is Correct (1-2 sentences)**
- Explain the core concept
- Use precise terminology (metric names, formula components, framework terms)
- Connect to the learning objective

**Part 2: Why Alternatives Are Wrong (for multiple choice: 1 sentence per option)**
- Identify the misconception or error in each distractor
- Example: "Option A confuses high bias with high variance"
- Example: "Option C is a memorization strategy, not a generalization strategy"

**Part 3: Connection to Learning Objective (1 sentence minimum)**
- How does this answer reinforce the LO?
- Why does this matter in practice?

**Example (GOOD) - DX603:**
```
Part 1 (Why Correct):
"When training and test MSE are close and both reasonably low, the model is 
generalizing well—it learned the underlying pattern without memorizing noise. 
The model performs similarly on known and new data, which is the hallmark of good generalization."

Part 2 (Why Alternatives Wrong):
- Option A: Confuses overfitting (high complexity fits noise) with generalization (low complexity that still captures signal)
- Option D: Describes underfitting (high error on both), not generalization
- Option B: Uses validation metrics but doesn't address the concept of learning pattern vs. noise

Part 3 (Connection to LO):
"This reinforces the definition of generalization: ability to perform well on unseen data. 
In practice, this is the goal of all ML—build models that work on future data, not just on training examples."
```

**Example (GOOD) - DX604:**
```
Part 1 (Why Correct):
"Centralized governance consolidates data authority under one governance council with consistent 
policies. This ensures compliance and reduces duplicated rules across departments."

Part 2 (Why Alternatives Wrong):
- Option B: Decentralized governance distributes authority, which can lead to inconsistent policies and compliance gaps
- Option D: Schema design is about database structure, not governance framework architecture

Part 3 (Connection to LO):
"This exemplifies the tradeoff in governance types—centralized ensures consistency and compliance, 
while decentralized allows flexibility. Organizations choose based on regulatory and business needs."
```

---

### **Concrete vs. Abstract Answer Validation Checklist**

**Before finalizing EVERY question's correct_answer, ask:**

| Test | Example (❌ Wrong) | Example (✅ Correct) | Fix |
|---|---|---|---|
| Is the answer a vague concept? | "chart type" | "slopegraph" OR "stacked bar chart" | Replace abstract terms with specific choices |
| Does it avoid specifics? | "add labels" | "Add annotation: '+40% CAC increase' in red font with arrow" | Include visual/concrete details |
| Is it just framework label? | "use regularization" | "Apply Ridge regression with alpha=0.01, tuned via 5-fold CV" | Specify which type, parameter, tuning method |
| Is it a generic action? | "add more features" | "Add interaction term: study_hours × prior_GPA" | Name specific features/terms |
| Does it lack context? | "improve the model" | "Train decision tree instead of linear regression to capture nonlinearity" | Explain what and why |
| Is the action missing metric? | "reduce overfitting" | "Apply L1/L2 regularization and monitor validation AUC vs. training AUC" | Include measurable outcome |

**Application Rules:**

✅ For Level 1 fill-in: Answer is usually a single term
- Correct: "Bias", "Regularization", "Generalization"
- Evaluate against keywords to allow synonyms

✅ For Level 2 application: Answer specifies one concrete approach
- Correct: "Reduce model complexity; use fewer features or regularization"
- Each clause is actionable and specific

✅ For Level 3 strategy: Answer includes 2-3+ concrete actions with reasoning
- Correct: "(1) Reduce features (removed collinear variables). (2) Apply Ridge regularization (tuned via cross-validation). (3) Collect more data if possible."
- Each action is specific and measurable

---

### **Real-World Context Mapping**

**At least ONE question per section MUST include real-world context related to the course.**

**For DX603 (Machine Learning Fundamentals):**

Real-world scenarios to draw from:
- **Fraud Detection**: Binary classification, ROC thresholds, cost of FP vs FN
- **Credit Scoring**: Model cutoffs, profit curves, regulatory constraints
- **Medical Diagnosis**: Sensitivity vs specificity tradeoff, cost of Type I vs II error
- **Customer Churn**: Retention models, targeting high-value customers
- **Marketing Response**: Conversion prediction, lift analysis, campaign ROI

**For DX604 (Data Management at Scale):**

Real-world scenarios to draw from:
- **Healthcare (HIPAA)**: PHI schema requirements, data residency, audit trails
- **EU Operations (GDPR)**: Data retention policies, right-to-be-forgotten, schema design for compliance
- **Financial Services (SOX, PCI)**: Data governance, audit controls, schema validation rules
- **Data Quality**: Duplicate records, schema evolution, data stewardship roles
- **Multi-system Integration**: ETL design, schema mapping, data lineage tracking

**For DX699 (AI for Leaders):**

Real-world scenarios to draw from:
- **AI Governance**: Organizational readiness, risk assessment, ethical review boards
- **ROI Analysis**: Cost-benefit of AI investments, change management, skill gaps
- **Bias & Fairness**: Model bias in hiring/lending, regulatory risk, mitigation strategies
- **Data Privacy**: Customer trust, regulatory compliance, reputational risk
- **Workforce Change**: Upskilling needs, job displacement, organizational culture

**Implementation Rule:**
- For each section, identify 1-2 applicable real-world contexts
- Include ≥1 scenario/interpretation question per section that references this context
- Use business outcomes (cost, compliance, customer impact) as the evaluation metric

---

### **Anti-Pattern Examples in JSON Format**

Use these examples to identify and reject poor question quality.

**❌ ANTI-PATTERN 1: Abstract correct_answer**
```json
{
  "number": 5,
  "question_text": "What technique helps reduce overfitting?",
  "correct_answer": "use regularization and cross-validation",
  "keywords": ["regularization", "cross-validation"],
  "problem": "Too vague—doesn't specify WHICH regularization (Ridge? Lasso?) or HOW to use CV"
}
```
**✅ FIX:**
```json
{
  "number": 5,
  "question_text": "Which single change most reduces model variance without increasing bias significantly?",
  "correct_answer": "Apply Ridge regression (L2 penalty on coefficients) and tune alpha via 5-fold cross-validation",
  "keywords": ["Ridge", "L2 penalty", "cross-validation", "alpha", "shrink coefficients"],
  "explanation": "Ridge regression penalizes large coefficients without removing features. Cross-validation automatically selects the penalty strength (alpha). This maintains model flexibility while reducing sensitivity to training data (variance) with minimal bias increase."
}
```

---

**❌ ANTI-PATTERN 2: Keywords don't match answer**
```json
{
  "number": 8,
  "question_text": "Define overfitting in 1-2 sentences",
  "correct_answer": "Model learns training data too closely, including noise",
  "keywords": ["model", "data", "performance"],
  "problem": "Keywords are generic—'overfitting' not included, evaluator will reject valid answers"
}
```
**✅ FIX:**
```json
{
  "number": 8,
  "question_text": "Define overfitting in 1-2 sentences",
  "correct_answer": "Model learns training data too closely, including noise, leading to poor performance on new data",
  "keywords": ["overfitting", "noise", "memorizing", "generalization", "test error"],
  "explanation": "Overfitting occurs when a high-variance model fits the training sample so closely that it learns noise rather than the true underlying pattern. This causes good performance on training data but poor performance on new, unseen data. This is core to understanding the bias-variance tradeoff."
}
```

---

**❌ ANTI-PATTERN 3: MCQ options all too similar**
```json
{
  "number": 12,
  "question_type": "multiple_choice",
  "options": [
    "A) Regularization reduces overfitting",
    "B) Regularization reduces underfitting", 
    "C) Regularization affects bias",
    "D) Regularization is a technique"
  ],
  "problem": "Options don't test understanding—they're all statements about regularization, not realistic competing choices"
}
```
**✅ FIX:**
```json
{
  "number": 12,
  "question_type": "multiple_choice",
  "question_text": "Your model has training R²=0.98 but test R²=0.62. Which is the BEST first action without collecting more data?",
  "options": [
    "A) Increase model complexity (add polynomial terms) to improve training fit",
    "B) Apply Ridge regularization and tune via cross-validation to reduce variance",
    "C) Simplify to a linear model to ensure underfitting doesn't occur",
    "D) Remove all features except the top 2 most correlated with target"
  ],
  "correct_answer": "B",
  "problem": "Now each option represents a realistic decision choice, and learner must discriminate based on understanding overfitting"
}
```

---

**❌ ANTI-PATTERN 4: Missing explanation**
```json
{
  "number": 15,
  "question_text": "Why does collecting more data reduce variance?",
  "correct_answer": "It gives better estimate of true pattern",
  "explanation": "Because more data is better."
  "problem": "Explanation is too short and doesn't explain WHY or connect to LO"
}
```
**✅ FIX:**
```json
{
  "number": 15,
  "question_text": "Why does collecting more data reduce variance?",
  "correct_answer": "More data provides a better estimate of the true underlying pattern and dilutes the effect of noise in any single sample. The model becomes less sensitive to fluctuations in the training set.",
  "explanation": "Variance measures how much a model's predictions change when trained on different samples. More data means more observations of the true pattern and less relative influence of noise and outliers. This causes the model to learn more stable, generalizable relationships. In the bias-variance decomposition, increasing data specifically reduces variance without forcing the model to be simpler (so bias need not increase). This is why data collection is often the best remedy for overfitting when possible.",
  "learning_objective": "Explain the bias-variance tradeoff and how it arises in ML models",
  "keywords": ["more data", "variance", "sampling", "noise", "stable", "generalization"]
}
```

---

## **17. Implementation Notes**

### **Course-Specific Content**

**DX603 Week 3 Example:**
- Learning Objectives: 4-5 focused on underfitting/overfitting/bias-variance tradeoff
- Expected sections: 4-5 (one per LO)
- Questions: 25-32 total
- Real-world context: Fraud detection, credit scoring, medical diagnosis

**DX604 Week 3 Example:**
- Learning Objectives: 3 (schemas, governance types, governance implementation)
- Expected sections: 3
- Questions: 25-30 total
- Real-world context: HIPAA, GDPR, financial compliance, ETL design

**DX699 (Varies by topic):**
- Learning Objectives: 3-5 per week
- Expected sections: 3-5
- Questions: 25-35 total
- Real-world context: Organizational readiness, governance, ethics, ROI

---

### **Usage with generic_quiz.py**

The quiz_questions.json files generated must be compatible with the provided `generic_quiz.py` script.

**Running the quiz:**
```bash
python3 generic_quiz.py week_02012026/DX604/quiz_questions.json
```

**The script will:**
1. Load metadata (title, description, total_questions)
2. Parse all questions matching the JSON schema above
3. Deliver interactive quiz with immediate feedback
4. Score by: 
   - Multiple choice: exact letter match
   - True/False: normalized matching
   - Fill-in: keyword matching from provided keywords array
   - Open-ended: keyword threshold evaluation (50%+ keywords matched = correct)
5. Display results with breakdown by section and difficulty level

---

You are not required to generate generic_quiz.py as it already exists in the project and you should only generate quiz_questions.json in the respective folder of read me file.