#!/bin/bash
# Simple kubernetes setup script for CSC468 group project

# Get current git commit
hash="$(git rev-parse --short HEAD)"

# Set working directory to $repo/DockerFiles
#cd /local/repository/DockerFiles

# Build our containers
# -t tag image
# -f dockerfile name
containers=(flaskct)
for ct in ${containers[@]}; do
	docker build -t ct_"$hash" -f ct .
done
