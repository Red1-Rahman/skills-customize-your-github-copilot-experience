# Starter Code for FastAPI Todo API Assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# TODO: Define a Pydantic model for Todo items
# class Todo(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     completed: bool = False

# TODO: Create an in-memory database (list) to store todos
# todos_db = []

# TODO: Create a POST endpoint to create a new todo
# @app.post("/todos", status_code=201)
# async def create_todo(todo: Todo):
#     # Add todo to database
#     # Return the created todo

# TODO: Create a GET endpoint to retrieve all todos
# @app.get("/todos")
# async def get_todos():
#     # Return all todos from the database

# TODO: Create a GET endpoint to retrieve a single todo by id
# @app.get("/todos/{todo_id}")
# async def get_todo(todo_id: int):
#     # Find and return the todo, or raise 404 if not found

# TODO: Create a PUT endpoint to update a todo
# @app.put("/todos/{todo_id}")
# async def update_todo(todo_id: int, todo: Todo):
#     # Find and update the todo, or raise 404 if not found

# TODO: Create a DELETE endpoint to remove a todo
# @app.delete("/todos/{todo_id}", status_code=204)
# async def delete_todo(todo_id: int):
#     # Find and delete the todo, or raise 404 if not found

# TODO: Add query parameters for filtering and pagination
# @app.get("/todos")
# async def get_todos_filtered(
#     skip: int = 0,
#     limit: int = 10,
#     completed: Optional[bool] = None
# ):
#     # Implement filtering by completed status
#     # Implement pagination with skip and limit
#     # Return filtered and paginated results
