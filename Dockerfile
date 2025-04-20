# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 2025

# Define the command to run the application using Uvicorn
CMD ["uvicorn", "auto:app", "--host", "0.0.0.0", "--port", "2025"]