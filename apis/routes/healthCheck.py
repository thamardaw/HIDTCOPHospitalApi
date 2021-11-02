from fastapi import APIRouter, status

router = APIRouter(prefix="/healthcheck",tags=["Health Check"])

@router.get("/",status_code=status.HTTP_200_OK)
def get():
    return