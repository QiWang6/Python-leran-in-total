# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app03
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Union, Optional


app03 = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    name: str
    age: int = Field(default=0, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Addr


    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value


class Data(BaseModel):
    data: List[User]


@app03.post("/user")
async def user(user: User):
    print(user, type(user))
    print(user.name, user.birth)
    print(user.dict())
    return user


@app03.post("/data")
async def data(data: Data):
    return data