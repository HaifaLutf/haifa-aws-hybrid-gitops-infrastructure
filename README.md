
# 🚀 Hybrid-Cloud GitOps: EKS Infrastructure & Observability

This repository contains a production-ready, highly secure **AWS EKS** environment managed through **Infrastructure as Code (Terraform)** and **GitOps (Flux CD)**. The architecture features a Zero Trust ingress strategy using Cloudflare Tunnels, bypassing the need for public-facing load balancers.

### 🔗 Live Endpoints
* **Application:** [app.haifa.work](https://app.haifa.work)
* **Monitoring:** [grafana.haifa.work](https://grafana.haifa.work)

---

## 🏗️ Architecture Overview
![Architecture Diagram] <img width="1024" height="558" alt="image" src="https://github.com/user-attachments/assets/c717b389-863a-4c6a-8b9f-7bfdda2b1859" />


This project demonstrates a full-lifecycle DevOps workflow:
1. **Provisioning:** AWS VPC and EKS cluster managed via **Terraform**.
2. **Configuration:** Worker nodes prepped using **Ansible** for baseline dependencies.
3. **Synchronization:** **Flux CD** bootstraps the cluster and ensures the live state matches the configuration in the `clusters/` directory.
4. **Ingress:** **Cloudflare Tunnels** provide secure, encrypted tunnels from the EKS pods directly to the Cloudflare Edge.

---

## 🛠️ Tech Stack

| Category | Tools |
| :--- | :--- |
| **Cloud** | AWS (EKS, VPC, IAM, EBS) |
| **IaC** | Terraform, Ansible |
| **GitOps** | Flux CD |
| **Observability** | Prometheus, Grafana |
| **Security** | Cloudflare Zero Trust (Tunnels) |
| **Backend** | Python (Flask), PostgreSQL |

---

## 📂 Project Structure

```text
├── ansible/                # Node preparation playbooks
├── clusters/
│   └── haifa-eks-cluster/
│       ├── flux-system/    # Flux CD components
│       └── infrastructure/ # K8s manifests (Cloudflared, Monitoring, Postgres)
├── my-python-app/          # Flask application & Dockerfile
├── eks.tf                  # EKS Cluster definition
├── vpc.tf                  # Network topology
└── provider.tf             # AWS & Terraform config
