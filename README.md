# Django Microservices Exercise

A Dockerized microservices exercise implementing authentication, course registration, and notifications as separate Django services with independent MySQL databases and RabbitMQ messaging.

## Architecture

Each service follows a clear MVC-style boundary between models, request handling, and business logic. RabbitMQ carries inter-service notifications while each service owns its persistence and API behavior.

## Services

| Service | Responsibility |
| --- | --- |
| Auth | User authentication and identity workflows |
| Course registration | Course enrollment and registration state |
| Notification | Asynchronous notifications triggered by service events |

## Run

```bash
docker compose up --build
```

Use the service-specific configuration and environment files to set database and broker connection details.
