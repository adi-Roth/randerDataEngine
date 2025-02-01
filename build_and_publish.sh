#!/bin/bash

# Variables
PACKAGE_NAME="randerDataEngine"
ARTIFACTORY_REPO="your-artifactory-repo"  # Replace with your Artifactory repository name
ARTIFACTORY_URL="https://your-artifactory-instance/artifactory"  # Replace with your Artifactory URL
ARTIFACTORY_USER="your-username"  # Replace with your Artifactory username
ARTIFACTORY_API_KEY="your-api-key"  # Replace with your Artifactory API key

# Clean previous builds
rm -rf dist/

# Build the package
python setup.py sdist bdist_wheel

# Publish to Artifactory
jfrog rt upload \
  --url $ARTIFACTORY_URL \
  --user $ARTIFACTORY_USER \
  --apikey $ARTIFACTORY_API_KEY \
  "dist/*" \
  "$ARTIFACTORY_REPO/$PACKAGE_NAME/"
