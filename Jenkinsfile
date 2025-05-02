pipeline {
    agent any

    environment {
        PYTHON_PATH = '/usr/bin/python3'
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh """
                    ${PYTHON_PATH} -m venv ${VIRTUAL_ENV}
                    . ${VIRTUAL_ENV}/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Lint') {
            steps {
                sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    pylint --ignore=test_*.py app.py
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                    . ${VIRTUAL_ENV}/bin/activate
                    pytest test_app.py -v
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    # Kill any existing Flask process
                    pkill -f "python3 app.py" || true
                    
                    # Start the application in the background
                    . ${VIRTUAL_ENV}/bin/activate
                    nohup python3 app.py > app.log 2>&1 &
                    
                    # Wait for the application to start
                    sleep 5
                    
                    # Check if the application is running
                    curl -s http://localhost:8000> /dev/null || exit 1
                """
            }
        }

        stage('Run Flask App and Prometheus') {
            steps {
                echo 'Starting Flask App and Prometheus...'
                sh 'nohup python3 app.py > flask_app.log 2>&1 &'
                sh 'nohup prometheus --config.file=prometheus.yml > prometheus.log 2>&1 &'

                // Wait for Flask App to start
                sh 'sleep 5'

                // Check if Flask App is running
                sh 'curl -s http://localhost:8000 > /dev/null || (echo "Flask App failed to start" && exit 1)'

                // Check if Prometheus is running
                sh 'curl -s http://localhost:9090 > /dev/null || (echo "Prometheus failed to start" && exit 1)'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}