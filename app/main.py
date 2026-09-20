from fastapi import FastAPI
from pydantic import BaseModel
from .database import engine
from .models import Base
from .routes import router
from .supabase_client import supabase
from .auth import router as auth_router
from .protected import router as protected_router


app =  FastAPI(
    title = "TODO API",
    description = "A simple TODO API built with FastAPI and SQLAlchemy")

#create the database tables
Base.metadata.create_all(bind=engine)


# register all routes
app.include_router(router)
app.include_router(auth_router)
app.include_router(protected_router)

app.get("/")
def root():
    return {
        "message": "Todo API server running with supabase"
    }



