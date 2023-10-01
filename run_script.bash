#!/bin/bash

# Step 1: Start the Docker containers using docker-compose
docker run -d -p 8501:8501 amank2854/clockbox:latest

# Step 2: Add sleep time to wait for the server to start
sleep 4

# Step 3: Open the specified URL in a web browser
# Note: This command will open the URL in the default web browser on Linux.
# You can adjust it for other operating systems if needed.
start "http://localhost:8501"
