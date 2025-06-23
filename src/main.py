from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import metrics, messages

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

app.include_router(messages.router, prefix="/messages")
app.include_router(metrics.metrics_router, prefix="/metrics")
