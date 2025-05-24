pipeline {
    agent any
    environment {
        IMAGE_NAME = 'hanaa01/flask-app'
        IMAGE_TAG = '${IMAGE_NAME}:${env.GIT_COMMIT}'
    }
    stages {
        stage('Test') {
            steps {
                sh "pytest"
            }
        }
        stage('Login to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo ${PASSWORD} | docker login -u ${USERNAME} --password-stdin"
                }
                echo 'Login successfully'
            }
        }
        stage('Build docker image') {
            steps {
                script {
                    echo "Building Docker image ${IMAGE_TAG}"
                    sh "docker build -t ${IMAGE_TAG} . "
                }
        }
        }
        stage('Push image to docker hub') {
            steps {
                sh "docker push ${IMAGE_TAG} "
                echo "IMAGE PUSHED TO DOCKER HUB SUCCESSFULLY"
            }
        }
    }
}
