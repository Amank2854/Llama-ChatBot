#!/bin/bash

# Step 1: Start the Docker containers using docker-compose
docker-compose up -d

# Step 2: Open the specified URL in a web browser
# Note: This command will open the URL in the default web browser on Linux.
# You can adjust it for other operating systems if needed.
open "http://localhost:8501"
