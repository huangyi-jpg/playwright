

#接口自动化登录验证
def test_login_succes(auth_token):
    assert auth_token is not None
    assert len(auth_token) > 10