# Set the base image to use
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required packages
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the Python file
CMD [ "python", "app.py" ]
