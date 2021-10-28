from fastapi import APIRouter
from .routes import user
from .routes import patients

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(patients.router)
