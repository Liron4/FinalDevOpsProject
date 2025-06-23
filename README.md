# FastAPI Notes - DevOps Project

## Overview

This project is a production-ready FastAPI web service for managing notes/messages, fully instrumented for observability and deployed with a modern CI/CD pipeline.  
It demonstrates best practices in Python API development, Dockerization, monitoring with Prometheus and Grafana, and cloud deployment (Render).  

---

## Features

- **FastAPI** backend for CRUD operations on messages
- **Prometheus** metrics for request count, latency, and business events
- **Grafana** dashboards for real-time monitoring
- **Dockerized** for easy deployment
- **CI/CD** with GitHub Actions: automatic testing, linting, Docker image build & push, and Render deployment

---

## Project Structure

```
.
├── src/
│   ├── main.py              # FastAPI app entrypoint
│   ├── routers/
│   │   ├── messages.py      # Message endpoints & business logic
│   │   └── metrics.py       # Prometheus metrics & /metrics endpoint
│   └── tests/
│       ├── test_messages.py # Unit tests for message endpoints
│       └── test_metrics.py  # Unit tests for metrics endpoint
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build instructions
├── docker-compose.yml       # Local monitoring stack (Prometheus, Grafana, Node Exporter)
├── prometheus.yml           # Prometheus scrape config
├── grafana_dashboard.json   # Example Grafana dashboard
├── .github/workflows/
│   ├── CI.yml               # CI: lint, test, build
│   └── CD.yml               # CD: build, push, deploy to Render
└── README.md
```

---

## Highlights:

### Monitoring Stack (Prometheus & Grafana)

#### Start monitoring stack

```bash
docker compose up -d
```

- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000) (admin/admin)

#### Import the dashboard

- Add Prometheus as a data source (`http://prometheus:9090`)
- Import `grafana_dashboard.json` for ready-made panels

---

### CI/CD

- **CI**: On every pull request to `main`, GitHub Actions runs lint and tests
- **CD**: On every push to `main`, Docker image is built & pushed to Docker Hub, then Render is notified to redeploy

---

### Production Deployment

- The app is deployed on [Render](https://fastapi-notes-tl4r.onrender.com/)
- Docker image: [`liron123/fastapi-notes`](https://hub.docker.com/repository/docker/liron123/fastapi-notes)

---

- `POST /messages/` - Add a new message
- `GET /messages/` - List all messages
- `GET /messages/{msg_id}` - Get a message by ID
- `GET /metrics/` - Prometheus metrics endpoint

---

## Monitoring Metrics

- `http_requests_total` - Count of HTTP requests by method and endpoint
- `http_request_latency_seconds` - Request latency histogram
- `messages_created_total` - Business metric: messages created

---

## License

MIT License

---

## Note

- To start an activity on the server for testing purposes, head to https://fastapi-notes-tl4r.onrender.com/docs to trigger the endpoints. Root endpoint will redirect to it.

