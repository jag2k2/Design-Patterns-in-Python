pipeline {
    agent any
	environment {
		MY_PYTHON="C:\\Users\\Jeff Tipps\\AppData\\Local\\Programs\\Python\\Python37-32\\"
	}
    stages {
        stage('Build') {
            steps {
                bat "\"%MY_PYTHON%\"\\python --version"
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