from flask import Flask, request, jsonify
from chatbot import get_answer

app = Flask(__name__)

@app.get("/")
def home():
    return "Financial Q&A Chatbot API. Use GET/POST /ask with a 'query' parameter."

@app.route("/ask", methods=["GET", "POST"])
def ask():
    if request.method == "GET":
        user_query = request.args.get("query", "")
    else:  # POST
        data = request.get_json(silent=True) or {}
        user_query = data.get("query", "")

    answer = get_answer(user_query)
    return jsonify({"query": user_query, "answer": answer})

if __name__ == "__main__":
    # For local dev. In production, use gunicorn or similar.
    app.run(host="0.0.0.0", port=5000, debug=True)
