# Email Spam Classifier

## Overview
The Email Spam Classifier is a Flask-based web application designed to predict whether an email is spam or not using a machine learning model trained on text data.

## Deployment
The application is deployed on Render and can be accessed here:
[Email Spam Classifier](https://email-spaam-classifier.onrender.com)

## Project Structure
```
├── app.py                # Main Flask application
├── classifier            # Contains prediction logic
│   ├── __init__.py
│   ├── predict.py        # Function to classify email text
├── templates             # HTML templates for UI
│   ├── index.html
├── model.pkl             # Pre-trained ML model
├── vectorizer.pkl        # TfidfVectorizer for text processing
├── spam.csv              # Dataset used for training
├── requirements.txt      # Required dependencies
├── runtime.txt           # Python runtime specification
├── Procfile              # Deployment configuration
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.13.1
- Flask
- Scikit-learn
- Pandas
- Numpy
- NLTK

### Installation Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd email-spam-classifier
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open `http://127.0.0.1:5000/` in your browser to access the application.

## Usage Instructions
- Enter an email text in the provided input box.
- Click the "Predict" button.
- The application will classify the email as either "Spam" or "Not Spam."

## API Reference
### Endpoint: `POST /predict`
#### Request:
```json
{
  "email_text": "Win a free iPhone now! Click here to claim."
}
```
#### Response:
```json
{
  "prediction": "Spam"
}
```

## Deployment Details
This project is deployed on Render. The `Procfile` and `runtime.txt` files ensure a smooth deployment process.

## License
This project is licensed under the MIT License. Feel free to contribute and enhance its functionality.

