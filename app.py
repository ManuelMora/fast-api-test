from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return { "Hello": "World"}

@app.get('/user/{user_id}')
async def read_user(user_id: int, q: Union[str, None] = None):
    return { "user_id": user_id, "q": q }

