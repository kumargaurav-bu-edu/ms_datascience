# Model Performance Evaluation Quiz

This quiz covers the learning objectives for Week 12, focusing on model performance evaluation techniques including ranking vs classification, profit curves, ROC curves, lift curves, and capstone proposal development.

## Files

- `model_performance_quiz.json` - The quiz questions in JSON format (30 questions)
- `interactive_quiz.py` - Interactive Python script to take the quiz
- `learning-objective.txt` - Original learning objectives for reference

## Learning Objectives Covered

1. **Compare ranking to classifying** (Questions 1-3)
2. **Explain profit curves** (Questions 4-7)
3. **Describe ROC curves (Receiver Operating Characteristic)** (Questions 8-14)
4. **Describe lift curves** (Questions 15-19)
5. **Reflect on the process of developing a Capstone Proposal** (Questions 26-27)
6. **Additional topics**: Confusion matrix relationships, threshold effects, real-world applications, trade-offs (Questions 20-25, 28-30)

## Question Distribution

- **Level 1 (Basic)**: 8 questions - Definitions and conceptual clarity
- **Level 2 (Intermediate)**: 15 questions - Formula application and curve interpretation
- **Level 3 (Advanced)**: 7 questions - Comparing models and advanced scenarios

## Topics Covered

- Ranking vs Classification
- Profit Curves
- ROC Curves
- Lift Curves
- Confusion Matrix Relationships (TPR, FPR, Precision, Recall)
- AUC (Area Under the ROC Curve)
- Threshold Effects
- Real-World Applications (Credit Scoring, Fraud Detection, Marketing, Customer Churn)
- Capstone Proposal Development
- Trade-offs and Error Analysis

## How to Use

### Option 1: Interactive Quiz (Recommended)

Run the interactive Python script:

```bash
python interactive_quiz.py
```

Features:
- Shuffle questions option
- Filter by difficulty level
- Immediate feedback with explanations
- Performance tracking by topic and difficulty
- Results saved to `quiz_results.json`

### Option 2: Review Questions Directly

Open `model_performance_quiz.json` in any text editor or JSON viewer to review all questions, answers, and explanations.

## Quiz Structure

Each question includes:
- **ID**: Unique question identifier
- **Difficulty**: Level 1 (Basic), Level 2 (Intermediate), or Level 3 (Advanced)
- **Topic**: Subject area
- **Question**: The question text
- **Options**: Four multiple-choice options (A, B, C, D)
- **Correct**: The correct answer letter
- **Explanation**: Detailed explanation of why the answer is correct

## Real-World Context

Questions are designed with practical scenarios including:
- Fraud detection systems
- Credit scoring models
- Customer churn prediction
- Marketing response models
- Medical diagnosis

## Key Concepts Tested

### Formulas
- TPR (True Positive Rate) = TP / (TP + FN)
- FPR (False Positive Rate) = FP / (FP + TN)
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- Lift = (Response rate with model) / (Baseline response rate)
- Profit = (Conversions × Revenue) - (Contacts × Cost)

### Curve Interpretations
- **ROC Curve**: TPR vs FPR trade-off, AUC interpretation
- **Profit Curve**: Cumulative profit vs instances acted upon
- **Lift Curve**: Model performance vs random baseline

## Notes

- All questions are multiple-choice with 4 options
- Questions include detailed explanations for learning
- Real-world scenarios help connect theory to practice
- Formula application questions test computational understanding
- Scenario-based questions test critical thinking

## Expected Learning Outcomes

After completing this quiz, you should be able to:
- Distinguish between ranking and classification approaches
- Interpret and compare ROC, profit, and lift curves
- Calculate and interpret TPR, FPR, precision, recall, and lift
- Understand AUC and its limitations
- Select appropriate evaluation metrics for business problems
- Apply model evaluation concepts to real-world scenarios
- Reflect on capstone proposal development considerations
