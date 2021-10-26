from fastapi import APIRouter
from .routes import user

router = APIRouter(prefix="/api")

router.include_router(user.router)
