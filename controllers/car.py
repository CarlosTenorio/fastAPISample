from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, APIRouter, Body
from models.car import Car, CarPUT

router = APIRouter()

####
# Car with constructor
####
# @router.get("/")
# def read_car():
#     car1 = Car(3, 4, 'Porshe', '911', None)
#     car2 = Car(5, 4, 'Hyundai', 'i30', '345PJK')
#     cars = [car1, car2]
#     return {"cars": cars}


def _create_mock_cars():
    car1 = Car(id=0, doors=3, wheels=4, brand='Porshe',
               model='911', registrationId=None)
    car2 = Car(id=1, doors=5, wheels=4, brand='Hyundai',
               model='i30', registrationId='345PJK')
    return [car1, car2]

####
# Car with BaseModel
####
@router.get("/")
def read_car():
    cars = _create_mock_cars()
    return {"cars": cars}


@router.get("/{car_id}")
def read_car_detail(car_id: int):
    cars = _create_mock_cars()
    car_to_return = next(
        (car for car in cars if car.id == car_id), None)
    if(car_to_return):
        return car_to_return
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/")
def create_car(car: Car):
    cars = _create_mock_cars()
    cars.append(car)
    print(cars[2])
    return car


@router.put("/{car_id}")
async def update_item(car_id: int, car: CarPUT):
    cars = _create_mock_cars()
    car_to_update = next((car for car in cars if car.id == car_id), None)
    car_to_update.wheels = car.wheels
    car_to_update.model = car.model
    car_to_update.brand = car.brand
    car_to_update.doors = car.doors
    car_to_update.registrationId = car.registrationId
    return cars
