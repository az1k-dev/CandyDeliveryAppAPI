from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
import models.couriers
from database import get_session

router = APIRouter(prefix="/couriers")


@router.post("", status_code=status.HTTP_201_CREATED)
def import_couriers(couriers: models.couriers.CouriersPostRequest, session: Session = Depends(get_session)):
    return couriers


@router.get("/{courier_id}")
def get_courier_info(courier_id: int):
    return f"Hey, courier {courier_id}"
