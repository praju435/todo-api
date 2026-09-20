from fastapi import APIRouter, HTTPException, status

from .schemas import AuthRequest
from .supabase_client import supabase

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(auth: AuthRequest):
    if not auth.email or not auth.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required for signup."
        )

    response = supabase.auth.sign_up({
        "email": auth.email,
        "password": auth.password
    })

    if response.user is None:
        raise HTTPException(
            status_code=400,
            detail="unable to create account"
        )

    return{
        "user": response.user
    }

@router.post("/login")
def login(auth: AuthRequest):

    if not auth.email or not auth.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required for login."
        )
    try:
        response = supabase.auth.sign_in_with_password({
            "email": auth.email,
            "password": auth.password
        })

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="invalid login credentials"
        )
    if response.session is None:
        raise HTTPException(
            status_code=400,
            detail="invalid login credentials"
        )

    return{
        "access_token": response.session.access_token,
        "refresh_token": response.session.refresh_token
    }
    
