from classifier.preprocess import preprocess_text

def classify_email(email_text, model, vectorizer):
    processed_text = preprocess_text(email_text)
    transformed_text = vectorizer.transform([processed_text])
    prediction = model.predict(transformed_text)[0]
    return prediction
