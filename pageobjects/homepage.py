from framework.base_page import BasePage


class HomePage(BasePage):
    input_box = 'key_S'
    search_submit_btn = "xpath=>//*[@id='form_search_new']/input[9]"
    # username_box =
    # password_box =

    def type_search(self, text):
        self.type(self.input_box, text)

    def search_submit(self):
        self.click(self.search_submit_btn)
        self.sleep(10)

    # def log_in(self):
