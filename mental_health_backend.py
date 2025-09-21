from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM


app = Flask(__name__)
CORS(app)

# Load LLaMA3 model via Ollama
llm = OllamaLLM(model="llama3")

CRISIS_TERMS = ["suicide", "self-harm", "kill myself", "end my life"]
CRISIS_MESSAGE = (
    "It sounds like you are in crisis. "
    "Please contact a trained professional immediately. "
    "In India, you can call the Vandrevala Helpline: 1860 266 2345 or 9152987821."
)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Crisis keyword safety
    if any(term in user_message for term in CRISIS_TERMS):
        return jsonify({"reply": CRISIS_MESSAGE})

    # Get response from LLaMA3
    reply = llm(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
