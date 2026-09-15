pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management-app:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop employee-management-container || true'
                sh 'docker rm employee-management-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name employee-management-container employee-management-app:latest'
            }
        }

        stage('Verify Application') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000/health'
            }
        }
    }
}