# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: 03 fastapi quickstart
# @Project: Python-leran-in-total
# @Quelle:


from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def home():
    return {"user_id": 1002}


@app.get("/shop")
async def shop():
    return {"shop": "商品信息"}


if __name__=='__main__':
    uvicorn.run("03_fastapi_quickstart:app", port=8000, reload=True)