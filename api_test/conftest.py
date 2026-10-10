import os
import pytest
import requests

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:9091")
SELL_URL_USER_LOGIN = f"{BASE_URL}/user/login"

@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "admin",
        "password": "wyn123456",
    }

    response = requests.post(SELL_URL_USER_LOGIN, json=payload, timeout=10)
    assert response.status_code == 200
    token = response.json()["data"]
    print(f"\n[Fixture]成功获取token：{token[:20]}...")
    return token

@pytest.fixture(scope="session")
def base_headers(auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}",
    }
    return headers

@pytest.fixture
def proder_paylod():
    return {
        "title": "国服摄影机",
        "content": "1111111111111111111111111",
        "price": 255000,
        "type": "goods",
        "picture": "3199a06d2f2b469e83296d2d146f2c7b.jpg",
    }
