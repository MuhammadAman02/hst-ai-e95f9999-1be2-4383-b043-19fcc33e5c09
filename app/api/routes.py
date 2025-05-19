from fastapi import APIRouter
from app.api import ai_routes

# Create router
router = APIRouter()

# Include AI routes
router.include_router(ai_routes.router, prefix="/ai", tags=["ai"])

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}

# Add additional API routes here using the @router decorator