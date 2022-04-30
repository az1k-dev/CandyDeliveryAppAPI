from pydantic import BaseModel, validator, Field
from enum import Enum


class RegionItem(BaseModel):
    id: int | None
    region: int

    class Config:
        orm_mode = True
