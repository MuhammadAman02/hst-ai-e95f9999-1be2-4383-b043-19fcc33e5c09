from fastapi import APIRouter
from app.api import ai_routes, image_routes

# Create router
router = APIRouter()

# Include AI routes
router.include_router(ai_routes.router, prefix="/ai", tags=["ai"])

# Include Image routes
router.include_router(image_routes.router, prefix="/image", tags=["image"])

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}

# Add additional API routes here using the @router decorator