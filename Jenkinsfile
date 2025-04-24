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
                    }
                }
            }
        }
        stage("Clean Environment docker"){
            steps{
                bat "echo Test"
            }
        }

    }
}