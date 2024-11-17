# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the start script into the container
COPY start.sh .

# Make the start script executable
RUN chmod +x start.sh

# Command to run the start script
CMD ["./start.sh"]