pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.....'
                sh ' sh /CICD/flask_container_ci/dockerfile.sh'
                sh ' python3 /CICD/flask_container_ci/dockerimage.py'
            }
        }
        stage('Test And Deploy') {
            steps {
                echo 'Testing And Deploy'
                sh 'sh /CICD/flask_container_ci/deploy.sh'
                sh 'sh /CICD/flask_container_ci/test.sh'
            }
        }
    }
}
