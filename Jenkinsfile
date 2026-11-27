pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'SecureCloud source code checked out'
            }
        }

        stage('Environment Check') {
            steps {
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t securecloud:latest .'
            }
        }
    }

    post {
        success {
            echo 'SecureCloud CI pipeline completed successfully!'
        }

        failure {
            echo 'SecureCloud pipeline failed. Check Console Output.'
        }
    }
}
