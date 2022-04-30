from fastapi import APIRouter
from . import couriers

router = APIRouter()

router.include_router(couriers.router)
