from fastapi.exceptions import HTTPException
from starlette import status

SQLALCHEMY_ERROR = lambda exception,status_code = status.HTTP_500_INTERNAL_SERVER_ERROR: HTTPException(
    status_code=status_code,
    detail=str(exception)
)