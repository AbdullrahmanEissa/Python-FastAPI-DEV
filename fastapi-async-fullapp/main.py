from fastapi import FastAPI
from contextlib import asynccontextmanager
import models
from database import engine
from routers import items, users, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(items.router)
app.include_router(users.router)