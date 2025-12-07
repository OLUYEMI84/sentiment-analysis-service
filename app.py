from flask import Flask, request, jsonify
from model import load_model, predict_sentiment

app = Flask(__name__)
model, tokenizer = load_model()

@app.route("/")
def home():
    return "Welcome to the Sentiment Analysis Service!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    result = predict_sentiment(model, tokenizer, text)
    return jsonify({"input": text, "sentiment": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
