from flask import Flask, render_template, request, jsonify
import pickle
import os
from classifier.predict import classify_email

app = Flask(__name__)

# Load the trained model and vectorizer
model_path = "model.pkl"
vectorizer_path = "vectorizer.pkl"

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    with open(vectorizer_path, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
else:
    model = None
    vectorizer = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None or vectorizer is None:
        return jsonify({"error": "Model or vectorizer not found"}), 500

    email_text = request.form["email_text"]
    prediction = classify_email(email_text, model, vectorizer)

    result = "Spam" if prediction == 1 else "Not Spam"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
