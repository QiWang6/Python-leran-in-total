# @Time: 2024/10/16 
# @Author: Qi Wang
# @File: paginated_test3
# @Project: Python-leran-in-total
# @Quelle:


from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Item

app = FastAPI()


# 依赖项：创建数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/")
def get_items(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    # 使用 SQLAlchemy 查询数据库，分页获取数据
    items = db.query(Item).offset(offset).limit(limit).all()
    total = db.query(Item).count()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "data": items
    }

