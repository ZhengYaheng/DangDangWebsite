from framework.base_page import BasePage


class ItemList(BasePage):
    item_selected = "xpath=>//*[@id='p24181370']/p[1]/a"
    item_add_cart = "xpath=>//div[@id='search_nature_rg']/ul/li[1]/div[@class='shop_button']/p/a[1]"

    def item_click(self):
        self.click(self.item_selected)
        self.handles_list()

    def item_add(self):
        # self.handles_list()
        # self.current_handle()
        self.click(self.item_add_cart)
        # self.handles_list()
        # self.current_handle()
        # 切换到第二个窗口句柄，handle(1)
        self.handle(1)

