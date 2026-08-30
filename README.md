<p align="center"><img src="https://raw.githubusercontent.com/BasantAwad/BasantAwad/main/assets/introduction-banner.svg" alt="Terminal-inspired project banner" width="100%" /></p>

<!-- terminal-badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
</p>

<p align="center"><img src="https://raw.githubusercontent.com/BasantAwad/BasantAwad/main/assets/introduction-banner.svg" alt="Animated terminal profile for Basant Awad Mohamed" width="100%" /></p>

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
