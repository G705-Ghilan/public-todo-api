from typing import Annotated

from pydantic import BeforeValidator

# Passing object it to str(ObjectId) before start validating
PyObjectId = Annotated[str, BeforeValidator(str)]
