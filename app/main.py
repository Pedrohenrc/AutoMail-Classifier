from fastapi import FastAPI
from app.web.routes import router

app = FastAPI(title="AutoMail Classifier")

app.include_router(router)
