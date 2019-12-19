from framework.logger import Logger
import os
import configparser
from selenium import webdriver
import time


# 实例化一个日志器对象并调用类中方法get_log()得到一个日志器
logger = Logger(logger1='DangDang_logger').get_log()
# 封装一个浏览器类，主要是浏览器的打开、关闭,用的什么浏览器、打开哪个URL


class BrowserEngine(object):
    # 获取浏览器驱动文件路径
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    # 初始化浏览器对象
    def __init__(self, driver):
        self.driver = driver
    # 打开浏览器函数，从配置文件config.ini中选择所打开的浏览器，打开的网址

    def open_browser(self, driver):
        cookie = {u'name': u'USERNUM',
                  u'value': u'EUFlufcOrJ2AlzMZ9mKkbg==',
                  'path': '/',
                  'domain': '.dangdang.com',
                  'secure': False,
                  'expiry': None
                  }
        cookie1 = {u'name': u'__dd_token_id',
                   u'value': u'201912121210156493402330536495fd',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        cookie2 = {u'name': u'__rpm',
                   u'value': 'mix_317715...1576123670614|login_page.login_password_div..1576123812942',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        cookie3 = {u'name': u'__trace_id',
                   u'value': u'20191212121013079175840772874675702',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        cookie4 = {u'name': u'dangdang.com',
                   u'value': u'email=MTUyMTY4ODU5NzUxNDM5N0BkZG1vYmlscG'
                             u'hvbmVfX3VzZXIuY29t&nickname=&display_id=143083'
                             u'0613500&customerid=m/mMnYDEIDcN8zDRNc70Pw==&viptyp'
                             u'e=wwC8G9rNpAY=&show_name=152****5975',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        cookie5 = {u'name': u'ddoy',
                   u'value': u'email=1521688597514397@ddmobilphone__user.com&nickname=&agree_date=1&validate'
                             u'dflag=0&uname=15216885975&utype=1&.ALFG=on&.ALTM=1576123815',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        cookie6 = {u'name': u'login.dangdang.com',
                   u'value': u'.AYH=2019121212075412544201159&.ASPXAUTH=AS+9/+PpnSQOpelHkkj+b5'
                            u'cq8VZDacIHcC2EU+zBexnvOW8l0DozCQ==',
                   'path': '/',
                   'domain': '.dangdang.com',
                   'secure': False,
                   'expiry': None
                   }
        config = configparser.ConfigParser()
        # 配置文件的路径
        config_file = os.path.dirname(os.getcwd()) + '/config/config.ini'
        # read()方法是用来读取配置文件的
        config.read(config_file)

        browser = config.get('browserType', 'browserName')
        logger.info("You had select %s browser." % browser)
        url = config.get('testServer', 'URL')
        logger.info("The test server url is: %s" % url)

        # 打开配置文件config.ini中选择的浏览器及网页
        if browser == 'FireFox':
            driver = webdriver.Firefox()
            logger.info('打开火狐浏览器')
        elif browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('打开谷歌浏览器')
        else:
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info('打开ie浏览器')

        driver.get(url)
        logger.info('打开网页：%s' % url)
        driver.add_cookie(cookie)
        driver.add_cookie(cookie1)
        driver.add_cookie(cookie2)
        driver.add_cookie(cookie3)
        driver.add_cookie(cookie4)
        driver.add_cookie(cookie5)
        driver.add_cookie(cookie6)
        time.sleep(3)
        driver.refresh()
        driver.maximize_window()
        logger.info('网页最大化')
        driver.implicitly_wait(10)
        logger.info('等待10秒')
        return driver

    def quit_browser(self):
        logger.info('马上关闭浏览器')
        self.driver.quit()

