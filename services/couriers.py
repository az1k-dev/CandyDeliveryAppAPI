from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status

import tables
from models.couriers import CouriersPostRequest
from database import get_session


class CouriersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_courier(self, courier_id):
        courier = self.session.query(tables.Courier).filter(tables.Courier.id == courier_id).first()
        if not courier:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return courier

    def import_couriers(self, couriers: CouriersPostRequest):
        pass
