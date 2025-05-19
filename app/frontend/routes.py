from fastapi import Request
from fastapi.responses import HTMLResponse
from . import router
from .. import templates
import os

@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    """Serves the main index page using Jinja2 templates."""
    if templates:
        template_path = os.path.join(templates.env.loader.searchpath[0], 'index.html')
        if os.path.exists(template_path):
            return templates.TemplateResponse("index.html", {"request": request})
        else:
            return HTMLResponse(content="Welcome! Frontend template 'index.html' not found.", status_code=404)
    else:
        return HTMLResponse(content="Welcome! Templates directory not configured.", status_code=500)

# Add additional frontend routes here using the @router decorator