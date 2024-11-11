# syntax=docker/dockerfile:1

# Use official python image from docker hub
FROM python:3.11-slim

# Set working directory to current directory
WORKDIR .

# Copy requirements file
COPY requirements.txt /

# Copy python script into container
COPY brink_node.py /

# Install build dependencies for psutil, install python libraries
# then remove build dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Command to run the script
CMD ["python3", "diagnostics.py"]
