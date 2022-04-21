from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.dailyClosing import DailyClosing
from core.services.dailyClosing import DailyClosingService
from core.entity.dailyClosing import DailyClosing as DailyClosingDTO,DailyClosingSmall as DailyClosingSmallDTO
from infrastructure.repository.dailyClosing import DailyClosingRepository
from typing import List

router = APIRouter(prefix="/dailyClosing", tags=["Daily Closing"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[DailyClosingSmallDTO])
def get_all_dailyClosings(repo=Depends(DailyClosingRepository)):
    return DailyClosingService(repo).getAllDailyClosing()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=DailyClosingDTO)
def get_dailyClosing(id: int, repo=Depends(DailyClosingRepository)):
    return DailyClosingService(repo).getDailyClosing(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=DailyClosingDTO)
def create(request: DailyClosing, repo=Depends(DailyClosingRepository)):
    return DailyClosingService(repo).closeCashierCounter(request)
    # return {"detail": "DailyClosing create successful."}
