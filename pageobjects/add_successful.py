from framework.base_page import BasePage


class AddSuccessful(BasePage):
    go_cart = "xpath=>//*[@id='add_more']/div[2]/p/a[1]"

    def goto_cart(self):
        self.click(self.go_cart)
