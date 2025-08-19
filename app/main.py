from fastapi import FastAPI
from app.routes.product_routes import router

app = FastAPI(title="Store API - TDD com FastAPI")

app.include_router(router)
