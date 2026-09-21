import pytest

@pytest.fixture
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
    }

@pytest.fixture
def test_login(page):
    page.goto("http://192.168.124.128:8091")
    page.get_by_role("link", name="登录").click()
    page.get_by_placeholder("请输入账号").fill("admin")
    page.get_by_placeholder("请输入密码").fill("wyn123456")
    page.get_by_role("button", name="登录").click()
    return page