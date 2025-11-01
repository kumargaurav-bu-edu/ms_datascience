#!/usr/bin/env python3
"""
Machine Learning Quiz - Interactive Learning Game
10 questions covering various ML concepts with explanations
"""

import random

class MLQuiz:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                "question": "A classification model has 95% accuracy on training data but only 60% on test data. What is this called?",
                "options": [
                    "A) Underfitting",
                    "B) Overfitting", 
                    "C) Good generalization",
                    "D) Bias-variance tradeoff"
                ],
                "correct": "B",
                "explanation": "Overfitting occurs when a model performs well on training data but poorly on unseen test data, indicating it memorized rather than learned patterns."
            },
            {
                "question": "Which activation function is most commonly used in hidden layers of modern deep neural networks?",
                "options": [
                    "A) Sigmoid",
                    "B) Tanh", 
                    "C) ReLU",
                    "D) Linear"
                ],
                "correct": "C",
                "explanation": "ReLU (Rectified Linear Unit) is preferred because it avoids vanishing gradient problems and is computationally efficient."
            },
            {
                "question": "In a confusion matrix for binary classification, what does the top-right cell represent?",
                "options": [
                    "A) True Positives",
                    "B) False Positives", 
                    "C) True Negatives",
                    "D) False Negatives"
                ],
                "correct": "B",
                "explanation": "The top-right cell shows False Positives - cases predicted as positive but actually negative (Type I error)."
            },
            {
                "question": "Which metric is best for imbalanced datasets where the positive class is rare?",
                "options": [
                    "A) Accuracy",
                    "B) Precision", 
                    "C) F1-Score",
                    "D) Specificity"
                ],
                "correct": "C",
                "explanation": "F1-Score balances precision and recall, making it ideal for imbalanced datasets where accuracy can be misleading."
            },
            {
                "question": "What does regularization primarily help prevent in machine learning?",
                "options": [
                    "A) Underfitting",
                    "B) Overfitting", 
                    "C) Slow training",
                    "D) Poor accuracy"
                ],
                "correct": "B",
                "explanation": "Regularization adds penalties to complex models, preventing them from overfitting to training data."
            },
            {
                "question": "In K-means clustering, what does 'K' represent?",
                "options": [
                    "A) Number of features",
                    "B) Number of data points", 
                    "C) Number of clusters",
                    "D) Number of iterations"
                ],
                "correct": "C",
                "explanation": "K is the number of clusters you want the algorithm to find in your data."
            },
            {
                "question": "Which loss function is typically used for multi-class classification?",
                "options": [
                    "A) Mean Squared Error",
                    "B) Binary Cross-Entropy", 
                    "C) Categorical Cross-Entropy",
                    "D) Hinge Loss"
                ],
                "correct": "C",
                "explanation": "Categorical Cross-Entropy is designed for multi-class problems where each sample belongs to exactly one class."
            },
            {
                "question": "What is the main advantage of Random Forest over a single Decision Tree?",
                "options": [
                    "A) Faster training",
                    "B) Better interpretability", 
                    "C) Reduced overfitting",
                    "D) Lower memory usage"
                ],
                "correct": "C",
                "explanation": "Random Forest combines multiple trees, reducing overfitting through ensemble averaging and random feature selection."
            },
            {
                "question": "In gradient descent, what happens if the learning rate is too high?",
                "options": [
                    "A) Convergence is guaranteed",
                    "B) Training becomes very slow", 
                    "C) The algorithm may overshoot the minimum",
                    "D) Accuracy always improves"
                ],
                "correct": "C",
                "explanation": "A high learning rate can cause the algorithm to overshoot the optimal solution and fail to converge."
            },
            {
                "question": "Which technique is used to handle missing values by replacing them with the most frequent value?",
                "options": [
                    "A) Mean imputation",
                    "B) Mode imputation", 
                    "C) Median imputation",
                    "D) Forward fill"
                ],
                "correct": "B",
                "explanation": "Mode imputation replaces missing values with the most frequently occurring value in that feature."
            }
        ]
    
    def run_quiz(self):
        print("🧠 MACHINE LEARNING QUIZ 🧠")
        print("=" * 40)
        print("Answer each question by typing A, B, C, or D")
        print("=" * 40)
        
        # Shuffle questions for variety
        random.shuffle(self.questions)
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/10:")
            print(f"{q['question']}")
            print()
            for option in q['options']:
                print(f"  {option}")
            
            # Get user answer
            while True:
                answer = input("\nYour answer (A/B/C/D): ").upper().strip()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                print("Please enter A, B, C, or D")
            
            # Check answer
            if answer == q['correct']:
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Incorrect. The correct answer is {q['correct']}")
            
            print(f"💡 Explanation: {q['explanation']}")
            
            # Pause between questions
            input("\nPress Enter to continue...")
            print("-" * 50)
        
        # Final score
        print(f"\n🎉 QUIZ COMPLETE! 🎉")
        print(f"Your Score: {self.score}/10 ({self.score*10}%)")
        
        if self.score >= 8:
            print("🏆 Excellent! You're an ML expert!")
        elif self.score >= 6:
            print("👍 Good job! You have solid ML knowledge!")
        elif self.score >= 4:
            print("📚 Not bad! Keep studying to improve!")
        else:
            print("💪 Keep learning! Practice makes perfect!")

if __name__ == "__main__":
    quiz = MLQuiz()
    quiz.run_quiz()
