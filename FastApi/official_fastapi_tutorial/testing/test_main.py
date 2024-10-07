# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: test_main
# @Project: Python-leran-in-total
# @Quelle: https://fastapi.tiangolo.com/tutorial/testing/#fastapi-app-file


from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
