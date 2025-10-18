#!/usr/bin/env python3
# Run with: conda activate pyspark_local && python3 practice_problems_quiz.py
"""
Statistical Practice Problems Quiz
25 Multiple Choice Questions for applying statistical formulas and concepts

This quiz assumes you've learned the formulas and focuses on problem-solving.
Questions are similar in style to homework problems and require formula application.

Topics covered:
- Standard Deviation Calculations
- Central Limit Theorem Applications
- Hypothesis Testing
- Confidence Intervals
- Probability Calculations
- Distribution Properties
- Correlation and Independence
- Sample Statistics
- Z-scores and Standardization
- Statistical Inference
"""

import random
from typing import List, Dict

class PracticeProblemsQuiz:
    def __init__(self):
        self.questions = self._create_practice_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        
    def _create_practice_questions(self) -> List[Dict]:
        """Create practice problems similar to homework questions"""
        questions = [
            # Question 1: Standard Deviation of Independent Sums (like your example)
            {
                "question": "Dog growth: 1-2 months (μ=1lb, σ=0.5lb) + 2-4 months (μ=1.5lb, σ=0.5lb). What's the standard deviation for 1-4 months if independent?",
                "options": ["A) 0.5lb", "B) 0.71lb", "C) 1.0lb", "D) 2.5lb"],
                "correct": "B",
                "explanation": "For independent variables: σ_total = √(σ₁² + σ₂²) = √(0.5² + 0.5²) = √0.5 ≈ 0.71lb",
                "formula_used": "σ_total = √(σ₁² + σ₂²) for independent variables"
            },
            
            # Question 2: Similar problem with different values
            {
                "question": "Plant height: Week 1-2 (μ=3cm, σ=0.8cm) + Week 3-4 (μ=2.5cm, σ=1.2cm). What's the standard deviation for total growth (Week 1-4) if independent?",
                "options": ["A) 1.44cm", "B) 2.0cm", "C) 1.0cm", "D) 0.4cm"],
                "correct": "A",
                "explanation": "σ_total = √(0.8² + 1.2²) = √(0.64 + 1.44) = √2.08 ≈ 1.44cm",
                "formula_used": "σ_total = √(σ₁² + σ₂²)"
            },
            
            # Question 3: Central Limit Theorem
            {
                "question": "A population has μ=50 and σ=12. For samples of size n=36, what is the standard error of the sample mean?",
                "options": ["A) 12", "B) 6", "C) 2", "D) 1.33"],
                "correct": "C",
                "explanation": "Standard error = σ/√n = 12/√36 = 12/6 = 2",
                "formula_used": "SE = σ/√n"
            },
            
            # Question 4: Z-score calculation
            {
                "question": "For a normal distribution with μ=75 and σ=8, what is the z-score for x=83?",
                "options": ["A) 1.0", "B) -1.0", "C) 0.5", "D) 8.0"],
                "correct": "A",
                "explanation": "z = (x - μ)/σ = (83 - 75)/8 = 8/8 = 1.0",
                "formula_used": "z = (x - μ)/σ"
            },
            
            # Question 5: Confidence Interval
            {
                "question": "A sample of 25 has x̄=100 and σ=15. What is the 95% confidence interval for μ? (z₀.₀₂₅ = 1.96)",
                "options": ["A) [94.12, 105.88]", "B) [91.2, 108.8]", "C) [85, 115]", "D) [97, 103]"],
                "correct": "A",
                "explanation": "CI = 100 ± 1.96×(15/√25) = 100 ± 1.96×3 = 100 ± 5.88 = [94.12, 105.88]",
                "formula_used": "CI = x̄ ± z_(α/2) × (σ/√n)"
            },
            
            # Question 6: Probability Addition Rule
            {
                "question": "P(A) = 0.4, P(B) = 0.3, P(A ∩ B) = 0.1. What is P(A ∪ B)?",
                "options": ["A) 0.7", "B) 0.6", "C) 0.12", "D) 0.5"],
                "correct": "B",
                "explanation": "P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0.4 + 0.3 - 0.1 = 0.6",
                "formula_used": "P(A ∪ B) = P(A) + P(B) - P(A ∩ B)"
            },
            
            # Question 7: Conditional Probability
            {
                "question": "P(Rain and Cold) = 0.15, P(Cold) = 0.4. What is P(Rain|Cold)?",
                "options": ["A) 0.375", "B) 0.06", "C) 0.55", "D) 0.25"],
                "correct": "A",
                "explanation": "P(Rain|Cold) = P(Rain ∩ Cold)/P(Cold) = 0.15/0.4 = 0.375",
                "formula_used": "P(A|B) = P(A ∩ B)/P(B)"
            },
            
            # Question 8: Expected Value
            {
                "question": "E[X] = 20, E[Y] = 15. What is E[3X + 2Y]?",
                "options": ["A) 35", "B) 90", "C) 105", "D) 70"],
                "correct": "B",
                "explanation": "E[3X + 2Y] = 3E[X] + 2E[Y] = 3(20) + 2(15) = 60 + 30 = 90",
                "formula_used": "E[aX + bY] = aE[X] + bE[Y]"
            },
            
            # Question 9: Variance of Independent Sum
            {
                "question": "Var(X) = 16, Var(Y) = 9. If X and Y are independent, what is Var(X + Y)?",
                "options": ["A) 25", "B) 7", "C) 144", "D) 5"],
                "correct": "A",
                "explanation": "For independent variables: Var(X + Y) = Var(X) + Var(Y) = 16 + 9 = 25",
                "formula_used": "Var(X + Y) = Var(X) + Var(Y) for independent X, Y"
            },
            
            # Question 10: Hypothesis Testing
            {
                "question": "Testing H₀: μ = 50 vs H₁: μ ≠ 50. Sample: n=64, x̄=52, σ=8. What is the test statistic?",
                "options": ["A) 2.0", "B) 1.0", "C) 0.25", "D) 16"],
                "correct": "A",
                "explanation": "z = (x̄ - μ₀)/(σ/√n) = (52 - 50)/(8/√64) = 2/1 = 2.0",
                "formula_used": "z = (x̄ - μ₀)/(σ/√n)"
            },
            
            # Question 11: Sample Size for Margin of Error
            {
                "question": "To achieve margin of error = 2 with 95% confidence and σ = 10, what sample size is needed?",
                "options": ["A) 25", "B) 49", "C) 96", "D) 100"],
                "correct": "C",
                "explanation": "ME = z×(σ/√n), so 2 = 1.96×(10/√n). Solving: √n = 19.6/2 = 9.8, so n ≈ 96",
                "formula_used": "n = (z×σ/ME)²"
            },
            
            # Question 12: Three Independent Variables
            {
                "question": "Three independent measurements: σ₁=2, σ₂=3, σ₃=4. What's the standard deviation of their sum?",
                "options": ["A) 9", "B) 5.39", "C) 3", "D) 29"],
                "correct": "B",
                "explanation": "σ_total = √(2² + 3² + 4²) = √(4 + 9 + 16) = √29 ≈ 5.39",
                "formula_used": "σ_total = √(σ₁² + σ₂² + σ₃²)"
            },
            
            # Question 13: Normal Distribution Probability
            {
                "question": "X ~ N(100, 15²). What is P(X > 115)? (Use z-table: P(Z > 1) ≈ 0.16)",
                "options": ["A) 0.16", "B) 0.84", "C) 0.5", "D) 0.32"],
                "correct": "A",
                "explanation": "z = (115-100)/15 = 1. P(X > 115) = P(Z > 1) ≈ 0.16",
                "formula_used": "z = (x - μ)/σ, then use standard normal table"
            },
            
            # Question 14: Type I Error
            {
                "question": "If α = 0.05 and we perform 20 independent tests, what's the expected number of Type I errors?",
                "options": ["A) 0.05", "B) 1", "C) 0.25", "D) 4"],
                "correct": "B",
                "explanation": "Expected Type I errors = n × α = 20 × 0.05 = 1",
                "formula_used": "E[Type I errors] = n × α"
            },
            
            # Question 15: Correlation and Standard Deviation
            {
                "question": "If the actual σ for combined growth is 0.9lb instead of expected 0.71lb (from Q1), what does this suggest?",
                "options": ["A) Negative correlation", "B) Positive correlation", "C) Independence", "D) Measurement error"],
                "correct": "B",
                "explanation": "Higher than expected variance (0.9² > 0.71²) indicates positive correlation between growth periods",
                "formula_used": "If σ_actual > σ_independent, then positive correlation exists"
            },
            
            # Question 16: Binomial to Normal Approximation
            {
                "question": "Binomial distribution with n=100, p=0.3. Using normal approximation, what are μ and σ?",
                "options": ["A) μ=30, σ=4.58", "B) μ=70, σ=4.58", "C) μ=30, σ=21", "D) μ=15, σ=3.87"],
                "correct": "A",
                "explanation": "μ = np = 100×0.3 = 30, σ = √(np(1-p)) = √(100×0.3×0.7) = √21 ≈ 4.58",
                "formula_used": "μ = np, σ = √(np(1-p))"
            },
            
            # Question 17: Chi-Square Test
            {
                "question": "Observed: 15, Expected: 10. What is this cell's contribution to χ²?",
                "options": ["A) 5", "B) 2.5", "C) 1.5", "D) 25"],
                "correct": "B",
                "explanation": "χ² contribution = (Observed - Expected)²/Expected = (15-10)²/10 = 25/10 = 2.5",
                "formula_used": "χ² = Σ[(O-E)²/E]"
            },
            
            # Question 18: Power Calculation
            {
                "question": "If β = 0.2 (Type II error rate), what is the statistical power?",
                "options": ["A) 0.2", "B) 0.8", "C) 1.2", "D) 0.04"],
                "correct": "B",
                "explanation": "Power = 1 - β = 1 - 0.2 = 0.8",
                "formula_used": "Power = 1 - β"
            },
            
            # Question 19: Sampling Distribution
            {
                "question": "Population: μ=40, σ=20. For n=25, what's the probability that x̄ > 44? (P(Z > 1) ≈ 0.16)",
                "options": ["A) 0.16", "B) 0.84", "C) 0.5", "D) 0.32"],
                "correct": "A",
                "explanation": "SE = 20/√25 = 4, z = (44-40)/4 = 1, P(x̄ > 44) = P(Z > 1) ≈ 0.16",
                "formula_used": "z = (x̄ - μ)/(σ/√n)"
            },
            
            # Question 20: Multiple Testing Correction
            {
                "question": "Bonferroni correction: 10 tests, desired overall α = 0.05. What should each test's α be?",
                "options": ["A) 0.05", "B) 0.005", "C) 0.5", "D) 0.0005"],
                "correct": "B",
                "explanation": "α_individual = α_overall/n = 0.05/10 = 0.005",
                "formula_used": "α_individual = α_overall/n_tests"
            },
            
            # Question 21: Confidence Level vs Alpha
            {
                "question": "For a 99% confidence interval, what is the value of α?",
                "options": ["A) 0.99", "B) 0.01", "C) 0.005", "D) 2.58"],
                "correct": "B",
                "explanation": "α = 1 - confidence level = 1 - 0.99 = 0.01",
                "formula_used": "α = 1 - confidence level"
            },
            
            # Question 22: Standard Error vs Standard Deviation
            {
                "question": "Sample of 16 from population with σ=12. What's the standard error of the mean?",
                "options": ["A) 12", "B) 4", "C) 3", "D) 0.75"],
                "correct": "C",
                "explanation": "SE = σ/√n = 12/√16 = 12/4 = 3",
                "formula_used": "SE = σ/√n"
            },
            
            # Question 23: Degrees of Freedom
            {
                "question": "Sample size n=15. For a t-test, how many degrees of freedom?",
                "options": ["A) 15", "B) 14", "C) 16", "D) 13"],
                "correct": "B",
                "explanation": "df = n - 1 = 15 - 1 = 14",
                "formula_used": "df = n - 1 for one-sample t-test"
            },
            
            # Question 24: Effect Size
            {
                "question": "Two groups: Group 1 (μ₁=80, σ=10), Group 2 (μ₂=75, σ=10). What's Cohen's d?",
                "options": ["A) 0.5", "B) 5", "C) 0.05", "D) 1.0"],
                "correct": "A",
                "explanation": "Cohen's d = |μ₁ - μ₂|/σ = |80 - 75|/10 = 5/10 = 0.5",
                "formula_used": "Cohen's d = |μ₁ - μ₂|/σ_pooled"
            },
            
            # Question 25: Probability Complement
            {
                "question": "If P(A) = 0.3, what is P(not A)?",
                "options": ["A) 0.3", "B) 0.7", "C) 1.3", "D) -0.3"],
                "correct": "B",
                "explanation": "P(not A) = 1 - P(A) = 1 - 0.3 = 0.7",
                "formula_used": "P(A^c) = 1 - P(A)"
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
    
    def check_answer(self, user_answer: str, correct_answer: str, explanation: str, formula_used: str) -> bool:
        """Check if the answer is correct and provide feedback"""
        if user_answer == correct_answer:
            print("✓ Correct!")
            print(f"📐 Formula: {formula_used}")
            print(f"💡 Explanation: {explanation}")
            return True
        else:
            print(f"✗ Incorrect. The correct answer is {correct_answer}")
            print(f"📐 Formula: {formula_used}")
            print(f"💡 Explanation: {explanation}")
            return False
    
    def run_quiz(self, shuffle: bool = True):
        """Run the complete practice quiz"""
        print("=" * 70)
        print("📊 STATISTICAL PRACTICE PROBLEMS QUIZ")
        print("25 Questions - Apply Your Formula Knowledge!")
        print("=" * 70)
        
        if shuffle:
            self.shuffle_questions()
        
        self.score = 0
        
        for i, question in enumerate(self.questions):
            user_answer = self.display_question(i, question)
            
            # Validate input
            while user_answer not in ['A', 'B', 'C', 'D']:
                user_answer = input("Please enter A, B, C, or D: ").upper().strip()
            
            if self.check_answer(user_answer, question['correct'], 
                               question['explanation'], question['formula_used']):
                self.score += 1
            
            # Pause between questions
            input("\nPress Enter to continue...")
        
        self.display_final_score()
    
    def display_final_score(self):
        """Display final quiz results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("\n" + "=" * 70)
        print("🎯 PRACTICE QUIZ COMPLETE!")
        print("=" * 70)
        print(f"Final Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🌟 Outstanding! You've mastered statistical problem-solving!")
        elif percentage >= 80:
            print("🎉 Excellent! You're ready for the homework!")
        elif percentage >= 70:
            print("👍 Good work! Review the problems you missed.")
        elif percentage >= 60:
            print("📚 Fair performance. Practice more problems.")
        else:
            print("📖 Keep practicing! Review the formulas and try again.")
        
        print(f"\n💡 TIP: If you missed questions, review the formulas in the Formula Learning Quiz!")
    
    def run_practice_mode(self):
        """Run quiz in practice mode - show answers immediately"""
        print("=" * 70)
        print("🔄 PRACTICE MODE - Immediate feedback after each question")
        print("=" * 70)
        
        for i, question in enumerate(self.questions):
            user_answer = self.display_question(i, question)
            
            while user_answer not in ['A', 'B', 'C', 'D']:
                user_answer = input("Please enter A, B, C, or D: ").upper().strip()
            
            if self.check_answer(user_answer, question['correct'], 
                               question['explanation'], question['formula_used']):
                self.score += 1
            
            input("\nPress Enter for next question...")
        
        self.display_final_score()
    
    def study_mode(self):
        """Display all questions and answers for study purposes"""
        print("=" * 70)
        print("📚 STUDY MODE - All Questions and Answers")
        print("=" * 70)
        
        for i, question in enumerate(self.questions):
            print(f"\n--- Question {i + 1} ---")
            print(f"{question['question']}\n")
            
            for option in question['options']:
                if option.startswith(question['correct']):
                    print(f"{option} ← CORRECT")
                else:
                    print(option)
            
            print(f"\n📐 Formula: {question['formula_used']}")
            print(f"💡 Explanation: {question['explanation']}")
            print("-" * 50)
    
    def filter_by_topic(self):
        """Filter questions by topic/formula type"""
        topics = {
            "1": "Standard Deviation & Variance",
            "2": "Central Limit Theorem & Standard Error", 
            "3": "Z-scores & Normal Distribution",
            "4": "Confidence Intervals",
            "5": "Hypothesis Testing",
            "6": "Probability Rules",
            "7": "All Topics"
        }
        
        print("\n📋 Choose a topic to practice:")
        for key, topic in topics.items():
            print(f"{key}. {topic}")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "7":
            return self.questions
        
        # Filter questions based on formula_used content
        topic_keywords = {
            "1": ["σ_total", "Var(", "standard deviation"],
            "2": ["SE =", "σ/√n", "Central Limit"],
            "3": ["z =", "Z >", "normal"],
            "4": ["CI =", "confidence"],
            "5": ["test statistic", "H₀", "α", "Power"],
            "6": ["P(", "probability"]
        }
        
        if choice in topic_keywords:
            keywords = topic_keywords[choice]
            filtered = []
            for q in self.questions:
                if any(keyword in q['formula_used'] or keyword in q['explanation'] 
                      for keyword in keywords):
                    filtered.append(q)
            return filtered
        
        return self.questions


def main():
    """Main function to run the practice quiz application"""
    quiz = PracticeProblemsQuiz()
    
    while True:
        print("\n" + "=" * 70)
        print("📊 STATISTICAL PRACTICE PROBLEMS QUIZ")
        print("=" * 70)
        print("Choose a mode:")
        print("1. 🎯 Full Practice Quiz (25 questions)")
        print("2. 🔄 Practice Mode (immediate feedback)")
        print("3. 📚 Study Mode (view all answers)")
        print("4. 🎲 Topic-Specific Practice")
        print("5. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            quiz.run_quiz()
        elif choice == '2':
            quiz.run_practice_mode()
        elif choice == '3':
            quiz.study_mode()
        elif choice == '4':
            filtered_questions = quiz.filter_by_topic()
            if filtered_questions:
                original_questions = quiz.questions
                quiz.questions = filtered_questions
                quiz.total_questions = len(filtered_questions)
                quiz.run_quiz()
                quiz.questions = original_questions
                quiz.total_questions = len(original_questions)
        elif choice == '5':
            print("📊 Great job practicing! Keep up the good work!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
