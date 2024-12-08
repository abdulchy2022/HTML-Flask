pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "my-flask-app:latest"       // Name of the Docker image
        APP_PORT = "5000"                         // Port the Flask app will run on
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/abdulchy2022/html-Flask.git' // Replace with your repo URL
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Deploy in Local Docker') {
            steps {
                echo 'Deploying Docker container...'
                // Stop any existing container running on the same port
                sh '''
                docker ps -q --filter "ancestor=$DOCKER_IMAGE" | xargs -r docker stop
                docker ps -q --filter "publish=$APP_PORT" | xargs -r docker stop
                '''
                // Run the Docker container
                sh 'docker run -d -p $APP_PORT:$APP_PORT $DOCKER_IMAGE'
            }
        }
    }
    post {
        success {
            echo 'Deployment successful. Access the app at http://localhost:$APP_PORT'
        }
        failure {
            echo 'Deployment failed. Check logs for details.'
        }
    }
}
