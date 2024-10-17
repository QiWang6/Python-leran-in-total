# @Time: 2024/10/16 
# @Author: Qi Wang
# @File: paginated_test1
# @Project: Python-leran-in-total
# @Quelle:
import uvicorn
from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# 模拟数据库中的数据
items = [{"name": f"Item {i}"} for i in range(100)]  # 模拟 100 条数据

@app.get("/items/", response_model=List[dict])
def get_items(limit: int = Query(11, description="每页返回的数量"),
              offset: int = Query(0, description="跳过的记录数量")):
    """
    获取分页的项目列表
    :param limit: 每页返回的记录数（默认为10）
    :param offset: 跳过的记录数（默认为0）
    :return: 分页的项目列表
    """
    return items[offset : offset + limit]


if __name__=='__main__':
    uvicorn.run("paginated_test1:app", reload=True)