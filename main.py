from contextlib import asynccontextmanager
from fastapi import APIRouter, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field, model_serializer


from app.core.config import get_settings
from app.core.functions import safe_object_id
from app.core.types import OutputBaseModel, PyObjectId
from app.db.mongodb import MongoDB, MongoDBDep
from app.routes.v1.v1_router import v1_router
from app.routes.v1.todos import todos_router


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Initialize MongoDB before server starts
    app.mongodb = MongoDB(get_settings())
    await app.mongodb.connect()

    yield
    # Close MongoDB when server shutdown
    await app.mongodb.close()


app = FastAPI(lifespan=app_lifespan)


# Include V1 routes
app.include_router(router=v1_router, prefix="/api/v1")
