from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings
from app.db.mongodb import MongoDB
from app.routes.v1.v1_router import v1_router


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
# app.include_router(router=v2_router, prefix="/api/v2")
