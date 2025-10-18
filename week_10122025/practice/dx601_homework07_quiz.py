#!/usr/bin/env python3
"""
DX 601 Homework 07 Concepts Quiz
25 Multiple Choice Questions covering key statistical and probability concepts

Topics covered:
- Probability and Expected Values
- Central Limit Theorem
- Sums of Random Variables
- Sample Distributions and CDF
- Z-scores and Normal Distributions
- P-values and Hypothesis Testing
- Independence Testing
- Conditional Probability
- Limits and Mathematical Functions
- Probability Density Functions
- Distribution Identification
- Multiple Testing Correction
- Monte Carlo Simulation
- Pi Estimation
- T-tests
- ROC Curves
- Residual Analysis
"""

import random
import math
import numpy as np
import scipy.stats
from typing import List, Dict, Tuple

class StatisticsQuiz:
    def __init__(self):
        self.questions = self._create_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        
    def _create_questions(self) -> List[Dict]:
        """Create all 25 quiz questions"""
        questions = [
            # Question 1: Probability and Expected Values
            {
                "question": "You have a slot machine with 50% win probability. After winning 10 times in a row, what is the expected win percentage if you play 90 more times (total 100 plays)?",
                "options": ["A) 40%", "B) 50%", "C) 60%", "D) 55%"],
                "correct": "B",
                "explanation": "Each play is independent. The expected win rate remains 50% regardless of previous outcomes."
            },
            
            # Question 2: Central Limit Theorem
            {
                "question": "If ant territory radius grows 1cm/day with σ=0.5cm, what's the standard deviation of growth over 90 days using CLT?",
                "options": ["A) 0.5cm", "B) 4.74cm", "C) 45cm", "D) 90cm"],
                "correct": "B",
                "explanation": "For independent variables, σ_total = σ_individual × √n = 0.5 × √90 ≈ 4.74cm"
            },
            
            # Question 3: Sums of Independent Random Variables
            {
                "question": "Dog growth: 1-2 months (μ=1lb, σ=0.5lb) + 2-4 months (μ=1.5lb, σ=0.5lb). What's the standard deviation for 1-4 months if independent?",
                "options": ["A) 0.5lb", "B) 0.71lb", "C) 1.0lb", "D) 2.5lb"],
                "correct": "B",
                "explanation": "For independent variables: σ_total = √(σ₁² + σ₂²) = √(0.5² + 0.5²) = √0.5 ≈ 0.71lb"
            },
            
            # Question 4: Correlation and Covariance
            {
                "question": "If the actual standard deviation for dog growth (1-4 months) is 0.75lb instead of 0.71lb, what does this indicate?",
                "options": ["A) Negative correlation", "B) Positive correlation", "C) Independence", "D) Measurement error"],
                "correct": "B",
                "explanation": "Higher than expected variance indicates positive correlation between the two growth periods."
            },
            
            # Question 5: Empirical CDF
            {
                "question": "What does the empirical CDF represent?",
                "options": ["A) Theoretical probability", "B) Sample mean", "C) Proportion of data ≤ x", "D) Sample variance"],
                "correct": "C",
                "explanation": "The empirical CDF gives the proportion of sample data points that are less than or equal to a given value."
            },
            
            # Question 6: Z-scores
            {
                "question": "For a normal distribution with μ=5.4 and σ=1.6, what's the z-score for x=3.5?",
                "options": ["A) -1.19", "B) 1.19", "C) -0.84", "D) 0.84"],
                "correct": "A",
                "explanation": "z = (x - μ)/σ = (3.5 - 5.4)/1.6 = -1.9/1.6 = -1.19"
            },
            
            # Question 7: P-values
            {
                "question": "What does a p-value represent in hypothesis testing?",
                "options": ["A) Probability the null hypothesis is true", "B) Probability of observing data this extreme or more extreme given H₀", "C) Probability of Type I error", "D) Effect size"],
                "correct": "B",
                "explanation": "P-value is the probability of observing the data (or more extreme) assuming the null hypothesis is true."
            },
            
            # Question 8: Independence Testing
            {
                "question": "How can you test if two variables are independent?",
                "options": ["A) Calculate correlation coefficient", "B) Compare means", "C) Chi-square test", "D) Both A and C"],
                "correct": "D",
                "explanation": "Both correlation analysis and chi-square tests can be used to assess independence between variables."
            },
            
            # Question 9: Conditional Probability
            {
                "question": "P(A|B) represents:",
                "options": ["A) P(A) × P(B)", "B) P(A and B) / P(B)", "C) P(A) + P(B)", "D) P(A) - P(B)"],
                "correct": "B",
                "explanation": "Conditional probability P(A|B) = P(A and B) / P(B), the probability of A given B has occurred."
            },
            
            # Question 10: Limits
            {
                "question": "What is lim(x→3) [(x+3)(x-3)]/(x-3)?",
                "options": ["A) 0", "B) 3", "C) 6", "D) Undefined"],
                "correct": "C",
                "explanation": "Simplify to (x+3) after canceling (x-3), then substitute x=3 to get 6."
            },
            
            # Question 11: Gaussian Distribution
            {
                "question": "In the PDF f(x) = (1/(3√(2π))) × exp(-0.5×((x-4)/3)²), what is the standard deviation?",
                "options": ["A) 1", "B) 3", "C) 4", "D) 9"],
                "correct": "B",
                "explanation": "Comparing with standard form, the denominator shows σ=3 in the coefficient and exponent."
            },
            
            # Question 12: Distribution Identification
            {
                "question": "A histogram shows roughly equal frequency across all bins. This suggests:",
                "options": ["A) Normal distribution", "B) Uniform distribution", "C) Exponential distribution", "D) Poisson distribution"],
                "correct": "B",
                "explanation": "Equal frequencies across bins indicates a uniform distribution where all values are equally likely."
            },
            
            # Question 13: Multiple Testing Correction
            {
                "question": "With 100 tests and desired overall false positive rate ≤ 0.5, what's the maximum α per test (Bonferroni)?",
                "options": ["A) 0.05", "B) 0.01", "C) 0.005", "D) 0.0005"],
                "correct": "C",
                "explanation": "Bonferroni correction: α_individual = α_overall / n_tests = 0.5 / 100 = 0.005"
            },
            
            # Question 14: Monte Carlo Simulation
            {
                "question": "Monte Carlo simulation is used to:",
                "options": ["A) Calculate exact probabilities", "B) Estimate probabilities through random sampling", "C) Prove mathematical theorems", "D) Solve differential equations"],
                "correct": "B",
                "explanation": "Monte Carlo uses random sampling to estimate probabilities and solve complex problems numerically."
            },
            
            # Question 15: Pi Estimation
            {
                "question": "In the unit circle method for estimating π, why do we multiply by 4?",
                "options": ["A) Circle has 4 quadrants", "B) Ratio of circle area to square area is π/4", "C) Mathematical convention", "D) Improves accuracy"],
                "correct": "B",
                "explanation": "Circle area = π×1² = π, Square area = 2×2 = 4, so ratio = π/4. Multiply by 4 to get π."
            },
            
            # Question 16: T-test Assumptions
            {
                "question": "Student's t-test assumes:",
                "options": ["A) Large sample size", "B) Known population variance", "C) Normal distribution", "D) Equal variances"],
                "correct": "C",
                "explanation": "T-test assumes the data comes from a normal distribution, especially important for small samples."
            },
            
            # Question 17: ROC Curves
            {
                "question": "In an ROC curve, what indicates a perfect classifier?",
                "options": ["A) Diagonal line", "B) Curve below diagonal", "C) Curve through (0,1)", "D) Horizontal line"],
                "correct": "C",
                "explanation": "Perfect classifier goes from (0,0) to (0,1) to (1,1), achieving 100% TPR with 0% FPR."
            },
            
            # Question 18: Type I and Type II Errors
            {
                "question": "Type I error occurs when:",
                "options": ["A) Rejecting true null hypothesis", "B) Accepting false null hypothesis", "C) Sample size is too small", "D) Variance is unknown"],
                "correct": "A",
                "explanation": "Type I error (α) is rejecting the null hypothesis when it's actually true (false positive)."
            },
            
            # Question 19: Statistical Power
            {
                "question": "Statistical power is:",
                "options": ["A) 1 - α", "B) 1 - β", "C) α + β", "D) α × β"],
                "correct": "B",
                "explanation": "Power = 1 - β, where β is the probability of Type II error. Power is the probability of correctly rejecting a false null hypothesis."
            },
            
            # Question 20: Confidence Intervals
            {
                "question": "A 95% confidence interval means:",
                "options": ["A) 95% chance the parameter is in the interval", "B) 95% of intervals will contain the true parameter", "C) 5% chance of error", "D) Both B and C"],
                "correct": "D",
                "explanation": "95% of such intervals will contain the true parameter, and there's a 5% chance this specific interval doesn't."
            },
            
            # Question 21: Sampling Distribution
            {
                "question": "The sampling distribution of the mean has variance:",
                "options": ["A) σ²", "B) σ²/n", "C) σ/√n", "D) σ√n"],
                "correct": "B",
                "explanation": "Variance of sample mean = σ²/n, where σ² is population variance and n is sample size."
            },
            
            # Question 22: Hypothesis Testing Steps
            {
                "question": "The correct order of hypothesis testing steps is:",
                "options": ["A) State hypotheses, collect data, calculate test statistic, make decision", "B) Collect data, state hypotheses, calculate p-value, make decision", "C) Calculate test statistic, state hypotheses, collect data, make decision", "D) Make decision, state hypotheses, collect data, calculate test statistic"],
                "correct": "A",
                "explanation": "Proper order: 1) State H₀ and H₁, 2) Collect data, 3) Calculate test statistic, 4) Compare to critical value or calculate p-value, 5) Make decision."
            },
            
            # Question 23: Residual Analysis
            {
                "question": "Positive residuals in a model indicate:",
                "options": ["A) Model overestimates", "B) Model underestimates", "C) Perfect fit", "D) Random error"],
                "correct": "B",
                "explanation": "Positive residual = observed - predicted > 0, meaning observed > predicted, so model underestimates."
            },
            
            # Question 24: Central Limit Theorem Conditions
            {
                "question": "The Central Limit Theorem requires:",
                "options": ["A) Normal population", "B) Large sample size", "C) Known variance", "D) Independent samples"],
                "correct": "D",
                "explanation": "CLT requires independent samples. With sufficient sample size, it works regardless of population distribution."
            },
            
            # Question 25: Effect Size
            {
                "question": "Cohen's d measures:",
                "options": ["A) Statistical significance", "B) Effect size", "C) Sample size needed", "D) Confidence level"],
                "correct": "B",
                "explanation": "Cohen's d is a measure of effect size, indicating the magnitude of difference between groups in standard deviation units."
            }
        ]
        
        return questions
    
    def shuffle_questions(self):
        """Shuffle the order of questions"""
        random.shuffle(self.questions)
    
    def display_question(self, question_num: int, question_data: Dict) -> str:
        """Display a single question with options"""
        print(f"\n--- Question {question_num + 1} ---")
        print(f"{question_data['question']}\n")
        
        for option in question_data['options']:
            print(option)
        
        return input("\nYour answer (A, B, C, or D): ").upper().strip()
    
    def check_answer(self, user_answer: str, correct_answer: str, explanation: str) -> bool:
        """Check if the answer is correct and provide feedback"""
        if user_answer == correct_answer:
            print("✓ Correct!")
            print(f"Explanation: {explanation}")
            return True
        else:
            print(f"✗ Incorrect. The correct answer is {correct_answer}")
            print(f"Explanation: {explanation}")
            return False
    
    def run_quiz(self, shuffle: bool = True):
        """Run the complete quiz"""
        print("=" * 60)
        print("DX 601 Homework 07 Concepts Quiz")
        print("25 Questions on Statistical and Probability Concepts")
        print("=" * 60)
        
        if shuffle:
            self.shuffle_questions()
        
        self.score = 0
        
        for i, question in enumerate(self.questions):
            user_answer = self.display_question(i, question)
            
            # Validate input
            while user_answer not in ['A', 'B', 'C', 'D']:
                user_answer = input("Please enter A, B, C, or D: ").upper().strip()
            
            if self.check_answer(user_answer, question['correct'], question['explanation']):
                self.score += 1
            
            # Pause between questions
            input("\nPress Enter to continue...")
        
        self.display_final_score()
    
    def display_final_score(self):
        """Display final quiz results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 60)
        print("QUIZ COMPLETE!")
        print("=" * 60)
        print(f"Final Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🌟 Excellent! You have a strong understanding of the concepts!")
        elif percentage >= 80:
            print("👍 Great job! You understand most of the key concepts.")
        elif percentage >= 70:
            print("👌 Good work! Review the areas you missed.")
        elif percentage >= 60:
            print("📚 Fair performance. Consider reviewing the homework material.")
        else:
            print("📖 Keep studying! Review the homework and course materials.")
    
    def run_practice_mode(self):
        """Run quiz in practice mode - show answers immediately"""
        print("=" * 60)
        print("PRACTICE MODE - Immediate feedback after each question")
        print("=" * 60)
        
        for i, question in enumerate(self.questions):
            user_answer = self.display_question(i, question)
            
            while user_answer not in ['A', 'B', 'C', 'D']:
                user_answer = input("Please enter A, B, C, or D: ").upper().strip()
            
            if self.check_answer(user_answer, question['correct'], question['explanation']):
                self.score += 1
            
            input("\nPress Enter for next question...")
        
        self.display_final_score()
    
    def study_mode(self):
        """Display all questions and answers for study purposes"""
        print("=" * 60)
        print("STUDY MODE - All Questions and Answers")
        print("=" * 60)
        
        for i, question in enumerate(self.questions):
            print(f"\n--- Question {i + 1} ---")
            print(f"{question['question']}\n")
            
            for option in question['options']:
                if option.startswith(question['correct']):
                    print(f"{option} ← CORRECT")
                else:
                    print(option)
            
            print(f"\nExplanation: {question['explanation']}")
            print("-" * 40)


def main():
    """Main function to run the quiz application"""
    quiz = StatisticsQuiz()
    
    while True:
        print("\n" + "=" * 60)
        print("DX 601 Homework 07 Concepts Quiz")
        print("=" * 60)
        print("Choose a mode:")
        print("1. Full Quiz (25 questions)")
        print("2. Practice Mode (immediate feedback)")
        print("3. Study Mode (view all answers)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            quiz.run_quiz()
        elif choice == '2':
            quiz.run_practice_mode()
        elif choice == '3':
            quiz.study_mode()
        elif choice == '4':
            print("Thanks for using the quiz! Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
