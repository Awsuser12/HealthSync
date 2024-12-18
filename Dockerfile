# Use the official Python base image
FROM python:3.10-slim

# Set a working directory in the container
WORKDIR /app

# Copy requirements file to the container
COPY requirement.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy all application files to the container
COPY . .

# Expose the port used by the application
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
