from fastapi import FastAPI
from pydantic import BaseModel
from .database import engine
from .models import Base
from .routes import router

app =  FastAPI(
    title = "TODO API",
    description = "A simple TODO API built with FastAPI and SQLAlchemy")

#create the database tables
Base.metadata.create_all(bind=engine)


# register all routes
app.include_router(router)



