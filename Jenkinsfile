pipeline {
agent any
environment {
   registryCredential = 'dockerhub_id'
   backendimagename = "darkerlighter/backendapi"
   frontendimagename = "darkerlighter/frontend"
    }
    stages {
        stage("Clone Repository") {
            steps {
                git([url: 'git@github.com:ShaharRubel/DevopsProject.git', branch: 'main', credentialsId: 'github_repo'])
            }
        }
        stage("Install required libraries"){
            steps{
                bat "pip install -r requirements.txt"
            }
        }
        stage("Deploy application with docker compose"){
            steps{
                bat 'docker-compose up -d'
            }
        }
        stage("Run backend & frontend testing"){
            steps{
                bat 'python tests/backend_testing.py'
                bat "python tests/frontend_testing.py"
            }
        }
        stage("Clean Environment docker"){
            steps{
                bat 'docker-compose down --rmi local'
            }
        }

        stage("Build docker images"){
            steps{
                bat "docker build -t ${backendimagename}:${BUILD_NUMBER} -f backend/Dockerfile ."
                bat "docker build -t ${frontendimagename}:${BUILD_NUMBER} -f frontend/Dockerfile ."
            }
        }
        stage("Push docker image"){
            steps{
                script {
                    withCredentials([usernamePassword(credentialsId: registryCredential, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"

                        // Push the images
                        bat "docker push ${backendimagename}:${BUILD_NUMBER}"
                        bat "docker push ${frontendimagename}:${BUILD_NUMBER}"
                        // Retag images to latest
                        bat "docker tag ${backendimagename}:${BUILD_NUMBER} ${backendimagename}:latest"
                        bat "docker tag ${frontendimagename}:${BUILD_NUMBER} ${frontendimagename}:latest"
                        // Push images as Latest
                        bat "docker push ${backendimagename}:latest"
                        bat "docker push ${frontendimagename}:latest"
                    }
                }
            }
        }
        stage("Delete unused docker images"){
            steps{
                bat "docker rmi ${backendimagename}:${BUILD_NUMBER}"
                bat "docker rmi ${frontendimagename}:${BUILD_NUMBER}"
                bat "docker rmi ${backendimagename}:latest"
                bat "docker rmi ${frontendimagename}:latest"

            }
        }

    }
}