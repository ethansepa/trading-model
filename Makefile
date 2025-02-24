# Define the name of your Docker Compose service
SERVICE_NAME=api

# Build the Docker container
build:
	docker-compose up --build

# Start the services in the background
up:
	docker-compose up -d

# Stop the services
down:
	docker-compose down

# Restart the services
restart:
	docker-compose down
	docker-compose up -d

# Show the status of the containers
status:
	docker-compose ps

# Clean up the environment (remove containers, networks, and volumes)
clean:
	docker-compose down --volumes
