from typing import Annotated, Any

from pydantic import BaseModel, BeforeValidator, model_serializer


# Passing object it to str(ObjectId) before start validating
PyObjectId = Annotated[str, BeforeValidator(str)]


class OutputBaseModel(BaseModel):
    @model_serializer(mode="wrap")
    def _exclude_none(self, handler: Any) -> dict[str, Any]:
        return {
            key: value
            for key, value in handler(self).items()
            if value is not None
        }
