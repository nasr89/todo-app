from fastapi import FastAPI

from src.routes.todo import todo_route

app = FastAPI()

app.include_router(todo_route)
