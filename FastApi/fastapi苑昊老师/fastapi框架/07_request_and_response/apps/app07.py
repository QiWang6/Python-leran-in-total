# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app07
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Union, List


app07 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app07.post("/user02", response_model=UserOut)  # 输出模型里需要隐藏密码
def create_user(user: UserIn):
    print(user)
    return user


'''@app07.get("/items/{item_id}", response_model=Item, response_model_exclude_none=True)
async def read_item(item_id: str):
    return items[item_id]'''


@app07.get("/items/{item_id}", response_model=Item, response_model_include={"name", "price"})
async def read_item(item_id: str):
    return items[item_id]


@app07.get("/items2/{item_id}", response_model=Item, response_model_exclude={"tags"})
async def read_item(item_id: str):
    return items[item_id]

