from pydantic import BaseModel, validator, Field
from enum import Enum
from models.regions import RegionItem
from models.hours import HourItem


class CourierTypeEnum(str, Enum):
    foot = "foot"
    bike = "bike"
    car = "car"


class CourierItem(BaseModel):
    courier_id: int
    courier_type: CourierTypeEnum
    regions: list[RegionItem]
    working_hours: list[HourItem]

    class Config:
        orm_mode = True

    def get_getresponse(self):
        return CourierGetResponse(
            courier_id=self.courier_id,
            courier_type=self.courier_type,
            regions=list(map(lambda r: r.region, self.regions)),
            working_hours=list(map(lambda h: h.hour, self.working_hours))
        )


class CourierPostRequest(BaseModel):
    id: int
    courier_type = CourierTypeEnum
    regions: list[int]
    working_hours: list[str]


class CouriersPostRequest(BaseModel):
    data: list[CourierPostRequest]


class CourierGetResponse(BaseModel):
    courier_id: int
    courier_type: str

    regions: list[int]
    working_hours: list[str]
