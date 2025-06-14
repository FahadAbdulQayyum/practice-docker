# To Run this project using docker

```bash
docker build Dockerfile -t my-custom-app
```

## You can see the images

```bash
docker images
```

## You can build the images

```bash
# Build the Docker image and tag it with a name (e.g., my-fast-api)
# docker build -t <image-name>
docker build -t my-fast-api .
```

## You can run the built image

```bash
# Run the Docker container, mapping port 2025 on the host to port 2025 in the container
# docker run -p <host-port>:<container-port> <image-name>
docker build run -p 2025:2025 my-fast-api
```

## You can specify the volume

```bash
# Run the Docker container, mapping port 2025 on the host to port 2025 in the container
# docker run -d -p <host-port>:<container-port> --name <volume-container-name> -v <address-specified> <image-name>
docker run -d -p 2025:2025 --name Vol-Attached-Container -v E:\docker:/var/lib my-fast-api
```

## You can delete images and container

```bash
# Use `rmi' for removing image
docker rmi 1d4FEe... 
# First stop the container before removing otherwise it does not remove it
docker stop my-project-container
# Use `rm' for removing container
docker rm my-project-container
```

# Jenkins

Run the following commands for jenkins:

```bash
# This command installs the jenkins and run it locally, you can access it via `localhost:808`
# It asks you about the password which you get from logs of 'jenkins' running container like a hashed form string
# As like this e.g., 4f91e958bdac4d91b6b52d95354b6dc8
docker run -d -p 8081:8080 --name jenkins jenkins/jenkins
```

