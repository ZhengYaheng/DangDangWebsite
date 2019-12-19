from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger
import time
from selenium import webdriver


logger = Logger(logger1="BasePage_logger").get_log()


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def find_element(self, selector):
        element = ''
        if "=>" not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        try:
            element = self.driver.find_element_by_xpath(selector_value)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            # logger.info("通过定位器%s的值%s找到元素%s" % (selector_by, selector_value, element.text))
        except NoSuchElementException as e:
            logger.error("抛出异常NoSuchElementException：%s" % e)
        return element

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            # logger.info("清除文本框成功")
        except NameError as e:
            logger.info("清除文本框失败:%s" % e)

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            # logger.info("已经输入内容：%s" % text)
        except NameError as e:
            logger.error("输入失败：%s" % e)

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        text = el.text
        self.sleep(5)
        try:
            el.click()
            # logger.info("点击%s元素" % text)
        except NameError as e:
            logger.info("点击元素失败：%s" % e)

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()
        # logger.info("退出浏览器")

    # 关闭当前浏览器窗口
    def close(self):
        try:
            self.driver.close()
            # logger.info("已关闭%s窗口")
        except NameError as e:
            logger.error("关闭窗口抛异常：%s" % e)

    # 等待网页反应
    def sleep(self, seconds):
        time.sleep(seconds)
        logger.info("等待%s秒钟" % seconds)

    # 打印句柄
    def handles_list(self):
        print(self.driver.window_handles)

    # 打印当前句柄
    def current_handle(self):
        print(self.driver.current_window_handle)

    # 切换句柄
    def handle(self, value):
        try:
            if isinstance(value, int):
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[value])
                print("切换句柄成功")
            elif isinstance(value, str):
                self.driver.switch_to.window(value)
            else:
                print(f"传入的type参数 {value} 错误，仅可传int、str")

        except:
            print(f"根据 {value} 获取句柄失败")

    # 查看cookie
    def list_cookie(self):
        cookies = self.driver.get_cookies()
        return cookies

    # 刷新网页
    def refresh(self):
        self.driver.refresh()

