import uvicorn
from fastapi import FastAPI
from api.routes import helpers, trophies, users, lives, points, minutes, fastforwards, store_items
from api.Repositories.db import DataBase
app = FastAPI()
DataBase()

app.include_router(helpers.router)
app.include_router(trophies.router)
app.include_router(users.router)
app.include_router(lives.router)
app.include_router(points.router)
app.include_router(minutes.router)
app.include_router(fastforwards.router)
app.include_router(store_items.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")