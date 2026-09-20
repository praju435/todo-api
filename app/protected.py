from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from .supabase_client import supabase
from .dependecies import get_current_user

router = APIRouter(tags=["Protection"])

@router.get("/public/info")
def public_info():
    return{
        "message": "welcome sucker this info is public"
    }

@router.get("/protected/profile")
def profile(user=Depends(get_current_user)):

    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }

@router.get("/protected/dashboard")
def dashboard(auth=Depends(get_current_user)):

    user = auth["user"]

    return {
        "message": "Welcome to your dashboard",
        "user_id": user.id,
        "email": user.email
    }