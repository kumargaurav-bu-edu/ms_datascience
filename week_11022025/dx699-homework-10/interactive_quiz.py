"""
Interactive Clustering Concepts Quiz
Run this program to take the quiz interactively.
"""

import json
import random

def load_quiz(filename="clustering_quiz.json"):
    """Load quiz questions from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)

def shuffle_options(question):
    """Shuffle options while keeping track of correct answer"""
    options = question['options'].copy()
    correct_answer = question['correct']
    correct_text = options[ord(correct_answer) - ord('A')]
    
    # Shuffle options
    indices = list(range(len(options)))
    random.shuffle(indices)
    shuffled_options = [options[i] for i in indices]
    
    # Find new position of correct answer
    new_correct_index = shuffled_options.index(correct_text)
    new_correct_letter = chr(ord('A') + new_correct_index)
    
    return shuffled_options, new_correct_letter, correct_text

def take_quiz():
    """Interactive quiz function"""
    quiz_data = load_quiz("clustering_quiz.json")
    questions = quiz_data['questions']
    
    # Option to shuffle questions
    shuffle = input("Would you like to shuffle the questions? (y/n): ").lower() == 'y'
    if shuffle:
        random.shuffle(questions)
    
    score = 0
    total = len(questions)
    results = []
    
    print(f"\n{'='*60}")
    print(f"Welcome to the Clustering Concepts Quiz!")
    print(f"Total Questions: {total}")
    print(f"{'='*60}\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{total}")
        print(f"{q['question']}\n")
        
        # Shuffle options for each question
        shuffled_options, correct_letter, correct_text = shuffle_options(q)
        
        # Display options
        for idx, option in enumerate(shuffled_options):
            letter = chr(ord('A') + idx)
            print(f"{letter}. {option}")
        
        # Get user answer
        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").upper().strip()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        # Check answer
        is_correct = user_answer == correct_letter
        if is_correct:
            score += 1
            print("\n✓ Correct!")
        else:
            print(f"\n✗ Incorrect. The correct answer is {correct_letter}.")
        
        print(f"Explanation: {q['explanation']}")
        
        results.append({
            'question_id': q['id'],
            'question': q['question'],
            'user_answer': user_answer,
            'correct_answer': correct_letter,
            'is_correct': is_correct
        })
        
        input("\nPress Enter to continue...")
    
    # Display final results
    print(f"\n{'='*60}")
    print(f"Quiz Complete!")
    print(f"{'='*60}")
    print(f"Score: {score}/{total} ({(score/total)*100:.1f}%)")
    print(f"\nResults Summary:")
    
    for result in results:
        status = "✓" if result['is_correct'] else "✗"
        print(f"{status} Question {result['question_id']}: {result['question'][:50]}...")
    
    # Save results
    with open("quiz_results.json", 'w') as f:
        json.dump({
            'score': score,
            'total': total,
            'percentage': (score/total)*100,
            'results': results
        }, f, indent=2)
    
    print(f"\nResults saved to quiz_results.json")

if __name__ == "__main__":
    take_quiz()
