from fastapi import FastAPI

from app.database import engine, Model
from app.dependencies import get_db
from app.routers import speedsters

Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(speedsters.router)


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    print(get_db)
