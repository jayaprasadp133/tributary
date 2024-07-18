# Sensor Streaming System🌡️

This project is a backend for a sensor streaming system that provides real-time engine temperature data. It uses Flask for the web framework and Redis for storing sensor data.

## Requirements📋

- Docker: Ensure Docker and Docker Compose are installed on your system. You can download Docker Desktop from [here](https://www.docker.com/products/docker-desktop).

## Getting Started🚀

Follow these steps to set up and run the sensor streaming system:

## 1. Clone the Repository

```sh
git clone https://github.com/your-username/sensor-streaming-system.git
cd sensor-streaming-system
```
This command will build the Docker image for the Flask application defined in the Dockerfile and start the Flask server and Redis database.

## 2. Start the Application
This command will build the Docker image for the Flask application defined in the Dockerfile and start the Flask server and Redis database.
```sh
docker-compose up
```

## 3. Access the Flask Application
Once the containers are up and running, you can access the Flask application at http://localhost:5000.



## 4. Test the Endpoints
You can test the endpoints using curl commands in a terminal or any REST client:

### Record Temperature:
```sh
curl -X POST -H "Content-Type: application/json" -d '{"temperature": 75}' http://localhost:5000/record
```
### Collect Temperature:
```sh
curl http://localhost:5000/collect
```


## 5. Shutdown the Containers
To stop the Docker containers and remove the network:
```sh
docker-compose down
```

## Additional Notes ℹ️
Dependencies: All Python dependencies are listed in the requirements.txt file. If you need to add more dependencies, update this file and rebuild the Docker image using docker-compose up --build.

Dockerfile: The Dockerfile defines the environment for the Flask application.

docker-compose.yml: The docker-compose.yml file configures and runs multiple services (Flask and Redis) in Docker containers.

## Troubleshooting🛠️
If you encounter any issues during setup or running the application, ensure Docker and Docker Compose are correctly installed and that there are no conflicts with existing services on port 5000.

```sh

You can now easily copy this entire content and paste it into your README.md file.
```



