from fastapi import APIRouter
from controllers import car

api_router = APIRouter()
api_router.include_router(car.router, prefix="/cars", tags=["cars"])
