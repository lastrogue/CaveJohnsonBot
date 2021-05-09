#!/bin/bash
# Kill all docker containers
echo "Killing containers....."
docker kill $(docker ps -q)
echo "Containers killed."
# Remove docker containers
echo "Removing containers....."
docker rm $(docker ps -a -q)
echo "Containers removed."
# Remove docker images
echo "Removing images....."
docker rmi $(docker images -q)
echo "Images removed."
# Builds based on current docker configuration and files
echo "Rebuilding Image....."
docker build -t discord_py_cj .
echo "Images rebuilt."
# Starts the docker container in detached mode and always restarts
echo "Starting Container....."
docker run -d --restart always discord_py_cj
echo "Container started."
echo "Image rebuilt and container started."