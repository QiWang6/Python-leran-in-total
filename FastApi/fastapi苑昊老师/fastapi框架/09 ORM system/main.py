# @Time: 2024/10/15 
# @Author: Qi Wang
# @File: main
# @Project: Python-leran-in-total
# @Quelle:


from fastapi import FastAPI
import uvicorn


app = FastAPI()


if __name__=='__main__':
    uvicorn.run("main:app", port=8000, reload=True)