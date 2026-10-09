def test_login_succes(auth_token):
    assert auth_token is not None
    assert len(auth_token) > 10