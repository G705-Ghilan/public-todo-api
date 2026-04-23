from fastapi import APIRouter
from app.routes.v1.todos import todos_router

v1_router = APIRouter()
v1_router.include_router(todos_router)
# Future example adding users router, etc.