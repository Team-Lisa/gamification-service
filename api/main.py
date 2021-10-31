import uvicorn
from fastapi import FastAPI
from api.routes import helpers, trophies
from api.Repositories.db import DataBase
app = FastAPI()
DataBase()

app.include_router(helpers.router)
app.include_router(trophies.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")