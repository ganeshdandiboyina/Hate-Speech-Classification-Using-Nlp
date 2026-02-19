📁 Project Folder Structure

hate-speech-classification/ 🚫🧠
│
├── 📂 data/
│   └── dataset.csv 📄
│      → Contains labeled text data (Hate Speech / Non-Hate Speech)
│
├── 📂 models/
│   ├── hate_speech_model.pkl 🤖
│   │    → Trained Machine Learning model
│   │
│   └── vectorizer.pkl 📊
│        → TF-IDF vectorizer used for text feature extraction
│
├── 📂 templates/ 🌐
│   └── index.html
│        → Frontend HTML file for user input (if using Flask UI)
│
├── 📂 static/ 🎨
│   └── style.css
│        → CSS styling for frontend
│
├── 📄 app.py 🚀
│    → Main Flask application file
│    → Loads model and predicts hate speech
│
├── 📄 train_model.py 🧠
│    → Script to train the machine learning model
│    → Saves model and vectorizer
│
├── 📄 requirements.txt 📦
│    → Contains all required Python libraries
│
├── 📄 README.md 📘
│    → Project documentation
│
└── 📄 screenshot.png 🖼 (optional)
     → Screenshot of project interface


📂 Folder Explanation (Simple)

Folder/File	       Purpose

📂 data	           Contains dataset
📂 models	         Stores trained ML model
📂 templates	     HTML frontend
📂 static	         CSS styling

app.py	Main application file
train_model.py	Model training script
requirements.txt	Dependencies
README.md	Project documentation

🧠 How Project Works Internally
User Input 📝
   ↓
Flask App (app.py) 🚀
   ↓
Load TF-IDF Vectorizer 📊
   ↓
Convert text → numerical format 🔢
   ↓
Load trained model 🤖
   ↓
Predict Hate / Non-Hate 🚫✅
   ↓
Show result to user 🌐


This structure makes your project look:

    ✅ Professional
    ✅ Recruiter-ready
    ✅ Production-level
    ✅ Easy to understand


   





