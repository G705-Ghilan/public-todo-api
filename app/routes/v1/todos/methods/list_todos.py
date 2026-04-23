from app.db.mongodb import MongoDBDep
from app.routes.v1.todos.router import todos_router
from app.routes.v1.todos.schema import TodoItem


@todos_router.get('/todos', response_model=list[TodoItem], response_model_exclude_none=True)
async def list_todos(db: MongoDBDep):
    return await db.todos_collection.find({}).to_list()
