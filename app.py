"""
This module provides a Flask application that generates a random number between 10000 and 100000.
"""
import random
from flask import Flask, render_template, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus counter to track requests to /api/v1/generate
REQUEST_COUNT = Counter('generate_requests_total', 'Total number of requests to /api/v1/generate')

@app.route('/')
def home():
    """
    Render the index.html template
    """
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify if /api/v1/generate is working fine
    """
    try:
        response = generate_number()
        if response.status_code == 200:
            return jsonify({'status': 'healthy'}), 200
        return jsonify({'status': 'unhealthy'}), 500
    except ValueError as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

@app.route('/api/v1/generate', methods=['GET'])
def generate_number():
    """
    Generate a random number between 10000 and 100000
    """
    REQUEST_COUNT.inc()  # Increment Prometheus counter
    number = random.randint(10000, 100000)
    return jsonify({'number': number})

@app.route('/metrics', methods=['GET'])
def metrics():
    """
    Expose Prometheus metrics
    """
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)
