from pydantic import BaseModel, validator
from enum import Enum


class CourierTypeEnum(str, Enum):
    foot = "foot"
    bike = "bike"
    car = "car"


class CourierItem(BaseModel):
    courier_id: int
    courier_type: CourierTypeEnum
    regions: list[int]
    working_hours: list[str]

    class Config:
        orm_mode = True


class CouriersPostRequest(BaseModel):
    data: list[CourierItem]
