from flask import Flask, request, jsonify, send_from_directory
import pyttsx3
import datetime

app = Flask(__name__, static_folder=".")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Homepage
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Voice command API
@app.route("/command", methods=["POST"])
def command():
    data = request.json
    text = data["text"].lower()

    if "time" in text:
        response = datetime.datetime.now().strftime("%H:%M")

    elif "hello" in text:
        response = "Hello DK, how can I help you?"

    else:
        response = "I did not understand"

    speak(response)
    return jsonify({"response": response})

app.run(debug=True)