from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
from fastapi import APIRouter
from fastapi.responses import Response

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["method", "endpoint"]
)

MESSAGES_CREATED = Counter(
    "messages_created_total",
    "Total messages created"
)

metrics_router = APIRouter()


@metrics_router.get("/")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
