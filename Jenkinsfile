pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Environment Check') {
            steps {
                bat 'python --version'
                bat 'docker --version'
            }
        }

        stage('Inspect Project') {
            steps {
                bat 'dir'
            }
        }
    }

    post {
        success {
            echo 'SecureCloud pipeline completed successfully!'
        }

        failure {
            echo 'SecureCloud pipeline failed. Check Console Output.'
        }
    }
}
