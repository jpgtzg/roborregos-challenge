# Use a base Linux image
FROM python:3.12-slim

# Install any additional dependencies if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev

# Install RPi.GPIO
RUN pip install RPi.GPIO

# Set up your application directory
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install any additional Python dependencies
RUN pip install -r requirements.txt

# Run your application
CMD ["python", "main.py"]
