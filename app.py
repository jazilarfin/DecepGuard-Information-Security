from flask import Flask, render_template, request
import tensorflow as tf
import os

app = Flask(__name__)

# -----------------------------------------------------
# MODEL SETUP
# -----------------------------------------------------
MODEL_PATH = "model/email_classifier_final.keras"

print("Looking for model at:", os.path.abspath(MODEL_PATH))
if not os.path.exists(MODEL_PATH):
    print("\n❌ ERROR: Model file NOT found!\n")
else:
    print("\n✅ Model file FOUND\n")

# Try loading the model
try:
    from tensorflow.keras.layers import TextVectorization
    model = tf.keras.models.load_model(
        MODEL_PATH,
        custom_objects={"TextVectorization": TextVectorization}
    )
    print("\n✅ Model loaded successfully!\n")
except Exception as e:
    print("\n❌ ERROR LOADING MODEL:", e, "\n")
    model = None

# -----------------------------------------------------
# CLASSIFIER FUNCTION
# -----------------------------------------------------
def classify_email(text):
    try:
        input_tensor = tf.constant([[text]], dtype=tf.string)
        prediction = model(input_tensor, training=False).numpy()[0][0]
        label = "Malicious" if prediction > 0.5 else "Legit"
        return label, float(prediction)
    except Exception as e:
        print("\n❌ ERROR during prediction:", e)
        return "Error", 0.0

# -----------------------------------------------------
# FLASK ROUTES
# -----------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    score = None
    email_text = ""  # <-- Add this to always pass to template

    if request.method == "POST":
        email_text = request.form["email"]  # <-- capture textarea text
        result, score = classify_email(email_text)

    # Pass email_text to template
    return render_template("index.html", result=result, score=score, email_text=email_text)

# -----------------------------------------------------
# RUN APP
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
