from fastapi import APIRouter
from .routes import inventoryItem, pharmacyItem, user, patient,\
     authentication, healthCheck, uom, category, salesServiceItem,\
     bill, payment, deposit, dailyClosing, inventoryTransaction,\
     transactionType, inventory


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
router.include_router(inventoryItem.router)
router.include_router(pharmacyItem.router)
router.include_router(inventoryTransaction.router)
router.include_router(transactionType.router)
router.include_router(inventory.router)