import pytest
import requests

sell_url = "http://192.168.124.128:9091"
SELL_URL_USER_LOGIN = f'{sell_url}/user/login'
#接口登录，并获取请求头token
@pytest.fixture(scope="session")
def auth_token():
    url = SELL_URL_USER_LOGIN
    passed = {
        "username":"admin",
        "password":"wyn123456"
    }

    reposnts = requests.post(url, json=passed)
    assert reposnts.status_code == 200
    token = reposnts.json()["data"]
    print(f"\n[Fixture]成功获取token：{token[:20]}...")
    return token
#存储请求头
@pytest.fixture(scope="session")
def base_headers(auth_token):
    headers = {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {auth_token}"
    }
    return headers

#发布商品
@pytest.fixture
def proder_paylod():
    return {
        "title": "国服摄影机",
        "content": "1111111111111111111111111",
        "price": 255000,
        "type": "goods",
        "picture":"3199a06d2f2b469e83296d2d146f2c7b.jpg"
    }
