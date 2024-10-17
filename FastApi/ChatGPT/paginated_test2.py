# @Time: 2024/10/16 
# @Author: Qi Wang
# @File: paginated_test2
# @Project: Python-leran-in-total
# @Quelle:

import uvicorn
from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

items = [{"name": f"Item {i}"} for i in range(100)]


@app.get("/items/")
def get_items(limit: int = Query(10), offset: int = Query(10)):
    total = len(items)
    data = items[offset: offset + limit]

    return {
        "total": total,  # 总记录数
        "limit": limit,  # 每页返回条数
        "offset": offset,  # 当前的偏移量
        "data": data  # 实际返回的数据
    }


if __name__=='__main__':
    uvicorn.run("paginated_test2:app", reload=True)