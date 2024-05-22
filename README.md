# Kubernetes_helm

# tagging local image to azure acr
docker tag calc iscsregistry.azurecr.io/calculator:v1  

# pushing the taged image to acr
docker push iscsregistry.azurecr.io/sub:v1   

# Apply the Deployment YAML files to your Kubernetes cluster
kubectl apply -f adder-deployment.yaml
kubectl apply -f subtractor-deployment.yaml
kubectl apply -f coordinator-deployment.yaml

# Apply the Service YAML files to your Kubernetes cluster:
kubectl apply -f adder-service.yaml
kubectl apply -f subtractor-service.yaml
kubectl apply -f coordinator-service.yaml

# Check the Service IP Address: After the Service is created, you can check its IP address using:
kubectl get services

## HELM for kubernetes deployment management
# Set up Helm If Helm is not already installed, install it on your local machine:

# Install Helm (Linux/macOS)
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install Helm (windows)
# Install Chocolatey: Run the following command to install Chocolatey:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
# Verify Installation
choco

# Install Helm (Windows)
choco install kubernetes-helm

# Create a Helm Chart
helm create my-microservices-chart

# Install Helm Chart: Once you’ve defined your Helm chart, you can install it on your Kubernetes cluster:
# Package the Helm Chart: Navigate to the directory containing your Helm chart and package it:
cd my-microservices-chart
helm package .

# Deploy the Helm Chart
helm install my-microservices-release my-microservices-chart/

