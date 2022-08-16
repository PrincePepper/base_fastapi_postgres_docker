from uuid import uuid4

from sqlalchemy import Column, String, Float, MetaData
from sqlalchemy.dialects.postgresql import UUID

from ..database import Model

metadata = MetaData()


class Speedster(Model):
    __tablename__ = "speedsters"
    __metadata__ = metadata
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    gender = Column(String)  # improve with Enum Choice, if you want
    email = Column(String, unique=True, index=True)
    password = Column(String)
    velocity_kms_per_hour = Column(Float)
    height_in_cm = Column(Float)
    weight_in_kg = Column(Float)
