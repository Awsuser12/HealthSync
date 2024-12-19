pipeline {
    agent any

    environment {
        // Define the path to the .env file
        DOTENV_PATH = './env'
    }

    stages {
        stage('Load Environment Variables') {
            steps {
                script {
                    // Read and load variables from the .env file
                    def props = readProperties file: "${DOTENV_PATH}"
                    env.AWS_ACCESS_KEY_ID = props['AWS_ACCESS_KEY_ID']
                    env.AWS_SECRET_ACCESS_KEY = props['AWS_SECRET_ACCESS_KEY']
                    env.AWS_DEFAULT_REGION = props['AWS_DEFAULT_REGION']
                    env.ECR_REPO = props['ECR_REPO']
                    env.CLUSTER_NAME = props['CLUSTER_NAME']
                    env.IMAGE_TAG = props['IMAGE_TAG']
                }
                echo "Environment variables loaded successfully."
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    sh 'docker build -t ${ECR_REPO}:${IMAGE_TAG} .'
                }
            }
        }

        stage('Push to ECR') {
            steps {
                echo "Pushing Docker image to AWS ECR..."
                script {
                    sh '''
                    aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
                    docker push ${ECR_REPO}:${IMAGE_TAG}
                    '''
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                echo "Deploying application to EKS..."
                script {
                    // Update kubeconfig for EKS cluster
                    sh '''
                    aws eks --region ${AWS_DEFAULT_REGION} update-kubeconfig --name ${CLUSTER_NAME}
                    cp /var/jenkins_home/deployment.yaml ${WORKSPACE}/deployment.yaml
                    kubectl apply -f ${WORKSPACE}/deployment.yaml
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "Verifying application deployment..."
                script {
                    sh '''
                    kubectl get pods
                    kubectl get services
                    '''
                }
            }
        }
    }
}
