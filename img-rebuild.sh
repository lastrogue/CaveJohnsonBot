#!/bin/bash
# Kill all docker containers
echo "--------------Killing containers.....--------------"
docker kill $(docker ps -q)
echo "--------------Containers killed.--------------"
# Remove docker containers
echo "--------------Removing containers.....--------------"
docker rm $(docker ps -a -q)
echo "--------------Containers removed.--------------"
# Remove docker images
echo "--------------Removing images.....--------------"
docker rmi $(docker images -q)
echo "--------------Images removed.--------------"
# Builds cj docker based on current docker configuration and files
echo "--------------Rebuilding Image.....--------------"
docker build -t discord_py_cj . # Edit . to point to directory where cj dockerfile is located.
echo "--------------Images rebuilt.--------------"
# Builds GLaDOS docker based on current docker configuration and files
echo "--------------Rebuilding Image.....--------------"
docker build -t discord_py_glados . # Edit . to point to directory where GLaDOS dockerfile is located.
echo "--------------Images rebuilt.--------------"
# Starts the cj docker container in detached mode and always restarts
echo "--------------Starting cj Container.....--------------"
docker run -d --restart always discord_py_cj
echo "--------------Cj Container started.--------------"
# Starts the GLaDOS docker container in detached mode and always restarts
echo "--------------Starting GLaDOS Container.....--------------"
docker run -d --restart always discord_py_glados
echo "--------------GLaDOS Container started.--------------"
echo "--------------Images rebuilt and containers started.--------------"