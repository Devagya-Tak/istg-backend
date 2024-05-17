#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Ensure staticfilesBuild directory exists
mkdir -p staticfilesBuild

# Move collected static files to the build directory
mv staticfiles/* staticfilesBuild/
