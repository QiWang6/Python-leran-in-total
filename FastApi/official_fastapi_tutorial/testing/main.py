# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: main
# @Project: Python-leran-in-total
# @Quelle: https://fastapi.tiangolo.com/tutorial/testing/#fastapi-app-file

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


if __name__=='__main__':
    uvicorn.run("main:app", reload=True)