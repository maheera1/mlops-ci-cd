pipeline {
    agent any

    environment {
        IMAGE_NAME = 'hamnaakayani/mlops-app'  // Docker Hub Image Name
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u hamnaakayani --password-stdin'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    // Stop running container if exists
                    sh '''
                    CONTAINER_ID=$(docker ps -q --filter ancestor=$IMAGE_NAME)
                    if [ ! -z "$CONTAINER_ID" ]; then
                        docker stop $CONTAINER_ID
                        docker rm $CONTAINER_ID
                    fi
                    '''

                    // Run new container
                    sh 'docker run -d -p 5000:5000 $IMAGE_NAME'
                }
            }
        }
    }
}
