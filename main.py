from fastapi import FastAPI
from views import user_router


app = FastAPI()


@app.get("/ping")
def pong():
    return {"message": "pong for user api"}


app.include_router(user_router)
