from fastapi import APIRouter
from .routes import user
from .routes import patient
from .routes import authentication
from .routes import healthCheck
from .routes import uom
from .routes import category
from .routes import salesServiceItem

router = APIRouter(prefix="/api")

router.include_router(healthCheck.router)
router.include_router(user.router)
router.include_router(authentication.router)
router.include_router(patient.router)
router.include_router(uom.router)
router.include_router(category.router)
router.include_router(salesServiceItem.router)
