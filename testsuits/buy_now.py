import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.homepage import HomePage
from pageobjects.item_list_page import ItemList
from pageobjects.item_details import ItemDetails
from pageobjects.check_out import CheckOut


class BuyNow(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()
        # browser = BrowserEngine(self)

    def test_buy_now(self):
        # 在当当网首页搜索儿童睡前故事
        homepage = HomePage(self.driver)
        homepage.type_search("儿童睡前故事")
        homepage.search_submit()
        # 在搜索结果中点击第一个商品
        item_list = ItemList(self.driver)
        # item_list.item_click()
        item_list.item_add()
        # 在商品详情页面
        # item_details = ItemDetails(self.driver)
        # 加入购物车
        # item_details.add_cart()
        # 点击立即购买
        # item_details.buy_now()
        # 在结算页面，点击去支付
        checkout = CheckOut(self.driver)
        checkout.pay()


if __name__ == '__main__':
    unittest.main()






