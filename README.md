# DecepGuard – Email Phishing Detector

DecepGuard is a web-based application that detects phishing emails using a machine learning model. It allows users to paste an email’s text and instantly get a prediction of whether it is **Malicious** or **Legit**, along with a confidence score.

---

## Features

- Detects phishing emails using a trained TensorFlow model.
- Displays prediction results with a confidence percentage.
- Retains the email text after submission for easy editing.
- Clean, modern, responsive UI.

---

## Project Structure

DecepGuard/
├── app.py # Main Flask application
├── templates/
│ └── index.html # HTML template for the web app
├── model/
│ └── email_classifier_final.keras # Trained ML model
├── requirements.txt # Python dependencies
├── .gitignore # Ignore venv and cache files
└── README.md # This file

---

## Installation
Clone the repository for use
