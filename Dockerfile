<<<<<<< HEAD
# Use the Jenkins image as the base image
FROM jenkins/jenkins:lts

# Switch to root user to install dependencies
USER root

# Install prerequisites and Docker
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io python3 python3-pip && \
    apt-get clean && \
    ln -s /usr/bin/python3 /usr/bin/python

# Add Jenkins user to the Docker group (create if it doesn't exist)
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create the Docker directory and volume for DinD
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Switch back to the Jenkins user
USER jenkins
=======
## Source Image
FROM python:3.12-bookworm-slim

## Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Workidr
WORKDIR /app

## System dependencies
RUN apt-get update && apt-getinstall -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copy to container
COPY . .

## Python dependencies
RUN pip install --co-cache-dir -e .

## Expose port
EXPOSE 5000

## Run the app
CMD ["python", "app/application.py"]
>>>>>>> 16a58f6 (Final changes)
