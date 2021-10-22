from fastapi import APIRouter
from .routes import user,authentication

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(authentication.router)