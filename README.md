# TaskManager API

A simple task management API built with FastAPI.

## Features
- Create, read, and delete tasks.
- RESTful API with FastAPI.
- Dockerized application.
- Configuration via environment variables.

## Getting Started

### Prerequisites
- Python 3.11+
- Docker (optional, for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TaskManager
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```

### Running the App
1. Run the app locally:
   ```bash
   uvicorn app.main:app --reload
   ```
2. Access the API at `http://127.0.0.1:8000`.

### Docker Deployment
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Run the app in a container:
   ```bash
   docker-compose up
   ```

## API Endpoints
- `GET /` - Root endpoint.
- [POST /tasks](http://_vscodecontentref_/9) - Create a new task.
- [GET /tasks](http://_vscodecontentref_/10) - List all tasks.
- [GET /tasks/{task_id}](http://_vscodecontentref_/11) - Get a task by ID.
- [DELETE /tasks/{task_id}](http://_vscodecontentref_/12) - Delete a task by ID.