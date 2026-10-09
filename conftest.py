import pytest
import requests

sell_url = "http://192.168.124.128:9091"
SELL_URL_USER_LOGIN = f'{sell_url}/user/login'

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

@pytest.fixture(scope="session")
def base_headers(auth_token):
    headers = {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {auth_token}"
    }
    return headers


@pytest.fixture
def login(page):
    page.goto("http://192.168.124.128:8091")
    page.get_by_role("link", name="登录").click()
    page.get_by_placeholder("请输入账号").fill("admin")
    page.get_by_placeholder("请输入密码").fill("wyn123456")
    page.get_by_role("button", name="登录").click()
    return page