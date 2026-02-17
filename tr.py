import pandas as pd
import re
import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, classification_report

# Download necessary NLTK resources
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("C:\\Users\\ganes\\OneDrive\\Desktop\\hatespeech.csv")

# Preprocessing
def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

df["clean_tweet"] = df["tweet"].astype(str).apply(preprocess_text)

# Feature extraction
vectorizer = TfidfVectorizer(stop_words="english", max_features=8000, ngram_range=(1, 3))
X = vectorizer.fit_transform(df["clean_tweet"])
y = df["label"]

# Handle class imbalance
X_resampled, y_resampled = SMOTE(random_state=42).fit_resample(X, y)

# No need to convert to dense array here
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train LinearSVC model (works with sparse matrices)
svm_model = LinearSVC(class_weight='balanced')
svm_model.fit(X_train, y_train)

# Predict function
def predict_hate_speech(text):
    text = preprocess_text(text)
    text_vector = vectorizer.transform([text])  # No need to convert to array
    prediction = svm_model.predict(text_vector)[0]
    return "Hate Speech" if prediction == 1 else "Not Hate Speech"

# Evaluate model
y_pred = svm_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
pickle.dump(svm_model, open("svm_hate_speech_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Test predictions
sample_texts = ["I hate you", "Kills them all", "Love everyone"]
print([predict_hate_speech(text) for text in sample_texts])