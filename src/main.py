from fastapi import FastAPI
from routers import metrics, messages

app = FastAPI()

app.include_router(messages.router, prefix="/messages")
app.include_router(metrics.metrics_router, prefix="/metrics")
