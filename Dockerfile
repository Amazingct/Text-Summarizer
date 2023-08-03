# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy all files from the current directory to the container's working directory
COPY . /app

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for Flask application
EXPOSE 8080

# Run the Flask application (assuming your main file is app.py)
CMD ["python", "app.py"]