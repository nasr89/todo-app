from fastapi import APIRouter

import src.all_routes
import src.operations.to_do as db
from src.model.pydantic_model import Todo

todo_route = APIRouter()


# create a new todo
@todo_route.post(src.all_routes.todo_create)
def new_todo(doc: Todo):
    # doc = dict(doc)
    # todo: str = doc["todo"]
    todo: str = doc.todo  # Accessing the attribute directly
    res = db.create_to_do(todo)
    return res


# get all todos
@todo_route.get(src.all_routes.todo_all)
def all_todos():
    res = db.get_all()
    return res


# get one
@todo_route.get(src.all_routes.todo_one)
def todo_one(_id: int):
    res = db.get_one(_id)
    return res


# update one
@todo_route.patch(src.all_routes.todo_update)
def todo_update(_id: int, doc: Todo):
    # doc = dict(doc)
    # title: str = doc["todo"]
    title: str = doc.todo  # Accessing the attribute directly
    res = db.update_todo(_id, title)
    return res


# delete one
@todo_route.delete(src.all_routes.todo_delete)
def todo_delete(_id: int):
    res = db.delete_todo(_id)
    return res
