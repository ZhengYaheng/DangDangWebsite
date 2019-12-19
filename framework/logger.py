import logging
import time
import os


# 定义一个日志类，规定日志级别、日志存储路径
class Logger(object):

    # 通过Logging.Logger(日志器名称，日志器级别)实例化方法得到一个日志器对象
    def __init__(self, logger1):
        self.logger = logging.Logger(logger1)
        self.logger.setLevel(logging.DEBUG)
        # 日志存放的路径,os.path.abspath('.')当前目录的绝对路径，dirname()返回上一层目录
        log_path = os.path.dirname(os.getcwd()) + '/logs/'
        # 获取系统时间，得到一个字符串形式的时间
        current_period = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 由当前时间命名的.log日志文件名
        log_name = log_path + current_period + '.log'
        # 通过logging.FileHandler(生成的日志文件名称)
        # 创建一个名为fh的，输出到磁盘文件的处理器
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 创建一个格式器
        formatter = logging.Formatter("%(levelname)s %(asctime)s %(filename)s %(funcName)s %(message)s")
        # 给处理器fh指定输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 为logger添加处理器
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
