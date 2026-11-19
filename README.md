# SecureCloud – AWS DevOps Deployment Platform

An end-to-end deployment project demonstrating automated testing, containerization, CI/CD, and cloud deployment using AWS.

## Overview

SecureCloud is a Flask-based application deployed on AWS EC2 using Docker and Terraform. It uses GitHub Actions to automate testing, Docker image building, publishing, and deployment.

## Tech Stack

- **Application:** Python, Flask
- **Database:** SQLite
- **Testing:** Pytest
- **Containerization:** Docker
- **Container Registry:** Docker Hub
- **CI/CD:** GitHub Actions
- **Cloud Provider:** AWS
- **Infrastructure as Code:** Terraform
- **Deployment:** AWS Systems Manager (SSM)
- **Authentication:** AWS IAM OIDC

## Architecture

Developer pushes code to GitHub  
↓  
GitHub Actions runs tests  
↓  
Docker image is built  
↓  
Docker image is pushed to Docker Hub  
↓  
GitHub Actions authenticates with AWS using OIDC  
↓  
AWS SSM sends deployment commands to EC2  
↓  
EC2 pulls the specific Docker image version  
↓  
Docker container runs the Flask application

## Features

- User registration API
- SQLite database integration
- Automated testing with Pytest
- Dockerized application
- Automated CI/CD pipeline
- AWS EC2 deployment
- Infrastructure provisioning using Terraform
- GitHub Actions authentication using OIDC
- Deployment through AWS Systems Manager without SSH
- Persistent database storage using Docker volumes

## CI/CD Pipeline

GitHub Actions automates the following:

1. Checkout source code
2. Configure Python
3. Install dependencies
4. Run automated tests
5. Build Docker image
6. Push image to Docker Hub
7. Authenticate with AWS using OIDC
8. Deploy application to EC2 using SSM
9. Verify deployment using a health endpoint

## AWS Infrastructure

Infrastructure managed using Terraform includes:

- Amazon EC2
- Virtual Private Cloud (VPC)
- Public subnet and internet connectivity
- Internet Gateway
- Route table
- Security Group
- IAM roles and instance profile
- AWS Systems Manager integration

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Application health check |
| GET | `/api/users` | Retrieve users |
| POST | `/api/users` | Register a user |

## Running Locally

### Clone the repository

```bash
git clone https://github.com/shreeharibv-hub/SecureCloud.git
cd SecureCloud
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run tests

```bash
python -m pytest -v
```

## Docker

Build the Docker image:

```bash
docker build -t securecloud .
```

Run the container:

```bash
docker run -d \
  --name securecloud-app \
  -p 5000:5000 \
  -v securecloud-data:/data \
  securecloud
```

## Infrastructure Deployment

Terraform is used to provision AWS infrastructure.

```bash
terraform init
terraform plan
terraform apply
```

GitHub Actions handles automated application deployment through AWS Systems Manager.

## Project Goal

This project demonstrates practical experience with cloud infrastructure, Infrastructure as Code, containerization, automated testing, CI/CD pipelines, and AWS deployment workflows.
