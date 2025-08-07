# Smart AI Interview Coach

Smart AI Interview Coach is an AI-powered interactive interview preparation tool designed to help users prepare for both technical and behavioral interviews. The app evaluates spoken or written responses, provides feedback based on semantic similarity, logs user data into a MySQL database, and generates personalized topic recommendations.

## Features

- Answer Evaluation  
  Evaluate your responses against ideal answers using Sentence-BERT embeddings and cosine similarity.

- Voice Input Support  
  Upload `.wav` audio files and get transcriptions using Whisper or another speech-to-text engine.

- Personalized Recommendations  
  Based on logged user data and low-scoring responses, the system provides targeted improvement suggestions.

- User Logging  
  All evaluations, feedback, and scores are logged using a unique user identifier in a MySQL database.

- Categorized Questions  
  Questions are grouped into Personal and Technical types and shown in dropdowns for better UX and error reduction.

**Tech Stack**

- Python 3.10+
- Streamlit
- Sentence-BERT (all-MiniLM-L6-v2)
- Whisper (or compatible speech-to-text module)
- MySQL
- scikit-learn
- pandas


Folder Structure

smart-interview-coach/
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
├── README.md # This file

├── data/
│ └── ideal_answers.csv # Ideal questions and answers with categories

├── evaluator/
│ └── scorer.py # Answer scoring logic

├── recommender/
│ └── recommender.py # Feedback and recommendation system

├── speech/
│ └── transcriber.py # Voice to text module

├── models/ # Placeholder for future models
└── logs/ # Placeholder for logging or backups

**How It Works**

User selects a question from dropdown or enters it manually.
User writes or uploads their response (audio or text).
The app finds the matching ideal answer and scores the response using Sentence-BERT embeddings.
Feedback is displayed and stored in MySQL.
Recommendations are generated from recent low-scoring answers.
