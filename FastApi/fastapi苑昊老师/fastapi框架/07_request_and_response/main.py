# @Time: 2024/10/14 
# @Author: Qi Wang
# @File: main
# @Project: Python-leran-in-total
# @Quelle:

from fastapi import FastAPI
import uvicorn
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app06 import app06
from apps.app07 import app07


app = FastAPI()


app.include_router(app01, tags=["01 Path Parameter"])
app.include_router(app02, tags=["02 Query Parameter"])
app.include_router(app03, tags=["03 Request Data"])
app.include_router(app06, tags=["06 Request对象"])
app.include_router(app07, tags=["07 Response Parameter"])


if __name__=='__main__':
    uvicorn.run("main:app", port=8000, reload=True)