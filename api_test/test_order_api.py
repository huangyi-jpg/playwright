import requests

ORDER_URL = "http://192.168.124.128:9091/order"
#发布商品断言
def test_create_order(base_headers,proder_paylod):

    requese = requests.post(ORDER_URL,json=proder_paylod,headers=base_headers)

    print(f"响应码：{requese.status_code}")
    print(f"相应文本：{requese.text}")

    assert requese.status_code == 200


