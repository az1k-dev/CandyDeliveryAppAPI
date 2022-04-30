from pydantic import BaseModel, validator, Field
from enum import Enum


class HourItem(BaseModel):
    id: int | None
    hour: str

    class Config:
        orm_mode = True
