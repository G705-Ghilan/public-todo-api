from fastapi import HTTPException, status
from pymongo import ReturnDocument

from app.core.functions import safe_object_id
from app.db.mongodb import MongoDBDep
from app.routes.v1.todos.router import todos_router
from app.routes.v1.todos.schema import TodoItem, UpdateTask


@todos_router.put('/todos/{id}', response_model=TodoItem, response_model_exclude_none=True)
async def update_todo(id: str, updated: UpdateTask, db: MongoDBDep) -> TodoItem:
    values = updated.model_dump(exclude_none=True, by_alias=True)

    if len(values) > 0:
        result = await db.todos_collection.find_one_and_update(
            {"_id": safe_object_id(id)},
            {"$set": values},
            return_document=ReturnDocument.AFTER
        )
        if result:
            return result
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No todo with id: {id}"
            )

    if not (item := await db.todos_collection.find_one({'_id': safe_object_id(id)})):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No todo with id: {id}"
        )

    return item


