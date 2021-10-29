from fastapi import APIRouter
from .routes import user
from .routes import patient

router = APIRouter(prefix="/api")

router.include_router(user.router)
router.include_router(patient.router)
