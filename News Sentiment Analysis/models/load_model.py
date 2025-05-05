import joblib

# Load saved model components
model = joblib.load('xgboost_sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def clean_text(text):
    return text.lower().strip()

def predict_sentiment(title, description):
    combined_text = clean_text(title) + " " + clean_text(description)

    # Vectorize input using the same training vectorizer
    X_input = vectorizer.transform([combined_text])

    # Make prediction
    prediction = model.predict(X_input)

    # Decode numeric label back to sentiment string
    sentiment_label = label_encoder.inverse_transform(prediction)[0]

    return sentiment_label
