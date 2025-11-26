pipeline {
    agent any
    
    environment {
        DOCKERHUB_USERNAME = 'hades504'
        IMAGE_NAME = 'hades504/imt2023103-todo-cli'
        IMAGE_TAG = "${BUILD_NUMBER}"

        GITHUB_CREDS = credentials('githubcicd')
        DOCKERHUB_CREDS = credentials('ci/cddocker')
    }
    
    stages {

        stage('Checkout') {
            steps {
                echo "Pulling code from GitHub..."
                git branch: 'main',
                    url: 'git@github.com:NirbhaySharma504/Todo-CI-CD.git',
                    credentialsId: 'githubcicd'
            }
        }

        stage('Build - Install Dependencies') {
            steps {
                echo "Setting up Python virtual environment..."
                sh '''
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
                echo "Running Python tests..."
                sh '''
                    . venv/bin/activate
                    python3 todo_app.py test
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Pushing Docker image..."
                sh "echo \$DOCKERHUB_CREDS_PSW | docker login -u \$DOCKERHUB_CREDS_USR --password-stdin"
                sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                sh "docker logout"
            }
        }

        stage('Verify Docker Image') {
            steps {
                echo "Verifying Docker image..."
                sh "docker images | grep ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "✓ Pipeline completed successfully!"
        }
        failure {
            echo "✗ Pipeline failed!"
        }
        always {
            cleanWs()
        }
    }
}
