import reflex as rx
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define the state
class State(rx.State):
    """The app state."""
    count: int = 0

    def increment(self):
        """Increment the count."""
        self.count += 1
        logger.info(f"Count incremented to {self.count}")

    def decrement(self):
        """Decrement the count."""
        self.count -= 1
        logger.info(f"Count decremented to {self.count}")

# Define the UI
def index():
    """The main view."""
    return rx.center(
        rx.vstack(
            rx.heading("Reflex App", size="lg"),
            rx.text("Welcome to Reflex - Python-first web framework"),
            rx.hstack(
                rx.button(
                    "Decrement",
                    on_click=State.decrement,
                    color_scheme="red",
                ),
                rx.heading(State.count, size="md"),
                rx.button(
                    "Increment",
                    on_click=State.increment,
                    color_scheme="green",
                ),
            ),
            rx.text(
                "Reflex allows you to build web apps in pure Python",
                color="gray.500",
                font_size="sm",
            ),
            spacing="4",
            padding="2em",
        ),
        width="100%",
        height="100vh",
    )

# Create the app
app = rx.App()

# Add the index page
app.add_page(index)

# API routes can be added with FastAPI
@app.api.get("/api/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}