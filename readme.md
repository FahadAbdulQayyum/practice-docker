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

