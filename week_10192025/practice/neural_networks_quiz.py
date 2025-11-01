#!/usr/bin/env python3
"""
Neural Networks Quiz - 25 Multiple Choice Questions
Based on BU Data Science Week 10 Neural Networks Content
"""

import random
import json
from datetime import datetime

class NeuralNetworksQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the main advantage of neural networks over simple linear regression?",
                "options": [
                    "A) They are faster to compute",
                    "B) They can model complex non-linear relationships",
                    "C) They require less data",
                    "D) They are easier to interpret"
                ],
                "correct": "B",
                "explanation": "Neural networks can model complex non-linear relationships through multiple layers and activation functions like ReLU."
            },
            {
                "question": "What does ReLU stand for?",
                "options": [
                    "A) Rectified Linear Unit",
                    "B) Recursive Linear Unit",
                    "C) Relative Linear Unit",
                    "D) Random Linear Unit"
                ],
                "correct": "A",
                "explanation": "ReLU stands for Rectified Linear Unit, an activation function that outputs the input if positive, zero otherwise."
            },
            {
                "question": "What is the output of ReLU(-5)?",
                "options": [
                    "A) -5",
                    "B) 5",
                    "C) 0",
                    "D) 1"
                ],
                "correct": "C",
                "explanation": "ReLU outputs 0 for any negative input, so ReLU(-5) = 0."
            },
            {
                "question": "What is the output of ReLU(3.5)?",
                "options": [
                    "A) 0",
                    "B) 3.5",
                    "C) -3.5",
                    "D) 1"
                ],
                "correct": "B",
                "explanation": "ReLU outputs the input value when it's positive, so ReLU(3.5) = 3.5."
            },
            {
                "question": "Why is ReLU important in neural networks?",
                "options": [
                    "A) It makes computation faster",
                    "B) It introduces non-linearity to prevent collapse to linear function",
                    "C) It reduces memory usage",
                    "D) It eliminates the need for training"
                ],
                "correct": "B",
                "explanation": "ReLU introduces non-linearity, preventing multiple linear layers from collapsing into a single linear function."
            },
            {
                "question": "What are the adjustable parameters in a neural network called?",
                "options": [
                    "A) Weights and biases",
                    "B) Inputs and outputs",
                    "C) Layers and nodes",
                    "D) Functions and variables"
                ],
                "correct": "A",
                "explanation": "Weights and biases are the adjustable parameters that the network learns during training."
            },
            {
                "question": "In the book profitability example, what were the two input features?",
                "options": [
                    "A) Author and genre",
                    "B) Number of pages and sale price",
                    "C) Publication year and rating",
                    "D) Length and width"
                ],
                "correct": "B",
                "explanation": "The example used number of pages and sale price as the two features to predict book profitability."
            },
            {
                "question": "What happens when you combine multiple linear layers without activation functions?",
                "options": [
                    "A) You get exponential complexity",
                    "B) The network becomes more powerful",
                    "C) You still get just another linear function",
                    "D) The network stops working"
                ],
                "correct": "C",
                "explanation": "A linear combination of linear functions is still just a linear function - no added complexity."
            },
            {
                "question": "What is a bias in a neural network?",
                "options": [
                    "A) An error in the model",
                    "B) A number added to each weighted sum",
                    "C) A type of activation function",
                    "D) A training algorithm"
                ],
                "correct": "B",
                "explanation": "A bias is a constant number added to the weighted sum in each neuron, allowing for more flexibility."
            },
            {
                "question": "How many layers does the simple neural network example in the text have?",
                "options": [
                    "A) 2 layers",
                    "B) 3 layers (input, hidden, output)",
                    "C) 4 layers",
                    "D) 1 layer"
                ],
                "correct": "B",
                "explanation": "The example has 3 layers: input layer (features), hidden layer (PV 1.A and 1.B), and output layer (PV 2)."
            },
            {
                "question": "What is the main difference between a decision tree and neural network approach?",
                "options": [
                    "A) Decision trees use if-then rules, neural networks use weighted sums",
                    "B) Decision trees are always more accurate",
                    "C) Neural networks can't handle categorical data",
                    "D) There is no difference"
                ],
                "correct": "A",
                "explanation": "Decision trees use explicit if-then branching rules, while neural networks use weighted sums with activation functions."
            },
            {
                "question": "What makes neural networks potentially very powerful?",
                "options": [
                    "A) They are fast to compute",
                    "B) They can approximate any function with proper weights",
                    "C) They require no training",
                    "D) They are easy to interpret"
                ],
                "correct": "B",
                "explanation": "Neural networks are universal function approximators - they can approximate any function given enough parameters and proper training."
            },
            {
                "question": "In the example, what is PV 1.A calculated as?",
                "options": [
                    "A) (pages * 0.01) + (price * 0.03)",
                    "B) (pages * 0.005) - (price * 0.06)",
                    "C) (pages * 2) + (price * 3)",
                    "D) (pages + price) / 2"
                ],
                "correct": "B",
                "explanation": "PV 1.A = (number of pages) * 0.005 - (sale price) * 0.06 according to the example."
            },
            {
                "question": "What is PV 1.B calculated as in the example?",
                "options": [
                    "A) (pages * 0.005) - (price * 0.06)",
                    "B) (pages * 0.01) + (price * 0.03)",
                    "C) (pages * 2) + (price * 3)",
                    "D) ReLU(pages + price)"
                ],
                "correct": "B",
                "explanation": "PV 1.B = (number of pages) * 0.01 + (sale price) * 0.03 according to the example."
            },
            {
                "question": "How is PV 2 calculated in the ReLU example?",
                "options": [
                    "A) PV1.A + PV1.B",
                    "B) ReLU(PV1.A) + ReLU(PV1.B)",
                    "C) ReLU(PV1.A) * 2 + ReLU(PV1.B) * 3",
                    "D) (PV1.A * PV1.B) / 2"
                ],
                "correct": "C",
                "explanation": "PV 2 = ReLU(PV 1.A) * 2 + ReLU(PV 1.B) * 3 in the ReLU example."
            },
            {
                "question": "Why can't you easily write down a decision tree for a large neural network?",
                "options": [
                    "A) Trees are too simple",
                    "B) The number of branches grows exponentially",
                    "C) Neural networks don't use branching",
                    "D) Trees can't handle numbers"
                ],
                "correct": "B",
                "explanation": "The number of branches in the equivalent tree grows exponentially with the number of linear equations, making it unmanageable."
            },
            {
                "question": "What is the purpose of adding complexity to neural networks?",
                "options": [
                    "A) To make them slower",
                    "B) To give more ability to control behavior through weights",
                    "C) To make them harder to understand",
                    "D) To use more memory"
                ],
                "correct": "B",
                "explanation": "Added complexity gives more parameters to adjust, providing more control over the network's behavior."
            },
            {
                "question": "According to the text, how many parameters does GPT-4 have?",
                "options": [
                    "A) Over a billion",
                    "B) Over a trillion",
                    "C) Over a million",
                    "D) Over a thousand"
                ],
                "correct": "B",
                "explanation": "The text states that GPT-4 has over a trillion parameters (weights and biases)."
            },
            {
                "question": "How long did GPT-4 take to train according to the text?",
                "options": [
                    "A) About one month",
                    "B) About six months",
                    "C) About three months",
                    "D) About one year"
                ],
                "correct": "C",
                "explanation": "The text mentions that GPT-4 takes about three months to train."
            },
            {
                "question": "What is a hidden layer in a neural network?",
                "options": [
                    "A) The input layer",
                    "B) The output layer",
                    "C) Layers between input and output",
                    "D) Layers that are not used"
                ],
                "correct": "C",
                "explanation": "Hidden layers are the layers between the input and output layers that process information internally."
            },
            {
                "question": "In the book example, what determines if a book is 'more profitable'?",
                "options": [
                    "A) Earning $500 or more",
                    "B) Earning $1,000 or more",
                    "C) Having more than 200 pages",
                    "D) Costing more than $15"
                ],
                "correct": "B",
                "explanation": "Books that earn $1,000 or more in aggregate are considered more profitable in the example."
            },
            {
                "question": "What is the main challenge in training neural networks?",
                "options": [
                    "A) Finding the right architecture",
                    "B) Setting the weights and biases to optimal values",
                    "C) Getting enough data",
                    "D) Choosing the right programming language"
                ],
                "correct": "B",
                "explanation": "The main challenge is finding the optimal values for all the weights and biases through training."
            },
            {
                "question": "What type of function can neural networks approximate?",
                "options": [
                    "A) Only linear functions",
                    "B) Only polynomial functions",
                    "C) Basically any function",
                    "D) Only simple functions"
                ],
                "correct": "C",
                "explanation": "Neural networks can approximate basically any function if the weights are set properly and the network is sufficiently complex."
            },
            {
                "question": "What happens in a neural network without biases?",
                "options": [
                    "A) It works perfectly",
                    "B) It becomes faster",
                    "C) It's not truly general and can't do everything",
                    "D) It uses less memory"
                ],
                "correct": "C",
                "explanation": "Without biases, the neural network is not truly general and cannot approximate all possible functions."
            },
            {
                "question": "What is the relationship between logistic regression and neural networks?",
                "options": [
                    "A) They are completely different",
                    "B) Neural networks are like multiple coordinated logistic regressions",
                    "C) Logistic regression is always better",
                    "D) They can't be compared"
                ],
                "correct": "B",
                "explanation": "Neural networks are similar to logistic regression in that they sum weighted features, but coordinate many such sums in a complex structure."
            }
        ]
        
        self.score = 0
        self.total_questions = len(self.questions)
        self.user_answers = []
        
    def shuffle_questions(self):
        """Shuffle the questions for variety"""
        random.shuffle(self.questions)
    
    def run_quiz(self):
        """Run the complete quiz"""
        print("=" * 60)
        print("🧠 NEURAL NETWORKS QUIZ - 25 Questions")
        print("=" * 60)
        print("Instructions:")
        print("- Answer each question by typing A, B, C, or D")
        print("- You can type 'quit' at any time to exit")
        print("- Your score will be shown at the end")
        print("=" * 60)
        
        input("\nPress Enter to start the quiz...")
        
        # Option to shuffle questions
        shuffle_choice = input("\nWould you like to shuffle the questions? (y/n): ").lower()
        if shuffle_choice == 'y':
            self.shuffle_questions()
        
        # Run through all questions
        for i, question_data in enumerate(self.questions, 1):
            print(f"\n{'='*60}")
            print(f"Question {i}/{self.total_questions}")
            print('='*60)
            
            answer = self.ask_question(question_data)
            
            if answer.lower() == 'quit':
                print("\nQuiz terminated by user.")
                return
            
            self.user_answers.append({
                'question_num': i,
                'question': question_data['question'],
                'user_answer': answer,
                'correct_answer': question_data['correct'],
                'is_correct': answer.upper() == question_data['correct'],
                'explanation': question_data['explanation']
            })
            
            if answer.upper() == question_data['correct']:
                self.score += 1
                print("✅ Correct!")
            else:
                print(f"❌ Incorrect. The correct answer is {question_data['correct']}")
            
            print(f"💡 Explanation: {question_data['explanation']}")
            
            # Show progress
            if i < self.total_questions:
                input("\nPress Enter for next question...")
        
        self.show_results()
    
    def ask_question(self, question_data):
        """Ask a single question and get user input"""
        print(f"\n{question_data['question']}\n")
        
        for option in question_data['options']:
            print(option)
        
        while True:
            answer = input("\nYour answer (A/B/C/D or 'quit'): ").strip().upper()
            
            if answer.lower() == 'quit':
                return answer
            
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            
            print("Please enter A, B, C, D, or 'quit'")
    
    def show_results(self):
        """Display final results and statistics"""
        print("\n" + "="*60)
        print("🎯 QUIZ RESULTS")
        print("="*60)
        
        percentage = (self.score / self.total_questions) * 100
        
        print(f"Final Score: {self.score}/{self.total_questions} ({percentage:.1f}%)")
        
        # Grade assignment
        if percentage >= 90:
            grade = "A"
            emoji = "🏆"
            message = "Excellent! You have a strong understanding of neural networks!"
        elif percentage >= 80:
            grade = "B"
            emoji = "🎉"
            message = "Great job! You have a good grasp of the concepts!"
        elif percentage >= 70:
            grade = "C"
            emoji = "👍"
            message = "Good work! Review the concepts you missed."
        elif percentage >= 60:
            grade = "D"
            emoji = "📚"
            message = "You're getting there! More study needed."
        else:
            grade = "F"
            emoji = "💪"
            message = "Keep studying! Neural networks take practice to master."
        
        print(f"\nGrade: {grade} {emoji}")
        print(f"Message: {message}")
        
        # Show incorrect answers for review
        incorrect_answers = [ans for ans in self.user_answers if not ans['is_correct']]
        
        if incorrect_answers:
            print(f"\n📋 REVIEW - Questions you missed ({len(incorrect_answers)} total):")
            print("-" * 60)
            
            for ans in incorrect_answers:
                print(f"\nQ{ans['question_num']}: {ans['question']}")
                print(f"Your answer: {ans['user_answer']}")
                print(f"Correct answer: {ans['correct_answer']}")
                print(f"Explanation: {ans['explanation']}")
        
        # Save results option
        save_choice = input("\nWould you like to save your results to a file? (y/n): ").lower()
        if save_choice == 'y':
            self.save_results()
    
    def save_results(self):
        """Save quiz results to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"neural_networks_quiz_results_{timestamp}.json"
        
        results_data = {
            'timestamp': datetime.now().isoformat(),
            'score': self.score,
            'total_questions': self.total_questions,
            'percentage': (self.score / self.total_questions) * 100,
            'answers': self.user_answers
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(results_data, f, indent=2)
            print(f"✅ Results saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving results: {e}")

def main():
    """Main function to run the quiz"""
    quiz = NeuralNetworksQuiz()
    
    try:
        quiz.run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please restart the quiz.")

if __name__ == "__main__":
    main()
