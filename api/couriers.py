from fastapi import APIRouter
import models.couriers

router = APIRouter(prefix="/couriers")


@router.post("/")
def import_couriers(couriers: models.couriers.CouriersPostRequest):
    return couriers


@router.get("/{courier_id}")
def get_courier_info(courier_id: int):
    return f"Hey, courier {courier_id}"
