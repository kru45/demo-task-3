pipeline {
    agent any

    environment {
        // We map the Jenkins Secret (ID: store-discount-key) 
        // to a variable Python can read (DISCOUNT_CODE)
        DISCOUNT_CODE = credentials('store-discount-key')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls your latest code from GitHub
                checkout scm
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Verifying Discount Logic...'
                // If the math or the secret is wrong, the pipeline stops here
                sh 'python3 test_discount.py'
            }
        }

        stage('Execute Service') {
            steps {
                echo 'Tests Passed! Running Discount Service...'
                sh 'python3 discount_service.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished execution.'
        }
        success {
            echo 'The Discount Service is healthy and ready!'
        }
        failure {
            echo 'Alert: The Discount Service or Secret is mismatched!'
        }
    }
}
