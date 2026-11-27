# SecureCloud – AWS DevOps Deployment Platform

An end-to-end cloud deployment project demonstrating automated testing, containerization, CI/CD automation, Infrastructure as Code, and deployment on AWS.

## Overview

**SecureCloud** is a Flask-based application deployed on AWS EC2 using Docker and Terraform.

The project implements an automated CI/CD workflow using GitHub Actions. Whenever code is pushed to the GitHub repository, the workflow runs automated tests, builds a Docker image, publishes it to Docker Hub, and deploys the application to an EC2 instance through AWS Systems Manager (SSM).

AWS IAM OIDC authentication enables GitHub Actions to access AWS using temporary credentials without storing long-lived AWS access keys.

## Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions Workflow
    |
    +----> Checkout Source Code
    |
    +----> Install Dependencies
    |
    +----> Run Pytest
    |
    +----> Build Docker Image
    |
    +----> Push Image to Docker Hub
    |
    +----> Authenticate with AWS using OIDC
    |
    v
AWS Systems Manager (SSM)
    |
    v
AWS EC2 Instance
    |
    +----> Pull Specific Docker Image Version
    |
    +----> Run Docker Container
    |
    v
Flask Application
    |
    v
Health Check Verification
```

## Tech Stack

| Category | Technologies |
|---|---|
| Application | Python, Flask |
| Database | SQLite |
| Testing | Pytest |
| Containerization | Docker |
| Container Registry | Docker Hub |
| CI/CD | GitHub Actions |
| Cloud Provider | AWS |
| Infrastructure as Code | Terraform |
| Deployment | AWS Systems Manager (SSM) |
| Authentication | AWS IAM OIDC |
| Version Control | Git, GitHub |

## Features

- Flask-based REST API application.
- User registration and retrieval APIs.
- SQLite database integration.
- Automated testing using Pytest.
- Docker-based application containerization.
- Docker image publishing to Docker Hub.
- Automated CI/CD using GitHub Actions.
- AWS infrastructure provisioning using Terraform.
- Secure AWS authentication using GitHub Actions OIDC.
- Remote deployment through AWS Systems Manager without SSH.
- Version-specific Docker image deployment.
- Persistent SQLite database storage using Docker volumes.
- Application health verification through a health endpoint.

## CI/CD Pipeline

GitHub Actions automates the application delivery process through the following stages:

| Stage | Description |
|---|---|
| 1. Checkout | Retrieves the latest repository source code. |
| 2. Environment Setup | Configures Python and installs dependencies. |
| 3. Testing | Executes automated tests using Pytest. |
| 4. Docker Build | Builds the application Docker image. |
| 5. Image Publishing | Pushes the image to Docker Hub. |
| 6. AWS Authentication | Uses OIDC to obtain temporary AWS credentials. |
| 7. Deployment | Sends deployment commands to EC2 through AWS SSM. |
| 8. Verification | Checks application availability using the health endpoint. |

## AWS Infrastructure

Terraform manages the AWS infrastructure required for deployment.

The infrastructure includes:

- **Amazon EC2:** Hosts the Dockerized Flask application.
- **Amazon VPC:** Provides network isolation.
- **Public Subnet:** Hosts the EC2 instance with the required internet connectivity.
- **Internet Gateway:** Enables internet connectivity for the public subnet.
- **Route Table:** Controls subnet traffic routing.
- **Security Group:** Controls inbound and outbound network traffic.
- **IAM Roles and Instance Profile:** Provide permissions for EC2 and AWS service interactions.
- **AWS Systems Manager:** Enables remote instance management and deployment without SSH.

## Security Implementation

SecureCloud incorporates several security practices:

- **OIDC Authentication:** Uses federated identity between GitHub Actions and AWS IAM.
- **Temporary Credentials:** Avoids storing long-lived AWS access keys in GitHub.
- **IAM Least Privilege:** Restricts permissions to the required AWS operations.
- **Security Groups:** Limits network access to required traffic.
- **Encrypted EBS:** Protects EC2 storage at rest.
- **SSM-Based Deployment:** Avoids relying on direct SSH access for deployment.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Checks application health. |
| GET | `/api/users` | Retrieves registered users. |
| POST | `/api/users` | Registers a new user. |

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/shreeharibv-hub/SecureCloud.git
cd SecureCloud
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run automated tests

```bash
python -m pytest -v
```

## Running with Docker

### 1. Build the Docker image

```bash
docker build -t securecloud .
```

### 2. Run the container

```bash
docker run -d \
  --name securecloud-app \
  -p 5000:5000 \
  -v securecloud-data:/data \
  securecloud
```

The Docker volume provides persistent storage for the SQLite database across container recreation, provided the application database path is configured to use `/data`.

## Infrastructure Deployment

Terraform is used to provision the required AWS infrastructure.

Navigate to the Terraform directory:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Preview infrastructure changes:

```bash
terraform plan
```

Provision the infrastructure:

```bash
terraform apply
```

GitHub Actions handles the application deployment through AWS Systems Manager after successful CI/CD execution.

## Repository Structure

```text
SecureCloud/
│
├── app/
│   ├── ...
│
├── tests/
│   └── test_app.py
│
├── terraform/
│   └── ...
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
└── README.md
```

*The directory structure above is a high-level representation; adjust it to match the actual repository.*

## Project Goal

The goal of SecureCloud is to demonstrate practical implementation of:

- Cloud infrastructure provisioning.
- Infrastructure as Code using Terraform.
- Containerization using Docker.
- Automated testing and CI/CD.
- Secure cloud authentication using OIDC.
- AWS EC2 deployment using Systems Manager.
- Persistent application data management.
- Reliable application deployment and health verification.

**SecureCloud demonstrates an end-to-end approach to building, testing, packaging, and deploying applications on AWS using modern DevOps practices.**
