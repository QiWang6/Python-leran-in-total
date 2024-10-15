# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: urls
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import APIRouter

user = APIRouter()


@user.post("/login")
def user_login():
    return {"user": "login"}


@user.post("/reg")
def user_reg():
    return {"user": "reg"}
