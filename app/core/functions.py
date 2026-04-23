from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status


# Avoid invalid objectId characters length error
def safe_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid todo id format"
        )
