# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory into the container
COPY backend /app/backend

# Expose the port that FastAPI will run on
EXPOSE 8000

# Set the correct Python path inside the container to include /app
ENV PYTHONPATH=/app/backend

# Define the default command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
