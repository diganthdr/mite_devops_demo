"""
This module provides a Flask application that generates a random number between 10000 and 100000.
"""
import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the index.html template
    """
    return render_template('index.html')

@app.route('/api/v1/generate', methods=['GET'])
def generate_number():
    """
    Generate a random number between 10000 and 100000
    """
    number = random.randint(10000, 100000)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(port=8888, debug=True)
