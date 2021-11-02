from fastapi import APIRouter
from .routes import user
from .routes import patient
from .routes import authentication
from .routes import healthCheck

router = APIRouter(prefix="/api")

router.include_router(healthCheck.router)
router.include_router(user.router)
router.include_router(authentication.router)
router.include_router(patient.router)
