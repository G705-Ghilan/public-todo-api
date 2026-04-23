from typing import Annotated

from fastapi import Depends, Request
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.core.config import Settings


class MongoDB:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.mongo_client: AsyncMongoClient | None = None
        self.database: AsyncDatabase | None = None

    async def connect(self) -> None:
        self.mongo_client = AsyncMongoClient(self.settings.mongodb_url)
        self.database = self.mongo_client.get_database('todo')

        # Ping database
        ping_response = await self.database.command('ping')
        if int(ping_response.get("ok")) != 1:
            raise Exception(f"MongoDB connect failed, {ping_response}")

    async def close(self) -> None:
        if self.mongo_client:
            await self.mongo_client.close()

    @property
    def todos_collection(self):
        return self.database.get_collection('todos')


# Get Injected mongodb from FastApi app
def get_mongodb(request: Request) -> MongoDB:
    return request.app.mongodb


# MongoDB dependency for FastAPI endpoints
MongoDBDep = Annotated[MongoDB, Depends(get_mongodb)]
