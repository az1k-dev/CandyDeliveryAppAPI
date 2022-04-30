from fastapi import APIRouter, status
import models.couriers

router = APIRouter(prefix="/couriers")


@router.post("", status_code=status.HTTP_201_CREATED)
def import_couriers(couriers: models.couriers.CouriersPostRequest):
    return couriers


@router.get("/{courier_id}")
def get_courier_info(courier_id: int):
    return f"Hey, courier {courier_id}"
