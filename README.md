# To-Do List CLI Application - IMT2023103

A simple command-line To-Do List application built with Python.

## Installation Instructions

### 1. Install Docker (Linux/WSL)

```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add user to docker group
sudo usermod -aG docker $USER

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
docker --version
```

### 2. Install Jenkins (Windows)

1. Download Jenkins from: https://www.jenkins.io/download/
2. Download the Windows installer (.msi file)
3. Run the installer and follow the setup wizard
4. Access Jenkins at: http://localhost:8080
5. Get initial admin password from: `C:\Program Files\Jenkins\secrets\initialAdminPassword`
6. Install suggested plugins
7. Create admin user

### 3. Configure Jenkins

**Install Required Plugins:**
- Docker Pipeline
- GitHub Integration

**Add DockerHub Credentials:**
1. Manage Jenkins → Credentials → System → Global credentials
2. Add Credentials:
   - Kind: Username with password
   - Username: Your DockerHub username
   - Password: Your DockerHub password
   - ID: dockerhub-credentials

### 4. Create Jenkins Pipeline

1. New Item → Pipeline
2. Name: "IMT2023103-TodoApp"
3. Pipeline Definition: Pipeline script from SCM
4. SCM: Git
5. Repository URL: Your GitHub repo URL
6. Script Path: Jenkinsfile
7. Save and Build

## Local Testing

```bash
# Run application
python3 todo_app.py

# Run tests
python3 todo_app.py test

# Build Docker image
docker build -t imt2023103/todo-app .

# Run Docker container
docker run -it imt2023103/todo-app

# Check Docker images
docker images
```

## DockerHub

Create account at: https://hub.docker.com
Repository: imt2023103/todo-app

## File Structure
# Todo-CI-CD
