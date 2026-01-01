# 🚀 Kubernetes DevOps Project – Demo Application

## 📌 Overview
This project demonstrates **end-to-end DevOps skills** by containerizing a Python application and deploying it on **Kubernetes (Minikube)** with **Ingress, CPU-based Autoscaling, and Monitoring**.

It follows **real-world Kubernetes practices** used in production environments.

---

## 🛠️ Tech Stack
- **Programming**: Python (Flask)
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube)
- **Ingress Controller**: NGINX
- **Autoscaling**: Horizontal Pod Autoscaler (CPU utilization-based)
- **Monitoring**: Prometheus & Grafana (kube-prometheus-stack)
- **OS**: Windows (PowerShell)

---

## 📁 Project Structure

devops-project/
├── app/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── k8s/
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ingress.yaml
│ └── hpa.yaml
├── monitoring/
│ └── notes.md
└── README.md


---

## 🚀 Application Features
- Containerized Python web application
- Kubernetes Deployment with multiple replicas
- Service exposed internally via ClusterIP
- External access using NGINX Ingress
- **CPU-based Horizontal Pod Autoscaling**  
- Cluster and application monitoring with Prometheus & Grafana

---

## ⚙️ Prerequisites
Ensure the following are installed:
- Docker
- Minikube
- kubectl
- Helm

Start Minikube:
```bash
minikube start --cpus=2 --memory=4000
