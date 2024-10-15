# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app04
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List, Union, Optional


app06 = APIRouter()


@app06.post("/items")
async def items(request: Request):
    print("URL:", request.url)
    print("客户端IP地址:", request.client.host)
    print("客户端宿主", request.headers.get("user-agent"))
    print("cookies", request.cookies.get("a"))

    return {
        "URL": request.url,
        "客户端IP地址:": request.client.host,
        "客户端宿主": request.headers.get("user-agent"),
        "cookies": request.cookies
    }
