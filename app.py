from flask import Flask, request, jsonify, render_template
import joblib
import re
import nltk
from nltk.corpus import stopwords
import numpy as np

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Load pre-trained model and vectorizer
try:
    model = joblib.load("hate_speech_svm_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    print(" Model and vectorizer loaded successfully!")
except Exception as e:
    print(f" Error loading model: {e}")
    model, vectorizer = None, None  # Prevent crashes if model loading fails

# Initialize Flask app
app = Flask(__name__)

def preprocess_text(text):
    """Function to clean and preprocess input text"""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+|#\w+', '', text)  # Remove mentions and hashtags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])  # Remove stopwords
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure request contains JSON
        if not request.is_json:
            return jsonify({"error": "Request must be in JSON format"}), 400

        # Get JSON data
        data = request.get_json()
        text = data.get("text", "").strip()

        # Validate input
        if not text:
            return jsonify({"error": "No text provided for prediction"}), 400

        # Check if model is loaded
        if model is None or vectorizer is None:
            return jsonify({"error": "Model not loaded properly"}), 500

        # Preprocess and vectorize input text
        processed_text = preprocess_text(text)
        text_vectorized = vectorizer.transform([processed_text])
        
        # Make prediction with probability
        prediction = model.predict(text_vectorized)[0]
        probability = model.predict_proba(text_vectorized)[0][prediction]

        # Assign label based on confidence score
        result = "Hate Speech" if prediction == 1 else "Not Hate Speech"

        return jsonify({
            "text": text,
            "prediction": result,
            "confidence": round(float(probability), 2)
            
        })
        

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return error message

if __name__ == '__main__':
    
    app.run(debug=True)
