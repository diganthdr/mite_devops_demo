from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/v1/generate', methods=['GET'])
def generate_number():
    number = random.randint(10000, 100000)
    return jsonify({'number': number})

if __name__ == '__main__':
    app.run(debug=True) 