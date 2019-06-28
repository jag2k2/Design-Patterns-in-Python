pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat "python --version"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}