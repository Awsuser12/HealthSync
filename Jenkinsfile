pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = 'AKIAUZPNLVFPGWGVS7G3'
        AWS_SECRET_ACCESS_KEY = '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'
        AWS_DEFAULT_REGION = 'eu-north-1'
        ECR_REPO = '329599658334.dkr.ecr.eu-north-1.amazonaws.com/fastapi-app'
        CLUSTER_NAME = 'my-eks-cluster'
        IMAGE_TAG = 'latest'
    }

    stages {
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
                    sh '''
                    aws eks --region ${AWS_DEFAULT_REGION} update-kubeconfig --name ${CLUSTER_NAME}
                    echo "apiVersion: apps/v1
                    kind: Deployment
                    metadata:
                      name: fastapi-app
                      labels:
                        app: fastapi-app
                    spec:
                      replicas: 1
                      selector:
                        matchLabels:
                          app: fastapi-app
                      template:
                        metadata:
                          labels:
                            app: fastapi-app
                        spec:
                          containers:
                          - name: fastapi-container
                            image: ${ECR_REPO}:${IMAGE_TAG}
                            ports:
                            - containerPort: 8000
                    ---
                    apiVersion: v1
                    kind: Service
                    metadata:
                      name: fastapi-service
                    spec:
                      type: LoadBalancer
                      ports:
                      - port: 80
                        targetPort: 8000
                      selector:
                        app: fastapi-app" > deployment.yaml
                    kubectl apply -f deployment.yaml
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
