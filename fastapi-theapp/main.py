from fastapi import FastAPI
import models
from database import engine
from routers import item, user, auth #(Importing The Routers and authentication Router)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the authentication router
app.include_router(auth.router)

# Include the routers for items and users

app.include_router(item.router)
app.include_router(user.router)
