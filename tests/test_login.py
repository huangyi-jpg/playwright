from pages.product_page import ProductPage
from playwright.sync_api import expect

def test_playwright_product(test_login):
    product = ProductPage(test_login)
    product.publish(
        img_path = "D:/playwright-demo/data/荷叶.jpg",
        name = "五号化合物",
        passder = "辉阿哥金克拉估计快了",
        mrold = "55152"
    )
    test_login.wait_for_load_state("networkidle")
    expect(test_login.get_by_text("融销通").first).to_be_visible()

def test_shangpin_dinggou(test_login):
    product = ProductPage(test_login)
    product.gouwu()
    expect(test_login.get_by_text("订单提交成功").first).to_be_visible()