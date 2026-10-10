import requests

RORDER_URL = "http://192.168.124.128:9091/cart/add/173"
LORDER_URL = "http://192.168.124.128:9091/cart/show"
ORDER_URL = "http://192.168.124.128:9091/cart/commitOrder/172/250"
#发布商品断言
def test_create_order(base_headers):
    #添加商品到购物车
    proders = {
    }
    requese = requests.post(RORDER_URL,json=proders,headers=base_headers)
    print(f"响应码：{requese.status_code}")
    print(f"相应文本：{requese.text}")

    #查询购物车内的商品
    requesed = requests.get(LORDER_URL,headers=base_headers)
    print(f"响应码：{requesed.status_code}")
    print(f"相应文本：{requesed.text}")
    assert requesed.status_code == 200

#提交订单
    proder = [{
        "shoppingId": 22,
        "orderId": 173,
        "title": "六号化合物",
        "content": "浣熊市土特产，里昂的最爱。。",
        "price": "250.00",
        "picture": "01812547bfde4551b092f8c82396ea07.png",
        "ownName": "admin",
        "count": 2,
        "selected": True
    }]
    requeses = requests.post(ORDER_URL,json=proder,headers=base_headers)
    print(f"响应码：{requeses.status_code}")
    print(f"相应文本：{requeses.text}")
    assert requeses.status_code == 200

