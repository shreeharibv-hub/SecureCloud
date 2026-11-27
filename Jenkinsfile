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
                bat 'if not exist reports mkdir reports'
                bat 'python -m pytest tests/ --junitxml=reports/test-results.xml'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'python -m pip install bandit'
                bat 'python -m bandit -r app -ll -s B104'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t securecloud:latest .'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'reports/*.xml', fingerprint: true
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
