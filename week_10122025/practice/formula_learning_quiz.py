#!/usr/bin/env python3
# Run with: conda activate pyspark_local && python3 formula_learning_quiz.py
"""
Statistical Formulas Learning Quiz
Interactive quiz focused on teaching essential statistical formulas with detailed explanations

This quiz is designed to help you learn and memorize key statistical formulas
before attempting practice problems. Each question teaches a specific formula
with step-by-step explanations and examples.

Topics covered:
- Standard Deviation of Sums (Independent Variables)
- Central Limit Theorem
- Z-scores and Standardization
- Confidence Intervals
- Hypothesis Testing
- Probability Rules
- Expected Value and Variance
- Correlation and Covariance
- Sample Statistics
- Distribution Properties
"""

import random
from typing import List, Dict

class FormulaLearningQuiz:
    def __init__(self):
        self.questions = self._create_formula_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        
    def _create_formula_questions(self) -> List[Dict]:
        """Create formula learning questions with detailed explanations"""
        questions = [
            # Formula 1: Standard Deviation of Independent Sums
            {
                "formula_name": "Standard Deviation of Independent Random Variables",
                "formula": "σ_total = √(σ₁² + σ₂² + ... + σₙ²)",
                "question": "When combining two independent random variables X and Y, how do you calculate the standard deviation of their sum (X + Y)?",
                "options": [
                    "A) σ_total = σ_X + σ_Y", 
                    "B) σ_total = √(σ_X² + σ_Y²)", 
                    "C) σ_total = σ_X × σ_Y", 
                    "D) σ_total = (σ_X + σ_Y)/2"
                ],
                "correct": "B",
                "explanation": "For INDEPENDENT variables, variances add: Var(X+Y) = Var(X) + Var(Y). Since σ² = Var, we get σ_total = √(σ_X² + σ_Y²). This is the Pythagorean theorem for standard deviations!",
                "example": "Example: Dog growth 1-2 months (σ=0.5lb) + 2-4 months (σ=0.5lb) → σ_total = √(0.5² + 0.5²) = √0.5 ≈ 0.71lb",
                "key_insight": "Independence is crucial! If variables are correlated, you need to add the covariance term."
            },
            
            # Formula 2: Central Limit Theorem
            {
                "formula_name": "Central Limit Theorem - Standard Error",
                "formula": "σ_x̄ = σ/√n",
                "question": "According to the Central Limit Theorem, what is the standard deviation of the sample mean (standard error)?",
                "options": [
                    "A) σ_x̄ = σ × √n", 
                    "B) σ_x̄ = σ/√n", 
                    "C) σ_x̄ = σ/n", 
                    "D) σ_x̄ = σ × n"
                ],
                "correct": "B",
                "explanation": "The standard error (SE) of the sample mean decreases as sample size increases: SE = σ/√n. This shows why larger samples give more precise estimates.",
                "example": "Example: Population σ=10, sample size n=25 → SE = 10/√25 = 10/5 = 2",
                "key_insight": "As n increases, SE decreases, making sample means cluster closer to the population mean."
            },
            
            # Formula 3: Z-score
            {
                "formula_name": "Z-score (Standardization)",
                "formula": "z = (x - μ)/σ",
                "question": "To standardize a value and find how many standard deviations it is from the mean, which formula should you use?",
                "options": [
                    "A) z = (μ - x)/σ", 
                    "B) z = (x - μ)/σ", 
                    "C) z = σ/(x - μ)", 
                    "D) z = (x + μ)/σ"
                ],
                "correct": "B",
                "explanation": "Z-score measures how many standard deviations a value is from the mean: z = (x - μ)/σ. Positive z means above average, negative z means below average.",
                "example": "Example: x=85, μ=80, σ=5 → z = (85-80)/5 = 1 (one standard deviation above mean)",
                "key_insight": "Z-scores allow comparison across different scales and distributions."
            },
            
            # Formula 4: Confidence Interval for Mean
            {
                "formula_name": "Confidence Interval for Population Mean",
                "formula": "CI = x̄ ± z_(α/2) × (σ/√n)",
                "question": "When constructing a confidence interval for the population mean (σ known), what should you add and subtract from the sample mean?",
                "options": [
                    "A) z × σ", 
                    "B) z × (σ/√n)", 
                    "C) z × (σ/n)", 
                    "D) z × √n"
                ],
                "correct": "B",
                "explanation": "CI = x̄ ± z_(α/2) × SE, where SE = σ/√n. The z-value depends on confidence level (e.g., z=1.96 for 95% confidence).",
                "example": "Example: x̄=50, σ=10, n=25, 95% CI → 50 ± 1.96×(10/√25) = 50 ± 3.92 = [46.08, 53.92]",
                "key_insight": "Larger samples (bigger n) give narrower confidence intervals."
            },
            
            # Formula 5: Test Statistic for One-Sample Z-test
            {
                "formula_name": "One-Sample Z-test Statistic",
                "formula": "z = (x̄ - μ₀)/(σ/√n)",
                "question": "What is the test statistic for a one-sample z-test?",
                "options": [
                    "A) z = (x̄ - μ₀)/σ", 
                    "B) z = (x̄ - μ₀)/(σ/√n)", 
                    "C) z = (μ₀ - x̄)/(σ/√n)", 
                    "D) z = (x̄ - μ₀)/(σ/n)"
                ],
                "correct": "B",
                "explanation": "Test statistic compares sample mean to hypothesized mean, standardized by standard error: z = (x̄ - μ₀)/(σ/√n).",
                "example": "Example: Testing H₀: μ=100, x̄=105, σ=15, n=36 → z = (105-100)/(15/√36) = 5/2.5 = 2",
                "key_insight": "This measures how many standard errors the sample mean is from the hypothesized mean."
            },
            
            # Formula 6: Probability Addition Rule
            {
                "formula_name": "Addition Rule for Probability",
                "formula": "P(A ∪ B) = P(A) + P(B) - P(A ∩ B)",
                "question": "What is the addition rule for the probability of A OR B?",
                "options": [
                    "A) P(A ∪ B) = P(A) + P(B)", 
                    "B) P(A ∪ B) = P(A) + P(B) - P(A ∩ B)", 
                    "C) P(A ∪ B) = P(A) × P(B)", 
                    "D) P(A ∪ B) = P(A) - P(B)"
                ],
                "correct": "B",
                "explanation": "We subtract P(A ∩ B) to avoid double-counting the overlap. For mutually exclusive events, P(A ∩ B) = 0.",
                "example": "Example: P(A)=0.3, P(B)=0.4, P(A∩B)=0.1 → P(A∪B) = 0.3 + 0.4 - 0.1 = 0.6",
                "key_insight": "Always subtract the intersection to avoid counting it twice!"
            },
            
            # Formula 7: Conditional Probability
            {
                "formula_name": "Conditional Probability",
                "formula": "P(A|B) = P(A ∩ B)/P(B)",
                "question": "What is the formula for conditional probability P(A given B)?",
                "options": [
                    "A) P(A|B) = P(A) × P(B)", 
                    "B) P(A|B) = P(A ∩ B)/P(B)", 
                    "C) P(A|B) = P(A)/P(B)", 
                    "D) P(A|B) = P(B)/P(A)"
                ],
                "correct": "B",
                "explanation": "Conditional probability is the probability of A occurring given that B has occurred: P(A|B) = P(A ∩ B)/P(B).",
                "example": "Example: P(Rain and Cold) = 0.1, P(Cold) = 0.3 → P(Rain|Cold) = 0.1/0.3 = 1/3",
                "key_insight": "This restricts the sample space to only cases where B occurs."
            },
            
            # Formula 8: Expected Value of Linear Combination
            {
                "formula_name": "Expected Value of Linear Combination",
                "formula": "E[aX + bY] = aE[X] + bE[Y]",
                "question": "What is the expected value of a linear combination aX + bY?",
                "options": [
                    "A) E[aX + bY] = E[X] + E[Y]", 
                    "B) E[aX + bY] = aE[X] + bE[Y]", 
                    "C) E[aX + bY] = abE[X]E[Y]", 
                    "D) E[aX + bY] = a + b + E[X] + E[Y]"
                ],
                "correct": "B",
                "explanation": "Expected value is linear: E[aX + bY] = aE[X] + bE[Y]. This works regardless of whether X and Y are independent.",
                "example": "Example: E[X]=10, E[Y]=5 → E[2X + 3Y] = 2(10) + 3(5) = 20 + 15 = 35",
                "key_insight": "Linearity of expectation always holds, even for dependent variables!"
            },
            
            # Formula 9: Variance of Independent Sum
            {
                "formula_name": "Variance of Independent Variables",
                "formula": "Var(X + Y) = Var(X) + Var(Y) [if independent]",
                "question": "For independent random variables X and Y, what is Var(X + Y)?",
                "options": [
                    "A) Var(X + Y) = Var(X) + Var(Y)", 
                    "B) Var(X + Y) = Var(X) × Var(Y)", 
                    "C) Var(X + Y) = √(Var(X) + Var(Y))", 
                    "D) Var(X + Y) = |Var(X) - Var(Y)|"
                ],
                "correct": "A",
                "explanation": "For independent variables, variances add: Var(X + Y) = Var(X) + Var(Y). This is why standard deviations follow the Pythagorean theorem.",
                "example": "Example: Var(X)=4, Var(Y)=9 → Var(X+Y) = 4+9 = 13, so σ(X+Y) = √13 ≈ 3.6",
                "key_insight": "Independence is key! For dependent variables, you need to add 2×Cov(X,Y)."
            },
            
            # Formula 10: Sample Standard Deviation
            {
                "formula_name": "Sample Standard Deviation",
                "formula": "s = √[Σ(xᵢ - x̄)²/(n-1)]",
                "question": "What is the formula for sample standard deviation?",
                "options": [
                    "A) s = √[Σ(xᵢ - x̄)²/n]", 
                    "B) s = √[Σ(xᵢ - x̄)²/(n-1)]", 
                    "C) s = Σ(xᵢ - x̄)²/(n-1)", 
                    "D) s = √[Σ(xᵢ - μ)²/n]"
                ],
                "correct": "B",
                "explanation": "Sample standard deviation uses (n-1) in denominator (Bessel's correction) to get unbiased estimate: s = √[Σ(xᵢ - x̄)²/(n-1)].",
                "example": "Example: Data [2,4,6], x̄=4 → s = √[(2-4)² + (4-4)² + (6-4)²]/(3-1) = √[8/2] = 2",
                "key_insight": "We use (n-1) because we lose one degree of freedom when estimating the mean."
            },
            
            # Formula 11: Correlation Coefficient
            {
                "formula_name": "Pearson Correlation Coefficient",
                "formula": "r = Σ[(xᵢ-x̄)(yᵢ-ȳ)] / √[Σ(xᵢ-x̄)²Σ(yᵢ-ȳ)²]",
                "question": "The Pearson correlation coefficient measures:",
                "options": [
                    "A) Linear relationship strength and direction", 
                    "B) Causation between variables", 
                    "C) Difference in means", 
                    "D) Sum of squared errors"
                ],
                "correct": "A",
                "explanation": "Correlation r measures linear relationship strength (-1 ≤ r ≤ 1). r = ±1 means perfect linear relationship, r = 0 means no linear relationship.",
                "example": "Example: r = 0.8 means strong positive linear relationship; r = -0.3 means weak negative relationship",
                "key_insight": "Correlation ≠ Causation! High correlation doesn't imply one variable causes the other."
            },
            
            # Formula 12: Margin of Error
            {
                "formula_name": "Margin of Error",
                "formula": "ME = z_(α/2) × (σ/√n)",
                "question": "What is the margin of error for a confidence interval?",
                "options": [
                    "A) ME = z × σ", 
                    "B) ME = z × (σ/√n)", 
                    "C) ME = z × (σ/n)", 
                    "D) ME = z/√n"
                ],
                "correct": "B",
                "explanation": "Margin of error is half the width of confidence interval: ME = z_(α/2) × SE = z_(α/2) × (σ/√n).",
                "example": "Example: 95% CI, σ=10, n=100 → ME = 1.96 × (10/√100) = 1.96 × 1 = 1.96",
                "key_insight": "To halve the margin of error, you need 4 times the sample size!"
            },
            
            # Formula 13: Power of a Test
            {
                "formula_name": "Statistical Power",
                "formula": "Power = 1 - β = P(Reject H₀ | H₁ is true)",
                "question": "Statistical power is defined as:",
                "options": [
                    "A) Power = α", 
                    "B) Power = 1 - α", 
                    "C) Power = 1 - β", 
                    "D) Power = β"
                ],
                "correct": "C",
                "explanation": "Power = 1 - β, where β is Type II error probability. Power is the probability of correctly rejecting a false null hypothesis.",
                "example": "Example: If β = 0.2, then Power = 1 - 0.2 = 0.8 (80% power)",
                "key_insight": "Higher power means better ability to detect true effects. Increase power by increasing sample size or effect size."
            },
            
            # Formula 14: Bayes' Theorem
            {
                "formula_name": "Bayes' Theorem",
                "formula": "P(A|B) = P(B|A) × P(A) / P(B)",
                "question": "What is Bayes' theorem?",
                "options": [
                    "A) P(A|B) = P(A) × P(B)", 
                    "B) P(A|B) = P(B|A) × P(A) / P(B)", 
                    "C) P(A|B) = P(A) / P(B)", 
                    "D) P(A|B) = P(B|A) / P(A)"
                ],
                "correct": "B",
                "explanation": "Bayes' theorem updates probability based on new evidence: P(A|B) = P(B|A) × P(A) / P(B). It relates forward and reverse conditional probabilities.",
                "example": "Example: Medical test - P(Disease|Positive) = P(Positive|Disease) × P(Disease) / P(Positive)",
                "key_insight": "This is fundamental for updating beliefs with new information!"
            },
            
            # Formula 15: Chi-Square Test Statistic
            {
                "formula_name": "Chi-Square Test Statistic",
                "formula": "χ² = Σ[(Observed - Expected)²/Expected]",
                "question": "What is the chi-square test statistic formula?",
                "options": [
                    "A) χ² = Σ(Observed - Expected)", 
                    "B) χ² = Σ[(Observed - Expected)²/Expected]", 
                    "C) χ² = Σ(Observed/Expected)", 
                    "D) χ² = Σ[(Observed - Expected)/Expected]"
                ],
                "correct": "B",
                "explanation": "Chi-square measures how much observed frequencies deviate from expected: χ² = Σ[(O-E)²/E]. Larger values indicate greater deviation.",
                "example": "Example: Observed=15, Expected=10 → contribution = (15-10)²/10 = 25/10 = 2.5",
                "key_insight": "Used for goodness-of-fit tests and tests of independence."
            }
        ]
        
        return questions
    
    def display_formula_question(self, question_num: int, question_data: Dict) -> str:
        """Display a formula learning question WITHOUT showing the formula first"""
        print(f"\n{'='*80}")
        print(f"FORMULA {question_num + 1}: {question_data['formula_name']}")
        print(f"{'='*80}")
        print(f"❓ QUESTION: {question_data['question']}\n")
        
        for option in question_data['options']:
            print(f"   {option}")
        
        return input("\nYour answer (A, B, C, or D): ").upper().strip()
    
    def show_detailed_explanation(self, question_data: Dict, user_answer: str, is_correct: bool):
        """Show detailed explanation with formula, example, and insights"""
        print(f"\n{'='*80}")
        if is_correct:
            print("✅ CORRECT! Well done!")
        else:
            print(f"❌ INCORRECT. The correct answer is {question_data['correct']}")
        
        print(f"{'='*80}")
        print(f"📐 FORMULA: {question_data['formula']}")
        print(f"\n💡 EXPLANATION:")
        print(f"   {question_data['explanation']}")
        
        print(f"\n📝 EXAMPLE:")
        print(f"   {question_data['example']}")
        
        print(f"\n🔑 KEY INSIGHT:")
        print(f"   {question_data['key_insight']}")
        print(f"{'='*80}")
    
    def run_formula_quiz(self):
        """Run the formula learning quiz"""
        print("🎓 STATISTICAL FORMULAS LEARNING QUIZ")
        print("=" * 80)
        print("This quiz teaches essential statistical formulas with detailed explanations.")
        print("Take your time to understand each formula before moving to the next.")
        print("=" * 80)
        
        self.score = 0
        
        for i, question in enumerate(self.questions):
            user_answer = self.display_formula_question(i, question)
            
            # Validate input
            while user_answer not in ['A', 'B', 'C', 'D']:
                user_answer = input("Please enter A, B, C, or D: ").upper().strip()
            
            is_correct = user_answer == question['correct']
            if is_correct:
                self.score += 1
            
            self.show_detailed_explanation(question, user_answer, is_correct)
            
            # Pause between questions
            input("\n⏸️  Press Enter to continue to the next formula...")
        
        self.display_final_score()
    
    def display_final_score(self):
        """Display final quiz results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 80)
        print("🎯 FORMULA LEARNING COMPLETE!")
        print("=" * 80)
        print(f"Final Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🌟 Outstanding! You've mastered these statistical formulas!")
        elif percentage >= 80:
            print("🎉 Excellent! You have a strong grasp of the formulas.")
        elif percentage >= 70:
            print("👍 Good job! Review the formulas you missed.")
        elif percentage >= 60:
            print("📚 Fair progress. Consider reviewing the formulas again.")
        else:
            print("📖 Keep studying! These formulas are fundamental to statistics.")
        
        print("\n💡 TIP: Now that you've learned the formulas, try the practice quiz!")
    
    def formula_reference_sheet(self):
        """Display all formulas as a reference sheet"""
        print("📋 STATISTICAL FORMULAS REFERENCE SHEET")
        print("=" * 80)
        
        for i, question in enumerate(self.questions):
            print(f"\n{i+1}. {question['formula_name']}")
            print(f"   Formula: {question['formula']}")
            print(f"   Key Insight: {question['key_insight']}")
            print("-" * 60)
    
    def study_specific_formula(self):
        """Allow user to study a specific formula in detail"""
        print("\n📚 STUDY SPECIFIC FORMULA")
        print("=" * 40)
        
        for i, question in enumerate(self.questions):
            print(f"{i+1}. {question['formula_name']}")
        
        try:
            choice = int(input(f"\nChoose a formula to study (1-{len(self.questions)}): ")) - 1
            if 0 <= choice < len(self.questions):
                question = self.questions[choice]
                print(f"\n{'='*80}")
                print(f"📐 {question['formula_name']}")
                print(f"{'='*80}")
                print(f"Formula: {question['formula']}")
                print(f"\nExplanation: {question['explanation']}")
                print(f"\nExample: {question['example']}")
                print(f"\nKey Insight: {question['key_insight']}")
                print(f"{'='*80}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the formula learning application"""
    quiz = FormulaLearningQuiz()
    
    while True:
        print("\n" + "=" * 80)
        print("🎓 STATISTICAL FORMULAS LEARNING SYSTEM")
        print("=" * 80)
        print("Choose an option:")
        print("1. 📝 Take Formula Learning Quiz (Interactive)")
        print("2. 📋 View Formula Reference Sheet")
        print("3. 🔍 Study Specific Formula")
        print("4. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            quiz.run_formula_quiz()
        elif choice == '2':
            quiz.formula_reference_sheet()
        elif choice == '3':
            quiz.study_specific_formula()
        elif choice == '4':
            print("📚 Happy studying! Remember: Practice makes perfect!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
