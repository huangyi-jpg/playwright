from pages.product_page import ProductPage
from playwright.sync_api import expect

def test_playwright_product(login):
    product = ProductPage(login)
    product.publish(
        img_path = "D:/playwright-demo/data/云天.png",
        name = "六号化合物",
        passder = "浣熊市土特产，里昂的最爱。。",
        mrold = "250"
    )
    login.wait_for_load_state("networkidle")
    expect(login.get_by_text("融销通").first).to_be_visible()
    product.gouwu()
    expect(login.get_by_text("订单提交成功").first).to_be_visible()