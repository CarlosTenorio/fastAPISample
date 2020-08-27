from fastapi import Depends, FastAPI
from api import api_router

app = FastAPI()
app.include_router(api_router)
