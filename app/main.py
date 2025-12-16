from fastapi import FastAPI
from app.routes import router

# Initialize the FastAPI app
app = FastAPI()

# Include the task routes
app.include_router(router)

@app.get("/")
def read_root():
    """
    Root endpoint to verify the app is running.
    """
    return {"message": "Welcome to TaskManager API"}