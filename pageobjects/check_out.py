from framework.base_page import BasePage


class CheckOut(BasePage):
    pay_btn = "checkout_btn"

    def pay(self):
        # self.refresh()
        self.click(self.pay_btn)
