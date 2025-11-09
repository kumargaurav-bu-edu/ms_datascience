"""
Quiz Generator for Clustering Concepts
Generates 30 multiple choice questions based on clustering, similarity, 
cluster descriptions, and intelligibility concepts.
"""

import json
import random

class QuizGenerator:
    def __init__(self):
        self.questions = []
        
    def generate_questions(self):
        """Generate 30 multiple choice questions"""
        
        # Question 1: Basic clustering definition
        self.questions.append({
            "id": 1,
            "question": "What is clustering in data science?",
            "options": [
                "A supervised learning technique that predicts labels for new data points",
                "An unsupervised learning technique that groups similar data points together",
                "A regression technique that predicts continuous values",
                "A classification technique that assigns data to predefined categories"
            ],
            "correct": "B",
            "explanation": "Clustering is an unsupervised learning technique that groups similar data points together without predefined labels."
        })
        
        # Question 2: Why use circles for clusters
        self.questions.append({
            "id": 2,
            "question": "Why might it sometimes be better to use circles rather than irregular shapes to define clusters?",
            "options": [
                "Circles are computationally faster to calculate",
                "Circular clusters are more intuitive and easier to interpret, especially when using distance-based metrics like Euclidean distance",
                "Irregular shapes are not allowed in clustering algorithms",
                "Circles provide more accurate clustering results for all datasets"
            ],
            "correct": "B",
            "explanation": "Circular clusters are often preferred because they align with distance-based metrics like Euclidean distance and are more interpretable."
        })
        
        # Question 3: Distance metrics
        self.questions.append({
            "id": 3,
            "question": "Which distance metric is most commonly used in k-means clustering?",
            "options": [
                "Manhattan distance",
                "Euclidean distance",
                "Cosine similarity",
                "Hamming distance"
            ],
            "correct": "B",
            "explanation": "Euclidean distance is the default and most commonly used distance metric in k-means clustering."
        })
        
        # Question 4: K-means algorithm
        self.questions.append({
            "id": 4,
            "question": "What is the main objective function that k-means clustering minimizes?",
            "options": [
                "The sum of squared distances between points and their assigned cluster centroids",
                "The maximum distance between any two points in a cluster",
                "The number of clusters",
                "The variance within each cluster"
            ],
            "correct": "A",
            "explanation": "K-means minimizes the sum of squared distances (SSE) between data points and their assigned cluster centroids."
        })
        
        # Question 5: Cluster descriptions
        self.questions.append({
            "id": 5,
            "question": "What is a cluster description and how can it be created?",
            "options": [
                "A visual representation of cluster centroids using scatter plots",
                "A summary of the characteristics that define a cluster, often created using supervised learning on cluster labels",
                "A list of all data points belonging to a cluster",
                "The statistical mean of all features in a cluster"
            ],
            "correct": "B",
            "explanation": "A cluster description summarizes the defining characteristics of a cluster. It can be created by using supervised learning techniques on the cluster labels to identify which features are most important."
        })
        
        # Question 6: Industry applications
        self.questions.append({
            "id": 6,
            "question": "What can clustering be used for in industry?",
            "options": [
                "Only for data visualization purposes",
                "Customer segmentation, anomaly detection, market research, and pattern discovery",
                "Only for predicting future sales",
                "Only for classification tasks"
            ],
            "correct": "B",
            "explanation": "Clustering has numerous industry applications including customer segmentation, anomaly detection, market research, and discovering hidden patterns in data."
        })
        
        # Question 7: Similarity measures
        self.questions.append({
            "id": 7,
            "question": "What does cosine similarity measure?",
            "options": [
                "The Euclidean distance between two points",
                "The angle between two vectors, measuring orientation rather than magnitude",
                "The Manhattan distance between two points",
                "The Hamming distance between two binary vectors"
            ],
            "correct": "B",
            "explanation": "Cosine similarity measures the cosine of the angle between two vectors, focusing on direction rather than magnitude. It's useful for text data and high-dimensional spaces."
        })
        
        # Question 8: Hierarchical clustering
        self.questions.append({
            "id": 8,
            "question": "What is a key difference between agglomerative and divisive hierarchical clustering?",
            "options": [
                "Agglomerative starts with all points as separate clusters and merges them; divisive starts with one cluster and splits it",
                "Agglomerative is faster than divisive for large datasets",
                "Divisive is always more accurate than agglomerative",
                "There is no difference between them"
            ],
            "correct": "A",
            "explanation": "Agglomerative (bottom-up) hierarchical clustering starts with each point as its own cluster and merges similar clusters. Divisive (top-down) starts with all points in one cluster and recursively splits them."
        })
        
        # Question 9: K-means initialization
        self.questions.append({
            "id": 9,
            "question": "What is a common method to improve k-means clustering results?",
            "options": [
                "Running the algorithm multiple times with different random initializations and selecting the best result",
                "Always using k=2",
                "Using only numerical features",
                "Normalizing all features to have mean 0"
            ],
            "correct": "A",
            "explanation": "K-means can converge to local minima. Running it multiple times with different random initializations (k-means++) helps find better solutions."
        })
        
        # Question 10: Intelligibility
        self.questions.append({
            "id": 10,
            "question": "What is intelligibility in the context of machine learning?",
            "options": [
                "The accuracy of a machine learning model",
                "The ability to understand and explain how a model makes decisions, which is key to building trust",
                "The computational speed of a model",
                "The number of features used in a model"
            ],
            "correct": "B",
            "explanation": "Intelligibility refers to the ability to understand and explain how a machine learning model works and makes decisions, which is crucial for building trust in ML systems."
        })
        
        # Question 11: Silhouette score
        self.questions.append({
            "id": 11,
            "question": "What does the silhouette score measure in clustering?",
            "options": [
                "The number of clusters",
                "How similar objects are to their own cluster compared to other clusters",
                "The distance between cluster centroids",
                "The variance within each cluster"
            ],
            "correct": "B",
            "explanation": "The silhouette score measures how well-separated clusters are by comparing how similar an object is to its own cluster versus other clusters. Values range from -1 to 1, with higher values indicating better clustering."
        })
        
        # Question 12: DBSCAN
        self.questions.append({
            "id": 12,
            "question": "What is a key advantage of DBSCAN over k-means clustering?",
            "options": [
                "DBSCAN requires specifying the number of clusters in advance",
                "DBSCAN can discover clusters of arbitrary shape and identify noise/outliers",
                "DBSCAN is always faster than k-means",
                "DBSCAN only works with circular clusters"
            ],
            "correct": "B",
            "explanation": "DBSCAN can find clusters of arbitrary shape and can identify outliers as noise points, unlike k-means which assumes spherical clusters."
        })
        
        # Question 13: Feature scaling
        self.questions.append({
            "id": 13,
            "question": "Why is feature scaling important in distance-based clustering algorithms?",
            "options": [
                "It makes the algorithm run faster",
                "Features with larger scales would dominate the distance calculations, making smaller-scale features less influential",
                "It reduces the number of features needed",
                "It's not important for clustering"
            ],
            "correct": "B",
            "explanation": "Without scaling, features with larger ranges (e.g., income in thousands) will dominate distance calculations over features with smaller ranges (e.g., age), leading to biased clustering results."
        })
        
        # Question 14: Cluster evaluation
        self.questions.append({
            "id": 14,
            "question": "What is the formula for calculating the Within-Cluster Sum of Squares (WCSS)?",
            "options": [
                "Σ Σ ||x - μ||² where x is a point and μ is the cluster centroid",
                "Σ (x - μ) where x is a point and μ is the mean",
                "Σ ||x₁ - x₂|| where x₁ and x₂ are points in the same cluster",
                "Σ μ² where μ is the cluster centroid"
            ],
            "correct": "A",
            "explanation": "WCSS = Σ Σ ||x - μ||² calculates the sum of squared distances from each point to its cluster centroid, summed across all clusters."
        })
        
        # Question 15: Supervised learning for cluster descriptions
        self.questions.append({
            "id": 15,
            "question": "How can supervised learning be used to generate cluster descriptions?",
            "options": [
                "By training a classifier to predict cluster labels from features, then analyzing which features are most important",
                "By using regression to predict cluster labels",
                "By applying clustering to the output of a supervised model",
                "Supervised learning cannot be used for cluster descriptions"
            ],
            "correct": "A",
            "explanation": "After clustering, you can treat cluster labels as targets and train a supervised learning model (like a decision tree or logistic regression) to identify which features best distinguish each cluster."
        })
        
        # Question 16: Elbow method
        self.questions.append({
            "id": 16,
            "question": "What is the elbow method used for in clustering?",
            "options": [
                "Determining the optimal number of clusters by finding the 'elbow' point where WCSS decreases sharply",
                "Measuring cluster quality",
                "Initializing cluster centroids",
                "Calculating distance metrics"
            ],
            "correct": "A",
            "explanation": "The elbow method plots WCSS against the number of clusters (k). The optimal k is often at the 'elbow' where the rate of decrease sharply changes."
        })
        
        # Question 17: Nearest neighbors
        self.questions.append({
            "id": 17,
            "question": "In the context of clustering, what is the relationship between similarity and neighbors?",
            "options": [
                "Similar points are those that are neighbors in the feature space",
                "Neighbors are always in different clusters",
                "Similarity and neighbors are unrelated concepts",
                "Neighbors must have identical feature values"
            ],
            "correct": "A",
            "explanation": "Points that are similar (close in distance or high in similarity) are neighbors in the feature space and are typically grouped into the same cluster."
        })
        
        # Question 18: Real-world problem solving
        self.questions.append({
            "id": 18,
            "question": "How can multiple datasets be used to address a real-world problem using clustering?",
            "options": [
                "By combining datasets to identify patterns across different data sources and create comprehensive insights",
                "By using only the largest dataset",
                "By clustering each dataset separately without integration",
                "Multiple datasets cannot be used together for clustering"
            ],
            "correct": "A",
            "explanation": "Multiple datasets can be integrated to provide richer feature sets, enabling more comprehensive clustering that reveals patterns across different data sources and dimensions."
        })
        
        # Question 19: Trust in ML
        self.questions.append({
            "id": 19,
            "question": "Why is intelligibility a key component to trust in machine learning?",
            "options": [
                "It makes models run faster",
                "Users and stakeholders need to understand how models make decisions to trust and adopt them, especially in critical applications",
                "It increases model accuracy",
                "It reduces computational costs"
            ],
            "correct": "B",
            "explanation": "Intelligibility enables users to understand model behavior, validate decisions, identify biases, and trust the system, which is essential for adoption in business and critical applications."
        })
        
        # Question 20: K-means convergence
        self.questions.append({
            "id": 20,
            "question": "What does k-means clustering converge to?",
            "options": [
                "A global optimum solution",
                "A local optimum that minimizes within-cluster sum of squares",
                "The true number of clusters in the data",
                "A solution with maximum inter-cluster distance"
            ],
            "correct": "B",
            "explanation": "K-means converges to a local optimum (not necessarily global) that minimizes the within-cluster sum of squares. Multiple runs with different initializations help find better solutions."
        })
        
        # Question 21: Cluster validation
        self.questions.append({
            "id": 21,
            "question": "What is the difference between internal and external cluster validation?",
            "options": [
                "Internal validation uses ground truth labels; external validation does not",
                "Internal validation evaluates clustering without ground truth (e.g., silhouette score); external validation uses known labels (e.g., adjusted Rand index)",
                "Internal validation is always more accurate",
                "There is no difference"
            ],
            "correct": "B",
            "explanation": "Internal validation (silhouette, Davies-Bouldin) evaluates clustering quality without ground truth. External validation (adjusted Rand index, F-measure) compares clusters to known labels."
        })
        
        # Question 22: Customer segmentation
        self.questions.append({
            "id": 22,
            "question": "In customer segmentation using clustering, what types of features are typically used?",
            "options": [
                "Only demographic features",
                "Demographic, behavioral, and transactional features combined",
                "Only purchase history",
                "Only geographic location"
            ],
            "correct": "B",
            "explanation": "Effective customer segmentation uses a combination of demographic (age, income), behavioral (purchase frequency, website visits), and transactional (spending amounts) features."
        })
        
        # Question 23: Manhattan distance
        self.questions.append({
            "id": 23,
            "question": "What is the formula for Manhattan distance between two points (x₁, y₁) and (x₂, y₂)?",
            "options": [
                "|x₁ - x₂| + |y₁ - y₂|",
                "√((x₁ - x₂)² + (y₁ - y₂)²)",
                "|x₁ - x₂|² + |y₁ - y₂|²",
                "(x₁ - x₂) + (y₁ - y₂)"
            ],
            "correct": "A",
            "explanation": "Manhattan distance (L1 norm) is the sum of absolute differences: |x₁ - x₂| + |y₁ - y₂|. It measures distance along grid lines, like city blocks."
        })
        
        # Question 24: Centroid calculation
        self.questions.append({
            "id": 24,
            "question": "How is a cluster centroid calculated in k-means clustering?",
            "options": [
                "As the median of all points in the cluster",
                "As the mean (average) of all points in the cluster",
                "As the point closest to all other points in the cluster",
                "As a randomly selected point in the cluster"
            ],
            "correct": "B",
            "explanation": "The cluster centroid is the mean (average) of all points assigned to that cluster. It's recalculated in each iteration of k-means."
        })
        
        # Question 25: Anomaly detection
        self.questions.append({
            "id": 25,
            "question": "How can clustering be used for anomaly detection?",
            "options": [
                "By identifying points that don't belong to any cluster or belong to very small clusters",
                "By clustering only normal data points",
                "By using only k=1",
                "Clustering cannot be used for anomaly detection"
            ],
            "correct": "A",
            "explanation": "Anomalies are often points that are far from cluster centroids, don't belong to any cluster (in DBSCAN), or form very small clusters, making clustering effective for anomaly detection."
        })
        
        # Question 26: Feature importance in clusters
        self.questions.append({
            "id": 26,
            "question": "When creating cluster descriptions using supervised learning, what technique helps identify which features are most important for each cluster?",
            "options": [
                "Feature scaling",
                "Feature importance scores from tree-based models or coefficients from linear models",
                "Removing features with low variance",
                "Using only categorical features"
            ],
            "correct": "B",
            "explanation": "Supervised learning models (decision trees, random forests, logistic regression) provide feature importance scores or coefficients that indicate which features best distinguish each cluster."
        })
        
        # Question 27: Cluster interpretability
        self.questions.append({
            "id": 27,
            "question": "What makes a cluster description more interpretable?",
            "options": [
                "Using only numerical features",
                "Using simple, understandable rules (e.g., 'high income AND frequent purchases') rather than complex mathematical formulas",
                "Using as many features as possible",
                "Using only binary features"
            ],
            "correct": "B",
            "explanation": "Interpretable cluster descriptions use simple, human-understandable rules (often from decision trees) that clearly explain cluster characteristics, making them more actionable for business users."
        })
        
        # Question 28: Hierarchical clustering linkage
        self.questions.append({
            "id": 28,
            "question": "What are the common linkage criteria in hierarchical clustering?",
            "options": [
                "Single, complete, average, and Ward linkage",
                "Only Euclidean and Manhattan linkage",
                "Only k-means linkage",
                "Only centroid linkage"
            ],
            "correct": "A",
            "explanation": "Common linkage criteria include: single (minimum distance), complete (maximum distance), average (mean distance), and Ward (minimizes within-cluster variance)."
        })
        
        # Question 29: High-dimensional clustering
        self.questions.append({
            "id": 29,
            "question": "What is a challenge when clustering high-dimensional data?",
            "options": [
                "All points become equidistant, making it difficult to distinguish clusters (curse of dimensionality)",
                "Clustering algorithms don't work with more than 10 features",
                "High-dimensional data always clusters perfectly",
                "There are no challenges with high-dimensional data"
            ],
            "correct": "A",
            "explanation": "The curse of dimensionality makes distances in high-dimensional spaces less meaningful as all points become roughly equidistant, making clustering challenging. Dimensionality reduction (PCA) or feature selection can help."
        })
        
        # Question 30: Clustering in business context
        self.questions.append({
            "id": 30,
            "question": "Why is it important to create interpretable cluster descriptions for business applications?",
            "options": [
                "It makes the algorithm run faster",
                "Business stakeholders need to understand cluster characteristics to take actionable decisions and trust the results",
                "It increases the number of clusters",
                "It's not important for business applications"
            ],
            "correct": "B",
            "explanation": "Interpretable cluster descriptions enable business users to understand what each cluster represents, make informed decisions, and trust the clustering results, leading to better adoption and actionability."
        })
        
        return self.questions
    
    def save_quiz(self, filename="clustering_quiz.json"):
        """Save quiz questions to a JSON file"""
        quiz_data = {
            "title": "Clustering Concepts Quiz",
            "total_questions": len(self.questions),
            "questions": self.questions
        }
        with open(filename, 'w') as f:
            json.dump(quiz_data, f, indent=2)
        print(f"Quiz saved to {filename}")
    
    def display_quiz(self):
        """Display all quiz questions in a readable format"""
        for q in self.questions:
            print(f"\nQuestion {q['id']}: {q['question']}")
            for option in q['options']:
                print(f"  {option}")
            print(f"  Correct Answer: {q['correct']}")
            print(f"  Explanation: {q['explanation']}")
    
    def create_interactive_quiz(self, filename="clustering_quiz.py"):
        """Create an interactive Python quiz program"""
        quiz_code = '''"""
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
    
    print(f"\\n{'='*60}")
    print(f"Welcome to the Clustering Concepts Quiz!")
    print(f"Total Questions: {total}")
    print(f"{'='*60}\\n")
    
    for i, q in enumerate(questions, 1):
        print(f"\\nQuestion {i}/{total}")
        print(f"{q['question']}\\n")
        
        # Shuffle options for each question
        shuffled_options, correct_letter, correct_text = shuffle_options(q)
        
        # Display options
        for idx, option in enumerate(shuffled_options):
            letter = chr(ord('A') + idx)
            print(f"{letter}. {option}")
        
        # Get user answer
        while True:
            user_answer = input("\\nYour answer (A/B/C/D): ").upper().strip()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        # Check answer
        is_correct = user_answer == correct_letter
        if is_correct:
            score += 1
            print("\\n✓ Correct!")
        else:
            print(f"\\n✗ Incorrect. The correct answer is {correct_letter}.")
        
        print(f"Explanation: {q['explanation']}")
        
        results.append({
            'question_id': q['id'],
            'question': q['question'],
            'user_answer': user_answer,
            'correct_answer': correct_letter,
            'is_correct': is_correct
        })
        
        input("\\nPress Enter to continue...")
    
    # Display final results
    print(f"\\n{'='*60}")
    print(f"Quiz Complete!")
    print(f"{'='*60}")
    print(f"Score: {score}/{total} ({(score/total)*100:.1f}%)")
    print(f"\\nResults Summary:")
    
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
    
    print(f"\\nResults saved to quiz_results.json")

if __name__ == "__main__":
    take_quiz()
'''
        with open(filename, 'w') as f:
            f.write(quiz_code)
        print(f"Interactive quiz program saved to {filename}")

def main():
    """Main function to generate quiz"""
    generator = QuizGenerator()
    questions = generator.generate_questions()
    
    print(f"Generated {len(questions)} quiz questions")
    
    # Save to JSON
    generator.save_quiz("clustering_quiz.json")
    
    # Create interactive quiz program
    generator.create_interactive_quiz("interactive_quiz.py")
    
    print("\nQuiz files created successfully!")
    print("- clustering_quiz.json: Contains all 30 questions in JSON format")
    print("- interactive_quiz.py: Interactive quiz program you can run")
    print("\nTo take the quiz, run: python interactive_quiz.py")

if __name__ == "__main__":
    main()
