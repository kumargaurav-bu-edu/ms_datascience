#!/usr/bin/env python3

"""
Vector Fundamentals Quiz (Week 9)

Learning objectives tested:
- Recognize and describe vectors including magnitude and direction
- Implement basic vector/scalar and vector/vector operations (addition, multiplication)
- Recognize problems (incl. linear regression) formulated as vector/matrix multiplication
- Recognize common vector similarity measures
- Calculate common vector similarity measures

Run: python vector_quiz.py
"""

from __future__ import annotations

import math
import random
from typing import Dict, List, Tuple, Callable, Any


# ---------- Vector utilities (no external deps) ----------
def dot(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def norm(a: List[float]) -> float:
    return math.sqrt(dot(a, a))


def cosine_similarity(a: List[float], b: List[float]) -> float:
    na = norm(a)
    nb = norm(b)
    if na == 0 or nb == 0:
        raise ValueError("Cosine similarity undefined for zero vector")
    c = dot(a, b) / (na * nb)
    # numeric guard
    return max(-1.0, min(1.0, c))


def unit_vector(a: List[float]) -> List[float]:
    n = norm(a)
    if n == 0:
        raise ValueError("Zero vector has no direction")
    return [x / n for x in a]


def is_close(x: float, y: float, atol: float = 1e-6) -> bool:
    return abs(x - y) <= atol


# ---------- Quiz engine ----------
class Question:
    def __init__(self, prompt: str, qtype: str, answer: Any, explanation: str, options: Dict[str, str] | None = None, tol: float = 1e-6):
        self.prompt = prompt
        self.qtype = qtype  # 'mcq', 'multi', 'bool', 'num'
        self.answer = answer
        self.explanation = explanation
        self.options = options or {}
        self.tol = tol

    def ask(self) -> Tuple[bool, str]:
        print("\n----")
        print(self.prompt)
        if self.qtype in {"mcq", "multi"} and self.options:
            for key in sorted(self.options.keys()):
                print(f"  {key}) {self.options[key]}")
        user = input("Your answer: ").strip()

        try:
            if self.qtype == "mcq":
                correct = str(self.answer).strip().lower()
                ok = user.lower() == correct
                return ok, self.explanation
            elif self.qtype == "multi":
                # multiple select: answers as comma-separated letters
                expected = {s.strip().lower() for s in self.answer}
                got = {s.strip().lower() for s in user.replace(";", ",").split(",") if s.strip()}
                ok = got == expected
                return ok, self.explanation
            elif self.qtype == "bool":
                expected = str(self.answer).lower() in {"true", "t", "1", "yes"}
                got = user.lower() in {"true", "t", "1", "yes"}
                return got == expected, self.explanation
            elif self.qtype == "num":
                val = float(user)
                ok = is_close(val, float(self.answer), self.tol)
                return ok, self.explanation
            else:
                return False, "Unsupported question type"
        except Exception as e:
            return False, f"Input error: {e}. {self.explanation}"


def build_questions() -> List[Question]:
    pi = math.pi
    questions: List[Question] = []

    # 1. Magnitude recognition
    questions.append(Question(
        prompt="1) What is the magnitude of the vector [3, 4]?",
        qtype="mcq",
        answer="a",
        options={
            "a": "5",
            "b": "7",
            "c": "25",
            "d": "3.5",
        },
        explanation="Magnitude = sqrt(3^2 + 4^2) = 5.",
    ))

    # 2. Dot product calculation
    questions.append(Question(
        prompt="2) Compute the dot product [1, 2, 3] · [4, 5, 6] (enter a number)",
        qtype="num",
        answer=32.0,
        tol=1e-9,
        explanation="Dot = 1*4 + 2*5 + 3*6 = 32.",
    ))

    # 3. Cosine similarity orthogonal
    questions.append(Question(
        prompt="3) Cosine similarity between [1,0,0] and [0,1,0] (enter a number)",
        qtype="num",
        answer=0.0,
        tol=1e-9,
        explanation="Orthogonal vectors have cos similarity 0.",
    ))

    # 4. Scalar-vector vs vector-vector
    questions.append(Question(
        prompt="4) Which is a scalar–vector product?",
        qtype="mcq",
        answer="b",
        options={
            "a": "[1,2] + [3,4]",
            "b": "3 * [1,2]",
            "c": "[1,2] × [3,4]",
            "d": "[1,2] · [3,4]",
        },
        explanation="Multiplying a vector by a scalar (3*[1,2]) is scalar–vector product.",
    ))

    # 5. Unit vector component
    u = unit_vector([3.0, 4.0])
    questions.append(Question(
        prompt="5) The x-component of the unit vector in direction of [3,4] (enter a number)",
        qtype="num",
        answer=u[0],
        tol=1e-6,
        explanation="Unit vector is [3/5, 4/5]; x = 0.6.",
    ))

    # 6. Linear regression formulation recognition
    questions.append(Question(
        prompt=(
            "6) Which statements reflect linear regression as vector/matrix multiplication?\n"
            "   Select all that apply (comma-separated letters)."
        ),
        qtype="multi",
        answer={"a", "c"},
        options={
            "a": "y = Xβ + ε",
            "b": "y = β / X",
            "c": "Predictions: y_hat = Xβ",
            "d": "β = X + y",
        },
        explanation="Linear regression uses y ≈ Xβ; predictions are y_hat = Xβ.",
    ))

    # 7. Polar to Cartesian
    questions.append(Question(
        prompt="7) For polar (r,θ) = (1, π/2), what is x? (enter a number)",
        qtype="num",
        answer=0.0,
        tol=1e-6,
        explanation="x = r cosθ = cos(π/2) = 0.",
    ))

    # 8. Similarity measures recognition
    questions.append(Question(
        prompt="8) Which measure is direction-only (ignores magnitude)?",
        qtype="mcq",
        answer="c",
        options={
            "a": "Euclidean distance",
            "b": "Dot product",
            "c": "Cosine similarity",
            "d": "Manhattan distance",
        },
        explanation="Cosine similarity depends only on angle (direction).",
    ))

    # 9. Orthogonality True/False
    questions.append(Question(
        prompt="9) True/False: [1,0,1] is orthogonal to [0,1,0].",
        qtype="bool",
        answer=True,
        explanation="Dot = 1*0 + 0*1 + 1*0 = 0 ⇒ orthogonal.",
    ))

    # 10. Scalar projection/simple component
    questions.append(Question(
        prompt=(
            "10) Scalar projection of v=[2,2,0] onto the x-axis unit vector is (enter a number)"
        ),
        qtype="num",
        answer=2.0,
        tol=1e-9,
        explanation="Unit x is [1,0,0]; projection is v·ux = 2.",
    ))

    # 11. Dot product numeric
    questions.append(Question(
        prompt="11) Compute [2, -1, 0] · [1, 4, 3] (enter a number)",
        qtype="num",
        answer=-2.0,
        tol=1e-9,
        explanation="2*1 + (-1)*4 + 0*3 = -2.",
    ))

    # 12. Norm numeric
    questions.append(Question(
        prompt="12) ||[0, -5, 12]|| (enter a number)",
        qtype="num",
        answer=13.0,
        tol=1e-9,
        explanation="sqrt(0^2 + (-5)^2 + 12^2) = 13.",
    ))

    # 13. Cosine equals dot of unit vectors
    questions.append(Question(
        prompt="13) dot(u_hat, v_hat) equals which quantity?",
        qtype="mcq",
        answer="a",
        options={
            "a": "cos(theta)",
            "b": "sin(theta)",
            "c": "1",
            "d": "0",
        },
        explanation="By definition, cos similarity = dot of unit vectors.",
    ))

    # 14. Orthogonal implies cosine 0 (boolean)
    questions.append(Question(
        prompt="14) True/False: If u ⟂ v then cosine similarity is 0.",
        qtype="bool",
        answer=True,
        explanation="Orthogonality implies zero dot ⇒ zero cosine.",
    ))

    # 15. Euclidean distance numeric
    questions.append(Question(
        prompt="15) Euclidean distance between [1,2] and [4,6] (enter a number)",
        qtype="num",
        answer=5.0,
        tol=1e-9,
        explanation="sqrt((4-1)^2 + (6-2)^2) = 5.",
    ))

    # 16. Manhattan distance MCQ
    questions.append(Question(
        prompt="16) Manhattan (L1) distance between [1,2] and [4,6] is",
        qtype="mcq",
        answer="c",
        options={
            "a": "4",
            "b": "6",
            "c": "7",
            "d": "5",
        },
        explanation="|4-1| + |6-2| = 3 + 4 = 7.",
    ))

    # 17. Shapes in regression
    questions.append(Question(
        prompt=(
            "17) If X has shape (100, 3), which is the shape of β for y_hat = Xβ?"
        ),
        qtype="mcq",
        answer="b",
        options={
            "a": "(100,)",
            "b": "(3,)",
            "c": "(3, 100)",
            "d": "(100, 100)",
        },
        explanation="β must have 3 entries to match X's columns.",
    ))

    # 18. Projection numeric
    questions.append(Question(
        prompt="18) Component of v=[3,4,0] along unit y-axis (enter a number)",
        qtype="num",
        answer=4.0,
        tol=1e-9,
        explanation="Unit y is [0,1,0]; v·uy = 4.",
    ))

    # 19. Cosine similarity numeric
    cs_19 = cosine_similarity([1, 1, 0], [2, 0, 0])
    questions.append(Question(
        prompt="19) cos sim between [1,1,0] and [2,0,0] (enter a number)",
        qtype="num",
        answer=cs_19,
        tol=1e-6,
        explanation="(1*2 + 1*0)/(sqrt(2)*2) = 1/√2.",
    ))

    # 20. Orthogonal pair MCQ
    questions.append(Question(
        prompt="20) Which pair is orthogonal?",
        qtype="mcq",
        answer="a",
        options={
            "a": "[1,1] and [1,-1]",
            "b": "[1,0] and [1,1]",
            "c": "[2,2] and [2,2]",
            "d": "[0,1] and [0,1]",
        },
        explanation="Dot([1,1],[1,-1]) = 1-1 = 0.",
    ))

    # 21. Unit vector component numeric
    questions.append(Question(
        prompt="21) First component of unit([0,3,4]) (enter a number)",
        qtype="num",
        answer=0.0,
        tol=1e-9,
        explanation="Unit vector preserves zeros; x-component is 0.",
    ))

    # 22. Scaling flips direction bool
    questions.append(Question(
        prompt="22) True/False: Scaling a vector by a negative scalar flips its direction.",
        qtype="bool",
        answer=True,
        explanation="Negative scaling reverses direction.",
    ))

    # 23. Projection magnitude numeric (different values)
    questions.append(Question(
        prompt="23) Projection of v=[-3,4] onto unit x-axis (enter a number)",
        qtype="num",
        answer=-3.0,
        tol=1e-9,
        explanation="Unit x is [1,0]; v·ux = -3.",
    ))

    # 24. L1 norm naming MCQ
    questions.append(Question(
        prompt="24) L1 norm is also known as",
        qtype="mcq",
        answer="b",
        options={
            "a": "Euclidean",
            "b": "Manhattan",
            "c": "Chebyshev",
            "d": "Hamming",
        },
        explanation="L1 = Manhattan; L2 = Euclidean; L∞ = Chebyshev.",
    ))

    # 25. Angle between vectors numeric
    angle_25 = math.acos(max(-1.0, min(1.0, cosine_similarity([1, 0], [1, 1]))))
    questions.append(Question(
        prompt="25) Angle between [1,0] and [1,1] in radians (enter a number)",
        qtype="num",
        answer=angle_25,
        tol=1e-6,
        explanation="arccos( (1)/(1*√2) ) = π/4.",
    ))

    # 26. Norm of unit vector MCQ
    questions.append(Question(
        prompt="26) The norm of any unit vector is",
        qtype="mcq",
        answer="b",
        options={
            "a": "0",
            "b": "1",
            "c": "-1",
            "d": "arbitrary",
        },
        explanation="By definition, unit vectors have norm 1.",
    ))

    # 27. Regression predictions expression MCQ
    questions.append(Question(
        prompt="27) Which expression gives linear regression predictions?",
        qtype="mcq",
        answer="a",
        options={
            "a": "Xβ",
            "b": "βX",
            "c": "X + β",
            "d": "X ⊙ β (Hadamard)",
        },
        explanation="Predictions y_hat = Xβ.",
    ))

    # 28. Dot of same unit vector is 1 numeric
    uu = unit_vector([3.0, 4.0])
    questions.append(Question(
        prompt="28) dot(u, u) for u = unit([3,4]) (enter a number)",
        qtype="num",
        answer=dot(uu, uu),
        tol=1e-9,
        explanation="Any unit vector dotted with itself equals 1.",
    ))

    # 29. Opposite direction cosine numeric
    questions.append(Question(
        prompt="29) cos sim between [1,0] and [-1,0] (enter a number)",
        qtype="num",
        answer=-1.0,
        tol=1e-9,
        explanation="Opposite unit directions ⇒ cosine = -1.",
    ))

    # 30. Vector-scalar product dimension MCQ
    questions.append(Question(
        prompt="30) The result of k·v (k scalar, v vector) has",
        qtype="mcq",
        answer="a",
        options={
            "a": "the same dimension as v",
            "b": "double the dimension",
            "c": "is a scalar",
            "d": "is undefined",
        },
        explanation="Scalar multiplication preserves vector dimension.",
    ))

    return questions


def print_objectives():
    print("""
Learning objectives
- Recognize and describe vectors (magnitude, direction)
- Implement basic vector/vector and vector/scalar operations
- Recognize linear regression as matrix multiplication (y ≈ Xβ)
- Recognize common vector similarity measures
- Calculate cosine similarity and related quantities
""".strip())


def main():
    print("Vector Fundamentals Quiz (Week 9)")
    print_objectives()
    print("\nInstructions: Answer MCQ with option letter, multi-select as comma-separated letters,"
          " booleans as True/False, and numeric answers as numbers.")

    questions = build_questions()
    random.shuffle(questions)

    score = 0
    total = len(questions)
    results: List[Tuple[bool, str]] = []

    for q in questions:
        ok, explanation = q.ask()
        results.append((ok, explanation))
        if ok:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Incorrect.")
            print("Explanation:", explanation)

    print("\n==== Summary ====")
    print(f"Score: {score}/{total} ({(100.0*score/total):.1f}%)")


if __name__ == "__main__":
    main()


