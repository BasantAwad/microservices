# Django Microservices Project

This project implements three microservices using Django and Docker:

1. **Auth Service** - Handles user authentication
2. **Course Registration Service** - Manages course registrations
3. **Notification Service** - Sends notifications

Each service has its own MySQL database and communicates via RabbitMQ message broker.

## Setup

1. Ensure Docker and Docker Compose are installed.
2. Run `docker-compose up --build` to start all services.
3. Access services at:
   - Auth Service: http://localhost:8001
   - Course Service: http://localhost:8002
   - Notification Service: http://localhost:8003
   - RabbitMQ Management: http://localhost:15672

## Services

- **Auth Service**: Port 8001, DB: auth_db (external port 33061)
- **Course Service**: Port 8002, DB: course_db (external port 33062)
- **Notification Service**: Port 8003, DB: notification_db (external port 33063)

## Message Broker

RabbitMQ is used for inter-service communication. Auth and Course services send messages to Notification Service.