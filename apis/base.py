from fastapi import APIRouter
from .routes import user, patient, authentication, healthCheck, uom, category, salesServiceItem, bill, payment, deposit, dailyClosing

router = APIRouter(prefix="/api")

router.include_router(healthCheck.router)
router.include_router(user.router)
router.include_router(authentication.router)
router.include_router(patient.router)
router.include_router(uom.router)
router.include_router(category.router)
router.include_router(salesServiceItem.router)
router.include_router(bill.router)
router.include_router(payment.router)
router.include_router(deposit.router)
router.include_router(dailyClosing.router)
