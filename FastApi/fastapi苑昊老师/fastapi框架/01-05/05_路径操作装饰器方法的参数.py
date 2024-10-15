# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: 05_路径操作装饰器方法的参数
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.post("/items", tags=["这是一个items的测试接口"],
          summary="这是items的总结",
          description="这是item测试的描述",
          response_description="这是items测试的响应描述",
          deprecated=True)
def Test():
    return {"items": "items data"}


if __name__=='__main__':
    uvicorn.run("05_路径操作装饰器方法的参数:app", port=8000, reload=True)