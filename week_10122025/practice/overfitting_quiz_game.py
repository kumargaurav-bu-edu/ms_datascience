#!/usr/bin/env python3
"""
Interactive Overfitting Quiz Game
A fun way to learn about overfitting in data science!
"""

import random
import time
from typing import List, Dict, Tuple

class OverfittingQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is overfitting in data science?",
                "options": [
                    "When a model performs equally well on training and test data",
                    "When a model learns the training data too well and fails to generalize to new data",
                    "When a model is too simple to capture underlying patterns",
                    "When a model has too few parameters"
                ],
                "correct": 1,
                "explanation": "Overfitting occurs when a model becomes too specialized to the training data, memorizing noise and specific details rather than learning generalizable patterns."
            },
            {
                "question": "Which of the following is a key characteristic of an overfitted model?",
                "options": [
                    "High training error and high test error",
                    "Low training error and low test error",
                    "Low training error and high test error",
                    "High training error and low test error"
                ],
                "correct": 2,
                "explanation": "This is the classic signature of overfitting - the model performs excellently on data it has seen (training) but poorly on new, unseen data (test)."
            },
            {
                "question": "What does it mean for a pattern to 'recur' in the context of data science models?",
                "options": [
                    "The same data points appear multiple times",
                    "The pattern appears consistently in new, unseen datasets",
                    "The model produces the same output every time",
                    "The training process repeats multiple iterations"
                ],
                "correct": 1,
                "explanation": "A true pattern should be reproducible and appear in different datasets, not just the original training data."
            },
            {
                "question": "In the flower height example, if the first 100 flowers have an average height of 12 inches, what concern would arise with an overfitted model?",
                "options": [
                    "It would predict exactly 12 inches for all future flowers",
                    "It would memorize individual flower heights rather than the general pattern",
                    "It would ignore the height measurements completely",
                    "It would only work for flowers in the same garden"
                ],
                "correct": 1,
                "explanation": "An overfitted model would remember specific flowers instead of learning the general average height pattern."
            },
            {
                "question": "Which scenario best demonstrates overfitting?",
                "options": [
                    "A model that predicts house prices with 95% accuracy on both training and test data",
                    "A model that memorizes every training example and achieves 100% training accuracy but 60% test accuracy",
                    "A model that achieves 70% accuracy on both training and test data",
                    "A model that improves performance as more data is added"
                ],
                "correct": 1,
                "explanation": "This shows the classic overfitting pattern - perfect training performance with poor generalization."
            },
            {
                "question": "What is the relationship between model complexity and overfitting?",
                "options": [
                    "More complex models are always better",
                    "Simpler models always overfit",
                    "Very complex models are more prone to overfitting",
                    "Model complexity has no relationship to overfitting"
                ],
                "correct": 2,
                "explanation": "Complex models have more capacity to memorize training data, making them more susceptible to overfitting."
            },
            {
                "question": "Which technique is commonly used to detect overfitting?",
                "options": [
                    "Using only training data for evaluation",
                    "Cross-validation with separate training and validation sets",
                    "Increasing the number of features",
                    "Reducing the dataset size"
                ],
                "correct": 1,
                "explanation": "By testing on data the model hasn't seen during training, we can detect if it's overfitting."
            },
            {
                "question": "What is underfitting?",
                "options": [
                    "When a model is too complex for the data",
                    "When a model is too simple to capture the underlying patterns",
                    "When a model performs perfectly on test data",
                    "When a model has too many parameters"
                ],
                "correct": 1,
                "explanation": "Underfitting is the opposite of overfitting - the model is too simple to learn even the basic patterns in the data."
            },
            {
                "question": "In the book price prediction example, what would indicate overfitting?",
                "options": [
                    "The model learns general relationships between price, page count, and profitability",
                    "The model memorizes specific books from training data rather than learning general patterns",
                    "The model ignores page count completely",
                    "The model predicts the same profitability for all books"
                ],
                "correct": 1,
                "explanation": "An overfitted model would remember individual books instead of learning the general relationship between features and profitability."
            },
            {
                "question": "Which of the following is NOT a common cause of overfitting?",
                "options": [
                    "Too many features relative to the number of training examples",
                    "Training for too many iterations",
                    "Using cross-validation",
                    "Having a very complex model architecture"
                ],
                "correct": 2,
                "explanation": "Cross-validation actually helps prevent overfitting by providing a way to validate model performance on unseen data."
            },
            {
                "question": "What is the bias-variance tradeoff in relation to overfitting?",
                "options": [
                    "Overfitted models have high bias and low variance",
                    "Overfitted models have low bias and high variance",
                    "Overfitted models have high bias and high variance",
                    "Bias and variance are unrelated to overfitting"
                ],
                "correct": 1,
                "explanation": "Overfitted models fit the training data very well (low bias) but vary greatly with different datasets (high variance)."
            },
            {
                "question": "Which regularization technique helps prevent overfitting by adding a penalty term to the loss function?",
                "options": [
                    "Data augmentation",
                    "L1 and L2 regularization",
                    "Feature scaling",
                    "Data normalization"
                ],
                "correct": 1,
                "explanation": "Regularization techniques add penalty terms to prevent the model from becoming too complex and overfitting."
            },
            {
                "question": "What is early stopping in the context of preventing overfitting?",
                "options": [
                    "Stopping data collection early",
                    "Terminating training when validation performance starts to degrade",
                    "Stopping the model from making predictions",
                    "Ending the feature selection process"
                ],
                "correct": 1,
                "explanation": "Early stopping prevents the model from continuing to overfit by stopping when validation performance begins to worsen."
            },
            {
                "question": "How does increasing the training dataset size typically affect overfitting?",
                "options": [
                    "Always increases overfitting",
                    "Has no effect on overfitting",
                    "Generally reduces overfitting",
                    "Only affects underfitting"
                ],
                "correct": 2,
                "explanation": "More training data gives the model more examples to learn from, making it harder to memorize and more likely to learn general patterns."
            },
            {
                "question": "What is the purpose of a validation set in machine learning?",
                "options": [
                    "To train the model",
                    "To test the final model performance",
                    "To tune hyperparameters and detect overfitting during training",
                    "To store backup data"
                ],
                "correct": 2,
                "explanation": "The validation set provides feedback during model development without contaminating the final test evaluation."
            },
            {
                "question": "Which statement about the generalization ability of models is correct?",
                "options": [
                    "Overfitted models generalize well to new data",
                    "The goal is to find models that perform well on unseen data",
                    "Generalization is only important for training data",
                    "Models should only work on the specific dataset they were trained on"
                ],
                "correct": 1,
                "explanation": "Generalization - the ability to perform well on new, unseen data - is the primary goal of machine learning."
            },
            {
                "question": "In k-fold cross-validation, what happens if a model consistently performs much better on training folds than validation folds?",
                "options": [
                    "The model is underfitting",
                    "The model is likely overfitting",
                    "The model is perfectly balanced",
                    "The cross-validation is invalid"
                ],
                "correct": 1,
                "explanation": "Consistently better performance on training than validation data across multiple folds indicates overfitting."
            },
            {
                "question": "What is dropout in neural networks designed to prevent?",
                "options": [
                    "Underfitting",
                    "Slow training",
                    "Overfitting",
                    "Data leakage"
                ],
                "correct": 2,
                "explanation": "Dropout randomly removes neurons during training, preventing the model from relying too heavily on specific neurons and reducing overfitting."
            },
            {
                "question": "If you observe that your model's training accuracy keeps improving while validation accuracy starts decreasing, what is happening?",
                "options": [
                    "The model is underfitting",
                    "The model is starting to overfit",
                    "The model is perfectly trained",
                    "There's an error in the validation data"
                ],
                "correct": 1,
                "explanation": "When training accuracy continues improving while validation accuracy decreases, the model is beginning to overfit to the training data."
            },
            {
                "question": "Which approach would be LEAST effective at preventing overfitting?",
                "options": [
                    "Using regularization techniques",
                    "Collecting more training data",
                    "Adding more complex features without additional data",
                    "Using cross-validation for model selection"
                ],
                "correct": 2,
                "explanation": "This would likely increase overfitting by making the model more complex without providing more data to learn from."
            }
        ]
        
        self.score = 0
        self.total_questions = 0
        self.incorrect_answers = []
        
    def display_welcome(self):
        """Display welcome message and instructions"""
        print("=" * 60)
        print("🧠 WELCOME TO THE OVERFITTING QUIZ GAME! 🧠")
        print("=" * 60)
        print("📚 Learn about overfitting in data science through interactive questions!")
        print("🎯 Choose your answer by typing A, B, C, or D")
        print("💡 Get immediate feedback and explanations")
        print("🏆 Track your progress and review mistakes")
        print("=" * 60)
        print()
        
    def display_question(self, question_data: Dict, question_num: int, total: int):
        """Display a single question with options"""
        print(f"📝 Question {question_num}/{total}")
        print("-" * 40)
        print(f"❓ {question_data['question']}")
        print()
        
        for i, option in enumerate(question_data['options']):
            letter = chr(65 + i)  # Convert 0,1,2,3 to A,B,C,D
            print(f"   {letter}) {option}")
        print()
        
    def get_user_answer(self) -> str:
        """Get and validate user input"""
        while True:
            answer = input("Your answer (A/B/C/D): ").upper().strip()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("❌ Please enter A, B, C, or D")
            
    def check_answer(self, user_answer: str, question_data: Dict, question_num: int) -> bool:
        """Check if answer is correct and provide feedback"""
        correct_index = question_data['correct']
        correct_letter = chr(65 + correct_index)  # Convert index to letter
        user_index = ord(user_answer) - 65  # Convert letter to index
        
        is_correct = user_index == correct_index
        
        if is_correct:
            print("✅ Correct! Well done!")
            self.score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {correct_letter}")
            self.incorrect_answers.append({
                'question_num': question_num,
                'question': question_data['question'],
                'your_answer': user_answer,
                'correct_answer': correct_letter,
                'explanation': question_data['explanation']
            })
            
        print(f"💡 Explanation: {question_data['explanation']}")
        print()
        return is_correct
        
    def display_progress(self, current: int, total: int):
        """Display current progress"""
        percentage = (current / total) * 100
        progress_bar = "█" * int(percentage // 5) + "░" * (20 - int(percentage // 5))
        print(f"📊 Progress: [{progress_bar}] {percentage:.1f}% ({current}/{total})")
        print(f"🎯 Current Score: {self.score}/{current}")
        print()
        
    def display_final_results(self):
        """Display final quiz results"""
        percentage = (self.score / self.total_questions) * 100
        
        print("=" * 60)
        print("🏁 QUIZ COMPLETED!")
        print("=" * 60)
        print(f"📊 Final Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        # Performance feedback
        if percentage >= 90:
            print("🌟 Outstanding! You have excellent understanding of overfitting!")
        elif percentage >= 80:
            print("🎉 Great job! You have a strong grasp of overfitting concepts!")
        elif percentage >= 70:
            print("👍 Good work! You understand the basics well!")
        elif percentage >= 60:
            print("📚 Not bad! Review the concepts and try again!")
        else:
            print("💪 Keep studying! Overfitting is tricky but you'll get it!")
            
        print("=" * 60)
        
    def review_mistakes(self):
        """Allow user to review incorrect answers"""
        if not self.incorrect_answers:
            print("🎉 Perfect score! No mistakes to review!")
            return
            
        print(f"\n📋 REVIEW OF INCORRECT ANSWERS ({len(self.incorrect_answers)} questions)")
        print("=" * 60)
        
        for i, mistake in enumerate(self.incorrect_answers, 1):
            print(f"\n❌ Mistake #{i}")
            print(f"Question {mistake['question_num']}: {mistake['question']}")
            print(f"Your answer: {mistake['your_answer']}")
            print(f"Correct answer: {mistake['correct_answer']}")
            print(f"💡 Explanation: {mistake['explanation']}")
            print("-" * 40)
            
    def play_quiz(self, num_questions: int = None, randomize: bool = True):
        """Main quiz game loop"""
        self.display_welcome()
        
        # Determine number of questions
        if num_questions is None:
            while True:
                try:
                    num_questions = int(input(f"How many questions? (1-{len(self.questions)}, or press Enter for all): ") or len(self.questions))
                    if 1 <= num_questions <= len(self.questions):
                        break
                    print(f"Please enter a number between 1 and {len(self.questions)}")
                except ValueError:
                    print("Please enter a valid number")
        
        # Select and optionally randomize questions
        selected_questions = self.questions.copy()
        if randomize:
            random.shuffle(selected_questions)
        selected_questions = selected_questions[:num_questions]
        
        self.total_questions = num_questions
        
        print(f"\n🚀 Starting quiz with {num_questions} questions!")
        print("Press Enter when ready...")
        input()
        
        # Main quiz loop
        for i, question_data in enumerate(selected_questions, 1):
            self.display_question(question_data, i, num_questions)
            user_answer = self.get_user_answer()
            self.check_answer(user_answer, question_data, i)
            
            if i < num_questions:
                self.display_progress(i, num_questions)
                print("Press Enter for next question...")
                input()
                print("\n" + "="*60 + "\n")
        
        # Show final results
        self.display_final_results()
        
        # Ask if user wants to review mistakes
        if self.incorrect_answers:
            review = input("\n🔍 Would you like to review your mistakes? (y/n): ").lower().strip()
            if review.startswith('y'):
                self.review_mistakes()
                
    def quick_practice(self, num_questions: int = 5):
        """Quick practice mode with fewer questions"""
        print("⚡ QUICK PRACTICE MODE")
        self.play_quiz(num_questions, randomize=True)


def main():
    """Main function to run the quiz game"""
    quiz = OverfittingQuiz()
    
    while True:
        print("\n" + "="*50)
        print("🎮 OVERFITTING QUIZ GAME MENU")
        print("="*50)
        print("1. 📚 Full Quiz (20 questions)")
        print("2. ⚡ Quick Practice (5 questions)")
        print("3. 🎯 Custom Quiz (choose number)")
        print("4. 🚪 Exit")
        print("="*50)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            quiz = OverfittingQuiz()  # Reset for new game
            quiz.play_quiz()
        elif choice == '2':
            quiz = OverfittingQuiz()  # Reset for new game
            quiz.quick_practice()
        elif choice == '3':
            quiz = OverfittingQuiz()  # Reset for new game
            try:
                num = int(input(f"How many questions (1-{len(quiz.questions)}): "))
                if 1 <= num <= len(quiz.questions):
                    quiz.play_quiz(num)
                else:
                    print("Invalid number of questions!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == '4':
            print("👋 Thanks for playing! Keep learning about overfitting!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
