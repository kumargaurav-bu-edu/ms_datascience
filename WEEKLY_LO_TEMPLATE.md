# Weekly Learning Objectives - Template for AI Agents

## Purpose
This template shows the **recommended structure** for organizing learning objectives when generating quizzes using `generic_quiz.py`. You do NOT need to modify your actual weekly LO files from college. Instead, use this template as a **reference guide** when instructing agents to generate quiz_questions.json.

---

## How to Use This Template

**When asking an agent to generate a quiz, provide:**
1. The course code, week number, and topic (from your actual LO file)
2. Copy the **exact learning objectives** from your college-provided LO file
3. Optionally add real-world context examples that match this template structure
4. Reference this template in your prompt to show desired organization

**Example Agent Prompt:**
```
I want to generate a quiz for DX604 Week 3.

Course: DX604 O1: Data Management at Scale
Week: Week 3

Learning Objectives (from course materials):
- Define data schemas
- Compare various types of data governance
- Explore best practices for implementing data governance

Please generate 25-35 questions following the template at:
WEEKLY_LO_TEMPLATE.md

Focus on HIPAA compliance, GDPR, and ETL contexts.
```

---

## Template Format

```markdown
# COURSE_CODE - WEEK# Learning Objectives

## Metadata
- **Course**: Full Course Name (e.g., DX604 O1: Data Management at Scale)
- **Week**: Week # (e.g., Week 3)
- **Topic**: Brief topic descriptor
- **Date Range**: (Optional)

---

## Learning Objectives

### LO 1: [Exact LO text from your course materials]
**Context**: What this learning objective tests
**Key Topics**:
- Topic A
- Topic B
- Topic C

**Real-World Context**: Industry/business examples

---

### LO 2: [Exact LO text from your course materials]
**Context**: What this learning objective tests
**Key Topics**:
- Topic A
- Topic B
- Topic C

**Real-World Context**: Industry/business examples

---

## Summary
- **Total Learning Objectives**: #
- **Expected Quiz Questions**: 25-35
- **Distribution**: ~8-9 questions per LO
```

---

## Subject-Specific Examples

### Example 1: DX604 Week 3 Format

```markdown
# DX604 O1 - Week 3 Learning Objectives

## Metadata
- **Course**: DX604 O1: Data Management at Scale
- **Week**: Week 3
- **Topic**: Data Schemas, Data Governance, and Implementation

---

## Learning Objectives

### LO 1: Define data schemas
**Context**: Understanding the three schema types and their purposes
**Key Topics**:
- Conceptual, logical, and physical schemas
- Schema normalization
- Schema evolution

**Real-World Context**: Healthcare (HIPAA), E-commerce, Financial Services

---

### LO 2: Compare various types of data governance
**Context**: Contrasting governance frameworks and their tradeoffs
**Key Topics**:
- Centralized governance
- Decentralized governance
- Regulatory compliance role

**Real-World Context**: GDPR, HIPAA, SOX compliance, global organizations

---

### LO 3: Explore best practices for implementing data governance
**Context**: Organizational components, roles, processes for successful governance
**Key Topics**:
- Data governance council and roles
- Data governance policies and standards
- Data stewardship and quality management
- Technology and tools (Collibra, Atlas, etc.)

**Real-World Context**: Healthcare governance, Financial services governance, Multi-team organizations

---

## Summary
- **Total Learning Objectives**: 3
- **Expected Quiz Questions**: 25-35
- **Distribution**: ~8-12 questions per LO
```

---

### Example 2: DX603 Week 3 Format

```markdown
# DX603 O1 - Week 3 Learning Objectives

## Metadata
- **Course**: DX603 O1: Machine Learning Fundamentals
- **Week**: Week 3
- **Topic**: Underfitting, Overfitting, Generalization, and Bias-Variance Tradeoff

---

## Learning Objectives

### LO 1: Analyze the notions of underfitting and overfitting and the problems with each
**Context**: Core distinction between model complexity and performance
**Key Topics**:
- Definition of underfitting (too simple)
- Definition of overfitting (too complex)
- Training vs. test error patterns
- Problems caused by each

**Real-World Context**: Fraud detection (false negative costs), Credit scoring (approval bias), Medical diagnosis

---

### LO 2: Define the crucial concept of generalization
**Context**: The goal of machine learning—performing well on unseen data
**Key Topics**:
- Generalization definition
- Test/validation error vs. training error
- Why generalization matters
- Role in model selection

**Real-World Context**: Marketing response models, Customer churn prediction, Retention strategies

---

### LO 3: Explain the bias-variance tradeoff and how it arises in ML models
**Context**: Mathematical understanding of why models fail
**Key Topics**:
- Bias definition and high-bias models
- Variance definition and high-variance models
- Bias-variance decomposition of test MSE
- Irreducible error
- Complexity tradeoff

**Real-World Context**: Model selection in production, Cost-benefit analysis of model complexity

---

### LO 4: Discuss the importance of strategies for navigating the bias-variance tradeoff
**Context**: Practical techniques to improve model performance
**Key Topics**:
- Regularization (Ridge, Lasso)
- Validation set and cross-validation
- Collecting more data
- Feature selection and reduction
- Model complexity reduction

**Real-World Context**: Overfitting prevention in credit scoring, Data quality improvements, Cost vs. accuracy tradeoffs

---

## Summary
- **Total Learning Objectives**: 4
- **Expected Quiz Questions**: 25-35
- **Distribution**: ~6-9 questions per LO
```

---

### Example 3: DX699 Sample Format

```markdown
# DX699 O2 - Week X Learning Objectives

## Metadata
- **Course**: DX699 O2: AI for Leaders
- **Week**: Week X
- **Topic**: [Your course topic]

---

## Learning Objectives

### LO 1: [Exact LO from your course]
**Context**: What this tests
**Key Topics**:
- Topic A
- Topic B
- Topic C

**Real-World Context**: Business/organizational examples

---

## Summary
- **Total Learning Objectives**: #
- **Expected Quiz Questions**: 25-35
```

---

## Quick Copy-Paste Structure

When you get your college LOs, just fill in this minimal template:

```markdown
# [COURSE_CODE] - Week [#] Learning Objectives

## Learning Objectives

### LO 1: [Copy exact LO text from college]
### LO 2: [Copy exact LO text from college]
### LO 3: [Copy exact LO text from college]

## Summary
- **Total Learning Objectives**: [#]
- **Expected Quiz Questions**: 25-35
```

Then, when asking an agent to generate the quiz, you can reference:
- This template file
- Your actual weekly LO file
- The main instructions in `whatisexpected.md`

---

## Agent Instruction Example

When you want to generate a quiz, provide this to the agent:

```
Generate a quiz for DX604 Week 3.

Weekly LO file: week_02012026/DX604/week3_dx604_lo.md

Follow the template structure in: WEEKLY_LO_TEMPLATE.md (Example 1: DX604 Week 3 Format)

Use whatisexpected.md as the detailed quality standards.

Generate 25-35 questions covering:
1. Data Schemas (8-10 questions)
2. Data Governance Types (8-10 questions)
3. Data Governance Implementation (8-10 questions)

Real-world contexts: HIPAA, GDPR, ETL design, financial compliance
```

---

## Key Takeaway

✅ **Keep your original weekly LO files as-is** - They don't need modification
✅ **Use this template as a reference** - When structuring information for agents
✅ **Reference this file in agent prompts** - Link agents to this template + whatisexpected.md
✅ **Minimalist approach** - Add only course code, week, and exact LOs from college

The agent will use this template structure + your actual LOs + whatisexpected.md to generate high-quality quizzes.
