# Random Number Generator

A simple Flask application that generates random numbers with a web interface.

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Running Tests

To run the unit tests:
```bash
pytest
```

## Features

- Simple web interface to generate random numbers
- REST API endpoint at `/api/v1/generate`
- Unit tests for both the web interface and API 