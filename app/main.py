from fastapi import FastAPI
from .database import engine
from .routes import router

from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
app.include_router(router, prefix="/api")
