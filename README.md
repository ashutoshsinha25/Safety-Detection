
---

# Industry Safety Detection using Yolov7

This project utilizes Yolov7 for detecting safety compliance in industrial environments. The solution is designed to be deployed using AWS services and can be integrated into a CI/CD pipeline with GitHub Actions.

## Table of Contents
- [Data](#data)
- [Yolov7 GitHub Repository](#yolov7-github-repository)
- [Yolov7 Tutorial](#yolov7-tutorial)
- [Project Workflow](#project-workflow)
- [Configuration Files](#configuration-files)
- [Git Commands](#git-commands)
- [AWS Configurations](#aws-configurations)
- [How to Run](#how-to-run)
- [AWS CI/CD Deployment with GitHub Actions](#aws-cicd-deployment-with-github-actions)
- [Environment Variables](#environment-variables)

## Data
[Link to dataset]

## Yolov7 GitHub Repository
[Link to Yolov7 GitHub repository]

## Yolov7 Tutorial
[Link to Yolov7 tutorial]

## Project Workflow
The project follows a structured workflow, divided into the following components:
1. **constants**: Define project constants.
2. **config_entity**: Configuration management.
3. **artifact_entity**: Manage artifacts.
4. **components**: Core components of the project.
5. **pipeline**: Workflow pipeline.
6. **app.py**: Main application file.

## Git Commands
To commit and push changes to the repository:

```bash
git add .
git commit -m "Updated"
git push origin main
```

## AWS Configurations
- AWS CLI Download: [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

To configure AWS:

```bash
aws configure
```

## How to Run
Set up the environment and run the application:

```bash
conda create -n safety python=3.8 -y
conda activate safety
pip install -r requirements.txt
python app.py
```

## AWS CI/CD Deployment with GitHub Actions
### Step 1: Login to AWS Console
Create an IAM user with the following access permissions:
1. **EC2 Access**: Virtual machine management.
2. **ECR**: Elastic Container Registry to store your Docker images.

### Step 2: Description of Deployment
1. Build a Docker image of the source code.
2. Push the Docker image to ECR.
3. Launch an EC2 instance.
4. Pull the Docker image from ECR in the EC2 instance.
5. Launch the Docker image in the EC2 instance.

### Step 3: Required AWS Policies
- **AmazonEC2ContainerRegistryFullAccess**
- **AmazonEC2FullAccess**

### Step 4: Create ECR Repository
Create an ECR repository to store/save the Docker image.
- Save the URI: `136566696263.dkr.ecr.us-east-1.amazonaws.com/yolov7app`

### Step 5: Create EC2 Machine (Ubuntu)
Open the EC2 instance and install Docker:

```bash
# Optional
sudo apt-get update -y
sudo apt-get upgrade

# Required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### Step 6: Configure EC2 as Self-Hosted Runner
Navigate to `Settings > Actions > Runner > New Self-Hosted Runner` in GitHub, choose the OS, and run the commands provided.

### Step 7: Setup GitHub Secrets
Add the following secrets to GitHub:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION = us-east-1`
- `AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com`
- `ECR_REPOSITORY_NAME = simple-app`

## Environment Variables
For local replication, it's recommended to store all secret keys in a `.env` file:

```plaintext
AWS_ACCESS_KEY_ID=<your-access-key-id>
AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com
ECR_REPOSITORY_NAME=simple-app
```

Ensure that your `.env` file is listed in the `.gitignore` to prevent it from being tracked by Git.

---
