pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Building branch: ${env.BRANCH_NAME}"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build step running...'
            }
        }

        stage('Test') {
            steps {
                echo 'Test step running...'
            }
        }
    }
}
