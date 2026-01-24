"""
Interactive Text Representation Quiz
Run this program to take the quiz interactively.
Covers: Representation, Bag of Words, TF-IDF, N-grams, and Named Entity Extraction
"""

import json
import random
import os

def load_quiz(filename="text_representation_quiz.json"):
    """Load quiz questions from JSON file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    with open(file_path, 'r') as f:
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

def filter_questions_by_level(questions, level=None):
    """Filter questions by difficulty level"""
    if level is None:
        return questions
    return [q for q in questions if q.get('level', '').lower() == level.lower()]

def take_quiz():
    """Interactive quiz function"""
    quiz_data = load_quiz("text_representation_quiz.json")
    questions = quiz_data['questions']
    
    print(f"\n{'='*70}")
    print(f"Welcome to the {quiz_data['title']}!")
    print(f"{'='*70}")
    print(f"\nDescription: {quiz_data.get('description', '')}")
    print(f"\nLearning Objectives:")
    for obj in quiz_data.get('learning_objectives', []):
        print(f"  • {obj}")
    print(f"\nTotal Questions: {len(questions)}")
    
    # Ask for difficulty level filter
    print(f"\n{'='*70}")
    print("Difficulty Levels Available:")
    print("  1. All levels (Basic, Intermediate, Advanced)")
    print("  2. Basic only")
    print("  3. Intermediate only")
    print("  4. Advanced only")
    print("  5. Basic + Intermediate")
    print("  6. Intermediate + Advanced")
    
    level_choice = input("\nSelect difficulty level (1-6, default=1): ").strip() or "1"
    
    level_map = {
        "1": None,
        "2": "Basic",
        "3": "Intermediate",
        "4": "Advanced",
        "5": ["Basic", "Intermediate"],
        "6": ["Intermediate", "Advanced"]
    }
    
    selected_level = level_map.get(level_choice, None)
    
    if isinstance(selected_level, list):
        questions = [q for q in questions if q.get('level', '') in selected_level]
    elif selected_level:
        questions = filter_questions_by_level(questions, selected_level)
    
    if not questions:
        print("No questions found for the selected level.")
        return
    
    print(f"\nQuestions in selected level(s): {len(questions)}")
    
    # Option to shuffle questions
    shuffle = input("Would you like to shuffle the questions? (y/n, default=y): ").lower()
    if shuffle != 'n':
        random.shuffle(questions)
    
    # Option to limit number of questions
    limit_input = input(f"How many questions would you like to answer? (1-{len(questions)}, default=all): ").strip()
    if limit_input:
        try:
            limit = int(limit_input)
            questions = questions[:limit]
        except ValueError:
            pass
    
    score = 0
    total = len(questions)
    results = []
    
    print(f"\n{'='*70}")
    print(f"Starting Quiz!")
    print(f"Total Questions: {total}")
    print(f"{'='*70}\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\n{'='*70}")
        print(f"Question {i}/{total}")
        print(f"Level: {q.get('level', 'N/A')} | Topic: {q.get('topic', 'N/A')}")
        print(f"{'='*70}")
        print(f"\n{q['question']}\n")
        
        # Shuffle options for each question
        shuffled_options, correct_letter, correct_text = shuffle_options(q)
        
        # Display options
        for idx, option in enumerate(shuffled_options):
            letter = chr(ord('A') + idx)
            print(f"  {letter}. {option}")
        
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
            'level': q.get('level', 'N/A'),
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
    
    # Performance by level
    level_stats = {}
    for result in results:
        level = result['level']
        if level not in level_stats:
            level_stats[level] = {'correct': 0, 'total': 0}
        level_stats[level]['total'] += 1
        if result['is_correct']:
            level_stats[level]['correct'] += 1
    
    if level_stats:
        print(f"\nPerformance by Level:")
        for level, stats in sorted(level_stats.items()):
            percentage = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"  {level}: {stats['correct']}/{stats['total']} ({percentage:.1f}%)")
    
    # Performance by topic
    topic_stats = {}
    for result in results:
        topic = result['topic']
        if topic not in topic_stats:
            topic_stats[topic] = {'correct': 0, 'total': 0}
        topic_stats[topic]['total'] += 1
        if result['is_correct']:
            topic_stats[topic]['correct'] += 1
    
    if topic_stats:
        print(f"\nPerformance by Topic:")
        for topic, stats in sorted(topic_stats.items()):
            percentage = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"  {topic}: {stats['correct']}/{stats['total']} ({percentage:.1f}%)")
    
    print(f"\nDetailed Results Summary:")
    for result in results:
        status = "✓" if result['is_correct'] else "✗"
        print(f"{status} Q{result['question_id']} ({result['level']}): {result['question'][:60]}...")
    
    # Save results
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(script_dir, "quiz_results.json")
    
    with open(results_path, 'w') as f:
        json.dump({
            'quiz_title': quiz_data['title'],
            'score': score,
            'total': total,
            'percentage': (score/total)*100,
            'level_stats': level_stats,
            'topic_stats': topic_stats,
            'results': results
        }, f, indent=2)
    
    print(f"\nResults saved to quiz_results.json")
    
    # Provide feedback
    percentage = (score/total)*100
    if percentage >= 90:
        print("\n🎉 Excellent work! You have a strong understanding of text representation concepts.")
    elif percentage >= 75:
        print("\n👍 Good job! Review the incorrect answers to strengthen your understanding.")
    elif percentage >= 60:
        print("\n📚 Keep practicing! Focus on reviewing the explanations for questions you missed.")
    else:
        print("\n📖 Review the material and try again. Pay special attention to TF-IDF formulas and n-gram concepts.")

if __name__ == "__main__":
    take_quiz()

