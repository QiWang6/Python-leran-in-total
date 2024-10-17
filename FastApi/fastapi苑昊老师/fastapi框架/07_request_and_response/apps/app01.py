# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: app01
# @Project: Python-leran-in-total
# @Quelle:


from fastapi import APIRouter, Query

app01 = APIRouter()


# 路由匹配顺序


@app01.get("/user/{user_id}")  # 装饰器中的{user_id}
def get_user(user_id: int, QueryTest = Query(10, description="测试Query用法")):  # 这里需要有同名的位置变量
    print("user_id", user_id, type(user_id))
    return {
        "user_id": user_id,
        "Query_Test": QueryTest
    }


@app01.get("/user/1")
def get_user():
    return {
        "user_id": "root user"
    }


@app01.get("/articles/{article_name}")
def get_article(article_name):
    print("article_name", article_name, type(article_name))
    return {
        "article_name": article_name
    }
