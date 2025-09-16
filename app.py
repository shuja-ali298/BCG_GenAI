import pandas as pd

def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is $198 billion."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by 12% over the last year."
    elif user_query == "What are the total assets?":
        return "The total assets are $411 billion."
    elif user_query == "What is the cash flow from operating activities?":
        return "The cash flow from operating activities is $92 billion."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Test the chatbot
while True:
    user_input = input("Ask a financial question: ")
    if user_input.lower() == 'exit':
        break
    print(simple_chatbot(user_input))

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def chatbot():
    user_query = request.args.get('query', '')
    
    if user_query == "What is the total revenue?":
        return "The total revenue is $198 billion."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has increased by 12% over the last year."
    elif user_query == "What are the total assets?":
        return "The total assets are $411 billion."
    elif user_query == "What is the cash flow from operating activities?":
        return "The cash flow from operating activities is $92 billion."
    else:
        return "Sorry, I can only provide information on predefined queries."

if __name__ == "__main__":
    app.run(debug=True)