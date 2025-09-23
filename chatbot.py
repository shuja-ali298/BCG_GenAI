
---

# chatbot.py

```python
# chatbot.py
from difflib import get_close_matches

# Canonical Q&A pairs (edit/extend freely)
QA_PAIRS = {
    "what is the total revenue?": "The total revenue is $198 billion.",
    "how has net income changed over the last year?": "Net income increased by 12% over the last year.",
    "what are the total assets?": "Total assets are $411 billion.",
    "what is the cash flow from operating activities?": "Cash flow from operating activities is $92 billion.",
}

# Optional aliases → canonical forms (helps normalize phrasing)
ALIAS = {
    "whats the total revenue?": "what is the total revenue?",
    "total revenue?": "what is the total revenue?",
    "revenue?": "what is the total revenue?",
    "net income change?": "how has net income changed over the last year?",
    "operating cash flow?": "what is the cash flow from operating activities?",
    "cash from ops?": "what is the cash flow from operating activities?",
    "assets?": "what are the total assets?",
}

def normalize(q: str) -> str:
    return (q or "").strip().lower()

def get_answer(user_query: str) -> str:
    q = normalize(user_query)

    # Direct hit via alias map
    if q in ALIAS:
        q = ALIAS[q]

    # Exact match
    if q in QA_PAIRS:
        return QA_PAIRS[q]

    # Fuzzy match (closest of known keys)
    keys = list(QA_PAIRS.keys())
    match = get_close_matches(q, keys, n=1, cutoff=0.75)
    if match:
        return QA_PAIRS[match[0]]

    return "Sorry, I can only answer a few predefined finance questions (revenue, net income change, assets, operating cash flow)."

if __name__ == "__main__":
    print("Financial Q&A Chatbot — type 'exit' to quit.")
    while True:
        user_input = input("> ")
        if user_input.strip().lower() == "exit":
            break
        print(get_answer(user_input))
