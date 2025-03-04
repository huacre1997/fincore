import asyncio
from time import sleep
from typing import Union
import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    res = {"Hello": "World"}
    await asyncio.sleep(3)
    print("paso el sleep")
    async with httpx.AsyncClient() as client:
        await asyncio.sleep(2)
        print("devolvio response")
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
    await asyncio.sleep(1)
    print("aea")
    demo = response.json()
    res.update(demo)
    return res


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
