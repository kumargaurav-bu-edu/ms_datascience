"""
Interactive Model Performance Evaluation Quiz
Run this program to take the quiz interactively.
Covers: Ranking vs Classification, Profit Curves, ROC Curves, Lift Curves, and Capstone Proposal Development
"""

import json
import random

def load_quiz(filename="model_performance_quiz.json"):
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
    quiz_data = load_quiz("model_performance_quiz.json")
    questions = quiz_data['questions']
    
    print(f"\n{'='*70}")
    print(f"Welcome to the Model Performance Evaluation Quiz!")
    print(f"Topics: Ranking vs Classification, Profit Curves, ROC Curves, Lift Curves")
    print(f"Total Questions: {len(questions)}")
    print(f"{'='*70}\n")
    
    # Option to shuffle questions
    shuffle = input("Would you like to shuffle the questions? (y/n): ").lower() == 'y'
    if shuffle:
        random.shuffle(questions)
    
    # Option to filter by difficulty
    print("\nDifficulty levels: Level 1 (Basic), Level 2 (Intermediate), Level 3 (Advanced)")
    filter_difficulty = input("Filter by difficulty level? (Enter 1, 2, 3, or 'all'): ").strip()
    if filter_difficulty in ['1', '2', '3']:
        level_map = {'1': 'Level 1 (Basic)', '2': 'Level 2 (Intermediate)', '3': 'Level 3 (Advanced)'}
        questions = [q for q in questions if q.get('difficulty') == level_map[filter_difficulty]]
        print(f"Filtered to {len(questions)} questions of {level_map[filter_difficulty]} difficulty.\n")
    
    score = 0
    total = len(questions)
    results = []
    
    for i, q in enumerate(questions, 1):
        print(f"\n{'='*70}")
        print(f"Question {i}/{total}")
        if 'difficulty' in q:
            print(f"Difficulty: {q['difficulty']}")
        if 'topic' in q:
            print(f"Topic: {q['topic']}")
        print(f"{'='*70}")
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
        
        print(f"\nExplanation: {q['explanation']}")
        
        results.append({
            'question_id': q['id'],
            'question': q['question'],
            'topic': q.get('topic', 'N/A'),
            'difficulty': q.get('difficulty', 'N/A'),
            'user_answer': user_answer,
            'correct_answer': correct_letter,
            'is_correct': is_correct
        })
        
        input("\nPress Enter to continue...")
    
    # Display final results
    print(f"\n{'='*70}")
    print(f"Quiz Complete!")
    print(f"{'='*70}")
    print(f"Score: {score}/{total} ({(score/total)*100:.1f}%)")
    
    # Performance by topic
    topic_scores = {}
    for result in results:
        topic = result['topic']
        if topic not in topic_scores:
            topic_scores[topic] = {'correct': 0, 'total': 0}
        topic_scores[topic]['total'] += 1
        if result['is_correct']:
            topic_scores[topic]['correct'] += 1
    
    print(f"\n{'='*70}")
    print("Performance by Topic:")
    print(f"{'='*70}")
    for topic, scores in topic_scores.items():
        percentage = (scores['correct'] / scores['total']) * 100
        print(f"{topic}: {scores['correct']}/{scores['total']} ({percentage:.1f}%)")
    
    # Performance by difficulty
    difficulty_scores = {}
    for result in results:
        diff = result['difficulty']
        if diff not in difficulty_scores:
            difficulty_scores[diff] = {'correct': 0, 'total': 0}
        difficulty_scores[diff]['total'] += 1
        if result['is_correct']:
            difficulty_scores[diff]['correct'] += 1
    
    print(f"\n{'='*70}")
    print("Performance by Difficulty:")
    print(f"{'='*70}")
    for diff, scores in difficulty_scores.items():
        percentage = (scores['correct'] / scores['total']) * 100
        print(f"{diff}: {scores['correct']}/{scores['total']} ({percentage:.1f}%)")
    
    print(f"\n{'='*70}")
    print("Results Summary:")
    print(f"{'='*70}")
    for result in results:
        status = "✓" if result['is_correct'] else "✗"
        print(f"{status} Question {result['question_id']}: {result['question'][:60]}...")
    
    # Save results
    with open("quiz_results.json", 'w') as f:
        json.dump({
            'score': score,
            'total': total,
            'percentage': (score/total)*100,
            'topic_scores': {k: {'correct': v['correct'], 'total': v['total'], 
                                'percentage': (v['correct']/v['total'])*100} 
                            for k, v in topic_scores.items()},
            'difficulty_scores': {k: {'correct': v['correct'], 'total': v['total'],
                                     'percentage': (v['correct']/v['total'])*100}
                                 for k, v in difficulty_scores.items()},
            'results': results
        }, f, indent=2)
    
    print(f"\nResults saved to quiz_results.json")

if __name__ == "__main__":
    take_quiz()
