import os
import importlib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Determine which framework to use based on environment variable
# Default to FastAPI if not specified
FRAMEWORK = os.getenv("FRAMEWORK", "fastapi").lower()

# Import the appropriate application based on the framework
if FRAMEWORK == "fastapi":
    from app import app
    application = app
elif FRAMEWORK == "nicegui":
    try:
        from nicegui import ui, app as nicegui_app
        # Setup NiceGUI app here
        application = nicegui_app
    except ImportError:
        print("NiceGUI not installed. Please install with: pip install nicegui")
        exit(1)
elif FRAMEWORK == "reactpy":
    try:
        import reactpy
        from app.frontend.reactpy_app import app as reactpy_app
        application = reactpy_app
    except ImportError:
        print("ReactPy not installed. Please install with: pip install reactpy")
        exit(1)
elif FRAMEWORK == "reflex":
    try:
        import reflex
        from app.frontend.reflex_app import app as reflex_app
        application = reflex_app
    except ImportError:
        print("Reflex not installed. Please install with: pip install reflex")
        exit(1)
else:
    # Default to FastAPI
    from app import app
    application = app

# This is used by ASGI servers like Uvicorn
app = application

if __name__ == "__main__":
    import uvicorn
    # Run the application with uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)