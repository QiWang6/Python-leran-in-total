# @Time: 2024/10/8 
# @Author: Qi Wang
# @File: main
# @Project: Python-leran-in-total
# @Quelle: ChatGPT

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    return {
        "name": item.name,
        "price": item.price,
        "is_offer": item.is_offer
    }


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


# 模拟验证函数，从请求头中获取 Authorization
def fake_auth(authorization: str = Header(None)):
    if authorization != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/protected/")
def read_protected_data(token: str = Depends(fake_auth)):
    return {"message": "Protected data"}


if __name__=='__main__':
    uvicorn.run("main:app", reload=True)