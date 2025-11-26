pipeline {
    agent any

    environment {
        // Docker image details
        DOCKER_IMAGE = 'hades504/imt2023103-todo-cli'
        DOCKER_TAG   = '3'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                // Uses the same SCM config as "Declarative: Checkout SCM"
                checkout scm
            }
        }

        stage('Build - Install Dependencies') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    set -e
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Python tests...'
                sh '''
                    set -e
                    . venv/bin/activate
                    python3 todo_app.py test
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    set -e
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image...'
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ci/cddocker',
                        usernameVariable: 'DOCKERHUB_CREDS_USR',
                        passwordVariable: 'DOCKERHUB_CREDS_PSW'
                    )
                ]) {
                    sh '''
                        set -e
                        echo "${DOCKERHUB_CREDS_PSW}" | docker login -u "${DOCKERHUB_CREDS_USR}" --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Verify Docker Image') {
            steps {
                echo 'Verifying Docker image...'
                sh '''
                    set -e
                    docker images | grep "${DOCKER_IMAGE}" || (echo "Local image not found" && exit 1)
                    docker pull ${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }
    }

    post {
        success {
            echo '✓ Pipeline completed successfully!'
        }
        failure {
            echo '✗ Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}
