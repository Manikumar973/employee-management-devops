pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Employee Management Application'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Employee Management Application'
            }
        }
    }
}