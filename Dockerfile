# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy your randerDataEngine repo into the container
COPY . /packages/randerDataEngine

# Install your package globally
RUN pip install -e /packages/randerDataEngine

# Verify the installation by listing the installed packages
RUN pip list

# Set the default command for the container (optional)
CMD ["python3"]
