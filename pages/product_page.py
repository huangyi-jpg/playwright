class ProductPage:
    def __init__(self,page):
        self.page = page

    def publish(self,img_path,name,passder,mrold):
        self.page.get_by_role("link", name="农产品交易").click()
        self.page.get_by_role("button", name="免费发布商品").click()
        self.page.locator("input[type='file']").set_input_files(img_path)
        self.page.get_by_placeholder("请输入商品标题").fill(name)
        self.page.get_by_placeholder("请输入商品详细介绍").fill(passder)
        self.page.get_by_label("定价").fill(mrold)
        self.page.get_by_role("button", name="发布").last.click()
        # page.screenshot(path="login_fail_debug.png", full_page=True)
        # assert (page.get_by

    def gouwu(self):
        self.page.get_by_text("苹果", exact=True).click()
        self.page.get_by_role("button", name="加入购物车").click()
        self.page.get_by_role("link", name="农产品交易").click()
        self.page.get_by_role("button", name="购物车").click()
        self.page.locator("div").filter(has_text="苹果").get_by_role("checkbox").first.click()
        self.page.get_by_role("button", name="结算").click()