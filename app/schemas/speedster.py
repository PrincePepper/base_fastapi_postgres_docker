from typing import Literal
from uuid import UUID

from pydantic import BaseModel, EmailStr


# Основная схема
class SpeedsterBase(BaseModel):
    name: str
    gender: Literal["male", "female", "other/non-binary"]
    email: EmailStr
    velocity_kms_per_hour: float
    height_in_cm: float
    weight_in_kg: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Barry Allen",
                "gender": "male",
                "email": "barry.allen@starlabs.dc",
                "velocity_kms_per_hour": 2,
                "height_in_cm": 182.88,
                "weight_in_kg": 88.45,
            }
        }


# Пароль никогда не должен быть возвращен в ответе.
# Для этого используется третья схема, определенная ниже.
# Проверяется только запрос на создание.
class SpeedsterCreate(SpeedsterBase):
    password: str

    class Config:
        schema_extra = {
            "example": {
                **SpeedsterBase.Config.schema_extra.get("example"),
                "password": "secret",
            }
        }


# default schema to return on a response
class Speedster(SpeedsterBase):
    id: UUID

    class Config:
        orm_mode = True  # TL;DR; помогает связать модель со схемой

        schema_extra = {
            "example": {
                **SpeedsterBase.Config.schema_extra.get("example"),
                "id": "1fd43a2a-c0b9-4bc4-9b38-ec2d1f1b9898",
            }
        }
