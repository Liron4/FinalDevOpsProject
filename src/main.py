from fastapi import FastAPI
from src.routers import about, messages, root

app = FastAPI()

app.include_router(root.router)
app.include_router(about.router)
app.include_router(messages.router)