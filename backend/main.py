from fastapi import FastAPI
from pydantic import BaseModel
from backend.schemas.project_schema import Project


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to AI Software Architect Agent"}


@app.get("/projects")
def get_projects():
    return {
        "projects": [
            "Hospital Management System",
            "E-Commerce Platform",
            "Turf Booking System"
        ]
    }


@app.post("/projects")
def create_project(project: Project):
    return {
        "project_name": project.project_name,
        "description": project.description,
        "status": "Project Created Successfully"
    }

@app.put("/projects/{project_id}")
def update_project(project_id: int):
    return {
        "message": f"Project {project_id} updated"
    }


@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    return {
        "message": f"Project {project_id} deleted"
    }
@app.get("/search")
def search_project(project_name: str):
    return {
        "message": f"You searched for {project_name}"
    }
@app.get("/filter")
def filter_projects(status: str, owner: str):
    return {
        "status": status,
        "owner": owner
    }