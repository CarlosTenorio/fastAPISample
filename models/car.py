
from pydantic import BaseModel
from typing import Optional


# class Car(BaseModel):
#     def __init__(self,
#                  doors: int,
#                  wheels: int,
#                  brand: str,
#                  model: str,
#                  registrationId: str):
#         self.doors = doors
#         self.wheels = wheels
#         self.brand = brand
#         self.model = model
#         self.registrationId = registrationId


class Car(BaseModel):
    id: int
    doors: int
    wheels: int
    brand: str
    model: str
    registrationId: Optional[str] = None


class CarPUT(BaseModel):
    doors: int
    wheels: int
    brand: str
    model: str
    registrationId: Optional[str] = None
