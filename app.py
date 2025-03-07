from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello MLOps Assignment 1 is running!"

# New Feature: Simple function for testing
def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
