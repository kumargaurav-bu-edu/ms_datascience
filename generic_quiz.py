#!/usr/bin/env python3
"""
Reusable Interactive Quiz Program
Loads questions from a JSON file and runs an interactive quiz.

Usage:
    python3 quiz.py [quiz_file.json]
    
If no file is specified, defaults to quiz_questions.json in the same directory.
"""

import json
import os
import sys
import random
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class QuestionType(Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    SHORT_ANSWER = "short_answer"
    FILL_IN = "fill_in"
    CALCULATION = "calculation"
    SCENARIO = "scenario"
    INTERPRETATION = "interpretation"
    ANALYSIS = "analysis"


@dataclass
class Question:
    """Represents a quiz question with all its components."""
    number: int
    level: int
    question_type: QuestionType
    section: str
    question_text: str
    options: List[str] = None
    correct_answer: str = None
    explanation: str = None
    learning_objective: str = None
    keywords: List[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Question':
        """Create a Question instance from a dictionary."""
        # Convert question_type string to enum
        qtype_str = data.get('question_type', '').lower()
        try:
            qtype = QuestionType(qtype_str)
        except ValueError:
            raise ValueError(f"Invalid question_type: {qtype_str}. Must be one of: {[e.value for e in QuestionType]}")
        
        return cls(
            number=data.get('number', 0),
            level=data.get('level', 1),
            question_type=qtype,
            section=data.get('section', ''),
            question_text=data.get('question_text', ''),
            options=data.get('options') if data.get('options') else None,
            correct_answer=data.get('correct_answer', ''),
            explanation=data.get('explanation', ''),
            learning_objective=data.get('learning_objective', ''),
            keywords=data.get('keywords', []) if data.get('keywords') else []
        )


class Quiz:
    """Main quiz application class."""
    
    def __init__(self, json_file_path: Optional[str] = None):
        """
        Initialize the quiz.
        
        Args:
            json_file_path: Path to JSON file containing questions. 
                          If None, looks for quiz_questions.json in the same directory.
        """
        self.json_file_path = json_file_path or self._find_default_json()
        self.quiz_metadata = {}
        self.questions = self._load_questions_from_json()
        self.score = 0
        self.total_questions = len(self.questions)
        self.user_answers = {}
        self.correct_answers = {}
    
    def _find_default_json(self) -> str:
        """Find the default JSON file, searching in current directory and subdirectories."""
        script_dir = Path(__file__).parent
        
        # First, check in the same directory as the script
        default_file = script_dir / "quiz_questions.json"
        if default_file.exists():
            return str(default_file)
        
        # Search in subdirectories for quiz JSON files
        possible_names = ["quiz_questions.json", "example_quiz.json"]
        for name in possible_names:
            for json_file in script_dir.rglob(name):
                if json_file.is_file():
                    return str(json_file)
        
        # If not found, return the default path (will show helpful error)
        return str(default_file)
    
    def _load_questions_from_json(self) -> List[Question]:
        """Load questions from JSON file."""
        if not os.path.exists(self.json_file_path):
            # Try to find available JSON files to suggest
            script_dir = Path(__file__).parent
            json_files = list(script_dir.rglob("*.json"))
            quiz_files = [f for f in json_files if "quiz" in f.name.lower()]
            
            error_msg = f"Quiz file not found: {self.json_file_path}\n\n"
            if quiz_files:
                error_msg += "Available quiz files found:\n"
                for qf in quiz_files[:5]:  # Show up to 5 files
                    rel_path = qf.relative_to(script_dir)
                    error_msg += f"  - {rel_path}\n"
                error_msg += f"\nRun: python {Path(__file__).name} <path_to_json_file>\n"
                error_msg += f"Example: python {Path(__file__).name} week_01182026/DX699-O2/quiz_questions.json"
            else:
                error_msg += "Please create a JSON file with quiz questions or specify a valid path.\n"
                error_msg += f"Usage: python {Path(__file__).name} <path_to_json_file>"
            
            raise FileNotFoundError(error_msg)
        
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {self.json_file_path}: {e}")
        
        # Load metadata
        self.quiz_metadata = data.get('quiz_metadata', {})
        
        # Load questions
        questions_data = data.get('questions', [])
        if not questions_data:
            raise ValueError(f"No questions found in {self.json_file_path}")
        
        questions = []
        for q_data in questions_data:
            try:
                question = Question.from_dict(q_data)
                questions.append(question)
            except Exception as e:
                print(f"Warning: Skipping question {q_data.get('number', 'unknown')}: {e}", file=sys.stderr)
                continue
        
        if not questions:
            raise ValueError(f"No valid questions could be loaded from {self.json_file_path}")
        
        return questions
    
    def _check_answer(self, question: Question, user_answer: str) -> Tuple[Optional[bool], str]:
        """
        Check if user's answer is correct.
        
        Returns:
            Tuple of (is_correct, explanation)
            is_correct can be True, False, or None (for open-ended questions needing review)
        """
        user_answer = user_answer.strip()
        if not user_answer:
            return False, question.explanation
        
        user_answer_upper = user_answer.upper()
        correct = question.correct_answer.upper() if question.correct_answer else ""
        
        if question.question_type == QuestionType.MULTIPLE_CHOICE:
            # Extract just the letter
            user_letter = user_answer_upper[0] if user_answer_upper else ""
            return user_letter == correct, question.explanation
        
        elif question.question_type == QuestionType.TRUE_FALSE:
            # Normalize true/false answers (user -> "True"/"False"; correct is already .upper() -> "TRUE"/"FALSE")
            user_answer_lower = user_answer.lower()
            if user_answer_lower in ['true', 't', '1', 'yes', 'y']:
                user_normalized = "TRUE"
            elif user_answer_lower in ['false', 'f', '0', 'no', 'n']:
                user_normalized = "FALSE"
            else:
                return False, question.explanation
            
            return user_normalized == correct, question.explanation
        
        elif question.question_type == QuestionType.FILL_IN:
            # Check if answer contains key terms (case-insensitive)
            user_lower = user_answer.lower()
            correct_lower = correct.lower()
            # Check for exact match or keyword match
            if correct_lower in user_lower or user_lower in correct_lower:
                return True, question.explanation
            # Check keywords
            if question.keywords:
                for keyword in question.keywords:
                    if keyword.lower() in user_lower:
                        return True, question.explanation
            return False, question.explanation
        
        elif question.question_type in [QuestionType.SHORT_ANSWER, QuestionType.SCENARIO, 
                                        QuestionType.CALCULATION, QuestionType.INTERPRETATION, 
                                        QuestionType.ANALYSIS]:
            # For open-ended questions, check for keywords
            user_lower = user_answer.lower()
            if question.keywords:
                matches = sum(1 for keyword in question.keywords if keyword.lower() in user_lower)
                # Require at least 2-3 keyword matches for partial credit
                threshold = max(2, len(question.keywords) // 2)
                if matches >= threshold:
                    return True, question.explanation
                elif matches > 0:
                    return False, f"Your answer is on the right track but could be more complete. {question.explanation}"
            # If no keywords, provide explanation anyway (instructor review)
            return None, question.explanation
        
        return False, question.explanation
    
    def _display_question(self, question: Question):
        """Display a question to the user."""
        print("\n" + "="*80)
        print(f"Question {question.number} (Level {question.level}) - {question.section}")
        print("="*80)
        print(f"\n{question.question_text}\n")
        
        if question.options:
            for option in question.options:
                print(option)
            print("\nEnter your answer (A, B, C, or D): ", end="")
        elif question.question_type == QuestionType.TRUE_FALSE:
            print("Enter your answer (True/False): ", end="")
        elif question.question_type == QuestionType.FILL_IN:
            print("Fill in the blank: ", end="")
        else:
            print("Enter your answer: ", end="")
    
    def _get_user_input(self) -> Optional[str]:
        """Get and validate user input."""
        while True:
            try:
                answer = input().strip()
                if answer:
                    return answer
                print("Please enter an answer: ", end="")
            except (EOFError, KeyboardInterrupt):
                print("\n\nQuiz interrupted. Exiting...")
                return None
    
    def run_quiz(self, shuffle: bool = False):
        """Run the complete quiz."""
        # Display quiz title and metadata
        title = self.quiz_metadata.get('title', 'Interactive Quiz')
        description = self.quiz_metadata.get('description', '')
        
        print("\n" + "="*80)
        print(title.upper())
        print("="*80)
        
        if description:
            print(f"\n{description}")
        
        print("\nInstructions:")
        print("- Answer each question to the best of your ability")
        print("- For multiple choice: Enter A, B, C, or D")
        print("- For True/False: Enter True or False (or T/F, Yes/No)")
        print("- For open-ended questions: Provide a thoughtful answer")
        print("- You'll receive immediate feedback after each question")
        print(f"\nTotal questions: {self.total_questions}")
        print("\nPress Enter to begin...")
        input()
        
        questions_to_ask = self.questions.copy()
        if shuffle:
            random.shuffle(questions_to_ask)
        
        for i, question in enumerate(questions_to_ask, 1):
            self._display_question(question)
            user_answer = self._get_user_input()
            
            if user_answer is None:
                break
            
            self.user_answers[question.number] = user_answer
            self.correct_answers[question.number] = question.correct_answer
            
            # Check answer
            is_correct, explanation = self._check_answer(question, user_answer)
            
            print("\n" + "-"*80)
            if is_correct is True:
                print("✓ CORRECT!")
                self.score += 1
            elif is_correct is False:
                print("✗ INCORRECT")
                if question.correct_answer:
                    print(f"Correct answer: {question.correct_answer}")
            else:
                print("? REVIEW NEEDED (Open-ended question - check explanation)")
                # Give partial credit for attempting
                self.score += 0.5
            
            print(f"\nExplanation:\n{explanation}")
            print("-"*80)
            
            if i < len(questions_to_ask):
                print("\nPress Enter to continue to next question...")
                input()
        
        self._show_results()
    
    def _show_results(self):
        """Display quiz results."""
        print("\n" + "="*80)
        print("QUIZ RESULTS")
        print("="*80)
        
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        print(f"\nScore: {self.score:.1f} / {self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            grade = "A (Excellent!)"
        elif percentage >= 80:
            grade = "B (Good job!)"
        elif percentage >= 70:
            grade = "C (Satisfactory)"
        elif percentage >= 60:
            grade = "D (Needs improvement)"
        else:
            grade = "F (Review required)"
        
        print(f"Grade: {grade}")
        
        # Show breakdown by section
        print("\n" + "-"*80)
        print("Breakdown by Section:")
        print("-"*80)
        
        sections = {}
        for q in self.questions:
            if q.section not in sections:
                sections[q.section] = {'total': 0, 'correct': 0}
            sections[q.section]['total'] += 1
            # Check if this question was answered correctly
            if q.number in self.user_answers:
                is_correct, _ = self._check_answer(q, self.user_answers[q.number])
                if is_correct is True:
                    sections[q.section]['correct'] += 1
                elif is_correct is None:
                    sections[q.section]['correct'] += 0.5
        
        for section, stats in sections.items():
            section_pct = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"{section}: {stats['correct']:.1f}/{stats['total']} ({section_pct:.1f}%)")
        
        print("\n" + "="*80)
        print("Thank you for taking the quiz!")
        print("Review the explanations to reinforce your understanding.")
        print("="*80 + "\n")


def main():
    """Main entry point for the quiz application."""
    # Get JSON file path from command line argument or use default
    json_file = None
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        if not os.path.exists(json_file):
            print(f"Error: File not found: {json_file}", file=sys.stderr)
            sys.exit(1)
    
    try:
        quiz = Quiz(json_file_path=json_file)
    except Exception as e:
        print(f"Error loading quiz: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Ask if user wants to shuffle questions
    print("Would you like to shuffle the questions? (y/n): ", end="")
    try:
        shuffle_choice = input().strip().lower()
        shuffle = shuffle_choice in ['y', 'yes']
    except (EOFError, KeyboardInterrupt):
        shuffle = False
    
    quiz.run_quiz(shuffle=shuffle)


if __name__ == "__main__":
    main()
