from framework.base_page import BasePage


class ItemDetails(BasePage):
    add_cart_btn = "part_buy_button"
    buy_now_btn = "buy_now_button"
    # 弹出框中立即购买按钮定位pop_img = "xpath=>//div[@id='pc_bugnow_go']"
    pop_img = "xpath=>//div[@class='pc_daoliu_cloce_div']/img[@class='pc_daoliu_cloce_img']"

    def add_cart(self):
        self.handle(1)
        self.click(self.add_cart_btn)
        self.click(self.pop_img)
        self.click(self.add_cart_btn)
    #     self.sleep(20)
    #     try:
    #         self.click(self.pop_img)
    #     except:
    #         print("没有微信扫码下单窗口弹出")
    #     self.handles_list()
    #     self.handle(1)
    #     self.sleep(10)

    """
    def buy_now(self):
        # self.handle(1)
        # self.sleep(10)
        # try:
        #     self.handles(2)
        #     self.click(self.pop_img)
        # except:
        #     print("没有微信扫码下单窗口弹出")
        # self.sleep(10)
        self.handles_list()
        self.handle(1)
        self.click(self.buy_now_btn)
        print(self.list_cookie())
        self.click(self.pop_img)
        self.click(self.buy_now_btn)
        '''
        try:
            self.click(self.pop_img)
            print("点击弹出框中立即购买后"+self.list_cookie())
        except Exception as e:
            print("没有微信扫码下单窗口弹出%s" % e)
        '''
    """


