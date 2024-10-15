# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: urls
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter  # APIRouter为接口路由对象

shop = APIRouter()


@shop.get("/food")
def shop_food():
    return {"shop": "food"}


@shop.get("/bed")
def shop_bed():
    return {"shop": "bed"}




