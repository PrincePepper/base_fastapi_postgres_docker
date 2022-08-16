from typing import List
from uuid import UUID

from fastapi.params import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..models.speedster import Speedster
from ..schemas.speedster import SpeedsterCreate


class SpeedstersRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db  # произойдет внедрение зависимостей

    def find(self, uuid: UUID) -> Speedster:
        query = self.db.query(Speedster)
        return query.filter(Speedster.id == uuid).first()

    def find_by_email(self, email: EmailStr):
        query = self.db.query(Speedster)
        return query.filter(Speedster.email == email).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Speedster]:
        query = self.db.query(Speedster)
        return query.offset(skip).limit(max).all()

    def create(self, speedster: SpeedsterCreate) -> Speedster:
        speedster.password += "__you_must_hash_me"

        db_speedster = Speedster(**speedster.dict())

        self.db.add(db_speedster)
        self.db.commit()
        self.db.refresh(db_speedster)

        return db_speedster
