# Python Application Project Base

This project base is designed to support multiple Python web frameworks and AI application types as described in the HST AI Python Engineer prompts. It provides a flexible structure that can be used for various application types including web applications, AI/ML applications, data processing, and automation.

## Project Structure

```
project_root/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logging_config.py
│   ├── frontend/
│   │   ├── __init__.py
│   │   ├── nicegui_app.py
│   │   ├── reactpy_app.py
│   │   ├── reflex_app.py
│   │   └── routes.py
│   ├── models/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   ├── static/
│   └── templates/
├── logs/
│   └── app.log
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   └── partials/
│       ├── footer.html
│       └── header.html
├── Dockerfile
├── fly.toml
├── main.py
├── requirements.txt
└── run.py
```

## Supported Frameworks

This project base supports multiple modern Python web frameworks:

1. **FastAPI** - Default framework for building APIs
2. **NiceGUI** - Python-based UI framework for building web interfaces
3. **ReactPy** - React-inspired UI library for Python
4. **Reflex** - Python-first web framework

## Getting Started

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

You can run the application with different frameworks by setting the `FRAMEWORK` environment variable:

```bash
# Run with FastAPI (default)
python main.py

# Run with NiceGUI
FRAMEWORK=nicegui python main.py

# Run with ReactPy
FRAMEWORK=reactpy python main.py

# Run with Reflex
FRAMEWORK=reflex python main.py
```

Alternatively, you can set the framework in a `.env` file:

```
FRAMEWORK=nicegui
```

## Application Types

This project base supports various application types as described in the HST AI Python Engineer prompts:

### Web Applications
- FastAPI/Flask/Django web services
- RESTful APIs
- GraphQL APIs
- Modern UI frameworks (NiceGUI, ReactPy, Reflex)
- Server-side rendered applications

### AI/ML Applications
- Chatbots and conversational agents
- Natural language processing systems
- Computer vision applications
- Recommendation systems
- Fraud detection systems

### Data Processing
- ETL pipelines
- Data analysis scripts
- Reporting systems
- Big data processing

### Automation
- Task automation scripts
- Workflow automation
- Scheduled jobs
- System monitoring

## Core Principles

This project follows these key principles:

1. **Code Quality and Organization**
   - Small, focused functions and classes (< 50 lines)
   - Type hints for type safety
   - PEP 8 style guidelines
   - Modular designs
   - Extensive logging for debugging

2. **Component Creation**
   - Separate files for each module
   - Established Python libraries
   - SOLID principles
   - Proper package organization

3. **State Management**
   - Appropriate data structures
   - Proper database models and ORM
   - Minimal global state
   - Response caching when appropriate

4. **Error Handling**
   - Proper exception handling
   - Logging for errors
   - User-friendly error messages
   - Custom exceptions when appropriate

5. **Performance**
   - Code optimization
   - Async/await for I/O-bound operations
   - Efficient data structures and algorithms
   - Minimal unnecessary computations

6. **Security**
   - Input validation
   - Proper authentication
   - Data sanitization
   - Security best practices

7. **Testing**
   - Unit tests for critical functions
   - Integration tests
   - Pytest for testing
   - Error handling verification

8. **Documentation**
   - Docstrings for complex functions
   - Up-to-date README
   - Setup instructions
   - API endpoint documentation