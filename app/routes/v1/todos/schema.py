from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.core.types import PyObjectId


class TodoInput(BaseModel):
    task_title: str
    note: str | None = None
    completed: bool


class TodoItem(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    task_title: str
    note: str | None = None
    completed: bool
    created_at: datetime


class UpdateTask(BaseModel):
    task_title: str | None = None
    note: str | None = None
    completed: bool | None = None
