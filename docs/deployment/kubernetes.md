# Kubernetes Deployment Guide

This project supports deployment to Kubernetes using **Helm**.

## Prerequisites
- A Kubernetes cluster (Minikube, KIND, or a cloud provider)
- [Helm](https://helm.sh/docs/intro/install/) installed
- [kubectl](https://kubernetes.io/docs/tasks/tools/) installed

## Chart Structure
The Helm chart is located in `deploy/kubernetes/helm/data-continuum`. It manages:
- **API**: FastAPI backend
- **UI**: React frontend
- **ML**: Machine Learning service
- **Seeder**: Data seeding job
- **Infrastructure**: Postgres, MongoDB, Redis (basic deployments)
- **Airflow**: Webserver and Scheduler

## Getting Started

### 1. Build Docker Images
Before deploying, ensure your Docker images are built and available in your cluster's registry.

```bash
docker build -t data-continuum-api:latest ./api
docker build -t data-continuum-ui:latest ./ui
docker build -t data-continuum-ml:latest ./ml
docker build -t data-continuum-seeder:latest ./seeder
```

*Note: If using Minikube, run `eval $(minikube docker-env)` before building.*

### 2. Install the Chart
Navigate to the root directory and run:

```bash
helm install data-continuum ./deploy/kubernetes/helm/data-continuum
```

### 3. Verify Deployment
Check the status of your pods:

```bash
kubectl get pods
```

### 4. Access the Services
You can port-forward to access the services locally:

```bash
# API
kubectl port-forward svc/data-continuum-api 8000:8000

# UI
kubectl port-forward svc/data-continuum-ui 5173:5173

# Airflow
kubectl port-forward svc/data-continuum-airflow-webserver 8080:8080
```

## Configuration
You can customize the deployment by modifying `values.yaml` or by passing `--set` flags during installation.

Example:
```bash
helm install data-continuum ./deploy/kubernetes/helm/data-continuum \
  --set replicaCount=3 \
  --set api.image.tag=v1.2.3
```

## Uninstalling
To remove the deployment:

```bash
helm uninstall data-continuum
```
