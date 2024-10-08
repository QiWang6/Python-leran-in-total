# @Time: 2024/10/8 
# @Author: Qi Wang
# @File: test_main
# @Project: Python-leran-in-total
# @Quelle: ChatGPT

from fastapi.testclient import TestClient
from .main import app  # 假设你的 FastAPI 应用在 main.py 文件中。注意这里要在main之前加一个"."

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}


def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Test Item", "price": 25.5, "is_offer": True}
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test Item",
        "price": 25.5,
        "is_offer": True
    }


def test_read_items():
    response = client.get("/items/", params={"skip": 5, "limit": 20})
    assert response.status_code == 200
    assert response.json() == {"skip": 5, "limit": 20}


def test_protected_data():
    # 传递正确的 token
    response = client.get("/protected/", headers={"Authorization": "valid-token"})
    assert response.status_code == 200
    assert response.json() == {"message": "Protected data"}

    # 传递错误的 token
    response = client.get("/protected/", headers={"Authorization": "invalid-token"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}

    # 不传递 token
    response = client.get("/protected/")
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}



