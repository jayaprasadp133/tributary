# Sensor Streaming System

This project is a backend for a sensor streaming system that provides real-time engine temperature data.

## Endpoints

- `/record`: Records a new engine temperature reading to the Redis database.
- `/collect`: Collects the most current engine temperature and calculates an average.

## Setup

1. Ensure Docker and Docker Compose are installed.
2. Build and start the containers:
   ```sh
   docker-compose up --build
