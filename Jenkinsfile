pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.....'
                sh ' sh /jenkins-pipeline/flask_container_ci/dockerfile.sh'
                sh ' python3 /jenkins-pipeline/flask_container_ci/dockerimage.py'
            }
        }
        stage('Test And Deploy') {
            steps {
                echo 'Testing And Deploy'
                sh 'sh /jenkins-pipeline/flask_container_ci/deploy.sh'
                sh 'sh /jenkins-pipeline/flask_container_ci/test.sh'
            }
        }
    }
}
