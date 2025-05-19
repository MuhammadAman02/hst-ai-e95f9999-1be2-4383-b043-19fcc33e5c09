from reactpy import component, html, run
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="ReactPy Application")

@component
def HelloWorld():
    """A simple ReactPy component that renders a hello world message."""
    return html.div(
        html.h1("Hello from ReactPy!"),
        html.p("This is a ReactPy application running with FastAPI."),
        html.div(
            html.h2("Features"),
            html.ul(
                html.li("Component-based UI"),
                html.li("Python-first web development"),
                html.li("FastAPI integration"),
                html.li("Hot reloading"),
            )
        ),
        className="container",
        style={"maxWidth": "800px", "margin": "0 auto", "padding": "2rem"}
    )

# Configure the app with ReactPy
configure(app, HelloWorld)

# Add API routes if needed
@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}