#!/bin/bash

# Build the Docker image
docker build -t my-fastapi-app .

# Run the Docker container
docker run -d -p 80:80 my-fastapi-app