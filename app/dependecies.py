from fastapi import Header
from fastapi.responses import JSONResponse

from .supabase_client import supabase


def get_current_user(authorization: str | None = Header(default=None)):

    if not authorization:
        return JSONResponse(
            status_code=401,
            content={"error": "Access token required"}
        )

    if not authorization.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={"error": "Access token required"}
        )

    token = authorization.replace("Bearer ", "", 1).strip()

    if not token:
        return JSONResponse(
            status_code=401,
            content={"error": "Access token required"}
        )

    try:
        response = supabase.auth.get_user(token)
    except Exception:
        return JSONResponse(
            status_code=401,
            content={"error": "Invalid or expired token"}
        )

    if response.user is None:
        return JSONResponse(
            status_code=401,
            content={"error": "Invalid or expired token"}
        )

    return response.user