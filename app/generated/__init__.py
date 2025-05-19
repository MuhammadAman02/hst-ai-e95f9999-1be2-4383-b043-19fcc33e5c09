from fastapi import APIRouter

router = APIRouter()

# Import generated routes/modules here to register them with the router
# Example:
# from . import your_feature_module

# Include routers from feature modules
# Example:
# router.include_router(your_feature_module.router, tags=["your-feature"])

# Routes defined in submodules will be automatically associated with this router
# if they use the '@router' decorator.