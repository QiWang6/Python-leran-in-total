# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: main
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import FastAPI
import uvicorn
from apps.app01.urls import shop
from apps.app02.urls import user

app = FastAPI()


app.include_router(shop, prefix="/shop", tags=["ShoppingCenterAPI"])
app.include_router(user, prefix="/user", tags=["UserCenterAPI"])


if __name__=='__main__':
    uvicorn.run("main:app", port=8000, reload=True)