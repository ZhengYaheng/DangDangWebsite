# 导入单元测试unittest模块
import unittest
# 下载python3可用的HTMLTestRunner.py文件存放到python的Lib目录后.
# 导入HTMLTestRunner输出报告模块
import HTMLTestRunner
# 导入所需测试类
from testsuits.buy_now import BuyNow
# 导入os模块，获取路径
import os
# 导入time模块, 获取系统时间
import time


# 设置测试报告保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统时间，以时间戳命名报告文件的名称
# strftime(format, t):把参数t也就是时间转化为指定格式format,不指定参数t则转化当前系统时间
report_time = time.strftime("%Y-%m-%d %H%M%S")
# 定制报告名称
report_file = report_path + report_time + 'HTMLtemplate.html'

fp = open(report_file, 'wb')

# 构建测试套件suite
suits = unittest.TestSuite()
# 把测试类加到测试套件中，方法addTest(测试类名('测试类中测试函数名'))
# 多个测试类测试方法，逐条加进测试套件中
suits.addTest(BuyNow('test_buy_now'))

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner模块里的HTMLTestRunner类的对象，用于生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="当当网测试报告", description="用例测试情况")
    # 执行测试套件
    runner.run(suits)



