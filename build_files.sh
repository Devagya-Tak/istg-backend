#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
pip install -r requirements.txt

# Create the staticfiles directory if it doesn't exist
mkdir -p staticfilesBuild

# Collect static files
python3 manage.py collectstatic --noinput

# Move collected static files to the build directory
mv staticfiles staticfilesBuild
