import sys

import src.decoders.todo as decode
from src.connection import db_session
from src.model.sql_model import Todo

sys.path.append("./")


# create a todo
def create_to_do(todo: str) -> dict:
    try:
        req = Todo(todo)
        db_session.add(req)
        db_session.commit()
        return {"status": "ok", "message": "new todo added"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# get all to-do list


def get_all():
    try:
        res = db_session.query(Todo).all()
        docs = decode.decode_todos(res)
        return {"status": "ok", "data": docs}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# get one todo
def get_one(_id: int):
    try:
        criteria = {"_id": _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            record = decode.decode_todo(res)
            return {"status": "ok", "data": record}
        else:
            return {
                "status": "error",
                "message": f"Record with id {_id} do not exist",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# update a todo
def update_todo(_id: int, title: str):
    try:
        criteria = {"_id": _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            res.todo = title  # type: ignore
            db_session.commit()
            return {"status": "ok", "message": "Record updated successfuly"}
        else:
            return {
                "status": "error",
                "message": f"Record with id {_id} do not exist",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# delete a todo
def delete_todo(_id: int):
    try:
        criteria = {"_id": _id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {"status": "ok", "message": "Record deleted successfuly"}
        else:
            return {
                "status": "error",
                "message": f"Record with id {_id} do not exist",
            }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# res = create_to_do("creating a html course")
# print(res)

# res = get_all()
# print(res)

# res = get_one(5)
# print(res)

# res = update_todo(1, 'creating a website')
# print(res)

# res = delete_todo(4)
# print(res)
