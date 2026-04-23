from datetime import datetime, timezone

from app.db.mongodb import MongoDBDep
from app.routes.v1.todos.schema import TodoInput, TodoItem
from app.routes.v1.todos.router import todos_router


@todos_router.post('/todos', response_model=TodoItem, response_model_exclude_none=True)
async def create_todo(todo: TodoInput, db: MongoDBDep):
    todo_item = todo.model_dump(by_alias=True, exclude_none=True)
    todo_item['created_at'] = datetime.now(timezone.utc)

    result = await db.todos_collection.insert_one(todo_item)
    todo_item["_id"] = result.inserted_id

    return todo_item
